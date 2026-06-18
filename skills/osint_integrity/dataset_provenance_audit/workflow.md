# Workflow — Dataset Provenance Audit

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Establish origin and licensing (read, search)
Identify the primary source of the dataset — who collected it, when, using what method. Locate the license or terms of use. Search for the original publication or methodology document. Flag if origin cannot be established or if the chain from original collection to current form has undocumented steps.

## Step 2 — Run integrity and sampling checks (exec, reason)
Compute a hash of the current dataset and compare to any published hash. Validate schema conformance, check for duplicates, and assess completeness. Examine the sampling frame: what population does the dataset claim to represent, and what is actually included? Identify coverage gaps, temporal biases, geographic biases, or platform-specific selection effects.

## Step 3 — Assess transformation history and fitness for purpose (reason)
Reconstruct the transformation chain from original collection to the dataset in hand. For each transformation (filtering, aggregation, re-labeling, merging), assess whether it could introduce bias or information loss relevant to the analytic question. Rate fitness-for-purpose: directly fit, fit with disclosed limitations, or unfit for this question.

## Step 4 — Produce the audit report and use recommendation (write)
Write the structured provenance audit report covering all findings. State the use/no-use recommendation with specific conditions: if usable, list the limitation disclosures that must accompany any product; if not usable, state what would make it acceptable or what alternative sources should be sought.

## Anti-criteria (must NOT happen)
- Do not use a dataset in an analytic product without completing the provenance audit and documenting its limitations
- Do not treat a large dataset as automatically representative — size does not correct for sampling bias
- Do not assume that because a dataset has been used by others it has been properly vetted; audit independently for each analytic question

## AGEINT upstream
`docs/ageint/osint-integrity.md`
