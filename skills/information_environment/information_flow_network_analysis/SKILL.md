---
name: information_environment.information_flow_network_analysis
description: Analyze how information propagates through a network to find amplifiers and bottlenecks.
---

# Information Flow Network Analysis

Information Flow Network Analysis maps how specific content, narratives, or claims propagate through social and media networks by modeling the information environment as a directed graph of accounts, publications, and linking relationships. It identifies amplifiers (super-spreaders), gatekeepers (bottlenecks that shape what passes), bridges (cross-community connectors), and sinks (endpoints where narratives lose velocity). The technique draws on network science, computational social science, and OSINT tradecraft to characterize the structural conditions that enable or constrain narrative spread.

## When to use

- Tracing the origin and spread path of a disinformation narrative to understand how it achieved scale
- Identifying key amplifier accounts whose removal or counter-messaging would most disrupt propagation
- Mapping cross-community bridges that move content between ideologically distinct clusters
- Assessing the structural resilience of an information ecosystem to narrative attack
- Prioritizing counter-narrative placement by identifying high-traffic chokepoints

## What it produces

- A structural map of who spread what, to whom, in what order
- Role classifications: seeds (first movers), amplifiers (high out-degree), bridges (cross-cluster), gatekeepers (high betweenness), and sinks
- Velocity timeline showing how propagation accelerated or decelerated
- Structural vulnerability assessment identifying which nodes or edges most enable rapid spread

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Betweenness centrality identifies the accounts most critical to cross-community information flow — targeting or countering them has disproportionate effect
- Velocity curves reveal injection events: sudden acceleration often marks amplification by a high-follower account or coordinated boost
- Cross-community bridges are the most dangerous propagation points — content that crosses ideological clusters becomes harder to contain
- Network topology changes over time; snapshot analyses miss dynamic rewiring that happens during active operations
