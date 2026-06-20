# Workflow — Threat Model Review

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Extract the model's declared elements (read)
Read the threat model and extract its declared scope boundary, actor/adversary list, attack surface inventory, trust boundaries, threat categories, and stated mitigations. Note the modeling methodology used (STRIDE, PASTA, attack tree, narrative) and the date of last update.

## Step 2 — Independently derive expected elements (reason)
From the system description (or the threat model's own system description), independently enumerate: who could plausibly threaten this system (insiders, nation-state, criminal, activist, ideological actor, supply chain, cognitive/influence actors); what attack surfaces exist (technical, organizational, social, informational); what trust relationships are asserted. Do this derivation before re-reading the model to avoid anchoring on its existing content.

## Step 3 — Compute gaps and audit assumptions (reason)
Compare the derived set to the model's declared set. Identify: missing actors, missing surfaces, incorrect trust-boundary placements, and missing threat categories. Extract all explicit and implicit assumptions (e.g., 'insiders are trusted', 'users will recognize phishing', 'the supply chain vendor is low-risk'). Rate each assumption as validated, unvalidated-plausible, or unvalidated-risky. For each stated mitigation, judge whether it is actually implemented or merely planned.

## Step 4 — Produce gap report and recommendations (write)
Write the gap table: each row maps to a dimension (actors/surfaces/assumptions/mitigations/scope), cites evidence, assigns severity (critical/high/medium/low), and recommends a specific remediation. Write the assumption register as a tagged list. Write the scope recommendation narrative explaining whether boundaries should be expanded and why. Produce a prioritized remediation list (critical gaps first).

## Evidence requirements
- For Threat Model Review, tie each gap report, assumption register, and revised scope recommendation claim to concrete evidence from the specific threat model, system description, and review focus item, source excerpt, observation, or command result that supports it.
- For Threat Model Review, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the gap report.
- Before recommending any Threat Model Review action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Threat Model Review: the gap report is supported by multiple independent artifact excerpts, test output, citations, assumptions, and reproducibility records; extract the model's declared elements and independently derive expected elements checks agree, and no unresolved contradiction would change the result.
- Medium for Threat Model Review: the gap report is plausible, but one important threat model source, comparison case, or alternative explanation remains incomplete.
- Low for Threat Model Review: the gap report rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Threat Model Review cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating critical_review evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Threat Model Review, use only authorized threat model, system description, and review focus, public or source-approved records, and caller-provided context needed for the defensive task.
- For Threat Model Review, minimize person-level detail in the gap report; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Threat Model Review, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Threat Model Review: treating threat model as complete when extract the model's declared elements and independently derive expected elements checks or contradictory evidence are missing.
- Threat Model Review: producing advice that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Threat Model Review: reporting the gap report without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Threat Model Review outputs to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the gap report from Threat Model Review into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Threat Model Review to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures with threat model, system description, and review focus' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not accept the existing model's scope as the correct scope without independently deriving what should be in scope from the system description
- do not treat a stated mitigation as an implemented control — verify that it is operationally active and testable before crediting it
- do not restrict the actor taxonomy to technical adversaries — cognitive-security and social-engineering actors must be assessed for any system involving human users
- do not produce a gap report without severity ratings — an undifferentiated list of concerns is not actionable

## AGEINT upstream
`docs/ageint/adversarial-assurance.md`
