# Wave 1 Codebase Architecture Digest

Sources:
- Recovered explorer result from stale agent close: mapped CLI, registry, loader, author, definitions, scenarios, dashboard, manuscript assets, insights, config, and tests.
- Direct codegraph: `codegraph_explore("CogSecSkills architecture CLI definitions scenarios examples dashboard manuscript_assets validation flow")`.
- Direct shell discovery: existing AGENTS files and file-count/depth commands.

Key findings:
- The execution spine is `python -m cogsecskills` -> `src/cogsecskills/__main__.py` -> `src/cogsecskills/cli.py`.
- Source layers are stable: `registry/skills.yaml` and `registry/groups.yaml` plan the corpus; `definitions/<group>/<slug>.yaml` owns skill substance; `skills/<group>/<slug>/` is generated harness-facing output; `scenarios/defensive_readiness.yaml` owns deterministic readiness fixtures; examples and dashboard are generated/checkable evidence surfaces.
- Codegraph identified `Scenario` and `ExampleSection` as dataclasses with low direct caller count, but the pytest suite has explicit scenario/example modules, so codegraph's "no covering tests found" marker should be treated as index limitation rather than proof of missing tests.
- LSP failed with `Transport closed`; no LSP centrality claims are used.

Expansion markers:
- LEAD: Add an offline agent-output eval layer that consumes the current scenarios/examples without replacing deterministic checks.
- LEAD: Add a plan task to harden codegraph/LSP availability only if the repo wants richer developer-local diagnostics; not needed for product behavior.

## EXPAND
- LEAD: Offline eval harness over scenarios/examples — WHY: current fixtures validate shape, not scored generated outputs — ANGLE: inspect OpenAI eval guidance and local scenario schema.
- DEAD END: LSP centrality — LSP transport closed; codegraph plus tests are enough for this planning pass.

