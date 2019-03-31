# tox-constraints

*Makes tests reproducible with minimal configuration*

## Usage

On occasions when I have been too lazy to provide friendly examples, my other projects may be a good place to look.

[This is such an occasion](https://github.com/apljungquist/xfmt/commit/99341b58694e846dc009fca01cb6fb3d442fbe66).

## Objectives

The primary objective of this project is to make it easy to have reproducible tests.
This is accomplished by

1. collecting all packages and constraints used by a project,
2. compiling a list of locked package versions, and
3. enforcing the use of the locked version of packages.

## Collection

Packages are collected from these sources

### Tox deps

Manually ensuring that all packages used in tox are pinned in the constraints is laborious.
To make this easier this plugin established a pattern for modular requirements files and automatically populates one such file with all the abstract dependencies listed in the deps variables.

I suspect there are some problems related to constraints.
<!--
As such the recommended method as of now is to introduce all constraints via files.
TODO: Implement and test lock/constraints overriding.
-->

### Setuptools install_requires

This one is a bit inelegant as of writing.
To make it easy to collect packages listed here it is expected that they be factored out from `setup.py` to the file `requirements/install_requires.txt`.
<!--
TODO: Would `pyproject.toml` be easier to collect from?
-->

One benefit of this method is that it makes the [enforcement](#enforcement) easier.

I suspect there are deficiencies related to conditional inclusions such as platform, python version, and extras.


## Compilation

Use `pip-compile` manually or in a build script.
See `Makefile` of this project for example.


## Enforcement

Two invocations of tox can have show different results even if the code being tested has not changed.
This can happen for instance if a different version of the dependencies is installed.
Both packages used to run the tests, and the dependencies of the package under test, can change.

To avoid this the tox documentation suggests that

> If you have a requirements.txt file or a constraints.txt file you can add it to your deps variable

This method has some drawbacks:

1. The constraints are applied only to the other packages listed in the deps variable, not to the package under test or its dependencies.
2. It is verbose and repetitive.

Drawback 1 above can be mitigated by also adding `.` to the deps variable but this
smells a little bit and aggrevates drawback 2.


## Why not just use ...

### tox

This project is a plugin for `tox` so, in a way, it is being used.
Vanilla `tox` does have a few deficiencies however, some of which I have complained about above.

### pip-tools

`pip-compile` is my recommended way of locking package versions so, in a way, it is being used.

### pipenv
<!--
I seem to remember pipenv being an all-or-nothing solution but I have not researched it specifically for this project.
TODO: Research what pipenv can do for the objectives of this project
-->
