---
name: cognitive_security.astroturfing_detection
description: Distinguish manufactured grassroots activity from organic engagement.
---

# Astroturfing Detection

Astroturfing detection identifies manufactured grassroots activity — coordinated campaigns designed to simulate organic, spontaneous public support or opposition. The technique draws on network-structure analysis, account behavioral signals, and content-similarity patterns to distinguish authentic civic expression from synthetic amplification. Defensively, it helps analysts, journalists, and platform trust-and-safety teams surface coordinated inauthentic behavior (CIB) and protect genuine public discourse from being drowned out or misrepresented.

## When to use

- a narrative is spreading unusually fast and account patterns look homogeneous
- a social movement or petition appears but its account base lacks organic growth history
- a platform trust-and-safety team is investigating potential CIB
- an analyst needs to distinguish genuine public opinion from manufactured consensus before briefing decision-makers
- a journalist is fact-checking whether a hashtag campaign is organic

## What it produces

- a tiered confidence assessment (high/medium/low) that the activity is coordinated and inauthentic
- a list of behavioral and structural indicators used to reach the conclusion
- cluster-level view of which accounts appear to be operating in concert
- recommended follow-on steps (e.g., platform reporting, further OSINT, or temporal anchoring)

## Defensive boundary

Use Astroturfing Detection only for cognitive-security defense: recognize, assess, document, or defend audiences, decision-makers, and public discourse. Do not use this skill to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.

## Misuse redirect

If a request asks Astroturfing Detection to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation, refuse that path and redirect to the safe defensive form: assess supplied material for manipulation indicators and recommend resilience measures.

## Evidence discipline

- For Astroturfing Detection, bind each finding to a labeled source — content, behavioral, narrative, media, and audience-risk evidence, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Astroturfing Detection, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Astroturfing Detection recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Astroturfing Detection: independent lines of content, behavioral, narrative, media, and audience-risk evidence converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Astroturfing Detection: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Astroturfing Detection: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Astroturfing Detection cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Astroturfing Detection should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Astroturfing Detection, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Astroturfing Detection, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Astroturfing Detection, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Astroturfing Detection failure: mistaking persuasive resonance for verified harm or intent.
- Astroturfing Detection failure: producing guidance that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Astroturfing Detection failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Astroturfing Detection to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Astroturfing Detection into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Astroturfing Detection to assess supplied material for manipulation indicators and recommend resilience measures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- look for behavioral coordination, not just content similarity — same message from 1000 accounts with identical posting cadence is more diagnostic than similar phrasing alone
- anchor findings to observable signals (creation date spikes, follower-graph density, cross-platform account reuse) rather than inferred intent
- assign confidence tiers and document which specific indicators drove each tier to support adversarial review of the conclusion
