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
- For Cognitive Attack Kill Chain, tie each kill chain map, defender action plan, and residual uncertainty log claim to concrete evidence from the specific campaign evidence, target context, and prior threat intel item, source excerpt, observation, or command result that supports it.
- For Cognitive Attack Kill Chain, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the kill chain map.
- Before recommending any Cognitive Attack Kill Chain action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Cognitive Attack Kill Chain: the kill chain map is supported by multiple independent content, behavioral, narrative, media, and audience-risk evidence; collect and organize campaign evidence and map evidence to kill-chain stages checks agree, and no unresolved contradiction would change the result.
- Medium for Cognitive Attack Kill Chain: the kill chain map is plausible, but one important campaign evidence source, comparison case, or alternative explanation remains incomplete.
- Low for Cognitive Attack Kill Chain: the kill chain map rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Cognitive Attack Kill Chain cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating cognitive_security evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Cognitive Attack Kill Chain, use only authorized campaign evidence, target context, and prior threat intel, public or source-approved records, and caller-provided context needed for the defensive task.
- For Cognitive Attack Kill Chain, minimize person-level detail in the kill chain map; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Cognitive Attack Kill Chain, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Cognitive Attack Kill Chain: treating campaign evidence as complete when collect and organize campaign evidence and map evidence to kill-chain stages checks or contradictory evidence are missing.
- Cognitive Attack Kill Chain: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Cognitive Attack Kill Chain: reporting the kill chain map without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Cognitive Attack Kill Chain outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the kill chain map from Cognitive Attack Kill Chain into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Cognitive Attack Kill Chain to assess supplied material for manipulation indicators and recommend resilience measures with campaign evidence, target context, and prior threat intel' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not use this framework to plan or optimize an offensive influence operation — it is strictly for defensive threat modeling and counter-operation planning
- do not assert a stage is complete without observable evidence — speculation about stages with no evidence should be labeled as 'unknown' not 'completed'
- do not focus solely on disrupting a single stage while ignoring that the adversary may adapt and re-enter at a different stage
- do not collapse the distinction between the adversary completing a stage and achieving the intended effect — completion and effectiveness are separate assessments

## AGEINT upstream
`docs/ageint/cognitive-security.md`
