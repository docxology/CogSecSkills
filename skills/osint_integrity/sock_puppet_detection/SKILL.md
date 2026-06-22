---
name: osint_integrity.sock_puppet_detection
description: Identify inauthentic personas from behavioral, temporal, and network signals.
---

# Sock-Puppet Detection

Sock-puppet detection identifies inauthentic online personas — accounts created to simulate independent real people — by analyzing behavioral, temporal, network, and content signals that distinguish coordinated inauthentic behavior from organic activity. The technique is a core defensive OSINT practice used to assess whether an apparent grassroots voice is actually a manufactured identity. Detection relies on converging indicators rather than any single signature, since sophisticated operations deliberately vary surface features to evade heuristics.

## When to use

- an account is amplifying a narrative of investigative or strategic interest and its authenticity is uncertain
- a cluster of accounts appears to be coordinating — posting the same content within minutes, using similar language, or targeting the same individuals
- an OSINT investigation requires assessing whether apparent public opinion is manufactured
- a platform policy enforcement analysis needs to distinguish bots, sock puppets, and cyborg accounts from organic users
- an analyst needs to assess whether a source cited as 'ordinary users' is actually an organized network

## What it produces

- a behavioral indicator profile: posting volume, times of day, posting pace, content diversity, and ratio of original posts to amplifications
- a temporal indicator profile: account age relative to creation of content niche, account-name change history, activity spikes correlated with geopolitical events
- a network indicator profile: ratio of followers to following, interaction cluster overlap with other suspected inauthentic accounts, follower acquisition rate
- a content and identity indicator profile: profile image reverse-search result, biographic inconsistency, language register inconsistency, topic monoculture
- a confidence-tiered verdict: likely inauthentic / possible inauthentic / insufficient evidence / likely authentic

## Defensive boundary

Use Sock-Puppet Detection only for OSINT integrity and source-verification defense: recognize, assess, document, or defend source provenance, privacy, chain of custody, and public-source accountability. Do not use this skill to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.

## Misuse redirect

If a request asks Sock-Puppet Detection to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence, refuse that path and redirect to the safe defensive form: verify supplied claims, media, sources, or datasets with documented public-source methods.

## Evidence discipline

- For Sock-Puppet Detection, bind each finding to a labeled source — source records, custody notes, metadata, corroborating references, and contradiction logs, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Sock-Puppet Detection, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Sock-Puppet Detection recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Sock-Puppet Detection: independent lines of source records, custody notes, metadata, corroborating references, and contradiction logs converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Sock-Puppet Detection: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Sock-Puppet Detection: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Sock-Puppet Detection cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Sock-Puppet Detection should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Sock-Puppet Detection, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Sock-Puppet Detection, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Sock-Puppet Detection, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Sock-Puppet Detection failure: overstating identity, location, attribution, or source reliability from incomplete public traces.
- Sock-Puppet Detection failure: producing guidance that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Sock-Puppet Detection failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Sock-Puppet Detection to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Sock-Puppet Detection into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Sock-Puppet Detection to verify supplied claims, media, sources, or datasets with documented public-source methods' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- no single indicator is definitive — new accounts are also started by real people, and not all high-volume posters are bots; require convergence across indicator classes
- compare the account against a baseline of authentic accounts in the same community to avoid applying inappropriate standards
- temporal spikes correlated with political events are among the strongest early signals — capture them before accounts are deleted
- coordinated behavior is more diagnostic than individual account properties — the network pattern is harder to fake than the account surface
