---
name: counterintelligence.adversary_tradecraft_profiling
description: Profile an adversary's methods, patterns, and signatures to anticipate their moves.
---

# Adversary Tradecraft Profiling

Adversary tradecraft profiling systematically characterizes the methods, patterns, tools, and operational signatures an adversary habitually employs across known operations. Drawn from counterintelligence practice, it converts scattered incident data into a durable behavioral model that enables anticipation of future moves, attribution of ambiguous incidents, and identification of gaps the adversary exploits. The technique applies structured elicitation across the TTPS (Tactics, Techniques, Procedures, and Signatures) framework to distinguish stable behavioral fingerprints from adaptive camouflage.

## When to use

- a threat actor has left multiple attributed incidents and a durable behavioral model would aid defense or attribution
- an analyst needs to distinguish a known adversary's pattern from coincidental or unrelated activity
- decision-makers require anticipatory warning indicators rather than post-hoc attribution
- a new incident is ambiguous and comparison against a tradecraft profile could resolve attribution

## What it produces

- a TTPS table mapping observed tactics to their techniques, confidence levels, and frequency across known cases
- a set of behavioral signatures and leading indicators to watch for in future operations
- explicit caveats on collection bias, mirror-imaging risk, and adversary adaptive capacity

## Defensive boundary

Use Adversary Tradecraft Profiling only for counterintelligence and analytic-process defense: recognize, assess, document, or defend analytic teams, collection processes, and institutional trust boundaries. Do not use this skill to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft.

## Misuse redirect

If a request asks Adversary Tradecraft Profiling to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft, refuse that path and redirect to the safe defensive form: review supplied interactions or processes for deception, elicitation, or insider-risk indicators.

## Evidence discipline

- For Adversary Tradecraft Profiling, bind each finding to a labeled source — interaction records, process artifacts, deception indicators, and alternative explanations, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Adversary Tradecraft Profiling, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Adversary Tradecraft Profiling recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Adversary Tradecraft Profiling: independent lines of interaction records, process artifacts, deception indicators, and alternative explanations converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Adversary Tradecraft Profiling: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Adversary Tradecraft Profiling: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Adversary Tradecraft Profiling cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Adversary Tradecraft Profiling should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Adversary Tradecraft Profiling, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Adversary Tradecraft Profiling, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Adversary Tradecraft Profiling, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Adversary Tradecraft Profiling failure: turning defensive tradecraft recognition into operational evasion advice.
- Adversary Tradecraft Profiling failure: producing guidance that would help a requester evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft.
- Adversary Tradecraft Profiling failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Adversary Tradecraft Profiling to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Adversary Tradecraft Profiling into an operational playbook to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Adversary Tradecraft Profiling to review supplied interactions or processes for deception, elicitation, or insider-risk indicators' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- distinguish stable signatures (consistent across operations under pressure) from adaptive camouflage (one-off deceptions); the former is probative, the latter is noise
- profile the behavior, not the identity — capabilities and habits leave evidence even when attribution is uncertain
- flag collection gaps explicitly; a profile derived from only visible operations systematically misses the techniques used when the adversary evades detection
