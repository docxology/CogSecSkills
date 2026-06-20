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

- For Evidence Grading, tie each graded evidence table, and weight of evidence summary claim to concrete evidence from the specific analytic question, evidence items, and grading rubric item, source excerpt, observation, or command result that supports it.
- For Evidence Grading, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the graded evidence table.
- Before recommending any Evidence Grading action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Evidence Grading: the graded evidence table is supported by multiple independent study designs, source quality, reproducibility artifacts, and uncertainty records; inventory and characterize each evidence item and grade quality for each item checks agree, and no unresolved contradiction would change the result.
- Medium for Evidence Grading: the graded evidence table is plausible, but one important analytic question source, comparison case, or alternative explanation remains incomplete.
- Low for Evidence Grading: the graded evidence table rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Evidence Grading cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating research_methods evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Evidence Grading, use only authorized analytic question, evidence items, and grading rubric, public or source-approved records, and caller-provided context needed for the defensive task.
- For Evidence Grading, minimize person-level detail in the graded evidence table; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Evidence Grading, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Evidence Grading: treating analytic question as complete when inventory and characterize each evidence item and grade quality for each item checks or contradictory evidence are missing.
- Evidence Grading: producing advice that would help a requester cherry-pick sources, fabricate citations, or overstate certainty from weak evidence.
- Evidence Grading: reporting the graded evidence table without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Evidence Grading outputs to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the graded evidence table from Evidence Grading into an operational playbook to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Evidence Grading to synthesize supplied or authorized sources with explicit confidence and uncertainty labels with analytic question, evidence items, and grading rubric' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- quality and relevance are independent axes — grade them separately before combining
- high relevance cannot compensate for low quality; they multiply, not add
- document the reasoning for each grade so a second analyst can reproduce or challenge it
- gaps and absences in evidence are themselves data points that belong in the graded table
