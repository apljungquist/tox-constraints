"""Tests checking that this project interacts as expected with other projects.

A sort ot system test if you will.
"""
import pathlib
import shutil
import subprocess

import pytest  # type: ignore

_PROJECT_ROOT = pathlib.Path(__file__).parents[1]
_SAMPLE_PROJECTS = _PROJECT_ROOT / "sample_projects"
_PROJECT_NAMES = [
    # Keep slow tests and expected failures in the back to fail fast
    pytest.param("coalmine", marks=[]),
    pytest.param("simple", marks=[]),
]


@pytest.mark.parametrize("project_name", _PROJECT_NAMES)
def test_does_not_break(project_name, tmpdir):
    """Smoke test

    Ensures that having tox-constraints installed does not interfere in projects that
    do not use it.

    Ensures that for projects that use tox constraints do not smoke.
    This is especially useful in combination with offensive programming mechanisms.
    """
    # Copy to:
    # 1. avoid interaction with this project e.g. by accidentally using its constraints
    #    file, and
    # 2. ensure test starts with clean slat
    dst = tmpdir / project_name
    shutil.copytree(_SAMPLE_PROJECTS / project_name, dst)
    subprocess.check_call(["tox"], cwd=dst)
