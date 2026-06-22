# Workflow — Statistical Validity Review

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Extract statistical claims and methods (read)
Record every quantitative claim: test used, sample size, reported p-value, effect size, confidence interval, and whether analysis was pre-registered or pre-specified. Note how many outcome variables were measured and how many are reported as significant.

## Step 2 — Audit power and multiple comparisons (reason)
Estimate whether the sample size was adequate for the effect size claimed (use Cohen's conventions or the study's own domain norms). Count the number of statistical tests performed (explicit and implicit through reported subgroup comparisons) and assess whether the Type I error rate was controlled (Bonferroni, FDR, or pre-registration). Flag any garden-of-forking-paths indicators: selective reporting, undisclosed exclusions, outcome switching.

## Step 3 — Check test appropriateness and assumption violations (reason)
Verify that the statistical test matches the data type and distribution (e.g., t-test on ordinal data, parametric test on heavily skewed distributions). Check whether key assumptions (independence, normality, homoscedasticity) are tested or acknowledged. Assess whether effect sizes are reported and whether they indicate practical significance independent of significance testing.

## Step 4 — Produce findings table and corrected inference (write)
Write the statistical findings table: each row is one identified issue with category, evidence, severity, and inferential consequence. Then write the corrected-inference narrative: state explicitly what the data support after applying honest statistical discipline, and classify the primary claim as: supported, partially supported (with caveats), or insufficiently supported.

## Evidence requirements
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

## Failure modes
- Statistical Validity Review failure: performing theatrical critique without concrete evidence, severity, or remediation path.
- Statistical Validity Review failure: producing guidance that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Statistical Validity Review failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Statistical Validity Review to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Statistical Validity Review into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Statistical Validity Review to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not treat a statistically significant p-value as self-validating — significance is necessary but not sufficient for a trustworthy finding
- do not dismiss a study solely because of a small sample without also checking whether effect size and confidence intervals are consistent with the claim
- do not confuse reporting standards (e.g., CONSORT compliance) with actual statistical validity — a well-formatted report can still be analytically flawed
- do not apply this audit to reject inconvenient findings; rate severity by methodological criteria alone, independent of the direction of the result

## AGEINT upstream
`docs/ageint/adversarial-assurance.md`
