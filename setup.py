import setuptools

with open("requirements/install_requires.txt") as fp:
    install_requires = list(fp)

setuptools.setup(
    name="tox-constraints",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    install_requires=install_requires,
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    entry_points={"tox": ["constraints = tox_constraints.hooks"]},
)
