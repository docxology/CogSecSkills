---
name: cognitive_security.influence_operation_mapping
description: Map an influence operation across actors, behaviors, content, and channels (ABCD).
---

# Influence Operation Mapping

Influence Operation Mapping produces a structured decomposition of a suspected or confirmed influence operation across four analytic dimensions — Actors, Behaviors, Content, and Distribution (ABCD) — adapted from the SIO framework and related investigative tradecraft (Graphika, Stanford Internet Observatory). The technique traces who is operating, what coordinated inauthentic or manipulative behaviors they exhibit, what narratives and content they produce, and through which platforms and channels content moves. The output is an operation map that supports attribution reasoning, platform reporting, counter-operation design, and public disclosure.

## When to use

- Investigating a suspected coordinated inauthentic behavior campaign on one or more platforms
- Building an evidence package for platform trust-and-safety reporting or law enforcement referral
- Analyzing a known influence operation post-takedown to understand TTPs and build future detection signatures
- Comparing a new campaign to prior actor profiles to assess whether known threat actors are responsible
- Designing a public disclosure or counter-narrative response that requires accurate understanding of operation structure

## What it produces

- A structured ABCD map decomposing the operation by actors (account clusters and likely principals), behaviors (coordinated inauthentic tactics), content (narrative themes and formats), and distribution (platform pathways and amplification patterns)
- An attribution confidence assessment with explicit alternative hypotheses and a tiered confidence rating
- A behavioral fingerprint usable for detecting future operations by the same actor or using the same TTPs
- Prioritized defensive and counter-operation recommendations tied to the specific operation structure

## Defensive boundary

Use Influence Operation Mapping only for cognitive-security defense: recognize, assess, document, or defend audiences, decision-makers, and public discourse. Do not use this skill to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.

## Misuse redirect

If a request asks Influence Operation Mapping to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation, refuse that path and redirect to the safe defensive form: assess supplied material for manipulation indicators and recommend resilience measures.

## Evidence discipline

- For Influence Operation Mapping, bind each finding to a labeled source — content, behavioral, narrative, media, and audience-risk evidence, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Influence Operation Mapping, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Influence Operation Mapping recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Influence Operation Mapping: independent lines of content, behavioral, narrative, media, and audience-risk evidence converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Influence Operation Mapping: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Influence Operation Mapping: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Influence Operation Mapping cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Influence Operation Mapping should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Influence Operation Mapping, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Influence Operation Mapping, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Influence Operation Mapping, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Influence Operation Mapping failure: mistaking persuasive resonance for verified harm or intent.
- Influence Operation Mapping failure: producing guidance that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Influence Operation Mapping failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Influence Operation Mapping to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Influence Operation Mapping into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Influence Operation Mapping to assess supplied material for manipulation indicators and recommend resilience measures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Work the ABCD dimensions independently before synthesizing — conflating actor and content analysis leads to circular attribution
- Treat attribution as a hypothesis under evidence, not a conclusion; always state the alternative explanations and what evidence would change the assessment
- Distinguish coordinated inauthentic behavior from organic polarization — coordination indicators (timing, infrastructure, template reuse) must be empirical, not inferred from content alone
- Document the evidence chain: every element of the map should link to a specific artifact, not to an inference chain from a single indicator
