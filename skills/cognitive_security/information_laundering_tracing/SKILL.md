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

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Follow the claim, not the framing — different outlets restate the claim; identify the invariant core across reframings
- Classify each node by outlet credibility tier before assessing the laundering leap — a Tier-3 tabloid → Tier-2 partisan blog is a smaller leap than Tier-2 → Tier-1 mainstream
- Mark where caveats ('alleged', 'unverified', 'according to anonymous source') were present and when they were stripped — caveat removal is the signature of laundering
- Distinguish saturation laundering (dozens of low-credibility citations overwhelming search results) from blue-check laundering (a single high-credibility outlet canonizing the claim)
