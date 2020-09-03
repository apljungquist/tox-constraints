import setuptools


def _read_requirements():
    with open("requirements/install_requires.txt") as f:
        return list(f)


setuptools.setup(
    name="optional",
    version="0.1.1",
    install_requires=_read_requirements(),
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    classifiers=["Private :: Do not upload to PyPI"],
)
