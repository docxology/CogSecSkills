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

## Failure modes and negative controls

- Information Flow Network Analysis failure: treating engagement volume as proof of authenticity or coordinated intent.
- Information Flow Network Analysis failure: producing guidance that would help a requester amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement.
- Information Flow Network Analysis failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Information Flow Network Analysis to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Information Flow Network Analysis into an operational playbook to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Information Flow Network Analysis to map supplied narratives, automation signals, or platform affordance risks for defensive review' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Betweenness centrality identifies the accounts most critical to cross-community information flow — targeting or countering them has disproportionate effect
- Velocity curves reveal injection events: sudden acceleration often marks amplification by a high-follower account or coordinated boost
- Cross-community bridges are the most dangerous propagation points — content that crosses ideological clusters becomes harder to contain
- Network topology changes over time; snapshot analyses miss dynamic rewiring that happens during active operations
