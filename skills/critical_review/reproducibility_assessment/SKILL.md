---
name: critical_review.reproducibility_assessment
description: Assess whether a result can be regenerated from the stated data, code, and seeds.
---

# Reproducibility Assessment

Reproducibility Assessment systematically checks whether a claimed result — computational, empirical, or analytical — can be regenerated from the stated data, code, seeds, and environment by an independent party following only the documented procedure. It distinguishes direct reproduction (same data, same code), replication (same procedure, new data), and conceptual replication (same hypothesis, different operationalization), and assesses the degree to which the artifact meets the requirements of each tier. In the cognitive-security domain, reproducibility is a foundational epistemic standard: assessments, threat models, and evidence bases that cannot be independently verified are vulnerable to manipulation and should not be used as sole justification for consequential decisions.

## When to use

- when evaluating a research claim, intelligence assessment, or analytical product before using it as a basis for decisions
- when accepting an external artifact into an evidence base that will support consequential conclusions
- when auditing a published result in the cognitive-security, AI, or social-science domain for epistemic reliability
- when a result has influenced policy or public belief and its provenance needs independent verification

## What it produces

- a reproducibility scorecard rating each key criterion (data availability, code availability, environment specification, seed/randomness control, result match) against the direct/replication/conceptual tiers
- a specific gap report identifying which claimed results could not be reproduced, why, and what would be needed to close each gap
- an overall reproducibility tier assessment (fully reproducible / partially reproducible / not reproducible / not assessable) with confidence
- a prioritized set of recommendations for the artifact authors to improve reproducibility

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- distinguish the three reproducibility tiers — direct reproduction, replication, and conceptual replication — and assess each separately; conflating them obscures what is actually verifiable
- treat an undocumented seed, environment, or preprocessing step as a gap even if the result seems plausible — undocumented steps cannot be independently verified and create attack surfaces for manipulation
- a result is not reproducible merely because the authors say it is — independent execution is required for direct reproduction
- missing data or code should be classified as 'not assessable' not 'reproducible' — an absence of counter-evidence is not evidence of reproducibility
