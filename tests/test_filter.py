# pylint: disable=missing-docstring,redefined-outer-name
import pathlib

import pytest

from tox_constraints import git_filter


@pytest.fixture
def sample():
    dirpath = pathlib.Path(__file__).with_suffix("")
    filepath = dirpath / "constraints.txt"
    return filepath.read_text()


def test_roundtrip(sample):
    assert git_filter.smudge_text(git_filter.clean_text(sample)) == sample


def test_username_not_in_clean(sample):
    assert "-e file://" not in git_filter.clean_text((sample))
