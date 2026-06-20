# Workflow — Counter-Messaging Strategy

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Characterize the falsehood and context (read)
Read the false claim or narrative precisely. Identify: (1) the factual error or misleading element; (2) the manipulation technique being used (fabrication, decontextualization, false amplification, false authority, emotional exploitation, etc.); (3) why the claim is compelling to the target audience — what psychological or social need it meets; (4) the current spread state (pre-viral, viral, post-peak).

## Step 2 — Profile audience and select framework (read, reason)
Review the audience profile: prior beliefs, trust anchors, media channels, vulnerability factors. Determine intervention timing. Select primary framework: (a) inoculation/pre-bunking if the claim has not yet reached the audience widely — expose them to a weakened form of the manipulation technique with a warning label; (b) accuracy nudge if the audience is exposed but not deeply committed — a simple, clear factual correction from a trusted source may suffice; (c) narrative replacement if the false claim fills a genuine explanatory gap — provide a more compelling true alternative narrative that meets the same psychological need; (d) technique disclosure if the claim is too viral to de-bunk by repetition — publicly name and explain the manipulation technique being used.

## Step 3 — Assess amplification risk and design constraints (reason)
Estimate whether any counter-message format risks amplifying the falsehood: does quoting it expose it to a larger audience? Does the correction framing seem partisan and thus limit reach? Are there backfire-effect risks for a strongly identity-committed audience? Identify what must NOT appear in the counter-message (specific false phrases, inflammatory framing, institutional logos that trigger distrust for this audience). Document constraints that will govern the message design.

## Step 4 — Design the counter-message architecture (reason, write)
Define: (1) the CORE TRUTH to center — the accurate, affirmative statement that should dominate audience memory after exposure; (2) the MANIPULATION LABEL — the name of the technique being used, stated plainly; (3) the MESSENGER — who should deliver this message to maximize credibility with the target audience; (4) the CHANNEL SEQUENCE — which platforms or formats to use, in what order, to maximize reach within amplification constraints; (5) the TIMING — relative to the spread curve and any news cycle.

## Step 5 — Draft and quality-check the strategy document (write)
Write the full counter_messaging_strategy document. For each message variant in the table, verify: Does it lead with the truth? Does it name the technique rather than repeat the false claim verbatim? Is the messenger appropriate? Is the format right for the channel? Apply the 'ethical check': would this message use any manipulation technique to counter manipulation? If yes, redesign. Emit the strategy document and message variants table.

## Evidence requirements
- For Counter-Messaging Strategy, tie each counter messaging strategy, and message variants table claim to concrete evidence from the specific false claim or narrative, audience profile, and intervention timing item, source excerpt, observation, or command result that supports it.
- For Counter-Messaging Strategy, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the counter messaging strategy.
- Before recommending any Counter-Messaging Strategy action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Counter-Messaging Strategy: the counter messaging strategy is supported by multiple independent content, behavioral, narrative, media, and audience-risk evidence; characterize the falsehood and context and profile audience and select framework checks agree, and no unresolved contradiction would change the result.
- Medium for Counter-Messaging Strategy: the counter messaging strategy is plausible, but one important false claim or narrative source, comparison case, or alternative explanation remains incomplete.
- Low for Counter-Messaging Strategy: the counter messaging strategy rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Counter-Messaging Strategy cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating cognitive_security evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Counter-Messaging Strategy, use only authorized false claim or narrative, audience profile, and intervention timing, public or source-approved records, and caller-provided context needed for the defensive task.
- For Counter-Messaging Strategy, minimize person-level detail in the counter messaging strategy; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Counter-Messaging Strategy, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Counter-Messaging Strategy: treating false claim or narrative as complete when characterize the falsehood and context and profile audience and select framework checks or contradictory evidence are missing.
- Counter-Messaging Strategy: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Counter-Messaging Strategy: reporting the counter messaging strategy without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Counter-Messaging Strategy outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the counter messaging strategy from Counter-Messaging Strategy into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Counter-Messaging Strategy to assess supplied material for manipulation indicators and recommend resilience measures with false claim or narrative, audience profile, and intervention timing' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not design counter-messages that lead with the false claim — stating the falsehood first strengthens its memory trace even when labeled false
- do not repeat the exact false phrasing of the claim in the counter-message text — use indirect reference or technique-naming instead
- do not use emotional manipulation, false urgency, or social-proof amplification in the counter-message even if those techniques would 'work' — the corrector must not model the attack
- do not recommend messenger or channel without grounding in the specific audience's trust structure — generic 'trusted authority' advice is insufficient
- do not conflate this skill with an operational influence-operation design tool — this skill is strictly for institutional defensive and educational counter-messaging

## AGEINT upstream
`docs/ageint/cognitive-security.md`
