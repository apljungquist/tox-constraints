# tox-constraints

*Reproducible tests, with minimal configuration, by default*


## Limitations

This section lists known problems with the current implementation.

### PyPy compatibility

The version of pip that ships with pypy does not seem to like the `-r` option on which this plugin depends.

### Incomplete constraints
If the constraints file does not include some package, that package will not have its version pinned but the tests may still pass.
That is unless hashes are used.
This is the primary version I use hashes in library packages - to ensure pip fails if not all packages are constrained.
