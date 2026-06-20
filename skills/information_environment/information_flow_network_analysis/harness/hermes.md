# Hermes adapter — Information Flow Network Analysis

Binds the neutral `skill.yaml` tool verbs to Hermes tools. Follow `../workflow.md`; the logic is identical across harnesses.

| Neutral verb | Hermes tool | Notes |
| --- | --- | --- |
| `read` | `fs.read` / context payload | Read supplied files or prompt payload. |
| `reason` | private model reasoning | Apply the technique in-turn; expose only concise rationale. |
| `write` | `fs.write` / final message | Write the product or return it. |

## Invocation

Run the workflow steps in order with the caller's context as the source of truth. Enforce the defensive boundary: Use Information Flow Network Analysis only for information-environment monitoring and platform-risk defense: recognize, assess, document, or defend platform integrity, narrative context, and authentic community behavior. Do not use this skill to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement. If a required tool is unavailable, state the limitation and downgrade the tool-dependent claim to unverified rather than fabricating evidence. If the caller asks for prohibited manipulation, deception, targeting, evasion, or operational influence guidance, apply this redirect: If a request asks Information Flow Network Analysis to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement, refuse that path and redirect to the safe defensive form: map supplied narratives, automation signals, or platform affordance risks for defensive review.

## Output contract

Return the `skill.yaml` outputs (network_role_map, flow_analysis_report) as Markdown, with a calibrated confidence statement, evidence labels, uncertainty notes, and any relevant privacy/legal constraints. Keep the product defensive and accountable.
