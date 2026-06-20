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

- For Cross-Impact Matrix, tie each cross impact matrix, loop inventory, and leverage ranking claim to concrete evidence from the specific driver list, influence scale, and focal question item, source excerpt, observation, or command result that supports it.
- For Cross-Impact Matrix, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the cross impact matrix.
- Before recommending any Cross-Impact Matrix action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Cross-Impact Matrix: the cross impact matrix is supported by multiple independent hypotheses, assumptions, indicators, evidence tables, and confidence notes; establish the driver set and fill the matrix cell by cell checks agree, and no unresolved contradiction would change the result.
- Medium for Cross-Impact Matrix: the cross impact matrix is plausible, but one important driver list source, comparison case, or alternative explanation remains incomplete.
- Low for Cross-Impact Matrix: the cross impact matrix rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Cross-Impact Matrix cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Cross-Impact Matrix, use only authorized driver list, influence scale, and focal question, public or source-approved records, and caller-provided context needed for the defensive task.
- For Cross-Impact Matrix, minimize person-level detail in the cross impact matrix; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Cross-Impact Matrix, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Cross-Impact Matrix: treating driver list as complete when establish the driver set and fill the matrix cell by cell checks or contradictory evidence are missing.
- Cross-Impact Matrix: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Cross-Impact Matrix: reporting the cross impact matrix without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Cross-Impact Matrix outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the cross impact matrix from Cross-Impact Matrix into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Cross-Impact Matrix to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with driver list, influence scale, and focal question' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- assess each cell (i→j) independently before looking at the full matrix — premature holistic framing biases individual cells
- distinguish direction (positive/negative) from magnitude — a strong negative relationship is as important as a strong positive one
- row sums reveal active drivers; column sums reveal sensitive/dependent variables — both matter for intervention design
