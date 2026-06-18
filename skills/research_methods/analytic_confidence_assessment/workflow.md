# Workflow — Analytic Confidence Assessment

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Inventory evidence and assumptions (read)
Read the analytic judgment and all supporting evidence. Catalog each source with its type (human, technical, open, liaison), reliability history, and access freshness. List every assumption the conclusion implicitly requires.

## Step 2 — Score three confidence dimensions (reason)
Score source quality (reliability and credibility of each source), corroboration (number of independent confirming sources and absence of contradictory evidence), and assumption load (how many high-impact assumptions remain untested). Use a consistent three-level rubric: high/moderate/low for each dimension.

## Step 3 — Derive overall confidence tier (reason)
Combine dimension scores using a conservative rule: overall confidence cannot exceed the weakest dimension. Note whether corroboration is genuine independence or from common-origin sources, and flag any single point of failure in the evidence chain.

## Step 4 — Write confidence statement (write)
Produce the confidence assessment: state the tier, provide a one-paragraph justification citing each dimension score, list the two or three conditions that would raise or lower confidence, and note any cognitive biases (availability, anchoring) that may have inflated the initial estimate.

## Anti-criteria (must NOT happen)
- do not assign confidence based on how comfortable the analyst feels with the conclusion rather than on evidence and assumption load
- do not treat corroboration from sources sharing a common origin (e.g., all from the same reporting chain) as independent confirmation
- do not omit a confidence statement because the judgment is preliminary — a low-confidence label is informative, not a failure

## AGEINT upstream
`docs/ageint/research-methods.md`
