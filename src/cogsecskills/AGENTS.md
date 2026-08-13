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
  `artifacts/evals.py`, `artifacts/examples.py`, and
  `artifacts/manuscript_assets/rows.py`.
- `authoring/author.py`, `authoring/definitions.py`, and `authoring/scaffold.py`
  own skill rendering and drift checks from canonical definitions.
- `quality/insights.py`, `artifacts/scenarios.py`, `artifacts/examples.py`,
  `artifacts/evals.py`, `artifacts/dashboard.py`, `artifacts/release_metadata.py`,
  and `artifacts/manuscript_assets/` own local navigation, deterministic scenario
  checks, worked examples, offline output-review fixtures, generated dashboard
  output, release claim metadata, manuscript supplements, data exports, and figures.

### `artifacts/manuscript_assets/` layout

Figure code is split by concern rather than living in one module:

| Module | Owns |
| --- | --- |
| `figure_specs.py` | `FigureMetadata`, `FIGURES`, `FIGURE_NAMES` — the registry of which figures exist |
| `figure_theme.py` | Design tokens: DPI, sizes, `TOKENS`, `COLOR_FAMILIES`, per-group palettes |
| `figure_helpers.py` | Shared drawing/theming helpers every panel draws through |
| `figure_charts.py` | Plotted-series panels: group counts, verb heatmap, reference density |
| `figure_diagrams.py` | Hand-laid panels: skill atlas, AGEINT network, plan/build/teach flow, harness matrix |
| `figure_cover.py` | The title-page installation cover (owns the `COVER_*` type scale) |
| `figures.py` | The `write_figures` orchestrator, re-exporting the names above |
| `png_probe.py` | Dependency-free PNG checks used by the generated-figure drift gate |
| `paths.py`, `rows.py`, `tables.py`, `assets_io.py` | Output paths, row collection, table rendering, write/check orchestration |

Add a new figure by appending to `FIGURES` in `figure_specs.py` and adding its
`_write_*` panel to whichever of `figure_charts` / `figure_diagrams` /
`figure_cover` matches its kind, then wiring it into `write_figures`. Import
shared constants from `figure_theme`, never by re-declaring them in a panel.

Panels are mutually independent: they share the theme tokens and the helpers and
never call each other, which is what lets them live in separate modules. A
refactor here is verifiable — regenerate and confirm every figure is
byte-identical, and check the write return code before trusting that comparison.

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
