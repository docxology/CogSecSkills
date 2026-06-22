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
- For Information Flow Network Analysis, bind each finding to a labeled source — platform observations, narrative movement, automation signals, and provenance data, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Information Flow Network Analysis, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Information Flow Network Analysis recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Information Flow Network Analysis: independent lines of platform observations, narrative movement, automation signals, and provenance data converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Information Flow Network Analysis: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Information Flow Network Analysis: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Information Flow Network Analysis cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Information Flow Network Analysis should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Information Flow Network Analysis, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Information Flow Network Analysis, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Information Flow Network Analysis, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Information Flow Network Analysis failure: treating engagement volume as proof of authenticity or coordinated intent.
- Information Flow Network Analysis failure: producing guidance that would help a requester amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement.
- Information Flow Network Analysis failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Information Flow Network Analysis to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Information Flow Network Analysis into an operational playbook to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Information Flow Network Analysis to map supplied narratives, automation signals, or platform affordance risks for defensive review' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not conflate high centrality with culpability — amplifiers may be unaware they are spreading inauthentic content
- Do not present network maps as complete pictures when the underlying data is sampled or platform-limited
- Do not use structural role classifications alone to recommend content removal or account action — those decisions require additional policy and legal analysis
- Do not ignore the temporal dimension; a static snapshot misrepresents dynamic propagation events

## AGEINT upstream
`docs/ageint/information-environment.md`
