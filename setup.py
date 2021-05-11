import os

import setuptools


def read_requirements(name):
    with open(
        os.path.join(os.path.dirname(__file__), "requirements", name + ".txt")
    ) as fp:
        return list(fp)


def read_install_requires():
    return read_requirements("install_requires")


def read_extras_reqire(name):
    return read_requirements("extras_require-" + name)


with open(os.path.join(os.path.dirname(__file__), "README.md"), "r") as fp:
    long_description = fp.read()

setuptools.setup(
    name="tox-constraints",
    version="0.13",
    author="AP Ljungquist",
    author_email="ap@ljungquist.eu",
    url="https://github.com/apljungquist/tox-constraints",
    description="Reproducible tests, by default.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=read_install_requires(),
    extras_require={name: read_extras_reqire(name) for name in ["recutter"]},
    include_package_data=True,
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    entry_points={
        "tox": ["constraints = tox_constraints.hooks"],
        "console_scripts": [
            "toxc-recut=tox_constraints.recutter:main",
            "toxc-install=tox_constraints.git_filter:install",
            "toxc-clean=tox_constraints.git_filter:clean",
            "toxc-smudge=tox_constraints.git_filter:smudge",
        ],
    },
    classifiers=["License :: OSI Approved :: MIT License"],
)
