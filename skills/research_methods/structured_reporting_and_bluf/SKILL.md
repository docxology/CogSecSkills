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

- For Structured Reporting & BLUF, ensure every claim in the body is backed by concrete evidence — a cited source or an explicitly stated assumption — so that unlabeled inferences become visible, and verify the BLUF, caveats, and 'what would change this assessment' note all rest on that same traceable evidence rather than unsupported assertion.
- For Structured Reporting & BLUF, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the structured report.
- Before recommending any Structured Reporting & BLUF action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Structured Reporting & BLUF: the bottom-line judgment and its standardized confidence label appear first and accurately summarize the body, every factual claim is traceable to a cited source or an explicitly labeled assumption, the caveats section surfaces the conditions that would most change the judgment, and headline and supporting argument contain no contradiction a reader would catch.
- Medium for Structured Reporting & BLUF: the structured report is plausible, but one important analytic judgment source, comparison case, or alternative explanation remains incomplete.
- Low for Structured Reporting & BLUF: the structured report rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Structured Reporting & BLUF cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating research_methods evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Structured Reporting & BLUF, use only authorized analytic judgment, evidence and sources, and assumptions, public or source-approved records, and caller-provided context needed for the defensive task.
- For Structured Reporting & BLUF, minimize person-level detail in the structured report; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Structured Reporting & BLUF, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Structured Reporting & BLUF: burying the key judgment in a narrative-reveal structure, stating confidence verbally without a standardized tier, omitting countervailing evidence to protect the headline, or letting the BLUF drift out of sync with the body, so a decision-maker who reads only the first paragraph receives a distorted or unsupported conclusion.
- Structured Reporting & BLUF: producing advice that would help a requester cherry-pick sources, fabricate citations, or overstate certainty from weak evidence.
- Structured Reporting & BLUF: reporting the structured report without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Structured Reporting & BLUF outputs to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the structured report from Structured Reporting & BLUF into an operational playbook to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Structured Reporting & BLUF to synthesize supplied or authorized sources with explicit confidence and uncertainty labels with analytic judgment, evidence and sources, and assumptions' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- the BLUF must be self-sufficient — a reader who stops after one paragraph should have the judgment, its confidence level, and the single most important caveat
- every factual claim in the body must cite a source or be labeled as an assumption — unlabeled inferences are invisible liabilities
- caveats and countervailing evidence belong in the report body, not as an afterthought or footnote
- descending order of importance: each paragraph should matter less than the one before it, so truncation at any point leaves the most important content intact
