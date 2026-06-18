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

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- no single indicator is definitive — new accounts are also started by real people, and not all high-volume posters are bots; require convergence across indicator classes
- compare the account against a baseline of authentic accounts in the same community to avoid applying inappropriate standards
- temporal spikes correlated with political events are among the strongest early signals — capture them before accounts are deleted
- coordinated behavior is more diagnostic than individual account properties — the network pattern is harder to fake than the account surface
