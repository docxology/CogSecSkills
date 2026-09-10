# TEST-07: Massive duplication between coverage-variant test files (same fixtures/asserts copied verbatim)

|Field|Value|
|---|---|
|Audit ID|`TEST-07`|
|Lens|`TEST`|
|Severity|`low`|
|Red-team verdict|`VALID`|
|Status|Open (validated 2026-09-10)|
| Tracking | PENDING-ISSUE-LINK |

## Summary
Coverage-variant test files duplicate topical tests verbatim: tests/quality/test_cogsecskills_edge_cases.py:141-171 copies the copytree-fixture + yaml-mutation + `_content_findings` sequence of tests/artifacts/test_cogsecskills_examples_branches.py:52-77; two identically-named `test_check_definitions_render_failure` twins carry the same 25-line YAML fixture; and `test_validate_skill_unsupported_verbs` re-tests what `test_unsupported_verbs_in_validate_skill` already covers. Copied fixtures mean a fixture bug or message-format change must be fixed in several places, and the clones already drift by accretion (the final_coverage twin adds a monkeypatched leg its sibling lacks). Nothing mitigates the duplication — no shared fixture, no conftest dedupe — so the copies add maintenance cost with zero added defect detection.

## Evidence
- tests/quality/test_cogsecskills_edge_cases.py:141-171 — `def test_examples_not_in_registry(tmp_path):` / `def test_examples_repeated_section_titles(tmp_path):` both inline `for d in ("registry", "skills", "examples"): shutil.copytree(...)` + `write_examples` + yaml mutation + `_content_findings`, duplicating tests/artifacts/test_cogsecskills_examples_branches.py:52-77 `test_check_examples_duplicate` / `test_check_examples_repeated_section_titles` (same mutations `raw["examples"][0]["skill_id"]` and `raw["examples"][0]["sections"][1]["title"] = ...[0]["title"]`, same asserts).
- tests/authoring/test_cogsecskills_author_defs_coverage.py (~135-190) `test_check_definitions_render_failure` carries the identical 25-line `bad.yaml` fixture as tests/authoring/test_cogsecskills_definitions_branches.py (~257-300) `test_check_definitions_render_failure`, both ending `assert len(findings) > 0`.
- tests/quality/test_cogsecskills_final_coverage.py:67-70 `test_validate_skill_unsupported_verbs` first leg (`check_conformance(spec, support=narrow, harnesses=("claude",))` → `assert conf["claude"].unsupported_verbs == (ToolVerb.READ,)`) duplicates tests/quality/test_cogsecskills_validate_coverage.py:56-70 `test_unsupported_verbs_in_validate_skill`.

## Impact
A fixture bug or message-format change must be fixed in every copy; pytest collects both twins, doubling maintenance with no added defect detection. The real divergence between clones is drift by accretion: final_coverage's unsupported-verbs test adds a monkeypatched `validate_skill` leg absent from its twin (near-clones diverging over time — the claimed hazard, though the original 'why' cited a different, imprecise instance: both render-failure twins assert only `len(findings) > 0` and the examples twins assert the same substrings). Verb-narrowing is also covered independently at tests/quality/test_cogsecskills_harness_validate.py:254+, so the coverage-clone copies add no unique detection.

## Remediation
1. Keep one canonical test per behavior in the topical file — examples behaviors in tests/artifacts/test_cogsecskills_examples_branches.py, definitions render-failure in tests/authoring/test_cogsecskills_definitions_branches.py — and delete the coverage-clone copies at tests/quality/test_cogsecskills_edge_cases.py:141-171 and tests/authoring/test_cogsecskills_author_defs_coverage.py (~135-190).
2. Delete tests/quality/test_cogsecskills_final_coverage.py:67-70 `test_validate_skill_unsupported_verbs` — the behavior is covered by tests/quality/test_cogsecskills_validate_coverage.py:56-70 and independently by tests/quality/test_cogsecskills_harness_validate.py:254+.
3. While deduping, resolve the twins to the stronger assertion (see TEST-02 for the vacuous `len(findings) > 0` pins).

## Audit trail
- Discovered by the TEST lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `VALID`, confidence `high`.
- Verifier notes: All three duplication claims confirmed by direct read of cited files. Nothing mitigates: no shared fixture/helper across the pairs (edge_cases inlines the copytree loop; branches file has _copy_fixture), no conftest dedupe, and twins live in separate files so pytest collects both. Minor correction to the 'why': the drift example is imprecise — both render-failure twins assert only `len(findings) > 0` (no divergence there), and the examples twins assert the same message substrings; the real divergence is that final_coverage's unsupported-verbs test adds a monkeypatched validate_skill leg absent from its twin (near-clones drifting by accretion — the claimed hazard, just not the cited instance). Also confirmed tests/quality/test_cogsecskills_harness_validate.py:254+ covers verb-narrowing independently, so coverage-clone copies add no unique defect detection. Severity low (test hygiene/maintenance only, no shipped behavior) is correct.
<!-- PR and issue links are added to the Tracking field after filing. -->