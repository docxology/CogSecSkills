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
- For Information Laundering Tracing, bind each finding to a labeled source — content, behavioral, narrative, media, and audience-risk evidence, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Information Laundering Tracing, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Information Laundering Tracing recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Information Laundering Tracing: independent lines of content, behavioral, narrative, media, and audience-risk evidence converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Information Laundering Tracing: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Information Laundering Tracing: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Information Laundering Tracing cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Information Laundering Tracing should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Information Laundering Tracing, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Information Laundering Tracing, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Information Laundering Tracing, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Information Laundering Tracing failure: mistaking persuasive resonance for verified harm or intent.
- Information Laundering Tracing failure: producing guidance that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Information Laundering Tracing failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Information Laundering Tracing to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Information Laundering Tracing into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Information Laundering Tracing to assess supplied material for manipulation indicators and recommend resilience measures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not conflate organic viral spread with coordinated laundering without affirmative evidence of coordination — fast spread is not itself evidence of a campaign
- Do not omit the outlet tier classification — calling every node 'media' flattens the legitimization dynamic that makes laundering analytically meaningful
- Do not focus only on the most recent mainstream appearance; the full upstream chain must be traced to identify origin and key amplification nodes
- Do not name the laundering operation as deliberate unless the evidence (coordination signals, timing, identical seeding) supports that conclusion — maintain confidence calibration

## AGEINT upstream
`docs/ageint/cognitive-security.md`
