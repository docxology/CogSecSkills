# Workflow — Coordinated Inauthentic Behavior Detection

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Build the co-activity matrix (read)
Ingest the activity dataset and compute pairwise co-activity scores: how often any two accounts post about the same content within a defined time window (e.g. 60 seconds, 5 minutes). Also compute content-reuse similarity (near-duplicate detection on post text) and shared amplification targets (who they retweet or link to).

## Step 2 — Cross-reference prior CIB reports and known networks (search)
Search existing CIB takedown reports (Meta, Twitter/X archived reports, DFRLab, Stanford Internet Observatory) for account overlaps, infrastructure overlaps, or behavioral signatures matching the current dataset.

## Step 3 — Cluster and characterize coordination (reason)
Apply graph community detection or hierarchical clustering to the co-activity matrix. For each cluster exceeding a minimum size threshold, characterize the dominant coordination type: relay amplification, synchronized posting, content templating, or cross-platform bridging. Score each cluster on three independent axes — timing, content, and network — and require convergence on at least two for a CIB assessment.

## Step 4 — Estimate reach, assess confidence, and write report (reason, write)
Estimate the cumulative reach of coordinated content (impressions, shares) and the amplification multiplier relative to organic baseline. Assess confidence for each cluster and overall. Document methodology, evidence, confidence, false-positive risk factors, and alternative explanations considered. Enumerate recommended actions: investigation expansion, counter-narrative options, or platform reporting.

## Evidence requirements
- For Coordinated Inauthentic Behavior Detection, bind each finding to a labeled source — platform observations, coordination signals, narrative movement, automation signals, and provenance data, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Coordinated Inauthentic Behavior Detection, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Coordinated Inauthentic Behavior Detection recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Coordinated Inauthentic Behavior Detection: independent lines of platform observations, narrative movement, automation signals, and provenance data converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Coordinated Inauthentic Behavior Detection: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Coordinated Inauthentic Behavior Detection: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Coordinated Inauthentic Behavior Detection cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Coordinated Inauthentic Behavior Detection should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Coordinated Inauthentic Behavior Detection, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Coordinated Inauthentic Behavior Detection, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Coordinated Inauthentic Behavior Detection, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Coordinated Inauthentic Behavior Detection failure: treating engagement volume as proof of authenticity or coordinated intent.
- Coordinated Inauthentic Behavior Detection failure: producing guidance that would help a requester amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement.
- Coordinated Inauthentic Behavior Detection failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Coordinated Inauthentic Behavior Detection to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Coordinated Inauthentic Behavior Detection into an operational playbook to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Coordinated Inauthentic Behavior Detection to map supplied narratives, automation signals, or platform affordance risks for defensive review' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not equate shared political viewpoint or hashtag use with coordination — organic movements also amplify common narratives
- Do not attribute coordination to a specific actor or state without a separate, independent attribution evidence chain
- Do not report a CIB finding with binary confidence; always express confidence level and enumerate alternative explanations
- Do not use the technique to target or suppress authentic grassroots activity that happens to be synchronized by external events

## AGEINT upstream
`docs/ageint/information-environment.md`
