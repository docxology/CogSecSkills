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

## Failure modes
- Adversary Tradecraft Profiling failure: turning defensive tradecraft recognition into operational evasion advice.
- Adversary Tradecraft Profiling failure: producing guidance that would help a requester evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft.
- Adversary Tradecraft Profiling failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Adversary Tradecraft Profiling to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Adversary Tradecraft Profiling into an operational playbook to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Adversary Tradecraft Profiling to review supplied interactions or processes for deception, elicitation, or insider-risk indicators' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not assume the profile is exhaustive — adversaries operate outside analyst visibility; explicitly state what is NOT known
- do not treat frequency as proof of capability — an adversary may withhold their most capable techniques for high-value operations
- do not attribute purely from style similarity without corroborating evidence — tradecraft can be copied to frame a third party
- do not update the profile based on incidents the adversary may have staged to shape the profile

## AGEINT upstream
`docs/ageint/counterintelligence.md`
