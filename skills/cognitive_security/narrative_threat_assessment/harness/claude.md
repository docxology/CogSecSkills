# Harness Adapter — Claude Code

Maps the neutral tool verbs in [`../workflow.md`](../workflow.md) to Claude Code
tools for the Narrative Threat Assessment skill.

| Neutral verb | Claude Code tool | Notes |
| --- | --- | --- |
| read | Read | Read the narrative artifact and any provided context files precisely. |
| search | Grep / WebSearch | Grep local circulation samples; WebSearch for provenance and prior debunks. Do not amplify the narrative. |
| reason | (model reasoning) | Decompose claims, map levers, classify techniques, rate harm — no tool call. |
| write | Write | Write the defensive threat assessment and recommendations to a file. |

## Invocation

Invoke when the user asks to assess whether a narrative is a cognitive threat.
Supply `narrative_text` (required) and optional `context`. Run the workflow steps
in order; treat the narrative strictly as an object of study.

## Output contract

Produce a `threat_assessment` document (claims, audience and levers, manipulation
techniques, provenance/intent with calibrated uncertainty, reach, rated harm and
urgency) plus a prioritized `defensive_recommendations` list (prebunking, lateral
reading, counter-framing). Defensive and accountable only — never a manipulation
playbook, never uncritical amplification, never false-confidence attribution.
