# Workflow — Framing & Priming Analysis

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Close-read for linguistic markers (read)
Read the content carefully, annotating: (a) lexical choices that activate strong schema (e.g., 'flood' vs. 'wave' of migrants); (b) conceptual metaphors structuring a domain (e.g., 'fighting' a disease, 'cleaning up' crime); (c) category labels that foreground or background attributes; (d) what is mentioned first vs. last; (e) what comparisons or baseline figures are offered as anchors.

## Step 2 — Identify active frames and priming sequences (reason)
From the annotations, identify the dominant frame(s) — the organizing interpretive lens. Name each frame precisely (e.g., 'national security threat frame,' 'economic burden frame,' 'humanitarian victim frame'). Map the priming sequence: which schema is activated early and how it predisposes processing of subsequent claims. Identify what interpretive conclusions the frame makes available and which it forecloses.

## Step 3 — Assess omissions and suppressed alternatives (reason)
For each active frame, specify what competing framings are crowded out. What facts, actors, or relationships does the dominant frame make less salient or harder to perceive? What questions does it render unaskable? Rate the severity of each framing device (low: minor salience shift; medium: channels interpretation toward one of several plausible conclusions; high: actively forecloses accurate understanding).

## Step 4 — Produce frame inventory and reframing brief (write)
Compile the frame inventory table. Write the reframing brief: describe the dominant frame strategy and its overall effect; for each high-severity device, provide a specific alternative framing with example language that activates a competing schema without repeating the hostile frame. Include inoculation language if appropriate: language that pre-exposes the audience to the framing device so it loses automatic interpretive force.

## Evidence requirements
- For Framing & Priming Analysis, bind each finding to a labeled source — content, behavioral, narrative, media, and audience-risk evidence, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Framing & Priming Analysis, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Framing & Priming Analysis recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Framing & Priming Analysis: independent lines of content, behavioral, narrative, media, and audience-risk evidence converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Framing & Priming Analysis: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Framing & Priming Analysis: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Framing & Priming Analysis cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Framing & Priming Analysis should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Framing & Priming Analysis, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Framing & Priming Analysis, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Framing & Priming Analysis, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Framing & Priming Analysis failure: mistaking persuasive resonance for verified harm or intent.
- Framing & Priming Analysis failure: producing guidance that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Framing & Priming Analysis failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Framing & Priming Analysis to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Framing & Priming Analysis into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Framing & Priming Analysis to assess supplied material for manipulation indicators and recommend resilience measures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not treat all framing as manipulation — every communicative act involves framing; assess whether the frame distorts or forecloses accurate understanding
- Do not counter a frame by repeating and negating it ('this is not an invasion') — produce only positive counter-frame language that activates an independent schema
- Do not assess priming effects without specifying the audience — a prime only activates schema that the audience has pre-loaded from prior experience
- Do not conflate framing with explicit falsehood — a frame can be factually accurate at every literal point while still systematically misleading at the interpretive level

## AGEINT upstream
`docs/ageint/cognitive-security.md`
