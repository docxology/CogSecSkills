# Reproducibility and Render Gates {#sec:reproducibility}

## Project-Local Asset and Validation Commands

Run project-local gates from a checked-out CogSecSkills project root:

```bash
export PROJECT_ROOT="${PROJECT_ROOT:-/path/to/CogSecSkills}"
cd "${PROJECT_ROOT}"
PYTHONPATH="src:." python -m cogsecskills definitions --write
PYTHONPATH="src:." python -m cogsecskills definitions --check
PYTHONPATH="src:." python -m cogsecskills scenarios --check
PYTHONPATH="src:." python -m cogsecskills examples --write
PYTHONPATH="src:." python -m cogsecskills examples --check
PYTHONPATH="src:." python -m cogsecskills dashboard --write
PYTHONPATH="src:." python -m cogsecskills dashboard --check
PYTHONPATH="src:." python -m cogsecskills manuscript-assets --write
PYTHONPATH="src:." python -m cogsecskills manuscript-assets --check
PYTHONPATH="src:." python -m cogsecskills validate
PYTHONPATH="src:." python -m cogsecskills report
PYTHONPATH="src:." python -m cogsecskills doctor
PYTHONPATH="src:." python -m pytest tests/test_cogsecskills_*.py tests/test_skill_library_conformance.py --cov=src/cogsecskills --cov-report=term-missing
```

`definitions --write` must run before rendering whenever skill substance or configured harnesses change. `definitions --check` should then pass before manuscript assets are regenerated. `scenarios --check` should pass before treating curated safe-use, unsafe-redirect, expected response-shape, and expected-answer fixtures as current. `examples --write` and `examples --check` keep the generated 100-skill worked-example views synchronized with their source YAML. `dashboard --write` should run after TODO, scenario, example, registry, or skill metadata changes, and `dashboard --check` should then pass before the dashboard is treated as current. `manuscript-assets --write` must run before rendering whenever registry or rendered skill metadata changes. `manuscript-assets --check` should then pass with no findings; otherwise the committed manuscript sources and figures no longer match the live library.

## Template Markdown/PDF Render Commands

Render and validate the manuscript through the sibling template checkout. Use
repository-relative paths or environment variables; do not rely on author-local
absolute filesystem paths.

```bash
export PROJECT_ROOT="${PROJECT_ROOT:-/path/to/CogSecSkills}"
export TEMPLATE_ROOT="${TEMPLATE_ROOT:-/path/to/template}"
cd "${TEMPLATE_ROOT}"
uv run python -m infrastructure.validation.cli markdown projects/working/CogSecSkills/manuscript/
uv run python scripts/03_render_pdf.py --project working/CogSecSkills
pdftotext "${PROJECT_ROOT}/output/pdf/CogSecSkills_combined.pdf" - | rg "References|Supplemental 100-Skill Catalogue|Use when|Claim Provenance Verification|Taxonomy|Reference Density|Harness Contract|Evidence Ladder|Skill Worked Examples|Scenario Readiness|expected answers|Quality Dashboard|Release Manifest"
rg -n "Citation .*undefined|undefined references|LaTeX Warning: Reference.*undefined|Missing character|Package .* Error|File .* not found" "${PROJECT_ROOT}/output/pdf/_combined_manuscript.log"
```

The final `rg` command is expected to produce no matches. A nonzero exit status
from that command is acceptable when it means the searched error strings were
absent. Avoid broad `not found` log searches because some LaTeX packages emit
benign informational lines such as `pdfdraftmode not found`.

## Traceability and Render Contract

- Do not cite results that cannot be regenerated or directly traced.
- Keep generated outputs under `output/` and manuscript source under `manuscript/`.
- Keep private data, credentials, and unpublished sensitive details out of the manuscript.
- Treat `scenarios/defensive_readiness.yaml` as a curated local fixture set for route, quality-contract, and expected-answer readiness, not as empirical validation.
- Treat `examples/skill-worked-examples.yaml`, `docs/skill-worked-examples.md`, and `output/data/skill_worked_examples.json` as deterministic local worked-example fixtures, not live model transcripts.
- Treat `docs/quality-dashboard.md` and `output/data/quality_dashboard.json` as generated navigation and drift surfaces, not as field-effectiveness evidence.
- Treat `manuscript/S10_skill_catalogue.md`, `manuscript/S11_skill_metadata_matrix.md`, `output/data/skill_catalogue.*`, and the eight `output/figures/*.png` manuscript figures as generated from source-owned inputs.
- Record exact verification command results before making release or publication claims.
- Keep repository URL, version, license, source revision, environment versions,
  lockfile presence, figure inventory, and gate results current in
  @sec:release_manifest before representing the manuscript as a release
  snapshot [@smith2016softwareCitation].

The narrow PDF margin is part of the render contract because the generated catalogue and metadata matrix are table-heavy. Any future margin change should be checked in the rendered PDF, not only in Markdown, so long labels, figure captions, and long-table cells remain readable.
