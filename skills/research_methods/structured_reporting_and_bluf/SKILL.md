---
name: research_methods.structured_reporting_and_bluf
description: Write findings bottom-line-up-front with traceable evidence and stated confidence.
---

# Structured Reporting & BLUF

Structured Reporting with Bottom-Line-Up-Front (BLUF) is an analytic communication standard that places the key judgment and its confidence level in the first sentence or paragraph, then supports it with traceable evidence, clearly stated assumptions, and logical argumentation in descending order of importance. Originating in military and intelligence tradecraft and codified in intelligence community analytic standards (ICD 203, ODNI), BLUF prevents the common failure mode in which important caveats or contrary evidence are buried where decision-makers never read them. The structure enforces accountability by requiring each claim in the body to be traceable to a specific source or assumption stated explicitly.

## When to use

- when delivering any analytic product that will inform a decision by someone who may not read past the first paragraph
- when accountability requires every claim to be traceable to a source or stated assumption
- when communicating to mixed audiences who need the bottom line but may want to drill into supporting evidence
- when drafting an assessment that will be challenged, peer reviewed, or used as a record

## What it produces

- a structured report beginning with the key judgment and confidence level
- a body in which every claim is traceable to a specific source or explicitly stated assumption
- a caveats section that surfaces disconfirming evidence and conditions under which the judgment would change
- an implications section tailored to the audience's decision context

## Defensive boundary

Use Structured Reporting & BLUF only for research-methods and synthesis integrity: recognize, assess, document, or defend reproducibility, calibrated confidence, and transparent synthesis. Do not use this skill to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence.

## Misuse redirect

If a request asks Structured Reporting & BLUF to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence, refuse that path and redirect to the safe defensive form: synthesize supplied or authorized sources with explicit confidence and uncertainty labels.

## Evidence discipline

- For Structured Reporting & BLUF, bind each finding to a labeled source — study designs, source quality, reproducibility artifacts, and uncertainty records, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Structured Reporting & BLUF, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Structured Reporting & BLUF recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Structured Reporting & BLUF: independent lines of study designs, source quality, reproducibility artifacts, and uncertainty records converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Structured Reporting & BLUF: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Structured Reporting & BLUF: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Structured Reporting & BLUF cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Structured Reporting & BLUF should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Structured Reporting & BLUF, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Structured Reporting & BLUF, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Structured Reporting & BLUF, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Structured Reporting & BLUF failure: collapsing heterogeneous evidence into an unsupported single confident conclusion.
- Structured Reporting & BLUF failure: producing guidance that would help a requester cherry-pick sources, fabricate citations, or overstate certainty from weak evidence.
- Structured Reporting & BLUF failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Structured Reporting & BLUF to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Structured Reporting & BLUF into an operational playbook to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Structured Reporting & BLUF to synthesize supplied or authorized sources with explicit confidence and uncertainty labels' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- the BLUF must be self-sufficient — a reader who stops after one paragraph should have the judgment, its confidence level, and the single most important caveat
- every factual claim in the body must cite a source or be labeled as an assumption — unlabeled inferences are invisible liabilities
- caveats and countervailing evidence belong in the report body, not as an afterthought or footnote
- descending order of importance: each paragraph should matter less than the one before it, so truncation at any point leaves the most important content intact
