# CogSecSkills TODO

Forward-only tracker for source-owned work. Keep history in completed changelog
or commit messages; keep this file focused on the current state and next useful
work.

## Verified State

- Library gate: `PYTHONPATH="src:." python -m cogsecskills validate` -> `0 error(s), 0 warning(s)`.
- Report gate: `PYTHONPATH="src:." python -m cogsecskills report` -> `registry_total: 100`, `implemented: 100`, `on_disk_skills: 100`, `ok: true`.
- Quality gate: `PYTHONPATH="src:." python -m cogsecskills doctor` -> `validation: 0 error(s); quality: 0 finding(s)`.
- Canonical definition gate: `PYTHONPATH="src:." python -m cogsecskills definitions --check` -> `canonical definitions are current`.
- Scenario gate: `PYTHONPATH="src:." python -m cogsecskills scenarios --check` -> `scenario readiness fixtures are current: 28 scenarios across 7 groups; 28 expected answers checked`.
- Worked-example gate: `PYTHONPATH="src:." python -m cogsecskills examples --check` -> `worked examples are current`.
- Dashboard gate: `PYTHONPATH="src:." python -m cogsecskills dashboard --check` -> `quality dashboard is current`.
- Manuscript asset gate: `PYTHONPATH="src:." python -m cogsecskills manuscript-assets --check` -> `manuscript assets are current`.
- Test gate: `PYTHONPATH="src:." python -m pytest tests/ --cov=src/cogsecskills --cov-report=term-missing` -> `722 passed`, `Total coverage: 93.88%`.

## Ongoing Guardrails

- Keep verification prose aligned with the exact latest gate run after any future source edits.
- Rerun `manuscript-assets --write` and `manuscript-assets --check` after registry or skill metadata changes.
- Rerun `definitions --write` and `definitions --check` after any canonical skill-definition change.
- Rerun `scenarios --check` after scenario fixtures, routing language, output contracts, or quality fields change.
- Rerun `examples --write` and `examples --check` after worked-example source changes.
- Preserve the defensive-only boundary; do not add offensive influence-operation playbooks.

## Deferred: Empirical Evaluation

- Add richer empirical validation only after scenario-output fixtures and claim boundaries are clear.
- Use `docs/analyst-output-review.md` as the initial rubric for exploratory internal review.
- Label any comparison against unstructured prompting as exploratory unless externally reviewed.

## Deferred: Live Connector Integrations

- Add connector-specific OSINT/web harness notes only when live connectors are intentionally wired.
- Require privacy/legal checks, source custody, rate-limit handling, and connector-specific tests before describing a connector as supported.

## Deferred: External Publication/DOI

- Add verified external citations only when a manuscript claim needs external literature rather than project-local evidence.
- Do not add DOI, release archive, public deployment, or peer-review claims until those artifacts exist.
