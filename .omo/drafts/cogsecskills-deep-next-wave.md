---
slug: cogsecskills-deep-next-wave
status: awaiting-approval
intent: unclear
pending-action: user approval before product implementation
approach: traceable evaluation and release evidence layer
---

# Draft: cogsecskills-deep-next-wave

## Components (topology ledger)
| id | outcome | status | evidence path |
| --- | --- | --- | --- |
| C1 | Evidence ladder traceability: every skill links to scenario ids, answer kind, worked example, quality capsule, and claim boundary in generated JSON/Markdown. | active | `.omo/ultraresearch/20260620-135250/wave-1-scenario-dashboard.md` |
| C2 | Section-aware scenario and worked-example validation that catches stale, generic, unsafe, or mismatched fixtures. | active | `.omo/ultraresearch/20260620-135250/wave-1-scenario-dashboard.md` |
| C3 | Offline local output-evaluation layer over reviewed fixtures, using the existing analyst-output rubric and no live provider calls. | active | `.omo/ultraresearch/20260620-135250/wave-1-external-evaluation.md` |
| C4 | Central figure metadata and claim-provenance map for manuscript defensibility. | active | `.omo/ultraresearch/20260620-135250/wave-1-manuscript-render.md` |
| C5 | Release metadata and claim matrix checker covering version, citation, CodeMeta, license, repository, DOI absence, and generated freshness. | active | `.omo/ultraresearch/20260620-135250/wave-1-external-release.md` |
| C6 | Optional harness-profile docs refresh with default/configured/documented status preserved. | active | `.omo/ultraresearch/20260620-135250/wave-1-external-sources.md` |
| C7 | AGENTS/runbook updates for any new evidence surfaces and commands. | active | `.omo/ultraresearch/20260620-135250/wave-1-docs-agents-tests.md` |
| C8 | Final local and template gates with exact verification numbers updated only after passing runs. | active | `.omo/ultraresearch/20260620-135250/verify-local-gates.md` |

## Open assumptions (announced defaults)
| assumption | adopted default | rationale | reversible? |
| --- | --- | --- | --- |
| Scope | Plan the next implementation wave now; do not implement product changes before approval. | `omo:ulw-plan` requires an approval gate for unclear/open-ended work. | Yes |
| Evidence level | Add deterministic local evidence and optional offline review fixtures before live runtime evaluation. | Current gates are green; external eval guidance distinguishes local tests from model-output evaluation. | Yes |
| Harness defaults | Keep default adapters as `claude`, `codex`, and `hermes`; optional profiles remain documentation metadata unless configured. | Existing contract and docs depend on this boundary. | Yes |
| Publication claims | Leave DOI/archive/publication/field-validation claims unavailable until real release evidence exists. | False publication metadata is high-risk and hard to unwind after publication. | No, once published |
| Generated files | Source-owned inputs drive generated outputs; no hand-editing generated skill trees, generated supplements, or generated dashboard files. | Repo convention and current validators rely on drift checks. | Yes |
| AGENTS hierarchy | Update existing AGENTS files only where stale; do not add more hierarchy by default. | The repo already has root plus eight subdirectory AGENTS files. | Yes |
| Git actions | Do not stage or commit by default; record suggested commit messages only. | The worktree is intentionally dirty and contains unrelated prior implementation changes. | Yes |

## Findings (cited - path:lines)
- `.omo/ultraresearch/20260620-135250/verify-local-gates.md`: current baseline is green, including definitions, scenarios, examples, dashboard, manuscript assets, validate, report, doctor, pytest, markdown validation, and render.
- `.omo/ultraresearch/20260620-135250/wave-1-codebase-architecture.md`: source layers and CLI spine are stable; the next wave should add evidence levels rather than repairing existing structural gates.
- `.omo/ultraresearch/20260620-135250/wave-1-scenario-dashboard.md`: scenario/example/dashboard surfaces exist but should become per-skill traceability surfaces.
- `.omo/ultraresearch/20260620-135250/wave-1-manuscript-render.md`: figure inventory and claim-provenance metadata should be centralized.
- `.omo/ultraresearch/20260620-135250/wave-1-external-evaluation.md`: external eval practice supports a separate offline output-evaluation lane, not a field-effectiveness claim.
- `.omo/ultraresearch/20260620-135250/wave-1-external-release.md`: release metadata must be consistency-checked without inventing DOI/archive status.
- `.omo/ultraresearch/20260620-135250/wave-1-docs-agents-tests.md`: AGENTS hierarchy already exists; update it only for new commands and boundaries.

## Decisions (with rationale)
- Decision: Name the next wave "Traceable Evaluation And Release Evidence Layer." Rationale: the current repo is already green structurally; the next quality gain is auditability of what local evidence proves.
- Decision: Add an offline local evaluation checker in the plan, but explicitly exclude live model/provider calls. Rationale: it raises evidence quality while preserving the local claim boundary.
- Decision: Base the offline checker on `docs/analyst-output-review.md`, with 28 scenario-linked reviewed fixtures as the first coverage target and all published rubric dimensions scoring `2` to pass. Rationale: this reuses the current local review protocol instead of inventing a separate standard.
- Decision: Centralize figure metadata before more figure polish. Rationale: repeated figure inventories create drift risk.
- Decision: Add release metadata/claim checking before public release work, with default local-development mode reporting dirty git state rather than failing it. Rationale: the current worktree is intentionally dirty, while public/archive release mode should be stricter.
- Decision: Keep optional harness profiles as documentation and configuration targets, not default adapters. Rationale: the structural contract is configurable, but defaults should stay stable.

## Scope IN
- New or strengthened source-owned checks for evidence-ladder traceability, worked examples, scenarios, offline fixture reviews, release metadata, figure metadata, and claim provenance.
- Generated dashboard/manuscript/docs updates from source-owned inputs.
- Tests for new CLI/checker behavior and negative wording guards.
- Existing AGENTS files updated only where new source surfaces and commands require guidance.
- Suggested commit messages documented, but no staging or commit unless the user separately requests git actions.

## Scope OUT (Must NOT have)
- No live Claude, Codex, Hermes, Gemini, Perplexity, browser, OSINT connector, GitHub release, Zenodo archive, DOI minting, or publication action.
- No default harness expansion beyond `claude`, `codex`, and `hermes`.
- No field-effectiveness, benchmark, universal-runtime, runtime-certified, vendor-endorsement, or reproducible-build claims.
- No hand-editing generated skill files, generated supplements, generated dashboard docs, or rendered PDF/HTML outputs.
- No destructive git cleanup or broad revert of unrelated dirty worktree state.

## Open questions
- None blocking. The plan adopts conservative defaults that can be vetoed before implementation.

## Approval gate
status: awaiting-approval
next action: user approves or vetoes `.omo/plans/cogsecskills-deep-next-wave.md` before product implementation begins.
