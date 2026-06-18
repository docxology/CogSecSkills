# Hermes adapter — Chain-of-Custody Documentation

Binds the neutral `skill.yaml` tool verbs to Hermes tools. Follow `../workflow.md`; the logic is identical across harnesses.

| Neutral verb | Hermes tool | Notes |
| --- | --- | --- |
| `read` | `fs.read` / context payload | Read supplied files or prompt payload. |
| `exec` | `shell` / exec fn | Invoke an execution tool when bound. |
| `write` | `fs.write` / final message | Write the product or return it. |
| `reason` | chain-of-thought | Reason through the steps in-turn. |

## Invocation

Run the workflow steps in order with the caller's context as the source of truth. If a required tool is unavailable, state the limitation and downgrade the tool-dependent claim to unverified rather than fabricating evidence.

## Output contract

Return the `skill.yaml` outputs (custody_log, integrity_summary) as Markdown, with a calibrated confidence statement. Keep the product defensive and accountable.
