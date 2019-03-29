"""A simple package that works in some versions and is broken in others"""

import setuptools


def tweet():
    print("Tweet, tweet!")


def croak():
    print("Croak")
    raise RuntimeError


actions = {
    "1.0.1": croak,
    "1.1": tweet,
    "1.1.1": croak,
}

version = "1.1"

setuptools.setup(
    name="tox-constraints-canary",
    version=version,
)

actions[version]()
