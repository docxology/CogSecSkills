# CogSecSkills TODO

Forward-only tracker for source-owned work. Keep history in completed changelog
or commit messages; keep this file focused on the current state and next useful
work.

## Verified State (v1.6.0)

- Library gate: `validate` -> `0 error(s), 0 warning(s)`.
- Quality gate: `doctor` -> `validation: 0 error(s); quality: 0 finding(s)`.
- Definition gate: `definitions --check` -> `canonical definitions are current`.
- Scenario gate: `scenarios --check` -> `28 scenarios across 7 groups; 28 expected answers checked`.
- Example gate: `examples --check` -> `worked examples are current`.
- Eval gate: `evals --check` -> `offline evaluation fixtures are current`.
- Dashboard gate: `dashboard --check` -> `quality dashboard is current`.
- Release gate: `release-metadata --check` -> `release metadata is current (local mode)`.
- Manuscript gate: `manuscript-assets --check` -> `manuscript assets are current`.
- Test gate: `pytest tests/ --cov=src/cogsecskills` -> `847 passed`, `98.21% coverage`.
- Lint gate: `ruff check` + `ruff format --check` -> clean (69 files).
- Type gate: `mypy` -> `no issues found in 31 source files`.

## Ongoing Guardrails

- Keep verification prose aligned with the exact latest gate run after any source edits.
- Rerun `manuscript-assets --write` and `--check` after registry or skill metadata changes.
- Rerun `definitions --write` and `--check` after canonical skill-definition changes.
- Rerun `scenarios --check` after scenario fixture or quality-field changes.
- Rerun `examples --write` and `--check` after worked-example source changes.
- Preserve the defensive-only boundary; do not add offensive influence-operation playbooks.

## Minor: Coverage — examples.py (95.73%, 7 lines uncovered)

Lines 216-217, 239, 280-281, 285-286.

- **Line 216-217**: `_content_findings` path when `example.skill_id not in registry_ids` (continue branch) and `spec is None` (rendered-skill-missing continue branch). These are reached only when the example's skill_id is absent from the registry or has no on-disk spec — covered by `test_examples_not_in_registry` but the continue skips the rest of the loop body, leaving the downstream branches uncovered for that example. Fix: add a second example to the test fixture that is in the registry but has a missing spec, then assert the finding without needing the downstream branches.
- **Line 239**: `len(titles) != len(set(titles))` — repeated section titles. Covered by `test_examples_repeated_section_titles` calling `_content_findings` directly, but the test uses the first example whose skill_id maps to a spec, so the branch is reached. Verify the test is hitting `_content_findings` and not `check_examples` (which short-circuits on stale generated files).
- **Lines 280-281, 285-286**: `check_examples` generated-file missing/stale branches. Covered by `test_examples_check_missing_generated_json` and `test_examples_check_stale_generated_md`. Verify these tests are reaching the exact lines by ensuring `_expected_outputs` succeeds (needs a valid registry).

## Minor: Coverage — scenarios.py (96.63%, 7 lines uncovered)

Lines 369, 493, 504, 508, 519, 558, 562.

- **Line 369**: `_check_scenario_text` — unsafe scenario missing "unsafe"/"misuse" keyword. The test `test_check_scenarios_unsafe_without_redirect_keyword` covers the redirect-keyword check but not the unsafe-keyword check (it includes "unsafe" in the query). Fix: add a test with an unsafe scenario whose query says "force a conclusion" without "unsafe" or "misuse".
- **Line 493**: `_check_route` — expected skill not in top-10 route matches. The test `test_scenarios_route_no_match` covers this but the route may still match due to token overlap. Fix: use a query with zero token overlap to the skill's triggers.
- **Line 504**: `_check_spec_contract` — `spec.status != "implemented"`. Fix: create a scenario pointing to a `planned` skill on disk.
- **Line 508**: `_check_spec_contract` — workflow file missing. Fix: create a skill directory with no `workflow.md`.
- **Line 519**: `_check_spec_contract` — workflow has < 3 `## Step` headings. Fix: create a workflow with only 2 steps.
- **Line 558**: `_check_spec_contract` — adapter file missing. Fix: declare a harness adapter path but don't create the file.
- **Line 562**: `_check_spec_contract` — `spec.harness` is empty. Fix: create a spec with no harness map.

## Minor: Coverage — definitions.py (96.09%, 5 lines + 9 branches uncovered)

Lines 239, 284, 286, 298, 310, 319->317, 340->338, 465->472.

- **Line 239**: `_definitions_for_write` — registry entry that is in neither `existing` nor `specs` (a planned entry with no on-disk skill). Fix: seed a registry with a `planned` entry and no skill on disk, call `_definitions_for_write`.
- **Lines 284, 286**: `_negative_controls_are_specific` — `entry.group.lower() in negative_text` True path and `any(token ...)` fallback True path. Fix: call with a definition whose negative controls contain the group name but not the skill name/slug.
- **Lines 298, 310**: `_negative_control_item_is_specific` and `_quality_item_is_specific` — slug-phrase match and token-match fallback paths. Fix: call these functions directly with items containing the slug or a specificity token.
- **Line 465->472**: `check_definitions` — `rendered_definition_files` raises `AuthorError`/`SpecError`/`ValueError`. Fix: create a definition with an invalid tool verb that passes `load_definitions` but fails `rendered_definition_files`.

## Minor: Coverage — validate.py (96.26%, 7 lines uncovered)

Lines 156-158, 174-175, 294-295.

- **Lines 156-158**: `validate_skill` — `OSError` on `adapter_path.read_text()`. This path is reached only when `adapter_path.is_file()` returns True but `read_text()` raises. On macOS, `IsADirectoryError` is a subclass of `OSError`, but `is_file()` returns False for directories, so the "not found" branch fires first. Fix: use a mock or a file with permission bits set to 000 (chmod) so `is_file()` returns True but `read_text()` raises `PermissionError` (an `OSError` subclass).
- **Lines 174-175**: `validate_skill` — `check_conformance` returns `unsupported_verbs`. Fix: pass a `support` map where a harness can't realise a verb the skill uses, then call `validate_skill` with that harness set. Alternatively, call `check_conformance` directly (already covered by `test_validate_skill_unsupported_verbs`).
- **Lines 294-295**: `conformance_report` — `load_registry` raises `FileNotFoundError`/`SpecError`. Fix: create a tmp_path with a malformed `registry/skills.yaml` that raises on load, then call `conformance_report`.

## Minor: Coverage — author.py (96.86%, 3 lines + 5 branches uncovered)

Lines 140, 172, 595, 626->621, 657->650.

- **Line 140**: `load_definition_file` — `not isinstance(loaded, dict)` after YAML parse. Fix: create a YAML file containing a list, call `load_definition_file`.
- **Line 172**: `_list_field` — `isinstance(source, (list, tuple))` branch with items. Fix: call `_list_field` with a list source.
- **Line 595**: `rendered_definition_files` — `entry is None` (skill id not in registry). Fix: call `rendered_definition_files` with a definition whose `id` is not in the registry.
- **Lines 626->621, 657->650**: `author_batch` — `delete_defs` True/False and `promote` True/False branches. Fix: call `author_batch` with `delete_defs=False` and `promote=False`.

## Minor: Coverage — remaining low-gap modules

- **dashboard.py (98.64%)**: Line 60->68 (TODO section absent branch), 752 (check_dashboard finding for missing quality capsule). Fix: test `_read_verified_state` with a TODO that lacks "## Verified State", and test `check_dashboard` with a payload where a skill lacks a quality capsule.
- **figures.py (98.35%)**: Lines 348-352 (`_style_axes` with `grid_axis="other"` else branch), 687->686 (verb not in verb_index), 1444->1455 (cover DOI truthy branch). Fix: call `_style_axes` with `grid_axis="none"`, and test `_publication_doi` when a DOI is set in config.
- **rows.py (98.29%)**: Line 123 (`_group_title` fallback when group_id not found). Fix: call `_group_title` with a group_id not present in the rows.
- **tables.py (99.05%)**: Line 55 (`_latex_escape` with a backslash). Fix: call `_latex_escape` with a string containing `\\`.
- **loader.py (97.50%)**: Line 34 (`_project_root` called). This is the module-level function that delegates to `locate.project_root`. Covered indirectly by any test that calls `discover_skills()` without a root argument.
- **registry.py (99.10%)**: Line 26 (`_project_root` called). Same pattern as loader.
- **evals.py (99.27%)**: Lines 386-387 (`check_evals` missing generated file). Fix: delete the generated JSON after `write_evals`.

## Minor: Documentation Polish

- Update `docs/harness-installation.md` or `docs/harness-cookbook.md` with examples of `--format json` CLI usage for harness integration.
- Update `docs/README.md` to reference the new test files (10 test files added since v1.0.0).
- Add remaining docstrings: `_expected_source_text` and `_payload` in `evals.py`; `_example_payload` and `_render_markdown` in `examples.py`.

## Minor: CI Hardening

- Add Python 3.14 to the CI matrix once GitHub Actions supports it (currently 3.10-3.13).
- Bump `--cov-fail-under` from 94 to 97 to match the current coverage floor.

## Medium: Skill Definition Depth

- Audit all 100 canonical definitions for template-based boilerplate in `evidence_requirements`, `confidence_rubric`, `uncertainty_handling`, `privacy_legal_constraints`, and `failure_modes`. The `author.default_quality_fields` fallback uses a group-profile template — definitions that rely on it rather than providing skill-specific text should be deepened.
- Sample 10 definitions with the fewest references and assess whether more scholarly anchors should be added.
- Add a `doctor` check for definitions whose quality fields are identical to the `default_quality_fields` output (would flag template-only definitions).

## Medium: Manuscript Refresh

- Re-render the manuscript PDF from the live library after v1.6.0 changes. The `output/pdf/` and `output/web/` trees still reflect v0.1.0-era test counts (622, 90.94%) and version (0.1.0).
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

- The v1.0.0 Zenodo DOI exists (`10.5281/zenodo.20804586`). A v1.6.0 version DOI would require a new Zenodo deposit.
- Update `CITATION.cff` and `codemeta.json` with the new version DOI once deposited.
- Add verified external citations only when a manuscript claim needs external literature rather than project-local evidence.
