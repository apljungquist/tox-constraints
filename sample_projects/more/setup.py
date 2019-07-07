import pathlib

import setuptools


def _read_requirements(prefix, postfix=None):
    dirpath = pathlib.Path("requirements")
    if prefix == "install":
        filepath = dirpath / "install_requires.txt"
    elif prefix == "extras":
        filepath = dirpath / f"extras_require-{postfix}.txt"
    else:
        raise ValueError

    with filepath.open() as f:
        return list(f)


setuptools.setup(
    name="more",
    version="0",
    install_requires=_read_requirements("install"),
    extras_require={"more": _read_requirements("extras", "more")},
    classifiers=["Private :: Do not upload to PyPI"],
)
