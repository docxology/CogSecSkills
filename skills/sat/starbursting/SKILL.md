---
name: sat.starbursting
description: Generate questions (who/what/when/where/why/how) before answers to map the unknowns.
---

# Starbursting

Starbursting is a structured brainstorming technique that generates questions—organized by the six interrogatives Who, What, When, Where, Why, and How—before attempting to answer them. By systematically exhausting the question space first, it prevents analysts from leaping to premature conclusions, surfaces unknown unknowns, and identifies which gaps in knowledge are most consequential. In cognitive-security settings it is particularly useful for mapping the full attack surface of an influence operation or information environment before committing analytical resources.

## When to use

- a new topic, actor, or operation is being scoped and analysts may not yet know what they do not know
- premature closure on an answer is suspected and rigorous question generation is needed to reopen the problem
- planning collection requirements or research tasks where an exhaustive question list drives prioritization
- evaluating an influence narrative to identify which aspects have not been interrogated

## What it produces

- a comprehensive question map across all six interrogatives, making unknown unknowns explicit
- a prioritized list of the most consequential unanswered questions
- a basis for collection requirements, research tasks, or further structured analysis

## Defensive boundary

Use Starbursting only for structured analytic technique support: recognize, assess, document, or defend analytic rigor, alternative hypotheses, and calibrated judgment. Do not use this skill to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.

## Misuse redirect

If a request asks Starbursting to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation, refuse that path and redirect to the safe defensive form: apply the structured technique to supplied evidence while preserving alternatives and uncertainty.

## Evidence discipline

- For Starbursting, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Starbursting, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Starbursting recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Starbursting: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Starbursting: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Starbursting: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Starbursting cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Starbursting should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Starbursting, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Starbursting, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Starbursting, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Starbursting failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Starbursting failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Starbursting failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Starbursting to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Starbursting into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Starbursting to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- generate questions before seeking any answers — answering prematurely closes down question generation
- each interrogative (Who/What/When/Where/Why/How) must produce multiple questions, not just one
- questions about absence are as important as questions about presence (e.g., 'Why is X NOT mentioned?')
