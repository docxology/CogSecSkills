# Workflow — Evidence Grading

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Inventory and characterize each evidence item (read)
Read each evidence item. Record its source type (HUMINT, SIGINT, open source, academic study, etc.), collection date, access path, and any known reporting limitations or collection gaps. Establish the rubric tiers to be used (e.g., NATO A-F reliability / 1-6 credibility, or GRADE tiers for scientific evidence).

## Step 2 — Grade quality for each item (reason)
For each item, assess: source reliability (historical accuracy, independence, access, potential bias), methodological rigor (how the information was obtained and verified), and internal consistency. Assign a quality grade (e.g., A/B/C/D/F or High/Moderate/Low) and write a one-line justification.

## Step 3 — Grade relevance for each item (reason)
Assess how directly each item speaks to the analytic question: does it address the question directly, tangentially, or only by analogy? Assign a relevance grade and note whether the item provides confirming, disconfirming, or ambiguous signal relative to the hypothesis.

## Step 4 — Compute composite weight and summarize (reason, write)
Combine quality and relevance grades into a composite weight for each item. Aggregate across all items to identify the weight-of-evidence direction, confidence tier, critical gaps (things that would strongly bear on the question but are absent), and any contradictions between high-weight items. Write the graded evidence table and weight-of-evidence summary narrative.

## Anti-criteria (must NOT happen)
- do not let the volume of low-quality evidence substitute for a small number of high-quality items
- do not assign relevance based on whether the evidence supports the preferred conclusion — grade against the question, not the hypothesis
- do not omit disconfirming evidence from the graded table; a complete picture requires it
- do not use the same source twice as independent corroboration if they share a common reporting chain

## AGEINT upstream
`docs/ageint/research-methods.md`
