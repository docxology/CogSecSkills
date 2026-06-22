---
name: information_environment.coordinated_inauthentic_behavior_detection
description: Detect coordination signatures across accounts, timing, and content reuse.
---

# Coordinated Inauthentic Behavior Detection

Coordinated Inauthentic Behavior (CIB) detection identifies groups of accounts that act in concert to manipulate public discourse while concealing the organized nature of their activity. Unlike single-account bot detection, CIB detection looks for temporal co-occurrence, content reuse, synchronized amplification, and network clustering patterns that reveal cross-account coordination even when individual accounts appear authentic in isolation. The technique operationalizes the Facebook-originated CIB framework and related academic methods to distinguish organic consensus from manufactured consensus.

## When to use

- Investigating whether a trending narrative or hashtag is being artificially inflated by a coordinated group
- Assessing whether apparent public support for a position reflects genuine opinion or organized amplification
- Auditing influence operations targeting elections, public health messaging, or conflict narratives
- Supporting platform trust-and-safety teams in network-level enforcement decisions
- Providing evidence for journalistic or policy investigations into information operations

## What it produces

- Clusters of accounts linked by co-activity, content reuse, or network topology signatures
- Estimated reach and amplification multiplier of the coordinated behavior
- Behavioral typology of the coordination (synchronized posting, relay amplification, narrative seeding, etc.)
- Confidence-rated assessment distinguishing genuine coordination from coincidental co-activity

## Defensive boundary

Use Coordinated Inauthentic Behavior Detection only for information-environment monitoring and platform-risk defense: recognize, assess, document, or defend platform integrity, narrative context, and authentic community behavior. Do not use this skill to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement.

## Misuse redirect

If a request asks Coordinated Inauthentic Behavior Detection to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement, refuse that path and redirect to the safe defensive form: map supplied narratives, automation signals, or platform affordance risks for defensive review.

## Evidence discipline

- For Coordinated Inauthentic Behavior Detection, bind each finding to a labeled source — platform observations, coordination signals, narrative movement, automation signals, and provenance data, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Coordinated Inauthentic Behavior Detection, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Coordinated Inauthentic Behavior Detection recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Coordinated Inauthentic Behavior Detection: independent lines of platform observations, narrative movement, automation signals, and provenance data converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Coordinated Inauthentic Behavior Detection: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Coordinated Inauthentic Behavior Detection: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Coordinated Inauthentic Behavior Detection cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Coordinated Inauthentic Behavior Detection should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Coordinated Inauthentic Behavior Detection, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Coordinated Inauthentic Behavior Detection, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Coordinated Inauthentic Behavior Detection, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Coordinated Inauthentic Behavior Detection failure: treating engagement volume as proof of authenticity or coordinated intent.
- Coordinated Inauthentic Behavior Detection failure: producing guidance that would help a requester amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement.
- Coordinated Inauthentic Behavior Detection failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Coordinated Inauthentic Behavior Detection to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Coordinated Inauthentic Behavior Detection into an operational playbook to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Coordinated Inauthentic Behavior Detection to map supplied narratives, automation signals, or platform affordance risks for defensive review' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Coordination must be demonstrated across multiple independent dimensions — timing alone, or content reuse alone, is insufficient
- Inauthentic means the behavior misrepresents its organized nature, not that the viewpoint expressed is wrong
- Use temporal co-activity windows carefully: too narrow misses slow-rolling coordination, too wide captures organic convergence
- Always distinguish the coordination finding from any attribution claim about who orchestrates it — these require separate evidence chains
