---
name: information_environment.platform_affordance_risk_assessment
description: Assess how a platform's features enable or constrain manipulation.
---

# Platform Affordance Risk Assessment

Platform Affordance Risk Assessment systematically evaluates how a specific platform's technical features, algorithmic systems, and policy architecture enable or constrain information manipulation. Rooted in affordance theory (Gibson; Norman) and applied to sociotechnical systems, it maps each platform feature—virality mechanics, recommendation algorithms, group/channel structures, anonymity policies, ad targeting—to the manipulation vectors those features enable. The output equips analysts, platform trust-and-safety teams, and policymakers to prioritize design mitigations and anticipate where influence operations will exploit platform architecture.

## When to use

- before deploying a monitoring program on a new platform to understand where adversarial actors will have structural advantages
- when advising a platform's trust-and-safety team on design changes that could reduce manipulation surface
- when explaining why a specific influence operation succeeded on a given platform
- when comparing platforms to select the least-risky channel for a sensitive communication

## What it produces

- an affordance-to-manipulation-vector mapping that reveals which features are most exploitable
- a prioritized risk matrix with severity ratings grounded in real incident precedents
- identification of cross-feature interaction effects that amplify risk beyond what any single feature would imply
- a set of mitigation recommendations tied to specific platform design choices or policy changes

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- assess affordances as dual-use — the same feature that enables legitimate behavior enables manipulation; the question is asymmetry of benefit
- evaluate cross-feature interaction effects explicitly — recommendation algorithms plus pseudonymity plus virality produce non-additive risk
- ground severity ratings in real precedent — documented abuse incidents prevent hypothetical risk inflation
- distinguish platform design risk from policy enforcement failure — both matter but require different mitigations
