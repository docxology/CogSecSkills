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

- For Cognitive Bias Audit, bind each identified bias to concrete evidence — a quoted passage, a stated assumption, or a described organizational pressure — pair it with a debiasing action the analyst can actually implement, and note explicitly what text-based auditing cannot reveal without observing the analytic process itself.
- For Cognitive Bias Audit, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the bias audit report.
- Before recommending any Cognitive Bias Audit action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Cognitive Bias Audit: each flagged bias is anchored to a quoted passage from the analysis under review, its distortion magnitude is calibrated against domain stakes and logical path-dependence rather than asserted uniformly, the prioritized ranking is stable across the bias taxonomy, and no unresolved contradiction would change the recommended debiasing actions.
- Medium for Cognitive Bias Audit: the bias audit report is plausible, but one important analysis or decision source, comparison case, or alternative explanation remains incomplete.
- Low for Cognitive Bias Audit: the bias audit report rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Cognitive Bias Audit cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating cognitive_security evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Cognitive Bias Audit, use only authorized analysis or decision, domain context, and known pressures, public or source-approved records, and caller-provided context needed for the defensive task.
- For Cognitive Bias Audit, minimize person-level detail in the bias audit report; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Cognitive Bias Audit, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Cognitive Bias Audit: asserting a bias without quoting the text that shows it, rating every bias as high severity, or conflating cognitive bias with deliberate deception, so the catalogue lectures abstractly instead of making specific, calibrated, actionable bias intrusions visible to the analyst.
- Cognitive Bias Audit: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Cognitive Bias Audit: reporting the bias audit report without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Cognitive Bias Audit outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the bias audit report from Cognitive Bias Audit into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Cognitive Bias Audit to assess supplied material for manipulation indicators and recommend resilience measures with analysis or decision, domain context, and known pressures' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- name the bias specifically — 'anchoring on the first figure cited' not 'analyst may be biased'
- quote the text that shows the bias; do not assert bias without textual evidence
- distinguish between cognitive bias (systematic error in judgment) and random error or deliberate framing
- rate distortion magnitude by domain stakes and logical path-dependence, not by how uncomfortable the bias sounds
- pair every identified bias with a debiasing action that is actually feasible for this analyst in this context
- the taxonomy should cover: availability/representativeness/anchoring (heuristic biases), confirmation bias and its variants, mirror-imaging, groupthink and social proof, motivated reasoning and politicization, projection bias, and satisficing
