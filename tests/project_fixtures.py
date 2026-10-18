"""Shared real repository copies for artifact regression tests."""

from pathlib import Path
import shutil

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def copy_project_dirs(root: Path, *dirnames: str) -> Path:
    for dirname in dirnames:
        shutil.copytree(PROJECT_ROOT / dirname, root / dirname)
    return root
