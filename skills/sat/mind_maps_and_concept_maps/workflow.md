# Workflow — Mind Maps & Concept Maps

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Extract concepts (read)
Read the source material and list all candidate nodes: actors, events, beliefs, mechanisms, and contextual factors. Record the raw language used to name each concept rather than paraphrasing, so provenance is traceable.

## Step 2 — Draft links and labels (reason)
For each pair of concepts that stands in a meaningful relationship, draw a directed edge and label it with a verb phrase (e.g., 'funds', 'amplifies', 'contradicts', 'is prerequisite for'). Arrange nodes so that causal or temporal flow reads left-to-right or top-to-bottom.

## Step 3 — Audit for gaps and conflicts (reason)
Walk every node: identify nodes with no inbound links (potential unexamined causes), nodes with no outbound links (potential unexamined effects), and cycles (potential feedback loops). Note any two links that together imply a contradiction.

## Step 4 — Emit graph and analytic narrative (write)
Output the map in a machine-readable format (Mermaid flowchart or adjacency list). Append a gap-and-conflict report that names each identified structural problem, states what additional evidence or reasoning would resolve it, and flags any section of the map that rests on an assumption rather than confirmed fact.

## Evidence requirements
- For Mind Maps & Concept Maps, tie each concept graph, and gap and conflict report claim to concrete evidence from the specific source material, central topic, and map type item, source excerpt, observation, or command result that supports it.
- For Mind Maps & Concept Maps, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the concept graph.
- Before recommending any Mind Maps & Concept Maps action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Mind Maps & Concept Maps: the concept graph is supported by multiple independent hypotheses, assumptions, indicators, evidence tables, and confidence notes; extract concepts and draft links and labels checks agree, and no unresolved contradiction would change the result.
- Medium for Mind Maps & Concept Maps: the concept graph is plausible, but one important source material source, comparison case, or alternative explanation remains incomplete.
- Low for Mind Maps & Concept Maps: the concept graph rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Mind Maps & Concept Maps cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Mind Maps & Concept Maps, use only authorized source material, central topic, and map type, public or source-approved records, and caller-provided context needed for the defensive task.
- For Mind Maps & Concept Maps, minimize person-level detail in the concept graph; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Mind Maps & Concept Maps, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Mind Maps & Concept Maps: treating source material as complete when extract concepts and draft links and labels checks or contradictory evidence are missing.
- Mind Maps & Concept Maps: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Mind Maps & Concept Maps: reporting the concept graph without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Mind Maps & Concept Maps outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the concept graph from Mind Maps & Concept Maps into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Mind Maps & Concept Maps to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with source material, central topic, and map type' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not leave link labels blank — unlabeled edges reduce the map to an uninterpretable blob
- do not collapse distinct concepts into a single node to keep the map tidy — hidden conflation is worse than a dense map
- do not treat the completed map as a finished product; it is a living artifact that must be updated as new information arrives

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
