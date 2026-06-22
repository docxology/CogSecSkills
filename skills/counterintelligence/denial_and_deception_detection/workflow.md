# Workflow — Denial & Deception Detection

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Characterize the evidence and the beneficiary (read)
Document the full evidence body: each item, its source, how it entered the collection pipeline, and when it arrived relative to the analytic cycle. Identify who benefits most if the current assessment stands — that is the candidate deceiver. Assess their known D&D history and capability to access or influence each source channel.

## Step 2 — Apply the deceiver's calculus (reason)
Construct one or more deception scenarios: for each, specify what the adversary would need to (a) conceal (denial elements) and (b) fabricate or stage (deception elements) to produce the observed evidence picture. Ask: is this technically feasible? Would it require penetrating multiple independent sources simultaneously? What would the adversary risk in mounting this operation?

## Step 3 — Identify observable differences (reason)
For each deception scenario, list what would be observably different between the real world and the managed scenario. These are the deception indicators. Check each against existing collection: is it currently observed, absent, or unknown? Note that absence of expected confirmatory evidence is itself a potential deception indicator ('dog that didn't bark').

## Step 4 — Rate plausibility and flag the assessment (reason, write)
Score each deception scenario on adversary capability to execute, motive (what they gain from our erroneous conclusion), opportunity (access to collection channels), and the plausibility cost (how many improbable things must be simultaneously true). Assign HIGH/MEDIUM/LOW deception plausibility. Flag the current analytic assessment with the appropriate D&D caveat.

## Step 5 — Prescribe discriminating collection (write)
Output the deception indicators table and a prioritized collection plan. Rank collection gaps by their discriminating power: which single piece of new evidence would most sharply distinguish genuine from managed? Include recommendations for accessing channels the adversary cannot realistically control.

## Evidence requirements
- For Denial & Deception Detection, anchor each deception scenario, plausibility rating, and indicator status to concrete evidence about a specific item in the evidence body, its source channel, and its arrival timing, and treat a missing confirmatory signal as a flagged gap rather than as evidence of authenticity.
- For Denial & Deception Detection, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the dd assessment.
- Before recommending any Denial & Deception Detection action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Denial & Deception Detection: the deception scenario specifies which sources the adversary would need to control and conceal, the plausibility rating accounts for capability, motive, and opportunity together, the observable deception indicators are checked against actual collection, and no unresolved contradiction would change the conclusion.
- Medium for Denial & Deception Detection: the dd assessment is plausible, but one important evidence body source, comparison case, or alternative explanation remains incomplete.
- Low for Denial & Deception Detection: the dd assessment rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Denial & Deception Detection cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating counterintelligence evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Denial & Deception Detection, use only authorized evidence body, current assessment, and adversary profile, public or source-approved records, and caller-provided context needed for the defensive task.
- For Denial & Deception Detection, minimize person-level detail in the dd assessment; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Denial & Deception Detection, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Denial & Deception Detection: treating an absence of observed deception indicators as proof of authenticity when the deceiver's calculus was never genuinely constructed, or when investment in the current assessment was allowed to suppress the check, so a clean verdict reflects unexamined evidence rather than a tested picture.
- Denial & Deception Detection: producing advice that would help a requester evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft.
- Denial & Deception Detection: reporting the dd assessment without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Denial & Deception Detection outputs to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the dd assessment from Denial & Deception Detection into an operational playbook to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Denial & Deception Detection to review supplied interactions or processes for deception, elicitation, or insider-risk indicators with evidence body, current assessment, and adversary profile' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not dismiss a deception scenario solely because it would be 'too complicated' — sophisticated adversaries routinely execute multi-year, multi-source denial and deception operations
- do not conflate low base rate of deception with low current probability — if adversary motive and opportunity are present, base rates are not the right prior
- do not allow the current assessment's investment — resources committed, policies built on it — to suppress the D&D check; anchoring to sunk costs is a key adversary exploitation target
- do not treat a passed D&D check as permanent; circumstances change and an assessment that was clean yesterday can be contaminated today

## AGEINT upstream
`docs/ageint/counterintelligence.md`
