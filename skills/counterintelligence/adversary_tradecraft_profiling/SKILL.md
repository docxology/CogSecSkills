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

- For Adversary Tradecraft Profiling, bind every tactic, technique, signature, and anticipatory indicator to concrete evidence from a specific attributed incident in the corpus, naming the case, source, and attribution confidence, and flag any pattern resting on a single operation as provisional rather than probative evidence.
- For Adversary Tradecraft Profiling, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the tradecraft profile.
- Before recommending any Adversary Tradecraft Profiling action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Adversary Tradecraft Profiling: each stable TTP in the tradecraft profile is corroborated across two or more independently attributed incidents, the consistency-and-confidence scoring holds when any single case is removed, the anticipatory indicators follow logically from those patterns, and no unresolved contradiction would change the assessment.
- Medium for Adversary Tradecraft Profiling: the tradecraft profile is plausible, but one important incident corpus source, comparison case, or alternative explanation remains incomplete.
- Low for Adversary Tradecraft Profiling: the tradecraft profile rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Adversary Tradecraft Profiling cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating counterintelligence evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Adversary Tradecraft Profiling, use only authorized incident corpus, adversary identifier, and collection gaps, public or source-approved records, and caller-provided context needed for the defensive task.
- For Adversary Tradecraft Profiling, minimize person-level detail in the tradecraft profile; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Adversary Tradecraft Profiling, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Adversary Tradecraft Profiling: declaring the profile durable when the clustering step never separated stable signatures from one-off adaptive camouflage, or when known collection gaps were left unstated, so apparent patterns reflect biased visibility rather than genuine adversary habits.
- Adversary Tradecraft Profiling: producing advice that would help a requester evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft.
- Adversary Tradecraft Profiling: reporting the tradecraft profile without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Adversary Tradecraft Profiling outputs to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the tradecraft profile from Adversary Tradecraft Profiling into an operational playbook to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Adversary Tradecraft Profiling to review supplied interactions or processes for deception, elicitation, or insider-risk indicators with incident corpus, adversary identifier, and collection gaps' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- distinguish stable signatures (consistent across operations under pressure) from adaptive camouflage (one-off deceptions); the former is probative, the latter is noise
- profile the behavior, not the identity — capabilities and habits leave evidence even when attribution is uncertain
- flag collection gaps explicitly; a profile derived from only visible operations systematically misses the techniques used when the adversary evades detection
