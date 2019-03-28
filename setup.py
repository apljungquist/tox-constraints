import setuptools

setuptools.setup(
    name="tox-constraints",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
)
