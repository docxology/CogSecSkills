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
- For Network Analysis, tie each centrality report, structural findings, and collection gaps claim to concrete evidence from the specific node list, edge list, and analytic question item, source excerpt, observation, or command result that supports it.
- For Network Analysis, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the centrality report.
- Before recommending any Network Analysis action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Network Analysis: the centrality report is supported by multiple independent hypotheses, assumptions, indicators, evidence tables, and confidence notes; build the edge list and compute centrality and identify structure checks agree, and no unresolved contradiction would change the result.
- Medium for Network Analysis: the centrality report is plausible, but one important node list source, comparison case, or alternative explanation remains incomplete.
- Low for Network Analysis: the centrality report rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Network Analysis cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Network Analysis, use only authorized node list, edge list, and analytic question, public or source-approved records, and caller-provided context needed for the defensive task.
- For Network Analysis, minimize person-level detail in the centrality report; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Network Analysis, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Network Analysis: treating node list as complete when build the edge list and compute centrality and identify structure checks or contradictory evidence are missing.
- Network Analysis: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Network Analysis: reporting the centrality report without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Network Analysis outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the centrality report from Network Analysis into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Network Analysis to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with node list, edge list, and analytic question' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not rank nodes by degree centrality alone — a high-degree hub that bridges no communities is far less strategically significant than a low-degree broker spanning a structural hole
- do not treat unconfirmed or inferred edges as equivalent to confirmed links in centrality calculations — run sensitivity checks showing how rankings change if weak-evidence edges are removed
- do not produce a network diagram as the sole output without a quantitative centrality analysis — visual impressions of 'big nodes' are systematically misleading

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
