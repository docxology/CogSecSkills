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
- For Prebunking & Inoculation Design, bind each finding to a labeled source — content, behavioral, narrative, media, and audience-risk evidence, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Prebunking & Inoculation Design, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Prebunking & Inoculation Design recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Prebunking & Inoculation Design: independent lines of content, behavioral, narrative, media, and audience-risk evidence converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Prebunking & Inoculation Design: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Prebunking & Inoculation Design: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Prebunking & Inoculation Design cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Prebunking & Inoculation Design should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Prebunking & Inoculation Design, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Prebunking & Inoculation Design, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Prebunking & Inoculation Design, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Prebunking & Inoculation Design failure: mistaking persuasive resonance for verified harm or intent.
- Prebunking & Inoculation Design failure: producing guidance that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Prebunking & Inoculation Design failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Prebunking & Inoculation Design to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Prebunking & Inoculation Design into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Prebunking & Inoculation Design to assess supplied material for manipulation indicators and recommend resilience measures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not model the manipulation technique so vividly in the weakened dose that it functions as actual persuasion — dose calibration is non-negotiable
- do not produce generic 'think before you share' messaging without tying it to a specific named technique and refutation
- do not ignore attitudinal backlash risk: audiences who feel lectured or patronized may reactively increase trust in the technique being inoculated against
- do not skip efficacy-check items — untested inoculation content has unknown resistance-transfer and may provide false assurance

## AGEINT upstream
`docs/ageint/cognitive-security.md`
