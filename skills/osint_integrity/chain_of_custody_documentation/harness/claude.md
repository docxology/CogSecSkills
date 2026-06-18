# Claude Code adapter — Chain-of-Custody Documentation

Binds the neutral `skill.yaml` tool verbs to Claude Code tools. Follow `../workflow.md`; the logic is identical across harnesses.

| Neutral verb | Claude Code tool | Notes |
| --- | --- | --- |
| `read` | `Read` / `Grep` | Read supplied material and locate local evidence. |
| `exec` | `Bash` | Run commands or the project's own gates. |
| `write` | `Write` / final response | Emit the structured product. |
| `reason` | private model reasoning | Apply the technique; expose concise rationale. |

## Invocation

Run the workflow steps in order with the caller's context as the source of truth. If a required tool is unavailable, state the limitation and downgrade the tool-dependent claim to unverified rather than fabricating evidence.

## Output contract

Return the `skill.yaml` outputs (custody_log, integrity_summary) as Markdown, with a calibrated confidence statement. Keep the product defensive and accountable.
