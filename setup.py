import os

import setuptools

with open(
        os.path.join(os.path.dirname(__file__), "requirements", "install_requires.txt")
) as fp:
    install_requires = list(fp)

with open(os.path.join(os.path.dirname(__file__), "README.md"), "r") as fp:
    long_description = fp.read()

setuptools.setup(
    name="tox-constraints",
    version="0.5.2.dev",
    author="AP Ljungquist",
    author_email="ap@ljungquist.eu",
    url="https://github.com/apljungquist/tox-constraints",
    description="Reproducible tests, by default.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=install_requires,
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    entry_points={"tox": ["constraints = tox_constraints.hooks"]},
    classifiers=["License :: OSI Approved :: MIT License"]
)
