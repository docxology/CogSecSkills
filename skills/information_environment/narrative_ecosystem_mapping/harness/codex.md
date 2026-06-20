# Codex adapter — Narrative Ecosystem Mapping

Binds the neutral `skill.yaml` tool verbs to Codex tools. Follow `../workflow.md`; the logic is identical across harnesses.

| Neutral verb | Codex tool | Notes |
| --- | --- | --- |
| `read` | `shell` (`cat`, `rg`) | Read supplied files or stdin. |
| `search` | `shell` + optional web | Search the workspace or the web if available. |
| `reason` | private model reasoning | Apply the technique with concise rationale. |
| `write` | `apply_patch` / stdout | Persist the product or return Markdown. |

## Invocation

Run the workflow steps in order with the caller's context as the source of truth. Enforce the defensive boundary: Use Narrative Ecosystem Mapping only for information-environment monitoring and platform-risk defense: recognize, assess, document, or defend platform integrity, narrative context, and authentic community behavior. Do not use this skill to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement. If a required tool is unavailable, state the limitation and downgrade the tool-dependent claim to unverified rather than fabricating evidence. If the caller asks for prohibited manipulation, deception, targeting, evasion, or operational influence guidance, apply this redirect: If a request asks Narrative Ecosystem Mapping to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement, refuse that path and redirect to the safe defensive form: map supplied narratives, automation signals, or platform affordance risks for defensive review.

## Output contract

Return the `skill.yaml` outputs (narrative_inventory, ecosystem_map) as Markdown, with a calibrated confidence statement, evidence labels, uncertainty notes, and any relevant privacy/legal constraints. Keep the product defensive and accountable.
