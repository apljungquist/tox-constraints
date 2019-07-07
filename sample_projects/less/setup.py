import pathlib

import setuptools


def _read_requirements():
    dirpath = pathlib.Path("requirements")
    filepath = dirpath / "install_requires.txt"

    with filepath.open() as f:
        return list(f)


setuptools.setup(
    name="more",
    version="0",
    install_requires=_read_requirements(),
    classifiers=["Private :: Do not upload to PyPI"],
)
