# Ultraresearch Synthesis: CogSecSkills OmO Initialization

Workers: 6 spawned, 5 returned with findings, 1 timed out on a duplicate
manuscript lane. Waves: 1 first wave plus local verification. Sources:
repository files, code graph architecture, official harness documentation, and
executed local/template gates.

## Executive Summary

The pass found no material drift in CogSecSkills' core implementation claims.
The live code graph and source inspection show a clear data flow: `registry/`
plans the library, `definitions/` owns skill substance, `skills/` is rendered
harness-facing output, `scenarios/` owns deterministic local readiness
fixtures, and `dashboard.py` plus `manuscript_assets.py` generate review and
manuscript surfaces. Proof: `validate`, `report`, `doctor`, definitions,
scenarios, dashboard, manuscript-assets, pytest coverage, ruff, mypy, and
template render gates all passed in this session.

The actionable gap was local agent guidance, not runtime functionality. Before
this pass, only root and manuscript AGENTS files existed. This pass added
subtree AGENTS guidance for implementation code, canonical definitions,
rendered skills, registries, scenarios, docs, and tests, then locked that
hierarchy with a new contract test.

Optional harness wording also needed more precision. Official documentation
distinguishes product-specific context files, custom-instruction surfaces,
rules/skills, application frameworks, and tool protocols. The docs and
manuscript now state that optional profiles are documentation metadata until
configured, regenerated, reviewed, and validated.

## Findings By Theme

### Source Ownership

- `AGENTS.md` now names every source surface and the local AGENTS hierarchy.
- `definitions/AGENTS.md` says canonical YAML owns skill substance and rendered
  `skills/**` files must not be hand-edited as the durable source.
- `skills/AGENTS.md` states rendered skill files are harness-facing build
  output.
- `scenarios/AGENTS.md` records that `expected_answer` blocks are reviewed
  local fixtures, not live model outputs.
- `docs/AGENTS.md` states `quality-dashboard.md` is generated and keeps the
  default/configured/documented harness-status labels local.

### Optional Harness Profiles

- Gemini CLI documentation supports product-specific context files such as
  `GEMINI.md` and configured alternatives such as `AGENTS.md`:
  https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/gemini-md.md
- GitHub Copilot documentation separates repository-wide, path-specific, and
  agent instructions:
  https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions
- MCP documentation defines MCP as an open-source standard for connecting AI
  applications to external systems, not a model harness:
  https://modelcontextprotocol.io/docs/getting-started/intro
- The docs and manuscript now describe optional profiles by class rather than as
  one interoperable instruction standard.

### Verification

- `definitions --check`: canonical definitions are current.
- `scenarios --check`: 14 scenarios across 7 groups; 14 expected answers checked.
- `dashboard --check`: quality dashboard is current.
- `manuscript-assets --check`: manuscript assets are current.
- `validate`: 0 errors, 0 warnings.
- `report`: 100 registry entries, 100 implemented, 100 on-disk skills, ok true.
- `doctor`: validation 0 errors; quality 0 findings.
- Focused docs/manuscript/dashboard/AGENTS tests: 37 passed.
- Full pytest coverage gate: 609 passed, total coverage 92.60%.
- `ruff check`: all checks passed.
- `ruff format --check`: 32 files already formatted.
- `mypy`: no issues found in 16 source files.
- Template markdown validation: no issues found.
- Template PDF render: 13 sections rendered, 8/8 figures found.
- PDF content smoke: required scenario, dashboard, harness profile, catalogue,
  and GitHub installation strings found.
- PDF log scan: no unresolved-reference, missing-character, missing-file,
  package-error, LaTeX-error, fatal-error, or emergency-stop findings.

## Changed Durable Surfaces

- Added AGENTS hierarchy files under `src/cogsecskills/`, `definitions/`,
  `skills/`, `registry/`, `scenarios/`, `docs/`, and `tests/`.
- Updated root and manuscript AGENTS guidance.
- Tightened optional harness profile wording in docs and manuscript methods.
- Added `tests/test_cogsecskills_agents_contract.py`.
- Updated exact verified counts in TODO, ISA, architecture docs, release
  manifest, and regenerated the quality dashboard.

## Gaps

- One read-only manuscript worker did not return. The lane was not a blocker
  because the same surface was verified by direct tests, markdown validation,
  PDF rendering, PDF text smoke, and log scanning.
- No live external agent runtime, connector, release, DOI, or field evaluation
  was performed.

