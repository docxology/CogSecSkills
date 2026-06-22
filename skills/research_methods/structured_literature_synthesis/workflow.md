# Workflow — Structured Literature Synthesis

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Define the synthesis question and scope (reason, write)
State the single question the synthesis must answer and write explicit inclusion/exclusion criteria for source type, recency, language, relevance, and quality thresholds.

## Step 2 — Gather and deduplicate sources (search, web, read)
Collect candidate sources where permitted, remove duplicate studies, mirrors, and reprints, and record what was excluded and why.

## Step 3 — Extract claims and findings per source (read, reason)
For each retained source, extract concrete claims, citations, tight paraphrases or necessary quotes, and a per-source quality grade.

## Step 4 — Cluster findings by theme (reason)
Group extracted claims into themes relevant to the synthesis question while preserving citation traceability for each claim.

## Step 5 — Identify agreements, conflicts, and gaps (reason)
Mark where sources converge, where they conflict, and what the corpus does not answer. Treat gaps as first-class findings.

## Step 6 — Grade strength of evidence per theme (reason)
Apply the evidence-strength rubric to each theme as a whole, weighing source count, quality, independence, and consistency.

## Step 7 — Write the BLUF synthesis (write)
Put the bottom line up front, then present themes, evidence grades, conflicts, gaps, and full citations with every synthesized statement traceable to the evidence table.

## Evidence requirements
- For Structured Literature Synthesis, bind each finding to a labeled source — study designs, source quality, reproducibility artifacts, and uncertainty records, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Structured Literature Synthesis, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Structured Literature Synthesis recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Structured Literature Synthesis: independent lines of study designs, source quality, reproducibility artifacts, and uncertainty records converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Structured Literature Synthesis: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Structured Literature Synthesis: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Structured Literature Synthesis cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Structured Literature Synthesis should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Structured Literature Synthesis, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Structured Literature Synthesis, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Structured Literature Synthesis, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Structured Literature Synthesis failure: collapsing heterogeneous evidence into an unsupported single confident conclusion.
- Structured Literature Synthesis failure: producing guidance that would help a requester cherry-pick sources, fabricate citations, or overstate certainty from weak evidence.
- Structured Literature Synthesis failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Structured Literature Synthesis to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Structured Literature Synthesis into an operational playbook to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Structured Literature Synthesis to synthesize supplied or authorized sources with explicit confidence and uncertainty labels' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do **not** present a single source's claim as settled consensus.
- Do **not** hide or smooth over conflicting findings.
- Do **not** synthesize beyond what the sources support.
- Do **not** drop citations — no uncited statement in the briefing.
- Do **not** double-count duplicate sources as independent agreement.

## AGEINT upstream
`docs/ageint/research-methods.md`
