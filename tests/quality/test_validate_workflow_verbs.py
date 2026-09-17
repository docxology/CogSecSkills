"""Tests for the workflow-step verb gate in ``quality/validate.py``.

A workflow step heading tags the verbs it uses (``## Step N — Title (verb,
verb)``); the validator must error when a tagged verb is not declared by the
spec's tool list — a workflow must never promise a capability the spec does
not authorise.
"""

from __future__ import annotations

from pathlib import Path

import yaml

from cogsecskills.core.spec import SkillSpec
from cogsecskills.quality.validate import (
    conformance_report,
    validate_library,
    validate_skill,
)

VERBS = ("read",)


def _seed_registry(root: Path, *, status: str = "planned") -> None:
    (root / "registry").mkdir(parents=True, exist_ok=True)
    (root / "registry" / "skills.yaml").write_text(
        "skills:\n"
        f"  - {{id: sat.demo, name: Demo Technique, group: sat, status: {status}, "
        "summary: A demo technique.}\n",
        encoding="utf-8",
    )
    (root / "registry" / "groups.yaml").write_text(
        "groups:\n  - {id: sat, title: SAT}\n", encoding="utf-8"
    )


def _make_skill(
    tmp_path: Path,
    *,
    verbs: tuple[str, ...] = VERBS,
    workflow_text: str = "# W\n\n## Step 1 — S (read)\nText.\n",
    workflow_name: str = "workflow.md",
) -> tuple[SkillSpec, Path]:
    skills_dir = tmp_path / "skills" / "sat" / "demo"
    (skills_dir / "harness").mkdir(parents=True, exist_ok=True)
    tool_lines = "".join(f"  - {{verb: {verb}, purpose: p}}\n" for verb in verbs)
    (skills_dir / "skill.yaml").write_text(
        f"id: sat.demo\nname: Demo\ngroup: sat\nsummary: s\nstatus: planned\n"
        f"tools:\n{tool_lines}"
        f"workflow: {workflow_name}\n"
        "harness:\n  claude: harness/claude.md\n",
        encoding="utf-8",
    )
    (skills_dir / "SKILL.md").write_text("# Demo\n", encoding="utf-8")
    (skills_dir / workflow_name).write_text(workflow_text, encoding="utf-8")
    (skills_dir / "harness" / "claude.md").write_text(
        "| `read` | tool | note |\n", encoding="utf-8"
    )
    spec = SkillSpec.from_mapping(
        yaml.safe_load((skills_dir / "skill.yaml").read_text(encoding="utf-8"))
    )
    return spec, skills_dir


def test_undeclared_workflow_verb_is_flagged(tmp_path):
    spec, directory = _make_skill(
        tmp_path,
        verbs=("read",),
        workflow_text="# W\n\n## Step 1 — S (read, web)\nText.\n",
    )
    result = validate_skill(spec, directory)
    messages = [i.message for i in result.errors]
    assert any(
        "workflow steps tag verbs not declared in the spec: web" in m for m in messages
    )


def test_undeclared_verb_fails_validation_result(tmp_path):
    spec, directory = _make_skill(
        tmp_path,
        workflow_text="# W\n\n## Step 1 — S (exec)\nText.\n",
    )
    result = validate_skill(spec, directory)
    assert not result.ok


def test_declared_verbs_pass(tmp_path):
    spec, directory = _make_skill(
        tmp_path,
        workflow_text=(
            "# W\n\n## Step 1 — S (read)\nText.\n## Step 2 — T (read)\nText.\n"
        ),
    )
    result = validate_skill(spec, directory, harnesses=("claude",))
    assert result.ok, [i.message for i in result.errors]


def test_verb_tags_are_case_insensitive(tmp_path):
    spec, directory = _make_skill(
        tmp_path,
        workflow_text="# W\n\n## Step 1 — S (READ)\nText.\n",
    )
    result = validate_skill(spec, directory, harnesses=("claude",))
    assert result.ok, [i.message for i in result.errors]


def test_verb_tags_match_authoring_normalisation(tmp_path):
    """Whitespace-padded and mixed-case tags normalise like the renderer's."""
    spec, directory = _make_skill(
        tmp_path,
        workflow_text="# W\n\n## Step 1 — S ( read ,READ )\nText.\n",
    )
    result = validate_skill(spec, directory, harnesses=("claude",))
    assert result.ok, [i.message for i in result.errors]


def test_workflow_without_step_headings_passes(tmp_path):
    spec, directory = _make_skill(
        tmp_path, workflow_text="# W\n\nNo tagged steps here.\n"
    )
    result = validate_skill(spec, directory, harnesses=("claude",))
    assert result.ok, [i.message for i in result.errors]


def test_empty_verb_fragments_are_ignored(tmp_path):
    """A trailing comma leaves an empty fragment; it must not count as a verb."""
    spec, directory = _make_skill(
        tmp_path, workflow_text="# W\n\n## Step 1 — S (read,)\nText.\n"
    )
    result = validate_skill(spec, directory, harnesses=("claude",))
    assert result.ok, [i.message for i in result.errors]


def test_unreadable_workflow_reports_error(tmp_path):
    spec, directory = _make_skill(tmp_path)
    workflow = directory / "workflow.md"
    workflow.chmod(0o000)
    try:
        result = validate_skill(spec, directory)
    finally:
        workflow.chmod(0o644)
    assert any("unreadable" in i.message for i in result.errors)


def test_escaping_workflow_path_skips_verb_check(tmp_path):
    """A path-escape workflow is flagged by the path guard, not the verb check."""
    spec, directory = _make_skill(tmp_path, workflow_name="../escape.md")
    result = validate_skill(spec, directory)
    assert any("must stay inside" in i.message for i in result.errors)
    assert not any("workflow steps tag verbs" in i.message for i in result.errors)


def test_conformance_report_passes_configured_harnesses(tmp_path):
    """``conformance_report(..., harnesses=...)`` checks the same harness set
    ``validate_library`` does when given the same argument."""
    _seed_registry(tmp_path)
    spec, directory = _make_skill(tmp_path)
    result = validate_skill(spec, directory, harnesses=("claude",))
    assert result.ok, [i.message for i in result.errors]

    # Default harness set: codex/hermes adapters are undeclared → errors.
    default_report = conformance_report(tmp_path)
    assert default_report["errors"] > 0

    # Configured narrow harness set: only claude is required → clean.
    narrow_report = conformance_report(tmp_path, harnesses=("claude",))
    assert narrow_report["errors"] == 0
    assert narrow_report["ok"] is True


def test_validate_library_harnesses_flag_undeclared_adapters(tmp_path):
    """The same harness override reaches per-skill adapter checks."""
    _seed_registry(tmp_path)
    _make_skill(tmp_path)

    narrow = validate_library(tmp_path, harnesses=("claude",))
    assert narrow.ok, [i.message for i in narrow.errors]

    default = validate_library(tmp_path)
    assert any(
        "does not declare a 'codex' harness adapter" in i.message
        for i in default.errors
    )
