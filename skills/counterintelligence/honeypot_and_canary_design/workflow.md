# Workflow — Honeypot & Canary Design

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Review threat model and coverage gaps (read)
Ingest the threat model and existing monitoring coverage. Identify the attacker's most likely access paths and the assets they would plausibly seek. Note gaps where an adversary could operate undetected.

## Step 2 — Select decoy types and placement (reason)
For each coverage gap, select an appropriate decoy class: canary tokens (URL beacons embedded in documents), fake credential pairs, honeypot network services, dummy database tables, or decoy user accounts. Evaluate each candidate against the plausibility test: would a real adversary seeking real intelligence access this? Would a legitimate user ever encounter it? Prioritize decoys that pass both tests.

## Step 3 — Design alert logic and response playbook (reason)
For each decoy, specify the triggering event (HTTP callback, credential use attempt, login, query), the logging destination, the notification mechanism and recipient, and the immediate response steps. Ensure the response plan does not expose the detection mechanism to the adversary.

## Step 4 — Produce design specification and legal checklist (write)
Write the full canary/honeypot design specification covering: decoy inventory with placement rationale, alert logic per decoy, response playbook, naming and access-control requirements, and a legal/ethical review checklist addressing entrapment exposure, employee-monitoring law, authorized-use policies, and required sign-offs before deployment.

## Anti-criteria (must NOT happen)
- Do not include guidance for offensive deception operations — all designs here are strictly defensive detection tools
- Do not design decoys whose triggering event could be caused by routine legitimate activity — false positives degrade trust in the alert system
- Do not omit the legal review checklist — deploying honeypots in employee-accessible environments without policy and legal clearance can create liability
- Do not treat a triggered canary as conclusive attribution without corroborating evidence — a beacon callback confirms access, not necessarily identity

## AGEINT upstream
`docs/ageint/counterintelligence.md`
