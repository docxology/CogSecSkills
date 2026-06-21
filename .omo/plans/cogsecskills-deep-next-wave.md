# cogsecskills-deep-next-wave - Work Plan

## TL;DR (For humans)

**What you'll get:** A stronger evidence layer that makes every CogSecSkills claim easier to audit: skill scenarios and examples trace directly into the dashboard, reviewed local output fixtures can be checked without calling live models, manuscript figures and claims share one metadata source, and release metadata is checked before any public-release language is used.

**Why this approach:** The repo is already green structurally, so the next useful work is not another broad polish pass. The plan upgrades traceability and release discipline while preserving the boundary that local checks are not live runtime or field-effectiveness validation.

**What it will NOT do:** It will not call live model providers or OSINT connectors. It will not expand the default harness set beyond Claude, Codex, and Hermes. It will not claim DOI, archive, benchmark, field validation, runtime certification, vendor endorsement, or reproducible builds without real evidence.

**Effort:** Large
**Risk:** Medium - the changes add new verifier surfaces and generated artifacts, but avoid external services and preserve existing defaults.
**Decisions I made for you:** Keep all new evidence deterministic and local; base offline output review on the existing analyst-output rubric with 28 scenario-linked seed fixtures; keep optional harnesses documentation-only unless configured; make release checks local-development friendly by reporting dirty git state; update existing AGENTS files instead of adding more hierarchy; do not stage or commit unless separately approved.

Your next move: approve this plan, or veto one of the defaults above. Full execution detail follows below.

---

> TL;DR (machine): Large, medium risk; add traceable evidence ladder, offline fixture evaluation, release metadata checking, figure/claim metadata centralization, harness docs, AGENTS/runbook updates, and full local/template verification.

## Scope

### Must have
- Per-skill evidence traceability in generated dashboard JSON and Markdown.
- Stronger scenario and worked-example checks that validate structured answer shape, evidence labels, uncertainty language, refusal/redirect behavior, and source coverage.
- A new offline local output-evaluation layer over 28 scenario-linked reviewed fixtures, using the existing analyst-output rubric and no live provider calls.
- Centralized figure metadata used by manuscript asset generation, figure inventory docs, captions, and tests.
- A generated claim-provenance map that separates local conformance evidence, bibliography-backed motivation, deferred future work, and unsupported claims.
- Release metadata and claim matrix checks for package version, repository URL, license, `CITATION.cff`, CodeMeta, generated freshness, git state, and DOI/archive absence, with explicit modes for local development versus public/archive release readiness.
- Harness-profile documentation that preserves three statuses: default adapters, configured structural adapters, and documented external profiles.
- Updated README, QUICKSTART, harness docs, claim-boundary docs, TODO, ISA, manuscript prose, and existing AGENTS files after gates pass.
- Exact final verification numbers updated only after the final successful run.

### Must NOT have (guardrails, anti-slop, scope boundaries)
- No live Claude, Codex, Hermes, Gemini, Perplexity, browser, OSINT connector, GitHub release, Zenodo archive, DOI minting, or publication action.
- No expansion of default configured harnesses beyond `claude`, `codex`, and `hermes`.
- No field-effectiveness, benchmark, universal external-runtime support, runtime-certified, vendor-endorsement, reproducible-build, FAIR-compliance, DOI, or public-archive claims unless independently true and verified.
- No hand-editing generated rendered skill files, generated manuscript supplements, generated dashboard docs, or rendered PDF/HTML outputs.
- No broad revert, cleanup, or destructive git operation against unrelated dirty worktree content.
- No staging or committing unless the user separately requests git actions after implementation.

## Verification strategy

> All verification commands are agent-executed after approval. User approval is required before product implementation begins and before any optional git, publish, archive, or DOI action.

- Test decision: TDD for new CLI/checkers and generated artifacts; tests-after only for prose-only documentation edits.
- Evidence: each implementation todo writes a compact command transcript or summary under `.omo/evidence/task-<N>-cogsecskills-deep-next-wave.md`.
- Baseline: `.omo/ultraresearch/20260620-135250/verify-local-gates.md` records the current green snapshot: definitions, scenarios, examples, dashboard, manuscript assets, validate, report, doctor, pytest, markdown validation, and render.
- External docs used for new source claims must be re-opened during implementation before citation or vendor-specific wording is changed; planning URLs are not treated as permanently authoritative.

## Execution strategy

### Parallel execution waves

Wave 1 - evidence data model and checks:
- Todo 1, Todo 2, and Todo 3 are mostly sequential because they share scenario/example/dashboard data models.

Wave 2 - manuscript, release, and harness documentation:
- Todo 4, Todo 5, Todo 6, and Todo 7 can run in parallel after Todo 1 establishes shared traceability vocabulary.

Wave 3 - AGENTS, docs finalization, generated outputs, and verification:
- Todo 8 regenerates source-owned outputs and updates feature prose while leaving exact final verification numbers to Todo 9.
- Todo 9 runs final gates, updates exact gate-result numbers, and reruns the affected drift checks.

### Dependency matrix

| Todo | Depends on | Blocks | Can parallelize with |
| --- | --- | --- | --- |
| 1 | none | 2, 3, 4, 8 | none |
| 2 | 1 | 3, 8 | 4 after schema is stable |
| 3 | 1, 2 | 8, 9 | 5, 6, 7 |
| 4 | 1 | 8, 9 | 5, 6, 7 |
| 5 | none | 8, 9 | 4, 6, 7 |
| 6 | none | 8, 9 | 4, 5, 7 |
| 7 | none | 8, 9 | 4, 5, 6 |
| 8 | 1-7 | 9 | none |
| 9 | 8 | final response | none |

## Todos

> Implementation + Test = ONE todo. Never separate.

- [ ] 1. Add per-skill evidence-ladder traceability to dashboard data
  What to do / Must NOT do: Extend `src/cogsecskills/dashboard.py` only where the current payload is coarse: add per-skill `scenario_kinds`, `expected_answer_kinds`, expected-answer section titles, selected-skill consistency status, worked-example source path, worked-example section labels, and scenario-summary cross-check status. Preserve existing `scenario_ids`, `worked_example_id`, `quality_capsule_present`, `claim_boundary_status`, verbs, harnesses, references, and source-path fields instead of duplicating them. Update `docs/quality-dashboard.md` and `output/data/quality_dashboard.json` only through `python -m cogsecskills dashboard --write`. Do not hand-edit generated dashboard outputs.
  Parallelization: Wave 1 | Blocked by: none | Blocks: 2, 3, 4, 8
  References (executor has NO interview context - be exhaustive): `.omo/ultraresearch/20260620-135250/wave-1-scenario-dashboard.md`; `src/cogsecskills/dashboard.py:68`; `docs/quality-dashboard.md:31`; `tests/test_cogsecskills_dashboard.py:42`.
  Acceptance criteria (agent-executable): `PYTHONPATH="src:." python -m cogsecskills dashboard --write && PYTHONPATH="src:." python -m cogsecskills dashboard --check`; JSON has 100 skill rows and every row has the new traceability delta fields; Markdown includes scenario/example traceability sections; tests compare dashboard summary totals to `scenario_summary()` and `load_examples()`.
  QA scenarios (name the exact tool + invocation): happy: `python -m pytest tests/test_cogsecskills_dashboard.py -q`; failure: mutate a temp dashboard JSON copy missing one skill trace and assert `dashboard --check` fails in a `tmp_path` test. Evidence `.omo/evidence/task-1-cogsecskills-deep-next-wave.md`.
  Commit: N by default; if separately approved | feat(dashboard): expose per-skill evidence ladder traceability

- [ ] 2. Strengthen scenario and worked-example validation
  What to do / Must NOT do: Update `src/cogsecskills/scenarios.py` and `src/cogsecskills/examples.py` checks so fixtures validate structured section shape, evidence/inference/gap labels, uncertainty language, defensive boundary, expected output terms, refusal/redirect behavior, and scenario-summary/dashboard consistency. Keep all checks deterministic and local. Do not introduce live model calls or subjective online judging.
  Parallelization: Wave 1 | Blocked by: 1 | Blocks: 3, 8
  References (executor has NO interview context - be exhaustive): `.omo/ultraresearch/20260620-135250/wave-1-scenario-dashboard.md`; `src/cogsecskills/scenarios.py:284`; `src/cogsecskills/scenarios.py:425`; `src/cogsecskills/examples.py:20`; `examples/skill-worked-examples.yaml`.
  Acceptance criteria (agent-executable): `PYTHONPATH="src:." python -m cogsecskills scenarios --check`; `PYTHONPATH="src:." python -m cogsecskills examples --check`; tests include missing section, unsafe wording, stale selected skill, stale summary, and missing worked-example cases.
  QA scenarios (name the exact tool + invocation): happy: `python -m pytest tests/test_cogsecskills_scenarios.py tests/test_cogsecskills_examples.py -q`; failure: fixture-copy test removes a required answer section and expects the checker to fail. Evidence `.omo/evidence/task-2-cogsecskills-deep-next-wave.md`.
  Commit: N by default; if separately approved | test(scenarios): harden deterministic readiness fixtures

- [ ] 3. Add offline local output-evaluation fixtures and checker
  What to do / Must NOT do: Add a source-owned offline evaluation layer at `evals/local_output_review.yaml`, plus `src/cogsecskills/evals.py` and CLI `python -m cogsecskills evals --check`. Use `docs/analyst-output-review.md` as the normative rubric: `skill_fit`, `evidence_labeling`, `uncertainty`, `defensive_boundary`, and `output_usefulness`, each scored `0`, `1`, or `2`. The first coverage target is exactly 28 reviewed fixtures, one per current scenario id, each linked to `scenarios/defensive_readiness.yaml`, with all dimensions scored `2` to pass. Generate `docs/evaluation-readiness.md` and `output/data/evaluation_readiness.json` from the source fixture. It must not call APIs, browsers, connectors, or external model runtimes.
  Parallelization: Wave 1 | Blocked by: 1, 2 | Blocks: 8, 9
  References (executor has NO interview context - be exhaustive): `.omo/ultraresearch/20260620-135250/wave-1-external-evaluation.md`; `.omo/ultraresearch/20260620-135250/wave-1-external-sources.md`; `docs/analyst-output-review.md`; `scenarios/defensive_readiness.yaml`; OpenAI evals guide https://developers.openai.com/api/docs/guides/evals; OpenAI evaluation best practices https://developers.openai.com/api/docs/guides/evaluation-best-practices. Re-open official docs before adding vendor/eval claims.
  Acceptance criteria (agent-executable): `PYTHONPATH="src:." python -m cogsecskills evals --write && PYTHONPATH="src:." python -m cogsecskills evals --check` passes; tests prove missing fixture, mismatched scenario id, score below `2`, unsafe output, absent uncertainty, and live-provider wording fail; root AGENTS/source-surface docs mention `evals/` after the command exists.
  QA scenarios (name the exact tool + invocation): happy: `python -m pytest tests/test_cogsecskills_evals.py -q`; failure: temp fixture includes an unsafe operational passage and the checker rejects it. Evidence `.omo/evidence/task-3-cogsecskills-deep-next-wave.md`.
  Commit: N by default; if separately approved | feat(evals): add offline local output review gate

- [ ] 4. Centralize figure metadata and claim-provenance generation
  What to do / Must NOT do: Create one source of truth for figure metadata inside `src/cogsecskills/manuscript_assets.py` or a small adjacent module: filename, title, label, caption intent, semantic check strings, output path, and whether the cover is mirrored. Generate or update manuscript figure inventory and a claim-provenance/figure map from that metadata. Do not change rendered output directories by hand.
  Parallelization: Wave 2 | Blocked by: 1 vocabulary | Blocks: 8, 9
  References (executor has NO interview context - be exhaustive): `.omo/ultraresearch/20260620-135250/wave-1-manuscript-render.md`; `src/cogsecskills/manuscript_assets.py:37`; `src/cogsecskills/manuscript_assets.py:545`; `src/cogsecskills/manuscript_assets.py:645`; `tests/test_cogsecskills_manuscript_assets.py:27`; `tests/test_cogsecskills_manuscript_contract.py:47`.
  Acceptance criteria (agent-executable): `PYTHONPATH="src:." python -m cogsecskills manuscript-assets --write && PYTHONPATH="src:." python -m cogsecskills manuscript-assets --check`; tests import/inspect one figure metadata list and verify all eight figures, captions, semantic labels, and cover mirror path.
  QA scenarios (name the exact tool + invocation): happy: `python -m pytest tests/test_cogsecskills_manuscript_assets.py tests/test_cogsecskills_manuscript_contract.py -q`; failure: remove one expected semantic label from metadata in a temp test and expect check failure. Evidence `.omo/evidence/task-4-cogsecskills-deep-next-wave.md`.
  Commit: N by default; if separately approved | refactor(manuscript): centralize figure and claim metadata

- [ ] 5. Add release metadata and claim matrix checking
  What to do / Must NOT do: Add a release metadata checker, for example `src/cogsecskills/release.py` with CLI `python -m cogsecskills release-metadata --check`, that compares `pyproject.toml`, `CITATION.cff`, `codemeta.json`, manuscript release manifest, repository URL, license, generated freshness, git revision status, and DOI/archive fields. Default `local` mode must report dirty git state as a truthful local-development status, not fail because the worktree is dirty. Optional stricter modes, such as `--mode release-candidate` and `--mode public-archive`, may fail on dirty state or missing real archive metadata. Missing DOI/public archive is acceptable only when prose says unavailable. Do not publish, tag, push, archive, or mint DOI.
  Parallelization: Wave 2 | Blocked by: none | Blocks: 8, 9
  References (executor has NO interview context - be exhaustive): `.omo/ultraresearch/20260620-135250/wave-1-external-release.md`; `.omo/ultraresearch/20260620-135250/wave-1-external-sources.md`; `pyproject.toml:9`; `codemeta.json:2`; `manuscript/S02_release_manifest.md:12`; FORCE11 https://force11.org/info/software-citation-principles-published-2016/; Zenodo CFF help https://help.zenodo.org/docs/github/describe-software/citation-file/; GitHub citation docs https://docs.github.com/repositories/archiving-a-github-repository/referencing-and-citing-content.
  Acceptance criteria (agent-executable): `PYTHONPATH="src:." python -m cogsecskills release-metadata --check` passes in local mode and reports dirty state accurately; generated `docs/release-claim-matrix.md` or equivalent clearly separates safe, needs-evidence, and prohibited claims; tests cover version mismatch, invented DOI, stale repository URL, missing license, dirty local mode allowed, and dirty public/archive mode rejected.
  QA scenarios (name the exact tool + invocation): happy: `python -m pytest tests/test_cogsecskills_release_metadata.py -q`; failure: temp metadata copy sets a fake DOI while release status is unavailable and checker fails. Evidence `.omo/evidence/task-5-cogsecskills-deep-next-wave.md`.
  Commit: N by default; if separately approved | feat(release): check metadata and release claims

- [ ] 6. Refresh optional harness profile documentation without changing defaults
  What to do / Must NOT do: Update `registry/harness_profiles.yaml`, harness docs, methods/manuscript prose, and tests so optional profiles are current, source-backed, and clearly labeled. Preserve three statuses: default adapters, configured structural adapters, documented external profiles. Keep `HARNESSES = ("claude", "codex", "hermes")` unchanged and do not regenerate all skills with optional harness adapters unless explicitly configured.
  Parallelization: Wave 2 | Blocked by: none | Blocks: 8, 9
  References (executor has NO interview context - be exhaustive): `.omo/ultraresearch/20260620-135250/wave-1-external-sources.md`; GitHub Copilot custom instructions https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions; Gemini context files https://geminicli.com/docs/cli/gemini-md/; Cursor rules https://cursor.com/docs/rules; MCP intro https://modelcontextprotocol.io/docs/getting-started/intro. Re-open official docs before changing harness-specific prose.
  Acceptance criteria (agent-executable): docs/tests confirm every optional profile appears in docs and manuscript; negative tests reject `runtime certified`, `field validated`, `works in every external runtime`, and vendor-endorsement wording.
  QA scenarios (name the exact tool + invocation): happy: `python -m pytest tests/test_cogsecskills_docs_contract.py -q`; failure: temp docs string claims runtime certification and wording test rejects it. Evidence `.omo/evidence/task-6-cogsecskills-deep-next-wave.md`.
  Commit: N by default; if separately approved | docs(harness): clarify optional profile statuses

- [ ] 7. Update AGENTS hierarchy and runbooks for new source-owned surfaces
  What to do / Must NOT do: Review existing root and subdirectory `AGENTS.md` files and update only stale guidance for new commands, source ownership, generated-file boundaries, evidence ladder, release metadata, and claim boundaries. Do not add more AGENTS files unless a directory has materially different rules and no existing nearest guidance.
  Parallelization: Wave 2 | Blocked by: none | Blocks: 8, 9
  References (executor has NO interview context - be exhaustive): `.omo/ultraresearch/20260620-135250/wave-1-docs-agents-tests.md`; `AGENTS.md`; `definitions/AGENTS.md`; `docs/AGENTS.md`; `manuscript/AGENTS.md`; `registry/AGENTS.md`; `scenarios/AGENTS.md`; `skills/AGENTS.md`; `src/cogsecskills/AGENTS.md`; `tests/AGENTS.md`.
  Acceptance criteria (agent-executable): AGENTS docs mention new checkers only after they exist; no stale command list omits `evals --check` or `release-metadata --check`; tests or script check generated/source-owned boundary wording and `evals/` ownership.
  QA scenarios (name the exact tool + invocation): happy: `rg -n "evals --check|release-metadata --check|source-owned|generated" AGENTS.md definitions/AGENTS.md docs/AGENTS.md manuscript/AGENTS.md registry/AGENTS.md scenarios/AGENTS.md skills/AGENTS.md src/cogsecskills/AGENTS.md tests/AGENTS.md` and `PYTHONPATH="src:." python -m pytest tests/test_cogsecskills_agents_contract.py tests/test_cogsecskills_docs_contract.py -q`; failure: temp-doc test removes `evals --check` from root guidance and asserts the docs contract fails with a missing-command assertion. Evidence `.omo/evidence/task-7-cogsecskills-deep-next-wave.md`.
  Commit: N by default; if separately approved | docs(agents): update evidence-layer guidance

- [ ] 8. Regenerate source-owned outputs and update feature documentation
  What to do / Must NOT do: Run all source-owned generators in order, update README, QUICKSTART, docs, TODO, ISA, and manuscript prose for new commands and concepts, but leave exact final gate-result numbers to Todo 9 after the final successful run. Do not manually edit generated supplements/dashboard/skill outputs.
  Parallelization: Wave 3 | Blocked by: 1-7 | Blocks: 9
  References (executor has NO interview context - be exhaustive): `AGENTS.md`; `.omo/ultraresearch/20260620-135250/verify-local-gates.md`; `README.md`; `QUICKSTART.md`; `TODO.md`; `ISA.md`; `manuscript/S02_release_manifest.md`; `manuscript/`.
  Acceptance criteria (agent-executable): `PYTHONPATH="src:." python -m cogsecskills definitions --write`; `definitions --check`; `scenarios --check`; `examples --write`; `examples --check`; `evals --write`; `evals --check`; `dashboard --write`; `dashboard --check`; `manuscript-assets --write`; `manuscript-assets --check`; `release-metadata --check`; docs describe new surfaces without stale final-number claims.
  QA scenarios (name the exact tool + invocation): happy: local generator/check list above; failure: `rg -n "runtime certified|field validated|works in every external runtime|DOI:|published archive" README.md QUICKSTART.md docs manuscript TODO.md ISA.md` returns only explicit unavailable/deferred contexts. Evidence `.omo/evidence/task-8-cogsecskills-deep-next-wave.md`.
  Commit: N by default; if separately approved | docs: refresh evidence ladder and release status

- [ ] 9. Run full local and manuscript/template verification
  What to do / Must NOT do: Execute final gates, collect exact outputs, update only allowed source docs with the final numbers, and rerun affected drift checks after those updates. Do not declare completion if any local or template gate fails. Do not clean unrelated dirty files.
  Parallelization: Wave 3 | Blocked by: 8 | Blocks: final response
  References (executor has NO interview context - be exhaustive): `.omo/ultraresearch/20260620-135250/verify-local-gates.md`; `AGENTS.md`; `/Users/4d/Documents/GitHub/template`.
  Acceptance criteria (agent-executable): all commands below exit 0:
  ```bash
  PYTHONPATH="src:." python -m cogsecskills definitions --check
  PYTHONPATH="src:." python -m cogsecskills scenarios --check
  PYTHONPATH="src:." python -m cogsecskills examples --check
  PYTHONPATH="src:." python -m cogsecskills evals --check
  PYTHONPATH="src:." python -m cogsecskills dashboard --check
  PYTHONPATH="src:." python -m cogsecskills manuscript-assets --check
  PYTHONPATH="src:." python -m cogsecskills release-metadata --check
  PYTHONPATH="src:." python -m cogsecskills validate
  PYTHONPATH="src:." python -m cogsecskills report
  PYTHONPATH="src:." python -m cogsecskills doctor
  PYTHONPATH="src:." python -m pytest tests/test_cogsecskills_*.py tests/test_skill_library_conformance.py --cov=src/cogsecskills --cov-report=term-missing
  uv run ruff check src/cogsecskills tests
  uv run ruff format --check src/cogsecskills tests
  uv run mypy
  git diff --check
  ```
  From `/Users/4d/Documents/GitHub/template`:
  ```bash
  uv run python -m infrastructure.validation.cli markdown projects/working/CogSecSkills/manuscript/
  uv run python scripts/03_render_pdf.py --project working/CogSecSkills
  pdftotext /Users/4d/Documents/GitHub/projects/working/CogSecSkills/output/pdf/CogSecSkills_combined.pdf - | rg "Evidence Ladder|Skill Worked Examples|Scenario Readiness|expected answers|Quality Dashboard|Supplemental 100-Skill Catalogue|github.com/docxology/CogSecSkills"
  ! rg -n "Citation .*undefined|undefined references|LaTeX Warning: Reference.*undefined|Missing character|Package .* Error|File .* not found|^!|LaTeX Error|Fatal error|Emergency stop" /Users/4d/Documents/GitHub/projects/working/CogSecSkills/output/pdf/_combined_manuscript.log
  ```
  Exact final counts are updated only after these commands pass, then affected `--check` gates are rerun. The final render-log command is a no-match gate: it succeeds only when the listed error patterns are absent.
  QA scenarios (name the exact tool + invocation): happy: exact command transcript saved to `.omo/evidence/task-9-cogsecskills-deep-next-wave.md`; failure: if any command is unavailable or fails, capture exact stderr/stdout and mark the gate blocked rather than passing. Evidence `.omo/evidence/task-9-cogsecskills-deep-next-wave.md`.
  Commit: N by default; if separately approved | chore: verify evidence-layer hardening

## Final verification wave

> Runs after ALL todos. ALL must approve before completion is reported. Git, publish, archive, and DOI actions still require separate user approval.

- [ ] F1. Plan compliance audit: run `git diff --stat`, `git diff --name-only`, and `rg -n "runtime certified|field validated|works in every external runtime|published archive|DOI:" README.md QUICKSTART.md docs manuscript TODO.md ISA.md`; inspect `.omo/evidence/task-*-cogsecskills-deep-next-wave.md`; expected result is every todo has evidence and only unavailable/deferred contexts contain restricted claim words.
- [ ] F2. Code quality review: read new or edited modules under `src/cogsecskills/` and tests; run the local gates in Todo 9; expected result is thin CLI orchestration, deterministic file IO, no hidden network calls, no duplicated large schemas, and no test-only production behavior.
- [ ] F3. Real manual QA: open/read `docs/quality-dashboard.md`, generated evaluation docs, release claim matrix, `manuscript/S02_release_manifest.md`, and the PDF text smoke output; optionally inspect regenerated figure PNG dimensions; expected result is reader-facing clarity, not merely machine pass.
- [ ] F4. Scope fidelity: run `rg -n "requests\\.|httpx|urllib|webbrowser|perplexity|gemini|openai|anthropic|zenodo|gh release|git tag" src/cogsecskills tests docs manuscript . --glob '!uv.lock'` and inspect hits; expected result is no live runtime, connector, publication, default harness expansion, generated-file hand edit, or unrelated revert.

## Commit strategy

- Suggested commit messages are planning hints only. Do not stage or commit unless the user separately asks for git actions.
- If the user later requests commits, use narrow, topic-oriented commits only after each wave is green.
- Never stage unrelated dirty worktree content.
- Suggested commit order:
  1. `feat(dashboard): expose per-skill evidence ladder traceability`
  2. `test(scenarios): harden deterministic readiness fixtures`
  3. `feat(evals): add offline local output review gate`
  4. `refactor(manuscript): centralize figure and claim metadata`
  5. `feat(release): check metadata and release claims`
  6. `docs(harness): clarify optional profile statuses`
  7. `docs(agents): update evidence-layer guidance`
  8. `docs: refresh evidence ladder and release status`
  9. `chore: verify evidence-layer hardening`

## Success criteria

- Local gates are green with exact final counts reported.
- Template markdown validation and PDF render pass from the sibling template checkout.
- The dashboard lets a reader trace each of 100 skills to examples, scenario coverage, quality capsule, references, harnesses, and claim-boundary status.
- Offline output-evaluation fixtures add deterministic review evidence without external model calls.
- Release metadata and claim matrix prevent invented DOI/archive/field-validation/reproducible-build language.
- Manuscript figure and claim inventories are generated from centralized metadata.
- Optional harness profiles are clearer without changing default adapters.
- AGENTS and runbooks reflect the real source-owned workflow.
- The final answer distinguishes local structural/evidence readiness from live runtime or field-effectiveness validation.
