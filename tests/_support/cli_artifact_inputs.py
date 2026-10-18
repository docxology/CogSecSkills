"""Shared real inputs for cli artifact inputs tests."""

from __future__ import annotations

import copy

import re

import shutil

from pathlib import Path

from tests.project_fixtures import copy_project_dirs

import pytest

import yaml

from cogsecskills.cli import main

PROJECT_ROOT = Path(__file__).resolve().parents[2]


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


def _copy_fixture(tmp_path: Path, *dirnames: str) -> Path:
    return copy_project_dirs(tmp_path, *dirnames)


_VALID_SCENARIO: dict = {
    "id": "no-route",
    "group": "sat",
    "kind": "safe_defensive",
    "query": "zzqxzzwvk authorized qqpzwwkx",
    "expected_skill": "sat.x",
    "expected_output_terms": ["product"],
    "required_quality_terms": ["evidence"],
    "expected_response": {
        "required_sections": ["s1", "s2", "s3"],
        "must_include_terms": ["evidence", "confidence", "uncertainty", "defensive"],
        "must_exclude_terms": ["x", "y"],
    },
    "expected_answer": {
        "selected_skill": "sat.x",
        "answer_kind": "defensive_output",
        "sections": [
            {"title": "A", "body": "evidence inference gap confidence"},
            {"title": "B", "body": "uncertainty"},
            {"title": "C", "body": "defensive"},
        ],
        "rubric_scores": {},
    },
}


def _write_scenario_fixture(root: Path, scenario: dict) -> None:
    (root / "scenarios").mkdir(exist_ok=True)
    (root / "scenarios" / "defensive_readiness.yaml").write_text(
        yaml.safe_dump({"scenarios": [scenario]}, sort_keys=False), encoding="utf-8"
    )


__all__ = [
    "PROJECT_ROOT",
    "_ROW",
    "_VALID_SCENARIO",
    "_copy_fixture",
    "_seed_registry",
    "_write_scenario_fixture",
    "copy",
    "main",
    "pytest",
    "re",
    "shutil",
]
