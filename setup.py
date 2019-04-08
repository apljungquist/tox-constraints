import setuptools


with open("requirements/install_requires.txt") as fp:
    install_requires = list(fp)

setuptools.setup(
    name="tox-constraints",
    version="0.5.2.dev",
    install_requires=install_requires,
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    entry_points={"tox": ["constraints = tox_constraints.hooks"]},
)
