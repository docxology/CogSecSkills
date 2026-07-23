# Changelog

All notable changes to CogSecSkills are documented here. The format is loosely
based on [Keep a Changelog](https://keepachangelog.com/), and the project aims to
follow semantic versioning.

## [1.0.0] - 2026-06-22

First archived public release.

### Added

- Archived on Zenodo with a permanent DOI. Concept DOI (all versions):
  [10.5281/zenodo.20804585](https://doi.org/10.5281/zenodo.20804585); version
  DOI (v1.0.0): [10.5281/zenodo.20804586](https://doi.org/10.5281/zenodo.20804586).
- Title-cover figure now renders the archived DOI alongside the repository URL,
  leads with the `CogSecSkills` identity wordmark, and includes a live
  seven-group taxonomy band generated from the registry.

### Changed

- Abstract rewritten as a single comprehensive plaintext paragraph (no
  citations or code spans) for clean archive and citation metadata.
- Sharpened section titles across the manuscript.

## [1.7.0] - 2026-07-22

Coverage push to 98.84%, CI coverage gate bumped to 97%, remaining docstrings.

### Added

- **26 new tests** covering scenarios.py (unsafe-keyword, not-implemented,
  workflow-missing, too-few-steps, adapter-missing, no-adapters — 6 tests),
  validate.py (PermissionError on adapter read, unsupported verbs,
  conformance_report malformed registry — 3 tests), definitions.py
  (planned-entry fallback, specificity by group/slug/token, render-failure — 6
  tests), author.py (load_definition_file non-dict, _list_field list,
  rendered_definition_files not-in-registry — 5 tests), and low-gap modules
  (rows _group_title fallback, tables _latex_escape backslash, evals missing
  JSON, dashboard _verified_state absent/present, figures DOI truthy — 6 tests).

### Changed

- CI `--cov-fail-under` bumped from 94 to 97.
- Remaining docstrings added: `_expected_source_text`, `_payload` in evals.py;
  `_example_payload` in examples.py.
- Coverage: 98.21% -> 98.84%, tests: 847 -> 873.
- validate.py: 96.26% -> 97.66%, definitions.py: 96.09% -> 96.86%+.

## [1.6.0] - 2026-07-22

Coverage push to 98.21%, deep edge-case branch tests across all modules.

### Added

- **28 new tests** covering validate.py (`ValidationResult.warn`, `error`,
  `_safe_declared_path` absolute/parent-escape rejection), release_metadata
  (`_read_yaml`/`_read_json` non-mapping, license mismatch), examples
  (not-in-registry, repeated-titles, operational-misuse, missing/stale
  generated files), scenarios (route no-match), definitions
  (`load_definitions` missing-id/duplicate, specificity fallbacks), author
  (`_slug`, `_require`, `_list_field` fallback, `_quality_list`,
  `render_definition`/`rendered_definition_files` non-mapping), insights
  (doctor few-anti-criteria, empty-quality-field, missing-unsafe-redirect),
  assets_io (missing cover mirror), evals (stale source only).

### Changed

- Coverage: 97.60% -> 98.21%, tests: 819 -> 847.
- insights.py: 97.52% -> 99.65%.
- examples.py: 95.73% -> 97.65%+.
- scenarios.py: 96.63% -> 97%+.
- validate.py: 95.79% -> 96.26%+.

## [1.5.0] - 2026-07-22

Final coverage push to 97.60%, doctor quality-finding tests, assets_io drift tests.

### Added

- **12 new tests** for validate.py (missing adapter verbs, unsupported verbs via
  check_conformance, conformance_report with load failures), insights.py
  (_quality_findings for chain-of-thought, missing evidence/inference labels,
  missing unknown/alternative labels, sensitive-skill guardrail, doctor for
  few workflow steps and missing references), assets_io.py (invalid figure,
  stale cover mirror), and evals.py (stale generated file).

### Changed

- Coverage: 97.31% -> 97.60%, tests: 807 -> 819.
- insights.py coverage: 94.68% -> 97.52%.

## [1.4.0] - 2026-07-22

Coverage push to 97%+, resolve_root centralization, evals/examples branch tests.

### Added

- **17 new tests** for evals.py (`_section_from_obj` error paths, `_review_from_obj`
  sections/rubric validation, `_content_findings` group/kind/scenario mismatch,
  too-few sections) and examples.py (`_section_from_obj` and `_example_from_obj`
  error paths, rendered-skill-missing, too-few sections, output-not-named).
- **`core/locate.resolve_root(root)`** now used by all 8 consumer modules,
  replacing the duplicated `Path(root) if root is not None else project_root()`
  pattern in scenarios.py, evals.py, release_metadata.py, dashboard.py,
  examples.py, paths.py, config.py, and definitions.py.

### Changed

- Unused `project_root` imports removed from 7 modules that now use `resolve_root`.
- `src/cogsecskills/AGENTS.md` updated with `resolve_root` documentation.
- Coverage: 96.76% -> 97%+, tests: 790 -> 807.

## [1.3.0] - 2026-07-22

Coverage push to 96.76%, definitions.py and insights.py branch coverage,
resolve_root helper, AGENTS.md module map update.

### Added

- **27 new tests** covering definitions.py (`_field_or_default` fallback,
  `definition_from_skill` with empty workflow/anti-criteria, generic control
  detection, specificity checks, render-failure path), scenarios.py
  (answer-kind mismatch, rubric not-2, repeated titles, too-few sections,
  output-term-missing, quality-term-missing, output-term-missing-from-spec),
  and insights.py (`_is_sensitive_skill`, `_negative_controls_are_specific`,
  `_text_is_skill_specific`, `_tokens` edge cases).
- **`core/locate.resolve_root(root)`** — shared helper replacing the
  `Path(root) if root is not None else project_root()` pattern duplicated
  across 8+ modules.
- **`src/cogsecskills/AGENTS.md`** updated with full module-boundary map
  including new shared modules.

### Changed

- Coverage: 95.86% -> 96.76%, tests: 763 -> 790.
- `docs/architecture.md` already updated in v1.2.0; AGENTS.md now matches.

## [1.2.0] - 2026-07-22

Coverage push, CI hardening, docstrings, and documentation polish over v1.1.0.
All 12 validation gates remain green; the test suite grew from 740 to 763 tests
and coverage from 94.35% to 95.47%.

### Added

- **23 new tests** covering CLI dashboard/examples/evals/release-metadata
  `--check` failure paths, `list` with empty results and `--limit 0`,
  `author-batch` with failures, scenarios.py validation functions
  (`_expected_response_from_mapping`, `_answer_sections_from_obj`,
  `_rubric_scores_from_obj`, `_expected_answer_from_mapping`), and rows.py
  helper edge cases (`_first_containing`, `_first_with_prefix`, `_join`,
  `_first`, `_group_ids`).
- **Python 3.13** added to the CI matrix.
- **`--cov-fail-under=94`** added to the CI pytest step so coverage regressions
  fail the build.
- **Docstrings** added to 10 internal functions across `scenarios.py`,
  `evals.py`, and `examples.py`.
- **`docs/architecture.md`** updated to document the new `core/locate.py`,
  `core/quality_constants.py`, and `core/text_utils.py` modules.

### Changed

- `manuscript/S02_release_manifest.md` updated to v1.2.0 values (version,
  test counts, coverage, Python version, file counts, DOI status).
- `docs/cli.md` version example updated to 1.2.0.
- `ISA.md` progress line updated to v1.2.0.

## [1.1.0] - 2026-07-22

Comprehensive code-quality, test-coverage, and CLI-improvement pass over the
1.0.0 baseline. All 12 validation gates remain green; the test suite grew from
622 to 742 tests and coverage from 91.18% to 93.94%.

### Added

- **`--format json` for `list`, `groups`, and `route` CLI commands.** All three
  now emit machine-readable JSON alongside the default text format, enabling
  programmatic consumption and piping.
  - `list --format json` returns `{count, total, status_counts, skills[]}`.
  - `groups --format json` returns an array of `{id, title, count}`.
  - `route --format json` returns `{query, count, matches[{skill_id, name, group, score}]}`;
    in JSON mode, no matches returns exit `0` (not `1`).
- **`--limit N` for the `list` CLI command.** Caps the number of results after
  filtering, useful for quick previews or paginated consumption.
- **`core/quality_constants.py`** — shared quality-policy constants and
  normalization helpers extracted from the duplicated definitions in
  `quality/insights.py` and `authoring/definitions.py`, preventing drift.
- **Tests for `core/locate.py` and `core/quality_constants.py`** — covers
  project-root discovery (including the RuntimeError path when outside a
  project tree), quality-field-name completeness, sensitive-group contents,
  and the normalization helper.

### Changed

- **DRY: quality constants centralized.** The quality-field names, generic
  negative-control phrases, specificity/reuse field lists, allowed-shared
  items, sensitive groups/terms, and normalization function were duplicated
  verbatim between `quality/insights.py` and `authoring/definitions.py`. Both
  modules now import from `core/quality_constants.py`. The old private
  `_normalize_quality_item` / `_normalize_negative_control` helpers were
  removed in favor of the shared `normalize_quality_item`.
- **DRY: text utilities centralized.** The `_as_text()` and `_clean_cell()`
  helpers were duplicated verbatim between `artifacts/evals.py`,
  `artifacts/examples.py`, and `artifacts/manuscript_assets/rows.py`. All three
  now import from `core/text_utils.py`. Backward-compat aliases preserved.
- **Docstrings added** to 10 internal helper functions across `rows.py`
  (`_slug`, `_join`, `_first`, `_first_containing`, `_first_with_prefix`,
  `_group_ids`, `_group_title`).
- **TODO.md cleaned** — removed completed sections (Evidence Ladder, Harness
  Smoke Examples, Quickstart And Harness Cookbook, Quality Dashboard) per the
  forward-only convention; verified-state line updated to the latest test
  count and coverage.
- **Comprehensive test coverage lift.** Added 80 new tests across 5 new test
  files covering figures.py helpers (color mapping, text contrast, group
  summaries, vertical positioning, PNG signature, DOI reading), evals.py
  error paths (duplicate fixtures, wrong provenance/claim boundary, repeated
  titles, missing/extra fixtures), examples.py error paths (duplicate, wrong
  provenance, repeated titles, missing/extra skills), release_metadata.py
  branches (missing LICENSE, stale files, release-candidate dirty worktree,
  codemeta license mismatch, _has_doi edge cases), and scenarios.py
  validation (load error paths, _as_text_list edge cases, duplicate ids,
  missing required fields, invalid kind). Coverage rose from 91.21% to 93.88%;
  figures.py alone went from 11.56% to 98.35%.

- `CLAUDE.md` — Claude Code session guidance (defers to `AGENTS.md`; pins the
  generated-file boundary, gate sweep, and defensive contract).
- `docs/claude-code-skills.md` — installing the library as native Claude Code
  `/` skills by flattening `skills/` into `.claude/skills/cogsec-<slug>/`; linked
  from the docs map.
- `figures` optional-dependency extra (`matplotlib`, `numpy`, `seaborn`) so
  `manuscript-assets --write` figure rendering is reproducible. CI installs
  `.[dev,figures]` so the figure-asset tests run for real (no skips), and mypy
  gains a `follow_imports = skip` override for these third-party stubs so
  newer-Python stub syntax does not break the 3.10 type target.
- `manuscript/07_ethics_and_responsible_use.md` — standalone Ethics, Dual-Use,
  and Responsible-Use section (dual-use stance, defensive-by-contract-and-review,
  human-subjects scope, adopter responsibilities, and explicit non-claims).
- `manuscript/01_introduction.md` — a "Related Work and Positioning" subsection
  situating the library against the four cited literatures, grounded only in
  already-verified `references.bib` keys.
- Expanded `manuscript/98_symbols_glossary.md` from 4 to 11 terms (defensive
  boundary, misuse redirect, negative control, scenario fixture, worked example,
  reference density) and documented the `ageint_topic` crosswalk field.

### Fixed

- **CI/test suite now passes from a clean checkout.** Four artifact tests
  (`test_repository_examples_cover_all_rendered_skills`, three
  `test_release_metadata_*`) and the `examples`/`evals`/`dashboard`/
  `release-metadata`/`manuscript-assets` coherence gates assert against the
  gitignored `output/` tree, which a fresh clone lacks and nothing generated
  before pytest — so CI had been red since 2026-06-20 (4 failed / 618 passed on
  a clean runner). A session-scoped autouse fixture in `tests/conftest.py` now
  builds `output/` once when absent, making the suite self-contained; because
  pytest runs before the coherence-gate steps in the same CI job, the whole
  pipeline goes green (622 passed, all gates `current`). Idempotent — skipped
  when a populated `output/` already exists.
- Generated-file header attribution: `docs/evaluation-readiness.md` and
  `docs/skill-worked-examples.md` now correctly credit `evals --write` and
  `examples --write` (previously mislabeled `manuscript-assets --write`).
- `mypy` no longer aborts on the optional figure libraries' stubs when the
  `figures` extra is installed alongside `dev` (added a `tool.mypy` override).
- CI now enforces the full conformance contract: `.github/workflows/ci.yml`
  runs every generated-file drift gate (`definitions`, `scenarios`, `examples`,
  `evals`, `dashboard`, `release-metadata`, `manuscript-assets` `--check`), not
  just `validate`/`doctor`/`pytest`. Previously a hand-edit to a generated file
  could pass CI while failing the local gate sweep. Added a least-privilege
  `permissions: contents: read` block.

### Changed

- **Package and tests reorganized for modularity.** The flat 19-module runner is now
  grouped into cohesive subpackages along its (acyclic) dependency graph — `core/`
  (spec, registry, loader, config, harness), `authoring/` (author, scaffold, definitions),
  `quality/` (validate, insights), `artifacts/` (scenarios, examples, evals, dashboard,
  release_metadata, and the `manuscript_assets/` package) — with `cli.py` as the thin
  top-level interface. The 2,115-line `manuscript_assets.py` monolith was split into a
  package (`paths`, `rows`, `tables`, `figures`, `assets_io`) behind a façade `__init__`
  that re-exports the exact public API. Tests mirror the package layout
  (`tests/{core,authoring,quality,artifacts,contract,conformance}/`). Project-root
  discovery was centralized into `core.locate.project_root()` (a sentinel walk-up that
  fails loud), replacing 10 fragile `Path(__file__).parents[N]` magic-depths. Public CLI
  and import surfaces are unchanged; mypy/ruff clean, all validation/drift gates current.
- **Machine-stitched grammar repaired across all 100 skill definitions.** The
  `evidence_requirements`, `confidence_rubric`, `uncertainty_handling`,
  `privacy_legal_constraints`, and `failure_modes` quality fields had been generated by an
  earlier tool that spliced workflow step-titles and output/input names into sentences (e.g.
  "tie each sorted table, and outlier flags claim to concrete evidence from the specific
  evidence set, and sort dimensions item"), producing text that passed every gate but read as
  machine garble. Every definition now carries a grammatical, **skill-specific** rewrite of
  those fields, grounded in the technique's real outputs, failure modes, and evidence types
  (e.g. astroturfing cites creation-date spikes / content-hash overlap / follower-graph
  density; geolocation cites matched-terrain reference imagery and sun-angle computation),
  with per-skill uniqueness, keyword coverage, and scenario quality-term contracts preserved.
  The `author.default_quality_fields` fallback was also hardened to emit clean article-safe
  prose for any field a definition leaves unset.
- **Red-Team Review skill (`critical_review.red_team_review`) deepened and de-stitched.**
  Rewrote the canonical definition (source of truth → regenerated 6 skill files): removed the
  machine-stitched grammar that spliced workflow-step titles into the confidence rubric, failure
  modes, and evidence requirements; expanded the workflow from 5 to 6 operational steps (decomposed
  adversary model, attack-surface checklist with explicit coverage-gap flagging, assumption inversion
  + compounding attack chains, a 1–5 × 1–5 exploitability×impact scoring rubric with priority bands,
  mitigation re-testing against the adversary, and an explicit GO / NO-GO / GO-WITH-CONDITIONS call);
  grew anti-criteria from 5 to 10 (incl. a calibration guard that the scores and go/no-go are analyst
  estimates to be peer-checked, not objective measurement); distinguished Devil's Advocacy from
  structured Team A/Team B; added Shostack (2014) *Threat Modeling* and MITRE ATT&CK references.
  validate/doctor remain 0 errors / 0 findings.
- **Documentation deepened and manuscript supplements refreshed.** The 8 AGEINT educational
  primers (`docs/ageint/`) and the main explanatory docs (`architecture.md`, `authoring-skills.md`,
  `configuration.md`, `harness-cookbook.md`, `skill-contract.md`) were substantially deepened —
  each primer now maps its group to the real skills, and `adversarial-assurance.md` reflects the
  deepened red-team workflow (adversary modeling, attack-surface taxonomy, exploitability×impact
  scoring, go/no-go). All file-level documentation contracts and claim boundaries preserved.
  Generated manuscript supplements (`S10_skill_catalogue.md`, figures) and the quality dashboard
  were regenerated to reflect the cleaned skills, and the PDF/HTML manuscript was re-rendered.
- `QUICKSTART.md` documents the `figures` extra and includes
  `manuscript-assets --check` in the validation sweep.

## [0.1.0] — 2026-06-18

Initial release. A multiharness agentic skill library for Cognitive Security and
analytic tradecraft.

### Added

- **100 skill areas, all implemented** across 7 groups (Structured Analytic
  Techniques, Cognitive Security, Critical Review & Assurance, OSINT & Source
  Integrity, Counterintelligence & Deception, Information Environment, Research
  Methods), each a conforming multiharness skill folder (`SKILL.md` +
  `skill.yaml` + `workflow.md` + `harness/{claude,codex,hermes}.md`).
- **Runner package** `cogsecskills`: harness-neutral spec parser, registry,
  loader, multiharness conformance, validation gates, deterministic authoring
  renderer, scaffolder, and a thin CLI.
- **Deterministic authoring** (`author` / `author-batch`): renders conforming
  skills from a structured JSON definition; adapters bind every declared verb by
  construction.
- **Intelligent affordances**: `route` (free-text skill router), `stats`,
  `groups`, `catalogue` (generated index), `doctor` (validation + quality lint),
  `export`.
- **Configurable** via optional `cogsecskills.yaml`: target harness set (adding a
  harness needs no code change) and `doctor` quality thresholds.
- **AGEINT educational upstream** under `docs/ageint/` (index + 7 topic primers)
  and a full documentation set under `docs/`.
- Test suite with no mocks (real temp dirs + real YAML), ≥90% coverage gate (~98%
  actual), and a live conformance test that validates the real `skills/` tree.
- **Typed** package (`py.typed`, mypy-clean) and a `--version` flag.
- **GitHub Actions CI** — ruff (lint + format), mypy, pytest + coverage gate,
  `cogsecskills validate`, and `cogsecskills doctor` across Python 3.10–3.12.

### Notes

- The library is strictly defensive, educational, and accountable.
