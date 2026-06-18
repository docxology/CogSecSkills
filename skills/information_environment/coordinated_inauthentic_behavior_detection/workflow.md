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

## Anti-criteria (must NOT happen)
- Do not equate shared political viewpoint or hashtag use with coordination — organic movements also amplify common narratives
- Do not attribute coordination to a specific actor or state without a separate, independent attribution evidence chain
- Do not report a CIB finding with binary confidence; always express confidence level and enumerate alternative explanations
- Do not use the technique to target or suppress authentic grassroots activity that happens to be synchronized by external events

## AGEINT upstream
`docs/ageint/information-environment.md`
