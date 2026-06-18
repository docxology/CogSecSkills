# Harness Adapter — Hermes (Devil's Advocacy)

Maps the neutral tool verbs used in [../workflow.md](../workflow.md) onto the
Hermes JSON tool-call protocol.

| Neutral verb | Hermes tool | Notes |
| --- | --- | --- |
| read | `fs.read` | `{"tool": "fs.read", "args": {"path": "<file>"}}` — read consensus statement and evidence. |
| search | `fs.read` | Read candidate evidence files; Hermes has no dedicated grep — enumerate then read. |
| web | `web.search` | `{"tool": "web.search", "args": {"query": "<assumption to test>"}}` — optional open-source check. |
| reason | (model) | Native reasoning; no JSON call. Select vulnerable assumptions and build the counter-case. |
| write | `fs.write` | `{"tool": "fs.write", "args": {"path": "<file>", "content": "<markdown>"}}` — emit artifacts. |

## Invocation

Supply `consensus_judgment` and `evidence_base` in the task payload. Issue
`fs.read` JSON calls to ingest the inputs and cited evidence, optionally
`web.search` to test a load-bearing assumption, reason through the six workflow
steps, then issue `fs.write` JSON calls to persist the two Markdown artifacts.

## Output contract

Two `fs.write` calls producing the `counter_case` (strongest good-faith case
against the consensus, with evidence and reasoning) and the `robustness_verdict`
(survival assessment plus the resolving collection). The verdict must honestly
report a failed consensus when that is the outcome — never withhold it.
