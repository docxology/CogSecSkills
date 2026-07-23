# AGENTS.md - Runner And Generator Code

This directory contains the Python implementation. Keep it as the thin runner
and generator layer over declarative project data.

## Module Boundaries

- `cli.py` only parses arguments, calls module functions, and prints results.
- `core/spec.py`, `core/registry.py`, `core/loader.py`, `quality/validate.py`,
  and `core/harness.py` define parsing, registry loading, discovery, structural
  validation, and harness conformance.
- `core/locate.py` provides project-root discovery (`project_root`,
  `resolve_root`) — the shared helper replacing per-module `_project_root`.
- `core/quality_constants.py` holds shared quality-policy constants used by both
  `quality/insights.py` and `authoring/definitions.py`.
- `core/text_utils.py` holds shared `clean_cell` and `as_text` helpers used by
  `artifacts/evals.py`, `artifacts/examples.py`, and `manuscript_assets/rows.py`.
- `authoring/author.py`, `authoring/definitions.py`, and `authoring/scaffold.py`
  own skill rendering and drift checks from canonical definitions.
- `quality/insights.py`, `artifacts/scenarios.py`, `artifacts/examples.py`,
  `artifacts/evals.py`, `artifacts/dashboard.py`, `artifacts/release_metadata.py`,
  and `artifacts/manuscript_assets/` own local navigation, deterministic scenario
  checks, worked examples, offline output-review fixtures, generated dashboard
  output, release claim metadata, manuscript supplements, data exports, and figures.

## Editing Rules

- CLI remains a thin orchestrator. Keep CLI behavior synchronized with
  `docs/cli.md`, README command snippets, and CLI tests.
- Do not move quality or scenario policy into generated Markdown; keep checks in
  Python and source fixtures.
- Any new generated output needs both `--write` and `--check` behavior, plus a
  stale-file test.
- Do not add live model, web, OSINT connector, publication, or DOI claims to
  code comments or command output.

## Verification

```bash
PYTHONPATH="src:." python -m pytest tests/test_cogsecskills_*.py tests/test_skill_library_conformance.py --cov=src/cogsecskills --cov-report=term-missing
uv run ruff check src/cogsecskills tests
uv run ruff format --check src/cogsecskills tests
uv run mypy
```
