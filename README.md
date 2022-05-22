# tox-constraints

*Reproducible tests, with minimal configuration, by default*

## Benefits
This plugin is helpful because it
* makes using pinned versions the default,
* tells virtualenv to use the pinned versions,
* facilitates gathering of dependencies, and 
* alerts you of the above pitfalls so that, hopefully, you do not have to learn it the hard way.

## Motivation
The best way to improve reproducibility of tox *without* this plugin is to set `PIP_CONSTRAINT` using either
1. `setenv`, or 
2. `passenv`.

This is good, it ensures that all packages installed with pip will use the constraints file[^1].

Setting `PIP_CONSTRAINT` does however not ensure that packages installed with other tools will use the constraints file.
Notably tox creates environments using virtualenv, which seeds the environment with some version of pip, setuptools, and wheel.
By default, a version that was bundled with the virtualenv is used, so while the behavior may be surprising it should be reproducible.
The versions installed can be controlled[^2] using `setenv` or `passenv` to set
* `VIRTUALENV_PIP`,
* `VIRTUALENV_SETUPTOOLS`, and
* `VIRTUALENV_WHEEL`.

Setting `PIP_CONSTRAINT` also does not ensure that all packages that will be installed are listed in the constraints file[^3].
pip-compile is a great tool to help both resolve all transient dependencies and assign a consistent set of versions.
But it cannot pick up `deps` from `tox.ini` file or `build-system.requires` from `pyproject.toml`.

## Limitations
Known limitations and problems include
* `deps` from environments not on the `envlist` will not be gathered.
* `-l` should be set when gathering dependencies to avoid actually running the environments.
* To make dependencies available to pip pip-compile they must be factored out into text files that are read by `setup.py`.
* The `build-system.requires` section from `pyproject.toml` must be manually reproduced in a text file to make it available to pip-compile.
* pip-compile replaces `.` from a requirements file with something like `my-package @ file:///home/username/reponame`.
  This package previously provided clean and smudge programs to help deal with this (among other things).
  Another workaround is to put requirements in files and read them dynamically in `setup.py`.
  Since dynamic usage of `setup.py` is discouraged it would be nice to add support for extracting the dependencies from `setup.cfg` or `pyproject.toml`.

[^1]: Using the `-c` flag on the other hand does not ensure that build dependencies are pinned, see [pip#8439](https://github.com/pypa/pip/issues/8439).
[^2]: Except when it does not.
      Something about it caching and upgrading packages locally causes it to occasionally ignore the specified versions.
      It can be hard to realize that this is happening and when it does the best course of action seems to be removing the cache at `~/.local/share/virtualenv/`.
[^3]: One could enable hash checking mode in which case pip would refuse to install any package for which it has not been given a hash.
      However, this creates new problems such as the package under test not having a hash.
      This package previously attempted to solve this use case but stopped since hash checking mode has been mostly broken in pip since the new resolver.
      :face_exhaling:
