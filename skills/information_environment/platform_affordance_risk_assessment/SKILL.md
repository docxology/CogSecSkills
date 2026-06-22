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

- For Platform Affordance Risk Assessment, bind each finding to a labeled source — platform observations, narrative movement, automation signals, and provenance data, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Platform Affordance Risk Assessment, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Platform Affordance Risk Assessment recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Platform Affordance Risk Assessment: independent lines of platform observations, narrative movement, automation signals, and provenance data converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Platform Affordance Risk Assessment: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Platform Affordance Risk Assessment: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Platform Affordance Risk Assessment cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Platform Affordance Risk Assessment should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Platform Affordance Risk Assessment, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Platform Affordance Risk Assessment, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Platform Affordance Risk Assessment, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Platform Affordance Risk Assessment failure: treating engagement volume as proof of authenticity or coordinated intent.
- Platform Affordance Risk Assessment failure: producing guidance that would help a requester amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement.
- Platform Affordance Risk Assessment failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Platform Affordance Risk Assessment to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Platform Affordance Risk Assessment into an operational playbook to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Platform Affordance Risk Assessment to map supplied narratives, automation signals, or platform affordance risks for defensive review' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- assess affordances as dual-use — the same feature that enables legitimate behavior enables manipulation; the question is asymmetry of benefit
- evaluate cross-feature interaction effects explicitly — recommendation algorithms plus pseudonymity plus virality produce non-additive risk
- ground severity ratings in real precedent — documented abuse incidents prevent hypothetical risk inflation
- distinguish platform design risk from policy enforcement failure — both matter but require different mitigations
