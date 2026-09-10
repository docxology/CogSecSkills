# CORE-02: Documented usage `scaffold <skill-id> [--root PATH]` cannot work: --root is registered only on the top-level parser

|Field|Value|
|---|---|
|Audit ID|`CORE-02`|
|Lens|`CORE`|
|Severity|`low`|
|Red-team verdict|`ADJUSTED`|
|Status|Open (validated 2026-09-10)|
|Tracking|PENDING-ISSUE-LINK|

## Summary
The CLI module docstring advertises `cogsecskills scaffold <skill-id> [--root PATH]`, but `--root` is registered only on the top-level parser, and argparse only recognizes parent-parser options before the subcommand token — so the documented suffix placement exits 2 with `unrecognized arguments: --root /path`. The red team adjusted severity from medium to low because `docs/cli.md` explicitly documents the prefix-placement constraint and all tests exercise the working form; the defect is a misleading docstring usage block rather than broken runtime behavior.

## Evidence
`src/cogsecskills/cli.py:22` (module docstring usage):

```text
python -m cogsecskills scaffold <skill-id> [--root PATH]
```

`src/cogsecskills/cli.py:455-456`:

```python
parser.add_argument("--root", type=Path, default=None, help="project root override")
sub = parser.add_subparsers(dest="command", required=True)
```

No subparser defines `--root` (verified across all `add_parser` calls at lines 458-673; the scaffold subparser at lines 491-497 adds only `skill_id` and `--overwrite`). The verifier re-derived the argparse behavior independently and confirmed tests consistently use prefix placement (e.g. `tests/test_cogsecskills_cli_scaffold.py:167`: `main(["--root", str(tmp_path), "scaffold", "sat.demo"])`), while `docs/cli.md:33-38` explicitly states: "`--root` is parsed on the top-level parser, so it must appear **before** the subcommand".

## Impact
Users following the module docstring's usage line get an `unrecognized arguments` exit-2 error with no hint that the flag belongs before the subcommand. The same applies to other global flags (e.g. `--format`) on subcommands. No gate or test enforces docstring accuracy, so the misleading usage block persists; blast radius is limited because the canonical CLI doc is accurate and a working invocation exists.

## Remediation
Either (a) create a shared parent parser holding `--root` (and other global flags) and pass `parents=[common]` to every `sub.add_parser(...)` in `cli.py`, or (b) update the docstring usage lines at `cli.py:22` to place `--root` before the subcommand, matching `docs/cli.md`. Option (a) also fixes the suffix form for all global flags at once.

## Audit trail
- Discovered by the CORE lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `ADJUSTED`, confidence `high`.
- Verifier notes: Verified: (1) exact quotes and line numbers match current file; (2) re-derived argparse behavior myself — correct; (3) checked whether handled elsewhere: tests consistently use prefix placement (e.g. tests/test_cogsecskills_cli_scaffold.py:167 `main(["--root", str(tmp_path), "scaffold", "sat.demo"])`), and docs/cli.md:33-38 EXPLICITLY documents the constraint: "`--root` is parsed on the top-level parser, so it must appear **before** the subcommand: cogsecskills --root /path/to/library list". This doc disclaimer materially mitigates the finding — the canonical CLI doc is correct, and only the module docstring usage block (cli.py:22) implies suffix placement works. No gate/test enforces docstring accuracy. ADJUSTED from medium to low: real doc inconsistency (docstring usage lines are misleading for --root, and equally for other global flags like --format on subcommands), limited blast radius — no wrong/misleading runtime results, documented behavior in docs/cli.md is accurate, functional invocation exists and is what all tests exercise. Fix suggestion (shared parent parser) is sound but equally valid is updating the docstring usage lines to place --root before the subcommand.
<!-- PR and issue links are added to the Tracking field after filing. -->
