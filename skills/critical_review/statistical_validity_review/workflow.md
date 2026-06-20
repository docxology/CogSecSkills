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

## Failure modes
- Statistical Validity Review: treating study text as complete when extract statistical claims and methods and audit power and multiple comparisons checks or contradictory evidence are missing.
- Statistical Validity Review: producing advice that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Statistical Validity Review: reporting the statistical findings table without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Statistical Validity Review outputs to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the statistical findings table from Statistical Validity Review into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Statistical Validity Review to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures with study text, and primary claim' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not treat a statistically significant p-value as self-validating — significance is necessary but not sufficient for a trustworthy finding
- do not dismiss a study solely because of a small sample without also checking whether effect size and confidence intervals are consistent with the claim
- do not confuse reporting standards (e.g., CONSORT compliance) with actual statistical validity — a well-formatted report can still be analytically flawed
- do not apply this audit to reject inconvenient findings; rate severity by methodological criteria alone, independent of the direction of the result

## AGEINT upstream
`docs/ageint/adversarial-assurance.md`
