"""A simple package that works in some versions and is broken in others"""

import setuptools

from canary import VERSION

setuptools.setup(
    name="tox-constraints-canary",
    version=VERSION,
    py_modules=["canary"],
    entry_points={
        "console_scripts": ["canary = canary:main"],
    },
)
