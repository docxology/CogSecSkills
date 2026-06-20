# Workflow — Astroturfing Detection

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Ingest and scope the sample (read)
Load the candidate account set, post corpus, and engagement metadata. Establish the time window and platform scope. Note whether the sample was self-selected (tip-driven) or randomly drawn — this affects how representativeness claims will be qualified.

## Step 2 — Apply structural and behavioral heuristics (search, reason)
Check for account-creation date spikes (many accounts born in a short window), posting-velocity anomalies (accounts posting far more frequently than organic users), content-hash overlap (near-identical text or media reposted across accounts), and follower-graph clustering (accounts primarily follow one another). Cross-reference account names or bios against prior CIB disclosure archives and threat-intel feeds.

## Step 3 — Test alternative explanations (reason)
Before concluding CIB, rule out organic explanations: viral sharing by real users, platform-algorithmic amplification, a genuine grassroots community with centralized tooling (e.g., a petition site), or researcher/activist coordinated but transparent action. Distinguish 'coordinated' from 'inauthentic' — coordination is a necessary but not sufficient indicator.

## Step 4 — Score, tier, and compile report (reason, write)
Assign each identified cluster a confidence tier (high = multiple independent behavioral indicators; medium = 1-2 indicators with plausible alternatives; low = circumstantial). Write the detection report with: the indicators found per cluster, alternative explanations considered and ruled out, confidence tier, and recommended next steps (platform reporting, additional OSINT, informing relevant stakeholders).

## Evidence requirements
- For Astroturfing Detection, tie each detection report, and indicator table claim to concrete evidence from the specific campaign sample, and baseline context item, source excerpt, observation, or command result that supports it.
- For Astroturfing Detection, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the detection report.
- Before recommending any Astroturfing Detection action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Astroturfing Detection: the detection report is supported by multiple independent content, behavioral, narrative, media, and audience-risk evidence; ingest and scope the sample and apply structural and behavioral heuristics checks agree, and no unresolved contradiction would change the result.
- Medium for Astroturfing Detection: the detection report is plausible, but one important campaign sample source, comparison case, or alternative explanation remains incomplete.
- Low for Astroturfing Detection: the detection report rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Astroturfing Detection cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating cognitive_security evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Astroturfing Detection, use only authorized campaign sample, and baseline context, public or source-approved records, and caller-provided context needed for the defensive task.
- For Astroturfing Detection, minimize person-level detail in the detection report; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Astroturfing Detection, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Astroturfing Detection: treating campaign sample as complete when ingest and scope the sample and apply structural and behavioral heuristics checks or contradictory evidence are missing.
- Astroturfing Detection: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Astroturfing Detection: reporting the detection report without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Astroturfing Detection outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the detection report from Astroturfing Detection into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Astroturfing Detection to assess supplied material for manipulation indicators and recommend resilience measures with campaign sample, and baseline context' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not conflate 'coordinated' with 'inauthentic' — transparent coalitions using shared tooling can coordinate without being deceptive
- do not assert attribution to a specific state or actor without corroborating evidence beyond behavioral signals
- do not treat volume or speed of spread alone as evidence of astroturfing — viral organic content can spread quickly
- do not expose personal data of individual accounts beyond what is necessary to establish the behavioral pattern

## AGEINT upstream
`docs/ageint/cognitive-security.md`
