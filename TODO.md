# CogSecSkills TODO

Forward-only tracker for source-owned work. Keep history in completed changelog
or commit messages; keep this file focused on the current state and next useful
work.

## Verified State

- Library gate: `PYTHONPATH="src:." python -m cogsecskills validate` -> `0 error(s), 0 warning(s)`.
- Report gate: `PYTHONPATH="src:." python -m cogsecskills report` -> `registry_total: 100`, `implemented: 100`, `on_disk_skills: 100`, `ok: true`.
- Quality gate: `PYTHONPATH="src:." python -m cogsecskills doctor` -> `validation: 0 error(s); quality: 0 finding(s)`.
- Canonical definition gate: `PYTHONPATH="src:." python -m cogsecskills definitions --check` -> `canonical definitions are current`.
- Scenario gate: `PYTHONPATH="src:." python -m cogsecskills scenarios --check` -> `scenario readiness fixtures are current: 28 scenarios across 7 groups; 28 expected answers checked`.
- Worked-example gate: `PYTHONPATH="src:." python -m cogsecskills examples --check` -> `worked examples are current`.
- Dashboard gate: `PYTHONPATH="src:." python -m cogsecskills dashboard --check` -> `quality dashboard is current`.
- Manuscript asset gate: `PYTHONPATH="src:." python -m cogsecskills manuscript-assets --check` -> `manuscript assets are current`.
- Test gate: `PYTHONPATH="src:." python -m pytest tests/test_cogsecskills_*.py tests/test_skill_library_conformance.py --cov=src/cogsecskills --cov-report=term-missing` -> `620 passed`, `Total coverage: 90.10%`.
- Template markdown gate: `uv run python -m infrastructure.validation.cli markdown projects/working/CogSecSkills/manuscript/` -> `No issues found!`.
- Template render gate: `uv run python scripts/03_render_pdf.py --project working/CogSecSkills` -> combined PDF and HTML generated, 13 manuscript sections, 8/8 figures found.

## Completed: Evidence Ladder

- `scenarios/defensive_readiness.yaml` now includes reviewed expected-answer bodies for all 28 scenarios.
- `scenarios --check` validates required sections, declared outputs, evidence/inference/gap labels, confidence and uncertainty language, refusal/redirect language, and absence of operational misuse phrasing.
- `examples/skill-worked-examples.yaml` now provides one source-owned deterministic worked example per skill.
- `examples --check` validates exact 100-skill coverage, local fixture provenance, defensive answer shape, declared outputs, generated Markdown/JSON freshness, and absence of operational misuse phrasing.
- The fixture set remains defensive and non-operational; it is not a live model or field-evaluation result.

## Completed: Harness Smoke Examples

- `examples/harness-smoke-transcripts.md` covers safe and unsafe fixtures for Codex, Claude, Hermes, and a custom harness.
- Every fixture names the harness, scenario id, selected skill, loaded files, expected bounded output, unsafe boundary, and local fixture provenance.
- Tests check default adapter paths exist and custom harness paths are documented as structural until reviewed for a real runtime.

## Completed: Quickstart And Harness Cookbook

- `QUICKSTART.md`, `docs/harness-installation.md`, and `docs/harness-cookbook.md` now cover validation, scenario checks, dashboard checks, and default/custom harness binding.
- Copy-paste snippets point at repository files and validation commands rather than implied live execution.
- Custom harness language remains structural until a real runtime adapter is reviewed.

## Completed: Quality Dashboard

- `python -m cogsecskills dashboard --write` generates `docs/quality-dashboard.md` and `output/data/quality_dashboard.json`.
- `dashboard --check` detects missing or stale dashboard files, missing 100-skill coverage, missing scenario coverage, missing worked-example coverage, missing quality capsules, and missing verified-state rows.
- The dashboard is a navigation and drift surface, not evidence of field effectiveness.

## Ongoing Guardrails

- Keep verification prose aligned with the exact latest gate run after any future source edits.
- Rerun `manuscript-assets --write` and `manuscript-assets --check` after registry or skill metadata changes.
- Rerun `definitions --write` and `definitions --check` after any canonical skill-definition change.
- Rerun `scenarios --check` after scenario fixtures, routing language, output contracts, or quality fields change.
- Rerun `examples --write` and `examples --check` after worked-example source changes.
- Preserve the defensive-only boundary; do not add offensive influence-operation playbooks.

## Deferred: Empirical Evaluation

- Add richer empirical validation only after scenario-output fixtures and claim boundaries are clear.
- Use `docs/analyst-output-review.md` as the initial rubric for exploratory internal review.
- Label any comparison against unstructured prompting as exploratory unless externally reviewed.

## Deferred: Live Connector Integrations

- Add connector-specific OSINT/web harness notes only when live connectors are intentionally wired.
- Require privacy/legal checks, source custody, rate-limit handling, and connector-specific tests before describing a connector as supported.

## Deferred: External Publication/DOI

- Add verified external citations only when a manuscript claim needs external literature rather than project-local evidence.
- Do not add DOI, release archive, public deployment, or peer-review claims until those artifacts exist.
