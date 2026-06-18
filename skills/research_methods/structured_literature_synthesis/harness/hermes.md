# Harness Adapter — Hermes

Maps the neutral tool verbs in `workflow.md` to Hermes tools.

| Neutral verb | Hermes tool | Notes |
| --- | --- | --- |
| read | fs.read | Ingest each source document; extract claims. |
| search | web.search | Locate sources and themes where permitted. |
| web | web.fetch | Retrieve a specific permitted source by URL. |
| reason | (model) | Cluster, weigh conflicts, grade evidence inline. |
| write | fs.write | Emit the BLUF briefing and evidence table. |

## Invocation

Run inside Hermes. Provide the `synthesis_question`, the `sources` list, and
optional `inclusion_criteria`. Execute `workflow.md` in order: define scope,
gather and deduplicate via `web.search`/`web.fetch` (permitted retrieval only)
and `fs.read`, extract claims, cluster and grade by reasoning, then `fs.write`
the briefing.

## Output contract

Write a single markdown briefing plus the evidence table:

- BLUF bottom line first.
- Themes, each with a strength grade (strong / moderate / weak / insufficient).
- Conflicts surfaced honestly; gaps named with what would resolve them.
- Full citations; every synthesized statement traces to the evidence table.
