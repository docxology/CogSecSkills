# Wave 1 Docs, AGENTS, And Tests Digest

Sources:
- Recovered docs-contract auditor result.
- Recovered source-boundary explorer result.
- Recovered test/gate researcher result.
- Direct read of existing AGENTS list.

Key findings:
- Existing AGENTS hierarchy is already broad: root, `definitions/`, `docs/`, `manuscript/`, `registry/`, `scenarios/`, `skills/`, `src/cogsecskills/`, and `tests/`.
- The recovered source-boundary explorer originally suggested adding `definitions/` and `scenarios/` guidance, but current filesystem already has those files. The next pass should review/trim/update, not blindly create more hierarchy.
- Tests already cover docs contracts, manuscript contracts, dashboard drift, manuscript asset drift, scenario fixtures, examples, definitions, harness validation, and full-library conformance.
- Good next tests should avoid duplicating existing checks and instead focus on new behaviors: offline eval harness fixtures, profile-doc consistency, release evidence pack, and generated navigation surfaces.

Expansion markers:
- LEAD: init-deep should update existing AGENTS files only where stale after the evidence-ladder additions; no new broad AGENTS tree is needed.
- LEAD: The next plan should include a docs/contract drift guard for any new eval/release/dashboard surfaces.

## EXPAND
- LEAD: Review existing AGENTS files for evidence-ladder and optional-harness drift — WHY: hierarchy already exists, but source surfaces changed — ANGLE: compare AGENTS commands against current CLI.
- LEAD: Add tests only for new surfaces introduced by the next worker — WHY: existing tests are strong and duplicate tests add noise — ANGLE: plan eval/release/nav tests.

