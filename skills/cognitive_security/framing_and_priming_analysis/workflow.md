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
- For Framing & Priming Analysis, anchor every named frame, prime, and severity rating to concrete evidence in the supplied content — a specific lexical choice, metaphor, omission, or anchor — and to the audience whose pre-loaded schema that evidence would activate, rather than asserting interpretive effects in the abstract.
- For Framing & Priming Analysis, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the frame inventory.
- Before recommending any Framing & Priming Analysis action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Framing & Priming Analysis: each entry in the frame inventory ties a named device to a specific textual marker and the schema it activates, the dominant-frame reading is corroborated by contrastive comparison across alternative versions and the stated audience context, and no unresolved contradiction would change the reframing brief.
- Medium for Framing & Priming Analysis: the frame inventory is plausible, but one important content source, comparison case, or alternative explanation remains incomplete.
- Low for Framing & Priming Analysis: the frame inventory rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Framing & Priming Analysis cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating cognitive_security evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Framing & Priming Analysis, use only authorized content, alternative versions, and audience context, public or source-approved records, and caller-provided context needed for the defensive task.
- For Framing & Priming Analysis, minimize person-level detail in the frame inventory; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Framing & Priming Analysis, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Framing & Priming Analysis: declaring a frame mapped when the close-read of linguistic markers skipped the priming sequence or assessed activation without specifying the audience, treating every communicative framing as manipulation and missing what the dominant frame quietly forecloses.
- Framing & Priming Analysis: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Framing & Priming Analysis: reporting the frame inventory without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Framing & Priming Analysis outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the frame inventory from Framing & Priming Analysis into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Framing & Priming Analysis to assess supplied material for manipulation indicators and recommend resilience measures with content, alternative versions, and audience context' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not treat all framing as manipulation — every communicative act involves framing; assess whether the frame distorts or forecloses accurate understanding
- Do not counter a frame by repeating and negating it ('this is not an invasion') — produce only positive counter-frame language that activates an independent schema
- Do not assess priming effects without specifying the audience — a prime only activates schema that the audience has pre-loaded from prior experience
- Do not conflate framing with explicit falsehood — a frame can be factually accurate at every literal point while still systematically misleading at the interpretive level

## AGEINT upstream
`docs/ageint/cognitive-security.md`
