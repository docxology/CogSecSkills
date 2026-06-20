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

## Evidence requirements
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

## Failure modes
- Honeypot & Canary Design: treating threat model as complete when review threat model and coverage gaps and select decoy types and placement checks or contradictory evidence are missing.
- Honeypot & Canary Design: producing advice that would help a requester evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft.
- Honeypot & Canary Design: reporting the canary design spec without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Honeypot & Canary Design outputs to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the canary design spec from Honeypot & Canary Design into an operational playbook to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Honeypot & Canary Design to review supplied interactions or processes for deception, elicitation, or insider-risk indicators with threat model, asset inventory, and monitoring coverage' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not include guidance for offensive deception operations — all designs here are strictly defensive detection tools
- Do not design decoys whose triggering event could be caused by routine legitimate activity — false positives degrade trust in the alert system
- Do not omit the legal review checklist — deploying honeypots in employee-accessible environments without policy and legal clearance can create liability
- Do not treat a triggered canary as conclusive attribution without corroborating evidence — a beacon callback confirms access, not necessarily identity

## AGEINT upstream
`docs/ageint/counterintelligence.md`
