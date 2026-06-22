# Workflow — Narrative Threat Assessment

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Capture the narrative precisely (read)
Read the supplied artifact and record the core claim, sub-claims, framing, loaded terms, implied causation, and minimal necessary quotations. Label every quotation as the object of study rather than endorsement.

## Step 2 — Identify target audience and levers (reason)
Determine who the narrative appears designed to move, which belief or identity levers it exploits, and what prior beliefs it assumes or reinforces.

## Step 3 — Classify manipulation techniques (reason)
Map emotional triggers, false dichotomies, out-group threat, manufactured consensus, cherry-picking, or false equivalence to the exact text that exhibits each technique.

## Step 4 — Assess provenance and likely intent (read, search)
Examine sources, timing, circulation samples, prior debunks, and corroborating signals. Distinguish organic spread from coordination with calibrated uncertainty.

## Step 5 — Estimate reach and virality drivers (search, reason)
Estimate observed spread and identify platform affordances, influencer nodes, emotional payload, or event timing that may drive circulation.

## Step 6 — Rate harm potential and urgency (reason)
Rate plausible harm to individuals, groups, institutions, or public safety, then state the evidence each rating rests on.

## Step 7 — Recommend defensive responses (write)
Write the assessment and prioritize strictly defensive responses such as prebunking, lateral-reading prompts, and protective counter-framing.

## Evidence requirements
- For Narrative Threat Assessment, bind each finding to a labeled source — content, behavioral, narrative, media, and audience-risk evidence, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Narrative Threat Assessment, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Narrative Threat Assessment recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Narrative Threat Assessment: independent lines of content, behavioral, narrative, media, and audience-risk evidence converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Narrative Threat Assessment: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Narrative Threat Assessment: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Narrative Threat Assessment cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Narrative Threat Assessment should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Narrative Threat Assessment, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Narrative Threat Assessment, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Narrative Threat Assessment, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Narrative Threat Assessment failure: mistaking persuasive resonance for verified harm or intent.
- Narrative Threat Assessment failure: producing guidance that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Narrative Threat Assessment failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Narrative Threat Assessment to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Narrative Threat Assessment into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Narrative Threat Assessment to assess supplied material for manipulation indicators and recommend resilience measures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- **No offensive manipulation.** Never produce a how-to, playbook, or messaging
- **No uncritical amplification.** Do not restate the narrative as if true or
- **No false-confidence attribution.** Do not name an actor, sponsor, or intent
- **No targeting of individuals.** Do not produce dossiers on private people or

## AGEINT upstream
`docs/ageint/cognitive-security.md`
