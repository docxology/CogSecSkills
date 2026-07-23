from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

import yaml

from cogsecskills.artifacts.release_metadata import (
    check_release_metadata,
    write_release_metadata,
)


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _git(root: Path, *args: str) -> None:
    subprocess.run(["git", *args], cwd=root, check=True, capture_output=True, text=True)


def _copy_release_fixture(tmp_path: Path, *, clear_doi: bool = False) -> Path:
    for filename in ("pyproject.toml", "CITATION.cff", "codemeta.json", "LICENSE"):
        shutil.copy2(PROJECT_ROOT / filename, tmp_path / filename)
    for dirname in ("docs", "manuscript", "output", "figures"):
        if (PROJECT_ROOT / dirname).exists():
            shutil.copytree(PROJECT_ROOT / dirname, tmp_path / dirname)
    if clear_doi:
        # Simulate the pre-archive / local state regardless of whether the live
        # project has since been published with a real Zenodo DOI. Archive
        # availability is derived from CITATION.cff + codemeta.json (see
        # release_metadata._has_doi), so strip the DOI from those too.
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


def test_release_metadata_write_and_check_local_mode(tmp_path):
    root = _copy_release_fixture(tmp_path, clear_doi=True)

    result = write_release_metadata(root)

    assert result["mode"] == "local"
    assert check_release_metadata(root) == []
    markdown = (root / "docs" / "release-claim-matrix.md").read_text(encoding="utf-8")
    payload = json.loads(
        (root / "output" / "data" / "release_metadata.json").read_text(encoding="utf-8")
    )
    assert "does not publish" in markdown
    assert payload["archive"]["status"] == "unavailable"
    assert (
        payload["repository"]["expected"] == "https://github.com/docxology/CogSecSkills"
    )
    assert payload["git"]["snapshot_policy"].startswith("Exact git revision")
    assert "Git snapshot policy" in markdown


def test_release_metadata_check_survives_the_commit_that_changes_head(tmp_path):
    root = _copy_release_fixture(tmp_path)
    _git(root, "init")
    _git(root, "config", "user.email", "codex@example.invalid")
    _git(root, "config", "user.name", "Codex Test")

    write_release_metadata(root)
    _git(root, "add", ".")
    _git(root, "commit", "-m", "release metadata snapshot")

    assert check_release_metadata(root) == []


def test_release_metadata_detects_version_repo_and_license_drift(tmp_path):
    root = _copy_release_fixture(tmp_path)
    write_release_metadata(root)

    cff_path = root / "CITATION.cff"
    cff = yaml.safe_load(cff_path.read_text(encoding="utf-8"))
    cff["version"] = "9.9.9"
    cff_path.write_text(yaml.safe_dump(cff, sort_keys=False), encoding="utf-8")
    findings = check_release_metadata(root)
    assert any("version mismatch" in finding for finding in findings)

    cff["version"] = "0.1.0"
    cff["repository-code"] = "https://example.invalid/CogSecSkills"
    cff_path.write_text(yaml.safe_dump(cff, sort_keys=False), encoding="utf-8")
    findings = check_release_metadata(root)
    assert any("repository URL mismatch" in finding for finding in findings)

    cff["repository-code"] = "https://github.com/docxology/CogSecSkills"
    cff["license"] = "Proprietary"
    cff_path.write_text(yaml.safe_dump(cff, sort_keys=False), encoding="utf-8")
    findings = check_release_metadata(root)
    assert any("CITATION.cff license" in finding for finding in findings)


def test_release_metadata_public_archive_mode_requires_real_archive(tmp_path):
    root = _copy_release_fixture(tmp_path, clear_doi=True)
    write_release_metadata(root)

    findings = check_release_metadata(root, mode="public-archive")

    assert any(
        "public-archive mode requires a real DOI" in finding for finding in findings
    )


def test_cli_release_metadata_write_and_check(tmp_path, capsys):
    from cogsecskills.cli import main

    root = _copy_release_fixture(tmp_path)
    assert main(["--root", str(root), "release-metadata", "--write"]) == 0
    assert "wrote release metadata" in capsys.readouterr().out
    assert main(["--root", str(root), "release-metadata", "--check"]) == 0
    assert "release metadata is current" in capsys.readouterr().out
