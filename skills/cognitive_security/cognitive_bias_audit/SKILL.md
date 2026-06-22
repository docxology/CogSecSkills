---
name: cognitive_security.cognitive_bias_audit
description: Scan an analysis or decision for the specific biases most likely to distort it.
---

# Cognitive Bias Audit

Cognitive Bias Audit applies a structured checklist of well-documented cognitive biases — drawn from the intelligence analysis, behavioral economics, and judgment-and-decision-making literature — to a specific analysis or decision to identify which biases are most likely operating and how they may be distorting conclusions. The technique is derived from Richards Heuer's work on structured analytic techniques and Kahneman's dual-process research, adapted for defensive intelligence and cognitive-security contexts. It produces a prioritized catalogue of probable bias intrusions with targeted debiasing actions, not a generic lecture on bias. The goal is making bias visible and actionable rather than abstractly warning analysts that biases exist.

## When to use

- before finalizing an intelligence estimate or security assessment where consequential decisions follow
- when reviewing a peer's analysis for quality assurance or red-team purposes
- after a significant analytic failure as part of post-mortem — to identify which biases contributed
- when an analysis feels intuitively 'too clean' or converges too quickly on a conclusion
- when analysts have been operating under unusual time pressure, political sensitivity, or group consensus norms

## What it produces

- a named, evidence-grounded catalogue of the specific biases most likely operating in this analysis (not a generic list)
- quoted text from the analysis showing where each bias is visible
- an estimated distortion magnitude (High/Medium/Low) for each bias based on domain and stakes
- a concrete, actionable debiasing step for each identified bias — technique-specific, not generic advice
- a priority ranking so the analyst knows where to focus debiasing effort first

## Defensive boundary

Use Cognitive Bias Audit only for cognitive-security defense: recognize, assess, document, or defend audiences, decision-makers, and public discourse. Do not use this skill to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.

## Misuse redirect

If a request asks Cognitive Bias Audit to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation, refuse that path and redirect to the safe defensive form: assess supplied material for manipulation indicators and recommend resilience measures.

## Evidence discipline

- For Cognitive Bias Audit, bind each finding to a labeled source — content, behavioral, narrative, media, and audience-risk evidence, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Cognitive Bias Audit, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Cognitive Bias Audit recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Cognitive Bias Audit: independent lines of content, behavioral, narrative, media, and audience-risk evidence converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Cognitive Bias Audit: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Cognitive Bias Audit: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Cognitive Bias Audit cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Cognitive Bias Audit should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Cognitive Bias Audit, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Cognitive Bias Audit, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Cognitive Bias Audit, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Cognitive Bias Audit failure: mistaking persuasive resonance for verified harm or intent.
- Cognitive Bias Audit failure: producing guidance that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Cognitive Bias Audit failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Cognitive Bias Audit to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Cognitive Bias Audit into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Cognitive Bias Audit to assess supplied material for manipulation indicators and recommend resilience measures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- name the bias specifically — 'anchoring on the first figure cited' not 'analyst may be biased'
- quote the text that shows the bias; do not assert bias without textual evidence
- distinguish between cognitive bias (systematic error in judgment) and random error or deliberate framing
- rate distortion magnitude by domain stakes and logical path-dependence, not by how uncomfortable the bias sounds
- pair every identified bias with a debiasing action that is actually feasible for this analyst in this context
- the taxonomy should cover: availability/representativeness/anchoring (heuristic biases), confirmation bias and its variants, mirror-imaging, groupthink and social proof, motivated reasoning and politicization, projection bias, and satisficing
