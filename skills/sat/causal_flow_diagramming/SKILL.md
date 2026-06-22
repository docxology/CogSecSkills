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

- For Causal Flow Diagramming, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Causal Flow Diagramming, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Causal Flow Diagramming recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Causal Flow Diagramming: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Causal Flow Diagramming: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Causal Flow Diagramming: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Causal Flow Diagramming cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Causal Flow Diagramming should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Causal Flow Diagramming, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Causal Flow Diagramming, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Causal Flow Diagramming, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Causal Flow Diagramming failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Causal Flow Diagramming failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Causal Flow Diagramming failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Causal Flow Diagramming to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Causal Flow Diagramming into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Causal Flow Diagramming to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Polarity discipline: every causal arrow must be labeled + (same direction: A increases → B increases) or – (opposite direction: A increases → B decreases); ambiguous arrows are analytic gaps
- Loop typing is automatic from polarity: count the number of negative (–) links in a closed loop; even count = reinforcing (R), odd count = balancing (B)
- Delays are not decorative — a reinforcing loop with a long delay produces overshoot-and-collapse, not smooth growth; mark them explicitly
- Scope discipline: every variable in the diagram should be measurable in principle; avoid variables that are concepts rather than quantities (use 'perceived credibility of source X' not 'trust')
