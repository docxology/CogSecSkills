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
- For Structured Literature Synthesis, map every synthesized statement, theme grade, and reported conflict to concrete evidence in the per-claim evidence table — a specific source citation with its quality grade — and treat any uncited statement or unanswered question as a labelled gap rather than a supported finding.
- For Structured Literature Synthesis, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the synthesis briefing.
- Before recommending any Structured Literature Synthesis action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Structured Literature Synthesis: the BLUF briefing rests on a well-scoped synthesis question, the corpus is deduplicated so mirrors are not counted as independent agreement, every themed statement traces to a graded source in the evidence table, conflicts and gaps are reported rather than smoothed, and the dominant theme grades would not flip if any single source were removed.
- Medium for Structured Literature Synthesis: the synthesis briefing is plausible, but one important synthesis question source, comparison case, or alternative explanation remains incomplete.
- Low for Structured Literature Synthesis: the synthesis briefing rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Structured Literature Synthesis cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating research_methods evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Structured Literature Synthesis, use only authorized synthesis question, sources, and inclusion criteria, public or source-approved records, and caller-provided context needed for the defensive task.
- For Structured Literature Synthesis, minimize person-level detail in the synthesis briefing; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Structured Literature Synthesis, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Structured Literature Synthesis: presenting one source's claim as settled consensus, double-counting duplicate or reprinted studies as convergent support, smoothing over conflicting findings, or synthesizing beyond what the sources support, so the briefing reads as authoritative while resting on an incomplete or non-independent corpus.
- Structured Literature Synthesis: producing advice that would help a requester cherry-pick sources, fabricate citations, or overstate certainty from weak evidence.
- Structured Literature Synthesis: reporting the synthesis briefing without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Structured Literature Synthesis outputs to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the synthesis briefing from Structured Literature Synthesis into an operational playbook to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Structured Literature Synthesis to synthesize supplied or authorized sources with explicit confidence and uncertainty labels with synthesis question, sources, and inclusion criteria' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do **not** present a single source's claim as settled consensus.
- Do **not** hide or smooth over conflicting findings.
- Do **not** synthesize beyond what the sources support.
- Do **not** drop citations — no uncited statement in the briefing.
- Do **not** double-count duplicate sources as independent agreement.

## AGEINT upstream
`docs/ageint/research-methods.md`
