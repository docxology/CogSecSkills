"""CLI contract tests for the catalogue command's drift check."""

from __future__ import annotations

import shutil
from pathlib import Path

from cogsecskills.cli import main

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _copy_catalogue_fixture(tmp_path: Path) -> Path:
    shutil.copytree(PROJECT_ROOT / "registry", tmp_path / "registry")
    (tmp_path / "docs").mkdir()
    shutil.copy2(
        PROJECT_ROOT / "docs" / "catalogue.md", tmp_path / "docs" / "catalogue.md"
    )
    return tmp_path


def test_catalogue_check_current(tmp_path):
    root = _copy_catalogue_fixture(tmp_path)

    assert main(["--root", str(root), "catalogue", "--check"]) == 0


def test_catalogue_check_stale(tmp_path):
    root = _copy_catalogue_fixture(tmp_path)
    doc = root / "docs" / "catalogue.md"
    doc.write_text(
        doc.read_text(encoding="utf-8") + "\nunexpected hand edit\n", encoding="utf-8"
    )

    assert main(["--root", str(root), "catalogue", "--check"]) == 1


def test_catalogue_check_missing(tmp_path):
    root = _copy_catalogue_fixture(tmp_path)
    (root / "docs" / "catalogue.md").unlink()

    assert main(["--root", str(root), "catalogue", "--check"]) == 1


def test_catalogue_check_output_target(tmp_path):
    root = _copy_catalogue_fixture(tmp_path)
    target = tmp_path / "elsewhere.md"
    shutil.copy2(PROJECT_ROOT / "docs" / "catalogue.md", target)

    assert (
        main(["--root", str(root), "catalogue", "--check", "--output", str(target)])
        == 0
    )

    target.write_text(
        target.read_text(encoding="utf-8") + "\ndrift\n", encoding="utf-8"
    )
    assert (
        main(["--root", str(root), "catalogue", "--check", "--output", str(target)])
        == 1
    )


def test_catalogue_write_then_check_roundtrip(tmp_path):
    root = _copy_catalogue_fixture(tmp_path)
    doc = root / "docs" / "catalogue.md"
    doc.write_text("stale\n", encoding="utf-8")
    assert (
        main(["--root", str(root), "catalogue", "--markdown", "--output", str(doc)])
        == 0
    )

    assert main(["--root", str(root), "catalogue", "--check"]) == 0
