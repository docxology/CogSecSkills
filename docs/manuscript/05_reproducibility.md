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

## Template Markdown/PDF Render Commands

Render and validate the manuscript with an installed sibling template checkout.
The public combined-render APIs accept this checkout directly; no template
project mirror or legacy `scripts/03_render_pdf.py` is required. Set the paths
below, and use the template environment that already has its rendering
dependencies installed (`--no-sync` preserves that environment).

```bash
export PROJECT_ROOT="${PROJECT_ROOT:-/path/to/CogSecSkills}"
export TEMPLATE_ROOT="${TEMPLATE_ROOT:-/path/to/template}"
cd "${TEMPLATE_ROOT}"
uv run --no-sync python -m infrastructure.validation.cli markdown "${PROJECT_ROOT}/docs/manuscript" --repo-root "${PROJECT_ROOT}"
uv run --no-sync python - <<'PYRENDER'
from dataclasses import replace
from pathlib import Path
import os
import yaml
from infrastructure.rendering import RenderManager, RenderingConfig
from infrastructure.rendering.manuscript_discovery import discover_manuscript_files

project = Path(os.environ["PROJECT_ROOT"]).resolve()
manuscript = project / "docs" / "manuscript"
source_config = yaml.safe_load((manuscript / "config.yaml").read_text())
config = replace(
    RenderingConfig.from_project_config(source_config, env={}),
    manuscript_dir=str(manuscript), figures_dir=str(project / "output/figures"),
    output_dir=str(project / "output"), pdf_dir=str(project / "output/pdf"),
    web_dir=str(project / "output/web"),
)
manager = RenderManager(config)
sources = [p for p in discover_manuscript_files(manuscript) if p.suffix == ".md"]
print(manager.render_combined_pdf(sources, manuscript, "CogSecSkills"))
print(manager.render_combined_web(sources, manuscript, "CogSecSkills"))
PYRENDER
pdftotext "${PROJECT_ROOT}/output/pdf/CogSecSkills_combined.pdf" - | rg "References|Supplemental 100-Skill Catalogue|Use when|Claim Provenance Verification|Taxonomy|Reference Density|Harness Contract|Evidence Ladder|Skill Worked Examples|Scenario Readiness|expected answers|Quality Dashboard|Release Manifest"
rg -n "Citation .*undefined|undefined references|LaTeX Warning: Reference.*undefined|Missing character|Package .* Error|File .* not found" "${PROJECT_ROOT}/output/pdf/_combined_manuscript.log"
```

Rendering updates the combined PDF under `output/pdf/` and HTML under
`output/web/`; the root `CogSecSkills.pdf` is a separately published copy and
must be refreshed only after verifying the new combined PDF. Preserve the
previous PDF or render a staged snapshot before replacing a release artifact.

The final `rg` command is expected to produce no matches. A nonzero exit status
from that command is acceptable when it means the searched error strings were
absent. Avoid broad `not found` log searches because some LaTeX packages emit
benign informational lines such as `pdfdraftmode not found`.

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
