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

## Evidence requirements
- For Bot & Automation Detection, tie each account classifications, and detection report claim to concrete evidence from the specific account data, and context item, source excerpt, observation, or command result that supports it.
- For Bot & Automation Detection, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the account classifications.
- Before recommending any Bot & Automation Detection action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Bot & Automation Detection: the account classifications is supported by multiple independent platform observations, narrative movement, automation signals, and provenance data; ingest and profile accounts and cross-reference known indicators checks agree, and no unresolved contradiction would change the result.
- Medium for Bot & Automation Detection: the account classifications is plausible, but one important account data source, comparison case, or alternative explanation remains incomplete.
- Low for Bot & Automation Detection: the account classifications rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Bot & Automation Detection cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating information_environment evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Bot & Automation Detection, use only authorized account data, and context, public or source-approved records, and caller-provided context needed for the defensive task.
- For Bot & Automation Detection, minimize person-level detail in the account classifications; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Bot & Automation Detection, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Bot & Automation Detection: treating account data as complete when ingest and profile accounts and cross-reference known indicators checks or contradictory evidence are missing.
- Bot & Automation Detection: producing advice that would help a requester amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement.
- Bot & Automation Detection: reporting the account classifications without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Bot & Automation Detection outputs to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the account classifications from Bot & Automation Detection into an operational playbook to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Bot & Automation Detection to map supplied narratives, automation signals, or platform affordance risks for defensive review with account data, and context' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not classify an account as a bot based on any single signal such as high posting frequency alone — high-volume human journalists and activists exist
- Do not present bot classifications as definitive facts; always report confidence level and the evidence base
- Do not conflate automation detection with political content moderation — the technique assesses authenticity, not viewpoint
- Do not apply thresholds calibrated for one platform to another without recalibration

## AGEINT upstream
`docs/ageint/information-environment.md`
