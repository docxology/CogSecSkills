# CogSecSkills Visual Release Hardening

Status: local execution plan, not project content.

## Scope

- Fix release metadata drift caused by committed git revision snapshots.
- Add a source-owned visual design contract.
- Extend the quality dashboard with a generated static HTML surface.
- Regenerate release, dashboard, and manuscript outputs through their CLIs.
- Verify locally, render the manuscript, commit durable changes, and push main.

## Non-goals

- Do not commit `.omo/`.
- Do not expand default harnesses beyond `claude`, `codex`, and `hermes`.
- Do not claim live runtime certification, field validation, DOI/archive status,
  or provider endorsement.

## Superseded Context

The older `.omo/plans/cogsecskills-deep-next-wave.md` describes the evidence
ladder work completed by commit `3f67f18`. This pass starts from that pushed
state and only carries forward unresolved visual and release-metadata hardening.
