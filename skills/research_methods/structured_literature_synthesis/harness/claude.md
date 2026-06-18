# Harness Adapter — Claude Code

Maps the neutral tool verbs in `workflow.md` to Claude Code tools.

| Neutral verb | Claude Code tool | Notes |
| --- | --- | --- |
| read | Read | Ingest each source document; extract claims. |
| search | Grep | Search the corpus for claims, terms, themes. |
| web | WebSearch | Locate sources where retrieval is permitted. |
| web | WebFetch | Retrieve a specific permitted source by URL. |
| reason | (model) | Cluster, weigh conflicts, grade evidence inline. |
| write | Write | Emit the BLUF briefing and evidence table. |

## Invocation

Run inside Claude Code. Provide the `synthesis_question`, the `sources` list,
and optional `inclusion_criteria`. Execute `workflow.md` steps in order: define
scope, gather/deduplicate via WebSearch/WebFetch and Read, extract with Read,
cluster and grade by reasoning, then Write the briefing. Only fetch sources the
user is permitted to retrieve.

## Output contract

Write a single markdown briefing plus the evidence table:

- BLUF bottom line first.
- Themes, each with a strength grade (strong / moderate / weak / insufficient).
- Conflicts surfaced honestly; gaps named with what would resolve them.
- Full citations; every synthesized statement traces to the evidence table.
