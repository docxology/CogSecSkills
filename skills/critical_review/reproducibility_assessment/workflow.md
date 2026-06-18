# Workflow — Reproducibility Assessment

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Inventory stated methods and materials (read)
Read the artifact in full. Extract: the key claims to be verified; the data sources and their access status (public/private/restricted); the code repository or notebook location; the stated environment (OS, language version, library versions); any stated random seeds; and the preprocessing and analysis pipeline as documented.

## Step 2 — Assess data and code availability (reason)
For each required input (data, code, model weights, preprocessing scripts), check availability: is it accessible? is it versioned or pinned? does the described artifact match what is actually provided? Flag discrepancies. If key data or code is missing, mark the relevant claims as 'not assessable' for direct reproduction.

## Step 3 — Attempt direct reproduction (exec)
Where data, code, and environment are available, execute the pipeline following only the documented steps. Record actual outputs and compare to claimed results (numbers, figures, tables). Note any undocumented steps required to get the code to run. Record exact deviations between claimed and reproduced results, including direction and magnitude.

## Step 4 — Classify gaps and assess tiers (reason)
For each key claim, classify reproducibility status at each tier: direct (same data + code), replication (same method + new data), and conceptual (same hypothesis + different operationalization). Identify the root cause of each gap: missing data, missing code, undocumented preprocessing, environment sensitivity, randomness not controlled, or result genuinely differs. Assess whether gaps are remediable (documentation fix) or fundamental (design issue).

## Step 5 — Produce scorecard and recommendations (write)
Compile the reproducibility scorecard table with status and evidence for each criterion. Write the gap report narrative with root causes and recommendations. Assign the overall reproducibility tier. For cognitive-security use, explicitly note whether non-reproducible results should be treated as provisional and what additional evidence would be needed before treating them as reliable.

## Anti-criteria (must NOT happen)
- do not classify a result as reproducible without actually attempting execution — plausibility is not reproducibility
- do not treat unavailable data or code as 'acceptable' without explicitly flagging it as a non-assessable gap
- do not conflate replication (new data, same method) with direct reproduction (same data, same code) — they provide different epistemic assurance
- do not issue recommendations that merely ask authors to assert reproducibility without specifying what artifacts must be provided or what criteria must be met

## AGEINT upstream
`docs/ageint/adversarial-assurance.md`
