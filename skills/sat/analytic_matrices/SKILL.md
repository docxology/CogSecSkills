---
name: sat.analytic_matrices
description: Cross-tabulate variables to organize evidence and reveal relationships.
---

# Analytic Matrices

Analytic Matrices organize analytic variables (hypotheses, actors, drivers, criteria) as rows and columns of a structured grid, then systematically populate each cell with evidence, ratings, or judgments. The technique makes the analyst's logic explicit and auditable, surfaces blank cells (missing evidence) and conflicting cells (contradictory evidence), and reduces the cognitive load of tracking multiple dimensions simultaneously. It is used in intelligence analysis as a pre-step to ACH, in option analysis, and in influence-operation assessment to map actors against capabilities and behaviors.

## When to use

- Multiple competing hypotheses, options, or actors must be systematically compared against the same evidence base or criteria
- The analyst needs to make implicit evidence-weighting explicit and auditable for peer review or management
- There is risk of selective attention — remembering only the evidence that fits the leading hypothesis
- A complex problem involves several interacting dimensions that are hard to hold in working memory simultaneously

## What it produces

- A structured grid making the analyst's reasoning transparent and independently reviewable
- An explicit map of evidential coverage showing where gaps and conflicts exist
- A pattern-level view of the problem that is harder to achieve through narrative alone
- A reusable artifact that can be updated as new evidence arrives without rewriting prose

## Defensive boundary

Use Analytic Matrices only for structured analytic technique support: recognize, assess, document, or defend analytic rigor, alternative hypotheses, and calibrated judgment. Do not use this skill to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.

## Misuse redirect

If a request asks Analytic Matrices to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation, refuse that path and redirect to the safe defensive form: apply the structured technique to supplied evidence while preserving alternatives and uncertainty.

## Evidence discipline

- For Analytic Matrices, anchor each cell rating and the pattern summary to a cited source excerpt or rationale, record blank cells as explicit collection gaps rather than silent omissions, and present the full grid as evidence so a reviewer can audit the reasoning instead of trusting a collapsed single answer.
- For Analytic Matrices, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the analytic matrix.
- Before recommending any Analytic Matrices action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Analytic Matrices: the row and column axes capture a genuinely independent, decidable relationship, every cell is rated against a scheme fixed before population, blank and conflicting cells are explicitly adjudicated, the dominant pattern is corroborated by multiple sources, and no unresolved contradiction would overturn the leading row.
- Medium for Analytic Matrices: the analytic matrix is plausible, but one important analytic question source, comparison case, or alternative explanation remains incomplete.
- Low for Analytic Matrices: the analytic matrix rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Analytic Matrices cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Analytic Matrices, use only authorized analytic question, variables or hypotheses, and evidence or criteria, public or source-approved records, and caller-provided context needed for the defensive task.
- For Analytic Matrices, minimize person-level detail in the analytic matrix; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Analytic Matrices, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Analytic Matrices: treating a grid riddled with blank cells as a finished analysis or letting the rating scale drift during population, so unexamined gaps and post-hoc scoring quietly manufacture a winning row that the underlying evidence never earned.
- Analytic Matrices: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Analytic Matrices: reporting the analytic matrix without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Analytic Matrices outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the analytic matrix from Analytic Matrices into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Analytic Matrices to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with analytic question, variables or hypotheses, and evidence or criteria' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Choose axes so that the row-column intersection captures a meaningful, decidable relationship — not just a label intersection
- Blank cells are as analytically important as populated ones: they represent collection gaps or logical impossibilities that should be explained
- Conflicting cells (same position, contradictory evidence) must be flagged and adjudicated, not averaged away
- Rating schemes must be defined before filling the matrix; post-hoc scale adjustments introduce motivated reasoning
