# Workflow — Denial & Deception Detection

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Characterize the evidence and the beneficiary (read)
Document the full evidence body: each item, its source, how it entered the collection pipeline, and when it arrived relative to the analytic cycle. Identify who benefits most if the current assessment stands — that is the candidate deceiver. Assess their known D&D history and capability to access or influence each source channel.

## Step 2 — Apply the deceiver's calculus (reason)
Construct one or more deception scenarios: for each, specify what the adversary would need to (a) conceal (denial elements) and (b) fabricate or stage (deception elements) to produce the observed evidence picture. Ask: is this technically feasible? Would it require penetrating multiple independent sources simultaneously? What would the adversary risk in mounting this operation?

## Step 3 — Identify observable differences (reason)
For each deception scenario, list what would be observably different between the real world and the managed scenario. These are the deception indicators. Check each against existing collection: is it currently observed, absent, or unknown? Note that absence of expected confirmatory evidence is itself a potential deception indicator ('dog that didn't bark').

## Step 4 — Rate plausibility and flag the assessment (reason, write)
Score each deception scenario on adversary capability to execute, motive (what they gain from our erroneous conclusion), opportunity (access to collection channels), and the plausibility cost (how many improbable things must be simultaneously true). Assign HIGH/MEDIUM/LOW deception plausibility. Flag the current analytic assessment with the appropriate D&D caveat.

## Step 5 — Prescribe discriminating collection (write)
Output the deception indicators table and a prioritized collection plan. Rank collection gaps by their discriminating power: which single piece of new evidence would most sharply distinguish genuine from managed? Include recommendations for accessing channels the adversary cannot realistically control.

## Anti-criteria (must NOT happen)
- do not dismiss a deception scenario solely because it would be 'too complicated' — sophisticated adversaries routinely execute multi-year, multi-source denial and deception operations
- do not conflate low base rate of deception with low current probability — if adversary motive and opportunity are present, base rates are not the right prior
- do not allow the current assessment's investment — resources committed, policies built on it — to suppress the D&D check; anchoring to sunk costs is a key adversary exploitation target
- do not treat a passed D&D check as permanent; circumstances change and an assessment that was clean yesterday can be contaminated today

## AGEINT upstream
`docs/ageint/counterintelligence.md`
