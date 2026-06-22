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

- For Red Hat Analysis, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Red Hat Analysis, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Red Hat Analysis recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Red Hat Analysis: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Red Hat Analysis: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Red Hat Analysis: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Red Hat Analysis cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Red Hat Analysis should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Red Hat Analysis, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Red Hat Analysis, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Red Hat Analysis, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Red Hat Analysis failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Red Hat Analysis failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Red Hat Analysis failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Red Hat Analysis to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Red Hat Analysis into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Red Hat Analysis to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- reason from inside the adversary's frame, not from yours — their logic must be coherent given their values, not ours
- use the adversary's own stated goals, doctrinal documents, and behavioral history as primary anchors, not inferred intent
- distinguish between what the adversary wants, what they believe, and what they can do — collapsing these produces mirror imaging
- the most dangerous course of action is not necessarily the most probable; both must be separately assessed
