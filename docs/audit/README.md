# Red-Team Audit Reports — 2026-09-10

Deep red-team audit of the CogSecSkills package: evaluation methodology and
scoring validity, runner correctness, test-suite quality, documentation drift,
registry consistency, and reproducibility/CI/artifact integrity. One report per
validated finding in this folder; each finding's GitHub issue is linked in its
file's **Tracking** row, and every issue links back here.

| Field | Value |
|---|---|
| Scope | `src/` runner + quality/eval methodology, `tests/`, `docs/`, `registry/`+`definitions/`, CI/metadata/artifacts |
| Method | 6 independent discovery lenses -> 53 findings -> adversarial red-team re-verification of every finding |
| Result | **51 validated findings** (1 high, 20 medium, 30 low); 2 refuted and dropped; 1 advisory folded into the index |
| PR | PENDING-PR-LINK |
| Date | 2026-09-10 |

Severity reflects the red-team-adjusted value. The two critical-severity
discoveries were adjusted to high/medium after verification confirmed the
repo's claim-boundary disclaimers prevent wrong results from shipping; the
defects remain real (circular fixtures, tautological rubric gate) and are
tracked for repair.

## Validated findings

### Evaluation methodology & scoring validity (8)

| Finding | Severity | Verdict | Title |
|---|---|---|---|
| [`EVAL-01`](EVAL-01-eval-fixtures-machine-generated-very-expected-answers-they.md) | high | ADJUSTED | Eval fixtures are machine-generated from the very expected answers they 'review' (same-source circularity) |
| [`EVAL-02`](EVAL-02-rubric-scoring-tautological-gate-fails-unless-every-dimension.md) | medium | ADJUSTED | Rubric scoring is tautological: the gate fails unless every dimension scores the maximum 2 |
| [`EVAL-03`](EVAL-03-grader-reduces-substring-presence-fixture-s-own-text.md) | medium | ADJUSTED | 'Grader' reduces to substring presence in the fixture's own text; rubric dimensions are not measurable in code |
| [`EVAL-04`](EVAL-04-router-validation-circular-scenario-queries-were-authored-route.md) | medium | ADJUSTED | Router 'validation' is circular: scenario queries were authored to route, and routing is only checked against the author's own expectation |
| [`EVAL-05`](EVAL-05-reviewed-local-fixture-provenance-has-review-process-behind.md) | medium | ADJUSTED | 'Reviewed local fixture' provenance has no review process behind it; selection is 1:1 authored self-consistent fixtures (survivorship) |
| [`EVAL-07`](EVAL-07-hardcoded-28-fixture-constant-presented-coverage-metric.md) | low | VALID | Hardcoded '28 fixture' constant presented as a coverage metric |
| [`EVAL-08`](EVAL-08-scenario-expected-response-contract-never-checked-against-expected.md) | low | ADJUSTED | Scenario expected_response contract is never checked against the expected answer that supposedly satisfies it |
| [`EVAL-09`](EVAL-09-stale-contradictory-statistical-claims-across-documentation-coverage-test.md) | low | VALID | Stale and contradictory statistical claims across documentation (coverage %, test counts, score matrix presentation) |

### Runner correctness (15)

| Finding | Severity | Verdict | Title |
|---|---|---|---|
| [`CORE-01`](CORE-01-generated-skill-md-front-matter-embeds-unescaped-registry.md) | medium | VALID | Generated SKILL.md front matter embeds unescaped registry summary, producing invalid YAML for entries whose summary contains ': ' |
| [`CORE-03`](CORE-03-author-batch-s-per-item-exception-tuple-too.md) | medium | VALID | author_batch's per-item exception tuple is too narrow; a malformed _def.json aborts the whole batch with a raw traceback instead of the promised failed-report |
| [`CORE-04`](CORE-04-render-definition-writes-definition-fields-tags-triggers-inputs.md) | medium | VALID | render_definition writes definition fields (tags/triggers/inputs/outputs) without validation, so authored skills can fail SkillSpec parsing while the author command exits 0 |
| [`CORE-05`](CORE-05-skillspec-mapping-str-coerces-harness-version-values-harness.md) | medium | VALID | SkillSpec.from_mapping str()-coerces harness and version values: `harness: {claude: null}` becomes the adapter path 'None' and passes the conformance has_adapter check |
| [`CORE-02`](CORE-02-documented-usage-scaffold-skill-id-root-path-work.md) | low | ADJUSTED | Documented usage `scaffold <skill-id> [--root PATH]` cannot work: --root is registered only on the top-level parser |
| [`CORE-06`](CORE-06-str-list-strips-list-items-returns-single-string.md) | low | VALID | _as_str_list strips list items but returns the single-string form unstripped |
| [`CORE-07`](CORE-07-load-config-bool-coerces-require-references-quoted-false.md) | low | VALID | load_config bool()-coerces require_references, so quoted `"false"` silently becomes true |
| [`CORE-08`](CORE-08-load-registry-raises-typeerror-instead-specerror-skills-empty.md) | low | VALID | load_registry raises TypeError instead of SpecError when `skills:` is empty/null |
| [`CORE-09`](CORE-09-definition-path-definition-skill-unpack-split-1-two.md) | low | VALID | definition_path / definition_from_skill unpack `split('.', 1)` into two variables and crash with an opaque ValueError on a dot-less id |
| [`CORE-10`](CORE-10-catalogue-output-writes-without-creating-parent-directories.md) | low | VALID | `catalogue --output` writes without creating parent directories |
| [`CORE-11`](CORE-11-list-limit-accepts-negative-integers-silently-returns-all.md) | low | VALID | `list --limit` accepts negative integers and silently returns all-but-last-N rows |
| [`CORE-12`](CORE-12-load-config-str-coerces-harness-list-entries-null.md) | low | VALID | load_config str()-coerces harness list entries: null/number elements become harness names 'None'/'3' |
| [`CORE-13`](CORE-13-promote-implemented-regex-surgery-silently-ops-registry-formatting.md) | low | VALID | promote_to_implemented regex surgery silently no-ops when registry formatting drifts |
| [`CORE-14`](CORE-14-duplicate-yaml-keys-silently-last-wins-every-spec.md) | low | ADJUSTED | Duplicate YAML keys are silently last-wins in every spec/config/registry load path |
| [`CORE-15`](CORE-15-discover-skills-tolerates-duplicate-skill-ids-disk-unlike.md) | low | VALID | discover_skills tolerates duplicate skill ids on disk (unlike the registry, which raises), and dict-based consumers silently drop one |

### Test-suite quality (10)

| Finding | Severity | Verdict | Title |
|---|---|---|---|
| [`TEST-01`](TEST-01-contributing-md-s-mocks-tests-rule-violated-monkeypatching.md) | medium | ADJUSTED | CONTRIBUTING.md's 'No mocks in tests' rule violated by monkeypatching that fakes real behavior in 6 files |
| [`TEST-02`](TEST-02-vacuous-tautological-assertions-tests-only-check-doesn-t.md) | medium | ADJUSTED | Vacuous/tautological assertions: tests that only check 'it doesn't crash' or 'list is non-empty' |
| [`TEST-03`](TEST-03-hard-coded-catalogue-totals-100-28-7-8.md) | medium | VALID | Hard-coded catalogue totals (100/28/7/8) pinned in many tests — silent drift pins acknowledged in CONTRIBUTING but spread across 5+ files |
| [`TEST-04`](TEST-04-cwd-dependent-live-tree-tests-use-path-cwd.md) | medium | VALID | CWD-dependent live-tree tests use Path.cwd() — order/environment-sensitive |
| [`TEST-05`](TEST-05-chmod-000-permission-test-root-unsafe-environment-dependent.md) | medium | VALID | chmod-000 permission test is root-unsafe and environment-dependent |
| [`TEST-06`](TEST-06-coverage-driven-test-files-assert-implementation-lines-constants.md) | medium | ADJUSTED | Coverage-driven test files assert implementation lines and constants, not behavior |
| [`TEST-07`](TEST-07-massive-duplication-between-coverage-variant-test-files-same.md) | low | VALID | Massive duplication between coverage-variant test files (same fixtures/asserts copied verbatim) |
| [`TEST-08`](TEST-08-contract-tests-pin-exact-doc-prose-heading-inventory.md) | low | ADJUSTED | Contract tests pin exact doc prose and heading inventory — high churn coupling |
| [`TEST-09`](TEST-09-cli-output-asserted-via-substring-json-fragments-order.md) | low | ADJUSTED | CLI output asserted via substring JSON fragments — order/format-coupled |
| [`TEST-10`](TEST-10-coverage-gaps-negative-path-tests-missing-registry-config.md) | low | ADJUSTED | Coverage gaps: negative-path tests missing for registry/config edge interactions exercised only via happy path in live conformance |

### Documentation accuracy (6)

| Finding | Severity | Verdict | Title |
|---|---|---|---|
| [`DOCS-01`](DOCS-01-docs-harness-cookbook-md-references-non-existent-skill.md) | medium | ADJUSTED | docs/harness-cookbook.md references a non-existent skill id counterintelligence.elicitation_resistance |
| [`DOCS-04`](DOCS-04-claude-md-misstates-ci-coverage-gate-90-ci.md) | medium | VALID | CLAUDE.md misstates the CI coverage gate as >=90% when CI enforces 97 |
| [`DOCS-07`](DOCS-07-cli-md-calls-implementation-modules-sibling-modules-omits.md) | low | ADJUSTED | cli.md calls the implementation modules 'sibling modules' and omits four commands from the cli.py module summary |
| [`DOCS-08`](DOCS-08-docs-readme-md-gives-incomplete-regeneration-command-docs.md) | low | ADJUSTED | docs/README.md gives an incomplete regeneration command for docs/catalogue.md |
| [`DOCS-09`](DOCS-09-isa-md-constraint-still-describes-private-sidecar-layout.md) | low | VALID | ISA.md constraint still describes the private-sidecar layout that no longer exists |
| [`DOCS-10`](DOCS-10-readme-md-renders-two-example-links-without-separator.md) | low | ADJUSTED | README.md renders two example links without a separator |

### Registry/definitions consistency (3)

| Finding | Severity | Verdict | Title |
|---|---|---|---|
| [`REG-01`](REG-01-malformed-official-doc-url-autogen-profile-doubled-slash.md) | low | VALID | Malformed official_doc_url for autogen profile (doubled slash) |
| [`REG-02`](REG-02-registryentry-obj-coerces-required-keys-str-contradicting-spec.md) | low | VALID | RegistryEntry.from_obj coerces required keys with str(), contradicting the spec layer's explicit anti-coercion policy |
| [`REG-03`](REG-03-group-vocabulary-enforcement-silently-degrades-groups-yaml-absent.md) | low | VALID | Group-vocabulary enforcement silently degrades when groups.yaml is absent |

### Reproducibility, CI & release metadata (9)

| Finding | Severity | Verdict | Title |
|---|---|---|---|
| [`REPRO-01`](REPRO-01-zenodo-json-version-1-0-0-drifts-1.md) | medium | VALID | .zenodo.json version (1.0.0) drifts from the 1.7.0 declared everywhere else, and the drift gate cannot see it |
| [`REPRO-02`](REPRO-02-citation-cff-uses-invalid-cff-version-version-doi.md) | medium | VALID | CITATION.cff uses an invalid cff-version and a version DOI mislabeled for the wrong release |
| [`REPRO-03`](REPRO-03-release-claim-matrix-hard-codes-doi-status-contradicts.md) | medium | VALID | Release claim matrix hard-codes a DOI status that contradicts the files it reads |
| [`REPRO-04`](REPRO-04-figure-drift-gate-detect-semantic-staleness-100-skills.md) | medium | ADJUSTED | Figure drift gate cannot detect semantic staleness; '100 skills' is hard-coded in figure code |
| [`REPRO-05`](REPRO-05-ci-enforces-gates-contributor-docs-never-mention-docs.md) | low | ADJUSTED | CI enforces gates the contributor docs never mention; docs mention a gate CI does not run |
| [`REPRO-06`](REPRO-06-coverage-gate-numbers-conflict-across-pyproject-contributing-ci.md) | low | ADJUSTED | Coverage gate numbers conflict across pyproject, CONTRIBUTING, and CI |
| [`REPRO-07`](REPRO-07-release-metadata-check-never-enforces-clean-worktree-requirement.md) | low | ADJUSTED | release-metadata --check never enforces the clean-worktree requirement in CI |
| [`REPRO-08`](REPRO-08-committed-generated-surface-includes-raw-latex-build-byproducts.md) | low | VALID | Committed generated surface includes raw LaTeX build byproducts with no provenance manifest |
| [`REPRO-09`](REPRO-09-pyproject-comment-claims-pandas-figures-extra.md) | low | VALID | pyproject comment claims pandas is in the figures extra; it is not |

## Refuted / not filed

- **EVAL-06** (claim-boundary phrase-check bypass) — refuted by verification: the fixture set is
  byte-pinned to generator output by `check_evals`, so a live-transcript paste fails the staleness gate; the property is already enforced.
- **REPRO-10** (mypy/CI-leg matrix risk) — refuted as speculative; no defect demonstrated.
- **REG-04** (registry/definitions/skills consistency sweep) — **no defect found**: 100 registry rows ↔ 100 definitions ↔ 100 rendered skills, no duplicates, all statuses/verbs in vocabulary, all ageint targets present. Advisory: the `stub`/`planned` lifecycle states are exercised by zero production rows; cover them with a synthetic fixture test.

Cross-lens duplicates were merged before filing (DOCS-02→REPRO-02, DOCS-03→REPRO-01, DOCS-04→REPRO-06 context, DOCS-05/06→EVAL-09).

## Method notes

- Discovery: six read-only lens agents deep-read their surfaces and returned evidence-backed findings (`file:line` + verbatim quotes).
- Red team: every finding was independently re-verified by a fresh adversarial agent instructed to refute it; verdicts: 29 VALID, 22 ADJUSTED (severity/line corrections applied), 2 INVALID (dropped).
- Every finding's file carries the full verifier notes in its *Audit trail* section.

