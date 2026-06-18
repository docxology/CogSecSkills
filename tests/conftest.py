"""Pytest configuration for CogSecSkills.

Adds the project's ``src/`` directory to the import path so ``import cogsecskills``
works from a clean checkout without an editable install. This makes the suite
self-contained: ``pytest`` (or ``uv run pytest``) from the project root just works.
"""

import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "src")
for _path in (SRC, ROOT):
    if _path not in sys.path:
        sys.path.insert(0, _path)
