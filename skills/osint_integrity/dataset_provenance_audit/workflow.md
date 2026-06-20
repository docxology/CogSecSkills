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

## Evidence requirements
- For Dataset Provenance Audit, tie each provenance audit report, and integrity check results claim to concrete evidence from the specific dataset, analytic question, and dataset documentation item, source excerpt, observation, or command result that supports it.
- For Dataset Provenance Audit, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the provenance audit report.
- Before recommending any Dataset Provenance Audit action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Dataset Provenance Audit: the provenance audit report is supported by multiple independent source records, custody notes, metadata, corroborating references, and contradiction logs; establish origin and licensing and run integrity and sampling checks checks agree, and no unresolved contradiction would change the result.
- Medium for Dataset Provenance Audit: the provenance audit report is plausible, but one important dataset source, comparison case, or alternative explanation remains incomplete.
- Low for Dataset Provenance Audit: the provenance audit report rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Dataset Provenance Audit cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating osint_integrity evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Dataset Provenance Audit, use only authorized dataset, analytic question, and dataset documentation, public or source-approved records, and caller-provided context needed for the defensive task.
- For Dataset Provenance Audit, minimize person-level detail in the provenance audit report; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Dataset Provenance Audit, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Dataset Provenance Audit: treating dataset as complete when establish origin and licensing and run integrity and sampling checks checks or contradictory evidence are missing.
- Dataset Provenance Audit: producing advice that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Dataset Provenance Audit: reporting the provenance audit report without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Dataset Provenance Audit outputs to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the provenance audit report from Dataset Provenance Audit into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Dataset Provenance Audit to verify supplied claims, media, sources, or datasets with documented public-source methods with dataset, analytic question, and dataset documentation' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not use a dataset in an analytic product without completing the provenance audit and documenting its limitations
- Do not treat a large dataset as automatically representative — size does not correct for sampling bias
- Do not assume that because a dataset has been used by others it has been properly vetted; audit independently for each analytic question

## AGEINT upstream
`docs/ageint/osint-integrity.md`
