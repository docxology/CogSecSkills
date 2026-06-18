# Harness Adapter — Claude Code (Devil's Advocacy)

Maps the neutral tool verbs used in [../workflow.md](../workflow.md) onto Claude
Code's native tools.

| Neutral verb | Claude Code tool | Notes |
| --- | --- | --- |
| read | Read | Read the consensus statement, evidence files, and prior assessments. |
| search | Grep | Locate cited evidence, source references, and prior judgments across the workspace. |
| web | WebSearch | Optional — pull open-source reporting to test or contradict a cited assumption. |
| reason | (model) | Native reasoning; no tool call. Select vulnerable assumptions and build the counter-case. |
| write | Write | Emit the counter-case and robustness verdict as Markdown artifacts. |

## Invocation

Provide the `consensus_judgment` and `evidence_base` inputs inline or as file
paths. Read the inputs, then walk the six workflow steps in order, using Grep to
locate cited evidence and (optionally) WebSearch to test load-bearing
assumptions. Write the `counter_case` and `robustness_verdict` to Markdown files
in the working directory.

## Output contract

Two Markdown artifacts: `counter_case` (the strongest good-faith case against the
consensus, with its evidence and reasoning) and `robustness_verdict` (whether the
consensus survived, which assumptions held or cracked, and the resolving
collection). The verdict must report failure plainly if the consensus did not
survive — never omit an inconvenient result.
