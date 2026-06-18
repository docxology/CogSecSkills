"""Tests for the scaffold generator and the CLI, using real temp dirs."""

from __future__ import annotations

from pathlib import Path

import pytest

from cogsecskills.cli import main
from cogsecskills.loader import load_skill
from cogsecskills.scaffold import scaffold_skill
from cogsecskills.spec import SpecError
from cogsecskills.validate import validate_skill


def _seed_registry(root: Path, *rows: str) -> None:
    (root / "registry").mkdir(parents=True, exist_ok=True)
    (root / "registry" / "skills.yaml").write_text(
        "skills:\n" + "\n".join(rows) + "\n", encoding="utf-8"
    )
    (root / "registry" / "groups.yaml").write_text(
        "groups:\n  - {id: sat, title: SAT}\n", encoding="utf-8"
    )


_ROW = (
    "  - {id: sat.demo, name: Demo, group: sat, status: planned, summary: A demo area.}"
)


# --- scaffold ------------------------------------------------------------
def test_scaffold_creates_conforming_skill(tmp_path):
    _seed_registry(tmp_path, _ROW)
    created = scaffold_skill("sat.demo", root=tmp_path)
    assert len(created) == 6
    skill_yaml = tmp_path / "skills" / "sat" / "demo" / "skill.yaml"
    assert skill_yaml in created

    spec = load_skill(skill_yaml)
    assert spec.id == "sat.demo"
    assert spec.status == "stub"
    assert spec.tools  # scaffold gives a default tool plan
    # The scaffolded skill is structurally valid (stub status, all files present).
    result = validate_skill(spec, skill_yaml.parent)
    assert result.ok, [i.message for i in result.errors]
    for harness in ("codex", "hermes"):
        adapter = (skill_yaml.parent / "harness" / f"{harness}.md").read_text(
            encoding="utf-8"
        )
        assert "| `read` |" in adapter
        assert "| `reason` |" in adapter
        assert "| `write` |" in adapter


def test_scaffold_unknown_id(tmp_path):
    _seed_registry(tmp_path, _ROW)
    with pytest.raises(SpecError, match="not in the registry"):
        scaffold_skill("sat.missing", root=tmp_path)


def test_scaffold_refuses_overwrite(tmp_path):
    _seed_registry(tmp_path, _ROW)
    scaffold_skill("sat.demo", root=tmp_path)
    with pytest.raises(SpecError, match="already exists"):
        scaffold_skill("sat.demo", root=tmp_path)


def test_scaffold_overwrite_allowed(tmp_path):
    _seed_registry(tmp_path, _ROW)
    scaffold_skill("sat.demo", root=tmp_path)
    created = scaffold_skill("sat.demo", root=tmp_path, overwrite=True)
    assert len(created) == 6


# --- cli -----------------------------------------------------------------
def test_cli_list(tmp_path, capsys):
    _seed_registry(
        tmp_path,
        _ROW,
        "  - {id: sat.two, name: Two, group: sat, status: implemented, summary: s}",
    )
    rc = main(["--root", str(tmp_path), "list"])
    out = capsys.readouterr().out
    assert rc == 0
    assert "sat.demo" in out and "sat.two" in out
    assert "2 of 2 skill areas" in out


def test_cli_list_filtered(tmp_path, capsys):
    _seed_registry(
        tmp_path,
        _ROW,
        "  - {id: sat.two, name: Two, group: sat, status: implemented, summary: s}",
    )
    main(["--root", str(tmp_path), "list", "--status", "implemented"])
    out = capsys.readouterr().out
    assert "sat.two" in out and "sat.demo" not in out


def test_cli_validate_reports_errors(tmp_path, capsys):
    # implemented registry row with no on-disk skill => error => exit 1
    _seed_registry(
        tmp_path,
        "  - {id: sat.ghost, name: Ghost, group: sat, status: implemented, summary: s}",
    )
    rc = main(["--root", str(tmp_path), "validate"])
    out = capsys.readouterr().out
    assert rc == 1
    assert "error(s)" in out


def test_cli_report_json(tmp_path, capsys):
    _seed_registry(tmp_path, _ROW)
    rc = main(["--root", str(tmp_path), "report"])
    out = capsys.readouterr().out
    assert rc == 0
    assert '"registry_total": 1' in out


def test_cli_scaffold_and_show(tmp_path, capsys):
    _seed_registry(tmp_path, _ROW)
    rc = main(["--root", str(tmp_path), "scaffold", "sat.demo"])
    assert rc == 0
    assert "scaffolded 6 files" in capsys.readouterr().out

    rc = main(["--root", str(tmp_path), "show", "sat.demo"])
    out = capsys.readouterr().out
    assert rc == 0
    assert '"id": "sat.demo"' in out


def test_cli_scaffold_overwrite(tmp_path, capsys):
    _seed_registry(tmp_path, _ROW)
    assert main(["--root", str(tmp_path), "scaffold", "sat.demo"]) == 0
    capsys.readouterr()
    rc = main(["--root", str(tmp_path), "scaffold", "sat.demo", "--overwrite"])
    out = capsys.readouterr().out
    assert rc == 0
    assert "scaffolded 6 files" in out


def test_cli_show_planned_entry_not_on_disk(tmp_path, capsys):
    _seed_registry(tmp_path, _ROW)
    rc = main(["--root", str(tmp_path), "show", "sat.demo"])
    out = capsys.readouterr().out
    assert rc == 0
    assert "not yet built on disk" in out


def test_cli_show_unknown(tmp_path, capsys):
    _seed_registry(tmp_path, _ROW)
    rc = main(["--root", str(tmp_path), "show", "sat.nope"])
    out = capsys.readouterr().out
    assert rc == 1
    assert "unknown skill id" in out
