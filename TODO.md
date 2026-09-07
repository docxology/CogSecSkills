# CogSecSkills TODO

Forward-only tracker for source-owned work. Keep history in completed changelog
or commit messages; keep this file focused on the current state and next useful
work.

## Verified State (re-measured 2026-09-07)

- Library gate: `validate` -> `0 error(s), 0 warning(s)`.
- Quality gate: `doctor` -> `validation: 0 error(s); quality: 0 finding(s)`.
- Definition gate: `definitions --check` -> `canonical definitions are current`.
- Scenario gate: `scenarios --check` -> `28 scenarios across 7 groups; 28 expected answers checked`.
- Example gate: `examples --check` -> `worked examples are current`.
- Eval gate: `evals --check` -> `offline evaluation fixtures are current`.
- Dashboard gate: `dashboard --check` -> `quality dashboard is current`.
- Release gate: `release-metadata --check` -> `release metadata is current (local mode)`.
- Manuscript gate: `manuscript-assets --check` -> `manuscript assets are current`.
- Test gate: `pytest --cov=cogsecskills --cov-fail-under=99` -> `899 passed`, `99.93% branch coverage`.
- Lint gate: `ruff check` + `ruff format --check` -> clean (81 files: 38 `src/` + 43 `tests/`).
- Type gate: `mypy` -> `no issues found in 38 source files` (requires the `dev` extra: `uv sync --extra dev` installs `types-pyyaml`; a bare env reports 11 `import-untyped` errors for `yaml` — the dev extra is the supported invocation).
- Python legs: all five CI matrix interpreters (3.10–3.14) verified locally — `899 passed` each; branch coverage 99.91% (3.10, `tomli` fallback branch taken) / 99.93% (3.11–3.14).

## Ongoing Guardrails

- Keep verification prose aligned with the exact latest gate run after any source edits.
- Rerun `manuscript-assets --write` and `--check` after registry or skill metadata changes.
- Rerun `definitions --write` and `--check` after canonical skill-definition changes.
- Rerun `scenarios --check` after scenario fixture or quality-field changes.
- Rerun `examples --write` and `--check` after worked-example source changes.
- Never hand-edit generated files; regenerate via the owning `--write` command (see `CLAUDE.md`).
- Preserve the defensive-only boundary; do not add offensive influence-operation playbooks.

## Discovered 2026-09-07 (session audit)

- MINOR — cleared: stale top-level `manuscript/S10_skill_catalogue.md` and
  `manuscript/S11_skill_metadata_matrix.md` were dead duplicates of the
  `docs/manuscript/` generated files left behind by the manuscript migration
  (`f860c60` moved the writers; nothing referenced the old copies). Deleted.
- MINOR — cleared: tracked `output/.DS_Store` macOS junk removed and `.DS_Store`
  added to `.gitignore`.
- MINOR — cleared: `docs/manuscript/MANUSCRIPT_STATUS.md` described its own
  legacy location as `docs/manuscript/` (migration find-replace artifact); the
  intended legacy top-level `manuscript/` references are restored.
- MINOR — cleared: CHANGELOG had no entry for post-v1.7.0 work (2026-07-29 →
  2026-09-01, including the Python 3.10 CI-leg fix); added an `Unreleased`
  section.
- MINOR — cleared: coverage-floor drift — `pyproject.toml` enforced `fail_under
  = 90` while CI enforced `--cov-fail-under=97` (and docs quoted 90.94% / 97);
  both now enforce 99 and README / AGENTS / ISA / tests / architecture docs
  agree.
- CI matrix 3.10–3.13 was missing Python 3.14 (GA and supported by
  `setup-uv`/`uv`); the matrix now includes 3.14 with a local full-suite
  verification (see `Minor: CI Hardening`).
- MINOR — cleared: `CONTRIBUTING.md` still quoted the 90% coverage gate (two
  spots) and a stdout-redirect catalogue command; aligned to the 99% gate and
  the canonical `catalogue --markdown --output docs/catalogue.md`.
- MINOR — cleared: `docs/cli.md`'s `show` example carried a stale skill
  version (`1.1.0`); the real `sat.sorting` version is `0.1.0`.
- MINOR — cleared: the `cli.py` module usage example pointed at
  `docs/skill_catalogue.md`; the canonical generated path is
  `docs/catalogue.md` (per `docs/cli.md` and `CLAUDE.md`).
- MINOR — cleared: `ISA.md` still described the project as living at the
  private template sidecar (`projects/working/CogSecSkills`); updated to the
  canonical public-repository reality (`docxology/CogSecSkills`, CI + Zenodo,
  template used only for render).
- MINOR — cleared: `CONTRIBUTING.md`'s setup block ran `pytest --cov` right
  after a plain `uv sync`, which does not install the `dev` extra
  (pytest/mypy/ruff); the block now uses `uv sync --extra dev`. The other
  `uv sync` install blocks (README, QUICKSTART, docs/harness-installation)
  only run core-CLI gates afterward and are correct as-is.
- MEDIUM — cleared: `catalogue` was the only generated output without a
  `--check` drift gate (CLAUDE.md listed `docs/catalogue.md` as generated, CI
  gated the other eight surfaces); added `catalogue --check` (default target
  `docs/catalogue.md`, `--output` overrides) with contract tests and a CI
  coherence-gate step.
- MEDIUM — cleared: CI installed with `uv pip install -e ".[dev,figures]"`,
  resolving fresh from PyPI and ignoring `uv.lock` (a new ruff/pytest release
  could break CI with no repo change); CI now runs
  `uv sync --locked --extra dev --extra figures`, plus a workflow
  `concurrency` group so superseded runs cancel.
- MINOR — cleared: `validate_skill` had no way to drive its
  "cannot realise verbs" branch with real inputs (all default harnesses
  support the full verb set), so its test monkeypatched the internal
  `check_conformance` call against the no-mocks rule; `validate_skill` now
  exposes the same `support` seam as `check_conformance` and the test uses it.
- MINOR — cleared: three tests asserted only `len(findings) > 0` on
  deterministic error paths (unknown example skill id, definitions with no
  on-disk skill ×2); tightened to pin the exact finding strings.
- MINOR — cleared: stale gate numbers survived in `CLAUDE.md` (">=90%"
  coverage comment), `tests/AGENTS.md` and `src/cogsecskills/AGENTS.md`
  (`--cov-fail-under=97`); all aligned to 99.
- MINOR — cleared: `ISA.md` frontmatter `progress:` and the timeless ISC-6/7/17
  evidence line still carried v1.7.0-release-era numbers (873 tests/98.84%);
  frontmatter and evidence updated to the measured 2026-09-07 state, dated
  verification entry appended.
- MINOR — cleared: `.zenodo.json` still said version `1.0.0` while
  CITATION.cff/codemeta.json/pyproject say 1.7.0; aligned.
- MINOR — cleared: `docs/manuscript/MANUSCRIPT_STATUS.md` cited
  `infrastructure.core.project_paths.resolve_manuscript_dir`, a symbol that
  exists nowhere (the template's real resolver is
  `infrastructure.publishing.export_bundle.resolve_source_manuscript_dir`);
  dropped the brittle cross-repo citation in favor of the semantic fallback
  note.

## Minor: Coverage

- Maintain 99.9%+ test coverage across all modules (`examples.py`, `scenarios.py`, `definitions.py`, `validate.py`, `author.py`, `dashboard.py`, `evals.py`, `figure_helpers.py`, `tables.py`, `loader.py`, `registry.py` all at 99%+ to 100%).
- Ensure any newly authored utility or artifact renderer includes full branch coverage fixtures.

## Minor: CI Hardening

- Maintain the `--cov-fail-under=99` CI gate and keep it in agreement with
  `pyproject.toml` `fail_under` (raised from 90/97 on 2026-09-07; every matrix
  leg measured locally: 99.91% on 3.10 with the `tomli` fallback branch taken,
  99.93% on 3.11–3.14).

## Medium: Skill Definition Depth

- Audit all 100 canonical definitions periodically for potential domain deepening in evidence requirements and uncertainty handling.
- Expand scholarly anchors and reference density across emerging intelligence literature.

## Medium: Manuscript Refresh

- Re-render the manuscript PDF from the live library after v1.7.0 updates.
- Re-run template markdown validation and PDF render pipeline to update PDF artifacts.
- Verified 2026-09-07: the root `CogSecSkills.pdf` still renders the v1.0.0-era
  manuscript (last PDF-touching commit `79da8bd`, 2026-06-22) while the library
  is at 1.7.x and the generated supplements are current. Re-rendering needs the
  sibling docxology template working copy (`../template` with
  `projects/working/CogSecSkills`) and XeLaTeX; not run in this session.

## Medium: AGEINT Docs

- Verified 2026-08-30: each group primer in `docs/ageint/` names many concrete
  skills from its group inline (e.g. `cognitive-security.md` names 20+ of 24);
  cross-references are active. Periodically re-audit against the 100-skill
  taxonomy as definitions deepen.

## Major: Empirical Evaluation

- Design a live-runtime eval harness capable of invoking Claude/Codex/Hermes with scenario fixtures and scoring outputs against expected-answer rubrics.
- Use `docs/analyst-output-review.md` as the initial rubric for offline and online review.
- Label any comparison against unstructured prompting as exploratory unless externally reviewed.

## Major: Live Connector Integrations

- Add connector-specific OSINT/web harness notes only when live connectors are intentionally wired.
- Require privacy/legal checks, source custody, rate-limit handling, and connector-specific tests before describing a connector as supported.
- Document the connector boundary in `docs/connector-boundaries.md` when a live connector is wired.

## Major: External Publication / DOI

- Update `CITATION.cff` and `codemeta.json` with new version DOI once deposited on Zenodo.
- Add verified external citations only when a manuscript claim needs external literature rather than project-local evidence.
