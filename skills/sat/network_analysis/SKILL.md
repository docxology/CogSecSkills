---
name: sat.network_analysis
description: Map actors and links; compute centrality and brokerage to find key nodes.
---

# Network Analysis

Network analysis in the structured-analytic tradition maps actors, organizations, or information nodes as vertices and their relationships (communication, funding, co-authorship, amplification) as edges, then applies graph-theoretic measures — degree, betweenness, eigenvector centrality, clustering coefficient, structural holes — to identify key actors, brokers, and vulnerabilities that are invisible in prose analysis. In cognitive-security contexts it is the primary tool for characterizing coordinated inauthentic behavior networks, influence operation infrastructure, and information-ecosystem topology.

## When to use

- an influence operation or coordinated campaign is suspected and the relational structure of participating accounts or organizations needs to be characterized
- a threat actor network needs to be prioritized for disruption and the analysis needs to identify which nodes are structurally critical vs merely visible
- an information ecosystem audit needs to map which sources act as amplification hubs, brokers between communities, or bridges between fringe and mainstream audiences
- attribution analysis requires identifying shared infrastructure, common controllers, or coordination fingerprints across ostensibly independent actors

## What it produces

- a ranked centrality table identifying degree hubs, betweenness brokers, and eigenvector-central influencers in the network
- identification of structural holes (positions of brokerage between otherwise disconnected clusters) and the actors occupying them
- a community/cluster partition of the network with characterization of each cluster's apparent function or identity
- a collection gap map showing where missing links or nodes create analytic blind spots

## Defensive boundary

Use Network Analysis only for structured analytic technique support: recognize, assess, document, or defend analytic rigor, alternative hypotheses, and calibrated judgment. Do not use this skill to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.

## Misuse redirect

If a request asks Network Analysis to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation, refuse that path and redirect to the safe defensive form: apply the structured technique to supplied evidence while preserving alternatives and uncertainty.

## Evidence discipline

- For Network Analysis, bind every centrality ranking, broker claim, and cluster boundary to concrete evidence — a documented edge, its relationship type, and its recorded evidence quality drawn from the node and edge lists — and flag any node or link that rests only on low-confidence or single-source reporting as provisional rather than established.
- For Network Analysis, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the centrality report.
- Before recommending any Network Analysis action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Network Analysis: the betweenness-ranked centrality table, broker identification, and cluster partition are each corroborated by multiple independent edges whose evidence quality is documented, the rankings stay stable under removal of any weak-evidence link, the resilience and coordination-signature findings agree, and no unresolved contradiction would change the conclusion.
- Medium for Network Analysis: the centrality report is plausible, but one important node list source, comparison case, or alternative explanation remains incomplete.
- Low for Network Analysis: the centrality report rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Network Analysis cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Network Analysis, use only authorized node list, edge list, and analytic question, public or source-approved records, and caller-provided context needed for the defensive task.
- For Network Analysis, minimize person-level detail in the centrality report; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Network Analysis, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Network Analysis: declaring the network characterized when inferred or single-source edges were treated as confirmed links, so a high-degree hub is mistaken for the structurally critical actor and no sensitivity check or resilience simulation was run, leaving the centrality ranking an artifact of unexamined collection gaps rather than the actual topology.
- Network Analysis: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Network Analysis: reporting the centrality report without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Network Analysis outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the centrality report from Network Analysis into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Network Analysis to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with node list, edge list, and analytic question' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- distinguish degree centrality (raw connectivity) from betweenness centrality (brokerage) — the highest-degree node is rarely the most structurally critical
- record evidence quality for every edge; low-confidence links must be flagged rather than treated as equivalent to confirmed relationships
- the most dangerous actor in an influence network is often a broker occupying a structural hole, not the loudest amplifier
- always ask what the network looks like AFTER removing the top-ranked node — resilience analysis is as important as centrality ranking
