# Harness Adapter — Hermes

Maps the neutral tool verbs in [`../workflow.md`](../workflow.md) to Hermes tools
for the Narrative Threat Assessment skill.

| Neutral verb | Hermes tool | Notes |
| --- | --- | --- |
| read | fs.read | Read the narrative artifact and any provided context. |
| search | web.search | Search for provenance, prior debunks, and reach signals. Do not amplify the narrative. |
| reason | (model reasoning) | Decompose claims, map levers, classify techniques, rate harm — no tool call. |
| write | fs.write | Write the defensive threat assessment and recommendations. |

## Invocation

Invoke when the user asks whether a narrative is a cognitive threat or to
characterize an influence narrative defensively. Supply `narrative_text`
(required) and optional `context`. Run the workflow steps in order; the narrative
is only ever an object of study.

## Output contract

Return a `threat_assessment` document (claims, audience and levers, manipulation
techniques, provenance/intent with calibrated uncertainty, reach, rated harm and
urgency) plus a prioritized `defensive_recommendations` list (prebunking, lateral
reading, counter-framing). Defensive and accountable only — never a manipulation
playbook, never uncritical amplification, never false-confidence attribution.
