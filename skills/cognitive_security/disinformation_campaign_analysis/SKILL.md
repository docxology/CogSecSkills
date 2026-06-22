---
name: cognitive_security.disinformation_campaign_analysis
description: Decompose a campaign's objectives, narratives, TTPs, and amplification structure.
---

# Disinformation Campaign Analysis

Disinformation Campaign Analysis is a structured decomposition of an apparent coordinated influence operation into its constituent objectives, narrative architecture, actor network, tactics/techniques/procedures (TTPs), amplification infrastructure, and intended target audiences. The technique synthesizes frameworks from the intelligence community (DISARM Framework, EU STRATCOM, NATO StratCom COE), social-network analysis, and computational propaganda research to produce a structured campaign model that supports attribution, counter-strategy design, and resilience policy. It is strictly defensive and descriptive: the output characterizes what has happened or is happening to enable protection and response, not to facilitate imitation.

## When to use

- when a coordinated pattern of misleading content appears to be organized and purposeful rather than spontaneous
- when a platform or government body needs to characterize a suspected influence operation for policy response or public disclosure
- when a researcher, journalist, or analyst needs to map the structure of a disinformation campaign to understand its scope and intent
- before designing counter-messaging or resilience responses — the campaign model must be understood before counter-strategies can be correctly targeted
- when comparing a new suspected campaign against prior documented campaigns for attribution or pattern-matching purposes

## What it produces

- a campaign objective assessment: what the operation appears designed to achieve (sow division, suppress turnout, delegitimize institutions, create false consensus, etc.)
- a narrative hierarchy: the master narrative (the central false frame), supporting sub-narratives, and how they interlock
- an actor network description: visible accounts/channels, suspected coordination signals (timing, content synchronization, amplification patterns), and a confidence-rated attribution level
- a TTP inventory mapped to a recognized framework (DISARM) with specific manifestation descriptions for this campaign
- an amplification infrastructure characterization: platforms, bot/automation signals, cross-platform seeding patterns, engagement manipulation tactics
- a target audience profile: who the campaign appears designed to reach and why they may be vulnerable to this specific narrative package

## Defensive boundary

Use Disinformation Campaign Analysis only for cognitive-security defense: recognize, assess, document, or defend audiences, decision-makers, and public discourse. Do not use this skill to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.

## Misuse redirect

If a request asks Disinformation Campaign Analysis to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation, refuse that path and redirect to the safe defensive form: assess supplied material for manipulation indicators and recommend resilience measures.

## Evidence discipline

- For Disinformation Campaign Analysis, bind each finding to a labeled source — content, behavioral, narrative, media, and audience-risk evidence, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Disinformation Campaign Analysis, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Disinformation Campaign Analysis recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Disinformation Campaign Analysis: independent lines of content, behavioral, narrative, media, and audience-risk evidence converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Disinformation Campaign Analysis: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Disinformation Campaign Analysis: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Disinformation Campaign Analysis cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Disinformation Campaign Analysis should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Disinformation Campaign Analysis, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Disinformation Campaign Analysis, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Disinformation Campaign Analysis, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Disinformation Campaign Analysis failure: mistaking persuasive resonance for verified harm or intent.
- Disinformation Campaign Analysis failure: producing guidance that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Disinformation Campaign Analysis failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Disinformation Campaign Analysis to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Disinformation Campaign Analysis into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Disinformation Campaign Analysis to assess supplied material for manipulation indicators and recommend resilience measures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- separate observation from inference from attribution: clearly label what is directly observed in artifacts, what is inferred from patterns, and what is attributed to an actor with what confidence
- a narrative hierarchy is not a list of false claims — identify the master narrative frame that unifies the claims and makes them mutually reinforcing
- use a recognized TTP taxonomy (DISARM preferred) so findings are comparable across campaigns and actionable for counter-strategy
- coordination signals matter as much as content: synchronized timing, cross-amplification, identical text variants, and inauthentic behavior patterns are often more diagnostic than content alone
- be explicit about alternative explanations: spontaneous viral misinformation can mimic coordinated campaigns; state what would distinguish them
- attribution confidence must be explicitly rated on a scale (Low/Moderate/High) with stated basis — never assert attribution without stating the evidence
