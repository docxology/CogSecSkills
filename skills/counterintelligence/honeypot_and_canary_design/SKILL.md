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

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- A canary is only as valuable as the fidelity of its alert — design the notification path before the decoy, not after
- Placement must be plausible: a fake credentials file in an implausible location teaches attackers nothing and alerts on legitimate discovery
- No legitimate user should ever access the decoy — design its naming, location, and context so only adversarial access is likely
- Always obtain legal and policy sign-off before deployment; canary design in employee-accessible systems carries entrapment and labor-law considerations
