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

## Anti-criteria (must NOT happen)
- do not rank nodes by degree centrality alone — a high-degree hub that bridges no communities is far less strategically significant than a low-degree broker spanning a structural hole
- do not treat unconfirmed or inferred edges as equivalent to confirmed links in centrality calculations — run sensitivity checks showing how rankings change if weak-evidence edges are removed
- do not produce a network diagram as the sole output without a quantitative centrality analysis — visual impressions of 'big nodes' are systematically misleading

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
