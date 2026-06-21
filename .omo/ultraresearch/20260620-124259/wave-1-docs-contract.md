# Wave 1 - Documentation Contract

Worker: `019ee68f-5abf-7961-aef5-56901f9a92a4`

## Key Findings

- No material drift was found across README, QUICKSTART, TODO, ISA, docs,
  harness profiles, and manuscript methods sections.
- Default harnesses remain `claude`, `codex`, and `hermes`; optional profiles
  are documented external profiles unless configured and validated.
- The strongest remaining opportunity was adding local `AGENTS.md` guidance
  under docs/source-boundary subtrees.

## Expansion

- Closed by implementation: add `docs/AGENTS.md` and the broader AGENTS
  hierarchy, then lock it with tests.

