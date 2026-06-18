# Harness Adapter — Hermes

Maps the neutral tool verbs used in [`../workflow.md`](../workflow.md) onto the
Hermes tool namespace.

| Neutral verb | Hermes tool | Notes |
| --- | --- | --- |
| read | fs.read | Read the claim, cited articles, and attached files. |
| search | web.search | Find earlier instances and independent reporting of the claim. |
| web | web.fetch, web.search | Fetch primary and corroborating sources for direct inspection. |
| reason | (model reasoning) | Scope match, circular-reporting detection, independence weighing. |
| write | fs.write | Write the provenance chain, chain-of-custody note, and verdict. |

## Invocation

Invoke when a user asks to verify a claim, trace it to its source, or determine
whether it is true. Supply the claim and any starting URLs. Run
[`../workflow.md`](../workflow.md) in order; call `web.fetch` on every hop so the
assessment binds to fetched content rather than recollection.

## Output contract

Return two artifacts: (1) the **provenance chain** — ordered sources from
point-of-encounter back to origin, each with link and timestamp, plus a
chain-of-custody note; and (2) the **verdict** — one of verified / partially
verified / unverified / false / unverifiable, with confidence and the single
weakest link named explicitly.
