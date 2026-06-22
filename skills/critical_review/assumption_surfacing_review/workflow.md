# Workflow — Assumption Surfacing Review

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Extract claims and premises (read)
Read the target text carefully. Identify every stated conclusion and the explicit premises offered in support. Mark gaps where reasoning jumps without stated justification — these gaps signal implicit assumptions.

## Step 2 — Surface implicit assumptions (reason)
For each logical gap, articulate the unstated premise that would be required to make the reasoning valid. Use the phrasing 'This argument assumes that ...' to keep assumptions distinct from claims. Enumerate all, including background world-model assumptions about actors, causal mechanisms, and timelines.

## Step 3 — Classify and rate each assumption (reason)
For each identified assumption, assign a load-bearing role (critical / supporting / peripheral) and an evidentiary-support rating (strong / weak / none). Note whether the assumption is a single point of failure that an adversary could target to undermine the entire analysis.

## Step 4 — Identify high-risk assumptions and prescribe actions (reason, write)
Rank assumptions by combined risk: load-bearing × weak support × adversarial exploitability. For the highest-risk assumptions, specify a recommended action: validate with independent evidence, add a monitoring indicator, explicitly bound the claim, or reframe the conclusion to be conditioned on the assumption.

## Step 5 — Produce the assumption register and narrative (write)
Write the structured assumption register table and the review narrative. The narrative should state which assumptions most endanger analytic integrity, which are most susceptible to adversarial manipulation, and what concrete steps reviewers or decision-makers should take before acting on the document.

## Evidence requirements
- For Assumption Surfacing Review, bind each finding to a labeled source — artifact excerpts, test output, citations, assumptions, and reproducibility records, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Assumption Surfacing Review, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Assumption Surfacing Review recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Assumption Surfacing Review: independent lines of artifact excerpts, test output, citations, assumptions, and reproducibility records converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Assumption Surfacing Review: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Assumption Surfacing Review: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Assumption Surfacing Review cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Assumption Surfacing Review should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Assumption Surfacing Review, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Assumption Surfacing Review, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Assumption Surfacing Review, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Assumption Surfacing Review failure: performing theatrical critique without concrete evidence, severity, or remediation path.
- Assumption Surfacing Review failure: producing guidance that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Assumption Surfacing Review failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Assumption Surfacing Review to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Assumption Surfacing Review into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Assumption Surfacing Review to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not treat confident assertion as evidence — an assumption stated with high confidence is still an assumption
- Do not limit the review to assumptions the author explicitly labels as assumptions; the most dangerous are always the unacknowledged ones
- Do not conflate load-bearing role with likelihood of being wrong — a well-supported assumption can still be critical
- Do not recommend 'monitor' for a critical assumption with no evidence; critical unsupported assumptions require validation or the conclusion must be hedged

## AGEINT upstream
`docs/ageint/adversarial-assurance.md`
