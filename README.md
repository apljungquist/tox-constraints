# tox-constraints

*Reproducible tests, with minimal configuration, by default*

## Limitations

This section lists known problems with the current implementation.

### PyPy compatibility

The version of pip that ships with pypy does not seem to like the `-r` option on which this plugin depends.
