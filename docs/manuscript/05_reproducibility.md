# Reproducibility, Local Verification, and Render Gates {#sec:reproducibility}

## Project-Local Asset and Validation Commands

Run project-local gates from a checked-out CogSecSkills project root:

```bash
export PROJECT_ROOT="${PROJECT_ROOT:-/path/to/CogSecSkills}"
cd "${PROJECT_ROOT}"
uv sync --locked --extra dev --extra figures
uv run python -m cogsecskills definitions --write
uv run python -m cogsecskills definitions --check
uv run python -m cogsecskills scenarios --check
uv run python -m cogsecskills examples --write
uv run python -m cogsecskills examples --check
uv run python -m cogsecskills evals --write
uv run python -m cogsecskills evals --check
uv run python -m cogsecskills dashboard --write
uv run python -m cogsecskills dashboard --check
uv run python -m cogsecskills release-metadata --write
uv run python -m cogsecskills release-metadata --check
uv run python -m cogsecskills catalogue --markdown --output docs/catalogue.md
uv run python -m cogsecskills catalogue --check
uv run python -m cogsecskills manuscript-assets --write
uv run python -m cogsecskills manuscript-assets --check
uv run python -m cogsecskills validate
uv run python -m cogsecskills report
uv run python -m cogsecskills doctor
uv run pytest --cov=cogsecskills --cov-report=term-missing --cov-fail-under=99
```

`definitions --write` must run before rendering whenever skill substance or configured harnesses change. `definitions --check` should then pass before manuscript assets are regenerated. `scenarios --check` should pass before treating curated safe-use, unsafe-redirect, expected response-shape, and expected-answer fixtures as current. `examples --write` and `examples --check` keep the generated 100-skill worked-example views synchronized with their source YAML. `dashboard --write` should run after TODO, scenario, example, registry, or skill metadata changes, and `dashboard --check` should then pass before the Markdown, HTML, and JSON dashboard views are treated as current. `release-metadata --write` keeps committed release metadata deterministic by omitting exact git revision, branch, and dirty-state values from drift-checked files; those values are runtime observations used by stricter release modes. `manuscript-assets --write` must run before rendering whenever registry or rendered skill metadata changes. `manuscript-assets --check` should then pass with no findings; otherwise the committed manuscript sources and figures no longer match the live library.

## Pinned Template Render and Validation

Use a clean disposable checkout registered as `projects/working/CogSecSkills` in the pinned docxology/template workspace. Keep `docs/manuscript/` and its checked-in figure and evidence inputs available. From the Template checkout, run the combined PDF and HTML render followed by validation.

```bash
uv run --no-sync python scripts/pipeline/stage_03_render.py --project working/CogSecSkills
uv run --no-sync python scripts/pipeline/stage_04_validate.py --project working/CogSecSkills
```

The render writes `output/pdf/CogSecSkills_combined.pdf` and `output/web/index.html` in the disposable project. Validation checks the figure registry and manuscript evidence against local files. The separately published artifacts retain their own release identity.

## Traceability and Render Contract

- Do not cite results that cannot be regenerated or directly traced.
- Keep generated outputs under `output/` and manuscript source under `docs/manuscript/`.
- Keep private data, credentials, and unpublished sensitive details out of the manuscript.
- Treat `scenarios/defensive_readiness.yaml` as a curated local fixture set for route, quality-contract, and expected-answer readiness, not as empirical validation.
- Treat `examples/skill-worked-examples.yaml`, `docs/skill-worked-examples.md`, and `output/data/skill_worked_examples.json` as deterministic local worked-example fixtures, not live model transcripts.
- Treat `docs/quality-dashboard.md` and `output/data/quality_dashboard.json` as generated navigation and drift surfaces, not as field-effectiveness evidence.
- Treat `docs/manuscript/S10_skill_catalogue.md`, `docs/manuscript/S11_skill_metadata_matrix.md`, `output/data/skill_catalogue.*`, and the eight `output/figures/*.png` manuscript figures as generated from source-owned inputs.
- Record exact verification command results before making release or publication claims.
- Keep repository URL, version, license, source revision, environment versions,
  lockfile presence, figure inventory, and gate results current in
  @sec:release_manifest before representing the manuscript as a release
  snapshot [@smith2016softwareCitation].

The narrow PDF margin is part of the render contract because the generated catalogue and metadata matrix are table-heavy. Any future margin change should be checked in the rendered PDF, not only in Markdown, so long labels, figure captions, and long-table cells remain readable.
