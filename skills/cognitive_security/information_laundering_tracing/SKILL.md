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

- For Information Laundering Tracing, bind each finding to a labeled source — content, behavioral, narrative, media, and audience-risk evidence, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Information Laundering Tracing, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Information Laundering Tracing recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Information Laundering Tracing: independent lines of content, behavioral, narrative, media, and audience-risk evidence converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Information Laundering Tracing: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Information Laundering Tracing: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Information Laundering Tracing cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Information Laundering Tracing should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Information Laundering Tracing, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Information Laundering Tracing, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Information Laundering Tracing, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Information Laundering Tracing failure: mistaking persuasive resonance for verified harm or intent.
- Information Laundering Tracing failure: producing guidance that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Information Laundering Tracing failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Information Laundering Tracing to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Information Laundering Tracing into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Information Laundering Tracing to assess supplied material for manipulation indicators and recommend resilience measures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Follow the claim, not the framing — different outlets restate the claim; identify the invariant core across reframings
- Classify each node by outlet credibility tier before assessing the laundering leap — a Tier-3 tabloid → Tier-2 partisan blog is a smaller leap than Tier-2 → Tier-1 mainstream
- Mark where caveats ('alleged', 'unverified', 'according to anonymous source') were present and when they were stripped — caveat removal is the signature of laundering
- Distinguish saturation laundering (dozens of low-credibility citations overwhelming search results) from blue-check laundering (a single high-credibility outlet canonizing the claim)
