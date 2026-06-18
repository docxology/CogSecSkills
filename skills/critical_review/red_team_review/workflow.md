# Workflow — Red-Team Review

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Ingest and model the adversary (read)
Read the artifact thoroughly. Identify its stated goals, key assumptions, dependencies, and design rationale. If an adversary profile is provided, internalize it; otherwise construct a plausible adversary profile based on who would most want the artifact to fail and what capabilities they would plausibly have.

## Step 2 — Generate attack surface (reason)
Adopt the adversarial perspective fully. Systematically enumerate vulnerabilities across relevant dimensions: logical (assumptions that could be false or attacked), operational (execution steps that could fail or be disrupted), technical (exploitable design or implementation gaps), informational (how an adversary could exploit the artifact in the information environment), and reputational (how the artifact could be weaponized against its own authors). Generate failure modes without filtering for comfort.

## Step 3 — Rank and select highest-priority findings (reason)
For each identified vulnerability, estimate exploitability (how easily an adversary with the modeled capabilities could exploit it) and impact (how much damage successful exploitation would cause). Rank by exploitability x impact. Select the top vulnerabilities for deep treatment; note the rest in the catalog.

## Step 4 — Write adversarial narrative (reason, write)
Write the strongest case an adversary or critic could make against the artifact, from their perspective, as a coherent narrative — not as a list of concerns. This surfaces how the vulnerabilities compound and interact. Then shift perspective back to analyst and write specific, actionable mitigations for each top vulnerability.

## Step 5 — Compile vulnerability catalog and recommendations (write)
Produce the ranked vulnerability catalog table. Finalize the red-team narrative. Write a summary of the most critical findings and the mitigations most likely to substantially reduce risk. Flag any vulnerabilities assessed as inherent to the approach (not remediable) for escalation.

## Anti-criteria (must NOT happen)
- do not soften the adversarial perspective — an incomplete red team that avoids uncomfortable findings provides false assurance
- do not conflate a red-team review with a balanced review — the goal is maximum stress, not balance
- do not rank vulnerabilities by how senior the person who introduced them is
- do not terminate the review after finding the first major vulnerability — the worst flaw often compounds with secondary ones
- do not produce mitigations that merely restate the existing design without substantive change

## AGEINT upstream
`docs/ageint/adversarial-assurance.md`
