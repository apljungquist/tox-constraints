# tox-constraints

*Reproducible tests, with minimal configuration, by default*

## Benefits
This plugin is helpful in the following ways
* Consolidates knowledge, so you do not have to make the mistakes I made.
* Makes reproducibility opt-out per environment (as opposed to opt-in).
* Forces `virtualenv` to install the package versions you want.
* Facilitates gathering of dependencies.

## Motivation
The best way to improve reproducibility of tox *without* this plugin is to set PIP_CONSTRAINT using either
1. `setenv`, or 
2. `passenv`.

This is good, it ensures that dependencies from all of these sources will be pinned:
* build system requires from pyproject.toml ([This would not be true when using `-c` flag](https://github.com/pypa/pip/issues/8439))
* install requires from `setup.py`
* extras requite from `setup.py`
* deps from `tox.ini`

This of course assumes that all direct and transient dependencies are listed in the constraints file.
`pip-compile` is a great tool to help both resolve all transient dependencies and assign a consistent set of versions.
What it cannot do is read the `tox.ini` file.

(Omitting rant about `pip`s broken hash checking mode)

It does however have one surprising behavior; the versions of pip, setuptools and wheel may not match what the constraints file says.
This is because `virtualenv` when creating an environment seeds the environment with some version of these packages.
By default, it uses a version that was bundled with the `virtualenv`, so while it may be surprising it should be reproducible.
This issue can be mitigated by using `setenv` or `passenv` to set
* `VIRTUALENV_PIP`,
* `VIRTUALENV_SETUPTOOLS`, and
* `VIRTUALENV_WHEEL`.

(Omitting rant about virtualenv sometimes ignoring the above directives)

## Limitations
Known limitations and problems include
* `deps` from environments not on the `envlist` will not be gathered.
* `-l` should be set when gathering dependencies to avoid actually running the environments.
