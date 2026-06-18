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

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Polarity discipline: every causal arrow must be labeled + (same direction: A increases → B increases) or – (opposite direction: A increases → B decreases); ambiguous arrows are analytic gaps
- Loop typing is automatic from polarity: count the number of negative (–) links in a closed loop; even count = reinforcing (R), odd count = balancing (B)
- Delays are not decorative — a reinforcing loop with a long delay produces overshoot-and-collapse, not smooth growth; mark them explicitly
- Scope discipline: every variable in the diagram should be measurable in principle; avoid variables that are concepts rather than quantities (use 'perceived credibility of source X' not 'trust')
