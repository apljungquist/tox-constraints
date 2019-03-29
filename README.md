# tox-constraints

*Making tests (almost) reproducible using `tox` and `pip-tools`.*

The plugin tries to make tests more reproducible in two ways.

## Installing packages using `--constraint`

Two invocations of tox can have show different results even if the code being tested
has not changed.
This can happen for instance if a different version of the dependencies is installed.
Both packages used to run the tests, and the dependencies of the package under test,
can change.

To avoid this the tox documentation suggests that

> If you have a requirements.txt file or a constraints.txt file you can add it to your deps variable

This method has some drawbacks:

1. The constraints are applied only to the other packages listed in the deps variable,
   not to the package under test or its dependencies.
2. It is verbose and repetitive.

Drawback 1 above can be mitigated by also adding `.` to the deps variable but this
smells a little bit and aggrevates drawback 2.

## Exporting the deps variables from `tox.ini`

Manually ensuring that all packages used in tox are pinned in the constraints is
laborious.
To make this easier this plugin established a pattern for modular requirements files
and automatically populates one such file with all the abstract dependencies listed in
the deps variables.

## `install_requires.txt`

Factored out from setup.py to make dependencies accessible to `pip-compile`.

Initially included in `install_command` in the hope that it would allow hashes but it
turns out hashes do not work with package under test so two different
`install_command`s would be needed.

## TODO

- [ ] Multiple constraints (stable, high, low, devel)
- [ ] Pin versions
- [ ] Automatic tests
- [ ] `make`-less compilation (e.g. `tox-export` and `tox-compile`)
