# CORE-07: load_config bool()-coerces require_references, so quoted `"false"` silently becomes true

|Field|Value|
|---|---|
|Audit ID|`CORE-07`|
|Lens|`CORE`|
|Severity|`low`|
|Red-team verdict|`VALID`|
|Status|Open (validated 2026-09-10)|
|Tracking|PENDING-ISSUE-LINK|

## Summary
`load_config` coerces the quality flag with `bool(...)`, so a user writing `require_references: "false"` (quoted) in `cogsecskills.yaml` gets `True` — the exact inversion the codebase's own `SkillIO` check documents and forbids elsewhere for the sibling `required` field. The failure direction is fail-closed (the doctor gate becomes stricter than intended), which is why severity stays low, but the inversion is silent.

## Evidence
`src/cogsecskills/core/config.py:90`:

```python
require_references=bool(quality.get("require_references", False)),
```

The codebase's own doctrine at `src/cogsecskills/core/spec.py:111-114`:

```python
if not isinstance(required, bool):
    # The string "false" is truthy — coercing it would invert the channel's
    # required semantics. Demand a real boolean.
```

The verifier confirmed the mechanism: `yaml.safe_load` parses quoted `"false"` as the string `'false'`, `bool('false') == True`, and the gate at `quality/insights.py:179` (`if cfg.require_references and spec.status == "implemented" and not spec.references`) then fires against user intent. The sibling `_int` helper (`config.py:80-84`) explicitly rejects non-int values, making the asymmetry a plain oversight; tests cover only unquoted YAML booleans.

## Impact
A quoted boolean in `cogsecskills.yaml` silently flips the require-references gate on, so implemented skills without references start failing the doctor check for a reason the user believes they disabled. Docs show only bare `false`/`true` examples with no disclaimer, so nothing steers users away from the trap.

## Remediation
In `config.py` `load_config`, mirror the `SkillIO.from_obj` pattern: fetch the value, `if not isinstance(value, bool): raise ValueError(...)` naming the field, then assign. Add a test that `require_references: "false"` (quoted) raises rather than flipping the flag.

## Audit trail
- Discovered by the CORE lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `VALID`, confidence `high`.
- Verifier notes: Verified line 90 verbatim and current. Mechanism confirmed: yaml.safe_load parses quoted `"false"` as str 'false', bool('false') == True, so the gate at quality/insights.py:179 (`if cfg.require_references and spec.status == "implemented" and not spec.references`) would fire against user intent. No mitigating gate found: sibling `_int` (config.py:80-84) explicitly rejects non-int values while require_references skips that check — plain asymmetry; tests in tests/core/test_cogsecskills_config.py cover only unquoted YAML booleans; docs (configuration.md) show only bare false/true examples, no disclaimer. spec.py SkillIO.from_obj documents the exact same inversion hazard for the sibling `required` field. Severity re-derived: real defect, narrow blast radius — requires quoting the value, and the failure direction is fail-closed (stricter doctor gate), never silently weakens enforcement. Low is correct; proposed fix mirrors SkillIO's isinstance check.
<!-- PR and issue links are added to the Tracking field after filing. -->
