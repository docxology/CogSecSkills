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
- For Trend & Emergence Monitoring, tie each logged signal, emergence-stage classification, and escalation recommendation to concrete evidence from the supplied monitoring scope, watchlist, and baseline report, citing the specific velocity change or coordination indicator that supports it, and treat coordination signals as evidence of synthetic amplification rather than actor attribution.
- For Trend & Emergence Monitoring, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the signal log.
- Before recommending any Trend & Emergence Monitoring action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Trend & Emergence Monitoring: each escalated signal in the log clears the three-signal corroboration threshold across independent sources, shows velocity above the established baseline rather than mere volume, carries a defensible emergence-stage and organic-versus-coordinated assessment, and no unresolved contradiction would change which signals warrant deeper investigation.
- Medium for Trend & Emergence Monitoring: the signal log is plausible, but one important monitoring scope source, comparison case, or alternative explanation remains incomplete.
- Low for Trend & Emergence Monitoring: the signal log rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Trend & Emergence Monitoring cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating information_environment evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Trend & Emergence Monitoring, use only authorized monitoring scope, watchlist, and baseline report, public or source-approved records, and caller-provided context needed for the defensive task.
- For Trend & Emergence Monitoring, minimize person-level detail in the signal log; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Trend & Emergence Monitoring, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Trend & Emergence Monitoring: escalating a single-instance observation before the three-signal corroboration threshold is met, mistaking a consistently high-volume topic for emergence, or letting watchlist tunnel-vision suppress novel signals, so the early-warning output raises false alarms or misses genuine nascent narratives.
- Trend & Emergence Monitoring: producing advice that would help a requester amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement.
- Trend & Emergence Monitoring: reporting the signal log without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Trend & Emergence Monitoring outputs to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the signal log from Trend & Emergence Monitoring into an operational playbook to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Trend & Emergence Monitoring to map supplied narratives, automation signals, or platform affordance risks for defensive review with monitoring scope, watchlist, and baseline report' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not escalate a single-instance observation as an emerging trend — the three-signal corroboration threshold must be met before escalation
- do not conflate high volume with emergence — a consistently high-volume topic is the baseline, not an emergence signal; only velocity above baseline constitutes emergence
- do not attribute coordinated appearance to a state or non-state actor without separate attribution evidence — coordination indicators establish synthetic amplification, not actor identity
- do not allow watchlist tunnel-vision to prevent detection of novel signals outside the existing watchlist — include an unstructured scan component each cycle

## AGEINT upstream
`docs/ageint/information-environment.md`
