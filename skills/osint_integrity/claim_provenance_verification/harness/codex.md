# Harness Adapter — Codex

Maps the neutral tool verbs used in [`../workflow.md`](../workflow.md) onto
Codex's tool surface (shell-centric).

| Neutral verb | Codex tool | Notes |
| --- | --- | --- |
| read | shell (`cat`, `sed`) | Read the claim, cited articles, and attached files. |
| search | web, shell (`rg`) | Search the web for earlier/independent instances; grep local notes. |
| web | web / curl via shell | Fetch primary and corroborating sources for direct inspection. |
| reason | (model reasoning) | Scope match, circular-reporting detection, independence weighing. |
| write | apply_patch | Write the provenance chain, chain-of-custody note, and verdict. |

## Invocation

Trigger on requests to verify a claim, trace it to its source, or check whether
it is true. Pass the claim and any starting URLs. Execute
[`../workflow.md`](../workflow.md) in order; use `web` or `curl` via the shell to
open every source on the chain — never grade a source you have not fetched.

## Output contract

Emit two artifacts: (1) the **provenance chain** — ordered sources from
point-of-encounter to origin with links and timestamps plus a chain-of-custody
note; and (2) the **verdict** — verified / partially verified / unverified /
false / unverifiable, with confidence and the single weakest link named
explicitly.
