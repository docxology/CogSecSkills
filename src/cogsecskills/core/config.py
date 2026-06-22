"""Configuration — make CogSecSkills configurable without editing code.

An optional ``cogsecskills.yaml`` at the project root overrides the defaults
below. Everything has a sensible default, so the file is never required. YAML is
used (not TOML) so there is no new dependency and Python 3.10 is supported.

Example ``cogsecskills.yaml``::

    # Add or remove agent harnesses the library targets and validates.
    harnesses: [claude, codex, hermes]

    # Quality thresholds the `doctor` command enforces.
    quality:
      min_workflow_steps: 3
      min_anti_criteria: 2
      require_references: false

Adding a harness here makes ``scaffold``/``author`` generate an adapter for it and
``validate`` require one — no code change needed. An unknown harness is assumed to
support the full closed verb vocabulary (see :mod:`cogsecskills.harness`).
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml

from cogsecskills.core.harness import HARNESSES

CONFIG_FILENAME = "cogsecskills.yaml"


@dataclass(frozen=True)
class Config:
    """Resolved configuration for a CogSecSkills project."""

    harnesses: tuple[str, ...] = HARNESSES
    min_workflow_steps: int = 3
    min_anti_criteria: int = 2
    require_references: bool = False

    @classmethod
    def defaults(cls) -> "Config":
        return cls()


def config_path(root: Path | None = None) -> Path:
    base = Path(root) if root is not None else Path(__file__).resolve().parents[3]
    return base / CONFIG_FILENAME


def load_config(root: Path | None = None) -> Config:
    """Load ``cogsecskills.yaml`` if present, else return defaults.

    A malformed config raises :class:`ValueError` with a precise message rather
    than silently falling back — a config that is present but wrong should be
    surfaced, not ignored.
    """
    path = config_path(root)
    if not path.is_file():
        return Config.defaults()
    raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(raw, dict):
        raise ValueError(f"{path}: expected a top-level mapping")

    harnesses = raw.get("harnesses", list(HARNESSES))
    if not isinstance(harnesses, list) or not harnesses:
        raise ValueError(f"{path}: 'harnesses' must be a non-empty list")
    harnesses = tuple(str(h).strip() for h in harnesses if str(h).strip())
    if not harnesses:
        raise ValueError(f"{path}: 'harnesses' resolved to empty after cleaning")

    quality = raw.get("quality", {}) or {}
    if not isinstance(quality, dict):
        raise ValueError(f"{path}: 'quality' must be a mapping")

    def _int(key: str, default: int) -> int:
        value = quality.get(key, default)
        if not isinstance(value, int) or isinstance(value, bool):
            raise ValueError(f"{path}: quality.{key} must be an integer")
        return value

    return Config(
        harnesses=harnesses,
        min_workflow_steps=_int("min_workflow_steps", 3),
        min_anti_criteria=_int("min_anti_criteria", 2),
        require_references=bool(quality.get("require_references", False)),
    )
