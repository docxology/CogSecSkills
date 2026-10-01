# CogSecSkills TODO

Forward-only tracker for source-owned work. Keep history in completed changelog
or commit messages; keep this file focused on the current state and next useful
work.

## Verified State (v1.8.0, re-measured 2026-10-01)

The v1.8.0 local release candidate and rendered artifacts pass the checks
below. Hosted CI, GitHub asset publication, and Zenodo version acceptance are
separate verification steps. The prior v1.7.0 review remains historical.

- Library gate: `validate` -> `0 error(s), 0 warning(s)`.
- Quality gate: `doctor` -> `validation: 0 error(s); quality: 0 finding(s)`.
- Definition gate: `definitions --check` -> `canonical definitions are current`.
- Scenario gate: `scenarios --check` -> `28 scenarios across 7 groups; 28 expected answers checked`.
- Example gate: `examples --check` -> `worked examples are current`.
- Eval gate: `evals --check` -> `offline evaluation fixtures are current`.
- Dashboard gate: `dashboard --check` -> `quality dashboard is current`.
- Release gate: `release-metadata --check` -> `release metadata is current (local mode)`.
- Manuscript gate: `manuscript-assets --check` -> `manuscript assets are current`.
- Test gate: `uv run pytest --cov=cogsecskills --cov-report=term-missing --cov-fail-under=99` -> `1248 passed in 276.31s`, `99.65% total coverage` with branch measurement enabled (Python 3.14.4, macOS).
- Lint gate: `uv run ruff check src/cogsecskills tests` + `uv run ruff format --check src/cogsecskills tests` -> clean; 108 files already formatted.
- Type gate: `uv run mypy` -> `Success: no issues found in 51 source files`; use `uv sync --locked --extra dev --extra figures` for the complete development environment.
- Installed wheel: v1.8.0 runtime-only isolated environments on Python 3.14.4 and 3.10.20 pass version, doctor, definitions, and scenarios from an unrelated working directory with `--root`; default doctor from the library checkout also passes.
- Python legs: CI remains configured for 3.10–3.14; this review verified Python 3.14.4 locally. The full current matrix and hosted checks are deferred to the eventual published revision.
- Manuscript: the v1.8.0 71-page local PDF and HTML retain all 100 catalogue rows; root/output PDFs have identical hashes. Receipt: [`docs/release-1.8.0-acceptance.md`](docs/release-1.8.0-acceptance.md).
- Independent review: artifact and runtime custody repros pass after repair; historical review details and limits remain in [`docs/review-2026-10-01.md`](docs/review-2026-10-01.md); current release acceptance is recorded separately.

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

- Maintain the declared 99% total coverage floor with branch measurement enabled.
- Add meaningful real-file and real-process regressions for new contracts and failure cases; preserve platform limits explicitly.

## Minor: CI Hardening

- Maintain the `--cov-fail-under=99` CI gate and keep it in agreement with
  `pyproject.toml` `fail_under` (raised from 90/97 on 2026-09-07; every matrix
  leg measured locally: 99.91% on 3.10 with the `tomli` fallback branch taken,
  99.93% on 3.11–3.14).

## Minor: Build Metadata

- Preserve SPDX license metadata and the declared setuptools minimum; repeat
  wheel and sdist acceptance when build metadata changes, including the oldest
  supported Python and declared minimum backend.

## Medium: Skill Definition Depth

- Audit all 100 canonical definitions periodically for potential domain deepening in evidence requirements and uncertainty handling.
- Expand scholarly anchors and reference density across emerging intelligence literature.

## Medium: Manuscript Maintenance

- Verified v1.7.0 baseline on 2026-10-01: the root and output PDFs are identical
  local renders (71 pages, cover plus seven body figures, all 100 skill
  identifiers). HTML retains all 100 catalogue rows. Render/content/visual
  receipts and artifact hashes are in `docs/review-2026-10-01.md`.
- Verified v1.8.0 local render on 2026-10-01: both retained PDFs are identical;
  PDF and HTML retain all 100 skills. The new hashes and content/layout evidence
  are in `docs/release-1.8.0-acceptance.md`.
- Repeat source validation and rendering after future source changes. The
  explicit combined-render APIs in
  `docs/manuscript/05_reproducibility.md` use the installed sibling template and
  XeLaTeX against this checkout directly.
- Keep an updated archive deposit separate from local render acceptance.

## Medium: AGEINT Docs

- Verified 2026-08-30: each group primer in `docs/ageint/` names many concrete
  skills from its group inline (e.g. `cognitive-security.md` names 20+ of 24);
  cross-references are active. Periodically re-audit against the 100-skill
  taxonomy as definitions deepen.

## Major: Empirical Evaluation

- Implemented 2026-09-07 (not fully cleared): the live-runtime eval harness
  ships (`eval-live`, `runtime_eval.py`, `docs/live-eval.md`) — real harness
  subprocesses, deterministic transcript screening against scenario contracts,
  mechanical rubric screening, claim-bounded reports, and a config seam for
  any harness CLI. Run against a real Claude Code invocation
  (sat-ach-safe: 6/7 checks; missing section headers flagged) plus 12
  no-mock tests.
- Remaining: human-rubric review of live transcripts
  (`docs/analyst-output-review.md`) and any comparison against unstructured
  prompting stays exploratory until externally reviewed; per-run cost means
  no scheduled live runs in CI.

## Major: Live Connector Integrations

- Add connector-specific OSINT/web harness notes only when live connectors are intentionally wired.
- Require privacy/legal checks, source custody, rate-limit handling, and connector-specific tests before describing a connector as supported.
- Document the connector boundary in `docs/connector-boundaries.md` when a live connector is wired.
- Scoped 2026-09-07: see `docs/cross-repo-scoping.md` §2 — preferred seam is
  wrapping the platform `hum-search` process contract, declared via
  `runtime_eval.harness_commands`-style config rather than direct provider SDKs.

## Major: External Publication / DOI

- Publish the authorized v1.8.0 GitHub release with verified public assets and
  source identity; follow `docs/release-checklist.md`.
- Verify the resulting Zenodo version record under concept
  `10.5281/zenodo.21513316`, its version/source identity, and attached files.
  Record an actual new version DOI in citation/manuscript metadata only after
  verifying its reservation or publication status; see
  `docs/cross-repo-scoping.md` §3.
- Preserve the separate historical v1.0.0 manuscript archive and explicitly
  distinguish the existing software record's v1.7.0 source link from its stale
  `1.0.0` version metadata.
- Add verified external citations only when a manuscript claim needs external literature rather than project-local evidence.
