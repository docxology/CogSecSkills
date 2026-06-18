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

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- No single signal is diagnostic — classification requires converging behavioral, temporal, and network evidence
- Calibrate base rates to the platform and context before applying thresholds
- Distinguish bots (fully automated) from cyborgs (human + automated) from coordinated humans — they require different responses
- Report confidence levels honestly; avoid binary labels when evidence is ambiguous
