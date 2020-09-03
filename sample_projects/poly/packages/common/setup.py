import pathlib

import setuptools


def _read_requirements():
    with open("requirements/install_requires.txt") as f:
        return list(f)


setuptools.setup(
    name="common",
    version="0.2.5",
    install_requires=_read_requirements(),
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    classifiers=["Private :: Do not upload to PyPI"],
)
