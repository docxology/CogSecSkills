"""Pytest configuration for CogSecSkills.

Adds the project's ``src/`` directory to the import path so ``import cogsecskills``
works from a clean checkout without an editable install. This makes the suite
self-contained: ``pytest`` (or ``uv run pytest``) from the project root just works.
"""

import os
import sys
from pathlib import Path

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "src")
for _path in (SRC, ROOT):
    if _path not in sys.path:
        sys.path.insert(0, _path)

_PROJECT_ROOT = Path(ROOT)


@pytest.fixture(scope="session", autouse=True)
def _ensure_generated_artifacts():
    """Generate the gitignored ``output/`` artifacts once before the suite.

    A clean checkout has no ``output/`` tree — it is ``.gitignore``d as
    regeneratable. Several integration tests (and the CI coherence ``--check``
    gates, which run after pytest in the same job) assert against
    ``output/data/*.json`` and ``output/figures/*.png`` under the real project
    root, so they fail on a fresh clone unless those artifacts are built first.
    Generate them once per session when absent; idempotent and skipped when a
    populated ``output/`` already exists (e.g. a developer's working tree).
    """
    figures = _PROJECT_ROOT / "output" / "figures"
    examples_json = _PROJECT_ROOT / "output" / "data" / "skill_worked_examples.json"
    if examples_json.exists() and figures.is_dir() and any(figures.glob("*.png")):
        return

    from cogsecskills.artifacts.dashboard import write_dashboard
    from cogsecskills.artifacts.evals import write_evals
    from cogsecskills.artifacts.examples import write_examples
    from cogsecskills.artifacts.manuscript_assets import write_assets
    from cogsecskills.artifacts.release_metadata import write_release_metadata

    # Order matters: figures (write_assets) must exist before release-metadata,
    # which verifies the generated figure surface.
    write_examples(_PROJECT_ROOT)
    write_evals(_PROJECT_ROOT)
    write_assets(_PROJECT_ROOT)
    write_dashboard(_PROJECT_ROOT)
    write_release_metadata(_PROJECT_ROOT)
