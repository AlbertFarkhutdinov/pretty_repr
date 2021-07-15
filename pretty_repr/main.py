"""
This module contains description of the function
that allows to initialize custom classes with clear
and informative `repr` method and base class with such method.

"""


from typing import Any, Iterable, Optional, Set


def get_representation(
        instance: Any,
        excluded: Optional[Set[str]] = None,
        is_base_included: bool = True,
) -> str:
    """
    Return the 'official' string representation of `instance`.

    Parameters
    ----------
    instance : Any
        The instance, which representation is returned.
    excluded : set, optional
        Names of arguments that are excluded
        from the representation.
    is_base_included : bool, optional, default: True
        If it is True, arguments of base class are included.

    Returns
    -------
    str
        The 'official' string representation of `instance`.

    """
    _class_name = instance.__class__.__name__
    representation = [
        f'{_class_name}(',
    ]
    for _key, _value in instance.__dict__.items():
        _key_repr, _value_repr = _key, _value
        if is_base_included:
            _parent_class = instance.__class__.__bases__[0]
            while _parent_class.__name__ != 'object':
                if _key.startswith(f'_{_parent_class.__name__}__'):
                    _key_repr = _key[3 + len(_parent_class.__name__):]
                    break
                _parent_class = _parent_class.__bases__[0]
        if _key.startswith(f'_{_class_name}__'):
            _key_repr = _key[3 + len(_class_name):]
        if excluded and _key_repr in excluded:
            continue
        if isinstance(_value, Iterable):
            _value_repr = tuple(_value)
        representation.append(f'{_key_repr}={_value_repr!r}')
        representation.append(', ')
    if len(representation) > 1:
        representation.pop()
    representation.append(')')

    return ''.join(representation)


class RepresentableObject:
    """
    Class with custom representation.

    """

    def __repr__(self) -> str:
        """Return the 'official' string representation of instance."""
        return get_representation(
            self,
            is_base_included=True,
            excluded=self.excluded_attributes_for_repr
        )

    def __str__(self) -> str:
        """Return the nicely printable string representation of instance."""
        return repr(self)

    @property
    def excluded_attributes_for_repr(self) -> Set[str]:
        """Return attributes that are not shown in instance representation."""
        return set()
