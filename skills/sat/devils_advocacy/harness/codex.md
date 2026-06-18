# Harness Adapter — Codex (Devil's Advocacy)

Maps the neutral tool verbs used in [../workflow.md](../workflow.md) onto the
Codex CLI's tool surface (`shell` and `apply_patch`).

| Neutral verb | Codex tool | Notes |
| --- | --- | --- |
| read | shell (`cat`, `rg`) | Read the consensus statement and evidence; `cat` files, `rg` to locate cited sources. |
| search | shell (`rg`, `grep`) | Search the workspace for cited evidence and prior judgments. |
| reason | (model) | Native reasoning; no shell call. Select vulnerable assumptions and build the counter-case. |
| write | apply_patch | Create or update the counter-case and robustness-verdict Markdown files. |

## Invocation

Pass `consensus_judgment` and `evidence_base` as inline text or file paths. Use
`shell` (`cat`, `rg`) to read the inputs and locate cited evidence, reason
through the six workflow steps, then use `apply_patch` to write the two Markdown
artifacts into the working tree. Do not shell out to a network tool unless the
task explicitly permits open-source collection.

## Output contract

Two Markdown files written via `apply_patch`: the `counter_case` (strongest
good-faith case against the consensus) and the `robustness_verdict` (survival
assessment plus resolving collection). If the consensus fails the challenge, the
verdict must say so explicitly — suppressing the result violates the skill's
anti-criteria.
