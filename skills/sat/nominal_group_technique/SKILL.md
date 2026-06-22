---
name: sat.nominal_group_technique
description: Silent independent ideation before discussion to counter dominance and groupthink.
---

# Nominal Group Technique

Nominal Group Technique (NGT) is a structured ideation and prioritization method in which participants independently generate ideas in writing before any group discussion, then share, clarify, and vote on items in a controlled sequence. By separating divergent from convergent phases and enforcing silent individual work first, NGT neutralizes vocal-dominance bias, anchoring, and groupthink that corrupt unstructured brainstorming. In cognitive-security contexts it is used to surface the full range of hypotheses or threat indicators a team holds without social-pressure distortion.

## When to use

- a team needs to surface all plausible hypotheses or threat indicators without vocal-dominance or anchoring effects
- prior unstructured sessions have been dominated by a senior analyst or first-speaker
- the group includes participants with status differences that suppress dissent
- you need a defensible, auditable record of how a prioritized list was constructed

## What it produces

- a ranked list of ideas or hypotheses weighted by collective, independently cast votes
- a transparent audit trail separating individual input from group aggregation
- a baseline for subsequent structured techniques (ACH, what-if, premortem)

## Defensive boundary

Use Nominal Group Technique only for structured analytic technique support: recognize, assess, document, or defend analytic rigor, alternative hypotheses, and calibrated judgment. Do not use this skill to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.

## Misuse redirect

If a request asks Nominal Group Technique to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation, refuse that path and redirect to the safe defensive form: apply the structured technique to supplied evidence while preserving alternatives and uncertainty.

## Evidence discipline

- For Nominal Group Technique, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Nominal Group Technique, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Nominal Group Technique recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Nominal Group Technique: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Nominal Group Technique: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Nominal Group Technique: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Nominal Group Technique cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Nominal Group Technique should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Nominal Group Technique, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Nominal Group Technique, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Nominal Group Technique, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Nominal Group Technique failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Nominal Group Technique failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Nominal Group Technique failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Nominal Group Technique to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Nominal Group Technique into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Nominal Group Technique to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- no discussion is allowed during the silent generation phase — verbal cues before votes anchor everyone to the first speaker
- ideas are listed and numbered without authorship attribution before voting begins
- each participant votes independently on a fixed budget of points; tally only after all votes are cast
