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

## Failure modes
- Honeypot & Canary Design failure: turning defensive tradecraft recognition into operational evasion advice.
- Honeypot & Canary Design failure: producing guidance that would help a requester evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft.
- Honeypot & Canary Design failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Honeypot & Canary Design to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Honeypot & Canary Design into an operational playbook to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Honeypot & Canary Design to review supplied interactions or processes for deception, elicitation, or insider-risk indicators' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not include guidance for offensive deception operations — all designs here are strictly defensive detection tools
- Do not design decoys whose triggering event could be caused by routine legitimate activity — false positives degrade trust in the alert system
- Do not omit the legal review checklist — deploying honeypots in employee-accessible environments without policy and legal clearance can create liability
- Do not treat a triggered canary as conclusive attribution without corroborating evidence — a beacon callback confirms access, not necessarily identity

## AGEINT upstream
`docs/ageint/counterintelligence.md`
