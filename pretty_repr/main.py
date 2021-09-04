"""
This module contains description of the function
that allows to initialize custom classes with clear
and informative `repr` method and base class with such method.

"""


from typing import Any, Iterable, Optional, Set


def remove_private_prefix(attr_name: str, prefix: str) -> str:
    """Return the specified attribute name without the specified prefix."""
    return attr_name[len(prefix):]


def get_representation(
        instance: Any,
        excluded: Optional[Set[str]] = None,
        ancestor_private_attributes: bool = True,
        is_only_tuples: bool = True,
) -> str:
    """
    Return the 'official' string representation of the specified instance.

    Parameters
    ----------
    instance : Any
        The instance, which string representation is returned.
    excluded : set, optional
        Names of arguments that are excluded
        from the representation.
    ancestor_private_attributes : bool, optional, default: True
        Private attributes of ancestor classes without '__' prefix
        are included into string representation, if this parameter is True,
        and are skipped if it is False.
    is_only_tuples : bool, optional, default: True
        Iterable attributes are represented as tuples,
        if this parameter is True.

    Returns
    -------
    str
        The 'official' string representation of the specified instance.

    """
    _class_name = instance.__class__.__name__
    representation = [f'{_class_name}(']
    for _key, _value in instance.__dict__.items():
        _key_repr, _value_repr = _key, _value
        _ancestor = instance.__class__.__bases__[0]
        while _ancestor.__name__ != 'object':
            _prefix = f'_{_ancestor.__name__}__'
            if _key.startswith(_prefix):
                if ancestor_private_attributes:
                    _key_repr = remove_private_prefix(_key, prefix=_prefix)
                else:
                    _key_repr = ''
            _ancestor = _ancestor.__bases__[0]
        if _key_repr == '':
            continue
        _prefix = f'_{_class_name}__'
        if _key.startswith(_prefix):
            _key_repr = remove_private_prefix(_key, prefix=_prefix)
        if excluded and _key_repr in excluded:
            continue
        if is_only_tuples and isinstance(_value, Iterable):
            _value_repr = tuple(_value)
        representation.append(f'{_key_repr}={_value_repr!r}')
        representation.append(', ')
    if len(representation) > 1:
        representation.pop()
    representation.append(')')

    return ''.join(representation)


class RepresentableObject:
    """Class with custom representation."""

    def __repr__(self) -> str:
        """Return the 'official' string representation of instance."""
        return get_representation(
            self,
            ancestor_private_attributes=True,
            is_only_tuples=True,
            excluded=self.excluded_attributes_for_repr
        )

    def __str__(self) -> str:
        """Return the nicely printable string representation of instance."""
        return repr(self)

    @property
    def excluded_attributes_for_repr(self) -> Set[str]:
        """Return attributes that are not shown in instance representation."""
        return set()
