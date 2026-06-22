# Manuscript Agent Notes - CogSecSkills

This directory follows the docxology/template manuscript contract:

- `00_` through `09_` files are main sections.
- `S01_` and `S02_` files are authored supplemental material.
- `S10_skill_catalogue.md` and `S11_skill_metadata_matrix.md` are generated
  supplements; do not edit them directly.
- `98_` and `99_` files are back matter.
- Every manuscript section file starts with one H1 and a stable `{#sec:...}` label.
- Citations must use Pandoc syntax and resolve in `references.bib`.
- Canonical skill substance belongs in `definitions/<group>/<slug>.yaml`; the
  `skills/` tree is rendered from those definitions.
- Curated scenario readiness fixtures belong in
  `scenarios/defensive_readiness.yaml`; they are local route/contract checks,
  not live model evaluations.
- Generated library catalogue and figure content belongs behind
  `src/cogsecskills/artifacts/manuscript_assets/__init__.py`, not hard-coded prose.

## Editing Rules

- Do not fabricate results, benchmark numbers, citations, DOIs, or release claims.
- Keep `references.bib` limited to verified entries; if a DOI cannot be verified
  from an authoritative source, cite the URL without a DOI.
- Keep `S02_release_manifest.md` aligned with the latest completed local gates.
- Keep scenario claims aligned with `python -m cogsecskills scenarios --check`.
- Keep project-specific computation in source modules and scripts; keep manuscript files as prose and evidence maps.
- Prefer explicit paths to source surfaces when describing evidence.
- Figures referenced by the main manuscript must exist under `../output/figures/`
  and be produced by `python -m cogsecskills manuscript-assets --write` unless
  a future source-owned producer is documented.
- If generated supplements drift, update the generator or source metadata, then
  rerun `PYTHONPATH="src:." python -m cogsecskills manuscript-assets --write`.
- If rendered skills drift, update canonical definitions and rerun
  `PYTHONPATH="src:." python -m cogsecskills definitions --write`.

## Current Scope

A defensive, educational, harness-neutral library of Cognitive Security and analytic tradecraft skills with registry, AGEINT upstream, and conformance tests.

Evidence boundary: Keep the manuscript focused on the skills system. Local
validation supports claims about source coherence and render readiness, not
field efficacy or public release status.
