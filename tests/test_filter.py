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
    assert git_filter.clean_text(git_filter.smudge_text(sample)) == sample


@pytest.mark.parametrize("func", [git_filter.clean_text, git_filter.smudge_text])
def test_filters_are_idempontent(sample, func):
    expected = func(sample)
    actual = func(sample)
    assert actual == expected


def test_smudge_removed_marker(sample):
    evidence = "$"  # the presence of this string is evidence that the marker is present
    if not evidence in sample:
        raise RuntimeError("Evidence not present before test")
    assert evidence not in git_filter.smudge_text(sample)


def test_smudge_adds_url(sample):
    evidence = (
        "file://"  # the presence of this string is evidence that the url is present
    )
    if evidence in sample:
        raise RuntimeError("Evidence present before test")
    assert evidence in git_filter.smudge_text(sample)
