# Workflow — Assumption Surfacing Review

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Extract claims and premises (read)
Read the target text carefully. Identify every stated conclusion and the explicit premises offered in support. Mark gaps where reasoning jumps without stated justification — these gaps signal implicit assumptions.

## Step 2 — Surface implicit assumptions (reason)
For each logical gap, articulate the unstated premise that would be required to make the reasoning valid. Use the phrasing 'This argument assumes that ...' to keep assumptions distinct from claims. Enumerate all, including background world-model assumptions about actors, causal mechanisms, and timelines.

## Step 3 — Classify and rate each assumption (reason)
For each identified assumption, assign a load-bearing role (critical / supporting / peripheral) and an evidentiary-support rating (strong / weak / none). Note whether the assumption is a single point of failure that an adversary could target to undermine the entire analysis.

## Step 4 — Identify high-risk assumptions and prescribe actions (reason, write)
Rank assumptions by combined risk: load-bearing × weak support × adversarial exploitability. For the highest-risk assumptions, specify a recommended action: validate with independent evidence, add a monitoring indicator, explicitly bound the claim, or reframe the conclusion to be conditioned on the assumption.

## Step 5 — Produce the assumption register and narrative (write)
Write the structured assumption register table and the review narrative. The narrative should state which assumptions most endanger analytic integrity, which are most susceptible to adversarial manipulation, and what concrete steps reviewers or decision-makers should take before acting on the document.

## Anti-criteria (must NOT happen)
- Do not treat confident assertion as evidence — an assumption stated with high confidence is still an assumption
- Do not limit the review to assumptions the author explicitly labels as assumptions; the most dangerous are always the unacknowledged ones
- Do not conflate load-bearing role with likelihood of being wrong — a well-supported assumption can still be critical
- Do not recommend 'monitor' for a critical assumption with no evidence; critical unsupported assumptions require validation or the conclusion must be hedged

## AGEINT upstream
`docs/ageint/adversarial-assurance.md`
