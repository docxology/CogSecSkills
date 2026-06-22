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

## Defensive boundary

Use Information Flow Network Analysis only for information-environment monitoring and platform-risk defense: recognize, assess, document, or defend platform integrity, narrative context, and authentic community behavior. Do not use this skill to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement.

## Misuse redirect

If a request asks Information Flow Network Analysis to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement, refuse that path and redirect to the safe defensive form: map supplied narratives, automation signals, or platform affordance risks for defensive review.

## Evidence discipline

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

## Failure modes and negative controls

- Information Flow Network Analysis: presenting the role map as a complete picture when the underlying propagation data was sampled or platform-limited, the temporal dimension was collapsed into a single static snapshot, or high centrality was read as culpability, so the structural conclusions overstate what the partial graph can support.
- Information Flow Network Analysis: producing advice that would help a requester amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement.
- Information Flow Network Analysis: reporting the network role map without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Information Flow Network Analysis outputs to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the network role map from Information Flow Network Analysis into an operational playbook to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Information Flow Network Analysis to map supplied narratives, automation signals, or platform affordance risks for defensive review with propagation data, narrative seed, and account metadata' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Betweenness centrality identifies the accounts most critical to cross-community information flow — targeting or countering them has disproportionate effect
- Velocity curves reveal injection events: sudden acceleration often marks amplification by a high-follower account or coordinated boost
- Cross-community bridges are the most dangerous propagation points — content that crosses ideological clusters becomes harder to contain
- Network topology changes over time; snapshot analyses miss dynamic rewiring that happens during active operations
