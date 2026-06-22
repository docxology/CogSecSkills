---
name: sat.indicators_validation
description: Test indicators for diagnosticity: do they actually discriminate between outcomes?
---

# Indicators Validation

Indicators Validation is a quality-control technique that stress-tests a candidate indicator set to determine whether each indicator genuinely discriminates among the scenarios it is claimed to distinguish. It applies diagnosticity tests — asking whether an indicator would appear under only one outcome, under several, or under all — and prunes or restructures the indicator set accordingly. This prevents the common failure mode in which analysts collect confirmatory data against indicators that would appear regardless of which outcome is unfolding.

## When to use

- after an initial indicators generation pass, before deploying an indicator set for live monitoring
- when a monitoring regime has produced unexpected false positives or missed events
- when inherited indicator sets need a quality audit
- when indicators are being used in high-stakes warning contexts where a false negative or false positive carries significant cost

## What it produces

- a diagnosticity rating for every candidate indicator (high / medium / low / invalid)
- a disposition decision for each indicator: retain as-is, revise to increase specificity, or drop
- identification of scenario gaps — scenarios that lack a sufficient number of high-diagnosticity indicators
- a clean, validated indicators matrix ready for operational monitoring

## Defensive boundary

Use Indicators Validation only for structured analytic technique support: recognize, assess, document, or defend analytic rigor, alternative hypotheses, and calibrated judgment. Do not use this skill to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.

## Misuse redirect

If a request asks Indicators Validation to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation, refuse that path and redirect to the safe defensive form: apply the structured technique to supplied evidence while preserving alternatives and uncertainty.

## Evidence discipline

- For Indicators Validation, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Indicators Validation, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Indicators Validation recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Indicators Validation: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Indicators Validation: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Indicators Validation: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Indicators Validation cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Indicators Validation should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Indicators Validation, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Indicators Validation, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Indicators Validation, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Indicators Validation failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Indicators Validation failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Indicators Validation failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Indicators Validation to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Indicators Validation into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Indicators Validation to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- the diagnosticity test: ask 'would this indicator appear even if this scenario were NOT unfolding?' — if yes, it is not diagnostic for that scenario
- apply the counterfactual: for each indicator, enumerate every scenario under which it would appear, not just the target scenario
- distinguish true-positive traps (indicators that look confirmatory but appear under all outcomes) from genuinely diagnostic signals
- coverage check: ensure every scenario has at least two high-diagnosticity indicators or flag it as a coverage gap
