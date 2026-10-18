# Audit remediation, 2026-10-18

This current review is separate from the dated 2026-09-10 audit. Its original
head is `f2c15ca4bce17d1f8b58bd9f02b1b4f98b4c04be`; that immutable history is
preserved. Original quoted source and verdicts describe that historical snapshot.

The table records source repairs or a bounded current disposition for every
one of the 51 filed findings. Publication and issue closure require the exact
candidate gates; this local document alone does not establish a main merge.

Authored fixtures are not independent evaluations. No live harness benchmark,
field-effectiveness result, release, or archive is created by this repair.

Local followup runtime qualification:1291 tests passed at99.54% coverage; Ruff and
mypy51 source files passed. The 99% floor is unchanged. Final generated-file,
installed-wheel qualification is recorded in `audit-controls-acceptance-20261018.json`;
hosted gates must qualify the published head before main integration.
The fresh71-page PDF retains all100 catalogue identifiers and was visually
reviewed after repairing clipped commands; see [render acceptance](audit-controls-render-acceptance-20261018.json).

These source repairs address all51 dispositions, including the four followups
(#30,#52,#54,#56). Issue closure is handled by qualified main publication; this
document is not a live GitHub issue inventory. The preceding47-finding
acceptance remains an immutable dated source snapshot. Its runtime or render
receipts are not silently refreshed by these later changes. See
[the test-layout membership](audit-controls-layout-20261018.json).

## Individual dispositions

### CORE-01

[Issue #6](https://github.com/docxology/CogSecSkills/issues/6) — **prior repair verified**.

Front matter uses YAML scalar escaping and is parsed in a real render regression.

Evidence: [`src/cogsecskills/authoring/author.py`](../src/cogsecskills/authoring/author.py), [`tests/authoring/test_cogsecskills_author.py`](../tests/authoring/test_cogsecskills_author.py).

### CORE-02

[Issue #7](https://github.com/docxology/CogSecSkills/issues/7) — **repaired**.

Documented --root before the subcommand, matching argparse; no unsupported trailing-global-option promise.

Evidence: [`src/cogsecskills/cli.py`](../src/cogsecskills/cli.py), [`tests/authoring/test_cogsecskills_cli_scaffold.py`](../tests/authoring/test_cogsecskills_cli_scaffold.py).

### CORE-03

[Issue #8](https://github.com/docxology/CogSecSkills/issues/8) — **prior repair verified**.

Definition loading wraps read/parse errors and rejects non-mappings before setdefault; compatibility batch returns a per-file failure.

Evidence: [`src/cogsecskills/authoring/author.py`](../src/cogsecskills/authoring/author.py), [`tests/authoring/test_authoring_boundaries.py`](../tests/authoring/test_authoring_boundaries.py).

### CORE-04

[Issue #9](https://github.com/docxology/CogSecSkills/issues/9) — **prior repair verified**.

Authoring preflights definition fields, the actual SkillSpec parser and every output before writing.

Evidence: [`src/cogsecskills/authoring/author.py`](../src/cogsecskills/authoring/author.py), [`tests/authoring/test_authoring_boundaries.py`](../tests/authoring/test_authoring_boundaries.py).

### CORE-05

[Issue #10](https://github.com/docxology/CogSecSkills/issues/10) — **prior repair verified**.

Non-text harness paths and numeric versions are rejected, while documented optional null defaults remain explicit.

Evidence: [`src/cogsecskills/core/spec.py`](../src/cogsecskills/core/spec.py), [`tests/core/test_cogsecskills_spec_nulls.py`](../tests/core/test_cogsecskills_spec_nulls.py).

### CORE-06

[Issue #11](https://github.com/docxology/CogSecSkills/issues/11) — **prior repair verified**.

Scalar and sequence strings both strip whitespace; the real YAML regression verifies the scalar result.

Evidence: [`src/cogsecskills/core/spec.py`](../src/cogsecskills/core/spec.py), [`tests/core/test_input_boundaries.py`](../tests/core/test_input_boundaries.py).

### CORE-07

[Issue #12](https://github.com/docxology/CogSecSkills/issues/12) — **prior repair verified**.

require_references requires a real bool; quoted false/null are source-labeled errors.

Evidence: [`src/cogsecskills/core/config.py`](../src/cogsecskills/core/config.py), [`tests/core/test_input_boundaries.py`](../tests/core/test_input_boundaries.py).

### CORE-08

[Issue #13](https://github.com/docxology/CogSecSkills/issues/13) — **prior repair verified**.

Registry collection shapes raise source-labeled SpecError for null/bool/scalar/mapping values.

Evidence: [`src/cogsecskills/core/registry.py`](../src/cogsecskills/core/registry.py), [`tests/core/test_input_boundaries.py`](../tests/core/test_input_boundaries.py).

### CORE-09

[Issue #14](https://github.com/docxology/CogSecSkills/issues/14) — **prior repair verified**.

Shared skill_components validates group/slug and path containment before definition destinations are constructed.

Evidence: [`src/cogsecskills/authoring/definitions.py`](../src/cogsecskills/authoring/definitions.py), [`tests/authoring/test_authoring_boundaries.py`](../tests/authoring/test_authoring_boundaries.py).

### CORE-10

[Issue #15](https://github.com/docxology/CogSecSkills/issues/15) — **prior repair verified**.

Catalogue output creates its parents; the CLI regression writes a real nested path.

Evidence: [`src/cogsecskills/cli.py`](../src/cogsecskills/cli.py), [`tests/authoring/test_cogsecskills_cli_additions.py`](../tests/authoring/test_cogsecskills_cli_additions.py).

### CORE-11

[Issue #16](https://github.com/docxology/CogSecSkills/issues/16) — **prior repair verified**.

Negative result limits fail rather than becoming negative Python slices.

Evidence: [`src/cogsecskills/cli.py`](../src/cogsecskills/cli.py), [`tests/authoring/test_cli_error_paths.py`](../tests/authoring/test_cli_error_paths.py).

### CORE-12

[Issue #17](https://github.com/docxology/CogSecSkills/issues/17) — **prior repair verified**.

Harness entries are validated as safe nonempty unique text components, not coerced from null/numbers.

Evidence: [`src/cogsecskills/core/config.py`](../src/cogsecskills/core/config.py), [`tests/core/test_input_boundaries.py`](../tests/core/test_input_boundaries.py).

### CORE-13

[Issue #18](https://github.com/docxology/CogSecSkills/issues/18) — **prior repair verified**.

Promotion rejects unmatched/already-implemented rows and leaves the registry unchanged on failure.

Evidence: [`src/cogsecskills/authoring/author.py`](../src/cogsecskills/authoring/author.py), [`tests/authoring/test_cogsecskills_promote_strict.py`](../tests/authoring/test_cogsecskills_promote_strict.py).

### CORE-14

[Issue #19](https://github.com/docxology/CogSecSkills/issues/19) — **prior repair verified**.

Shared strict YAML reader rejects duplicate mappings including merge ambiguity; actual source-file regressions exercise boundaries.

Evidence: [`src/cogsecskills/core/yaml_io.py`](../src/cogsecskills/core/yaml_io.py), [`tests/core/test_input_boundaries.py`](../tests/core/test_input_boundaries.py).

### CORE-15

[Issue #20](https://github.com/docxology/CogSecSkills/issues/20) — **prior repair verified**.

Discovery rejects duplicate on-disk skill identifiers and external source symlinks.

Evidence: [`src/cogsecskills/core/loader.py`](../src/cogsecskills/core/loader.py), [`tests/core/test_input_boundaries.py`](../tests/core/test_input_boundaries.py).

### DOCS-01

[Issue #21](https://github.com/docxology/CogSecSkills/issues/21) — **prior repair verified**.

Cookbook names the actual SKILL.md, workflow.md and harness adapter paths; transcript files are checked on disk.

Evidence: [`docs/harness-cookbook.md`](../docs/harness-cookbook.md), [`tests/contract/test_cogsecskills_docs_contract.py`](../tests/contract/test_cogsecskills_docs_contract.py).

### DOCS-04

[Issue #22](https://github.com/docxology/CogSecSkills/issues/22) — **prior repair verified**.

CLAUDE, contributor, package and CI floors agree at 99%.

Evidence: [`CLAUDE.md`](../CLAUDE.md), [`tests/contract/test_cogsecskills_docs_contract.py`](../tests/contract/test_cogsecskills_docs_contract.py).

### DOCS-07

[Issue #23](https://github.com/docxology/CogSecSkills/issues/23) — **repaired**.

CLI reference and module docstring identify real concern packages and include evals and release metadata owners.

Evidence: [`docs/cli.md`](../docs/cli.md), [`tests/contract/test_cogsecskills_agents_contract.py`](../tests/contract/test_cogsecskills_agents_contract.py).

### DOCS-08

[Issue #24](https://github.com/docxology/CogSecSkills/issues/24) — **repaired**.

The docs index gives the complete catalogue write command, including --output.

Evidence: [`docs/README.md`](../docs/README.md), [`tests/contract/test_cogsecskills_docs_contract.py`](../tests/contract/test_cogsecskills_docs_contract.py).

### DOCS-09

[Issue #25](https://github.com/docxology/CogSecSkills/issues/25) — **prior repair verified**.

ISA constraints name the canonical public repository and the sibling template as a rendering dependency. Historical log entries remain dated history.

Evidence: [`ISA.md`](../ISA.md), [`tests/contract/test_cogsecskills_agents_contract.py`](../tests/contract/test_cogsecskills_agents_contract.py).

### DOCS-10

[Issue #26](https://github.com/docxology/CogSecSkills/issues/26) — **prior repair verified**.

README example links are separated in the current reader flow.

Evidence: [`README.md`](../README.md), [`tests/contract/test_cogsecskills_docs_contract.py`](../tests/contract/test_cogsecskills_docs_contract.py).

### EVAL-01

[Issue #27](https://github.com/docxology/CogSecSkills/issues/27) — **repaired**.

Generated mirrors are explicitly authored answer keys; copying them is not an independent evaluation. No fabricated review is added.

Evidence: [`src/cogsecskills/artifacts/evals.py`](../src/cogsecskills/artifacts/evals.py), [`tests/artifacts/test_fixture_provenance.py`](../tests/artifacts/test_fixture_provenance.py).

### EVAL-02

[Issue #28](https://github.com/docxology/CogSecSkills/issues/28) — **repaired**.

Removed all-2 self-ratings and passing-score claims. Loaded and direct-API authored fixtures reject attached scores; schema v2 records zero measured scores.

Evidence: [`src/cogsecskills/artifacts/evals.py`](../src/cogsecskills/artifacts/evals.py), [`tests/artifacts/test_fixture_provenance.py`](../tests/artifacts/test_fixture_provenance.py).

### EVAL-03

[Issue #29](https://github.com/docxology/CogSecSkills/issues/29) — **repaired**.

Generated and authored docs explicitly limit checks to headings and vocabulary presence; independent scoring is a separate future protocol.

Evidence: [`docs/analyst-output-review.md`](../docs/analyst-output-review.md), [`tests/artifacts/test_fixture_provenance.py`](../tests/artifacts/test_fixture_provenance.py).

### EVAL-04

[Issue #30](https://github.com/docxology/CogSecSkills/issues/30) — **implemented in followup; qualified publication required**.

Name-free authored paraphrase, distractor and noninformative controls exposed grammatical-token domination. Corpus rarity and stop-word filtering repair those regressions while preserving integer scores and exact-ID priority. These are authored software controls, not independent routing accuracy.

Evidence: [`src/cogsecskills/quality/insights.py`](../src/cogsecskills/quality/insights.py), [`tests/quality/test_routing_paraphrases.py`](../tests/quality/test_routing_paraphrases.py), [`tests/fixtures/routing_paraphrases.yaml`](../tests/fixtures/routing_paraphrases.yaml).

### EVAL-05

[Issue #31](https://github.com/docxology/CogSecSkills/issues/31) — **repaired**.

Canonical example and answer-key provenance says authored; no nonexistent review event is asserted. Rendered manuscript/docs/data are synchronized.

Evidence: [`examples/skill-worked-examples.yaml`](../examples/skill-worked-examples.yaml), [`tests/artifacts/test_fixture_provenance.py`](../tests/artifacts/test_fixture_provenance.py).

### EVAL-07

[Issue #32](https://github.com/docxology/CogSecSkills/issues/32) — **prior repair verified and count oracles repaired**.

Production counts derive from loaded scenarios; independent source-count expectations replace replicated 28 literals in generated-report tests.

Evidence: [`src/cogsecskills/artifacts/evals.py`](../src/cogsecskills/artifacts/evals.py), [`tests/artifacts/test_response_contracts.py`](../tests/artifacts/test_response_contracts.py).

### EVAL-08

[Issue #33](https://github.com/docxology/CogSecSkills/issues/33) — **prior repair verified**.

Required sections/terms and excluded terms are checked against answer bodies only; provenance/request metadata cannot satisfy contracts.

Evidence: [`src/cogsecskills/artifacts/response_contract.py`](../src/cogsecskills/artifacts/response_contract.py), [`tests/artifacts/test_response_contracts.py`](../tests/artifacts/test_response_contracts.py).

### EVAL-09

[Issue #34](https://github.com/docxology/CogSecSkills/issues/34) — **repaired**.

Current local measurements are dated and separate from immutable historical release receipts; fixture reports no longer display rubric pass scores.

Evidence: [`TODO.md`](../TODO.md), [`tests/artifacts/test_fixture_provenance.py`](../tests/artifacts/test_fixture_provenance.py).

### REG-01

[Issue #35](https://github.com/docxology/CogSecSkills/issues/35) — **repaired**.

Removed the doubled path slash; the canonical AutoGen documentation URL was opened successfully on 2026-10-18.

Evidence: [`registry/harness_profiles.yaml`](../registry/harness_profiles.yaml), [`tests/contract/test_cogsecskills_docs_contract.py`](../tests/contract/test_cogsecskills_docs_contract.py).

### REG-02

[Issue #36](https://github.com/docxology/CogSecSkills/issues/36) — **prior repair verified**.

Required registry keys must be actual nonempty strings; null/numeric identifiers are not coerced.

Evidence: [`src/cogsecskills/core/registry.py`](../src/cogsecskills/core/registry.py), [`tests/core/test_cogsecskills_registry_yaml_robustness.py`](../tests/core/test_cogsecskills_registry_yaml_robustness.py).

### REG-03

[Issue #37](https://github.com/docxology/CogSecSkills/issues/37) — **repaired**.

validate_library rejects an absent or empty group vocabulary, retaining lightweight loader compatibility without silently dropping validation. Both controls fail on baseline.

Evidence: [`src/cogsecskills/quality/validate.py`](../src/cogsecskills/quality/validate.py), [`tests/quality/test_validation_boundaries.py`](../tests/quality/test_validation_boundaries.py).

### REPRO-01

[Issue #38](https://github.com/docxology/CogSecSkills/issues/38) — **prior repair verified**.

Current package, citation, CodeMeta, manuscript and Zenodo metadata version checks agree; original deposits remain historical identities.

Evidence: [`src/cogsecskills/artifacts/release_metadata.py`](../src/cogsecskills/artifacts/release_metadata.py), [`tests/artifacts/test_cogsecskills_release_metadata.py`](../tests/artifacts/test_cogsecskills_release_metadata.py).

### REPRO-02

[Issue #39](https://github.com/docxology/CogSecSkills/issues/39) — **prior repair verified**.

CFF schema-version and DOI normalization are separate from software version; current metadata is checked against source.

Evidence: [`CITATION.cff`](../CITATION.cff), [`tests/artifacts/test_cogsecskills_release_metadata.py`](../tests/artifacts/test_cogsecskills_release_metadata.py).

### REPRO-03

[Issue #40](https://github.com/docxology/CogSecSkills/issues/40) — **prior repair verified**.

DOI claim rows derive from normalized declared metadata, not a hardcoded absence claim; declaration is not network/archive identity verification.

Evidence: [`src/cogsecskills/artifacts/release_metadata.py`](../src/cogsecskills/artifacts/release_metadata.py), [`tests/artifacts/test_cogsecskills_release_metadata.py`](../tests/artifacts/test_cogsecskills_release_metadata.py).

### REPRO-04

[Issue #41](https://github.com/docxology/CogSecSkills/issues/41) — **repaired**.

Atlas title and catalogue heading use len(rows); figure metadata names registry skills instead of a frozen numeric count. A two-row real fixture renders a two-skill heading. Pixel/source equivalence remains explicitly outside the structural drift gate.

Evidence: [`src/cogsecskills/artifacts/manuscript_assets/tables.py`](../src/cogsecskills/artifacts/manuscript_assets/tables.py), [`tests/artifacts/test_cogsecskills_manuscript_assets.py`](../tests/artifacts/test_cogsecskills_manuscript_assets.py).

### REPRO-05

[Issue #42](https://github.com/docxology/CogSecSkills/issues/42) — **prior repair verified**.

Contributor/source gate commands include all generated coherence checks and isolated-wheel validation; tag policy adds explicit runtime release checks.

Evidence: [`CONTRIBUTING.md`](../CONTRIBUTING.md), [`tests/contract/test_cogsecskills_docs_contract.py`](../tests/contract/test_cogsecskills_docs_contract.py).

### REPRO-06

[Issue #43](https://github.com/docxology/CogSecSkills/issues/43) — **prior repair verified**.

Package default, contributor and CI coverage floors are 99%; current measurement does not change the required floor.

Evidence: [`pyproject.toml`](../pyproject.toml), [`tests/contract/test_cogsecskills_docs_contract.py`](../tests/contract/test_cogsecskills_docs_contract.py).

### REPRO-07

[Issue #44](https://github.com/docxology/CogSecSkills/issues/44) — **repaired**.

v* tags run local coherence plus --check-policy --mode release-candidate before builds; real clean/dirty/unversioned Git controls exercise the policy without rewriting local projection bytes.

Evidence: [`src/cogsecskills/artifacts/release_metadata.py`](../src/cogsecskills/artifacts/release_metadata.py), [`tests/artifacts/test_cogsecskills_release_metadata.py`](../tests/artifacts/test_cogsecskills_release_metadata.py).

### REPRO-08

[Issue #45](https://github.com/docxology/CogSecSkills/issues/45) — **repaired**.

Ten tracked compiler intermediates are removed from the candidate index and ignored. Prior bytes are preserved outside the source and in Git history. The current source gets a fresh pinned-SDK render and composition/acceptance receipt; final PDF/HTML deliverables remain tracked.

Evidence: [`.gitignore`](../.gitignore), [`docs/manuscript/05_reproducibility.md`](../docs/manuscript/05_reproducibility.md).

### REPRO-09

[Issue #46](https://github.com/docxology/CogSecSkills/issues/46) — **repaired**.

The figures-extra comment lists only its actual matplotlib/numpy/seaborn dependencies.

Evidence: [`pyproject.toml`](../pyproject.toml), [`tests/artifacts/test_cogsecskills_figures.py`](../tests/artifacts/test_cogsecskills_figures.py).

### TEST-01

[Issue #47](https://github.com/docxology/CogSecSkills/issues/47) — **repaired**.

Artifact and adapter failure controls use actual malformed registry/UTF-8 files instead of fake project behavior. Cwd changes exercise real filesystem state, not mocked project data.

Evidence: [`tests/artifacts/test_cogsecskills_examples_branches.py`](../tests/artifacts/test_cogsecskills_examples_branches.py), [`tests/quality/test_adapter_input_errors.py`](../tests/quality/test_adapter_input_errors.py).

### TEST-02

[Issue #48](https://github.com/docxology/CogSecSkills/issues/48) — **prior repair verified**.

The cited route/empty-findings controls now assert concrete diagnostic content. Nonempty live rows are explicit before subset palette checks.

Evidence: [`tests/artifacts/test_artifact_source_errors.py`](../tests/artifacts/test_artifact_source_errors.py), [`tests/artifacts/test_cogsecskills_manuscript_assets.py`](../tests/artifacts/test_cogsecskills_manuscript_assets.py).

### TEST-03

[Issue #49](https://github.com/docxology/CogSecSkills/issues/49) — **repaired**.

Repeated report-count expectations derive independently from canonical YAML or rendered rows; the sole intentional 100-area taxonomy conformance contract remains explicit.

Evidence: [`tests/artifacts/test_cogsecskills_dashboard.py`](../tests/artifacts/test_cogsecskills_dashboard.py), [`tests/artifacts/test_manuscript_table_layout.py`](../tests/artifacts/test_manuscript_table_layout.py).

### TEST-04

[Issue #50](https://github.com/docxology/CogSecSkills/issues/50) — **repaired**.

Repository-wide scenarios and palette tests use __file__-anchored source roots; actual subprocess cwd controls cover discovery.

Evidence: [`tests/artifacts/test_cogsecskills_scenarios.py`](../tests/artifacts/test_cogsecskills_scenarios.py), [`tests/core/test_input_boundaries.py`](../tests/core/test_input_boundaries.py).

### TEST-05

[Issue #51](https://github.com/docxology/CogSecSkills/issues/51) — **repaired**.

A real invalid UTF-8 adapter exercises unreadable-file behavior independently of root/chmod semantics.

Evidence: [`tests/quality/test_adapter_input_errors.py`](../tests/quality/test_adapter_input_errors.py), [`tests/quality/test_validation_boundaries.py`](../tests/quality/test_validation_boundaries.py).

### TEST-06

[Issue #52](https://github.com/docxology/CogSecSkills/issues/52) — **implemented in followup; qualified publication required**.

Two redundant passing constant-pin cases were removed; actual producer PNG signature, DPI and dimensions are now checked. Schema/theme-key contracts and real figure/PNG drift controls remain. Six mixed variant files are folded into topical owner leaves with all72 moved test ASTs, original helper ASTs, and1290-node marker membership preserved.

Evidence: [`tests/artifacts/test_cogsecskills_figures.py`](../tests/artifacts/test_cogsecskills_figures.py), [`docs/audit-controls-layout-20261018.json`](../docs/audit-controls-layout-20261018.json).

### TEST-07

[Issue #53](https://github.com/docxology/CogSecSkills/issues/53) — **repaired**.

Exact AST inventory finds shared fixture helpers, no exact duplicate test functions. Shared real-directory copying is centralized while independently meaningful test cases and assertions remain.

Evidence: [`tests/project_fixtures.py`](../tests/project_fixtures.py), [`tests/artifacts/test_cogsecskills_evals.py`](../tests/artifacts/test_cogsecskills_evals.py).

### TEST-08

[Issue #54](https://github.com/docxology/CogSecSkills/issues/54) — **implemented in followup; qualified publication required**.

Exact manuscript title inventory is replaced by one anchored H1 per section, unique anchors and resolved section references. Copy-edit and malformed/duplicate-anchor controls prove the structural oracle. Real path/citation/claim-boundary checks remain.

Evidence: [`tests/contract/test_cogsecskills_manuscript_contract.py`](../tests/contract/test_cogsecskills_manuscript_contract.py), [`tests/contract/test_cogsecskills_docs_contract.py`](../tests/contract/test_cogsecskills_docs_contract.py).

### TEST-09

[Issue #55](https://github.com/docxology/CogSecSkills/issues/55) — **repaired**.

CLI report/count assertions parse JSON and inspect values instead of serialized fragments.

Evidence: [`tests/authoring/test_cogsecskills_cli_scaffold.py`](../tests/authoring/test_cogsecskills_cli_scaffold.py), [`tests/quality/test_cogsecskills_insights.py`](../tests/quality/test_cogsecskills_insights.py).

### TEST-10

[Issue #56](https://github.com/docxology/CogSecSkills/issues/56) — **implemented in followup; qualified publication required**.

Actual YAML definitions exercise normalized field-scoped quality allowances, non-allowed duplicates and cross-field rejection. Negative controls remain non-exempt. A real subprocess rejects a missing registry root with exit1/path diagnostics/no traceback, while valid-library report findings retain the documented JSON/exit0 contract.

Evidence: [`src/cogsecskills/authoring/definitions.py`](../src/cogsecskills/authoring/definitions.py), [`tests/conformance/test_reuse_policy.py`](../tests/conformance/test_reuse_policy.py), [`src/cogsecskills/cli.py`](../src/cogsecskills/cli.py).
