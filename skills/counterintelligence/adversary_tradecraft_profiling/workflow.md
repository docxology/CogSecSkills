# Workflow — Adversary Tradecraft Profiling

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Assemble the incident corpus (read)
Gather all attributed or candidate-attributed operations, incidents, and case reports. Note the source, confidence of attribution, and date for each. Flag any periods of known low observability that could bias the corpus.

## Step 2 — Extract and cluster TTPs (reason)
For each incident, extract observed tactics (what goal was pursued), techniques (how it was executed), procedures (specific operational details), and signatures (idiosyncratic markers). Cluster across incidents to identify patterns appearing in 2+ independent cases. Distinguish recurring patterns from unique events.

## Step 3 — Assess consistency and confidence (reason)
Score each extracted TTP by frequency (how many independent cases), consistency under pressure (does the pattern persist when the adversary knows they are observed?), and cross-source corroboration. Assign HIGH/MEDIUM/LOW confidence. Flag TTPs that rest on a single source or a single operation.

## Step 4 — Generate anticipatory indicators (reason, write)
For each high-confidence stable TTP, derive one or more observable leading indicators: what would be visible early in the next operation if this pattern held. Express as 'IF [observable], THEN [TTP inference] with [confidence]' to support future collection tasking.

## Step 5 — Document profile and caveats (write)
Produce the TTPS table, the anticipatory indicators list, and a caveats section addressing: known collection gaps, baseline rate of adversary adaptation, risk of mirror-imaging (assuming the adversary thinks as we do), and explicit statement of what would change each high-confidence assessment.

## Evidence requirements
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

## Failure modes
- Adversary Tradecraft Profiling: declaring the profile durable when the clustering step never separated stable signatures from one-off adaptive camouflage, or when known collection gaps were left unstated, so apparent patterns reflect biased visibility rather than genuine adversary habits.
- Adversary Tradecraft Profiling: producing advice that would help a requester evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft.
- Adversary Tradecraft Profiling: reporting the tradecraft profile without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Adversary Tradecraft Profiling outputs to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the tradecraft profile from Adversary Tradecraft Profiling into an operational playbook to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Adversary Tradecraft Profiling to review supplied interactions or processes for deception, elicitation, or insider-risk indicators with incident corpus, adversary identifier, and collection gaps' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not assume the profile is exhaustive — adversaries operate outside analyst visibility; explicitly state what is NOT known
- do not treat frequency as proof of capability — an adversary may withhold their most capable techniques for high-value operations
- do not attribute purely from style similarity without corroborating evidence — tradecraft can be copied to frame a third party
- do not update the profile based on incidents the adversary may have staged to shape the profile

## AGEINT upstream
`docs/ageint/counterintelligence.md`
