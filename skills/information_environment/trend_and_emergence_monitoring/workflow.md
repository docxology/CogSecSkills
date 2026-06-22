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

## Evidence requirements
- For Trend & Emergence Monitoring, bind each finding to a labeled source — platform observations, narrative movement, automation signals, and provenance data, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Trend & Emergence Monitoring, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Trend & Emergence Monitoring recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Trend & Emergence Monitoring: independent lines of platform observations, narrative movement, automation signals, and provenance data converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Trend & Emergence Monitoring: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Trend & Emergence Monitoring: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Trend & Emergence Monitoring cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Trend & Emergence Monitoring should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Trend & Emergence Monitoring, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Trend & Emergence Monitoring, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Trend & Emergence Monitoring, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Trend & Emergence Monitoring failure: treating engagement volume as proof of authenticity or coordinated intent.
- Trend & Emergence Monitoring failure: producing guidance that would help a requester amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement.
- Trend & Emergence Monitoring failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Trend & Emergence Monitoring to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Trend & Emergence Monitoring into an operational playbook to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Trend & Emergence Monitoring to map supplied narratives, automation signals, or platform affordance risks for defensive review' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not escalate a single-instance observation as an emerging trend — the three-signal corroboration threshold must be met before escalation
- do not conflate high volume with emergence — a consistently high-volume topic is the baseline, not an emergence signal; only velocity above baseline constitutes emergence
- do not attribute coordinated appearance to a state or non-state actor without separate attribution evidence — coordination indicators establish synthetic amplification, not actor identity
- do not allow watchlist tunnel-vision to prevent detection of novel signals outside the existing watchlist — include an unstructured scan component each cycle

## AGEINT upstream
`docs/ageint/information-environment.md`
