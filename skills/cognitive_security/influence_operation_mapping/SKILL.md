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

- For Influence Operation Mapping, tie each abcd operation map, attribution assessment, and counter operation brief claim to concrete evidence from the specific evidence collection, hypothesis, and threat actor profiles item, source excerpt, observation, or command result that supports it.
- For Influence Operation Mapping, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the abcd operation map.
- Before recommending any Influence Operation Mapping action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Influence Operation Mapping: the abcd operation map is supported by multiple independent content, behavioral, narrative, media, and audience-risk evidence; inventory evidence and scope operation and decompose actors checks agree, and no unresolved contradiction would change the result.
- Medium for Influence Operation Mapping: the abcd operation map is plausible, but one important evidence collection source, comparison case, or alternative explanation remains incomplete.
- Low for Influence Operation Mapping: the abcd operation map rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Influence Operation Mapping cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating cognitive_security evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Influence Operation Mapping, use only authorized evidence collection, hypothesis, and threat actor profiles, public or source-approved records, and caller-provided context needed for the defensive task.
- For Influence Operation Mapping, minimize person-level detail in the abcd operation map; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Influence Operation Mapping, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Influence Operation Mapping: treating evidence collection as complete when inventory evidence and scope operation and decompose actors checks or contradictory evidence are missing.
- Influence Operation Mapping: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Influence Operation Mapping: reporting the abcd operation map without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Influence Operation Mapping outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the abcd operation map from Influence Operation Mapping into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Influence Operation Mapping to assess supplied material for manipulation indicators and recommend resilience measures with evidence collection, hypothesis, and threat actor profiles' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Work the ABCD dimensions independently before synthesizing — conflating actor and content analysis leads to circular attribution
- Treat attribution as a hypothesis under evidence, not a conclusion; always state the alternative explanations and what evidence would change the assessment
- Distinguish coordinated inauthentic behavior from organic polarization — coordination indicators (timing, infrastructure, template reuse) must be empirical, not inferred from content alone
- Document the evidence chain: every element of the map should link to a specific artifact, not to an inference chain from a single indicator
