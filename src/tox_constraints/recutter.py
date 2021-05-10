"""Render various files

Useful for files that contain little unique information and either do not provide a
native way to get information dynamically from an external source or must have the
information bound statically because they are used early in the bootstrapping process.

The goal of this tool is to facilitate the creation and maintenance of code that is
mostly boilerplate yet require a lot of expertise to set up correctly. The model
adopted is roughly `file = expertise(information)` where the user provides the
information and the author provides the expertise.
"""
import argparse
from importlib import resources

import jinja2
import jinja2.meta

_TEMPLATES_PACKAGE = "tox_constraints.templates"


def _read_template(name):
    # TODO: Allow user to override bundled templates should they not like future updates
    return resources.read_text(_TEMPLATES_PACKAGE, name)


def _render_template(name, **kwargs):
    template = jinja2.Template(_read_template(name))
    return template.render(**kwargs)


def _template_kwarg_names(name):
    env = jinja2.Environment()
    ast = env.parse(_read_template(name))
    return jinja2.meta.find_undeclared_variables(ast)


def _template_names():
    other = {"__pycache__", "__init__.py"}
    return (
        resource
        for resource in resources.contents(_TEMPLATES_PACKAGE)
        if resource not in other
    )


def _init_subparser(subparsers, template_name):
    parser = subparsers.add_parser(template_name)
    for kwarg_name in _template_kwarg_names(template_name):
        parser.add_argument(
            "--" + kwarg_name, metavar=kwarg_name.upper(), required=True, type=str
        )


def _parser():
    parser = argparse.ArgumentParser(description="Render a file")
    parser.add_argument(
        "--output-file",
        type=str,
        metavar="PATH",
        help="write output to this path instead of printing to stdout",
    )
    subparsers = parser.add_subparsers(
        title="templates", required=True, dest="template_name"
    )
    for template_name in sorted(_template_names()):
        _init_subparser(subparsers, template_name)
    return parser


def main(args=None):
    """Render a file"""
    # TODO: Better way to collect information
    # Idea: Split tool in two parts
    # 1. Collect: Collect information from various sources such as pyproject.toml
    # 2. Render: Render requested files using collected information
    # Idea: Pluggable collectors and renderers
    kwargs = vars(_parser().parse_args(args))
    output_file = kwargs.pop("output_file")
    result = _render_template(kwargs.pop("template_name"), **kwargs)
    if output_file:
        # TODO: Rename fp to f
        with open(output_file, "w") as fp:
            fp.write(result)
    else:
        print(result)


if __name__ == "__main__":
    # This makes it quicker to set up run configuration in PyCharm
    main()
