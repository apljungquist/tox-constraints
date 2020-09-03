"""Git filter for portable constraints files"""
import pathlib
import subprocess
import sys
from typing import Tuple


def _run(cmd) -> str:
    return subprocess.run(cmd, capture_output=True, check=True, text=True).stdout


def _top_level() -> pathlib.Path:
    return pathlib.Path(_run(["git", "rev-parse", "--show-toplevel"]).strip())


def _replacement() -> Tuple[str, str]:
    # Prefix the replacement with # so that the result is still a valid constraints
    # file. If not done, bootstrapping toxc can become an issue.
    return f"-e file://{_top_level()}", "# $TOP_LEVEL$"


def clean_text(text: str) -> str:
    """Testable core of the clean command"""
    src, tgt = _replacement()
    return text.replace(src, tgt)


def smudge_text(text: str) -> str:
    """Testable core of the smudge command"""
    tgt, src = _replacement()
    return text.replace(src, tgt)


def install() -> None:
    """Configure git to use this filter"""
    _run(["git", "config", "filter.toxc.clean", "toxc-clean"])
    _run(["git", "config", "filter.toxc.smudge", "toxc-smudge"])


def clean():
    """Clean command for this git filter"""
    sys.stdout.write(clean_text(sys.stdin.read()))


def smudge():
    """Smudge command for this git filter"""
    sys.stdout.write(smudge_text(sys.stdin.read()))
