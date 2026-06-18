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

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Fitness-for-purpose is question-specific — a dataset adequate for one analytic question may be severely biased for another
- Absence of documentation is itself a finding; an undocumented dataset carries unknown risk that must be disclosed
- Transformation history matters: each filter, merge, or re-labeling step can introduce bias or lose information that was present in the original
- Licensing must be verified before analysis begins — using improperly licensed data can invalidate downstream findings and create legal liability
