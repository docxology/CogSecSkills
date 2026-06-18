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

## Anti-criteria (must NOT happen)
- do not conflate 'coordinated' with 'inauthentic' — transparent coalitions using shared tooling can coordinate without being deceptive
- do not assert attribution to a specific state or actor without corroborating evidence beyond behavioral signals
- do not treat volume or speed of spread alone as evidence of astroturfing — viral organic content can spread quickly
- do not expose personal data of individual accounts beyond what is necessary to establish the behavioral pattern

## AGEINT upstream
`docs/ageint/cognitive-security.md`
