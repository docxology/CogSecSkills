---
name: counterintelligence.indicators_of_deception_analysis
description: Apply the MOM/POP/MOSES/EVE deception-detection checklists to a body of evidence.
---

# Indicators of Deception Analysis

Indicators of Deception Analysis applies the structured MOM/POP/MOSES/EVE analytical framework to a body of evidence to assess whether an adversary may be conducting an active denial-and-deception (D&D) operation. MOM evaluates Motive, Opportunity, and Means; POP identifies Potential indicators of deception based on evidence anomalies; MOSES checks Manipulation, Omission, Selective emphasis, and Exaggeration patterns; and EVE applies Evidence, Validation, and Evaluation criteria. The combined framework converts an otherwise intuitive 'something seems off' judgment into a structured, documentable deception-hypothesis test.

## When to use

- When key intelligence or reporting contains anomalies that do not fit the established pattern or are too convenient for the adversary's narrative
- When a source with unusual access suddenly produces highly desirable, confirming intelligence
- When an adversary is known to have an active D&D program targeting your collection or decision-making
- Before finalizing a high-stakes assessment that depends heavily on a small number of critical sources
- When a previous assessment is later found to have been wrong in a direction that benefited an adversary

## What it produces

- A MOM checklist result: whether the adversary has motive, opportunity, and means to conduct deception targeting this intelligence
- A POP result: specific evidence anomalies that deviate from baseline expectations and could indicate manipulation
- A MOSES result: identification of patterns suggesting deliberate manipulation, omission, selective emphasis, or exaggeration
- An EVE result: assessment of whether available evidence supports or contradicts a deception hypothesis, with a confidence rating
- Recommended collection and analytic responses to test the deception hypothesis

## Defensive boundary

Use Indicators of Deception Analysis only for counterintelligence and analytic-process defense: recognize, assess, document, or defend analytic teams, collection processes, and institutional trust boundaries. Do not use this skill to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft.

## Misuse redirect

If a request asks Indicators of Deception Analysis to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft, refuse that path and redirect to the safe defensive form: review supplied interactions or processes for deception, elicitation, or insider-risk indicators.

## Evidence discipline

- For Indicators of Deception Analysis, tie each deception assessment report claim to concrete evidence from the specific evidence corpus, source profile, and baseline expectations item, source excerpt, observation, or command result that supports it.
- For Indicators of Deception Analysis, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the deception assessment report.
- Before recommending any Indicators of Deception Analysis action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Indicators of Deception Analysis: the deception assessment report is supported by multiple independent interaction records, process artifacts, deception indicators, and alternative explanations; establish baseline and ingest evidence and apply mom — motive, opportunity, means checks agree, and no unresolved contradiction would change the result.
- Medium for Indicators of Deception Analysis: the deception assessment report is plausible, but one important evidence corpus source, comparison case, or alternative explanation remains incomplete.
- Low for Indicators of Deception Analysis: the deception assessment report rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Indicators of Deception Analysis cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating counterintelligence evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Indicators of Deception Analysis, use only authorized evidence corpus, source profile, and baseline expectations, public or source-approved records, and caller-provided context needed for the defensive task.
- For Indicators of Deception Analysis, minimize person-level detail in the deception assessment report; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Indicators of Deception Analysis, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Indicators of Deception Analysis: treating evidence corpus as complete when establish baseline and ingest evidence and apply mom — motive, opportunity, means checks or contradictory evidence are missing.
- Indicators of Deception Analysis: producing advice that would help a requester evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft.
- Indicators of Deception Analysis: reporting the deception assessment report without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Indicators of Deception Analysis outputs to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the deception assessment report from Indicators of Deception Analysis into an operational playbook to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Indicators of Deception Analysis to review supplied interactions or processes for deception, elicitation, or insider-risk indicators with evidence corpus, source profile, and baseline expectations' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Apply each checklist component in sequence before synthesizing — premature synthesis anchors on the first plausible interpretation
- Absence of deception indicators is not confirmation of accuracy — sophisticated deception is designed to pass these checks
- A deception hypothesis requires a proposed adversary mechanism, not just anomalies; anomalies alone do not prove deception
- Document null findings per component as explicitly as positive findings — the record protects against post-hoc rationalization
