---
name: sat.causal_flow_diagramming
description: Trace cause-effect chains and feedback loops driving a system's behavior.
---

# Causal Flow Diagramming

Causal Flow Diagramming (also called causal loop diagramming or process mapping in intelligence analysis) traces the causal and feedback relationships among variables driving a system's behavior — showing which factors amplify (reinforcing loops) or dampen (balancing loops) each other and where interventions or disruptions would propagate. Adapted from systems dynamics (Forrester, Senge) and codified for intelligence analysis by Heuer & Pherson, it counters linear cause-and-effect thinking by surfacing non-obvious feedback paths, delays, and second-order effects that straight narrative obscures. In cognitive-security contexts it is used to map how disinformation, influence operations, or social dynamics self-amplify or self-correct.

## When to use

- A system shows persistent or recurring problematic behavior and linear cause-effect explanations have failed to account for it
- An analyst suspects feedback loops — where an effect amplifies or dampens its own cause — are driving the observed dynamics
- Decision-makers need to understand second-order consequences before intervening in a complex social, political, or information system
- An influence operation or disinformation campaign appears to be self-amplifying and the structural mechanisms of amplification need to be mapped
- Root cause analysis has identified contributing factors but their causal relationships remain unclear

## What it produces

- A visual causal map that makes feedback structures explicit and independently reviewable
- An inventory of reinforcing loops (engines of growth or collapse) and balancing loops (stabilizers or oscillators) with their behavioral signatures
- A set of identified leverage points — nodes where targeted intervention produces disproportionate system-wide effects
- An explicit record of delays and non-linear paths that linear narrative analysis would miss

## Defensive boundary

Use Causal Flow Diagramming only for structured analytic technique support: recognize, assess, document, or defend analytic rigor, alternative hypotheses, and calibrated judgment. Do not use this skill to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.

## Misuse redirect

If a request asks Causal Flow Diagramming to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation, refuse that path and redirect to the safe defensive form: apply the structured technique to supplied evidence while preserving alternatives and uncertainty.

## Evidence discipline

- For Causal Flow Diagramming, tie each causal flow diagram, loop inventory, and leverage point assessment claim to concrete evidence from the specific system description, known variables, and scope boundary item, source excerpt, observation, or command result that supports it.
- For Causal Flow Diagramming, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the causal flow diagram.
- Before recommending any Causal Flow Diagramming action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Causal Flow Diagramming: the causal flow diagram is supported by multiple independent hypotheses, assumptions, indicators, evidence tables, and confidence notes; define behavior-over-time and boundary and map causal links and polarities checks agree, and no unresolved contradiction would change the result.
- Medium for Causal Flow Diagramming: the causal flow diagram is plausible, but one important system description source, comparison case, or alternative explanation remains incomplete.
- Low for Causal Flow Diagramming: the causal flow diagram rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Causal Flow Diagramming cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Causal Flow Diagramming, use only authorized system description, known variables, and scope boundary, public or source-approved records, and caller-provided context needed for the defensive task.
- For Causal Flow Diagramming, minimize person-level detail in the causal flow diagram; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Causal Flow Diagramming, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Causal Flow Diagramming: treating system description as complete when define behavior-over-time and boundary and map causal links and polarities checks or contradictory evidence are missing.
- Causal Flow Diagramming: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Causal Flow Diagramming: reporting the causal flow diagram without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Causal Flow Diagramming outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the causal flow diagram from Causal Flow Diagramming into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Causal Flow Diagramming to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with system description, known variables, and scope boundary' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Polarity discipline: every causal arrow must be labeled + (same direction: A increases → B increases) or – (opposite direction: A increases → B decreases); ambiguous arrows are analytic gaps
- Loop typing is automatic from polarity: count the number of negative (–) links in a closed loop; even count = reinforcing (R), odd count = balancing (B)
- Delays are not decorative — a reinforcing loop with a long delay produces overshoot-and-collapse, not smooth growth; mark them explicitly
- Scope discipline: every variable in the diagram should be measurable in principle; avoid variables that are concepts rather than quantities (use 'perceived credibility of source X' not 'trust')
