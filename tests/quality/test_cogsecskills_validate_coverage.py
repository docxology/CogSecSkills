"""Behavioral edge cases of the validate gate.

Covers: an adapter that exists but cannot be read is reported as unreadable
(fault-injected OSError — permission-independent), a harness support map that
cannot realise a declared verb fails conformance, and a malformed registry is
reported by ``conformance_report`` instead of raising.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from cogsecskills.core.spec import SkillSpec, ToolVerb


def _make_spec(skills_dir: Path) -> SkillSpec:
    (skills_dir / "skill.yaml").write_text(
        "id: sat.demo\nname: Demo\ngroup: sat\nsummary: s\nstatus: implemented\n"
        "tools:\n  - {verb: read, purpose: p}\n"
        "harness:\n  claude: harness/claude.md\n  codex: harness/codex.md\n  hermes: harness/hermes.md\n",
        encoding="utf-8",
    )
    (skills_dir / "SKILL.md").write_text("# Demo\n", encoding="utf-8")
    (skills_dir / "workflow.md").write_text(
        "# W\n\n## Step 1 — S (read)\nText.\n", encoding="utf-8"
    )
    harness_dir = skills_dir / "harness"
    harness_dir.mkdir()
    for h in ("claude", "codex", "hermes"):
        (harness_dir / f"{h}.md").write_text(
            "| `read` | tool | note |\n", encoding="utf-8"
        )
    return SkillSpec.from_mapping(
        yaml.safe_load((skills_dir / "skill.yaml").read_text(encoding="utf-8"))
    )


def test_adapter_read_failure_reported_as_unreadable(tmp_path, monkeypatch):
    """An adapter that exists but cannot be read is an error, not a crash."""
    from cogsecskills.quality.validate import validate_skill

    skills_dir = tmp_path / "skills" / "sat" / "demo"
    skills_dir.mkdir(parents=True)
    spec = _make_spec(skills_dir)
    claude = skills_dir / "harness" / "claude.md"

    # Fault injection at the filesystem seam: an unreadable adapter (e.g. a
    # directory-shaped path) surfaces as IsADirectoryError/OSError. Injected via
    # monkeypatch so the test is permission-independent (root ignores chmod).
    original_read_text = Path.read_text

    def fail_on_claude(path, *args, **kwargs):
        if path == claude:
            raise IsADirectoryError(21, "Is a directory", str(path))
        return original_read_text(path, *args, **kwargs)

    monkeypatch.setattr(Path, "read_text", fail_on_claude)
    result = validate_skill(spec, skills_dir)
    assert any("unreadable" in i.message for i in result.errors)


def test_unsupported_verbs_in_validate_skill(tmp_path):
    """A harness support map that cannot realise a declared verb is an error."""

    skills_dir = tmp_path / "skills" / "sat" / "demo"
    skills_dir.mkdir(parents=True)
    spec = _make_spec(skills_dir)
    # A support map where claude can't realise 'read'
    from cogsecskills.core.harness import check_conformance

    conf = check_conformance(
        spec, support={"claude": frozenset()}, harnesses=("claude",)
    )
    assert conf["claude"].unsupported_verbs == (ToolVerb.READ,)


def test_conformance_report_malformed_registry(tmp_path):
    """A registry that fails to load is reported by conformance_report, not raised."""
    from cogsecskills.quality.validate import conformance_report

    # Create a malformed registry
    reg_dir = tmp_path / "registry"
    reg_dir.mkdir()
    (reg_dir / "skills.yaml").write_text(
        "skills:\n  - {id: bad, group: nonexistent, status: implemented, summary: s}\n",
        encoding="utf-8",
    )
    (reg_dir / "groups.yaml").write_text(
        "groups:\n  - {id: sat, title: SAT}\n", encoding="utf-8"
    )
    # This should not crash — conformance_report catches the error
    report = conformance_report(tmp_path)
    assert report["errors"] >= 1

    # Also test discover_skills raising FileNotFoundError or SpecError inside conformance_report
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(
            "cogsecskills.quality.validate.discover_skills",
            lambda *args, **kwargs: (_ for _ in ()).throw(
                FileNotFoundError("skills missing")
            ),
        )
        report_fail = conformance_report(tmp_path)
        assert report_fail["on_disk_skills"] == 0
