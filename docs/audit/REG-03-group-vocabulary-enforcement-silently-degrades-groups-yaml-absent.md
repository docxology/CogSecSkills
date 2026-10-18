# REG-03: Group-vocabulary enforcement silently degrades when groups.yaml is absent

|Field|Value|
|---|---|
|Audit ID|`REG-03`|
|Lens|`REG`|
|Severity|`low`|
|Red-team verdict|`VALID`|
|Status|Open (validated 2026-09-10)|
| Tracking | [GitHub issue](https://github.com/docxology/CogSecSkills/issues/37) |

## Summary
`load_registry` tolerates a missing `registry/groups.yaml`, and `validate.py` only checks entry groups against the vocabulary when the loaded set is non-empty. Deleting or renaming `groups.yaml` therefore silently disables the registry↔groups coherence check (and the documented `# id format: <group>.<slug>` header contract in skills.yaml becomes unenforced) while validation still passes, instead of failing loudly. Red team confirmed low severity: one coherence gate degrades on an abnormal deletion scenario with limited blast radius, and the id-prefix shape check still partially constrains.

## Evidence
`src/cogsecskills/core/registry.py:124` (no else branch; line 123 is `groups_file = groups_path(root)`, and an empty `groups` dict is returned silently on a missing file):

```python
if groups_file.is_file():
```

`src/cogsecskills/quality/validate.py:267` guarding the vocabulary check at 269-273 (comment at 266: `# Every catalogued group must be defined in groups.yaml (when defined).`):

```python
if defined_groups:
    for entry in registry.entries:
        if entry.group not in defined_groups:
            result.error(...)
```

## Impact
A contributor who deletes or renames `groups.yaml` gets a fully green validation run while the registry↔groups vocabulary cross-check is gone — a contract documented in `skills.yaml:10`, `AGENTS.md`/`ISA.md` (ISC-2), and `skill-contract.md:197` is silently unenforced. Registry entries can then reference groups outside the intended vocabulary with no error. The `<group>.<slug>` id-shape check (~validate.py:256-262) still runs on `entry.group` itself, so ids keep their shape; only cross-checking against the vocabulary is lost. No test covers a missing `groups.yaml` (no matches for `unlink`/`groups_file` in tests).

## Remediation
In `src/cogsecskills/core/registry.py`, make `load_registry` raise `FileNotFoundError` when `registry/skills.yaml` exists but `registry/groups.yaml` does not (mirroring the hard failure on missing skills.yaml at registry.py:109-110) — or alternatively have `validate.py` emit an error when the vocabulary file is missing. Also correct the `load_registry` docstring at registry.py:107 ("Load and validate ... skills.yaml + groups.yaml"), which currently overstates the actual conditional behavior. Add a test that deletes `groups.yaml` and asserts validation fails loudly rather than passing.

## Audit trail
- Discovered by the REG lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `VALID`, confidence `high`.
- Verifier notes: Checked: (1) quotes and line numbers confirmed exactly (finding cited 128-131, actual is 124-127 — minor line drift, evidence corrected); (2) re-derived reasoning: load_registry hard-fails on missing skills.yaml (registry.py:109-110) but only conditionally reads groups.yaml, returning empty groups dict; validate_library skips the group-vocabulary check when defined_groups is empty, so deleting/renaming groups.yaml silently disables the registry↔groups coherence check while validate still passes. The <group>.<slug> id-shape check (validate.py ~256-262) still runs on entry.group itself, so ids keep their shape — only cross-checking against the vocabulary is lost. (3) Mitigation search: no test covers a missing groups.yaml (grep for unlink/groups_file in tests: no matches); skills.yaml:10 header comment and AGENTS.md/ISA.md ISC-2 document the requirement but nothing enforces groups.yaml's existence; skill-contract.md:197 documents the conditional ('When groups.yaml defines any groups') — the behavior is intentional per the code comment, but the docstring at registry.py:107 ('Load and validate ... skills.yaml + groups.yaml') overstates. Nothing refutes the mechanism. Severity low is fair: silent degradation of one coherence gate on an abnormal deletion scenario, limited blast radius, and the id-prefix check still partially constrains. Fix suggestion is sound.
<!-- PR and issue links are added to the Tracking field after filing. -->