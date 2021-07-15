"""
This module is used for checking the project code for compliance with PEP8.

"""


from typing import List, Optional
import os

import pylint.lint


def get_inspected_files(
        pylint_dir: str,
        ignored: List[str],
) -> List[str]:
    """
    Return list of files checking for compliance with PEP8.

    Parameters
    ----------
    pylint_dir : str
        Root directory of checking.
    ignored : list
        List of paths that are ignored by checking.

    Returns
    -------
    list
        List of files checking for compliance with PEP8.

    """
    new_options = []
    for dir_name, _, files in os.walk(pylint_dir):
        is_ignored = False
        for path in ignored:
            if dir_name.startswith(path):
                is_ignored = True
                break
        if is_ignored:
            continue
        for file in files:
            if dir_name not in ignored and file.endswith('.py'):
                new_options.append(os.path.join(pylint_dir, file))
    return new_options


def get_pylint_options(
        is_documentation_ignored: bool,
        is_relative_import_ignored: bool,
        is_printed: bool,
        ignored_paths: Optional[set] = None,
) -> List[str]:
    """
    Return pylint options.

    Parameters
    ----------
    is_documentation_ignored : bool
        If it is True, checking for statements
        on missed docstrings (C0114, C0115, C0116) is ignored.
    is_relative_import_ignored : bool
        If it is True, checking for statements E0402 is ignored.
    is_printed : bool
        If it is True, pylint options are printed.
    ignored_paths : set, optional
        Set of paths that are ignored by checking.

    Returns
    -------
    list
        Pylint options.

    """
    pylint_options = ['--ignore-imports=yes']
    _ignored_paths = ignored_paths or set()
    _ignored_paths.update(
        {'venv', 'env', '.idea', '.pytest_cache'}
    )
    if is_documentation_ignored:
        pylint_options += [
            '--disable=C0114',
            '--disable=C0115',
            '--disable=C0116',
        ]
    if is_relative_import_ignored:
        pylint_options += [
            '--disable=E0402',
        ]
    pylint_dir = os.path.dirname(__file__)
    pylint_options += get_inspected_files(
        pylint_dir=pylint_dir,
        ignored=[os.path.join(pylint_dir, path) for path in _ignored_paths],
    )
    if is_printed:
        print(*pylint_options, sep='\n')
    return pylint_options


if __name__ == '__main__':
    PYLINT_OPTIONS = get_pylint_options(
        is_documentation_ignored=False,
        is_relative_import_ignored=False,
        is_printed=False,
    )
    pylint.lint.Run(PYLINT_OPTIONS)
