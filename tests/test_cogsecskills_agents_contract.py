from __future__ import annotations

import argparse
from pathlib import Path

from cogsecskills.cli import build_parser
from cogsecskills.manuscript_assets import GENERATED_HEADER


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def _read(rel_path: str) -> str:
    return (PROJECT_ROOT / rel_path).read_text(encoding="utf-8")


EXPECTED_AGENTS = (
    "AGENTS.md",
    "src/cogsecskills/AGENTS.md",
    "definitions/AGENTS.md",
    "skills/AGENTS.md",
    "registry/AGENTS.md",
    "scenarios/AGENTS.md",
    "docs/AGENTS.md",
    "manuscript/AGENTS.md",
    "tests/AGENTS.md",
)


def _subcommands() -> set[str]:
    parser = build_parser()
    subparser_action = next(
        action
        for action in parser._actions
        if isinstance(action, argparse._SubParsersAction)
    )
    return set(subparser_action.choices)


def test_agents_hierarchy_exists_and_names_local_boundaries():
    for rel_path in EXPECTED_AGENTS:
        assert (PROJECT_ROOT / rel_path).is_file(), rel_path

    root = _read("AGENTS.md")
    for phrase in (
        "Local AGENTS hierarchy",
        "definitions/<group>/<slug>.yaml",
        "skills/<group>/<slug>/",
        "scenarios/defensive_readiness.yaml",
        "examples/skill-worked-examples.yaml",
        "docs/quality-dashboard.md",
        "Optional harness profiles are documentation metadata",
    ):
        assert phrase in root

    expectations = {
        "src/cogsecskills/AGENTS.md": (
            "CLI remains a thin orchestrator",
            "Any new generated output needs both `--write` and `--check`",
        ),
        "definitions/AGENTS.md": (
            "canonical source of skill substance",
            "Do not make corresponding hand edits under `skills/**`",
        ),
        "skills/AGENTS.md": (
            "harness-facing build output",
            "do not patch the rendered file alone",
        ),
        "registry/AGENTS.md": (
            "harness_profiles.yaml",
            "does not change validation until a profile id is copied",
        ),
        "scenarios/AGENTS.md": (
            "expected_answer",
            "not live model outputs",
            "scenarios --check",
        ),
        "docs/AGENTS.md": (
            "quality-dashboard.md is generated",
            "skill-worked-examples.md is generated",
            "default adapters",
            "configured structural adapters",
            "documented external profiles",
        ),
        "manuscript/AGENTS.md": (
            "S10_skill_catalogue.md",
            "do not edit them directly",
        ),
        "tests/AGENTS.md": (
            "No mocks",
            "real `tmp_path`",
            "contract-test ownership",
        ),
    }
    for rel_path, phrases in expectations.items():
        text = _read(rel_path)
        for phrase in phrases:
            assert phrase in text, f"{rel_path}: {phrase}"


def test_boundary_guidance_avoids_external_certification_claims():
    boundary_paths = (
        *EXPECTED_AGENTS,
        "docs/harness-installation.md",
        "docs/harness-cookbook.md",
        "docs/configuration.md",
        "docs/skill-contract.md",
        "manuscript/02_system_context.md",
        "manuscript/03_methods.md",
    )
    forbidden = (
        "runtime certified",
        "works in every external runtime",
        "externally peer reviewed",
        "publication-ready",
        "field validated",
    )
    for rel_path in boundary_paths:
        text = _read(rel_path).lower()
        for phrase in forbidden:
            assert phrase not in text, f"{rel_path}: {phrase}"


def test_generated_manuscript_supplements_keep_source_header():
    for rel_path in (
        "manuscript/S10_skill_catalogue.md",
        "manuscript/S11_skill_metadata_matrix.md",
    ):
        assert _read(rel_path).startswith(GENERATED_HEADER), rel_path


def test_cli_surface_keeps_documented_gate_commands():
    assert {
        "validate",
        "report",
        "doctor",
        "definitions",
        "scenarios",
        "examples",
        "dashboard",
        "manuscript-assets",
        "scaffold",
        "author",
        "author-batch",
        "route",
        "catalogue",
    } <= _subcommands()
