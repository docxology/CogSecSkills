---
name: research_methods.evidence_grading
description: Grade evidence by quality and relevance using an explicit, repeatable rubric.
---

# Evidence Grading

Evidence Grading is a structured technique for systematically rating each piece of evidence on two independent axes — quality (methodological rigor, source reliability, and internal validity) and relevance (how directly the evidence addresses the analytic question at hand) — using an explicit, repeatable rubric so that different analysts reach consistent grades from the same materials. The technique prevents high-quality-but-irrelevant evidence from inflating confidence in a conclusion, and high-relevance-but-low-quality evidence from anchoring judgments. It is foundational to systematic reviews, intelligence source evaluation, and any workflow where heterogeneous evidence must be compared or weighted.

## When to use

- when synthesizing heterogeneous evidence of varying quality and directness
- when building an analytic line that must withstand peer review or challenge
- when preparing a structured argument and need to assign explicit weights to supporting evidence
- when evidence is contested and a transparent, repeatable grading process is required for accountability

## What it produces

- a graded evidence table with quality and relevance scores for each item
- a composite weight-of-evidence narrative showing where the body of evidence points
- identification of critical evidence gaps and contradictions that lower overall confidence

## Defensive boundary

Use Evidence Grading only for research-methods and synthesis integrity: recognize, assess, document, or defend reproducibility, calibrated confidence, and transparent synthesis. Do not use this skill to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence.

## Misuse redirect

If a request asks Evidence Grading to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence, refuse that path and redirect to the safe defensive form: synthesize supplied or authorized sources with explicit confidence and uncertainty labels.

## Evidence discipline

- For Evidence Grading, bind each finding to a labeled source — study designs, source quality, reproducibility artifacts, and uncertainty records, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Evidence Grading, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Evidence Grading recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Evidence Grading: independent lines of study designs, source quality, reproducibility artifacts, and uncertainty records converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Evidence Grading: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Evidence Grading: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Evidence Grading cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Evidence Grading should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Evidence Grading, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Evidence Grading, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Evidence Grading, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Evidence Grading failure: collapsing heterogeneous evidence into an unsupported single confident conclusion.
- Evidence Grading failure: producing guidance that would help a requester cherry-pick sources, fabricate citations, or overstate certainty from weak evidence.
- Evidence Grading failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Evidence Grading to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Evidence Grading into an operational playbook to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Evidence Grading to synthesize supplied or authorized sources with explicit confidence and uncertainty labels' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- quality and relevance are independent axes — grade them separately before combining
- high relevance cannot compensate for low quality; they multiply, not add
- document the reasoning for each grade so a second analyst can reproduce or challenge it
- gaps and absences in evidence are themselves data points that belong in the graded table
