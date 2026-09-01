from __future__ import annotations

import argparse
import re
from pathlib import Path

from cogsecskills.artifacts.manuscript_assets import GENERATED_HEADER
from cogsecskills.cli import build_parser

PROJECT_ROOT = Path(__file__).resolve().parents[2]


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
    "docs/manuscript/AGENTS.md",
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
        "docs/manuscript/AGENTS.md": (
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
        "docs/manuscript/02_system_context.md",
        "docs/manuscript/03_methods.md",
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
        "docs/manuscript/S10_skill_catalogue.md",
        "docs/manuscript/S11_skill_metadata_matrix.md",
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


# --- Documented-path resolution -------------------------------------------------
#
# The phrase assertions above catch guidance that goes *missing*, but they cannot
# catch guidance that goes *stale*: a path that still reads plausibly while the
# file it names has moved. Two such references survived a package reorganisation
# (`tests/test_skill_library_conformance.py` after tests moved into per-concern
# packages, and `manuscript_assets/rows.py` after it moved under `artifacts/`),
# and an agent following either one lands on nothing. This test closes that class
# by resolving every path-like token in every AGENTS.md against the real tree.

_PATH_EXTENSIONS = {
    ".bib",
    ".cff",
    ".html",
    ".json",
    ".md",
    ".py",
    ".toml",
    ".txt",
    ".yaml",
    ".yml",
}

# Tokens that are deliberately not repository paths.
_NON_PATH_TOKENS = {
    # Optional user config; only `cogsecskills.yaml.example` is committed.
    "cogsecskills.yaml",
    # A filename *suffix* describing the author-batch compatibility input.
    "_def.json",
}


def _documented_path_tokens(text: str):
    """Yield backtick-quoted tokens from ``text`` that look like repo paths."""
    for raw in re.findall(r"`([^`\n]+)`", text):
        token = raw.strip()
        if not token or " " in token or "<" in token or ">" in token:
            continue  # prose, shell snippets, or `<group>/<slug>` placeholders
        if token.startswith(("-", "$", "http")):
            continue  # CLI flags, shell vars, URLs
        if "/" not in token and Path(token).suffix not in _PATH_EXTENSIONS:
            continue  # bare identifiers such as `implemented` or `read`
        yield token


def _token_resolves(token: str, doc_dir: Path) -> bool:
    """True when ``token`` names something real, read from ``doc_dir`` or the root."""
    if token in _NON_PATH_TOKENS:
        return True
    bases = (doc_dir, PROJECT_ROOT)
    if "*" in token:
        # Glob patterns such as `harness/*.md` describe every skill directory,
        # so a match anywhere under the tree satisfies them.
        if any(list(base.glob(token)) for base in bases):
            return True
        return bool(list(PROJECT_ROOT.glob(f"**/{token}")))
    if any((base / token).exists() for base in bases):
        return True
    bare = token.rstrip("/")
    if "/" not in bare:
        # A bare filename (`skill.yaml`, `SKILL.md`) is a per-skill pattern name.
        return bool(list(PROJECT_ROOT.glob(f"**/{bare}")))
    # A token carrying a directory component must resolve at that exact path —
    # finding the basename elsewhere is precisely the drift being guarded against.
    return False


def test_agents_documented_paths_resolve():
    unresolved: list[str] = []
    for rel_path in EXPECTED_AGENTS:
        doc = PROJECT_ROOT / rel_path
        for token in _documented_path_tokens(doc.read_text(encoding="utf-8")):
            if not _token_resolves(token, doc.parent):
                unresolved.append(f"{rel_path}: `{token}`")
    assert not unresolved, "AGENTS.md references paths that do not exist: " + "; ".join(
        unresolved
    )
