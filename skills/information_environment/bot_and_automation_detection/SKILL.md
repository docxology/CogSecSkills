---
name: information_environment.bot_and_automation_detection
description: Distinguish automated from human activity using behavioral and temporal signals.
---

# Bot & Automation Detection

Bot and automation detection applies behavioral, temporal, network, and linguistic fingerprinting to distinguish automated or semi-automated accounts from genuine human participants in an information environment. The technique draws on academic research into coordinated amplification, sockpuppet behavior, and platform API abuse to surface accounts whose posting cadence, account-creation timing, content uniformity, or follower graph structure are inconsistent with organic human activity. Outputs support decisions about source credibility, narrative provenance, and the severity of inauthentic amplification.

## When to use

- Evaluating whether a trending topic or hashtag is being artificially amplified
- Assessing the credibility of apparent grassroots support for a narrative
- Auditing follower bases of key influencers for inauthentic inflation
- Investigating accounts that spread disinformation at superhuman posting rates
- Pre-publication triage of claimed 'public sentiment' signals

## What it produces

- A per-account classification table with confidence and evidence rationale
- An aggregate estimate of inauthentic amplification share in the dataset
- Identified behavioral signatures that distinguish automated from human accounts in this specific context
- Caveats on false-positive risk for high-volume legitimate users

## Defensive boundary

Use Bot & Automation Detection only for information-environment monitoring and platform-risk defense: recognize, assess, document, or defend platform integrity, narrative context, and authentic community behavior. Do not use this skill to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement.

## Misuse redirect

If a request asks Bot & Automation Detection to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement, refuse that path and redirect to the safe defensive form: map supplied narratives, automation signals, or platform affordance risks for defensive review.

## Evidence discipline

- For Bot & Automation Detection, bind every account classification and every amplification estimate to concrete evidence drawn from the supplied account metadata and post histories, naming the specific temporal, content, or network signal that supports it; a label without converging evidence is provisional and must carry its confidence level.
- For Bot & Automation Detection, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the account classifications.
- Before recommending any Bot & Automation Detection action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Bot & Automation Detection: the per-account classifications and the aggregate inauthentic-amplification estimate each rest on converging behavioral, temporal, network, and linguistic signals corroborated by independent platform observations and reputation lookups, the classifications stay stable when any single signal is removed, and no unresolved contradiction would change the authenticity conclusion.
- Medium for Bot & Automation Detection: the account classifications is plausible, but one important account data source, comparison case, or alternative explanation remains incomplete.
- Low for Bot & Automation Detection: the account classifications rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Bot & Automation Detection cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating information_environment evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Bot & Automation Detection, use only authorized account data, and context, public or source-approved records, and caller-provided context needed for the defensive task.
- For Bot & Automation Detection, minimize person-level detail in the account classifications; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Bot & Automation Detection, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Bot & Automation Detection: declaring accounts classified when the multi-signal scoring relied on a single feature such as posting frequency, the platform base rates were never calibrated, or high-volume legitimate users were swept in, so the labels reflect an under-grounded heuristic rather than demonstrated automation.
- Bot & Automation Detection: producing advice that would help a requester amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement.
- Bot & Automation Detection: reporting the account classifications without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Bot & Automation Detection outputs to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the account classifications from Bot & Automation Detection into an operational playbook to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Bot & Automation Detection to map supplied narratives, automation signals, or platform affordance risks for defensive review with account data, and context' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- No single signal is diagnostic — classification requires converging behavioral, temporal, and network evidence
- Calibrate base rates to the platform and context before applying thresholds
- Distinguish bots (fully automated) from cyborgs (human + automated) from coordinated humans — they require different responses
- Report confidence levels honestly; avoid binary labels when evidence is ambiguous
