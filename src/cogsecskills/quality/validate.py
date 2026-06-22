"""Validation gates for the skill library.

Three layers of checks:

1. **Per-skill structural** — a skill's directory has every companion file its
   spec promises (``SKILL.md``, the workflow doc, and one adapter per harness),
   and the spec's id matches its on-disk location.
2. **Multiharness conformance** — the spec maps onto every supported harness
   (see :mod:`cogsecskills.harness`).
3. **Library/registry coherence** — every on-disk skill is enumerated in the
   registry with a matching group, and every registry entry marked
   ``implemented`` actually exists on disk.

The asymmetry between "missing" and "extra" is deliberate (cf. the validation
asymmetry lesson): an *implemented* registry entry with no on-disk skill is a
hard error, while a *planned* entry with no on-disk skill is the normal,
expected state of an un-built area — not an error.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from cogsecskills.core.harness import HARNESSES, check_conformance
from cogsecskills.core.loader import (
    SPEC_FILENAME,
    discover_skills,
    load_skill,
    skill_dir,
    skills_root,
)
from cogsecskills.core.registry import SkillRegistry, load_registry
from cogsecskills.core.spec import SkillSpec, SpecError, ToolVerb

SEVERITY_ERROR = "error"
SEVERITY_WARNING = "warning"


@dataclass(frozen=True)
class ValidationIssue:
    """One problem found during validation."""

    severity: str
    skill_id: str
    message: str


@dataclass
class ValidationResult:
    """Aggregate validation outcome."""

    issues: list[ValidationIssue] = field(default_factory=list)

    @property
    def errors(self) -> list[ValidationIssue]:
        return [i for i in self.issues if i.severity == SEVERITY_ERROR]

    @property
    def warnings(self) -> list[ValidationIssue]:
        return [i for i in self.issues if i.severity == SEVERITY_WARNING]

    @property
    def ok(self) -> bool:
        return not self.errors

    def error(self, skill_id: str, message: str) -> None:
        self.issues.append(ValidationIssue(SEVERITY_ERROR, skill_id, message))

    def warn(self, skill_id: str, message: str) -> None:
        self.issues.append(ValidationIssue(SEVERITY_WARNING, skill_id, message))


def _safe_declared_path(
    directory: Path,
    declared: str,
    result: ValidationResult,
    skill_id: str,
    label: str,
) -> Path | None:
    """Resolve a spec-declared companion path without allowing path escape."""
    declared_path = Path(declared)
    if declared_path.is_absolute() or ".." in declared_path.parts:
        result.error(
            skill_id,
            f"{label} path {declared!r} must stay inside the skill directory",
        )
        return None
    return directory / declared_path


def _adapter_bound_verbs(text: str) -> frozenset[ToolVerb]:
    """Extract neutral verbs bound by an adapter's Markdown table rows."""
    verbs: set[ToolVerb] = set()
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [
            cell.strip().strip("`*_ ").lower()
            for cell in stripped.strip("|").split("|")
        ]
        if not cells or set(cells[0]) <= {"-"}:
            continue
        try:
            verbs.add(ToolVerb.coerce(cells[0]))
        except SpecError:
            continue
    return frozenset(verbs)


def validate_skill(
    spec: SkillSpec, directory: Path, harnesses: tuple[str, ...] | None = None
) -> ValidationResult:
    """Validate one skill's structural completeness and harness conformance.

    ``harnesses`` overrides the default harness set (e.g. resolved from
    ``cogsecskills.yaml``); defaults to :data:`cogsecskills.harness.HARNESSES`.
    """
    result = ValidationResult()
    directory = Path(directory)
    targets = harnesses if harnesses is not None else HARNESSES

    # 1. Claude Code native entry point.
    if not (directory / "SKILL.md").is_file():
        result.error(spec.id, "missing SKILL.md (Claude Code native entry point)")

    # 2. Workflow document referenced by the spec.
    workflow_path = _safe_declared_path(
        directory, spec.workflow, result, spec.id, "workflow"
    )
    if workflow_path is not None and not workflow_path.is_file():
        result.error(spec.id, f"missing workflow document {spec.workflow!r}")

    # 3. One adapter file per harness, both declared, present, and binding every
    #    neutral verb the spec uses.
    for harness in targets:
        declared = spec.harness.get(harness, "").strip()
        if not declared:
            result.error(
                spec.id, f"spec does not declare a {harness!r} harness adapter"
            )
            continue
        adapter_path = _safe_declared_path(
            directory, declared, result, spec.id, f"{harness!r} adapter"
        )
        if adapter_path is None:
            continue
        if not adapter_path.is_file():
            result.error(
                spec.id, f"declared {harness!r} adapter {declared!r} not found"
            )
            continue
        try:
            bound_verbs = _adapter_bound_verbs(adapter_path.read_text(encoding="utf-8"))
        except OSError as exc:
            result.error(spec.id, f"{harness!r} adapter {declared!r} unreadable: {exc}")
            continue
        missing = tuple(
            verb
            for verb in sorted(spec.verbs, key=lambda v: v.value)
            if verb not in bound_verbs
        )
        if missing:
            verbs = ", ".join(v.value for v in missing)
            result.error(
                spec.id,
                f"{harness!r} adapter does not bind declared tool verbs: {verbs}",
            )

    # 4. Multiharness conformance (verb support + adapter declared).
    for harness, conf in check_conformance(spec, harnesses=targets).items():
        if conf.unsupported_verbs:
            verbs = ", ".join(v.value for v in conf.unsupported_verbs)
            result.error(spec.id, f"harness {harness!r} cannot realise verbs: {verbs}")

    # 5. A skill that claims to be implemented must declare at least one tool.
    if spec.is_implemented and not spec.tools:
        result.error(spec.id, "implemented skill declares no tool-use capabilities")

    # 6. Directory/id/group coherence: <skills>/<group>/<slug>/ and
    #    skill id <group>.<slug>.
    expected_prefix = f"{spec.group}."
    if not spec.id.startswith(expected_prefix) or spec.id == expected_prefix:
        result.error(
            spec.id,
            f"skill id must be '<group>.<slug>' using group {spec.group!r}",
        )

    if directory.parent.name != spec.group:
        result.error(
            spec.id,
            f"on-disk group {directory.parent.name!r} != spec group {spec.group!r}",
        )

    # 7. Slug coherence: the leaf directory must equal the id's slug, so a
    #    skill can never be reached at a folder that disagrees with its id.
    slug = spec.id.split(".", 1)[1] if "." in spec.id else spec.id
    if directory.name != slug:
        result.error(
            spec.id,
            f"on-disk folder {directory.name!r} != skill slug {slug!r}",
        )

    return result


def _discover_with_dirs(root: Path | None) -> list[tuple[SkillSpec, Path]]:
    """Discover skills once, pairing each spec with its directory (no rescans)."""
    tree = skills_root(root)
    if not tree.is_dir():
        return []
    pairs = [
        (load_skill(path), skill_dir(path))
        for path in sorted(tree.rglob(SPEC_FILENAME))
    ]
    return sorted(pairs, key=lambda p: p[0].id)


def validate_library(
    root: Path | None = None, harnesses: tuple[str, ...] | None = None
) -> ValidationResult:
    """Validate every on-disk skill and check registry coherence.

    ``harnesses`` overrides the default harness set (resolve it from
    ``cogsecskills.yaml`` via :func:`cogsecskills.config.load_config`).
    """
    result = ValidationResult()
    try:
        pairs = _discover_with_dirs(root)
    except (FileNotFoundError, SpecError) as exc:
        result.error("<skills>", f"skills could not be loaded: {exc}")
        pairs = []
    specs = [spec for spec, _ in pairs]
    on_disk_ids = {spec.id for spec in specs}

    try:
        registry: SkillRegistry | None = load_registry(root)
    except (FileNotFoundError, SpecError) as exc:
        result.error("<registry>", f"registry could not be loaded: {exc}")
        registry = None

    for spec, directory in pairs:
        for issue in validate_skill(spec, directory, harnesses=harnesses).issues:
            result.issues.append(issue)

    if registry is not None:
        reg_ids = set(registry.ids)
        defined_groups = set(registry.groups)
        for entry in registry.entries:
            if (
                not entry.id.startswith(f"{entry.group}.")
                or entry.id == f"{entry.group}."
            ):
                result.error(
                    entry.id,
                    f"registry id must be '<group>.<slug>' using group {entry.group!r}",
                )
        # Missing/dangling: implemented registry rows must exist on disk (HARD).
        for entry in registry.by_status("implemented"):
            if entry.id not in on_disk_ids:
                result.error(
                    entry.id,
                    "registry marks skill 'implemented' but no on-disk skill found",
                )
        # Every catalogued group must be defined in groups.yaml (when defined).
        if defined_groups:
            for entry in registry.entries:
                if entry.group not in defined_groups:
                    result.error(
                        entry.id,
                        f"registry group {entry.group!r} is not defined in groups.yaml",
                    )
        # Every on-disk skill must be catalogued with a matching group.
        for spec in specs:
            if spec.id not in reg_ids:
                result.error(spec.id, "on-disk skill is not enumerated in the registry")
            else:
                matched = registry.get(spec.id)
                assert matched is not None
                if matched.group != spec.group:
                    result.error(
                        spec.id,
                        f"registry group {matched.group!r} != spec group {spec.group!r}",
                    )

    return result


def conformance_report(root: Path | None = None) -> dict[str, object]:
    """Build a machine-readable summary of library + registry state."""
    try:
        specs = discover_skills(root)
    except (FileNotFoundError, SpecError):
        specs = []
    result = validate_library(root)
    try:
        registry = load_registry(root)
        counts = registry.status_counts()
        total = len(registry)
    except (FileNotFoundError, SpecError):
        counts = {}
        total = 0
    return {
        "registry_total": total,
        "registry_status_counts": counts,
        "on_disk_skills": len(specs),
        "errors": len(result.errors),
        "warnings": len(result.warnings),
        "ok": result.ok,
    }
