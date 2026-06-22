---
name: osint_integrity.dataset_provenance_audit
description: Audit a dataset's origin, licensing, sampling, and integrity before analytic use.
---

# Dataset Provenance Audit

Dataset provenance audit systematically examines a dataset's origin, collection methodology, licensing terms, sampling frame, and integrity before it is used as an analytic input. Datasets used in OSINT and cognitive-security analysis are often scraped, crowd-sourced, or re-packaged — making undisclosed biases, legal encumbrances, and integrity failures common failure modes. The audit surfaces whether the dataset accurately represents what it claims to represent, whether the analyst has legal right to use it, and whether any transformations between origin and current form may have introduced errors or distortions. It is the due-diligence gate before any dataset is trusted in an analytic product.

## When to use

- Before using any externally sourced dataset in an analytic product, especially one that will inform decisions
- When a dataset's origin, methodology, or licensing is unclear or undocumented
- When the dataset has been transformed, aggregated, or re-packaged from its original form
- When the analytic question requires a representative sample of a population and sampling bias would materially affect conclusions

## What it produces

- A documented audit trail showing what is known and unknown about the dataset's origin and transformation history
- A fitness-for-purpose assessment tied to the specific analytic question, not a generic quality rating
- Explicit limitation disclosures that must accompany any product using the dataset

## Defensive boundary

Use Dataset Provenance Audit only for OSINT integrity and source-verification defense: recognize, assess, document, or defend source provenance, privacy, chain of custody, and public-source accountability. Do not use this skill to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.

## Misuse redirect

If a request asks Dataset Provenance Audit to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence, refuse that path and redirect to the safe defensive form: verify supplied claims, media, sources, or datasets with documented public-source methods.

## Evidence discipline

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

## Failure modes and negative controls

- Dataset Provenance Audit failure: overstating identity, location, attribution, or source reliability from incomplete public traces.
- Dataset Provenance Audit failure: producing guidance that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Dataset Provenance Audit failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Dataset Provenance Audit to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Dataset Provenance Audit into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Dataset Provenance Audit to verify supplied claims, media, sources, or datasets with documented public-source methods' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Fitness-for-purpose is question-specific — a dataset adequate for one analytic question may be severely biased for another
- Absence of documentation is itself a finding; an undocumented dataset carries unknown risk that must be disclosed
- Transformation history matters: each filter, merge, or re-labeling step can introduce bias or lose information that was present in the original
- Licensing must be verified before analysis begins — using improperly licensed data can invalidate downstream findings and create legal liability
