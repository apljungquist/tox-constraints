import pathlib
import re

import my_package
import pkg_resources
import pytest as pytest
import more_itertools

def test_my_package_is_available():
    assert my_package.VERSION


@pytest.mark.parametrize("dist", ["pip", "setuptools", "wheel"])
def test_virtualenv_seeded_correct_version(dist):
    constraints_file = pathlib.Path(__file__).parents[1]/"constraints.txt"
    match = more_itertools.one(re.finditer(f"^{dist}==(?P<version>.*)$", constraints_file.read_text(), flags=re.MULTILINE))
    expected = match.group("version")
    actual = pkg_resources.get_distribution(dist).version
    assert actual == expected
