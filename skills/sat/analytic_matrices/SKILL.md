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

- For Analytic Matrices, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Analytic Matrices, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Analytic Matrices recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Analytic Matrices: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Analytic Matrices: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Analytic Matrices: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Analytic Matrices cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Analytic Matrices should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Analytic Matrices, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Analytic Matrices, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Analytic Matrices, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Analytic Matrices failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Analytic Matrices failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Analytic Matrices failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Analytic Matrices to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Analytic Matrices into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Analytic Matrices to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Choose axes so that the row-column intersection captures a meaningful, decidable relationship — not just a label intersection
- Blank cells are as analytically important as populated ones: they represent collection gaps or logical impossibilities that should be explained
- Conflicting cells (same position, contradictory evidence) must be flagged and adjudicated, not averaged away
- Rating schemes must be defined before filling the matrix; post-hoc scale adjustments introduce motivated reasoning
