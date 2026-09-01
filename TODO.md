# CogSecSkills TODO

Forward-only tracker for source-owned work. Keep history in completed changelog
or commit messages; keep this file focused on the current state and next useful
work.

## Verified State (v1.7.0)

- Library gate: `validate` -> `0 error(s), 0 warning(s)`.
- Quality gate: `doctor` -> `validation: 0 error(s); quality: 0 finding(s)`.
- Definition gate: `definitions --check` -> `canonical definitions are current`.
- Scenario gate: `scenarios --check` -> `28 scenarios across 7 groups; 28 expected answers checked`.
- Example gate: `examples --check` -> `worked examples are current`.
- Eval gate: `evals --check` -> `offline evaluation fixtures are current`.
- Dashboard gate: `dashboard --check` -> `quality dashboard is current`.
- Release gate: `release-metadata --check` -> `release metadata is current (local mode)`.
- Manuscript gate: `manuscript-assets --check` -> `manuscript assets are current`.
- Test gate: `pytest --cov=cogsecskills --cov-fail-under=97` -> `899 passed`, `99.91% coverage`.
- Lint gate: `ruff check` + `ruff format --check` -> clean (82 files).
- Type gate: `mypy` -> `no issues found in 38 source files` (requires the `dev` extra: `uv sync --extra dev` installs `types-pyyaml`; a bare env reports 11 `import-untyped` errors for `yaml` — the dev extra is the supported invocation).

## Resolved (2026-08-30 review pass)

- `ruff format` drift fixed in
  `src/cogsecskills/artifacts/manuscript_assets/figure_cover.py` (one stray
  blank line); `ruff format --check` now fully clean.
- All "Verified State" numbers re-measured live on this checkout.

## Ongoing Guardrails


- Keep verification prose aligned with the exact latest gate run after any source edits.
- Rerun `manuscript-assets --write` and `--check` after registry or skill metadata changes.
- Rerun `definitions --write` and `--check` after canonical skill-definition changes.
- Rerun `scenarios --check` after scenario fixture or quality-field changes.
- Rerun `examples --write` and `--check` after worked-example source changes.
- Preserve the defensive-only boundary; do not add offensive influence-operation playbooks.

## Minor: Coverage

- Maintain 99.9%+ test coverage across all modules (`examples.py`, `scenarios.py`, `definitions.py`, `validate.py`, `author.py`, `dashboard.py`, `evals.py`, `figure_helpers.py`, `tables.py`, `loader.py`, `registry.py` all at 99%+ to 100%).
- Ensure any newly authored utility or artifact renderer includes full branch coverage fixtures.

## Minor: Documentation Polish

- Resolved 2026-08-31: `docs/harness-installation.md` now documents `--format
  json` for `validate`/`doctor` with verified output payloads; `tests/README.md`
  now describes the per-concern test packages, conventions, and coverage gates.

## Minor: CI Hardening

- Add Python 3.14 to the CI matrix once GitHub Actions supports it (currently 3.10-3.13).
- Maintain CI `--cov-fail-under=97` (or raise to 99%) in `.github/workflows/ci.yml`.

## Medium: Skill Definition Depth

- Audit all 100 canonical definitions periodically for potential domain deepening in evidence requirements and uncertainty handling.
- Expand scholarly anchors and reference density across emerging intelligence literature.

## Medium: Manuscript Refresh

- Re-render the manuscript PDF from the live library after v1.7.0 updates.
- Re-run template markdown validation and PDF render pipeline to update PDF artifacts.

## Medium: CLI Enhancements

- `--format json` added to `validate` and `doctor` (2026-08-30): machine-readable
  CI diagnostics with failure-path payload tests; documented in `docs/cli.md`.
- `stats` and `export` are already JSON-native (no `--format` flag needed);
  `list`, `route`, and `groups` already accept `--format json`.

## Medium: AGEINT Docs

- Verified 2026-08-30: each group primer in `docs/ageint/` names many concrete
  skills from its group inline (e.g. `cognitive-security.md` names 20+ of 24);
  cross-references are active. Periodically re-audit against the 100-skill
  taxonomy as definitions deepen.

## Major: Empirical Evaluation

- Design a live-runtime eval harness capable of invoking Claude/Codex/Hermes with scenario fixtures and scoring outputs against expected-answer rubrics.
- Use `docs/analyst-output-review.md` as the initial rubric for offline and online review.
- Label any comparison against unstructured prompting as exploratory unless externally reviewed.

## Major: Live Connector Integrations

- Add connector-specific OSINT/web harness notes only when live connectors are intentionally wired.
- Require privacy/legal checks, source custody, rate-limit handling, and connector-specific tests before describing a connector as supported.
- Document the connector boundary in `docs/connector-boundaries.md` when a live connector is wired.

## Major: External Publication / DOI

- Update `CITATION.cff` and `codemeta.json` with new version DOI once deposited on Zenodo.
- Add verified external citations only when a manuscript claim needs external literature rather than project-local evidence.
