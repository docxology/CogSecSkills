# Workflow — Collection Plan Design

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Clarify the intelligence requirement (read, ask)
Read the tasking or analytic question. Ask the tasking authority to resolve ambiguities about what decision will be made with the intelligence, what level of confidence is required, and what the deadline is. Confirm authorization for the collection.

## Step 2 — Derive scope, sources, and ethical boundaries (reason)
Map the requirement to information types and candidate open sources. Assess each source against legal constraints, terms-of-service obligations, and proportionality. Exclude sources where collection would be disproportionate, legally ambiguous, or outside the analytic requirement. Identify the legal basis for each included source.

## Step 3 — Design collection methods and data handling rules (reason, write)
For each in-scope source, specify the collection method (manual review, automated scraping, API, archive query), storage location, access controls, retention period, and deletion trigger. Define who may access the data and under what conditions.

## Step 4 — Draft the plan and source priority matrix (write)
Produce the written collection plan document and the source priority table. Obtain approval from the tasking authority and legal or compliance review before collection begins. Record the approval in the plan.

## Anti-criteria (must NOT happen)
- Do not begin collection before legal basis and scope are documented and approved
- Do not include sources in the plan simply because they are accessible — include only those that can plausibly answer the stated requirement
- Do not treat the collection plan as static — it must be updated if the analytic question or legal environment changes mid-effort

## AGEINT upstream
`docs/ageint/osint-integrity.md`
