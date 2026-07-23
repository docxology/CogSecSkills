"""CogSecSkills — agentic tool-use skills for Cognitive Security & analytic tradecraft.

This package is the *runner* for the CogSecSkills library: it discovers skills on
disk under ``skills/``, parses each skill's harness-neutral ``skill.yaml`` spec,
validates it, and proves the spec loads equally under every supported agent
harness (Claude Code, Codex, Hermes). The skills themselves are data + prompts;
this package is the small, fully-tested engine that makes them dependable.

Design follows the repository's thin-orchestrator contract: all logic lives here
(or in a skill's declarative spec); scripts and harnesses only orchestrate.

Public API
----------
- :class:`SkillSpec` — parsed, validated representation of one ``skill.yaml``.
- :data:`HARNESSES` — the supported harness identifiers.
- :func:`load_skill` / :func:`discover_skills` — read skills from disk.
- :class:`SkillRegistry` — the enumerated catalogue of all skill areas.
- :func:`validate_skill` / :func:`conformance_report` — validation gates.
"""

from __future__ import annotations

from cogsecskills.authoring.author import author_batch, render_definition
from cogsecskills.core.config import Config, load_config
from cogsecskills.core.harness import HARNESSES, HarnessConformance, check_conformance
from cogsecskills.quality.insights import (
    doctor,
    library_stats,
    render_catalogue_markdown,
    route_query,
)
from cogsecskills.core.loader import discover_skills, load_skill, skills_root
from cogsecskills.core.registry import (
    RegistryEntry,
    SkillRegistry,
    load_registry,
    registry_path,
)
from cogsecskills.authoring.scaffold import scaffold_skill
from cogsecskills.core.spec import SkillIO, SkillSpec, SkillTool, ToolVerb
from cogsecskills.quality.validate import (
    ValidationIssue,
    ValidationResult,
    conformance_report,
    validate_library,
    validate_skill,
)

__all__ = [
    "HARNESSES",
    "Config",
    "HarnessConformance",
    "RegistryEntry",
    "SkillIO",
    "SkillRegistry",
    "SkillSpec",
    "SkillTool",
    "ToolVerb",
    "ValidationIssue",
    "ValidationResult",
    "author_batch",
    "check_conformance",
    "conformance_report",
    "discover_skills",
    "doctor",
    "library_stats",
    "load_config",
    "load_registry",
    "load_skill",
    "registry_path",
    "render_catalogue_markdown",
    "render_definition",
    "route_query",
    "scaffold_skill",
    "skills_root",
    "validate_library",
    "validate_skill",
]

__version__ = "1.5.0"
