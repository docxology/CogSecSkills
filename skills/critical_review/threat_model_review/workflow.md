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

## Anti-criteria (must NOT happen)
- do not accept the existing model's scope as the correct scope without independently deriving what should be in scope from the system description
- do not treat a stated mitigation as an implemented control — verify that it is operationally active and testable before crediting it
- do not restrict the actor taxonomy to technical adversaries — cognitive-security and social-engineering actors must be assessed for any system involving human users
- do not produce a gap report without severity ratings — an undifferentiated list of concerns is not actionable

## AGEINT upstream
`docs/ageint/adversarial-assurance.md`
