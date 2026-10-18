from __future__ import annotations

import json
from pathlib import Path

from tests.project_fixtures import copy_project_dirs

import yaml

from cogsecskills.artifacts.examples import (
    EXAMPLES_JSON_PATH,
    EXAMPLES_MD_PATH,
    check_examples,
    load_examples,
    write_examples,
)

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _copy_examples_fixture(tmp_path: Path) -> Path:
    return copy_project_dirs(tmp_path, "registry", "skills", "examples")


def test_repository_examples_cover_all_rendered_skills():
    examples = load_examples(PROJECT_ROOT)
    skill_ids = {example.skill_id for example in examples}
    registry_ids = {
        entry["id"]
        for entry in yaml.safe_load(
            (PROJECT_ROOT / "registry" / "skills.yaml").read_text(encoding="utf-8")
        )["skills"]
    }

    assert len(examples) == len(registry_ids)
    assert skill_ids == registry_ids
    assert check_examples(PROJECT_ROOT) == []
    assert all(example.provenance == "authored local example" for example in examples)


def test_examples_write_and_check_generate_markdown_and_json(tmp_path):
    root = _copy_examples_fixture(tmp_path)

    expected_count = len(
        yaml.safe_load((root / "registry/skills.yaml").read_text())["skills"]
    )
    result = write_examples(root)

    assert result["examples"] == expected_count
    assert result["markdown"] == str(EXAMPLES_MD_PATH)
    assert result["data"] == str(EXAMPLES_JSON_PATH)
    assert check_examples(root) == []

    markdown = (root / EXAMPLES_MD_PATH).read_text(encoding="utf-8")
    payload = json.loads((root / EXAMPLES_JSON_PATH).read_text(encoding="utf-8"))
    assert "# CogSecSkills Skill Worked Examples" in markdown
    assert "deterministic local examples" in markdown
    assert payload["summary"]["examples"] == expected_count
    assert len(payload["examples"]) == expected_count
    assert all(item["skill_id"] for item in payload["examples"])


def test_examples_check_rejects_missing_stale_and_unsafe_source(tmp_path):
    root = _copy_examples_fixture(tmp_path)
    write_examples(root)

    source = root / "examples" / "skill-worked-examples.yaml"
    raw = yaml.safe_load(source.read_text(encoding="utf-8"))
    removed = raw["examples"].pop()
    source.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
    findings = check_examples(root)
    assert any("missing worked examples" in finding for finding in findings)

    raw["examples"].append(removed)
    raw["examples"][0]["sections"][0]["body"] += " step-by-step operational playbook"
    source.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
    findings = check_examples(root)
    assert any("operational misuse detail" in finding for finding in findings)

    raw["examples"][0]["sections"][0]["body"] = raw["examples"][0]["sections"][0][
        "body"
    ].replace(" step-by-step operational playbook", "")
    source.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
    (root / EXAMPLES_MD_PATH).write_text("manual drift\n", encoding="utf-8")
    findings = check_examples(root)
    assert any("stale generated examples file" in finding for finding in findings)


def test_cli_examples_write_and_check(tmp_path, capsys):
    from cogsecskills.cli import main

    root = _copy_examples_fixture(tmp_path)
    assert main(["--root", str(root), "examples", "--write"]) == 0
    assert "wrote worked examples" in capsys.readouterr().out
    assert main(["--root", str(root), "examples", "--check"]) == 0
    assert "worked examples are current" in capsys.readouterr().out
