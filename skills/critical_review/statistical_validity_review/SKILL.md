---
name: critical_review.statistical_validity_review
description: Check statistical methods, power, multiple comparisons, and inference against the claims.
---

# Statistical Validity Review

Statistical Validity Review is a structured audit of a study's statistical methods against the claims it makes, checking for adequate power, appropriate test selection, honest handling of multiple comparisons, correct interpretation of p-values and confidence intervals, and absence of post-hoc outcome switching. Grounded in Gelman's Type S/M error framework, the CONSORT/STROBE reporting standards, and the ASA statement on statistical significance, it distinguishes legitimate inferential weight from statistically decorated speculation. In cognitive-security contexts it is used to evaluate whether quantitative claims weaponized in influence or disinformation campaigns rest on sound methodology.

## When to use

- a quantitative claim is cited in a policy brief, news article, or influence campaign and needs reliability assessment
- a study reports surprising or politically convenient findings with small samples
- multiple outcome measures are reported and only the significant ones are highlighted
- effect sizes are not reported alongside p-values and you need to judge practical significance
- you suspect p-hacking, HARKing (Hypothesizing After Results are Known), or selective reporting
- a meta-analysis or systematic review needs its component studies pre-screened

## What it produces

- a categorized table of statistical flaws: power issues, test misuse, multiple-comparisons inflation, assumption violations, and reporting gaps
- severity ratings (critical/moderate/minor) indicating which flaws could flip the stated conclusion
- a corrected-inference statement: the claim the statistics actually support at an honest confidence level
- a recommendation on whether the quantitative claim should be accepted, heavily qualified, or rejected

## Defensive boundary

Use Statistical Validity Review only for critical review and assurance: recognize, assess, document, or defend evidence quality, implementation integrity, and decision accountability. Do not use this skill to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.

## Misuse redirect

If a request asks Statistical Validity Review to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation, refuse that path and redirect to the safe defensive form: review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures.

## Evidence discipline

- For Statistical Validity Review, tie each statistical findings table, and corrected inference claim to concrete evidence from the specific study text, and primary claim item, source excerpt, observation, or command result that supports it.
- For Statistical Validity Review, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the statistical findings table.
- Before recommending any Statistical Validity Review action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Statistical Validity Review: the statistical findings table is supported by multiple independent artifact excerpts, test output, citations, assumptions, and reproducibility records; extract statistical claims and methods and audit power and multiple comparisons checks agree, and no unresolved contradiction would change the result.
- Medium for Statistical Validity Review: the statistical findings table is plausible, but one important study text source, comparison case, or alternative explanation remains incomplete.
- Low for Statistical Validity Review: the statistical findings table rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Statistical Validity Review cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating critical_review evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Statistical Validity Review, use only authorized study text, and primary claim, public or source-approved records, and caller-provided context needed for the defensive task.
- For Statistical Validity Review, minimize person-level detail in the statistical findings table; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Statistical Validity Review, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Statistical Validity Review: treating study text as complete when extract statistical claims and methods and audit power and multiple comparisons checks or contradictory evidence are missing.
- Statistical Validity Review: producing advice that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Statistical Validity Review: reporting the statistical findings table without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Statistical Validity Review outputs to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the statistical findings table from Statistical Validity Review into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Statistical Validity Review to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures with study text, and primary claim' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- distinguish between a statistically significant result and an adequately powered, pre-registered, single-test result — only the latter carries full inferential weight
- always ask: what was the Family-Wise Error Rate across all tests reported, and was it controlled?
- check Type S (sign) and Type M (magnitude) error risk: a small noisy study can get the direction wrong at high rates even when the p-value passes threshold
- separate the study's analysis plan (pre-specified) from its reported outcomes (post-hoc) — treat any divergence as a multiple-comparisons concern
