# Workflow — Prebunking & Inoculation Design

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Characterize the technique and audience (read)
Ingest the manipulation technique specification and audience profile. Identify: (a) which psychological lever the technique exploits (fear, tribal identity, authority, scarcity, social proof); (b) the audience's prior exposure to this technique and their baseline attitudes; (c) any deployment constraints (format, channel, length, language register).

## Step 2 — Select inoculation structure and dose (reason)
Choose between technique-based inoculation (names and explains the rhetorical move, domain-agnostic, better generalization) and issue-based inoculation (refutes a specific claim directly, faster but topic-locked). Calibrate the weakened-dose example: it must be identifiable as the real technique without being persuasive. Determine refutation strategy: for technique-based, provide a worked deconstruction; for issue-based, provide a factual correction with source. Identify whether the audience motivation state is likely to be hot (aroused, fast) or cold (deliberative) at deployment time, and adjust format accordingly.

## Step 3 — Draft the inoculation content (write)
Write the inoculation message in this sequence: (1) Explicit warning — name the technique and state it will be used to mislead; (2) Weakened-dose example — show a mild instance of the technique in action; (3) Refutation — explain why the technique is misleading and what the legitimate version looks like; (4) Call to action — give the audience a specific recognition or verification behavior to practice. Keep language at audience literacy level. Flag emotional trigger points that require extra care not to model the technique being refuted.

## Step 4 — Produce efficacy-check items and design rationale (write)
Write 3–5 test items that probe resistance: recognition prompts (can the audience spot the technique in a novel example?), attitudinal probes (has their confidence in the technique's persuasiveness decreased?), and behavioral probes (will they share content using this technique?). Document design choices and their evidence base in the design rationale output.

## Evidence requirements
- For Prebunking & Inoculation Design, tie each inoculation content, efficacy check items, and design rationale claim to concrete evidence from the specific manipulation technique, target audience, and deployment context item, source excerpt, observation, or command result that supports it.
- For Prebunking & Inoculation Design, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the inoculation content.
- Before recommending any Prebunking & Inoculation Design action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Prebunking & Inoculation Design: the inoculation content is supported by multiple independent content, behavioral, narrative, media, and audience-risk evidence; characterize the technique and audience and select inoculation structure and dose checks agree, and no unresolved contradiction would change the result.
- Medium for Prebunking & Inoculation Design: the inoculation content is plausible, but one important manipulation technique source, comparison case, or alternative explanation remains incomplete.
- Low for Prebunking & Inoculation Design: the inoculation content rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Prebunking & Inoculation Design cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating cognitive_security evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Prebunking & Inoculation Design, use only authorized manipulation technique, target audience, and deployment context, public or source-approved records, and caller-provided context needed for the defensive task.
- For Prebunking & Inoculation Design, minimize person-level detail in the inoculation content; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Prebunking & Inoculation Design, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Prebunking & Inoculation Design: treating manipulation technique as complete when characterize the technique and audience and select inoculation structure and dose checks or contradictory evidence are missing.
- Prebunking & Inoculation Design: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Prebunking & Inoculation Design: reporting the inoculation content without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Prebunking & Inoculation Design outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the inoculation content from Prebunking & Inoculation Design into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Prebunking & Inoculation Design to assess supplied material for manipulation indicators and recommend resilience measures with manipulation technique, target audience, and deployment context' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not model the manipulation technique so vividly in the weakened dose that it functions as actual persuasion — dose calibration is non-negotiable
- do not produce generic 'think before you share' messaging without tying it to a specific named technique and refutation
- do not ignore attitudinal backlash risk: audiences who feel lectured or patronized may reactively increase trust in the technique being inoculated against
- do not skip efficacy-check items — untested inoculation content has unknown resistance-transfer and may provide false assurance

## AGEINT upstream
`docs/ageint/cognitive-security.md`
