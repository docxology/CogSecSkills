---
name: critical_review.threat_model_review
description: Review a system's threat model for missing actors, surfaces, and assumptions.
---

# Threat Model Review

Threat Model Review systematically audits an existing threat model — such as a STRIDE, PASTA, attack tree, or narrative threat assessment — to identify missing actors, overlooked attack surfaces, unvalidated assumptions, and incomplete trust boundaries. The technique applies adversarial thinking to the threat model itself, asking whether it captures the realistic threat population, whether its mitigations are actually implemented, and whether its scope boundaries are justified or merely convenient. In cognitive-security contexts this extends to information-environment threat models: identifying omitted influence actors, uncovered cognitive attack surfaces, and assumptions about audience resilience that have not been empirically validated.

## When to use

- a threat model has not been reviewed since its initial creation and the system or threat environment has changed
- a security or cognitive-security assessment depends on an existing threat model that may have been authored under optimistic assumptions
- a red-team exercise has surfaced attack paths not present in the official threat model
- the threat model was authored by internal stakeholders with blind spots toward insider threats or sociotechnical surfaces
- an information-environment assessment needs to check whether all relevant influence actors and cognitive attack vectors are represented

## What it produces

- a gap table identifying missing actors, surfaces, trust-boundary errors, unvalidated assumptions, and mitigation gaps with severity ratings
- an assumption register distinguishing validated from unvalidated assumptions and flagging the highest-risk unvalidated ones
- a revised scope recommendation with rationale for expanding or recentering the model's boundaries
- a prioritized remediation list so owners can address critical gaps first

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- derive what the threat model should contain independently from the system description before reading the existing model — compare derived set to present set to surface omissions
- treat every scope exclusion as an implicit assumption; make those assumptions explicit and then evaluate whether they are warranted
- for each stated mitigation, ask whether it is actually implemented and testable — a paper mitigation is not a real control
- in cognitive-security threat models, explicitly audit for social-engineering and influence-operation surfaces, which are systematically underrepresented in technically-oriented models
