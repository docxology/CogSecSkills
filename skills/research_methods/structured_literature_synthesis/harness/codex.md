# Harness Adapter — Codex

Maps the neutral tool verbs in `workflow.md` to Codex tools.

| Neutral verb | Codex tool | Notes |
| --- | --- | --- |
| read | shell (cat/rg) | Read source files from the workspace. |
| search | shell (rg) | Search the corpus for claims, terms, themes. |
| web | web | Retrieve sources where retrieval is permitted. |
| reason | (model) | Cluster, weigh conflicts, grade evidence inline. |
| write | apply_patch | Write the BLUF briefing and evidence table to disk. |

## Invocation

Run inside Codex. Supply the `synthesis_question`, the `sources` list, and
optional `inclusion_criteria`. Walk `workflow.md` in order: define scope, gather
and deduplicate (using `web` only for permitted retrieval), extract claims by
reading sources via shell, cluster and grade by reasoning, then write the output
with `apply_patch`.

## Output contract

Produce a single markdown briefing plus the evidence table:

- BLUF bottom line first.
- Themes, each with a strength grade (strong / moderate / weak / insufficient).
- Conflicts surfaced honestly; gaps named with what would resolve them.
- Full citations; every synthesized statement traces to the evidence table.
