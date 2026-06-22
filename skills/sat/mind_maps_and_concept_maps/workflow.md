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
- For Mind Maps & Concept Maps, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Mind Maps & Concept Maps, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Mind Maps & Concept Maps recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Mind Maps & Concept Maps: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Mind Maps & Concept Maps: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Mind Maps & Concept Maps: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Mind Maps & Concept Maps cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Mind Maps & Concept Maps should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Mind Maps & Concept Maps, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Mind Maps & Concept Maps, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Mind Maps & Concept Maps, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Mind Maps & Concept Maps failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Mind Maps & Concept Maps failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Mind Maps & Concept Maps failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Mind Maps & Concept Maps to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Mind Maps & Concept Maps into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Mind Maps & Concept Maps to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not leave link labels blank — unlabeled edges reduce the map to an uninterpretable blob
- do not collapse distinct concepts into a single node to keep the map tidy — hidden conflation is worse than a dense map
- do not treat the completed map as a finished product; it is a living artifact that must be updated as new information arrives

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
