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

## Defensive boundary

Use Information Provenance Tracing only for cognitive-security defense: recognize, assess, document, or defend audiences, decision-makers, and public discourse. Do not use this skill to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.

## Misuse redirect

If a request asks Information Provenance Tracing to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation, refuse that path and redirect to the safe defensive form: assess supplied material for manipulation indicators and recommend resilience measures.

## Evidence discipline

- For Information Provenance Tracing, bind each finding to a labeled source — content, behavioral, narrative, media, and audience-risk evidence, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Information Provenance Tracing, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Information Provenance Tracing recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Information Provenance Tracing: independent lines of content, behavioral, narrative, media, and audience-risk evidence converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Information Provenance Tracing: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Information Provenance Tracing: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Information Provenance Tracing cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Information Provenance Tracing should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Information Provenance Tracing, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Information Provenance Tracing, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Information Provenance Tracing, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Information Provenance Tracing failure: mistaking persuasive resonance for verified harm or intent.
- Information Provenance Tracing failure: producing guidance that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Information Provenance Tracing failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Information Provenance Tracing to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Information Provenance Tracing into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Information Provenance Tracing to assess supplied material for manipulation indicators and recommend resilience measures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Follow the artifact to the oldest recoverable instance — 'first known appearance' is the operative standard when true origin cannot be confirmed
- Distinguish mutation (meaning changed across republications) from corruption (factual content altered) from decontextualization (authentic content placed in false context)
- Assess source reliability independently from source earliness — the first source may itself be an anonymous or fabricated account
- Record every step with a retrievable URL or archive link so the chain can be independently verified
