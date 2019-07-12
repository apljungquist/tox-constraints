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
    name="coalmine",
    version="0",
    install_requires=_read_requirements("install"),
    extras_require={"melanin": _read_requirements("extras", "melanin")},
    classifiers=["Private :: Do not upload to PyPI"],
)
