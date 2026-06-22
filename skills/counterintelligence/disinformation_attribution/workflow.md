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
- For Disinformation Attribution, bind each finding to a labeled source — interaction records, process artifacts, deception indicators, and alternative explanations, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Disinformation Attribution, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Disinformation Attribution recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Disinformation Attribution: independent lines of interaction records, process artifacts, deception indicators, and alternative explanations converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Disinformation Attribution: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Disinformation Attribution: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Disinformation Attribution cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Disinformation Attribution should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Disinformation Attribution, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Disinformation Attribution, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Disinformation Attribution, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Disinformation Attribution failure: turning defensive tradecraft recognition into operational evasion advice.
- Disinformation Attribution failure: producing guidance that would help a requester evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft.
- Disinformation Attribution failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Disinformation Attribution to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Disinformation Attribution into an operational playbook to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Disinformation Attribution to review supplied interactions or processes for deception, elicitation, or insider-risk indicators' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not present attribution as certain when it is based on circumstantial or stylistic indicators alone; false certainty in attribution assessments has caused serious diplomatic and policy errors
- do not eliminate the false-flag hypothesis without explicitly addressing it — it must be evaluated, not merely mentioned
- do not allow 'who benefits' (cui bono) to drive attribution without corroborating behavioral or technical evidence; cui bono identifies candidates, not conclusions
- do not suppress alternative hypotheses once the lead is identified; they must remain live until definitively ruled out by evidence

## AGEINT upstream
`docs/ageint/counterintelligence.md`
