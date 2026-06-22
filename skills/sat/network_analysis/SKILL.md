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

## Failure modes and negative controls

- Network Analysis failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Network Analysis failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Network Analysis failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Network Analysis to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Network Analysis into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Network Analysis to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- distinguish degree centrality (raw connectivity) from betweenness centrality (brokerage) — the highest-degree node is rarely the most structurally critical
- record evidence quality for every edge; low-confidence links must be flagged rather than treated as equivalent to confirmed relationships
- the most dangerous actor in an influence network is often a broker occupying a structural hole, not the loudest amplifier
- always ask what the network looks like AFTER removing the top-ranked node — resilience analysis is as important as centrality ranking
