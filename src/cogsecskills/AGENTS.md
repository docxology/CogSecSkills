# AGENTS.md - Runner And Generator Code

This directory contains the Python implementation. Keep it as the thin runner
and generator layer over declarative project data.

## Module Boundaries

- `cli.py` only parses arguments, calls module functions, and prints results.
- `spec.py`, `registry.py`, `loader.py`, `validate.py`, and `harness.py` define
  parsing, registry loading, discovery, structural validation, and harness
  conformance.
- `author.py`, `definitions.py`, and `scaffold.py` own skill rendering and
  drift checks from canonical definitions.
- `insights.py`, `scenarios.py`, `examples.py`, `evals.py`, `dashboard.py`,
  `release_metadata.py`, and `manuscript_assets.py` own local navigation,
  deterministic scenario checks, worked examples, offline output-review
  fixtures, generated dashboard output, release claim metadata, manuscript
  supplements, data exports, and figures.

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
