# Release Checklist

This checklist is for preparing a local release candidate for
`github.com/docxology/CogSecSkills`. It does not publish, tag, or archive a
release by itself.

## Source Gates

```bash
PYTHONPATH="src:." python -m cogsecskills definitions --write
PYTHONPATH="src:." python -m cogsecskills definitions --check
PYTHONPATH="src:." python -m cogsecskills scenarios --check
PYTHONPATH="src:." python -m cogsecskills examples --write
PYTHONPATH="src:." python -m cogsecskills examples --check
PYTHONPATH="src:." python -m cogsecskills evals --write
PYTHONPATH="src:." python -m cogsecskills evals --check
PYTHONPATH="src:." python -m cogsecskills dashboard --write
PYTHONPATH="src:." python -m cogsecskills dashboard --check
PYTHONPATH="src:." python -m cogsecskills manuscript-assets --write
PYTHONPATH="src:." python -m cogsecskills manuscript-assets --check
PYTHONPATH="src:." python -m cogsecskills release-metadata --write
PYTHONPATH="src:." python -m cogsecskills release-metadata --check
PYTHONPATH="src:." python -m cogsecskills validate
PYTHONPATH="src:." python -m cogsecskills report
PYTHONPATH="src:." python -m cogsecskills doctor
PYTHONPATH="src:." python -m pytest tests/test_cogsecskills_*.py tests/test_skill_library_conformance.py --cov=src/cogsecskills --cov-report=term-missing
git diff --check
```

## Style And Type Gates

```bash
uv run ruff check src/cogsecskills tests
uv run ruff format --check src/cogsecskills tests
uv run mypy
```

## Manuscript Gates

From the sibling template checkout:

```bash
uv run python -m infrastructure.validation.cli markdown projects/working/CogSecSkills/manuscript/
uv run python scripts/03_render_pdf.py --project working/CogSecSkills
pdftotext /Users/4d/Documents/GitHub/projects/working/CogSecSkills/output/pdf/CogSecSkills_combined.pdf - | rg "Evidence Ladder|Skill Worked Examples|Scenario Readiness|expected answers|Quality Dashboard|Supplemental 100-Skill Catalogue|github.com/docxology/CogSecSkills"
rg -n "Citation .*undefined|undefined references|LaTeX Warning: Reference.*undefined|Missing character|Package .* Error|File .* not found|^!|LaTeX Error|Fatal error|Emergency stop" /Users/4d/Documents/GitHub/projects/working/CogSecSkills/output/pdf/_combined_manuscript.log
```

## Human Review

- Confirm `TODO.md` reflects only forward-looking work.
- Confirm `manuscript/references.bib` contains verified entries only.
- Confirm generated files carry generated headers where expected.
- Confirm claim wording stays local: structural conformance and deterministic
  readiness, not field effectiveness.
- Confirm any release tag or archive DOI is real before adding it to prose.
