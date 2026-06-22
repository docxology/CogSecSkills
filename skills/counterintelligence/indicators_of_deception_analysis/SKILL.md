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

- For Indicators of Deception Analysis, bind each finding to a labeled source — interaction records, process artifacts, deception indicators, and alternative explanations, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Indicators of Deception Analysis, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Indicators of Deception Analysis recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Indicators of Deception Analysis: independent lines of interaction records, process artifacts, deception indicators, and alternative explanations converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Indicators of Deception Analysis: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Indicators of Deception Analysis: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Indicators of Deception Analysis cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Indicators of Deception Analysis should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Indicators of Deception Analysis, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Indicators of Deception Analysis, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Indicators of Deception Analysis, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Indicators of Deception Analysis failure: turning defensive tradecraft recognition into operational evasion advice.
- Indicators of Deception Analysis failure: producing guidance that would help a requester evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft.
- Indicators of Deception Analysis failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Indicators of Deception Analysis to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Indicators of Deception Analysis into an operational playbook to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Indicators of Deception Analysis to review supplied interactions or processes for deception, elicitation, or insider-risk indicators' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Apply each checklist component in sequence before synthesizing — premature synthesis anchors on the first plausible interpretation
- Absence of deception indicators is not confirmation of accuracy — sophisticated deception is designed to pass these checks
- A deception hypothesis requires a proposed adversary mechanism, not just anomalies; anomalies alone do not prove deception
- Document null findings per component as explicitly as positive findings — the record protects against post-hoc rationalization
