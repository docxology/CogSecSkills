# TEST-01: CONTRIBUTING.md's 'No mocks in tests' rule violated by monkeypatching that fakes real behavior in 6 files

|Field|Value|
|---|---|
|Audit ID|`TEST-01`|
|Lens|`TEST`|
|Severity|`medium`|
|Red-team verdict|`ADJUSTED`|
|Status|Open (validated 2026-09-10)|
| Tracking | [GitHub issue](https://github.com/docxology/CogSecSkills/issues/47) |

## Summary
CONTRIBUTING.md declares the ground rule "**No mocks in tests.** Real `tmp_path` directories and real YAML.", yet six test files monkeypatch the very validation and exception surfaces they claim to cover (e.g. `check_conformance`, `discover_skills`, `_expected_outputs`, `rendered_definition_files`, `_publication_doi`). These stubs prove the code catches a synthetic error, not that the real pipeline produces one, so the self-declared rule is not honored by its own suite. Red team adjusted severity from high to medium because the blast radius is limited to test-suite honesty and coverage inflation — nothing wrong or misleading ships to users — and tests/AGENTS.md actually narrows the rule to project data ("No mocks for project data"), with CONTRIBUTING.md's blanket prohibition still contradicted in spirit.

## Evidence
CONTRIBUTING.md (Ground rules):

> '**No mocks in tests.** Real `tmp_path` directories and real YAML.'

All cited stubs confirmed at current line numbers:

- tests/quality/test_cogsecskills_final_coverage.py:106-110

```python
mp.setattr("cogsecskills.quality.validate.check_conformance", lambda *args, **kwargs: mock_conf,)
```

  (`mock_conf` built at ~101-104 from a real `HarnessConformance` object)
- tests/quality/test_cogsecskills_validate_coverage.py:92-97

```python
mp.setattr("cogsecskills.quality.validate.discover_skills", lambda *args, **kwargs: (_ for _ in ()).throw(FileNotFoundError("skills missing")))
```

- tests/artifacts/test_cogsecskills_examples_branches.py:154-157 — monkeypatch of `cogsecskills.artifacts.examples._expected_outputs` to raise.
- tests/quality/test_cogsecskills_lowgap_coverage.py:74-78 (`artifacts.evals._expected_outputs` -> `ValueError('synthetic error in _expected_outputs')`) and 125-129 (`figure_cover._publication_doi` -> constant `'10.5281/zenodo.20804585'`).
- tests/authoring/test_cogsecskills_definitions_branches.py:364-368 — `rendered_definition_files` -> throw `SpecError('synthetic rendering failure')`.

## Impact
The repo's own CONTRIBUTING.md and tests/AGENTS.md declare the contract "enforced, not conventional" and forbid mocks; these tests stub out the surfaces they claim to cover, so they prove a `try/except` catches a synthetic throw rather than that the real pipeline raises one. The DOI stub at lowgap 125-129, for example, tests nothing about real DOI resolution. Coverage is inflated: the suite claims error-path coverage that a real input would not exercise. Mitigating facts: real-failure coverage does exist for some surfaces (see Remediation), and the contract gates (`validate`/`doctor`/`coverage`) still run against the real tree, so no wrong results ship to users.

## Remediation
Replace the stubs with real failure fixtures the way existing tests already do — tests/quality/test_cogsecskills_validate_coverage.py:39-53 `test_adapter_permission_error` uses a real chmod-000 fixture, and `test_conformance_report_malformed_registry` (same file, ~70-90) uses real malformed YAML. Concretely:

1. tests/quality/test_cogsecskills_final_coverage.py:101-110 — build the conformance-failure scenario through the real `check_conformance` on a fixture that genuinely violates a rule, instead of injecting a hand-built `mock_conf`.
2. tests/quality/test_cogsecskills_validate_coverage.py:92-97 — point `discover_skills` at a real directory that is missing/empty so `FileNotFoundError` arises naturally.
3. tests/artifacts/test_cogsecskills_examples_branches.py:154-157 — write a real broken examples file so `_expected_outputs` fails on genuine content, not a synthetic raise.
4. tests/quality/test_cogsecskills_lowgap_coverage.py:74-78 — replace the `_expected_outputs` synthetic `ValueError` with a real malformed fixture; 125-129 — replace the constant-DOI stub with a fixture that exercises real DOI resolution (or delete the test if no real path exists).
5. tests/authoring/test_cogsecskills_definitions_branches.py:364-368 — write a real malformed definition so the render path fails on genuine content; delete or rewrite the monkeypatched branches otherwise.

## Audit trail
- Discovered by the TEST lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `ADJUSTED`, confidence `high`.
- Verifier notes: Checked: (1) all quotes/lines verified verbatim — no fabrication. (2) The finding's own fix reference exists: tests/quality/test_cogsecskills_validate_coverage.py:39-53 `test_adapter_permission_error` uses a real chmod-000 fixture, and test_conformance_report_malformed_registry (same file, ~70-90) uses real malformed YAML — so real-failure coverage exists for SOME surfaces, but the six monkeypatched branches are stub-only. (3) Mitigating context the finding overweights: tests/AGENTS.md states the rule as 'No mocks for project data. Use real tmp_path repositories, real YAML...' — a data-mock prohibition; the monkeypatches stub internal functions/exceptions rather than project data. CONTRIBUTING.md's blanket 'No mocks in tests' is still contradicted in spirit: the stubbed tests prove a try/except catches a synthetic throw, not that the real pipeline raises one (e.g. the DOI stub at lowgap 125-129 tests nothing about real DOI resolution). (4) Re-derived reasoning: the violation is real and the self-declared rule is not honored, but blast radius is limited to test-suite honesty/coverage inflation — nothing wrong or misleading ships to users, the contract gates (validate/doctor/coverage) still run against the real tree. 'High' (broken contract or misleading claim) overstates it; 'medium' (real defect, limited blast radius) fits. Wording correction: tests/AGENTS.md itself narrows the rule to project data, so the 'contract is enforced, not conventional' framing applies to the skill contract, not the mock rule.
<!-- PR and issue links are added to the Tracking field after filing. -->
