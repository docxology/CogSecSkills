# Workflow — Information Flow Network Analysis

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Construct the propagation graph (read)
Build a directed graph from the propagation edge list. Nodes are accounts or outlets; directed edges represent content-sharing events weighted by timestamp. Annotate nodes with available metadata (follower count, platform, community affiliation).

## Step 2 — Compute network metrics and classify roles (reason)
Calculate in-degree (reception), out-degree (amplification), betweenness centrality (brokerage/gatekeeper position), clustering coefficient (community embeddedness), and PageRank (weighted influence). Classify each node into a structural role: seed (first mover), amplifier (high out-degree relative to peers), bridge (high betweenness, low clustering), gatekeeper (high betweenness, incoming from many sources), or sink (high in-degree, low out-degree). Plot the velocity timeline (cumulative spread vs. time) to identify acceleration events.

## Step 3 — Identify structural vulnerabilities and community dynamics (reason)
Apply community detection (e.g. Louvain modularity) to identify clusters. Map cross-community bridges — accounts that carry content between otherwise disconnected communities. Assess which edges or nodes, if absent, would have most slowed propagation. Identify whether the spread pattern is consistent with organic diffusion, coordinated boosting, or cross-platform injection.

## Step 4 — Produce the flow analysis report (write)
Write the network role map table and the narrative analysis report. Include: propagation timeline, key amplifier and bridge accounts, community-crossing events, structural vulnerability assessment, comparison with known organic vs. coordinated baseline patterns, and cognitive-security implications for monitoring, counter-messaging placement, or defensive response.

## Anti-criteria (must NOT happen)
- Do not conflate high centrality with culpability — amplifiers may be unaware they are spreading inauthentic content
- Do not present network maps as complete pictures when the underlying data is sampled or platform-limited
- Do not use structural role classifications alone to recommend content removal or account action — those decisions require additional policy and legal analysis
- Do not ignore the temporal dimension; a static snapshot misrepresents dynamic propagation events

## AGEINT upstream
`docs/ageint/information-environment.md`
