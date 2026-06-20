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

## Failure modes and negative controls

- Dataset Provenance Audit: treating dataset as complete when establish origin and licensing and run integrity and sampling checks checks or contradictory evidence are missing.
- Dataset Provenance Audit: producing advice that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Dataset Provenance Audit: reporting the provenance audit report without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Dataset Provenance Audit outputs to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the provenance audit report from Dataset Provenance Audit into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Dataset Provenance Audit to verify supplied claims, media, sources, or datasets with documented public-source methods with dataset, analytic question, and dataset documentation' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Fitness-for-purpose is question-specific — a dataset adequate for one analytic question may be severely biased for another
- Absence of documentation is itself a finding; an undocumented dataset carries unknown risk that must be disclosed
- Transformation history matters: each filter, merge, or re-labeling step can introduce bias or lose information that was present in the original
- Licensing must be verified before analysis begins — using improperly licensed data can invalidate downstream findings and create legal liability
