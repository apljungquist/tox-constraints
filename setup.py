import os

import setuptools


def read_requirements(name):
    with open(
        os.path.join(os.path.dirname(__file__), "requirements", name + ".txt")
    ) as f:
        return list(f)


def read_install_requires():
    return read_requirements("install_requires")


with open(os.path.join(os.path.dirname(__file__), "README.md"), "r") as f:
    long_description = f.read()

setuptools.setup(
    name="tox-constraints",
    author="AP Ljungquist",
    author_email="ap@ljungquist.eu",
    url="https://github.com/apljungquist/tox-constraints",
    description="Reproducible tests, by default.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=read_install_requires(),
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    entry_points={
        "tox": ["constraints = tox_constraints.hooks"],
    },
    classifiers=["License :: OSI Approved :: MIT License"],
)
