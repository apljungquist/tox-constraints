import setuptools

setuptools.setup(
    name="tox-constraints",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    install_requires=["tox"],
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    entry_points={"tox": ["constraints = tox_constraints"]},
)
