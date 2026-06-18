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

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- distinguish between a statistically significant result and an adequately powered, pre-registered, single-test result — only the latter carries full inferential weight
- always ask: what was the Family-Wise Error Rate across all tests reported, and was it controlled?
- check Type S (sign) and Type M (magnitude) error risk: a small noisy study can get the direction wrong at high rates even when the p-value passes threshold
- separate the study's analysis plan (pre-specified) from its reported outcomes (post-hoc) — treat any divergence as a multiple-comparisons concern
