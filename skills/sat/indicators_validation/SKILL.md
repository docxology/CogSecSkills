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

- For Indicators Validation, support each diagnosticity score and disposition with concrete evidence from the candidate indicators, the scenario set, and known base rates, and record the counterfactual reasoning that justifies it; a retained indicator whose cross-scenario behaviour was never tested against evidence is unvalidated and must be flagged, not certified.
- For Indicators Validation, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the validated indicators matrix.
- Before recommending any Indicators Validation action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Indicators Validation: each indicator's diagnosticity was tested by the counterfactual of whether it would appear when its target scenario is not unfolding, base-rate and overlap traps were checked rather than assumed away, every scenario has adequate high-diagnosticity coverage, and no unresolved contradiction would change a retain, revise, or drop disposition.
- Medium for Indicators Validation: the validated indicators matrix is plausible, but one important candidate indicators source, comparison case, or alternative explanation remains incomplete.
- Low for Indicators Validation: the validated indicators matrix rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Indicators Validation cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Indicators Validation, use only authorized candidate indicators, scenarios or hypotheses, and base rate context, public or source-approved records, and caller-provided context needed for the defensive task.
- For Indicators Validation, minimize person-level detail in the validated indicators matrix; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Indicators Validation, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Indicators Validation: passing a set as validated when individual indicators were scored without auditing aggregate scenario coverage or when confirmatory traps that fire under all outcomes were retained, leaving a scenario effectively unmonitored while the matrix looks rigorous.
- Indicators Validation: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Indicators Validation: reporting the validated indicators matrix without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Indicators Validation outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the validated indicators matrix from Indicators Validation into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Indicators Validation to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with candidate indicators, scenarios or hypotheses, and base rate context' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- the diagnosticity test: ask 'would this indicator appear even if this scenario were NOT unfolding?' — if yes, it is not diagnostic for that scenario
- apply the counterfactual: for each indicator, enumerate every scenario under which it would appear, not just the target scenario
- distinguish true-positive traps (indicators that look confirmatory but appear under all outcomes) from genuinely diagnostic signals
- coverage check: ensure every scenario has at least two high-diagnosticity indicators or flag it as a coverage gap
