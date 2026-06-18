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

## Anti-criteria (must NOT happen)
- do not treat a statistically significant p-value as self-validating — significance is necessary but not sufficient for a trustworthy finding
- do not dismiss a study solely because of a small sample without also checking whether effect size and confidence intervals are consistent with the claim
- do not confuse reporting standards (e.g., CONSORT compliance) with actual statistical validity — a well-formatted report can still be analytically flawed
- do not apply this audit to reject inconvenient findings; rate severity by methodological criteria alone, independent of the direction of the result

## AGEINT upstream
`docs/ageint/adversarial-assurance.md`
