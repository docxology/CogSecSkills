# Workflow — Disinformation Attribution

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Inventory the evidence and candidate actors (read)
Compile all available campaign artifacts: account creation patterns, network structure, narrative content and its evolution, technical indicators (hosting infrastructure, metadata, cross-platform behavior), and linguistic fingerprints. List candidate attribution actors — typically 3-5 — including the null hypothesis (no single actor; emergent organic spread) and the false-flag hypothesis (Actor Z mimicking Actor Y).

## Step 2 — Identify diagnostic indicators (reason)
For each indicator in the evidence inventory, assess its diagnostic value: does it discriminate between candidate actors (HIGH diagnostic value), or would most candidates produce it (LOW diagnostic value)? Focus analytical weight on high-diagnostic indicators. Common high-diagnostic indicators include: infrastructure overlap with prior attributed operations, specific narrative timing keyed to Actor X's interests but not others', and operational security failures consistent with a specific actor's known tradecraft.

## Step 3 — Build the ACH matrix (reason)
Construct an Analysis of Competing Hypotheses matrix: rows are diagnostic indicators, columns are candidate actors (including null and false-flag). For each cell, rate consistency: C (consistent with / does not argue against), I (inconsistent with / argues against), N (neutral / uninformative), or U (unknown / not enough information). Weight cells by diagnostic value. The hypothesis with the fewest 'I' ratings across high-weight indicators is the current lead, but do not auto-select — inspect the pattern.

## Step 4 — Calibrate confidence and stress-test the lead (reason)
For the lead attribution hypothesis, ask: (1) How many independent high-diagnostic indicators support it? (2) What key assumption, if wrong, would overturn it? (3) Is the false-flag hypothesis plausible — could Actor Z convincingly mimic Actor Y here? (4) What is the base rate of this actor type running this operation type? Assign calibrated confidence: HIGH (multiple independent diagnostics, false-flag implausible), MEDIUM (consistent pattern but key assumption untested), LOW (only circumstantial or low-diagnostic evidence).

## Step 5 — Produce the assessment and gap list (write)
Write the attribution assessment in structured form: (1) lead hypothesis with confidence and rationale, (2) primary alternative hypothesis and why it cannot yet be ruled out, (3) explicitly stated key assumptions for the lead, (4) what would change the assessment (invalidating evidence). Append the ACH matrix as supporting evidence. Output the top 3-5 intelligence gaps that would most efficiently resolve remaining uncertainty.

## Evidence requirements
- For Disinformation Attribution, link every consistency rating in the matrix and every confidence claim in the assessment to concrete evidence from a specific campaign artifact, infrastructure overlap, narrative-timing observation, or linguistic sample, weighting only indicators that discriminate between candidate actors and labelling the rest as non-diagnostic evidence.
- For Disinformation Attribution, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the attribution matrix.
- Before recommending any Disinformation Attribution action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Disinformation Attribution: the lead actor is supported by multiple independent high-diagnostic indicators in the ACH matrix, the false-flag hypothesis has been explicitly evaluated rather than assumed away, the ranking survives removal of any single indicator, and no unresolved contradiction would overturn the attribution judgment.
- Medium for Disinformation Attribution: the attribution matrix is plausible, but one important campaign artifacts source, comparison case, or alternative explanation remains incomplete.
- Low for Disinformation Attribution: the attribution matrix rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Disinformation Attribution cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating counterintelligence evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Disinformation Attribution, use only authorized campaign artifacts, candidate actors, and strategic context, public or source-approved records, and caller-provided context needed for the defensive task.
- For Disinformation Attribution, minimize person-level detail in the attribution matrix; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Disinformation Attribution, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Disinformation Attribution: presenting an attribution as settled when it rests on stylistic or cui-bono reasoning alone, when the false-flag and null hypotheses were named but never genuinely tested, or when alternatives were dropped before evidence ruled them out, producing false certainty.
- Disinformation Attribution: producing advice that would help a requester evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft.
- Disinformation Attribution: reporting the attribution matrix without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Disinformation Attribution outputs to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the attribution matrix from Disinformation Attribution into an operational playbook to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Disinformation Attribution to review supplied interactions or processes for deception, elicitation, or insider-risk indicators with campaign artifacts, candidate actors, and strategic context' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not present attribution as certain when it is based on circumstantial or stylistic indicators alone; false certainty in attribution assessments has caused serious diplomatic and policy errors
- do not eliminate the false-flag hypothesis without explicitly addressing it — it must be evaluated, not merely mentioned
- do not allow 'who benefits' (cui bono) to drive attribution without corroborating behavioral or technical evidence; cui bono identifies candidates, not conclusions
- do not suppress alternative hypotheses once the lead is identified; they must remain live until definitively ruled out by evidence

## AGEINT upstream
`docs/ageint/counterintelligence.md`
