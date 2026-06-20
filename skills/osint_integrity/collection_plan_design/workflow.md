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

## Evidence requirements
- For Collection Plan Design, tie each collection plan, and source priority matrix claim to concrete evidence from the specific intelligence requirement, legal and policy constraints, and available resources item, source excerpt, observation, or command result that supports it.
- For Collection Plan Design, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the collection plan.
- Before recommending any Collection Plan Design action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Collection Plan Design: the collection plan is supported by multiple independent source records, custody notes, metadata, corroborating references, and contradiction logs; clarify the intelligence requirement and derive scope, sources, and ethical boundaries checks agree, and no unresolved contradiction would change the result.
- Medium for Collection Plan Design: the collection plan is plausible, but one important intelligence requirement source, comparison case, or alternative explanation remains incomplete.
- Low for Collection Plan Design: the collection plan rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Collection Plan Design cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating osint_integrity evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Collection Plan Design, use only authorized intelligence requirement, legal and policy constraints, and available resources, public or source-approved records, and caller-provided context needed for the defensive task.
- For Collection Plan Design, minimize person-level detail in the collection plan; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Collection Plan Design, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Collection Plan Design: treating intelligence requirement as complete when clarify the intelligence requirement and derive scope, sources, and ethical boundaries checks or contradictory evidence are missing.
- Collection Plan Design: producing advice that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Collection Plan Design: reporting the collection plan without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Collection Plan Design outputs to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the collection plan from Collection Plan Design into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Collection Plan Design to verify supplied claims, media, sources, or datasets with documented public-source methods with intelligence requirement, legal and policy constraints, and available resources' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not begin collection before legal basis and scope are documented and approved
- Do not include sources in the plan simply because they are accessible — include only those that can plausibly answer the stated requirement
- Do not treat the collection plan as static — it must be updated if the analytic question or legal environment changes mid-effort

## AGEINT upstream
`docs/ageint/osint-integrity.md`
