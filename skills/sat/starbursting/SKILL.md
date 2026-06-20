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

- For Starbursting, tie each question map, and key unknowns summary claim to concrete evidence from the specific topic or artifact, and context item, source excerpt, observation, or command result that supports it.
- For Starbursting, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the question map.
- Before recommending any Starbursting action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Starbursting: the question map is supported by multiple independent hypotheses, assumptions, indicators, evidence tables, and confidence notes; frame the topic and generate questions per interrogative checks agree, and no unresolved contradiction would change the result.
- Medium for Starbursting: the question map is plausible, but one important topic or artifact source, comparison case, or alternative explanation remains incomplete.
- Low for Starbursting: the question map rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Starbursting cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Starbursting, use only authorized topic or artifact, and context, public or source-approved records, and caller-provided context needed for the defensive task.
- For Starbursting, minimize person-level detail in the question map; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Starbursting, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Starbursting: treating topic or artifact as complete when frame the topic and generate questions per interrogative checks or contradictory evidence are missing.
- Starbursting: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Starbursting: reporting the question map without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Starbursting outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the question map from Starbursting into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Starbursting to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with topic or artifact, and context' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- generate questions before seeking any answers — answering prematurely closes down question generation
- each interrogative (Who/What/When/Where/Why/How) must produce multiple questions, not just one
- questions about absence are as important as questions about presence (e.g., 'Why is X NOT mentioned?')
