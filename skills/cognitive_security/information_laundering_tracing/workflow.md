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

## Anti-criteria (must NOT happen)
- Do not conflate organic viral spread with coordinated laundering without affirmative evidence of coordination — fast spread is not itself evidence of a campaign
- Do not omit the outlet tier classification — calling every node 'media' flattens the legitimization dynamic that makes laundering analytically meaningful
- Do not focus only on the most recent mainstream appearance; the full upstream chain must be traced to identify origin and key amplification nodes
- Do not name the laundering operation as deliberate unless the evidence (coordination signals, timing, identical seeding) supports that conclusion — maintain confidence calibration

## AGEINT upstream
`docs/ageint/cognitive-security.md`
