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
- For Evidence Grading, bind each finding to a labeled source — study designs, source quality, reproducibility artifacts, and uncertainty records, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Evidence Grading, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Evidence Grading recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Evidence Grading: independent lines of study designs, source quality, reproducibility artifacts, and uncertainty records converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Evidence Grading: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Evidence Grading: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Evidence Grading cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Evidence Grading should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Evidence Grading, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Evidence Grading, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Evidence Grading, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Evidence Grading failure: collapsing heterogeneous evidence into an unsupported single confident conclusion.
- Evidence Grading failure: producing guidance that would help a requester cherry-pick sources, fabricate citations, or overstate certainty from weak evidence.
- Evidence Grading failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Evidence Grading to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Evidence Grading into an operational playbook to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Evidence Grading to synthesize supplied or authorized sources with explicit confidence and uncertainty labels' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not let the volume of low-quality evidence substitute for a small number of high-quality items
- do not assign relevance based on whether the evidence supports the preferred conclusion — grade against the question, not the hypothesis
- do not omit disconfirming evidence from the graded table; a complete picture requires it
- do not use the same source twice as independent corroboration if they share a common reporting chain

## AGEINT upstream
`docs/ageint/research-methods.md`
