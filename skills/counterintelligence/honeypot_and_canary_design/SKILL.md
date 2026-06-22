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

- For Honeypot & Canary Design, bind each finding to a labeled source — interaction records, process artifacts, deception indicators, and alternative explanations, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Honeypot & Canary Design, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Honeypot & Canary Design recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Honeypot & Canary Design: independent lines of interaction records, process artifacts, deception indicators, and alternative explanations converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Honeypot & Canary Design: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Honeypot & Canary Design: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Honeypot & Canary Design cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Honeypot & Canary Design should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Honeypot & Canary Design, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Honeypot & Canary Design, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Honeypot & Canary Design, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Honeypot & Canary Design failure: turning defensive tradecraft recognition into operational evasion advice.
- Honeypot & Canary Design failure: producing guidance that would help a requester evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft.
- Honeypot & Canary Design failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Honeypot & Canary Design to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Honeypot & Canary Design into an operational playbook to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Honeypot & Canary Design to review supplied interactions or processes for deception, elicitation, or insider-risk indicators' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- A canary is only as valuable as the fidelity of its alert — design the notification path before the decoy, not after
- Placement must be plausible: a fake credentials file in an implausible location teaches attackers nothing and alerts on legitimate discovery
- No legitimate user should ever access the decoy — design its naming, location, and context so only adversarial access is likely
- Always obtain legal and policy sign-off before deployment; canary design in employee-accessible systems carries entrapment and labor-law considerations
