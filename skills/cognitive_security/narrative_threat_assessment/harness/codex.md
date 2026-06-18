# Harness Adapter — Codex

Maps the neutral tool verbs in [`../workflow.md`](../workflow.md) to Codex tools
for the Narrative Threat Assessment skill.

| Neutral verb | Codex tool | Notes |
| --- | --- | --- |
| read | shell (cat/sed) | Read the narrative artifact and context via shell file reads. |
| search | shell (rg) / web | Use `rg` on local circulation samples; `web` for provenance and prior debunks. Do not amplify the narrative. |
| reason | (model reasoning) | Decompose claims, map levers, classify techniques, rate harm — no tool call. |
| write | apply_patch | Write the defensive threat assessment and recommendations to a file. |

## Invocation

Invoke when the user asks to characterize a narrative as a cognitive threat.
Supply `narrative_text` (required) and optional `context`. Execute the workflow
steps in order; handle the narrative only as an object of study.

## Output contract

Emit a `threat_assessment` document (claims, audience and levers, manipulation
techniques, provenance/intent with calibrated uncertainty, reach, rated harm and
urgency) and a prioritized `defensive_recommendations` list (prebunking, lateral
reading, counter-framing). Defensive and accountable only — never a manipulation
how-to, never uncritical amplification, never false-confidence attribution.
