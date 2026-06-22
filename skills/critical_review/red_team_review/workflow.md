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
- For Red-Team Review, bind each finding to a labeled source — artifact excerpts, test output, citations, assumptions, and reproducibility records, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Red-Team Review, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Red-Team Review recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Red-Team Review: independent lines of artifact excerpts, test output, citations, assumptions, and reproducibility records converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Red-Team Review: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Red-Team Review: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Red-Team Review cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Red-Team Review should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Red-Team Review, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Red-Team Review, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Red-Team Review, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Red-Team Review failure: performing theatrical critique without concrete evidence, severity, or remediation path.
- Red-Team Review failure: producing guidance that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Red-Team Review failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Red-Team Review to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Red-Team Review into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Red-Team Review to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not soften the adversarial perspective — an incomplete red team that avoids uncomfortable findings provides false assurance
- do not conflate a red-team review with a balanced review — the goal is maximum stress, not balance
- do not rank vulnerabilities by how senior the person who introduced them is
- do not terminate the review after finding the first major vulnerability — the worst flaw often compounds with secondary ones
- do not produce mitigations that merely restate the existing design without substantive change

## AGEINT upstream
`docs/ageint/adversarial-assurance.md`
