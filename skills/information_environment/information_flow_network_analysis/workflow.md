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

## Evidence requirements
- For Information Flow Network Analysis, anchor every role classification and structural-vulnerability claim to concrete evidence from the supplied propagation edge list and account metadata, citing the specific centrality metric, velocity event, or community-crossing observation that supports it, and flag where missing edges leave the inference underdetermined.
- For Information Flow Network Analysis, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the network role map.
- Before recommending any Information Flow Network Analysis action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Information Flow Network Analysis: the network role map assigns amplifier, bridge, gatekeeper, and sink labels from centrality metrics computed on adequately sampled propagation data, the structural roles and the identified chokepoints remain stable across temporal snapshots, and no unresolved contradiction would change the assessment of how the narrative achieved scale.
- Medium for Information Flow Network Analysis: the network role map is plausible, but one important propagation data source, comparison case, or alternative explanation remains incomplete.
- Low for Information Flow Network Analysis: the network role map rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Information Flow Network Analysis cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating information_environment evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Information Flow Network Analysis, use only authorized propagation data, narrative seed, and account metadata, public or source-approved records, and caller-provided context needed for the defensive task.
- For Information Flow Network Analysis, minimize person-level detail in the network role map; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Information Flow Network Analysis, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Information Flow Network Analysis: presenting the role map as a complete picture when the underlying propagation data was sampled or platform-limited, the temporal dimension was collapsed into a single static snapshot, or high centrality was read as culpability, so the structural conclusions overstate what the partial graph can support.
- Information Flow Network Analysis: producing advice that would help a requester amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement.
- Information Flow Network Analysis: reporting the network role map without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Information Flow Network Analysis outputs to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the network role map from Information Flow Network Analysis into an operational playbook to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Information Flow Network Analysis to map supplied narratives, automation signals, or platform affordance risks for defensive review with propagation data, narrative seed, and account metadata' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not conflate high centrality with culpability — amplifiers may be unaware they are spreading inauthentic content
- Do not present network maps as complete pictures when the underlying data is sampled or platform-limited
- Do not use structural role classifications alone to recommend content removal or account action — those decisions require additional policy and legal analysis
- Do not ignore the temporal dimension; a static snapshot misrepresents dynamic propagation events

## AGEINT upstream
`docs/ageint/information-environment.md`
