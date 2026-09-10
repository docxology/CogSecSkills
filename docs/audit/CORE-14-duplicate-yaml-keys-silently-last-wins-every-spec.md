# CORE-14: Duplicate YAML keys are silently last-wins in every spec/config/registry load path

|Field|Value|
|---|---|
|Audit ID|`CORE-14`|
|Lens|`CORE`|
|Severity|`low`|
|Red-team verdict|`ADJUSTED`|
|Status|Open (validated 2026-09-10)|
|Tracking|PENDING-ISSUE-LINK|

## Summary
Every YAML load path in the codebase uses plain `yaml.safe_load`, which silently keeps the last occurrence of a duplicated mapping key with no diagnostic — so a `skill.yaml` or `cogsecskills.yaml` with `status:` twice takes whichever appears later. This contradicts the library's "malformed input raises with a precise message" doctrine. The red team adjusted the verdict to ADJUSTED because all cited line numbers in the original finding were stale, though the mechanism itself was confirmed — and the blast radius is larger than stated, since `artifacts/` load sites are also affected.

## Evidence
`src/cogsecskills/core/loader.py:48` (original cited line 41; corrected by verifier):

```python
raw = yaml.safe_load(spec_path.read_text(encoding="utf-8"))
```

Same pattern at `core/config.py:65`, `core/registry.py:111` and `:125`, `authoring/author.py:138`, plus `artifacts/evals.py:151`, `artifacts/examples.py:90`, `artifacts/release_metadata.py:57`, `artifacts/scenarios.py:277`, `artifacts/manuscript_assets/figure_helpers.py:195`. The doctrine at `spec.py:11-12` (module docstring): "All parsing is total: malformed input raises SpecError with a precise message rather than producing a half-built object" — repeated at `docs/architecture.md:149`. The verifier grepped for `add_constructor`/duplicate-key handling across `src/` and `tests/` and found none; existing duplicate checks only cover duplicate ids within parsed lists (e.g. `registry.py:118-119`), never a duplicated key within one mapping.

## Impact
A duplicated key — precisely the kind of authoring mistake the parsing doctrine says to surface — silently resolves to one of two valid values. In many cases downstream validation catches the consequence, but nothing flags the input mistake itself, and the affected surface is larger than the finding stated (all `artifacts/` load sites too).

## Remediation
Add a shared helper (e.g. a `SafeConstructor` subclass that raises on duplicate mapping keys, registered via `yaml.add_constructor`) in `core/loader.py` and use it at every YAML load site — `loader.py`, `config.py`, `registry.py`, `authoring/author.py`, and the `artifacts/` loaders. Add a test with a duplicated `status:` key asserting a precise error naming the file and key.

## Audit trail
- Discovered by the CORE lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `ADJUSTED`, confidence `high`.
- Verifier notes: Re-derived: (1) quote text is verbatim but all cited line numbers are stale/wrong — loader.py:41 is actually 48, config.py:56 is 65, registry.py:110/126 are 111/125, author.py:103 is 138 — hence ADJUSTED rather than VALID. (2) Mechanism confirmed real: every YAML load path in the repo uses plain yaml.safe_load, which silently drops duplicate mapping keys (last-wins) with no diagnostic; a grep for add_constructor/duplicate-key handling across src/ and tests/ found no duplicate-key-rejecting loader and no test exercising duplicated YAML keys (existing duplicate checks only cover duplicate ids within parsed lists, e.g. registry.py:118-119 'duplicate registry id', definitions.py:92-93, scenario/eval/example fixture dupes — none catch a duplicated key within one YAML mapping). (3) Doctrine claim confirmed: spec.py:11-12 module docstring 'All parsing is total: malformed input raises SpecError with a precise message rather than producing a half-built object'; docs/architecture.md:149 repeats it. A duplicated status: key slipping through contradicts that doctrine but silently resolves to a valid spec, so severity low is correct: real authoring-defect vector with limited blast radius (a duplicated key takes one of two valid values, likely caught downstream by validation gates like status checks in most cases). Proposed fix (shared duplicate-key-rejecting SafeConstructor helper used by all load sites) is sound; note the blast radius is larger than the finding states since artifacts/ load sites are also affected.
<!-- PR and issue links are added to the Tracking field after filing. -->
