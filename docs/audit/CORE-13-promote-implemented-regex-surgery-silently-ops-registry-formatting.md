# CORE-13: promote_to_implemented regex surgery silently no-ops when registry formatting drifts

|Field|Value|
|---|---|
|Audit ID|`CORE-13`|
|Lens|`CORE`|
|Severity|`low`|
|Red-team verdict|`VALID`|
|Status|Open (validated 2026-09-10)|
|Tracking|[GitHub issue](https://github.com/docxology/CogSecSkills/issues/18)|

## Summary
`promote_to_implemented` rewrites the registry status via a line-anchored regex that only matches single-line flow mappings with an unquoted id immediately after `{id:`. If an entry is ever reformatted to block style or the id gets quoted, `subn` matches zero times and the function returns without any error — `author-batch` reports success while the rendered-on-disk/registry-status pair silently drifts out of sync.

## Evidence
`src/cogsecskills/authoring/author.py:620-627` (finding cited 622-627; quote verbatim, line numbers off by 2):

```python
pattern = re.compile(r"(\{id:\s*" + re.escape(skill_id) + r",[^}]*?status:\s*)(stub|planned)")
new_text, n = pattern.subn(r"\1implemented", text)
if n:
```

There is no `else` branch; the function returns only the changed count and callers ignore it (`cli.py:_cmd_author_batch:422-427` discards the promote return value; `author_batch` ignores it too). The verifier confirmed the regex requires the literal `{id:` prefix and an unquoted id, so quoted ids or block-style entries match 0 times, and found no compensating gate: `quality/validate.py:259-263` only hard-errors on implemented rows missing from disk — the inverse failure is not flagged — and the coherence check at `validate.py:286-295` verifies only id enumeration and group match, not status. A test (`tests/authoring/test_cogsecskills_author.py:133-138`) even passes a nonexistent id and accepts unchanged behavior, pinning the silent no-op as accepted.

## Impact
If registry formatting ever drifts (pretty-printed YAML, quoted ids), promotion silently stops working: authors see a successful run while the registry status stays `stub`/`planned`, and no existing gate detects the mismatch. Mitigating context: the live registry is uniformly single-line flow mappings and the docstring says the line-anchored edit is intentional — a latent fragility rather than an active bug, hence low.

## Remediation
In `author.py` `promote_to_implemented` (lines 620-627), track ids that matched zero times and raise or warn instead of returning silently; callers (`_cmd_author_batch`, `author_batch`) should surface the mismatch. The more robust fix is to parse the YAML and rewrite statuses through a structured round-trip instead of line-anchored regex. Add a test where the registry entry uses a quoted id and assert the function reports failure rather than silently succeeding.

## Audit trail
- Discovered by the CORE lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `VALID`, confidence `high`.
- Verifier notes: Verified the code (actual lines 620-627; finding cited 622-627 — quote verbatim, line numbers off by 2). Re-derived the regex: requires the literal `{id:` flow-mapping prefix and an unquoted id immediately after; quoted ids (`id: "sat.x"`) or block-style entries match 0 times and the no-op is silent. Checked mitigation paths: (1) tests/authoring/test_cogsecskills_author.py:133-138 test_promote_to_implemented even passes a nonexistent id and accepts unchanged behavior, pinning the silent no-op as accepted; (2) src/cogsecskills/quality/validate.py:259-263 only hard-errors on implemented rows missing from disk — the inverse failure (rendered skill on disk while registry row stays stub/planned) is NOT flagged; the on-disk-vs-registry coherence check at validate.py:286-295 verifies only id enumeration and group match, not status; (3) cli.py _cmd_author_batch:422-427 prints rendered/failed counts and discards the promote return value; author_batch ignores it too. So the out-of-sync state escapes every existing gate. Mitigating context: docstring says the line-anchored edit is intentional ('Targeted per-line text edit so the registry's grouping and comments survive'), the live registry is uniformly single-line flow mappings, and field reordering after `id:` still matches ([^}]*? is order-agnostic post-id) — only quoting/block-style reformat breaks it. Low severity correct: hygiene-level latent fragility, limited blast radius.
<!-- PR and issue links are added to the Tracking field after filing. -->
