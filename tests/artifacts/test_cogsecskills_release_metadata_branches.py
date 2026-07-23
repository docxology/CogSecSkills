"""Tests for uncovered branches in release_metadata.py.

Covers: _has_doi edge cases, _findings for release-candidate mode,
missing LICENSE file, missing generated files, stale generated files.
"""

from __future__ import annotations

import json
import shutil
from pathlib import Path

import yaml

from cogsecskills.artifacts.release_metadata import (
    RELEASE_JSON_PATH,
    RELEASE_MD_PATH,
    _has_doi,
    check_release_metadata,
    write_release_metadata,
)

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _copy_fixture(tmp_path: Path, *, clear_doi: bool = True) -> Path:
    for filename in ("pyproject.toml", "CITATION.cff", "codemeta.json", "LICENSE"):
        shutil.copy2(PROJECT_ROOT / filename, tmp_path / filename)
    for dirname in ("docs", "manuscript", "output", "figures"):
        if (PROJECT_ROOT / dirname).exists():
            shutil.copytree(PROJECT_ROOT / dirname, tmp_path / dirname)
    if clear_doi:
        config_path = tmp_path / "manuscript" / "config.yaml"
        config = yaml.safe_load(config_path.read_text(encoding="utf-8"))
        config.setdefault("publication", {})
        config["publication"]["doi"] = ""
        config["publication"]["version_doi"] = ""
        config_path.write_text(
            yaml.safe_dump(config, sort_keys=False), encoding="utf-8"
        )
        cff_path = tmp_path / "CITATION.cff"
        cff = yaml.safe_load(cff_path.read_text(encoding="utf-8"))
        cff.pop("doi", None)
        cff.pop("identifiers", None)
        cff_path.write_text(yaml.safe_dump(cff, sort_keys=False), encoding="utf-8")
        codemeta_path = tmp_path / "codemeta.json"
        codemeta = json.loads(codemeta_path.read_text(encoding="utf-8"))
        codemeta.pop("identifier", None)
        codemeta_path.write_text(
            json.dumps(codemeta, indent=2) + "\n", encoding="utf-8"
        )
    return tmp_path


def test_has_doi_with_doi_field():
    assert _has_doi({"doi": "10.5281/zenodo.12345"})


def test_has_doi_with_identifiers_list():
    assert _has_doi({"identifiers": [{"type": "doi", "value": "10.1234/foo"}]})


def test_has_doi_without_doi():
    assert not _has_doi({"doi": ""})
    assert not _has_doi({})
    assert not _has_doi({"identifiers": [{"type": "url"}]})


def test_has_doi_with_identifier_string():
    assert _has_doi({"identifier": "10.5281/zenodo.999"})


def test_check_missing_license_file(tmp_path):
    root = _copy_fixture(tmp_path)
    write_release_metadata(root)
    (root / "LICENSE").unlink()
    findings = check_release_metadata(root)
    assert any("missing LICENSE file" in f for f in findings)


def test_check_stale_markdown(tmp_path):
    root = _copy_fixture(tmp_path)
    write_release_metadata(root)
    (root / RELEASE_MD_PATH).write_text("manual edit\n", encoding="utf-8")
    findings = check_release_metadata(root)
    assert any("stale generated release metadata file" in f for f in findings)


def test_check_stale_json(tmp_path):
    root = _copy_fixture(tmp_path)
    write_release_metadata(root)
    (root / RELEASE_JSON_PATH).write_text("{}", encoding="utf-8")
    findings = check_release_metadata(root)
    assert any("stale generated release metadata file" in f for f in findings)


def test_check_missing_generated_file(tmp_path):
    root = _copy_fixture(tmp_path)
    write_release_metadata(root)
    (root / RELEASE_MD_PATH).unlink()
    findings = check_release_metadata(root)
    assert any("missing generated release metadata file" in f for f in findings)


def test_release_candidate_mode_requires_clean_git(tmp_path):
    """release-candidate mode should flag a dirty worktree."""
    import subprocess

    root = _copy_fixture(tmp_path)
    subprocess.run(
        ["git", "init"], cwd=root, check=True, capture_output=True, text=True
    )
    subprocess.run(
        ["git", "config", "user.email", "test@example.invalid"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )
    subprocess.run(
        ["git", "config", "user.name", "Test"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )
    write_release_metadata(root)
    subprocess.run(
        ["git", "add", "."], cwd=root, check=True, capture_output=True, text=True
    )
    subprocess.run(
        ["git", "commit", "-m", "init"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )
    # Now modify a file to make the tree dirty
    (root / "LICENSE").write_text("modified\n", encoding="utf-8")
    findings = check_release_metadata(root, mode="release-candidate")
    assert any("clean git worktree" in f for f in findings)


def test_codemeta_license_mismatch(tmp_path):
    root = _copy_fixture(tmp_path)
    write_release_metadata(root)
    codemeta_path = root / "codemeta.json"
    codemeta = json.loads(codemeta_path.read_text(encoding="utf-8"))
    codemeta["license"] = "MIT"
    codemeta_path.write_text(json.dumps(codemeta, indent=2) + "\n", encoding="utf-8")
    findings = check_release_metadata(root)
    assert any("CodeMeta license" in f for f in findings)
