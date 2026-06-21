# Wave 1 - Corpus Boundaries

Worker: `019ee68f-50b0-7050-b076-cf3ecc0616df`

## Key Findings

- `registry/skills.yaml` is the plan, `definitions/<group>/<slug>.yaml` is the
  canonical source, and `skills/<group>/<slug>/` is rendered output.
- `scenarios/defensive_readiness.yaml` is a checked contract fixture, not a live
  model-evaluation artifact.
- `docs/quality-dashboard.md` and `output/data/quality_dashboard.json` are
  generated mirrors; their drift is checked by `dashboard --check`.
- Strongest AGENTS opportunities are `definitions/`, `skills/`, and
  `scenarios/`, where source/generated boundaries and expected-answer semantics
  are easy to violate.

## Expansion

- Closed by implementation: add `definitions/AGENTS.md`, `skills/AGENTS.md`, and
  `scenarios/AGENTS.md`.

