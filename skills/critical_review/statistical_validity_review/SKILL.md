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

- For Statistical Validity Review, bind each finding to a labeled source — artifact excerpts, test output, citations, assumptions, and reproducibility records, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Statistical Validity Review, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Statistical Validity Review recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Statistical Validity Review: independent lines of artifact excerpts, test output, citations, assumptions, and reproducibility records converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Statistical Validity Review: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Statistical Validity Review: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Statistical Validity Review cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Statistical Validity Review should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Statistical Validity Review, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Statistical Validity Review, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Statistical Validity Review, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Statistical Validity Review failure: performing theatrical critique without concrete evidence, severity, or remediation path.
- Statistical Validity Review failure: producing guidance that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Statistical Validity Review failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Statistical Validity Review to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Statistical Validity Review into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Statistical Validity Review to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- distinguish between a statistically significant result and an adequately powered, pre-registered, single-test result — only the latter carries full inferential weight
- always ask: what was the Family-Wise Error Rate across all tests reported, and was it controlled?
- check Type S (sign) and Type M (magnitude) error risk: a small noisy study can get the direction wrong at high rates even when the p-value passes threshold
- separate the study's analysis plan (pre-specified) from its reported outcomes (post-hoc) — treat any divergence as a multiple-comparisons concern
