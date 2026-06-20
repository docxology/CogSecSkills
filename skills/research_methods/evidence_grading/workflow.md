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

## Evidence requirements
- For Evidence Grading, tie each graded evidence table, and weight of evidence summary claim to concrete evidence from the specific analytic question, evidence items, and grading rubric item, source excerpt, observation, or command result that supports it.
- For Evidence Grading, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the graded evidence table.
- Before recommending any Evidence Grading action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Evidence Grading: the graded evidence table is supported by multiple independent study designs, source quality, reproducibility artifacts, and uncertainty records; inventory and characterize each evidence item and grade quality for each item checks agree, and no unresolved contradiction would change the result.
- Medium for Evidence Grading: the graded evidence table is plausible, but one important analytic question source, comparison case, or alternative explanation remains incomplete.
- Low for Evidence Grading: the graded evidence table rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Evidence Grading cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating research_methods evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Evidence Grading, use only authorized analytic question, evidence items, and grading rubric, public or source-approved records, and caller-provided context needed for the defensive task.
- For Evidence Grading, minimize person-level detail in the graded evidence table; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Evidence Grading, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Evidence Grading: treating analytic question as complete when inventory and characterize each evidence item and grade quality for each item checks or contradictory evidence are missing.
- Evidence Grading: producing advice that would help a requester cherry-pick sources, fabricate citations, or overstate certainty from weak evidence.
- Evidence Grading: reporting the graded evidence table without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Evidence Grading outputs to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the graded evidence table from Evidence Grading into an operational playbook to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Evidence Grading to synthesize supplied or authorized sources with explicit confidence and uncertainty labels with analytic question, evidence items, and grading rubric' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not let the volume of low-quality evidence substitute for a small number of high-quality items
- do not assign relevance based on whether the evidence supports the preferred conclusion — grade against the question, not the hypothesis
- do not omit disconfirming evidence from the graded table; a complete picture requires it
- do not use the same source twice as independent corroboration if they share a common reporting chain

## AGEINT upstream
`docs/ageint/research-methods.md`
