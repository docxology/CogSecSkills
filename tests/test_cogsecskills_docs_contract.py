"""Contract tests for forward-looking docs and example fixtures."""

from __future__ import annotations

import re
from pathlib import Path

import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _transcript_blocks(text: str) -> dict[str, str]:
    headings = list(re.finditer(r"^## (.+)$", text, flags=re.MULTILINE))
    blocks: dict[str, str] = {}
    for index, match in enumerate(headings):
        start = match.end()
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        blocks[match.group(1)] = text[start:end]
    return blocks


OPTIONAL_HARNESS_PROFILE_IDS = (
    "gemini_cli",
    "github_copilot",
    "devin_local",
    "devin_cascade",
    "cursor",
    "cline",
    "aider",
    "continue",
    "jetbrains_ai",
    "openai_agents_sdk",
    "langgraph",
    "microsoft_agent_framework",
    "autogen",
    "crewai",
    "pydantic_ai",
    "mcp_host",
    "perplexity_research",
)


def _harness_profiles() -> list[dict[str, str]]:
    raw = yaml.safe_load(
        (PROJECT_ROOT / "registry" / "harness_profiles.yaml").read_text(
            encoding="utf-8"
        )
    )
    return raw["profiles"]


def test_quickstart_and_docs_map_expose_next_reader_paths():
    quickstart = _read(PROJECT_ROOT / "QUICKSTART.md")
    docs_index = _read(PROJECT_ROOT / "docs" / "README.md")
    readme = _read(PROJECT_ROOT / "README.md")
    design = _read(PROJECT_ROOT / "DESIGN.md")

    assert "git clone https://github.com/docxology/CogSecSkills.git" in quickstart
    assert "python -m cogsecskills scenarios --check" in quickstart
    assert "python -m cogsecskills examples --check" in quickstart
    assert "python -m cogsecskills evals --check" in quickstart
    assert "python -m cogsecskills dashboard --check" in quickstart
    assert "python -m cogsecskills release-metadata --check" in quickstart
    assert "skills/osint_integrity/claim_provenance_verification" in quickstart
    assert "QUICKSTART.md" in docs_index
    assert "harness-cookbook.md" in docs_index
    assert "claim-boundaries.md" in docs_index
    assert "quality-dashboard.md" in docs_index
    assert "quality-dashboard.html" in docs_index
    assert "skill-worked-examples.md" in docs_index
    assert "evaluation-readiness.md" in docs_index
    assert "release-claim-matrix.md" in docs_index
    assert "future-validation-protocols.md" in docs_index
    assert "QUICKSTART.md" in readme
    assert "dashboard --write" in readme
    assert "examples --write" in readme
    assert "evals --write" in readme
    assert "release-metadata --write" in readme
    assert "DESIGN.md" in readme
    assert "Generated Dashboard" in design


def test_claim_boundary_and_connector_docs_preserve_local_claim_limits():
    claim_boundaries = _read(PROJECT_ROOT / "docs" / "claim-boundaries.md")
    connector_boundaries = _read(PROJECT_ROOT / "docs" / "connector-boundaries.md")

    assert "locally validated" in claim_boundaries
    assert "field validated" in claim_boundaries
    assert "runtime certified" in claim_boundaries
    assert "The current repository does not wire live OSINT" in connector_boundaries
    assert "Private-person identification" in connector_boundaries
    assert "Connector integration should add its own tests" in connector_boundaries


def test_harness_examples_cover_default_and_custom_harnesses():
    cookbook = _read(PROJECT_ROOT / "docs" / "harness-cookbook.md")
    transcripts = _read(PROJECT_ROOT / "examples" / "harness-smoke-transcripts.md")
    blocks = _transcript_blocks(transcripts)

    for harness in ("Codex", "Claude", "Hermes", "Custom Harness"):
        assert harness in cookbook
        assert harness in transcripts
        assert f"{harness} Safe" in blocks
        assert f"{harness} Unsafe" in blocks
    assert "not live model runs" in transcripts
    assert "Expected bounded output" in transcripts
    assert "Unsafe boundary" in transcripts
    assert len([name for name in blocks if name.endswith(("Safe", "Unsafe"))]) == 8

    for name, block in blocks.items():
        if not name.endswith(("Safe", "Unsafe")):
            continue
        for field in (
            "Fixture provenance:",
            "Harness:",
            "Scenario id:",
            "Selected skill:",
            "Files loaded:",
            "Expected bounded output:",
            "Unsafe boundary:",
        ):
            assert field in block, name
        assert "not a live model run" in block
        assert re.search(r"Scenario id: .+-(safe|unsafe)", block), name


def test_optional_harness_profile_registry_is_complete():
    profiles = _harness_profiles()
    required_fields = {
        "id",
        "display_name",
        "class",
        "recommended_config_name",
        "instruction_surface",
        "tool_surface",
        "official_doc_url",
        "claim_boundary",
    }
    allowed_classes = {
        "terminal_agent",
        "ide_or_cloud_agent",
        "local_agent",
        "ide_agent",
        "ide_or_cli_agent",
        "programmatic_runtime",
        "protocol_host",
        "research_companion",
    }

    ids = [str(profile["id"]) for profile in profiles]
    assert tuple(ids) == OPTIONAL_HARNESS_PROFILE_IDS
    assert len(ids) == len(set(ids))
    for profile in profiles:
        assert required_fields <= profile.keys(), profile["id"]
        assert profile["class"] in allowed_classes, profile["id"]
        assert profile["recommended_config_name"] == profile["id"]
        assert str(profile["official_doc_url"]).startswith("https://")
        assert (
            "Profile" in profile["claim_boundary"]
            or "profile" in profile["claim_boundary"]
        )


def test_optional_harness_profiles_are_documented_without_runtime_claims():
    docs_text = "\n".join(
        _read(PROJECT_ROOT / path)
        for path in (
            "docs/harness-installation.md",
            "docs/harness-cookbook.md",
            "docs/configuration.md",
            "docs/skill-contract.md",
        )
    )
    manuscript_text = "\n".join(
        _read(PROJECT_ROOT / path)
        for path in ("manuscript/02_system_context.md", "manuscript/03_methods.md")
    )

    for text in (docs_text, manuscript_text):
        for profile_id in OPTIONAL_HARNESS_PROFILE_IDS:
            assert profile_id in text
        for status_label in (
            "default adapters",
            "configured structural adapters",
            "documented external profiles",
        ):
            assert status_label in text
        for overclaim in (
            "runtime certified",
            "field validated",
            "works in every external runtime",
        ):
            assert overclaim not in text


def test_harness_transcript_loaded_files_exist_or_are_documented_custom_paths():
    transcripts = _read(PROJECT_ROOT / "examples" / "harness-smoke-transcripts.md")

    file_lines = [
        line[2:].strip()
        for line in transcripts.splitlines()
        if line.startswith("- skills/")
    ]
    assert len(file_lines) == 24
    for rel_path in file_lines:
        path = PROJECT_ROOT / rel_path
        if rel_path.endswith("/harness/custom_harness.md"):
            assert "custom_harness has been configured" in transcripts.replace("`", "")
            assert (PROJECT_ROOT / rel_path.rsplit("/harness/", maxsplit=1)[0]).is_dir()
            continue
        assert path.is_file(), rel_path


def test_group_examples_cover_all_skill_groups():
    examples = _read(PROJECT_ROOT / "examples" / "group-worked-examples.md")
    for skill_id in (
        "sat.analysis_of_competing_hypotheses",
        "cognitive_security.narrative_threat_assessment",
        "critical_review.project_critical_review",
        "osint_integrity.claim_provenance_verification",
        "counterintelligence.denial_and_deception_detection",
        "information_environment.narrative_ecosystem_mapping",
        "research_methods.structured_literature_synthesis",
    ):
        assert skill_id in examples
    assert "evidence" in examples.lower()
    assert "inference" in examples.lower()
    assert "confidence" in examples.lower()
    assert "uncertainty" in examples.lower()


def test_todo_forward_backlog_has_expected_next_lanes():
    todo = _read(PROJECT_ROOT / "TODO.md")
    for heading in (
        "Evidence Ladder",
        "Harness Smoke Examples",
        "Quickstart And Harness Cookbook",
        "Quality Dashboard",
        "Deferred: Empirical Evaluation",
        "Deferred: Live Connector Integrations",
        "Deferred: External Publication/DOI",
    ):
        assert heading in todo
    assert "expected answers checked" in todo
    assert "worked examples are current" in todo


def test_release_checklist_and_review_protocol_name_required_gates():
    release = _read(PROJECT_ROOT / "docs" / "release-checklist.md")
    review = _read(PROJECT_ROOT / "docs" / "analyst-output-review.md")

    for command in (
        "definitions --check",
        "scenarios --check",
        "evals --check",
        "dashboard --check",
        "release-metadata --check",
        "manuscript-assets --check",
        "uv run mypy",
    ):
        assert command in release
    assert "Score each dimension as `0`, `1`, or `2`" in review
    assert "refusal and safe redirect" in review


def test_future_protocols_are_marked_as_future_not_completed_validation():
    protocols = _read(PROJECT_ROOT / "docs" / "future-validation-protocols.md")
    for phrase in (
        "future work",
        "not completed validation",
        "Exploratory Baseline Comparison",
        "Analyst Usability Pilot",
        "Live Connector Readiness",
        "Publication And DOI Readiness",
    ):
        assert phrase in protocols
