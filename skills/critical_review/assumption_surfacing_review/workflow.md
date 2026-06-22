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
- For Assumption Surfacing Review, bind each surfaced assumption and its load-bearing and support ratings to concrete evidence drawn from the specific target-text passage or domain-context detail that reveals it, and label any premise resting only on confident assertion as an unsupported assumption rather than established evidence.
- For Assumption Surfacing Review, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the assumption register.
- Before recommending any Assumption Surfacing Review action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Assumption Surfacing Review: every load-bearing assumption in the register is grounded in a specific passage of the target text, the critical/supporting/peripheral classification and evidentiary-support rating hold up when any single excerpt is reconsidered, and no unresolved contradiction would change which premises are flagged as the most dangerous to the conclusion.
- Medium for Assumption Surfacing Review: the assumption register is plausible, but one important target text source, comparison case, or alternative explanation remains incomplete.
- Low for Assumption Surfacing Review: the assumption register rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Assumption Surfacing Review cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating critical_review evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Assumption Surfacing Review, use only authorized target text, and domain context, public or source-approved records, and caller-provided context needed for the defensive task.
- For Assumption Surfacing Review, minimize person-level detail in the assumption register; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Assumption Surfacing Review, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Assumption Surfacing Review: declaring the assumption register complete when implicit premises behind unstated reasoning gaps were never extracted or contradictory evidence about a critical premise was left unexamined, so an empty findings list reflects a shallow scan rather than a genuinely well-founded argument.
- Assumption Surfacing Review: producing advice that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Assumption Surfacing Review: reporting the assumption register without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Assumption Surfacing Review outputs to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the assumption register from Assumption Surfacing Review into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Assumption Surfacing Review to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures with target text, and domain context' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not treat confident assertion as evidence — an assumption stated with high confidence is still an assumption
- Do not limit the review to assumptions the author explicitly labels as assumptions; the most dangerous are always the unacknowledged ones
- Do not conflate load-bearing role with likelihood of being wrong — a well-supported assumption can still be critical
- Do not recommend 'monitor' for a critical assumption with no evidence; critical unsupported assumptions require validation or the conclusion must be hedged

## AGEINT upstream
`docs/ageint/adversarial-assurance.md`
