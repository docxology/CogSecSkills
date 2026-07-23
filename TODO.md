# CogSecSkills TODO

Forward-only tracker for source-owned work. Keep history in completed changelog
or commit messages; keep this file focused on the current state and next useful
work.

## Verified State (v1.2.0)

- Library gate: `PYTHONPATH="src:." python -m cogsecskills validate` -> `0 error(s), 0 warning(s)`.
- Report gate: `PYTHONPATH="src:." python -m cogsecskills report` -> `registry_total: 100`, `implemented: 100`, `on_disk_skills: 100`, `ok: true`.
- Quality gate: `PYTHONPATH="src:." python -m cogsecskills doctor` -> `validation: 0 error(s); quality: 0 finding(s)`.
- Canonical definition gate: `PYTHONPATH="src:." python -m cogsecskills definitions --check` -> `canonical definitions are current`.
- Scenario gate: `PYTHONPATH="src:." python -m cogsecskills scenarios --check` -> `scenario readiness fixtures are current: 28 scenarios across 7 groups; 28 expected answers checked`.
- Worked-example gate: `PYTHONPATH="src:." python -m cogsecskills examples --check` -> `worked examples are current`.
- Dashboard gate: `PYTHONPATH="src:." python -m cogsecskills dashboard --check` -> `quality dashboard is current`.
- Manuscript asset gate: `PYTHONPATH="src:." python -m cogsecskills manuscript-assets --check` -> `manuscript assets are current`.
- Test gate: `PYTHONPATH="src:." python -m pytest tests/ --cov=src/cogsecskills --cov-report=term-missing` -> `763 passed`, `Total coverage: 95.86%`.

## Ongoing Guardrails

- Keep verification prose aligned with the exact latest gate run after any future source edits.
- Rerun `manuscript-assets --write` and `manuscript-assets --check` after registry or skill metadata changes.
- Rerun `definitions --write` and `definitions --check` after any canonical skill-definition change.
- Rerun `scenarios --check` after scenario fixtures, routing language, output contracts, or quality fields change.
- Rerun `examples --write` and `examples --check` after worked-example source changes.
- Preserve the defensive-only boundary; do not add offensive influence-operation playbooks.

## Minor: Coverage Polish — definitions.py (88.27%)

Uncovered lines: 92, 94, 144-152, 163, 239, 271, 284, 286, 296-299, 308-311, 319->317, 340->338, 408, 416, 465->472, 486-489.

- **`_field_or_default` (lines 144-152)**: The fallback path when a spec field is falsy, constructing a `RegistryEntry` and calling `default_quality_fields`. Test: create a spec with empty `evidence_requirements` and verify the default is returned.
- **`definition_from_skill` empty workflow_steps (lines 92, 94)**: When `_workflow_steps` returns empty, the fallback step is used. Test: create a spec whose workflow.md has no `## Step N` headings.
- **`definition_from_skill` empty anti_criteria (line 163)**: When `_anti_criteria` returns empty, a default is used. Test: spec whose workflow has no Anti-criteria heading.
- **`_definitions_for_write` entry not in existing or specs (line 239)**: When a registry entry has no definition and no on-disk spec. Test: registry entry marked `planned` with no skill on disk.
- **`_negative_controls_are_specific` fallback paths (lines 271, 284, 286)**: The paths that check `entry.group.lower() in negative_text` and the `any(token ...)` fallback. Test: definition with group-name in negative controls but not skill name/slug.
- **`_negative_control_item_is_specific` fallback (lines 296-299, 308-311)**: Same logic but per-item. Test: individual negative-control item with group-level specificity.
- **`_definition_quality_findings` generic controls check (line 408)**: When `GENERIC_NEGATIVE_CONTROL_PHRASES` is found in negative controls. Test: definition with a generic phrase.
- **`_definition_quality_findings` specificity check (line 416)**: When quality fields lack skill-specific language. Test: definition with generic confidence_rubric.
- **`check_definitions` render-failure path (lines 465->472, 486-489)**: When `rendered_definition_files` raises. Test: definition with an invalid tool verb.

## Minor: Coverage Polish — scenarios.py (94.23%)

Uncovered lines: 369, 424, 440, 447, 451, 453, 493, 504, 508, 519, 558, 562.

- **`_check_scenario_text` unsafe-redirect missing keyword (line 369)**: The `unsafe` / `misuse` not-in-lower path for unsafe scenarios. Test: unsafe scenario query that says "force a conclusion" without "unsafe" or "misuse".
- **`_check_expected_response` output-term-missing path (line 424)**: When no expected output term is in the response text. Test: scenario with output terms that are absent from expected_response.
- **`_check_expected_answer` answer-kind mismatch (line 440)**: When `answer.answer_kind != expected_kind`. Test: safe scenario with `refusal_redirect` answer kind.
- **`_check_expected_answer` rubric-score-not-2 (line 447)**: When a rubric score is not 2. Test: scenario with `skill_fit: 1`.
- **`_check_expected_answer` repeated titles (line 451)**: When section titles repeat. Test: answer with two sections titled "A".
- **`_check_expected_answer` too-few sections (line 453)**: When fewer than 3 sections. Test: answer with 2 sections.
- **`_check_route` no match (line 493)**: When expected skill is not in top-10. Test: scenario referencing a skill that doesn't match the query tokens.
- **`_check_spec_contract` not-implemented (line 504)**: When `spec.status != "implemented"`. Test: scenario pointing to a `planned` skill.
- **`_check_spec_contract` workflow missing (line 508)**: When workflow file doesn't exist. Test: skill directory with no workflow.md.
- **`_check_spec_contract` too-few steps (line 519)**: When workflow has < 3 steps. Test: workflow with 2 `## Step` headings.
- **`_check_spec_contract` adapter missing (line 558)**: When an adapter file is missing. Test: skill with a harness declared but no adapter file.
- **`_check_spec_contract` no adapters declared (line 562)**: When `spec.harness` is empty. Test: spec with no harness map.

## Minor: Coverage Polish — evals.py (93.45%) and examples.py (91.94%)

- **evals.py lines 70, 79, 83, 86, 91**: `_section_from_obj` and `_review_from_obj` error paths (non-mapping section, missing title/body). Test: eval entry with a non-mapping section.
- **evals.py line 290**: Duplicate evaluation fixture detection. Test: two reviews with the same scenario_id.
- **evals.py line 308**: Wrong answer kind. Test: review with `defensive_output` for an unsafe scenario.
- **evals.py lines 381-382, 386-387**: `check_evals` missing/stale generated file. Test: delete or corrupt the generated markdown.
- **examples.py lines 58, 67, 71**: `_section_from_obj` and `_example_from_obj` error paths. Test: example with non-mapping section.
- **examples.py lines 216-217, 224**: Duplicate and missing-from-registry detection. Test: two examples with same skill_id.
- **examples.py line 239**: Repeated section titles. Test: example with duplicate section titles.
- **examples.py lines 280-281, 285-286**: `check_examples` missing/stale generated file. Test: delete the generated JSON.

## Minor: Coverage Polish — insights.py (93.26%)

Uncovered lines: 171, 201, 218, 226, 273, 282, 295, 339, 362.

- **Line 171**: `doctor` finding for fewer-than-min workflow steps. Test: spec with 2-step workflow.
- **Line 201**: Empty quality field detection. Test: spec with empty `defensive_boundary`.
- **Lines 218, 226**: Chain-of-thought wording and missing unsafe/redirect coverage. Test: spec with "chain-of-thought" in negative controls.
- **Lines 273, 282**: Evidence/inference and unknown/alternative label checks. Test: spec with evidence_requirements missing "inference".
- **Line 295**: Sensitive-skill guardrail check. Test: spec in `cognitive_security` group missing "authorized" in quality text.
- **Lines 339, 362**: `_negative_controls_are_specific` and `_text_is_skill_specific` fallback paths. Test: spec whose negative controls contain only group name, not skill name.

## Minor: Coverage Polish — dashboard.py (98.64%) and remaining modules

- **dashboard.py line 60->68, 752**: `_dashboard_payload` branch and `write_dashboard` return path.
- **assets_io.py lines 66, 74**: `check_assets` stale cover mirror and stale figure.
- **tables.py line 55**: `_latex_escape` edge case.
- **validate.py lines 71, 156-158, 174-175, 294-295**: `_adapter_bound_verbs` OSError and `validate_library` registry-load-failure paths.

## Minor: Documentation Polish

- Update `docs/harness-installation.md` or `docs/harness-cookbook.md` with examples of `--format json` CLI usage for harness integration.
- Update `src/cogsecskills/AGENTS.md` to reference the new shared modules (`core/quality_constants.py`, `core/text_utils.py`).
- Update `docs/README.md` to reference the new test files.

## Minor: Code Quality Polish

- Centralize the `_project_root(root)` pattern (duplicated in 8+ modules as `Path(root) if root is not None else project_root()`) into a single `core/locate.resolve_root(root)` helper. Each consuming module would import and call `resolve_root(root)` instead of defining its own `_project_root`.
- Add docstrings to remaining undocumented functions: `_expected_source_text` and `_payload` in `evals.py`, `_example_payload` and `_render_markdown` in `examples.py`, `_render_markdown` in `evals.py`.

## Minor: CI Hardening

- Add Python 3.14 to the CI matrix once GitHub Actions supports it (currently 3.10-3.13).
- Verify the `figures` extra installs cleanly on 3.14 (matplotlib/seaborn compat).

## Medium: Skill Definition Depth

- Audit all 100 canonical definitions for template-based boilerplate in `evidence_requirements`, `confidence_rubric`, `uncertainty_handling`, `privacy_legal_constraints`, and `failure_modes`. The `author.default_quality_fields` fallback uses a group-profile template — definitions that rely on it rather than providing skill-specific text should be deepened.
- Sample 10 definitions with the fewest references and assess whether more scholarly anchors should be added.
- Add a `doctor` check for definitions whose quality fields are identical to the `default_quality_fields` output (would flag template-only definitions).

## Medium: Manuscript Refresh

- Re-render the manuscript PDF from the live library after v1.2.0 changes. The `output/pdf/` and `output/web/` trees still reflect v0.1.0-era test counts (622, 90.94%) and version (0.1.0).
- Re-run the template markdown validation and PDF render pipeline to bring `S02_release_manifest.md` into the combined PDF.
- Update the `CogSecSkills.pdf` top-level artifact after re-render.

## Medium: CLI Enhancements

- Add `--format json` to `stats` command for consistency (already outputs JSON but lacks the `--format` flag).
- Add `--format json` to `export` command for consistency (already outputs JSON but lacks the `--format` flag).
- Consider adding `--format json` to `validate` and `doctor` for machine-readable output.

## Medium: AGEINT Docs

- Audit `docs/ageint/` primers for alignment with the current 100-skill taxonomy; add cross-references to new skills where relevant.
- Ensure each AGEINT primer names at least 3 concrete skills from its group.

## Major: Empirical Evaluation

- Design a live-runtime eval harness that can call Claude/Codex/Hermes with scenario fixtures and score the outputs against the expected-answer rubric.
- Use `docs/analyst-output-review.md` as the initial rubric for exploratory internal review.
- Label any comparison against unstructured prompting as exploratory unless externally reviewed.

## Major: Live Connector Integrations

- Add connector-specific OSINT/web harness notes only when live connectors are intentionally wired.
- Require privacy/legal checks, source custody, rate-limit handling, and connector-specific tests before describing a connector as supported.
- Document the connector boundary in `docs/connector-boundaries.md` when a live connector is wired.

## Major: External Publication / DOI

- The v1.0.0 Zenodo DOI exists (`10.5281/zenodo.20804586`). A v1.2.0 version DOI would require a new Zenodo deposit.
- Update `CITATION.cff` and `codemeta.json` with the new version DOI once deposited.
- Add verified external citations only when a manuscript claim needs external literature rather than project-local evidence.
