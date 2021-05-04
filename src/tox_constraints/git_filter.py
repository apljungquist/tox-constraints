"""Git filter for portable constraints files"""
import pathlib
import subprocess
import sys
from typing import Iterator, Tuple


def _run(cmd) -> str:
    return subprocess.run(cmd, capture_output=True, check=True, text=True).stdout


def _top_level() -> pathlib.Path:
    return pathlib.Path(_run(["git", "rev-parse", "--show-toplevel"]).strip())


def _replacements() -> Iterator[Tuple[str, str]]:
    # Prefix the replacement with # so that the result is still a valid constraints
    # file. If not done, bootstrapping toxc can become an issue.
    top_level = _top_level()
    yield f"-e file://{top_level}", "# $TOP_LEVEL$"
    yield f"file://{top_level}", "# $TOP_LEVEL_PLAIN$"


def clean_text(text: str) -> str:
    """Testable core of the clean command"""
    for src, tgt in _replacements():
        text = text.replace(src, tgt)
    return text


def smudge_text(text: str) -> str:
    """Testable core of the smudge command"""
    for tgt, src in _replacements():
        text = text.replace(src, tgt)
    return text


def install() -> None:
    """Configure git to use this filter"""
    _run(["git", "config", "--local", "filter.toxc.clean", "toxc-clean"])
    _run(["git", "config", "--local", "filter.toxc.smudge", "toxc-smudge"])


def clean():
    """Clean command for this git filter"""
    sys.stdout.write(clean_text(sys.stdin.read()))


def smudge():
    """Smudge command for this git filter"""
    sys.stdout.write(smudge_text(sys.stdin.read()))
