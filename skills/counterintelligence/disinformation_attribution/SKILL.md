---
name: counterintelligence.disinformation_attribution
description: Reason about attribution of an operation with calibrated confidence and alternatives.
---

# Disinformation Attribution

Disinformation attribution applies structured analytic reasoning to assign responsibility for an influence operation or disinformation campaign with calibrated confidence, while explicitly holding alternative attribution hypotheses. Unlike technical cyber attribution, disinformation attribution must integrate behavioral, linguistic, technical, and strategic indicators against a baseline of known actor profiles. The technique borrows from both intelligence analysis tradecraft (ACH, confidence calibration) and open-source investigation methodology (Bellingcat, EU DisinfoLab) to produce an attribution judgment that is auditable, challengeable, and honest about its limits.

## When to use

- a disinformation campaign or influence operation requires accountability and an actionable attribution judgment
- a policy response (counter-messaging, platform enforcement, diplomatic demarche) depends on knowing who is responsible
- multiple candidate actors are plausible and an unstructured 'best guess' would reflect only the most salient hypothesis rather than weighing all evidence
- a prior attribution claim needs to be audited for analytical rigor and hidden assumptions

## What it produces

- a structured ACH-style matrix showing how each indicator bears on each candidate actor
- a calibrated lead-attribution hypothesis with explicit confidence level, key assumptions, and named alternatives
- a prioritized collection gap list specifying what new evidence would most sharpen or overturn the assessment

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- attribution is a probabilistic judgment, not a binary finding — express it as 'with HIGH confidence, consistent with Actor X, alternative Actor Y cannot be ruled out'
- false-flag operations are a real phenomenon; never eliminate an actor as candidate solely because the operation bears their stylistic markers
- diagnostic indicators are those that discriminate between hypotheses — indicators that all candidates would produce equally are noise, not signal; weight only discriminating evidence
