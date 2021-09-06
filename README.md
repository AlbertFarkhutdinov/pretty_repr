# pretty_repr

![GitHub repo size](https://img.shields.io/github/issues/AlbertFarkhutdinov/pretty_repr)
![PyPI version](https://img.shields.io/pypi/v/pretty-repr)
![GitHub contributors](https://img.shields.io/github/contributors/AlbertFarkhutdinov/pretty_repr)
![GitHub stars](https://img.shields.io/github/stars/AlbertFarkhutdinov/pretty_repr)
![GitHub forks](https://img.shields.io/github/forks/AlbertFarkhutdinov/pretty_repr)
![GitHub licence](https://img.shields.io/github/license/AlbertFarkhutdinov/pretty_repr)

`pretty_repr` is a package that allows you to create clear and informative methods for your own classes in Python.

## Prerequisites

Before you begin, ensure you have installed the latest version of Python.

## Installing `pretty_repr`

To install `pretty_repr`, follow these steps:

Linux and macOS:
```
pip3 install pretty-repr
```

Windows:
```
pip install pretty-repr
```
## Using `pretty_repr`

There are will be examples of how to use `pretty_repr`.

### `get_representation`

1. The `get_representation` function requires an instance of some class 
as parameter and returns its string representation:

```
>>> from pretty_repr import get_representation
>>> class A:
...     def __init__(self, a, b, c, d=0):
...         self.a = a
...         self.__b = b
...         self._c = c
...         self.d = d
...
>>> example_1 = A(1, 2, 3)
>>> print(get_representation(example_1))
A(a=1, b=2, _c=3, d=0)
```

2. Run the following to exclude some parameters from the representation:

```
>>> print(get_representation(example_1, excluded={'a', '_c'}))
A(b=2, d=0)
```

3. If a parameter is iterable is represented as tuple by default:
```
>>> import numpy as np
>>> example_2 = A((1, 2), [3, 4], {5, 6}, np.zeros(3))
>>> print(get_representation(example_2))
A(a=(1, 2), b=(3, 4), _c=(5, 6), d=(0.0, 0.0, 0.0))
```

4. Run the following to change this behaviour:
```
>>> print(get_representation(example_2, is_only_tuples=False))
A(a=(1, 2), b=[3, 4], _c={5, 6}, d=array([0., 0., 0.]))
```

5. Inheritor representation includes all parameters of the ancestor 
as well as its own parameters:

```
>>> from pretty_repr import get_representation
>>> class B(A):
...     def __init__(self, e, f, h=1, **kwargs):
...         super().__init__(**kwargs)
...         self.e = e
...         self.__f = f
...         self.h = h
...
>>> example_3 = B(a=1, b=2, c=3, e=4, f=5)
>>> print(get_representation(example_3))
B(a=1, b=2, _c=3, d=0, e=4, f=5, h=1)
```

6. This representation includes private attributes of the ancestor.
Run the following to exclude it from representation:
```
>>> example_3._A__b
2
>>> print(get_representation(example_3, ancestor_private_attributes=False))
B(a=1, _c=3, d=0, e=4, f=5, h=1)
```

### `RepresentableObject`

The `RepresentableObject` class is the class which `__repr__` method returns 
`get_representation` function result:

```
>>> from pretty_repr import RepresentableObject
>>> print(get_representation(RepresentableObject()))
RepresentableObject()
>>> print(repr(RepresentableObject()))
RepresentableObject()
```

You can use class inherited from `RepresentableObject` 
instead of `__repr__` method implementation:

```
>>> class C(RepresentableObject):
...     def __init__(self, a, b, c, d=0):
...         self.a = a
...         self.__b = b
...         self._c = c
...         self.d = d
...
>>> example_1 = C(1, 2, 3)
>>> example_1
C(a=1, b=2, _c=3, d=0)

```

Define property `excluded_attributes_for_repr` 
to exclude some parameters from representation:

```
>>> class D(C):
...     def __init__(self, e, f, h=1, **kwargs):
...         super().__init__(**kwargs)
...         self.e = e
...         self.__f = f
...         self.h = h
...     @property
...     def excluded_attributes_for_repr(self):
...         return {'f', 'h'}
... 
>>> example_4 = D(a=1, b=2, c=3, e=4, f=5)
>>> example_4
D(a=1, b=2, _c=3, d=0, e=4)
```

## Contributing to `pretty_repr`
To contribute to `pretty_repr`, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contributors

* [@AlbertFarkhutdinov](https://github.com/AlbertFarkhutdinov) 

## Contact

If you want to contact me you can reach me at `albertfarhutdinov@gmail.com`.

## License
This project uses the following license: [MIT License](https://github.com/AlbertFarkhutdinov/pretty_repr/blob/main/LICENSE).