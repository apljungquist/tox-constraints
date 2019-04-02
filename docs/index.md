# tox-constraints docs


## Objectives

The primary objective of this project is to make it easy to have reproducible tests.
This is accomplished by

1. collecting all packages and constraints used by a project,
2. compiling a list of locked package versions, and
3. enforcing the use of the locked version of packages.

### Collection

Packages are collected from these sources

#### Tox deps

Manually ensuring that all packages used in tox are pinned in the constraints is laborious.
To make this easier this plugin established a pattern for modular requirements files and automatically populates one such file with all the abstract dependencies listed in the deps variables.

I suspect there are some problems related to constraints.
<!--
As such the recommended method as of now is to introduce all constraints via files.
TODO: Implement and test lock/constraints overriding.
-->

#### Setuptools install_requires

This one is a bit inelegant as of writing.
To make it easy to collect packages listed here it is expected that they be factored out from `setup.py` to the file `requirements/install_requires.txt`.
<!--
TODO: Would `pyproject.toml` be easier to collect from?
-->

One benefit of this method is that it makes the [enforcement](#enforcement) easier.

I suspect there are deficiencies related to conditional inclusions such as platform, python version, and extras.

### Compilation

Use `pip-compile` manually or in a build script.
See `Makefile` of this project for example.

### Enforcement

Two invocations of tox can have show different results even if the code being tested has not changed.
This can happen for instance if a different version of the dependencies is installed.
Both packages used to run the tests, and the dependencies of the package under test, can change.

To avoid this the tox documentation suggests that

> If you have a requirements.txt file or a constraints.txt file you can add it to your deps variable

This method has some drawbacks:

1. The constraints are applied only to the other packages listed in the deps variable, not to the package under test or its dependencies.
2. It is verbose and repetitive.

Drawback 1 above can be mitigated by also adding `.` to the deps variable but this
smells a little bit and aggravates drawback 2.


## Related projects

This section documents my research into other projects.
It should
* convince the reader that a project is not relevant and can be disregarded or,
* find ways in which a project can be used to accomplish the objective of this project, jointly or separately.

### tox

This project is a plugin for `tox` so, in a way, it is being used.
Vanilla `tox` does have a few deficiencies however, some of which I have complained about above.

### pip-tools

`pip-compile` is my recommended way of locking package versions so, in a way, it is being used.

### pipenv

Pipenv seems rather focused on application development, as opposed to library development.
This allows them to adopt a more rigid model in which it exists
* only one version of python,
* only one or two sets of abstract requirements (default, development),
* only one set of concrete constraints (`Pipfile.lock`).

It seems to [work OK-ish with tox](https://github.com/tox-dev/tox-pipenv)

> Is tox.ini deps section really in control?
> No, this is a known limitation.

However, none of the above should prevent it to be used as the primary source of concrete constraints instead of `constraints.txt`.
It should also still be possible to output the results of collection to a pipfile.

### poetry

My impression of poetry is that it aims to replace the PyPA packaging-installation chain with a single tool.
This seems risky and inflexible.
However, this opinion is largely unsupported by concrete evidence and should be taken lightly.

[Frost Ming](https://frostming.com/2019/01-04/pipenv-poetry) points out one important flaw

> Poetry only works under one workflow.
> For example, it doesn't support installing current dependencies into system Python, which is the typical workflow for developing in docker.


## Terminology

This section is an attempt to help myself separate some concepts and use them consistently.

### Abstract dependencies

[Donald Stufft](https://caremad.io/posts/2013/07/setup-vs-requirement/) *abstract dependencies* as

> dependencies which exist only as a name and an optional version specifier

He further compares them to duck typing:

> Think of it like duck typing your dependencies, you don’t care what specific “requests” you get as long as it looks like “requests”.

### Concrete dependencies

These are specific instances of abstract dependencies.
They are typically expressed as a specific version and a packaging index or referred to directly using a URL.

### Requirements

The [pip documentation](https://pip.pypa.io/en/stable/user_guide/#requirements-files) contains this excerpt

> “Requirements files” are files containing a list of items to be installed

In the context of this project each such item is a *requirement*.

Requirements must be abstract.
They can be put in a few locations like
* `install_requires` variable of a setup.py file,
* `deps` variable of a tox configuration (with exceptions),
* dedicated files named like
    * `requirements.txt` containing the product of all other requirements, or
    * `requirements/*.txt`.

### Constraints

The [pip documentation](https://pip.pypa.io/en/stable/user_guide/#constraints-files) contains this excerpt

> Constraints files are requirements files that only control which version of a requirement is installed, not whether it is installed or not.

In the context of this project each item in such a file is a *constraint*.

Constraints may be absent (equivalent to no constraint), abstract, or concrete.
They can be put in files named like
    * `constraints.txt` corresponding to `requirements.txt`, or
    * `constraints-*.txt` for alternative constraints.
