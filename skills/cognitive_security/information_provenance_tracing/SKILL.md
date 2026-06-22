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

- For Information Provenance Tracing, record every link in the chain with retrievable evidence — an archive link, a WHOIS or account-creation date, a reverse-image result, or a verbatim quote — and tie each origin and mutation claim to that evidence so the chain can be independently re-verified.
- For Information Provenance Tracing, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the provenance chain.
- Before recommending any Information Provenance Tracing action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Information Provenance Tracing: the provenance chain reaches a retrievable earliest instance whose source authenticity is independently confirmed, each republication's mutations are documented against adjacent links, and no unresolved contradiction would change the confidence-rated origin verdict.
- Medium for Information Provenance Tracing: the provenance chain is plausible, but one important artifact source, comparison case, or alternative explanation remains incomplete.
- Low for Information Provenance Tracing: the provenance chain rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Information Provenance Tracing cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating cognitive_security evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Information Provenance Tracing, use only authorized artifact, known context, and scope, public or source-approved records, and caller-provided context needed for the defensive task.
- For Information Provenance Tracing, minimize person-level detail in the provenance chain; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Information Provenance Tracing, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Information Provenance Tracing: treating the earliest found instance as the true origin without confirming the source node's authenticity or recording the mutation log, so a fabricated first publisher passes as a verified primary source and decontextualization goes unnoticed.
- Information Provenance Tracing: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Information Provenance Tracing: reporting the provenance chain without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Information Provenance Tracing outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the provenance chain from Information Provenance Tracing into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Information Provenance Tracing to assess supplied material for manipulation indicators and recommend resilience measures with artifact, known context, and scope' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Follow the artifact to the oldest recoverable instance — 'first known appearance' is the operative standard when true origin cannot be confirmed
- Distinguish mutation (meaning changed across republications) from corruption (factual content altered) from decontextualization (authentic content placed in false context)
- Assess source reliability independently from source earliness — the first source may itself be an anonymous or fabricated account
- Record every step with a retrievable URL or archive link so the chain can be independently verified
