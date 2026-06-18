---
name: cognitive_security.information_provenance_tracing
description: Trace a claim back to its origin through the chain of republication and mutation.
---

# Information Provenance Tracing

Information provenance tracing reconstructs the origin and mutation history of a specific claim, image, video, or dataset by following each documented republication back through the chain of custody to the earliest recoverable source. Unlike information laundering tracing (which focuses on legitimization tactics), provenance tracing is a fact-finding technique that asks 'where did this actually come from and how has it changed?' — establishing whether a claim descends from verified reporting, a fabricated source, or a misrepresentation of authentic material.

## When to use

- A claim has spread widely and its original source is disputed or unknown
- An image, video, or dataset is circulating out of context and needs verification of its actual origin
- A citation chain needs to be followed back to determine whether it ultimately rests on a verifiable primary source or a fabrication
- Countering a narrative requires demonstrating where it originated and how meaning changed in transit

## What it produces

- A chronological chain from earliest recoverable instance to the artifact under examination, with each link annotated for source type and reliability
- A mutation log noting how the claim's meaning, framing, or attributions changed at each republication
- A confidence-rated origin verdict: verified primary source, probable origin, ambiguous, or fabricated

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Follow the artifact to the oldest recoverable instance — 'first known appearance' is the operative standard when true origin cannot be confirmed
- Distinguish mutation (meaning changed across republications) from corruption (factual content altered) from decontextualization (authentic content placed in false context)
- Assess source reliability independently from source earliness — the first source may itself be an anonymous or fabricated account
- Record every step with a retrievable URL or archive link so the chain can be independently verified
