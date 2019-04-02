# tox-constraints

*Makes tests reproducible with minimal configuration*


## Usage

On occasions when I have been too lazy to provide friendly examples, my other projects may be a good place to look.

[This is such an occasion](https://github.com/apljungquist/xfmt/commit/99341b58694e846dc009fca01cb6fb3d442fbe66).


## Limitations

This section lists known problems with the current implementation.

### PyPy compatibility

The version of pip that ships with pypy does not like the `-r` option on which this plugin depends.


## Why not just use ...

Good question, I may have answered it [here](docs/index.md)