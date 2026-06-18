# Hermes adapter — Morphological Analysis

Binds the neutral `skill.yaml` tool verbs to Hermes tools. Follow `../workflow.md`; the logic is identical across harnesses.

| Neutral verb | Hermes tool | Notes |
| --- | --- | --- |
| `read` | `fs.read` / context payload | Read supplied files or prompt payload. |
| `reason` | chain-of-thought | Reason through the steps in-turn. |
| `write` | `fs.write` / final message | Write the product or return it. |

## Invocation

Run the workflow steps in order with the caller's context as the source of truth. If a required tool is unavailable, state the limitation and downgrade the tool-dependent claim to unverified rather than fabricating evidence.

## Output contract

Return the `skill.yaml` outputs (morphological_box, scenario_inventory, priority_findings) as Markdown, with a calibrated confidence statement. Keep the product defensive and accountable.
