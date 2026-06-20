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

- For Disinformation Attribution, tie each attribution matrix, attribution assessment, and intelligence gaps claim to concrete evidence from the specific campaign artifacts, candidate actors, and strategic context item, source excerpt, observation, or command result that supports it.
- For Disinformation Attribution, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the attribution matrix.
- Before recommending any Disinformation Attribution action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Disinformation Attribution: the attribution matrix is supported by multiple independent interaction records, process artifacts, deception indicators, and alternative explanations; inventory the evidence and candidate actors and identify diagnostic indicators checks agree, and no unresolved contradiction would change the result.
- Medium for Disinformation Attribution: the attribution matrix is plausible, but one important campaign artifacts source, comparison case, or alternative explanation remains incomplete.
- Low for Disinformation Attribution: the attribution matrix rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Disinformation Attribution cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating counterintelligence evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Disinformation Attribution, use only authorized campaign artifacts, candidate actors, and strategic context, public or source-approved records, and caller-provided context needed for the defensive task.
- For Disinformation Attribution, minimize person-level detail in the attribution matrix; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Disinformation Attribution, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Disinformation Attribution: treating campaign artifacts as complete when inventory the evidence and candidate actors and identify diagnostic indicators checks or contradictory evidence are missing.
- Disinformation Attribution: producing advice that would help a requester evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft.
- Disinformation Attribution: reporting the attribution matrix without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Disinformation Attribution outputs to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the attribution matrix from Disinformation Attribution into an operational playbook to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Disinformation Attribution to review supplied interactions or processes for deception, elicitation, or insider-risk indicators with campaign artifacts, candidate actors, and strategic context' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- attribution is a probabilistic judgment, not a binary finding — express it as 'with HIGH confidence, consistent with Actor X, alternative Actor Y cannot be ruled out'
- false-flag operations are a real phenomenon; never eliminate an actor as candidate solely because the operation bears their stylistic markers
- diagnostic indicators are those that discriminate between hypotheses — indicators that all candidates would produce equally are noise, not signal; weight only discriminating evidence
