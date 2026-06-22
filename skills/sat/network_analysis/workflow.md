# Workflow — Network Analysis

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Build the edge list (read)
Read all source material and extract every identified relationship as a directed or undirected edge: (source, target, relationship_type, evidence_quality). Annotate each node with its type (person / org / account) and any known attributes (affiliation, platform, known role). Flag nodes and edges whose existence depends on low-confidence or single-source reporting.

## Step 2 — Compute centrality and identify structure (reason)
From the edge list, compute: (a) degree centrality (in-degree and out-degree for directed graphs), (b) betweenness centrality to identify brokers, (c) eigenvector/PageRank centrality to identify nodes influential via their connections. Identify connected components, community structure (clusters), and structural holes. Note any coordination signatures: synchrony, shared infrastructure, or implausibly uniform behavior.

## Step 3 — Resilience and gap analysis (reason)
Simulate targeted removal of the top-3 nodes by betweenness centrality and assess whether the network fragments or routes around each removal. Identify the edges or nodes absent from current data whose presence would most change the centrality rankings — these are collection priorities. Flag any portions of the network that are inferred rather than observed.

## Step 4 — Report centrality findings and analytic narrative (write)
Produce the centrality table ranked by betweenness centrality as the primary sort key. Write the structural findings narrative covering brokers, clusters, coordination signatures, and resilience. Append a collection gaps section listing each missing node or edge, its estimated importance, and a recommended collection action.

## Evidence requirements
- For Network Analysis, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Network Analysis, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Network Analysis recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Network Analysis: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Network Analysis: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Network Analysis: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Network Analysis cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Network Analysis should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Network Analysis, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Network Analysis, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Network Analysis, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Network Analysis failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Network Analysis failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Network Analysis failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Network Analysis to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Network Analysis into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Network Analysis to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not rank nodes by degree centrality alone — a high-degree hub that bridges no communities is far less strategically significant than a low-degree broker spanning a structural hole
- do not treat unconfirmed or inferred edges as equivalent to confirmed links in centrality calculations — run sensitivity checks showing how rankings change if weak-evidence edges are removed
- do not produce a network diagram as the sole output without a quantitative centrality analysis — visual impressions of 'big nodes' are systematically misleading

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
