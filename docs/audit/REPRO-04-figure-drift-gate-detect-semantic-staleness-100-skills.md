# REPRO-04: Figure drift gate cannot detect semantic staleness; '100 skills' is hard-coded in figure code

|Field|Value|
|---|---|
|Audit ID|`REPRO-04`|
|Lens|`REPRO`|
|Severity|`medium`|
|Red-team verdict|`ADJUSTED`|
|Status|Open (validated 2026-09-10)|
| Tracking | [GitHub issue](https://github.com/docxology/CogSecSkills/issues/41) |

## Summary
The committed PNG drift gate checks only structural properties (header validity, byte floor, pixel floor, mutual distinctness) and deliberately avoids byte-exact comparison, so rendered figures can silently diverge from the live registry. The count '100' is hard-coded in the figure title, reader question, keywords, and the supplemental catalogue heading, and is never cross-checked against the actual registry length at generation time — if the catalogue ever grows past 100, the figure text stays frozen at "all 100 implemented skills" with no gate failing. Verdict was adjusted (not outright VALID) because the conformance test `assert len(registry) == 100` and multiple other independent gates pin the registry count, limiting the residual defect to figure/catalogue text semantics; severity confirmed medium.

## Evidence
- `src/cogsecskills/artifacts/manuscript_assets/png_probe.py:1-58` — the PNG gates are header validity, byte floor (`MIN_FIGURE_BYTES = 100_000`), pixel floor (`MIN_FIGURE_PIXELS = 1_000`), and mutual distinctness ('Byte floor — a blank figure... compresses to roughly 37 KB, while the smallest real figure is over 300 KB'). Per its docstring, an exact-bytes gate would flap, so byte-comparison is deliberately not used.
- `src/cogsecskills/artifacts/manuscript_assets/figure_specs.py:33-34` — 'Can the reader scan all 100 skills as one compact library surface?' and `('100 skills', 'library atlas', 'group')`.
- `src/cogsecskills/artifacts/manuscript_assets/figure_diagrams.py:199` — `"Library atlas of all 100 implemented skills"`.
- `src/cogsecskills/artifacts/manuscript_assets/tables.py:74` — `# Supplemental 100-Skill Catalogue {#sec:supplemental_skill_catalogue}`.
- Verifier path correction: the conformance test is `tests/conformance/test_skill_library_conformance.py:43` — `assert len(registry) == 100, "the catalogue is defined as 100 skill areas"` — not `tests/` root. Its failure catches registry growth but not stale PNG/text semantics.
- No test compares the figure labels/reader questions to `len(registry)`, and the PNG drift gate never re-verifies the text frozen inside the PNGs.

## Impact
Matplotlib output is deliberately not byte-compared, so figure text baked into committed PNGs can silently become semantically stale: if the catalogue grows beyond 100, the rendered figure still says "all 100 implemented skills" while every registry-level gate (conformance test, dashboard, examples, ISA.md ISC-1) fails on the count. The registry itself cannot grow silently — but the figure/catalogue prose that readers actually see can, and nothing catches the divergence. Contributor/maintenance cost: the hard-coded literals must be found and updated by hand in four separate places whenever the count changes.

## Remediation
1. In `src/cogsecskills/artifacts/manuscript_assets/figure_specs.py` / `figure_diagrams.py` / `tables.py`, build the '100' count strings from the live registry length (e.g. `len(rows)`) instead of hard-coded literals, so a catalogue change automatically updates the figure labels.
2. Alternatively (or additionally), add a test comparing the reader questions/labels/keywords in `figure_specs.py` and the heading in `tables.py` against the registry count (mirroring `tests/conformance/test_skill_library_conformance.py:43`), so label-vs-registry drift fails CI even if the literals remain.

## Audit trail
- Discovered by the REPRO lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `ADJUSTED`, confidence `high`.
- Verifier notes: All four quotes confirmed verbatim at cited lines. The hard-coded '100' strings in figure title/reader-question/keywords and catalogue heading are never cross-checked against the live registry: the PNG drift gate is structural only (dimensions/bytes, deliberately not byte-exact per docstring), and no test compares figure labels to len(registry). Path correction: the conformance test is tests/conformance/test_skill_library_conformance.py:43 (`assert len(registry) == 100, "the catalogue is defined as 100 skill areas"`), not tests/ root — its failure catches registry growth but not stale PNG/text semantics, exactly as argued. Multiple independent gates (dashboard, examples, ISA.md ISC-1) also pin == 100, so growth cannot ship silently via the registry; the residual defect is limited to figure/catalogue text drift, supporting medium rather than low. Fix suggestion (derive label from len(rows) or add label-vs-registry test) is sound.
<!-- PR and issue links are added to the Tracking field after filing. -->