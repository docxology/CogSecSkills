---
name: sat.morphological_analysis
description: Enumerate the parameter space of a problem to bound the set of possibilities.
---

# Morphological Analysis

Morphological analysis (Zwicky 1969; Ritchey 2011) decomposes a complex problem into its independent parameters, enumerates the discrete values each parameter can take, and maps the full cross-product to bound the space of possible configurations. In intelligence and cognitive-security contexts it prevents premature closure on a single scenario by forcing analysts to articulate every combination that remains logically consistent with current evidence, including surprising or low-salience possibilities.

## When to use

- an analysis is at risk of anchoring on the most familiar or most recent scenario while ignoring equally plausible alternatives
- a threat space has multiple independent axes (actor identity, method, target, timing) and all combinations need to be surfaced before prioritization
- collection requirements need to be written to discriminate among specific configurations in the parameter space
- a cognitive-security audit needs to catalogue the distinct narrative architectures an influence operation could adopt

## What it produces

- a complete enumeration of logically possible scenarios bounded by the chosen parameters
- explicit identification of which combinations are ruled out by known constraints and why
- a scenario inventory tagged by current evidential support, enabling targeted collection to close gaps

## Defensive boundary

Use Morphological Analysis only for structured analytic technique support: recognize, assess, document, or defend analytic rigor, alternative hypotheses, and calibrated judgment. Do not use this skill to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.

## Misuse redirect

If a request asks Morphological Analysis to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation, refuse that path and redirect to the safe defensive form: apply the structured technique to supplied evidence while preserving alternatives and uncertainty.

## Evidence discipline

- For Morphological Analysis, tie each parameter, each enumerated value, and every pruning decision to concrete evidence from the problem statement and known constraints, recording the ruling-out reason per excluded cell; a combination removed without evidential justification is an unexamined possibility and must be reinstated or its exclusion explicitly defended.
- For Morphological Analysis, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the morphological box.
- Before recommending any Morphological Analysis action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Morphological Analysis: the chosen parameters are genuinely independent, each value set was enumerated exhaustively before any pruning, every excluded cell carries a documented logical or evidential reason, and no unresolved contradiction would change the surviving scenario inventory or which cells are flagged most-likely and most-dangerous.
- Medium for Morphological Analysis: the morphological box is plausible, but one important problem statement source, comparison case, or alternative explanation remains incomplete.
- Low for Morphological Analysis: the morphological box rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Morphological Analysis cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Morphological Analysis, use only authorized problem statement, and known constraints, public or source-approved records, and caller-provided context needed for the defensive task.
- For Morphological Analysis, minimize person-level detail in the morphological box; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Morphological Analysis, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Morphological Analysis: treating the scenario space as bounded when cells were pruned on intuition or familiarity without a documented basis, or when co-varying parameters were left un-collapsed, so the configuration where the surprise actually lives is silently excluded from the inventory.
- Morphological Analysis: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Morphological Analysis: reporting the morphological box without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Morphological Analysis outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the morphological box from Morphological Analysis into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Morphological Analysis to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with problem statement, and known constraints' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- parameters must be genuinely independent — if two dimensions co-vary mechanically, collapse them into one
- enumerate value sets exhaustively before pruning — premature pruning re-introduces the closure the technique is designed to prevent
- record the reason for every pruned cell; a cell removed for the wrong reason is where the surprise will come from
- the most-dangerous scenario and the most-likely scenario are often different cells — report both
