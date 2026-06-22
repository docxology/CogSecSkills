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
- For Dataset Provenance Audit, bind each finding to a labeled source — source records, custody notes, metadata, corroborating references, and contradiction logs, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Dataset Provenance Audit, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Dataset Provenance Audit recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Dataset Provenance Audit: independent lines of source records, custody notes, metadata, corroborating references, and contradiction logs converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Dataset Provenance Audit: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Dataset Provenance Audit: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Dataset Provenance Audit cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Dataset Provenance Audit should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Dataset Provenance Audit, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Dataset Provenance Audit, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Dataset Provenance Audit, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Dataset Provenance Audit failure: overstating identity, location, attribution, or source reliability from incomplete public traces.
- Dataset Provenance Audit failure: producing guidance that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Dataset Provenance Audit failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Dataset Provenance Audit to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Dataset Provenance Audit into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Dataset Provenance Audit to verify supplied claims, media, sources, or datasets with documented public-source methods' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not use a dataset in an analytic product without completing the provenance audit and documenting its limitations
- Do not treat a large dataset as automatically representative — size does not correct for sampling bias
- Do not assume that because a dataset has been used by others it has been properly vetted; audit independently for each analytic question

## AGEINT upstream
`docs/ageint/osint-integrity.md`
