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

- For Structured Literature Synthesis, tie each synthesis briefing, and evidence table claim to concrete evidence from the specific synthesis question, sources, and inclusion criteria item, source excerpt, observation, or command result that supports it.
- For Structured Literature Synthesis, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the synthesis briefing.
- Before recommending any Structured Literature Synthesis action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Structured Literature Synthesis: the synthesis briefing is supported by multiple independent study designs, source quality, reproducibility artifacts, and uncertainty records; define the synthesis question and scope and gather and deduplicate sources checks agree, and no unresolved contradiction would change the result.
- Medium for Structured Literature Synthesis: the synthesis briefing is plausible, but one important synthesis question source, comparison case, or alternative explanation remains incomplete.
- Low for Structured Literature Synthesis: the synthesis briefing rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Structured Literature Synthesis cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating research_methods evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Structured Literature Synthesis, use only authorized synthesis question, sources, and inclusion criteria, public or source-approved records, and caller-provided context needed for the defensive task.
- For Structured Literature Synthesis, minimize person-level detail in the synthesis briefing; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Structured Literature Synthesis, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Structured Literature Synthesis: treating synthesis question as complete when define the synthesis question and scope and gather and deduplicate sources checks or contradictory evidence are missing.
- Structured Literature Synthesis: producing advice that would help a requester cherry-pick sources, fabricate citations, or overstate certainty from weak evidence.
- Structured Literature Synthesis: reporting the synthesis briefing without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Structured Literature Synthesis outputs to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the synthesis briefing from Structured Literature Synthesis into an operational playbook to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Structured Literature Synthesis to synthesize supplied or authorized sources with explicit confidence and uncertainty labels with synthesis question, sources, and inclusion criteria' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- **Traceability.** Every synthesized statement maps back to specific sources.
- **Honest conflict.** When sources disagree, the disagreement is reported as a
- **Evidence grading.** Each theme carries an explicit strength grade
