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

## Anti-criteria (must NOT happen)
- do not assume the profile is exhaustive — adversaries operate outside analyst visibility; explicitly state what is NOT known
- do not treat frequency as proof of capability — an adversary may withhold their most capable techniques for high-value operations
- do not attribute purely from style similarity without corroborating evidence — tradecraft can be copied to frame a third party
- do not update the profile based on incidents the adversary may have staged to shape the profile

## AGEINT upstream
`docs/ageint/counterintelligence.md`
