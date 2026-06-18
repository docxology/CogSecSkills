# Claude Code adapter — Image & Media Forensics Triage

Binds the neutral `skill.yaml` tool verbs to Claude Code tools. Follow `../workflow.md`; the logic is identical across harnesses.

| Neutral verb | Claude Code tool | Notes |
| --- | --- | --- |
| `read` | `Read` / `Grep` | Read supplied material and locate local evidence. |
| `web` | `WebFetch` / `WebSearch` | Fetch and inspect web sources. |
| `reason` | private model reasoning | Apply the technique; expose concise rationale. |
| `write` | `Write` / final response | Emit the structured product. |

## Invocation

Run the workflow steps in order with the caller's context as the source of truth. If a required tool is unavailable, state the limitation and downgrade the tool-dependent claim to unverified rather than fabricating evidence.

## Output contract

Return the `skill.yaml` outputs (triage_report) as Markdown, with a calibrated confidence statement. Keep the product defensive and accountable.
