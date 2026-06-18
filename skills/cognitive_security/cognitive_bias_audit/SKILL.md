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

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- name the bias specifically — 'anchoring on the first figure cited' not 'analyst may be biased'
- quote the text that shows the bias; do not assert bias without textual evidence
- distinguish between cognitive bias (systematic error in judgment) and random error or deliberate framing
- rate distortion magnitude by domain stakes and logical path-dependence, not by how uncomfortable the bias sounds
- pair every identified bias with a debiasing action that is actually feasible for this analyst in this context
- the taxonomy should cover: availability/representativeness/anchoring (heuristic biases), confirmation bias and its variants, mirror-imaging, groupthink and social proof, motivated reasoning and politicization, projection bias, and satisficing
