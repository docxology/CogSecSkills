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

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Work the ABCD dimensions independently before synthesizing — conflating actor and content analysis leads to circular attribution
- Treat attribution as a hypothesis under evidence, not a conclusion; always state the alternative explanations and what evidence would change the assessment
- Distinguish coordinated inauthentic behavior from organic polarization — coordination indicators (timing, infrastructure, template reuse) must be empirical, not inferred from content alone
- Document the evidence chain: every element of the map should link to a specific artifact, not to an inference chain from a single indicator
