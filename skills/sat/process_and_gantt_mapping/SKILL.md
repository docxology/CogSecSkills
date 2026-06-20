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

- For Process & Gantt Mapping, tie each process map, and gantt table claim to concrete evidence from the specific activity description, known steps, and time constraints item, source excerpt, observation, or command result that supports it.
- For Process & Gantt Mapping, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the process map.
- Before recommending any Process & Gantt Mapping action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Process & Gantt Mapping: the process map is supported by multiple independent hypotheses, assumptions, indicators, evidence tables, and confidence notes; characterize and scope the activity and decompose into ordered steps checks agree, and no unresolved contradiction would change the result.
- Medium for Process & Gantt Mapping: the process map is plausible, but one important activity description source, comparison case, or alternative explanation remains incomplete.
- Low for Process & Gantt Mapping: the process map rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Process & Gantt Mapping cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Process & Gantt Mapping, use only authorized activity description, known steps, and time constraints, public or source-approved records, and caller-provided context needed for the defensive task.
- For Process & Gantt Mapping, minimize person-level detail in the process map; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Process & Gantt Mapping, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Process & Gantt Mapping: treating activity description as complete when characterize and scope the activity and decompose into ordered steps checks or contradictory evidence are missing.
- Process & Gantt Mapping: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Process & Gantt Mapping: reporting the process map without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Process & Gantt Mapping outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the process map from Process & Gantt Mapping into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Process & Gantt Mapping to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with activity description, known steps, and time constraints' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- map what is required by the activity's logic, not only what has been observed — gaps in the map are collection requirements
- distinguish irreversible steps (choke points that confirm commitment) from reversible preparatory steps
- every step must have at least one observable indicator — steps with no indicator are collection gaps, not confirmed blanks
