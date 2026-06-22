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

- For Astroturfing Detection, bind every flagged cluster and every indicator-table entry to concrete evidence — a specific account record, a timestamp, a content hash, or a cross-platform observation — name the organic explanation it rules out, and label any cluster resting on inference alone as provisional rather than confirmed coordinated inauthentic behavior.
- For Astroturfing Detection, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the detection report.
- Before recommending any Astroturfing Detection action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Astroturfing Detection: each coordinated cluster in the detection report is supported by multiple independent behavioral and structural indicators — creation-date spikes, posting-velocity anomalies, content-hash overlap, and follower-graph density — drawn from more than one source, organic alternatives have been examined and ruled out, and no unresolved contradiction would change the inauthenticity verdict.
- Medium for Astroturfing Detection: the detection report is plausible, but one important campaign sample source, comparison case, or alternative explanation remains incomplete.
- Low for Astroturfing Detection: the detection report rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Astroturfing Detection cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating cognitive_security evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Astroturfing Detection, use only authorized campaign sample, and baseline context, public or source-approved records, and caller-provided context needed for the defensive task.
- For Astroturfing Detection, minimize person-level detail in the detection report; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Astroturfing Detection, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Astroturfing Detection: declaring activity inauthentic when the sample was never scoped for self-selection bias or the structural and behavioral heuristics were never actually run, so an absence of flagged clusters reflects an unfinished review rather than genuine grassroots discourse, and coordination has been conflated with deception.
- Astroturfing Detection: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Astroturfing Detection: reporting the detection report without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Astroturfing Detection outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the detection report from Astroturfing Detection into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Astroturfing Detection to assess supplied material for manipulation indicators and recommend resilience measures with campaign sample, and baseline context' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- look for behavioral coordination, not just content similarity — same message from 1000 accounts with identical posting cadence is more diagnostic than similar phrasing alone
- anchor findings to observable signals (creation date spikes, follower-graph density, cross-platform account reuse) rather than inferred intent
- assign confidence tiers and document which specific indicators drove each tier to support adversarial review of the conclusion
