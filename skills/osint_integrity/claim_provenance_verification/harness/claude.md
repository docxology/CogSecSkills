# Harness Adapter — Claude Code

Maps the neutral tool verbs used in [`../workflow.md`](../workflow.md) onto
Claude Code's native tools.

| Neutral verb | Claude Code tool | Notes |
| --- | --- | --- |
| read | Read | Read the supplied claim, cited articles, and attached files. |
| search | Grep, WebSearch | Grep local notes; WebSearch to find earlier and independent instances. |
| web | WebFetch, WebSearch | Fetch primary and corroborating sources; inspect content and dates. |
| reason | (model reasoning) | Scope match, circular-reporting detection, independence weighing. |
| write | Write | Emit the provenance chain, chain-of-custody note, and verdict. |

## Invocation

Invoke when the user asks to verify a claim, trace something to its source, or
asks "is this true?". Provide the claim text and any starting URLs. Run
[`../workflow.md`](../workflow.md) steps in order; use WebFetch on every hop
rather than reasoning about a source you have not opened.

## Output contract

Produce two artifacts: (1) the **provenance chain** — ordered sources from
point-of-encounter to origin, each with link and timestamp, plus a
chain-of-custody note; and (2) the **verdict** — one of verified / partially
verified / unverified / false / unverifiable, with a confidence level and the
single weakest link named explicitly.
