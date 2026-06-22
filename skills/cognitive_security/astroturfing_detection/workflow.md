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
- For Astroturfing Detection, bind each finding to a labeled source — content, behavioral, narrative, media, and audience-risk evidence, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Astroturfing Detection, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Astroturfing Detection recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Astroturfing Detection: independent lines of content, behavioral, narrative, media, and audience-risk evidence converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Astroturfing Detection: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Astroturfing Detection: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Astroturfing Detection cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Astroturfing Detection should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Astroturfing Detection, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Astroturfing Detection, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Astroturfing Detection, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Astroturfing Detection failure: mistaking persuasive resonance for verified harm or intent.
- Astroturfing Detection failure: producing guidance that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Astroturfing Detection failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Astroturfing Detection to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Astroturfing Detection into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Astroturfing Detection to assess supplied material for manipulation indicators and recommend resilience measures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not conflate 'coordinated' with 'inauthentic' — transparent coalitions using shared tooling can coordinate without being deceptive
- do not assert attribution to a specific state or actor without corroborating evidence beyond behavioral signals
- do not treat volume or speed of spread alone as evidence of astroturfing — viral organic content can spread quickly
- do not expose personal data of individual accounts beyond what is necessary to establish the behavioral pattern

## AGEINT upstream
`docs/ageint/cognitive-security.md`
