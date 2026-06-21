# CogSecSkills Targeted Ultra-Research Synthesis

This local note records the narrow OmO research pass for the visual/release
hardening wave. It is audit context, not committed project documentation.

## Findings

- `release-metadata --check` was not post-commit stable because the generated
  Markdown and JSON embedded live git revision, branch, dirty, and availability
  fields. A stable release surface must avoid drift-checking values that change
  because the release commit exists.
- `dashboard --write` already had a strong payload model. Adding HTML as a third
  generated artifact from the same payload avoids a separate frontend state
  machine and keeps drift checks deterministic.
- The repo had an AGENTS hierarchy but no visual design contract. A root
  `DESIGN.md` is the appropriate durable surface for future cover, figure, PDF,
  and static-dashboard decisions.

## Execution Rule

Keep `.omo/` untracked. Commit only durable project files: source, tests,
design/docs, generated dashboards, generated release metadata, manuscript
assets, and verification text.
