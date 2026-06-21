# Ultraresearch Synthesis: CogSecSkills Next Wave

Access date: 2026-06-20.

## Executive Synthesis

The current CogSecSkills baseline is structurally green: canonical definitions, rendered skills, scenarios, examples, dashboard, manuscript assets, validation, doctor, pytest, and template render all passed in the immediately preceding verification snapshot. The next useful wave should therefore avoid redoing broad polish and instead add a traceable evidence layer: deterministic scenario/example traceability, optional offline output-evaluation fixtures, release metadata consistency, figure/claim provenance centralization, and updated AGENTS/docs guidance.

The strongest framing is:

> CogSecSkills is locally validated as a source-synchronized, multiharness, defensive skill system. The next wave should make the evidence ladder auditable and release-ready without claiming live runtime behavior, field effectiveness, DOI/archive status, or vendor endorsement.

## Source Basis

Local research artifacts:
- `verify-local-gates.md`: immediately preceding green baseline.
- `wave-1-codebase-architecture.md`: CLI and source-surface architecture.
- `wave-1-scenario-dashboard.md`: scenario, expected-answer, example, and dashboard traceability gaps.
- `wave-1-manuscript-render.md`: figure inventory, claim-provenance, and render-contract gaps.
- `wave-1-docs-agents-tests.md`: AGENTS hierarchy and existing test surface.
- `wave-1-external-evaluation.md`: evaluation and red-team evidence framing.
- `wave-1-external-release.md`: release, citation, and reproducibility metadata.
- `wave-1-external-sources.md`: official source URLs opened directly.

External source basis:
- OpenAI evals: https://developers.openai.com/api/docs/guides/evals
- OpenAI evaluation best practices: https://developers.openai.com/api/docs/guides/evaluation-best-practices
- NIST AI RMF GenAI Profile: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework
- FORCE11 software citation principles: https://force11.org/info/software-citation-principles-published-2016/
- Zenodo CITATION.cff help: https://help.zenodo.org/docs/github/describe-software/citation-file/
- Zenodo GitHub integration: https://help.zenodo.org/docs/github/
- GitHub repository citation docs: https://docs.github.com/repositories/archiving-a-github-repository/referencing-and-citing-content
- GitHub Copilot custom instructions: https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions
- Gemini context files: https://geminicli.com/docs/cli/gemini-md/
- Cursor rules: https://cursor.com/docs/rules
- MCP introduction: https://modelcontextprotocol.io/docs/getting-started/intro

## Findings

### Evidence Ladder

The repo already has scenario fixtures and worked examples, but the dashboard should become a traceability surface rather than a count surface. The next implementation should expose per-skill scenario ids, answer kind, worked-example provenance, claim-boundary status, and coverage gaps in both Markdown and JSON.

### Offline Evaluation

External evaluation guidance distinguishes ordinary software tests from model-output evaluation. CogSecSkills should add an optional local offline-output review layer over reviewed fixture answers, not live provider calls. This can validate section shape, evidence labels, uncertainty language, refusal/redirect behavior, and rubric scores without certifying external runtimes.

### Manuscript And Figures

The manuscript is render-green, but figure inventory and caption contracts are still spread across generator code, tests, and generated text. A central figure metadata registry should drive generator output, figure inventory, captions, and tests. A claim-provenance map should separate local conformance evidence, bibliography-backed motivation, deferred future claims, and unsupported claims.

### Release Evidence

Release metadata should be consistency-checked before publication. The next wave should verify package version, repository URL, license, `CITATION.cff`, CodeMeta, release checklist, generated output freshness, and DOI/archive absence. It must not claim a DOI, public archive, reproducible build, FAIR compliance, or field validation unless those facts are actually established.

### Harness Profiles

Default adapters remain `claude`, `codex`, and `hermes`. Optional harness profiles are useful documentation metadata, but they are not runtime certification. Official docs support local instruction/context surfaces for tools such as Copilot, Gemini CLI, Cursor, and MCP-enabled hosts, but each profile must remain bounded as documented, configured, and locally validated only after explicit configuration.

### AGENTS Hierarchy

The current AGENTS hierarchy is already broad. The next pass should update existing guidance for any new commands and evidence boundaries, not create a larger rule tree by default.

## Recommended Plan Shape

Implement a "Traceable Evaluation And Release Evidence Layer" with these top-level components:

1. Evidence-ladder traceability in dashboard JSON/Markdown.
2. Section-aware scenario and worked-example validation.
3. Offline local output-evaluation fixtures and checker.
4. Central figure metadata and claim-provenance map.
5. Release metadata and claim-matrix checker.
6. Harness-profile documentation refresh using official-source nuance.
7. AGENTS/runbook updates for new source-owned surfaces.
8. Final local and template gates with exact verification numbers updated only after successful runs.

## Must Not Have

- No live model/provider calls.
- No default harness expansion beyond `claude`, `codex`, and `hermes`.
- No DOI, public-release, benchmark, field-validation, universal-runtime, or vendor-endorsement claims.
- No hand-edits to generated skill files, generated supplements, or generated dashboard outputs.
- No destructive git cleanup of unrelated dirty worktree state.

## Open Risks

- The local LSP transport failed with `Transport closed`; codegraph and tests were sufficient for planning, but LSP-derived centrality claims were not used.
- Any new CLI checker increases maintenance surface. Keep new commands narrow and source-owned.
- Release metadata checks must handle intentionally unavailable publication identifiers without treating their absence as failure.
