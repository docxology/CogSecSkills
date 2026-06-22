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

## Defensive boundary

Use Trust & Credibility Modeling only for cognitive-security defense: recognize, assess, document, or defend audiences, decision-makers, and public discourse. Do not use this skill to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.

## Misuse redirect

If a request asks Trust & Credibility Modeling to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation, refuse that path and redirect to the safe defensive form: assess supplied material for manipulation indicators and recommend resilience measures.

## Evidence discipline

- For Trust & Credibility Modeling, bind each finding to a labeled source — content, behavioral, narrative, media, and audience-risk evidence, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Trust & Credibility Modeling, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Trust & Credibility Modeling recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Trust & Credibility Modeling: independent lines of content, behavioral, narrative, media, and audience-risk evidence converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Trust & Credibility Modeling: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Trust & Credibility Modeling: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Trust & Credibility Modeling cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Trust & Credibility Modeling should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Trust & Credibility Modeling, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Trust & Credibility Modeling, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Trust & Credibility Modeling, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Trust & Credibility Modeling failure: mistaking persuasive resonance for verified harm or intent.
- Trust & Credibility Modeling failure: producing guidance that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Trust & Credibility Modeling failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Trust & Credibility Modeling to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Trust & Credibility Modeling into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Trust & Credibility Modeling to assess supplied material for manipulation indicators and recommend resilience measures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- trust has three independently exploitable components: competence (can they know?), benevolence (do they care about me?), and integrity (do they tell the truth?) — model all three separately
- trust is transitive and asymmetric: endorsement from a high-trust anchor confers credibility to unknown actors, but not vice versa — map these directional flows explicitly
- heuristic-based credibility assessment (surface signals: verification marks, institutional logos, authoritative tone) is the norm, not the exception — this is where attackers invest
- parasocial trust — the one-sided sense of relationship with media figures, influencers, or AI personas — transfers credibility without requiring reciprocal verification
- distinguish trust-establishment (building from scratch) from trust-transfer (borrowing from a trusted anchor) from trust-exploitation (weaponizing existing trust) — each requires different defensive measures
- trust architecture has network effects: a single compromised high-trust node can cascade credibility across many downstream actors
