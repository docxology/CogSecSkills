---
name: cognitive_security.information_laundering_tracing
description: Track how a fringe claim is legitimized through layered republication into mainstream channels.
---

# Information Laundering Tracing

Information laundering tracing maps the staged process by which a fringe, unverified, or deceptive claim acquires apparent legitimacy through layered republication across progressively more credible outlets. The technique follows a claim from its origin through aggregator blogs, partisan news sites, think-tank summaries, and eventually mainstream coverage, identifying the amplification nodes that stripped caveats and added false authority at each step. It is closely related to the 'firehose of falsehood' and 'blue-check laundering' documented in disinformation research.

## When to use

- A fringe or unverified claim has appeared in mainstream or authoritative outlets and the legitimization pathway needs to be understood
- Analysts need to identify which intermediate nodes are the primary laundering conduits to prioritize counter-messaging
- Assessing whether a narrative's mainstream appearance was organic viral spread or a coordinated laundering operation
- Briefing stakeholders on how misinformation acquires false credibility before being debunked

## What it produces

- A directed chain of publication nodes from origin to mainstream with timestamps and outlet-tier classifications
- Annotation of each key laundering step: which caveats were dropped, what credibility was borrowed, and which actor or outlet drove amplification
- An assessment of whether the laundering appears opportunistic (organic spread) or deliberate (coordinated seeding)

## Defensive boundary

Use Information Laundering Tracing only for cognitive-security defense: recognize, assess, document, or defend audiences, decision-makers, and public discourse. Do not use this skill to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.

## Misuse redirect

If a request asks Information Laundering Tracing to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation, refuse that path and redirect to the safe defensive form: assess supplied material for manipulation indicators and recommend resilience measures.

## Evidence discipline

- For Information Laundering Tracing, tie each laundering chain, and analysis narrative claim to concrete evidence from the specific claim text, known publications, and time window item, source excerpt, observation, or command result that supports it.
- For Information Laundering Tracing, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the laundering chain.
- Before recommending any Information Laundering Tracing action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Information Laundering Tracing: the laundering chain is supported by multiple independent content, behavioral, narrative, media, and audience-risk evidence; canonicalize the claim and map the publication chain checks agree, and no unresolved contradiction would change the result.
- Medium for Information Laundering Tracing: the laundering chain is plausible, but one important claim text source, comparison case, or alternative explanation remains incomplete.
- Low for Information Laundering Tracing: the laundering chain rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Information Laundering Tracing cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating cognitive_security evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Information Laundering Tracing, use only authorized claim text, known publications, and time window, public or source-approved records, and caller-provided context needed for the defensive task.
- For Information Laundering Tracing, minimize person-level detail in the laundering chain; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Information Laundering Tracing, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Information Laundering Tracing: treating claim text as complete when canonicalize the claim and map the publication chain checks or contradictory evidence are missing.
- Information Laundering Tracing: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Information Laundering Tracing: reporting the laundering chain without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Information Laundering Tracing outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the laundering chain from Information Laundering Tracing into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Information Laundering Tracing to assess supplied material for manipulation indicators and recommend resilience measures with claim text, known publications, and time window' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Follow the claim, not the framing — different outlets restate the claim; identify the invariant core across reframings
- Classify each node by outlet credibility tier before assessing the laundering leap — a Tier-3 tabloid → Tier-2 partisan blog is a smaller leap than Tier-2 → Tier-1 mainstream
- Mark where caveats ('alleged', 'unverified', 'according to anonymous source') were present and when they were stripped — caveat removal is the signature of laundering
- Distinguish saturation laundering (dozens of low-credibility citations overwhelming search results) from blue-check laundering (a single high-credibility outlet canonizing the claim)
