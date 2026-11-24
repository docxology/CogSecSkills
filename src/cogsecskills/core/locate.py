"""Locate the project root independent of module nesting depth.

The skill registry identifies a library checkout independently of module
nesting. An explicit root is available for inspecting an incomplete checkout.
"""

from __future__ import annotations

from pathlib import Path


def project_root() -> Path:
    """Prefer the current directory's library, then look above the module."""
    # Installed packages do not have the library's declarative data beside
    # their module files. Prefer the checkout the command is operating in;
    # generic pyproject.toml files in unrelated cwd trees are not sentinels.
    cwd = Path.cwd().resolve()
    for parent in (cwd, *cwd.parents):
        if (parent / "registry" / "skills.yaml").is_file():
            return parent
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "registry" / "skills.yaml").is_file():
            return parent
    # Fail loud rather than silently returning a wrong directory: a misresolved
    # root would make path-guarded code quietly skip outputs.
    raise RuntimeError(  # pragma: no cover - only reachable outside a project tree
        "could not locate the CogSecSkills project root "
        f"(no registry/skills.yaml above {cwd} or {here}). Pass --root explicitly."
    )


def resolve_root(root: Path | None = None) -> Path:
    """Return ``root`` as a Path, or fall back to :func:`project_root`.

    This is the shared helper for modules that need to resolve an optional
    ``root`` parameter to a concrete project root. It replaces the
    ``Path(root) if root is not None else project_root()`` pattern duplicated
    across 8+ modules.
    """
    return Path(root) if root is not None else project_root()
