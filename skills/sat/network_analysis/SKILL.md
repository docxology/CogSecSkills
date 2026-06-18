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

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- distinguish degree centrality (raw connectivity) from betweenness centrality (brokerage) — the highest-degree node is rarely the most structurally critical
- record evidence quality for every edge; low-confidence links must be flagged rather than treated as equivalent to confirmed relationships
- the most dangerous actor in an influence network is often a broker occupying a structural hole, not the loudest amplifier
- always ask what the network looks like AFTER removing the top-ranked node — resilience analysis is as important as centrality ranking
