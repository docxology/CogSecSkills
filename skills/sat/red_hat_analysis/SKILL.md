---
name: sat.red_hat_analysis
description: Model an adversary's perceptions and likely decisions from their frame, not yours.
---

# Red Hat Analysis

Red Hat Analysis (also called Red Team Perspective or Enemy-Think) requires the analyst to step fully inside an adversary's worldview — their goals, constraints, organizational culture, decision calculus, and risk tolerance — and reason forward from that frame rather than projecting one's own. The purpose is to anticipate adversary actions, identify exploitable vulnerabilities, and avoid the mirror-imaging error of assuming the adversary thinks and values as we do. In cognitive-security contexts it also surfaces how adversaries model and manipulate target audiences, revealing influence vectors that mirror-imaging would hide.

## When to use

- the analytic question involves predicting or understanding adversary decisions, intentions, or influence operations
- there is risk of mirror imaging — projecting own values, risk tolerance, or decision logic onto a culturally or ideologically distinct actor
- assessing how an adversary perceives and will respond to a signal, policy, or action
- identifying which cognitive vulnerabilities or information gaps an adversary is likely to exploit in a target audience

## What it produces

- a structured adversary worldview profile covering goals, constraints, culture, and decision calculus
- ranked adversary courses of action with internal reasoning chains from the adversary's perspective
- explicit mirror-imaging flags — places where current analysis assumes adversary rationality matches our own

## Defensive boundary

Use Red Hat Analysis only for structured analytic technique support: recognize, assess, document, or defend analytic rigor, alternative hypotheses, and calibrated judgment. Do not use this skill to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.

## Misuse redirect

If a request asks Red Hat Analysis to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation, refuse that path and redirect to the safe defensive form: apply the structured technique to supplied evidence while preserving alternatives and uncertainty.

## Evidence discipline

- For Red Hat Analysis, tie each adversary frame, courses of action, and mirror imaging flags claim to concrete evidence from the specific adversary profile, situation context, and analytic question item, source excerpt, observation, or command result that supports it.
- For Red Hat Analysis, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the adversary frame.
- Before recommending any Red Hat Analysis action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Red Hat Analysis: the adversary frame is supported by multiple independent hypotheses, assumptions, indicators, evidence tables, and confidence notes; build the adversary frame and develop adversary courses of action checks agree, and no unresolved contradiction would change the result.
- Medium for Red Hat Analysis: the adversary frame is plausible, but one important adversary profile source, comparison case, or alternative explanation remains incomplete.
- Low for Red Hat Analysis: the adversary frame rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Red Hat Analysis cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Red Hat Analysis, use only authorized adversary profile, situation context, and analytic question, public or source-approved records, and caller-provided context needed for the defensive task.
- For Red Hat Analysis, minimize person-level detail in the adversary frame; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Red Hat Analysis, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Red Hat Analysis: treating adversary profile as complete when build the adversary frame and develop adversary courses of action checks or contradictory evidence are missing.
- Red Hat Analysis: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Red Hat Analysis: reporting the adversary frame without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Red Hat Analysis outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the adversary frame from Red Hat Analysis into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Red Hat Analysis to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with adversary profile, situation context, and analytic question' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- reason from inside the adversary's frame, not from yours — their logic must be coherent given their values, not ours
- use the adversary's own stated goals, doctrinal documents, and behavioral history as primary anchors, not inferred intent
- distinguish between what the adversary wants, what they believe, and what they can do — collapsing these produces mirror imaging
- the most dangerous course of action is not necessarily the most probable; both must be separately assessed
