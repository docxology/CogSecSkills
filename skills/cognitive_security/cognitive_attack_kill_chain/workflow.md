# Workflow — Cognitive Attack Kill Chain

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Collect and organize campaign evidence (read, search)
Assemble all available evidence about the campaign: account creation patterns, content artifacts, distribution pathways, amplification networks, timing, and any prior threat intelligence on the actor or similar campaigns. Search for prior academic or government reports on analogous TTPs to supplement direct evidence. Organize evidence chronologically.

## Step 2 — Map evidence to kill-chain stages (reason)
Work through each kill-chain stage and assess whether evidence exists for it: (1) Reconnaissance — did the actor study the target audience's beliefs, vulnerabilities, and platform habits? (2) Weaponization — was content, persona infrastructure, or narrative strategy developed? (3) Delivery — through which channels and vectors was content introduced? (4) Exploitation — did the content succeed in shifting beliefs, amplifying division, or triggering action? (5) Installation — has a persistent narrative, framing, or trusted persona been embedded in the target information environment? (6) Command and Control — is there evidence of ongoing steering or adaptation of the campaign by the actor? (7) Persistence — has the campaign achieved durable effects that continue without active actor maintenance? Assign each stage a completion status and a confidence level.

## Step 3 — Identify disruption points and assess feasibility (reason)
For each stage assessed as not yet completed or in-progress, identify the available defender interventions: platform-level actions (account removal, content labeling, algorithmic down-ranking), counter-messaging or prebunking, source-credibility communication to the audience, law-enforcement or regulatory referral, or exposure/attribution. Assess feasibility given the defender's authorities, speed, and resources. Flag stages where intervention windows have already closed.

## Step 4 — Produce kill-chain map, action plan, and uncertainty log (write)
Write the stage-by-stage kill-chain map with completion assessments, confidence levels, and supporting evidence citations. Produce the defender action plan as a prioritized table with intervention, responsible actor, timing window, and expected disruption effect. Append the residual uncertainty log, specifying which stage assessments are low-confidence, what information would resolve them, and what the analytical implications are if those uncertainties resolve in the adversary's favor.

## Evidence requirements
- For Cognitive Attack Kill Chain, bind each finding to a labeled source — content, behavioral, narrative, media, and audience-risk evidence, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Cognitive Attack Kill Chain, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Cognitive Attack Kill Chain recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Cognitive Attack Kill Chain: independent lines of content, behavioral, narrative, media, and audience-risk evidence converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Cognitive Attack Kill Chain: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Cognitive Attack Kill Chain: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Cognitive Attack Kill Chain cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Cognitive Attack Kill Chain should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Cognitive Attack Kill Chain, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Cognitive Attack Kill Chain, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Cognitive Attack Kill Chain, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Cognitive Attack Kill Chain failure: mistaking persuasive resonance for verified harm or intent.
- Cognitive Attack Kill Chain failure: producing guidance that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Cognitive Attack Kill Chain failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Cognitive Attack Kill Chain to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Cognitive Attack Kill Chain into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Cognitive Attack Kill Chain to assess supplied material for manipulation indicators and recommend resilience measures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not use this framework to plan or optimize an offensive influence operation — it is strictly for defensive threat modeling and counter-operation planning
- do not assert a stage is complete without observable evidence — speculation about stages with no evidence should be labeled as 'unknown' not 'completed'
- do not focus solely on disrupting a single stage while ignoring that the adversary may adapt and re-enter at a different stage
- do not collapse the distinction between the adversary completing a stage and achieving the intended effect — completion and effectiveness are separate assessments

## AGEINT upstream
`docs/ageint/cognitive-security.md`
