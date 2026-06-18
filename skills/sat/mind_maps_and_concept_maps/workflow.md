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

## Anti-criteria (must NOT happen)
- do not leave link labels blank — unlabeled edges reduce the map to an uninterpretable blob
- do not collapse distinct concepts into a single node to keep the map tidy — hidden conflation is worse than a dense map
- do not treat the completed map as a finished product; it is a living artifact that must be updated as new information arrives

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
