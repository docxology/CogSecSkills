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
- For Threat Model Review, bind each finding to a labeled source — artifact excerpts, test output, citations, assumptions, and reproducibility records, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Threat Model Review, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Threat Model Review recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Threat Model Review: independent lines of artifact excerpts, test output, citations, assumptions, and reproducibility records converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Threat Model Review: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Threat Model Review: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Threat Model Review cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Threat Model Review should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Threat Model Review, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Threat Model Review, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Threat Model Review, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Threat Model Review failure: performing theatrical critique without concrete evidence, severity, or remediation path.
- Threat Model Review failure: producing guidance that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Threat Model Review failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Threat Model Review to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Threat Model Review into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Threat Model Review to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not accept the existing model's scope as the correct scope without independently deriving what should be in scope from the system description
- do not treat a stated mitigation as an implemented control — verify that it is operationally active and testable before crediting it
- do not restrict the actor taxonomy to technical adversaries — cognitive-security and social-engineering actors must be assessed for any system involving human users
- do not produce a gap report without severity ratings — an undifferentiated list of concerns is not actionable

## AGEINT upstream
`docs/ageint/adversarial-assurance.md`
