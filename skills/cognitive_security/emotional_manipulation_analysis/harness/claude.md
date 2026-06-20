# Claude Code adapter — Emotional Manipulation Analysis

Binds the neutral `skill.yaml` tool verbs to Claude Code tools. Follow `../workflow.md`; the logic is identical across harnesses.

| Neutral verb | Claude Code tool | Notes |
| --- | --- | --- |
| `read` | `Read` / `Grep` | Read supplied material and locate local evidence. |
| `reason` | private model reasoning | Apply the technique; expose concise rationale. |
| `write` | `Write` / final response | Emit the structured product. |

## Invocation

Run the workflow steps in order with the caller's context as the source of truth. Enforce the defensive boundary: Use Emotional Manipulation Analysis only for cognitive-security defense: recognize, assess, document, or defend audiences, decision-makers, and public discourse. Do not use this skill to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation. If a required tool is unavailable, state the limitation and downgrade the tool-dependent claim to unverified rather than fabricating evidence. If the caller asks for prohibited manipulation, deception, targeting, evasion, or operational influence guidance, apply this redirect: If a request asks Emotional Manipulation Analysis to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation, refuse that path and redirect to the safe defensive form: assess supplied material for manipulation indicators and recommend resilience measures.

## Output contract

Return the `skill.yaml` outputs (emotional_lever_map, defensive_brief) as Markdown, with a calibrated confidence statement, evidence labels, uncertainty notes, and any relevant privacy/legal constraints. Keep the product defensive and accountable.
