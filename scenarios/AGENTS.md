# AGENTS.md - Defensive Scenario Fixtures

This directory owns deterministic local readiness fixtures.

## Scenario Contract

- `defensive_readiness.yaml` contains curated safe-use and unsafe-redirect
  probes across the seven groups. The current source target is two safe and two
  unsafe fixtures per group.
- `expected_answer` blocks are reviewed local fixtures, not live model outputs.
- Unsafe scenarios must demonstrate refusal or defensive redirection without
  operational misuse detail.
- Safe scenarios must preserve evidence, inference, gap, confidence, and
  uncertainty language.

## Editing Rules

- Do not add offensive playbooks, targeting instructions, doxing detail, evasion
  guidance, source fabrication, or persuasion optimization.
- Keep expected routed skill ids synchronized with `route` behavior and rendered
  skill contracts.
- Scenario changes usually require regenerating the dashboard because scenario
  coverage is surfaced there.

## Verification

```bash
PYTHONPATH="src:." python -m cogsecskills scenarios --check
PYTHONPATH="src:." python -m cogsecskills examples --check
PYTHONPATH="src:." python -m cogsecskills dashboard --write
PYTHONPATH="src:." python -m cogsecskills dashboard --check
```
