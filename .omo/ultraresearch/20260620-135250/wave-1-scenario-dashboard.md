# Wave 1 Scenario, Examples, And Dashboard Digest

Sources:
- Parallel scenario/dashboard researcher result.
- Direct codegraph exploration of `src/cogsecskills/scenarios.py`, `src/cogsecskills/examples.py`, and `src/cogsecskills/dashboard.py`.
- Direct string audit across `scenarios/`, `examples/`, `docs/quality-dashboard.md`, and dashboard tests.

Key findings:
- The current evidence ladder already exists: 28 defensive-readiness scenarios across seven groups, 100 worked examples, generated quality dashboard Markdown, and generated dashboard JSON.
- The dashboard payload already records `scenario_coverage`, `worked_example_id`, `claim_boundary_status`, and evidence-ladder counts.
- The current dashboard is useful as a navigation surface, but the next layer should be more traceable: per-skill scenario ids, expected-answer kind, reviewed example provenance, and coverage state should be visible without opening YAML by hand.
- The scenario checker validates expected answers and unsafe redirects, but dashboard and scenario summaries should be cross-checked directly so future drift cannot leave a green dashboard with stale coverage numbers.
- Worked-example checks should move beyond keyword presence toward section-level shape checks: evidence, inference, uncertainty, defensive boundary, and expected output terms should be validated as structured fields.

Expansion markers:
- LEAD: Add a traceability matrix that links each skill to examples, scenarios, expected answer kind, and claim boundary.
- LEAD: Add dashboard tests that compare generated summary rows to `scenario_summary()` and `load_examples()` output.
- LEAD: Keep scenario fixtures deterministic and local; do not call live Claude, Codex, Hermes, Gemini, Perplexity, browsers, or OSINT connectors.

## EXPAND
- LEAD: Evidence ladder traceability matrix - WHY: current gates prove presence, not easy auditability - ANGLE: generated JSON/Markdown from existing loaders.
- LEAD: Section-aware worked-example validation - WHY: keyword checks can pass low-quality examples - ANGLE: parse `examples/skill-worked-examples.yaml` into required labels and sections.
