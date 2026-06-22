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

## Defensive boundary

Use Disinformation Attribution only for counterintelligence and analytic-process defense: recognize, assess, document, or defend analytic teams, collection processes, and institutional trust boundaries. Do not use this skill to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft.

## Misuse redirect

If a request asks Disinformation Attribution to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft, refuse that path and redirect to the safe defensive form: review supplied interactions or processes for deception, elicitation, or insider-risk indicators.

## Evidence discipline

- For Disinformation Attribution, bind each finding to a labeled source — interaction records, process artifacts, deception indicators, and alternative explanations, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Disinformation Attribution, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Disinformation Attribution recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Disinformation Attribution: independent lines of interaction records, process artifacts, deception indicators, and alternative explanations converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Disinformation Attribution: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Disinformation Attribution: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Disinformation Attribution cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Disinformation Attribution should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Disinformation Attribution, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Disinformation Attribution, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Disinformation Attribution, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Disinformation Attribution failure: turning defensive tradecraft recognition into operational evasion advice.
- Disinformation Attribution failure: producing guidance that would help a requester evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft.
- Disinformation Attribution failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Disinformation Attribution to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Disinformation Attribution into an operational playbook to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Disinformation Attribution to review supplied interactions or processes for deception, elicitation, or insider-risk indicators' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- attribution is a probabilistic judgment, not a binary finding — express it as 'with HIGH confidence, consistent with Actor X, alternative Actor Y cannot be ruled out'
- false-flag operations are a real phenomenon; never eliminate an actor as candidate solely because the operation bears their stylistic markers
- diagnostic indicators are those that discriminate between hypotheses — indicators that all candidates would produce equally are noise, not signal; weight only discriminating evidence
