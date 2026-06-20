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

- For Coordinated Inauthentic Behavior Detection, tie each coordination clusters, and cib report claim to concrete evidence from the specific account activity dataset, investigation scope, and known seed accounts item, source excerpt, observation, or command result that supports it.
- For Coordinated Inauthentic Behavior Detection, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the coordination clusters.
- Before recommending any Coordinated Inauthentic Behavior Detection action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Coordinated Inauthentic Behavior Detection: the coordination clusters is supported by multiple independent platform observations, narrative movement, automation signals, and provenance data; build the co-activity matrix and cross-reference prior cib reports and known networks checks agree, and no unresolved contradiction would change the result.
- Medium for Coordinated Inauthentic Behavior Detection: the coordination clusters is plausible, but one important account activity dataset source, comparison case, or alternative explanation remains incomplete.
- Low for Coordinated Inauthentic Behavior Detection: the coordination clusters rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Coordinated Inauthentic Behavior Detection cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating information_environment evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Coordinated Inauthentic Behavior Detection, use only authorized account activity dataset, investigation scope, and known seed accounts, public or source-approved records, and caller-provided context needed for the defensive task.
- For Coordinated Inauthentic Behavior Detection, minimize person-level detail in the coordination clusters; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Coordinated Inauthentic Behavior Detection, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Coordinated Inauthentic Behavior Detection: treating account activity dataset as complete when build the co-activity matrix and cross-reference prior cib reports and known networks checks or contradictory evidence are missing.
- Coordinated Inauthentic Behavior Detection: producing advice that would help a requester amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement.
- Coordinated Inauthentic Behavior Detection: reporting the coordination clusters without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Coordinated Inauthentic Behavior Detection outputs to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the coordination clusters from Coordinated Inauthentic Behavior Detection into an operational playbook to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Coordinated Inauthentic Behavior Detection to map supplied narratives, automation signals, or platform affordance risks for defensive review with account activity dataset, investigation scope, and known seed accounts' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Coordination must be demonstrated across multiple independent dimensions — timing alone, or content reuse alone, is insufficient
- Inauthentic means the behavior misrepresents its organized nature, not that the viewpoint expressed is wrong
- Use temporal co-activity windows carefully: too narrow misses slow-rolling coordination, too wide captures organic convergence
- Always distinguish the coordination finding from any attribution claim about who orchestrates it — these require separate evidence chains
