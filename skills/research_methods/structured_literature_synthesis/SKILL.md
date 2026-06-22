---
name: research_methods.structured_literature_synthesis
description: Synthesize a body of sources into a structured, evidence-graded, gap-aware briefing.
---

# Structured Literature Synthesis

Turn a body of sources into a structured, evidence-graded, gap-aware briefing. The method defines a synthesis question with inclusion/exclusion criteria, gathers and deduplicates sources, extracts graded claims with citations, clusters findings by theme, and surfaces agreements, conflicts, and gaps. It produces a BLUF synthesis where every statement traces back to its sources and conflicting evidence is reported honestly rather than smoothed over.

## When to use

- literature synthesis
- synthesize these sources
- what does the research say
- grade the evidence
- where are the gaps in the literature
- structured review of sources

## What it produces

- A **BLUF synthesis briefing**: bottom line up front, then themes with graded
- An **evidence table**: every extracted claim mapped to its source citation and
- An explicit **gap inventory**: questions no source in the corpus answers.

## Defensive boundary

Use Structured Literature Synthesis only for research-methods and synthesis integrity: recognize, assess, document, or defend reproducibility, calibrated confidence, and transparent synthesis. Do not use this skill to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence.

## Misuse redirect

If a request asks Structured Literature Synthesis to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence, refuse that path and redirect to the safe defensive form: synthesize supplied or authorized sources with explicit confidence and uncertainty labels.

## Evidence discipline

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

## Failure modes and negative controls

- Structured Literature Synthesis failure: collapsing heterogeneous evidence into an unsupported single confident conclusion.
- Structured Literature Synthesis failure: producing guidance that would help a requester cherry-pick sources, fabricate citations, or overstate certainty from weak evidence.
- Structured Literature Synthesis failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Structured Literature Synthesis to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Structured Literature Synthesis into an operational playbook to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Structured Literature Synthesis to synthesize supplied or authorized sources with explicit confidence and uncertainty labels' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- **Traceability.** Every synthesized statement maps back to specific sources.
- **Honest conflict.** When sources disagree, the disagreement is reported as a
- **Evidence grading.** Each theme carries an explicit strength grade
