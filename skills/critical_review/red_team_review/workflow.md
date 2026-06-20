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

## Evidence requirements
- For Red-Team Review, tie each vulnerability catalog, and red team narrative claim to concrete evidence from the specific artifact, adversary profile, and review scope item, source excerpt, observation, or command result that supports it.
- For Red-Team Review, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the vulnerability catalog.
- Before recommending any Red-Team Review action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Red-Team Review: the vulnerability catalog is supported by multiple independent artifact excerpts, test output, citations, assumptions, and reproducibility records; ingest and model the adversary and generate attack surface checks agree, and no unresolved contradiction would change the result.
- Medium for Red-Team Review: the vulnerability catalog is plausible, but one important artifact source, comparison case, or alternative explanation remains incomplete.
- Low for Red-Team Review: the vulnerability catalog rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Red-Team Review cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating critical_review evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Red-Team Review, use only authorized artifact, adversary profile, and review scope, public or source-approved records, and caller-provided context needed for the defensive task.
- For Red-Team Review, minimize person-level detail in the vulnerability catalog; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Red-Team Review, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Red-Team Review: treating artifact as complete when ingest and model the adversary and generate attack surface checks or contradictory evidence are missing.
- Red-Team Review: producing advice that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Red-Team Review: reporting the vulnerability catalog without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Red-Team Review outputs to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the vulnerability catalog from Red-Team Review into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Red-Team Review to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures with artifact, adversary profile, and review scope' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not soften the adversarial perspective — an incomplete red team that avoids uncomfortable findings provides false assurance
- do not conflate a red-team review with a balanced review — the goal is maximum stress, not balance
- do not rank vulnerabilities by how senior the person who introduced them is
- do not terminate the review after finding the first major vulnerability — the worst flaw often compounds with secondary ones
- do not produce mitigations that merely restate the existing design without substantive change

## AGEINT upstream
`docs/ageint/adversarial-assurance.md`
