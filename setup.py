import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = ["pylint==2.9.3", "pytest==6.2.4"]

setuptools.setup(
    name="pretty_repr",
    version="0.0.1",
    author="Albert Farkhutdinov",
    author_email="albertfarhutdinov@gmail.com",
    description=(
        "The package that allows you to create clear and informative methods "
        "for your own classes in Python."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlbertFarkhutdinov/pretty_repr",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)