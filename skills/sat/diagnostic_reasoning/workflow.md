# Workflow — Diagnostic Reasoning

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — State the datum and the hypothesis set (read)
Record the new datum precisely. List all active competing hypotheses. Note the current prior assessment (relative likelihood) for each hypothesis before this datum is considered.

## Step 2 — Assess expected likelihood per hypothesis (reason)
For each hypothesis H, ask: 'If H were true, how likely would we be to see this specific datum?' Rate each on a qualitative scale (very likely / somewhat likely / roughly neutral / somewhat unlikely / very unlikely). Then ask: 'If H were false, how likely would this datum be?' The ratio of these two assessments is the likelihood ratio.

## Step 3 — Determine direction and magnitude of update (reason)
Compare the likelihood ratios across hypotheses. Hypotheses where the datum is much more likely than under alternatives gain support; those where it is much less likely lose ground. Hypotheses where the likelihood ratio is near 1 are unchanged. Note that a datum can simultaneously support one hypothesis and refute another.

## Step 4 — Assess diagnostic value (reason, write)
Determine whether this datum is highly diagnostic (large spread in likelihood ratios across hypotheses), moderately diagnostic, or low-diagnostic (all ratios near 1). If low-diagnostic, explain what evidence would be more discriminating.

## Step 5 — Produce updated ranking and table (write)
Fill the diagnostic table. Write the updated hypothesis ranking with explicit reasoning. Note if the datum warrants a significant change in the lead hypothesis or only a marginal adjustment. Flag if collection against a specific more-diagnostic indicator is recommended.

## Anti-criteria (must NOT happen)
- do not treat evidence as confirming simply because it is consistent with the favored hypothesis — consistency without a high likelihood ratio is not confirmation
- do not process multiple data items simultaneously in one diagnostic assessment — each datum must be evaluated in isolation to preserve the logic
- do not allow the qualitative likelihood labels to substitute for explicit comparative reasoning across hypotheses — the ratio is the finding, not the label in isolation

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
