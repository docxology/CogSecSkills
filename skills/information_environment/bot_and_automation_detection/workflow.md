# Workflow — Bot & Automation Detection

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Ingest and profile accounts (read)
Load account metadata and post histories. Compute behavioral features: posts-per-day, interposting interval distribution, reply-to-original ratio, unique vocabulary size, profile completeness score, account age vs. follower count ratio.

## Step 2 — Cross-reference known indicators (search)
Check accounts against known bot taxonomies (e.g. Astroturf botnets, amplification bots, content-farm accounts). Look up any available reputation signals or prior flagging by platform trust-and-safety teams.

## Step 3 — Apply multi-signal classification (reason)
For each account, score it on temporal regularity (inter-tweet interval entropy), content diversity (type-token ratio, near-duplicate detection), network position (follow/unfollow churn, follow-back ratio), and metadata consistency (username patterns, profile image uniqueness). Converge signals into a classification: likely bot, cyborg, coordinated human, or genuine human. Flag edge cases explicitly.

## Step 4 — Assess amplification impact and emit report (reason, write)
Aggregate the per-account classifications to estimate inauthentic amplification share. Write the classification table and a detection report that documents methodology, confidence, specific signal evidence per account, false-positive risk factors, and recommended investigative or defensive actions.

## Anti-criteria (must NOT happen)
- Do not classify an account as a bot based on any single signal such as high posting frequency alone — high-volume human journalists and activists exist
- Do not present bot classifications as definitive facts; always report confidence level and the evidence base
- Do not conflate automation detection with political content moderation — the technique assesses authenticity, not viewpoint
- Do not apply thresholds calibrated for one platform to another without recalibration

## AGEINT upstream
`docs/ageint/information-environment.md`
