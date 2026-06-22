---
name: sat.structured_self_critique
description: Apply a checklist of challenge questions to one's own analysis before release.
---

# Structured Self-Critique

Structured Self-Critique applies a systematic checklist of challenge questions to an analyst's own completed assessment before it is released, surfacing hidden assumptions, unsupported leaps, alternative explanations, and gaps in evidence. Developed within the structured analytic techniques tradition (Heuer & Pherson), it serves as a final-stage quality-control discipline that counteracts confirmation bias, mindset, and overconfidence. By externalizing the critique as a formal process rather than relying on an analyst's informal self-review, it reduces the probability that cognitive biases survive into finished intelligence or decision-support products.

## When to use

- an analytic product is near-final and is about to be disseminated to decision-makers
- the analyst suspects she may have relied on a single dominant hypothesis without adequately testing alternatives
- the evidence base is thin or derived from a narrow set of sources that could share common distortions
- a previous assessment on the same topic has proven wrong and the revision needs explicit bias-control
- the stakes of an incorrect judgment are high enough to warrant a formal quality gate

## What it produces

- a checklist-driven annotation of the analysis identifying which judgments rest on assumption rather than evidence
- enumerated alternative explanations that were not adequately considered
- explicit confidence calibration notes flagging where certainty language exceeds the evidence
- a prioritized list of revisions needed before the product is safe to release

## Defensive boundary

Use Structured Self-Critique only for structured analytic technique support: recognize, assess, document, or defend analytic rigor, alternative hypotheses, and calibrated judgment. Do not use this skill to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.

## Misuse redirect

If a request asks Structured Self-Critique to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation, refuse that path and redirect to the safe defensive form: apply the structured technique to supplied evidence while preserving alternatives and uncertainty.

## Evidence discipline

- For Structured Self-Critique, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Structured Self-Critique, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Structured Self-Critique recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Structured Self-Critique: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Structured Self-Critique: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Structured Self-Critique: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Structured Self-Critique cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Structured Self-Critique should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Structured Self-Critique, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Structured Self-Critique, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Structured Self-Critique, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Structured Self-Critique failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Structured Self-Critique failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Structured Self-Critique failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Structured Self-Critique to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Structured Self-Critique into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Structured Self-Critique to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- treat each challenge question as a mandatory gate, not an optional reflection — every question must receive an explicit answer
- separate the two roles: the analyst who wrote the draft and the critic who challenges it must reason from different starting frames, even if they are the same person
- alternative explanations must be genuinely considered — not invented and immediately dismissed
- confidence language ('likely', 'almost certainly') must be anchored to an explicit probability range before the product is cleared
