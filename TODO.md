# CogSecSkills TODO

Forward-only tracker for source-owned work. Keep history in completed changelog
or commit messages; keep this file focused on the current state and next useful
work.

## Verified State (v1.1.0)

- Library gate: `PYTHONPATH="src:." python -m cogsecskills validate` -> `0 error(s), 0 warning(s)`.
- Report gate: `PYTHONPATH="src:." python -m cogsecskills report` -> `registry_total: 100`, `implemented: 100`, `on_disk_skills: 100`, `ok: true`.
- Quality gate: `PYTHONPATH="src:." python -m cogsecskills doctor` -> `validation: 0 error(s); quality: 0 finding(s)`.
- Canonical definition gate: `PYTHONPATH="src:." python -m cogsecskills definitions --check` -> `canonical definitions are current`.
- Scenario gate: `PYTHONPATH="src:." python -m cogsecskills scenarios --check` -> `scenario readiness fixtures are current: 28 scenarios across 7 groups; 28 expected answers checked`.
- Worked-example gate: `PYTHONPATH="src:." python -m cogsecskills examples --check` -> `worked examples are current`.
- Dashboard gate: `PYTHONPATH="src:." python -m cogsecskills dashboard --check` -> `quality dashboard is current`.
- Manuscript asset gate: `PYTHONPATH="src:." python -m cogsecskills manuscript-assets --check` -> `manuscript assets are current`.
- Test gate: `PYTHONPATH="src:." python -m pytest tests/ --cov=src/cogsecskills --cov-report=term-missing` -> `763 passed`, `Total coverage: 95.47%`.

## Ongoing Guardrails

- Keep verification prose aligned with the exact latest gate run after any future source edits.
- Rerun `manuscript-assets --write` and `manuscript-assets --check` after registry or skill metadata changes.
- Rerun `definitions --write` and `definitions --check` after any canonical skill-definition change.
- Rerun `scenarios --check` after scenario fixtures, routing language, output contracts, or quality fields change.
- Rerun `examples --write` and `examples --check` after worked-example source changes.
- Preserve the defensive-only boundary; do not add offensive influence-operation playbooks.

## Minor: Coverage Polish

- **scenarios.py (90.87%)**: Add tests for `_expected_response_from_mapping` non-mapping error, `_answer_sections_from_obj` non-list/empty/missing-title-body, `_rubric_scores_from_obj` non-mapping, `check_scenarios` missing-kind-per-group edge cases, safe-scenario missing defensive keyword, unsafe missing redirect keyword, too-few include/exclude terms, repeated section labels.
- **definitions.py (88.27%)**: Add tests for `definition_from_skill` with empty workflow_steps, `_field_or_default` with falsy spec field, `_definition_quality_findings` for generic negative controls, `_reused_quality_field_findings` with empty field values, `check_definitions` render-failure error handling.
- **cli.py (91.38%)**: Add tests for `list` with `--limit 0`, `list` with filters returning no results, `dashboard --check` with stale files, `examples --check` with stale files, `evals --check` with stale files, `release-metadata --check` with stale files, `scaffold` with existing directory and no `--overwrite`.
- **rows.py (86.32%)**: Add tests for `_first_containing`, `_first_with_prefix` fallback paths, `_group_ids` with empty input, `collect_skill_rows` with missing spec (planned entry).
- **dashboard.py (97.74%)**: Cover lines 56, 60->68, 752.
- **insights.py (93.26%)**: Cover lines 171, 201, 218, 226, 273, 282, 295, 339, 362.

## Minor: CI Hardening

- Add Python 3.13 and 3.14 to the CI matrix in `.github/workflows/ci.yml`.
- Verify the `figures` extra installs cleanly on 3.13+ (matplotlib/seaborn compat).
- Add a `--cov-fail-under=94` to the pytest CI step so coverage regressions fail the build.

## Minor: Documentation Polish

- Update `docs/architecture.md` to document the new `core/quality_constants.py` and `core/text_utils.py` modules.
- Update `docs/harness-installation.md` or `docs/harness-cookbook.md` with examples of `--format json` CLI usage for harness integration.
- Update `src/cogsecskills/AGENTS.md` to reference the new shared modules.
- Add `core/text_utils.py` and `core/quality_constants.py` to the module map in `docs/architecture.md`.

## Minor: Code Quality Polish

- Add docstrings to remaining undocumented internal functions in `scenarios.py` (`_expected_response_from_mapping`, `_expected_answer_from_mapping`, `_check_scenario_text`, `_check_expected_response`, `_check_expected_answer`, `_check_route`, `_check_spec_contract`).
- Add docstrings to remaining undocumented internal functions in `evals.py` (`_review_text`, `_payload`, `_expected_source_text`, `_expected_outputs`, `_content_findings`).
- Add docstrings to remaining undocumented internal functions in `examples.py` (`_example_text`, `_example_payload`, `_expected_outputs`, `_content_findings`).
- Consider centralizing the `_project_root(root)` pattern (duplicated in 8+ modules) into a single `core/locate.resolve_root(root)` helper.

## Medium: Skill Definition Depth

- Audit all 100 canonical definitions for template-based boilerplate in `evidence_requirements`, `confidence_rubric`, `uncertainty_handling`, `privacy_legal_constraints`, and `failure_modes`. The `author.default_quality_fields` fallback uses a group-profile template — definitions that rely on it rather than providing skill-specific text should be deepened.
- Sample 10 definitions with the fewest references and assess whether more scholarly anchors should be added.
- Consider adding a `doctor` check for definitions whose quality fields are identical to the `default_quality_fields` output (would flag template-only definitions).

## Medium: Manuscript Refresh

- Re-render the manuscript PDF from the live library after v1.1.0 changes. The `output/pdf/` and `output/web/` trees still reflect v0.1.0-era test counts (622, 90.94%) and version (0.1.0).
- Re-run the template markdown validation and PDF render pipeline to bring `S02_release_manifest.md` into the combined PDF.
- Update the `CogSecSkills.pdf` top-level artifact after re-render.

## Medium: CLI Enhancements

- Add `--format json` to `stats` command (already outputs JSON but without a `--format` flag for consistency).
- Add `--format json` to `export` command (already outputs JSON but without a `--format` flag for consistency).
- Consider adding `--format json` to `validate` and `doctor` for machine-readable output.
- Consider adding `--limit N` to `route` (already exists — verify documented).

## Medium: AGEINT Docs

- Audit `docs/ageint/` primers for alignment with the current 100-skill taxonomy; add cross-references to new skills where relevant.
- Ensure each AGEINT primer names at least 3 concrete skills from its group.

## Major: Empirical Evaluation

- Add richer empirical validation only after scenario-output fixtures and claim boundaries are clear.
- Use `docs/analyst-output-review.md` as the initial rubric for exploratory internal review.
- Label any comparison against unstructured prompting as exploratory unless externally reviewed.
- Design a live-runtime eval harness that can call Claude/Codex/Hermes with scenario fixtures and score the outputs against the expected-answer rubric.

## Major: Live Connector Integrations

- Add connector-specific OSINT/web harness notes only when live connectors are intentionally wired.
- Require privacy/legal checks, source custody, rate-limit handling, and connector-specific tests before describing a connector as supported.
- Document the connector boundary in `docs/connector-boundaries.md` when a live connector is wired.

## Major: External Publication / DOI

- The v1.0.0 Zenodo DOI exists (`10.5281/zenodo.20804586`). A v1.1.0 version DOI would require a new Zenodo deposit.
- Update `CITATION.cff` and `codemeta.json` with the new version DOI once deposited.
- Add verified external citations only when a manuscript claim needs external literature rather than project-local evidence.
