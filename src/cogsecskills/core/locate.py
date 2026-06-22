"""Locate the project root independent of module nesting depth.

Walking up to a sentinel (the skill registry or pyproject.toml) is robust to
package reorganization, unlike hardcoded ``Path(__file__).parents[N]`` depths,
which silently misresolve whenever a module moves between directories.
"""

from __future__ import annotations

from pathlib import Path


def project_root() -> Path:
    """Return the project root: the nearest ancestor containing the skill
    registry (``registry/skills.yaml``) or ``pyproject.toml``."""
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "registry" / "skills.yaml").is_file() or (
            parent / "pyproject.toml"
        ).is_file():
            return parent
    # Fail loud rather than silently returning a wrong directory: a misresolved
    # root would make path-guarded code quietly skip outputs.
    raise RuntimeError(  # pragma: no cover - only reachable outside a project tree
        "could not locate the CogSecSkills project root (no registry/skills.yaml "
        f"or pyproject.toml above {here})"
    )
