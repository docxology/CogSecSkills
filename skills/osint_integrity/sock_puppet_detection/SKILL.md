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

- For Sock-Puppet Detection, tie every flagged indicator in the assessment to concrete evidence — the archived creation date, posting-pace data, follower-growth curve, reverse-image result, or interaction-cluster overlap that supports it — record alternative explanations considered, and treat account signals as support for a hypothesis rather than a definitive identification, because an unsupported inauthenticity label is speculation, not evidence.
- For Sock-Puppet Detection, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the indicator assessment.
- Before recommending any Sock-Puppet Detection action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Sock-Puppet Detection: indicators converge across the behavioral, temporal, network, and content classes rather than resting on any single signature, the account is compared against an authentic baseline from the same community, alternative explanations such as an obsessive lone real user are weighed and excluded, and no unresolved contradiction would change the inauthenticity verdict.
- Medium for Sock-Puppet Detection: the indicator assessment is plausible, but one important account identifier source, comparison case, or alternative explanation remains incomplete.
- Low for Sock-Puppet Detection: the indicator assessment rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Sock-Puppet Detection cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating osint_integrity evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Sock-Puppet Detection, use only authorized account identifier, platform, and related accounts, public or source-approved records, and caller-provided context needed for the defensive task.
- For Sock-Puppet Detection, minimize person-level detail in the indicator assessment; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Sock-Puppet Detection, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Sock-Puppet Detection: labelling an account inauthentic from one indicator such as high posting volume or a stock-looking photo, conflating automation with inauthenticity, or publishing operator attribution from behavioral OSINT alone, so a hypothesis is mistaken for identification and legitimate adversarial speech risks being suppressed.
- Sock-Puppet Detection: producing advice that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Sock-Puppet Detection: reporting the indicator assessment without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Sock-Puppet Detection outputs to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the indicator assessment from Sock-Puppet Detection into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Sock-Puppet Detection to verify supplied claims, media, sources, or datasets with documented public-source methods with account identifier, platform, and related accounts' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- no single indicator is definitive — new accounts are also started by real people, and not all high-volume posters are bots; require convergence across indicator classes
- compare the account against a baseline of authentic accounts in the same community to avoid applying inappropriate standards
- temporal spikes correlated with political events are among the strongest early signals — capture them before accounts are deleted
- coordinated behavior is more diagnostic than individual account properties — the network pattern is harder to fake than the account surface
