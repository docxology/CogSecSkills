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

## Defensive boundary

Use Platform Affordance Risk Assessment only for information-environment monitoring and platform-risk defense: recognize, assess, document, or defend platform integrity, narrative context, and authentic community behavior. Do not use this skill to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement.

## Misuse redirect

If a request asks Platform Affordance Risk Assessment to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement, refuse that path and redirect to the safe defensive form: map supplied narratives, automation signals, or platform affordance risks for defensive review.

## Evidence discipline

- For Platform Affordance Risk Assessment, tie each affordance risk matrix, and risk narrative claim to concrete evidence from the specific platform name, threat actor profile, and prior incident reports item, source excerpt, observation, or command result that supports it.
- For Platform Affordance Risk Assessment, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the affordance risk matrix.
- Before recommending any Platform Affordance Risk Assessment action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Platform Affordance Risk Assessment: the affordance risk matrix is supported by multiple independent platform observations, narrative movement, automation signals, and provenance data; inventory platform features and map features to manipulation vectors checks agree, and no unresolved contradiction would change the result.
- Medium for Platform Affordance Risk Assessment: the affordance risk matrix is plausible, but one important platform name source, comparison case, or alternative explanation remains incomplete.
- Low for Platform Affordance Risk Assessment: the affordance risk matrix rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Platform Affordance Risk Assessment cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating information_environment evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Platform Affordance Risk Assessment, use only authorized platform name, threat actor profile, and prior incident reports, public or source-approved records, and caller-provided context needed for the defensive task.
- For Platform Affordance Risk Assessment, minimize person-level detail in the affordance risk matrix; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Platform Affordance Risk Assessment, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Platform Affordance Risk Assessment: treating platform name as complete when inventory platform features and map features to manipulation vectors checks or contradictory evidence are missing.
- Platform Affordance Risk Assessment: producing advice that would help a requester amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement.
- Platform Affordance Risk Assessment: reporting the affordance risk matrix without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Platform Affordance Risk Assessment outputs to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the affordance risk matrix from Platform Affordance Risk Assessment into an operational playbook to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Platform Affordance Risk Assessment to map supplied narratives, automation signals, or platform affordance risks for defensive review with platform name, threat actor profile, and prior incident reports' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- assess affordances as dual-use — the same feature that enables legitimate behavior enables manipulation; the question is asymmetry of benefit
- evaluate cross-feature interaction effects explicitly — recommendation algorithms plus pseudonymity plus virality produce non-additive risk
- ground severity ratings in real precedent — documented abuse incidents prevent hypothetical risk inflation
- distinguish platform design risk from policy enforcement failure — both matter but require different mitigations
