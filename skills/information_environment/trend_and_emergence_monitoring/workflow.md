# Workflow — Trend & Emergence Monitoring

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Refresh scope and baseline (read)
Load the monitoring scope definition and the baseline report from the prior cycle. Review the current watchlist. Identify any scope updates warranted by recent events. Confirm the time window for this cycle and the platforms to be scanned.

## Step 2 — Collect current signals (search, web)
Execute searches across the defined platform set using watchlist terms, hashtags, and related semantic queries. Retrieve a representative sample of content from each platform. Where direct API access is unavailable, use web retrieval of public-facing content. Log raw signal counts and note any content that appears new or anomalous relative to the baseline.

## Step 3 — Detect and classify emergence (reason)
Compare observed content volume and topic distribution against the baseline. Flag topics, hashtags, or narratives showing elevated velocity (not just volume). For each flagged signal, classify its emergence stage: seeding (low volume, specific seed accounts), early-growth (beginning organic spread or amplification), acceleration (rapid uptake), or plateau (peak reach, beginning to recede). Apply the three-signal corroboration threshold before escalating.

## Step 4 — Assess authenticity and coordination (reason)
For each escalated signal, assess whether spread appears organic or coordinated. Indicators of coordination: synchronized posting times, identical or near-identical content across unrelated accounts, unusual account-age or follower-acquisition patterns, content appearing on fringe platforms before mainstream ones (cross-platform seeding). Flag signals showing multiple coordination indicators for follow-on network analysis.

## Step 5 — Produce report and update baseline (write)
Populate the signal log table with all detected signals and their assessments. Write the monitoring report narrative covering the top three to five emerging signals with evidence, authenticity assessment, emergence stage, and recommended follow-on actions. Update the baseline with this cycle's observed distribution to enable next-cycle comparison.

## Anti-criteria (must NOT happen)
- do not escalate a single-instance observation as an emerging trend — the three-signal corroboration threshold must be met before escalation
- do not conflate high volume with emergence — a consistently high-volume topic is the baseline, not an emergence signal; only velocity above baseline constitutes emergence
- do not attribute coordinated appearance to a state or non-state actor without separate attribution evidence — coordination indicators establish synthetic amplification, not actor identity
- do not allow watchlist tunnel-vision to prevent detection of novel signals outside the existing watchlist — include an unstructured scan component each cycle

## AGEINT upstream
`docs/ageint/information-environment.md`
