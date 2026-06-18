---
name: cognitive_security.trust_and_credibility_modeling
description: Model how trust is established, transferred, and exploited across an information system.
---

# Trust & Credibility Modeling

Trust and credibility modeling maps the signals, heuristics, and institutional structures through which actors in an information system assess source reliability — and identifies how those pathways are exploited in influence operations. Drawing on Metzger & Flanagin's credibility research, social-capital theory, and the computational trust literature, this technique produces a structured model of how trust is established (competence + benevolence + integrity signals), transferred across networks (trust transitivity), and weaponized (credential mimicry, parasocial trust, authority spoofing). The goal is defensive: to audit trust architecture for vulnerabilities before adversaries exploit them.

## When to use

- auditing an information environment for trust vulnerabilities before a high-stakes event (election, crisis, product launch)
- investigating how an influence operation gained traction by exploiting legitimate credibility pathways
- designing counter-influence measures and needing to understand what trust signals the target audience actually uses
- evaluating a new source or actor's credibility claims in a domain where credentials can be mimicked
- training analysts or communicators to recognize trust-exploitation tactics in the wild
- post-incident analysis of how a false narrative achieved credibility with a specific audience

## What it produces

- a layered trust model showing competence, benevolence, and integrity signals for key actors and how these combine into composite credibility judgments
- a trust-transfer map tracing how credibility flows from high-trust anchors (institutions, peer endorsers) to novel or unknown sources
- a heuristic inventory — the mental shortcuts the audience actually uses to assess credibility (verification badges, affiliation signals, writing style, social proof)
- an exploitation vulnerability audit mapping each trust pathway to known attack techniques (credential mimicry, parasocial relationship manufacture, institutional spoofing, authority cascade attacks)
- hardening recommendations prioritized by pathway criticality and attack feasibility

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- trust has three independently exploitable components: competence (can they know?), benevolence (do they care about me?), and integrity (do they tell the truth?) — model all three separately
- trust is transitive and asymmetric: endorsement from a high-trust anchor confers credibility to unknown actors, but not vice versa — map these directional flows explicitly
- heuristic-based credibility assessment (surface signals: verification marks, institutional logos, authoritative tone) is the norm, not the exception — this is where attackers invest
- parasocial trust — the one-sided sense of relationship with media figures, influencers, or AI personas — transfers credibility without requiring reciprocal verification
- distinguish trust-establishment (building from scratch) from trust-transfer (borrowing from a trusted anchor) from trust-exploitation (weaponizing existing trust) — each requires different defensive measures
- trust architecture has network effects: a single compromised high-trust node can cascade credibility across many downstream actors
