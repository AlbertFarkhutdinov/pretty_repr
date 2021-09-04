"""
This module is used for checking the project code for compliance with PEP8.

"""


from pylint_af import PyLinter


if __name__ == '__main__':
    PyLinter(
        is_printed=False,
        ignored_statements={
            'E0401', 'E0402',
            'C0115', 'C0116',
            'W0201', 'R0903',
        },
    ).check()
