# Workflow — Information Laundering Tracing

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Canonicalize the claim (read)
State the exact claim in its most precise form. Identify the variant phrasings used across outlets so searches catch mutations. Document the first known instance if already available.

## Step 2 — Map the publication chain (search, web)
Search for every known publication of the claim across outlet tiers (origin, fringe/aggregator, partisan, mainstream, institutional). Use archive.org to recover deleted pages. Record URL, date, outlet name, outlet tier (1=fringe to 5=major mainstream/institutional), and direct quote of the claim.

## Step 3 — Identify laundering nodes and tactics (reason)
Order publications chronologically. At each transition between tier levels, note: (a) which caveats were dropped, (b) what authority was borrowed or invented (e.g., 'experts say', citation to earlier laundered piece), (c) whether the outlet added original reporting or merely aggregated. Flag nodes where the legitimization leap is largest.

## Step 4 — Assess coordination vs. organic spread (reason)
Examine timing gaps between publications, cross-ownership or editorial links between outlets, and whether low-credibility simultaneous publications suggest a seeding campaign. Note signals of coordination: identical phrasing across unrelated outlets, suspiciously rapid Tier-1 pickup, or known state-media involvement in the chain.

## Step 5 — Emit laundering chain and analysis (write)
Produce a chronological table of publication nodes with tier, fidelity, and caveat status. Write a narrative identifying the primary laundering nodes, the tactic used at each key step, and an overall assessment of whether the laundering appears opportunistic or deliberate. Flag the node(s) that most effectively legitimized the claim.

## Evidence requirements
- For Information Laundering Tracing, tie each laundering chain, and analysis narrative claim to concrete evidence from the specific claim text, known publications, and time window item, source excerpt, observation, or command result that supports it.
- For Information Laundering Tracing, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the laundering chain.
- Before recommending any Information Laundering Tracing action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Information Laundering Tracing: the laundering chain is supported by multiple independent content, behavioral, narrative, media, and audience-risk evidence; canonicalize the claim and map the publication chain checks agree, and no unresolved contradiction would change the result.
- Medium for Information Laundering Tracing: the laundering chain is plausible, but one important claim text source, comparison case, or alternative explanation remains incomplete.
- Low for Information Laundering Tracing: the laundering chain rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Information Laundering Tracing cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating cognitive_security evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Information Laundering Tracing, use only authorized claim text, known publications, and time window, public or source-approved records, and caller-provided context needed for the defensive task.
- For Information Laundering Tracing, minimize person-level detail in the laundering chain; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Information Laundering Tracing, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Information Laundering Tracing: treating claim text as complete when canonicalize the claim and map the publication chain checks or contradictory evidence are missing.
- Information Laundering Tracing: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Information Laundering Tracing: reporting the laundering chain without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Information Laundering Tracing outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the laundering chain from Information Laundering Tracing into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Information Laundering Tracing to assess supplied material for manipulation indicators and recommend resilience measures with claim text, known publications, and time window' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not conflate organic viral spread with coordinated laundering without affirmative evidence of coordination — fast spread is not itself evidence of a campaign
- Do not omit the outlet tier classification — calling every node 'media' flattens the legitimization dynamic that makes laundering analytically meaningful
- Do not focus only on the most recent mainstream appearance; the full upstream chain must be traced to identify origin and key amplification nodes
- Do not name the laundering operation as deliberate unless the evidence (coordination signals, timing, identical seeding) supports that conclusion — maintain confidence calibration

## AGEINT upstream
`docs/ageint/cognitive-security.md`
