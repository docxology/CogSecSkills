# REG-02: RegistryEntry.from_obj coerces required keys with str(), contradicting the spec layer's explicit anti-coercion policy

|Field|Value|
|---|---|
|Audit ID|`REG-02`|
|Lens|`REG`|
|Severity|`low`|
|Red-team verdict|`VALID`|
|Status|Open (validated 2026-09-10)|
| Tracking | PENDING-ISSUE-LINK |

## Summary
`RegistryEntry.from_obj` stringifies every required key with `str()`, exactly the coercion pattern the spec layer deliberately refuses and documents as a hazard. The result is an internal inconsistency: `id: 0` in the registry silently becomes the string `"0"` and passes validation, while the same shape in `skill.yaml` raises a `SpecError`. Red team confirmed the verdict at low severity because registry/skills.yaml is repo-controlled source data — the defect fails silently rather than producing wrong shipped output.

## Evidence
`src/cogsecskills/core/registry.py:55-58`:

```python
for key in ("id", "name", "group", "summary"):
    if not str(obj.get(key, "")).strip():
```

plus `status = str(obj.get("status", "planned")).strip().lower()` and `str()` coercion of every field in the `cls(...)` return.

`src/cogsecskills/core/spec.py:113-118` (the `_require_text` docstring the registry contradicts):

```
Coercion (``str(...)``) would silently accept ``id: 0`` / ``id: []`` / ``id: null`` as the strings ``"0"`` / ``"[]"`` / ``"None"``. Require the real type.
```

## Impact
Malformed registry rows fail silently instead of loudly: non-string values for `id`/`name`/`group`/`summary` are accepted after coercion, so the registry-side contract diverges from the definition-side contract enforced by `spec.py`. A wrong entry (e.g. a numeric id) ships as a plausible-looking string with no error, and the two validation layers give inconsistent answers for the same malformed shape. No test or gate enforces type strictness for registry rows (validation only checks mapping/required-key presence/status membership), so nothing catches the drift.

## Remediation
Apply the same `isinstance(value, str)` check used in `spec.py._require_text` to the registry's required keys in `src/cogsecskills/core/registry.py` (`from_obj`): reject non-string values for `id`, `name`, `group`, `summary` (and `status`) with a precise `SpecError`, and align the `cls(...)` construction so fields are no longer blanket-`str()`-coerced. Add a contract-test row asserting that `id: 0` in a registry entry fails loudly rather than becoming `"0"`.

## Audit trail
- Discovered by the REG lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `VALID`, confidence `high`.
- Verifier notes: Verified: registry.py from_obj does exactly the str() coercion spec.py's _require_text docstring warns against, so `id: 0` in the registry becomes '0' and passes while the same shape in skill.yaml raises. No test or gate enforces type strictness for registry rows (validation only checks mapping/required-key presence/status membership). Severity low is correct: registry/skills.yaml is repo-controlled source data; the divergence is an internal consistency defect failing silently rather than producing wrong shipped output.
<!-- PR and issue links are added to the Tracking field after filing. -->