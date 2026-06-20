---
name: counterintelligence.honeypot_and_canary_design
description: Design canary tokens and decoys to detect probing and exfiltration (defensive).
---

# Honeypot & Canary Design

Honeypot and canary design is a defensive counterintelligence technique for creating plausible decoy assets — files, credentials, data records, or network services — that have no legitimate operational use and whose access or exfiltration triggers a high-fidelity alert. Canary tokens are lightweight tripwires (unique URLs, document beacons, fake credentials) embedded in legitimate-looking material so that any adversary who accesses them reveals their presence and, often, attribution data. This skill covers the threat-model-driven selection, placement, and monitoring of such deceptions, strictly for detecting probing and unauthorized access rather than entrapment.

## When to use

- When threat modeling identifies a realistic risk of unauthorized access or data exfiltration and existing detection coverage has blind spots
- When insider risk is a concern and behavioral monitoring alone is insufficient
- When designing a defense-in-depth strategy that supplements perimeter and endpoint controls with deception-based tripwires
- After a suspected breach where attribution and scope confirmation are needed without tipping off the adversary

## What it produces

- A prioritized set of decoy types (canary documents, fake credentials, honeypot services) with threat-model justification for each
- Placement specifications that maximize the probability an adversary encounters the decoy while minimizing false-positive access by legitimate users
- Alert logic and response playbook for each tripwire type
- A legal, ethical, and HR-review checklist addressing jurisdiction, entrapment concerns, and authorized-use policy

## Defensive boundary

Use Honeypot & Canary Design only for counterintelligence and analytic-process defense: recognize, assess, document, or defend analytic teams, collection processes, and institutional trust boundaries. Do not use this skill to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft.

## Misuse redirect

If a request asks Honeypot & Canary Design to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft, refuse that path and redirect to the safe defensive form: review supplied interactions or processes for deception, elicitation, or insider-risk indicators.

## Evidence discipline

- For Honeypot & Canary Design, tie each canary design spec claim to concrete evidence from the specific threat model, asset inventory, and monitoring coverage item, source excerpt, observation, or command result that supports it.
- For Honeypot & Canary Design, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the canary design spec.
- Before recommending any Honeypot & Canary Design action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Honeypot & Canary Design: the canary design spec is supported by multiple independent interaction records, process artifacts, deception indicators, and alternative explanations; review threat model and coverage gaps and select decoy types and placement checks agree, and no unresolved contradiction would change the result.
- Medium for Honeypot & Canary Design: the canary design spec is plausible, but one important threat model source, comparison case, or alternative explanation remains incomplete.
- Low for Honeypot & Canary Design: the canary design spec rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Honeypot & Canary Design cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating counterintelligence evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Honeypot & Canary Design, use only authorized threat model, asset inventory, and monitoring coverage, public or source-approved records, and caller-provided context needed for the defensive task.
- For Honeypot & Canary Design, minimize person-level detail in the canary design spec; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Honeypot & Canary Design, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Honeypot & Canary Design: treating threat model as complete when review threat model and coverage gaps and select decoy types and placement checks or contradictory evidence are missing.
- Honeypot & Canary Design: producing advice that would help a requester evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft.
- Honeypot & Canary Design: reporting the canary design spec without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Honeypot & Canary Design outputs to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the canary design spec from Honeypot & Canary Design into an operational playbook to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Honeypot & Canary Design to review supplied interactions or processes for deception, elicitation, or insider-risk indicators with threat model, asset inventory, and monitoring coverage' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- A canary is only as valuable as the fidelity of its alert — design the notification path before the decoy, not after
- Placement must be plausible: a fake credentials file in an implausible location teaches attackers nothing and alerts on legitimate discovery
- No legitimate user should ever access the decoy — design its naming, location, and context so only adversarial access is likely
- Always obtain legal and policy sign-off before deployment; canary design in employee-accessible systems carries entrapment and labor-law considerations
