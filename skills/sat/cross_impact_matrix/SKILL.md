---
name: sat.cross_impact_matrix
description: Assess how each driver influences every other to find leverage and feedback.
---

# Cross-Impact Matrix

The Cross-Impact Matrix is a structured technique for mapping how each driver, trend, or variable in a system affects every other one, enabling analysts to identify reinforcing feedback loops, inhibitory relationships, and high-leverage nodes whose change cascades through the system. Cells in the matrix record the direction and magnitude of influence (positive, negative, neutral, conditional) rather than independent assessments of each factor. The technique is widely used in scenario planning, strategic foresight, and systemic-threat analysis to surface non-obvious interdependencies that single-variable analysis misses.

## When to use

- preparing for scenario development where key drivers need to be understood as a system rather than independently
- assessing the systemic consequences of an adversary's action on multiple domains simultaneously
- prioritizing intervention points when resources are constrained — the high-leverage node deserves the most attention
- checking whether a single-driver analysis has missed critical feedback effects

## What it produces

- a filled N×N influence matrix making all pairwise driver relationships explicit and comparable
- an inventory of feedback loops — reinforcing loops that amplify change and balancing loops that dampen it
- a leverage ranking distinguishing active drivers (high outgoing influence) from passive indicators (high incoming influence)
- analytic narrative tying the structural findings to the focal analytic or planning question

## Defensive boundary

Use Cross-Impact Matrix only for structured analytic technique support: recognize, assess, document, or defend analytic rigor, alternative hypotheses, and calibrated judgment. Do not use this skill to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.

## Misuse redirect

If a request asks Cross-Impact Matrix to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation, refuse that path and redirect to the safe defensive form: apply the structured technique to supplied evidence while preserving alternatives and uncertainty.

## Evidence discipline

- For Cross-Impact Matrix, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Cross-Impact Matrix, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Cross-Impact Matrix recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Cross-Impact Matrix: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Cross-Impact Matrix: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Cross-Impact Matrix: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Cross-Impact Matrix cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Cross-Impact Matrix should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Cross-Impact Matrix, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Cross-Impact Matrix, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Cross-Impact Matrix, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Cross-Impact Matrix failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Cross-Impact Matrix failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Cross-Impact Matrix failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Cross-Impact Matrix to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Cross-Impact Matrix into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Cross-Impact Matrix to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- assess each cell (i→j) independently before looking at the full matrix — premature holistic framing biases individual cells
- distinguish direction (positive/negative) from magnitude — a strong negative relationship is as important as a strong positive one
- row sums reveal active drivers; column sums reveal sensitive/dependent variables — both matter for intervention design
