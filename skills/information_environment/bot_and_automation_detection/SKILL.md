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

- For Bot & Automation Detection, bind each finding to a labeled source — platform observations, narrative movement, automation signals, and provenance data, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Bot & Automation Detection, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Bot & Automation Detection recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Bot & Automation Detection: independent lines of platform observations, narrative movement, automation signals, and provenance data converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Bot & Automation Detection: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Bot & Automation Detection: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Bot & Automation Detection cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Bot & Automation Detection should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Bot & Automation Detection, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Bot & Automation Detection, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Bot & Automation Detection, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Bot & Automation Detection failure: treating engagement volume as proof of authenticity or coordinated intent.
- Bot & Automation Detection failure: producing guidance that would help a requester amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement.
- Bot & Automation Detection failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Bot & Automation Detection to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Bot & Automation Detection into an operational playbook to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Bot & Automation Detection to map supplied narratives, automation signals, or platform affordance risks for defensive review' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- No single signal is diagnostic — classification requires converging behavioral, temporal, and network evidence
- Calibrate base rates to the platform and context before applying thresholds
- Distinguish bots (fully automated) from cyborgs (human + automated) from coordinated humans — they require different responses
- Report confidence levels honestly; avoid binary labels when evidence is ambiguous
