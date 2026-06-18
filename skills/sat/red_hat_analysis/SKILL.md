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

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- reason from inside the adversary's frame, not from yours — their logic must be coherent given their values, not ours
- use the adversary's own stated goals, doctrinal documents, and behavioral history as primary anchors, not inferred intent
- distinguish between what the adversary wants, what they believe, and what they can do — collapsing these produces mirror imaging
- the most dangerous course of action is not necessarily the most probable; both must be separately assessed
