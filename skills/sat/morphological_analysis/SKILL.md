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

- For Morphological Analysis, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Morphological Analysis, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Morphological Analysis recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Morphological Analysis: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Morphological Analysis: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Morphological Analysis: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Morphological Analysis cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Morphological Analysis should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Morphological Analysis, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Morphological Analysis, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Morphological Analysis, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Morphological Analysis failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Morphological Analysis failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Morphological Analysis failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Morphological Analysis to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Morphological Analysis into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Morphological Analysis to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- parameters must be genuinely independent — if two dimensions co-vary mechanically, collapse them into one
- enumerate value sets exhaustively before pruning — premature pruning re-introduces the closure the technique is designed to prevent
- record the reason for every pruned cell; a cell removed for the wrong reason is where the surprise will come from
- the most-dangerous scenario and the most-likely scenario are often different cells — report both
