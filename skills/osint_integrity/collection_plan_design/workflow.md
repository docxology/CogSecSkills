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
- For Collection Plan Design, bind each finding to a labeled source — source records, custody notes, metadata, corroborating references, and contradiction logs, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Collection Plan Design, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Collection Plan Design recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Collection Plan Design: independent lines of source records, custody notes, metadata, corroborating references, and contradiction logs converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Collection Plan Design: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Collection Plan Design: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Collection Plan Design cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Collection Plan Design should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Collection Plan Design, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Collection Plan Design, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Collection Plan Design, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Collection Plan Design failure: overstating identity, location, attribution, or source reliability from incomplete public traces.
- Collection Plan Design failure: producing guidance that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Collection Plan Design failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Collection Plan Design to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Collection Plan Design into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Collection Plan Design to verify supplied claims, media, sources, or datasets with documented public-source methods' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not begin collection before legal basis and scope are documented and approved
- Do not include sources in the plan simply because they are accessible — include only those that can plausibly answer the stated requirement
- Do not treat the collection plan as static — it must be updated if the analytic question or legal environment changes mid-effort

## AGEINT upstream
`docs/ageint/osint-integrity.md`
