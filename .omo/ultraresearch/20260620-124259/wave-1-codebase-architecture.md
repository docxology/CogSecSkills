# Wave 1 - Codebase Architecture

Worker: `019ee68f-48ef-76a0-a91e-0426b2e968c1`

## Key Findings

- `python -m cogsecskills` reaches `src/cogsecskills/__main__.py`, then `cli.main()`.
- `cli.py` exposes the public command surface: `validate`, `report`, `doctor`,
  `definitions`, `scenarios`, `dashboard`, `manuscript-assets`, `author`,
  `author-batch`, `scaffold`, `route`, `catalogue`, and support commands.
- Source ownership is layered: `registry/` plans, `definitions/` owns skill
  substance, `skills/` renders harness-facing files, `scenarios/` owns local
  expected-answer fixtures, `dashboard.py` and `manuscript_assets.py` generate
  documentation/data/figure mirrors.
- Test coverage already maps the major paths: authoring, definitions, scenarios,
  dashboard, manuscript assets, docs contracts, and full-library conformance.

## Expansion

none - architecture and command-surface mapping was complete for this pass.

