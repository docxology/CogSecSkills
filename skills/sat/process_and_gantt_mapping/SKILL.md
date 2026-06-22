---
name: sat.process_and_gantt_mapping
description: Lay out a process or adversary plan as sequenced, dependency-aware steps.
---

# Process & Gantt Mapping

Process and Gantt Mapping is a structured analytic technique that decomposes a complex activity — an adversary plan, a supply chain, a disinformation campaign, or an operational sequence — into discrete, dependency-ordered steps laid out on a timeline. The visual sequence reveals critical path nodes, prerequisite chains, observable tripwires, and resource-intensive choke points that prose analysis obscures. In cognitive-security work it is used to model how an influence operation, deception campaign, or hostile cognitive attack is likely structured so that indicators can be assigned to specific nodes and disruption points identified.

## When to use

- analyzing an adversary operational plan where timing, sequencing, and dependencies are analytically significant
- modeling a disinformation or influence campaign lifecycle to identify observable stages and disruption opportunities
- assessing whether a detected indicator belongs to an early or late phase of a suspected activity sequence
- communicating complex multi-step adversary activity to decision-makers or non-specialist audiences

## What it produces

- a sequenced, dependency-ordered decomposition of the activity with observable indicators at each node
- identification of critical-path nodes where delay or disruption would maximally affect the whole sequence
- choke points — resource-intensive or irreversible steps that, if detected, confirm significant commitment by the adversary
- a timeline that can be overlaid with collected intelligence to assess phase and remaining lead time

## Defensive boundary

Use Process & Gantt Mapping only for structured analytic technique support: recognize, assess, document, or defend analytic rigor, alternative hypotheses, and calibrated judgment. Do not use this skill to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.

## Misuse redirect

If a request asks Process & Gantt Mapping to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation, refuse that path and redirect to the safe defensive form: apply the structured technique to supplied evidence while preserving alternatives and uncertainty.

## Evidence discipline

- For Process & Gantt Mapping, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Process & Gantt Mapping, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Process & Gantt Mapping recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Process & Gantt Mapping: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Process & Gantt Mapping: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Process & Gantt Mapping: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Process & Gantt Mapping cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Process & Gantt Mapping should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Process & Gantt Mapping, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Process & Gantt Mapping, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Process & Gantt Mapping, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Process & Gantt Mapping failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Process & Gantt Mapping failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Process & Gantt Mapping failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Process & Gantt Mapping to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Process & Gantt Mapping into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Process & Gantt Mapping to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- map what is required by the activity's logic, not only what has been observed — gaps in the map are collection requirements
- distinguish irreversible steps (choke points that confirm commitment) from reversible preparatory steps
- every step must have at least one observable indicator — steps with no indicator are collection gaps, not confirmed blanks
