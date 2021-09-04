"""This module contain test for `pretty_repr` project."""


from .main import get_representation, RepresentableObject


class Parent(RepresentableObject):
    def __init__(self, attr_1, attr_2, default_1=1):
        """Initialize self. See help(type(self)) for accurate signature."""
        self.attr_1 = attr_1
        self.attr_2 = attr_2
        self.default_1 = default_1

    @property
    def attr_2(self):
        return self.__attr_2

    @attr_2.setter
    def attr_2(self, attr_2):
        self.__attr_2 = attr_2


class Child(Parent):
    def __init__(self, attr_3, attr_4, default_2=2, **kwargs):
        """Initialize self. See help(type(self)) for accurate signature."""
        super().__init__(**kwargs)
        self.attr_3 = attr_3
        self.attr_4 = attr_4
        self.default_2 = default_2

    @property
    def attr_4(self):
        return self.__attr_4

    @attr_4.setter
    def attr_4(self, attr_4):
        self.__attr_4 = attr_4


class GrandChild(Child):
    def __init__(self, attr_5, attr_6, default_3=3, **kwargs):
        """Initialize self. See help(type(self)) for accurate signature."""
        super().__init__(**kwargs)
        self.attr_5 = attr_5
        self.attr_6 = attr_6
        self.default_3 = default_3

    @property
    def attr_6(self):
        return self.__attr_6

    @attr_6.setter
    def attr_6(self, attr_6):
        self.__attr_6 = attr_6


class GrandChildExcluded(GrandChild):

    @property
    def excluded_attributes_for_repr(self):
        """Return attributes that are not shown in instance representation."""
        return {'attr_1', 'attr_4', 'attr_6'}


class ClassWithIterableAttributes(RepresentableObject):

    def __init__(self, attr_1, attr_2, attr_3):
        """Initialize self. See help(type(self)) for accurate signature."""
        self.attr_1 = attr_1
        self.attr_2 = attr_2
        self.attr_3 = attr_3


class TestPrettyRepr:

    def setup(self):
        self.parent = Parent(attr_1=1, attr_2=2)
        self.child = Child(attr_1=1, attr_2=2, attr_3=3, attr_4=4, default_1=2)
        _kwargs = {
            'attr_1': 1,
            'attr_2': 2,
            'attr_3': 3,
            'attr_4': 4,
            'attr_5': 5,
            'attr_6': 6,
        }
        self.grand_child = GrandChild(**_kwargs)
        self.grand_child_excluded = GrandChildExcluded(**_kwargs)
        self.class_with_iterable_attributes = ClassWithIterableAttributes(
            attr_1=(1, 2, 3),
            attr_2=[4, 5, 6],
            attr_3={1: 2, 3: 4, 5: 6}.items()
        )

    def test_parent(self):
        _exp = 'Parent(attr_1=1, attr_2=2, default_1=1)'
        _got = get_representation(self.parent)
        assert _got == _exp

    def test_child(self):
        _exp = (
            'Child(attr_1=1, attr_2=2, default_1=2, '
            'attr_3=3, attr_4=4, default_2=2)'
        )
        _got = get_representation(self.child)
        assert _got == _exp

    def test_grand_child(self):
        _exp = (
            'GrandChild(attr_1=1, attr_2=2, default_1=1, '
            'attr_3=3, attr_4=4, default_2=2, attr_5=5, attr_6=6, default_3=3)'
        )
        _got = get_representation(self.grand_child)
        assert _got == _exp

    def test_grand_child_with_excluded(self):
        _exp = (
            'GrandChild(attr_2=2, default_1=1, '
            'attr_3=3, default_2=2, attr_5=5, default_3=3)'
        )
        _got = get_representation(
            self.grand_child,
            excluded={'attr_1', 'attr_4', 'attr_6'}
        )
        assert _got == _exp

    def test_parent_without_base_arguments(self):
        _exp = 'Parent(attr_1=1, attr_2=2, default_1=1)'
        _got = get_representation(
            self.parent,
            ancestor_private_attributes=False,
        )
        assert _got == _exp

    def test_child_without_base_arguments(self):
        _exp = 'Child(attr_1=1, default_1=2, attr_3=3, attr_4=4, default_2=2)'
        _got = get_representation(
            self.child,
            ancestor_private_attributes=False,
        )
        assert _got == _exp

    def test_grand_child_without_base_arguments(self):
        _exp = (
            'GrandChild(attr_1=1, default_1=1, attr_3=3, '
            'default_2=2, attr_5=5, attr_6=6, default_3=3)'
        )
        _got = get_representation(
            self.grand_child,
            ancestor_private_attributes=False,
        )
        assert _got == _exp

    def test_parent_repr(self):
        _exp = 'Parent(attr_1=1, attr_2=2, default_1=1)'
        assert repr(self.parent) == _exp

    def test_child_repr(self):
        _exp = (
            'Child(attr_1=1, attr_2=2, default_1=2, '
            'attr_3=3, attr_4=4, default_2=2)'
        )
        assert repr(self.child) == _exp

    def test_grand_child_repr(self):
        _exp = (
            'GrandChild(attr_1=1, attr_2=2, default_1=1, '
            'attr_3=3, attr_4=4, default_2=2, attr_5=5, attr_6=6, default_3=3)'
        )
        assert repr(self.grand_child) == _exp

    def test_grand_child_repr_with_excluded(self):
        _exp = (
            'GrandChildExcluded(attr_2=2, default_1=1, '
            'attr_3=3, default_2=2, attr_5=5, default_3=3)'
        )
        _got = repr(self.grand_child_excluded)
        assert _got == _exp

    def test_class_with_iterable_attributes(self):
        _exp = (
            'ClassWithIterableAttributes(attr_1=(1, 2, 3), attr_2=[4, 5, 6], '
            'attr_3=dict_items([(1, 2), (3, 4), (5, 6)]))'
        )
        _got = get_representation(
            self.class_with_iterable_attributes,
            is_only_tuples=False,
        )
        assert _got == _exp

    def test_class_with_iterable_attributes_as_tuples(self):
        _exp = (
            'ClassWithIterableAttributes(attr_1=(1, 2, 3), attr_2=(4, 5, 6), '
            'attr_3=((1, 2), (3, 4), (5, 6)))'
        )
        _got = repr(self.class_with_iterable_attributes)
        assert _got == _exp
