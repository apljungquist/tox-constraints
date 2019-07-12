#!/usr/bin/env python3
import logging
import pathlib
import subprocess

import jinja2

logger = logging.getLogger(__name__)

SETUP_TEMPLATE = """\
import setuptools
{%- if not good %}
import sys

if sys.argv[1] != "sdist":
    print("Croak!")
    exit(1)
{%- endif %}

setuptools.setup(
    name="{{ canonical_name }}",
    version="{{ version }}",
    url="https://github.com/apljungquist/tox-constraints",
    license="MIT",
    author="AP Ljungquist",
    author_email="ap@ljungquist.eu",
    description="{{ description }}",
    classifiers=["License :: OSI Approved :: MIT License"],
    py_modules=["{{ canonical_name }}"],
    entry_points={
        "console_scripts": ["{{ canonical_name }} = {{ canonical_name }}:main"],
    },
)

"""

CANARY_TEMPLATE = """\
def main():
    print("Tweet Tweet!")

"""

README_TEMPLATE = """\
# {{ stylized_name }} 

*{{ description }}*

"""

GOOD = True
BAD = False


def breed_one(src, version, good, color):
    stylized_name = f"Canaria Domestica {color}"
    canonical_name = stylized_name.replace(" ", "_").lower()
    description = "A simple package that works in some versions and is broken in others"

    with (src / "setup.py").open("w") as f:
        f.write(jinja2.Template(SETUP_TEMPLATE).render(**locals()))

    with (src / f"{canonical_name}.py").open("w") as f:
        f.write(jinja2.Template(CANARY_TEMPLATE).render(**locals()))

    with (src / "README.md").open("w") as f:
        f.write(jinja2.Template(README_TEMPLATE).render(**locals()))

    subprocess.check_output(["python", "setup.py", "sdist"], cwd=src)


def breed_all(src):
    if not isinstance(src, pathlib.Path):
        src = pathlib.Path(src)

    if not src.exists():
        src.mkdir()

    colors = ["Red Black", "Red"]
    versions = {"1.0.0": BAD, "1.0.1": GOOD, "1.0.2": BAD}
    for color in colors:
        logger.info("Creating packages for %s", color)
        for version, good in versions.items():
            logger.info(
                "Creating %s package for version %s", "good" if good else "bad", version
            )
            breed_one(src, version, good, color)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    import fire

    fire.Fire()
