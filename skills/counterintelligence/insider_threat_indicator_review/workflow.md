# Workflow — Insider Threat Indicator Review

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Establish authorized scope and ingest observations (read)
Confirm the review is being conducted within an authorized insider threat program with appropriate legal basis. Ingest all provided behavioral observations, technical anomalies, and contextual background. Separate factual observations from interpretations before proceeding.

## Step 2 — Map indicators to framework categories (reason)
Systematically apply the CERT Insider Threat and NITTF indicator frameworks. Categorize each observation across domains: (1) Technical — unauthorized access, unusual data movement, policy violations; (2) Behavioral — expressed grievances, disaffection, sudden wealth or financial stress; (3) Personal stressors — relationship problems, substance abuse indicators, major life disruptions; (4) Loyalty/ideology — expressed sympathy toward adversary positions, unauthorized contact with foreign nationals in sensitive contexts; (5) Deception indicators — inconsistencies in statements, concealment behaviors.

## Step 3 — Assess aggregate risk and competing explanations (reason)
Evaluate the number, specificity, and convergence of indicators across categories. Consider competing explanations for each indicator cluster — most observations have benign explanations. Assign an aggregate risk rating: baseline (indicators within normal range), elevated (multiple indicators converging without clear benign explanation), or high (strong multi-category convergence with few benign alternatives).

## Step 4 — Produce indicator review report with next-step guidance (write)
Write the structured indicator review report with: per-category findings with evidence citations; aggregate risk rating and rationale; explicit caveats on what this review does and does not establish; and recommended next steps within program authorities (no action, enhanced authorized monitoring, referral to security officer, initiation of security interview). Note any information gaps that limit the assessment.

## Evidence requirements
- For Insider Threat Indicator Review, bind each finding to a labeled source — interaction records, process artifacts, deception indicators, and alternative explanations, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Insider Threat Indicator Review, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Insider Threat Indicator Review recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Insider Threat Indicator Review: independent lines of interaction records, process artifacts, deception indicators, and alternative explanations converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Insider Threat Indicator Review: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Insider Threat Indicator Review: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Insider Threat Indicator Review cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Insider Threat Indicator Review should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Insider Threat Indicator Review, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Insider Threat Indicator Review, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Insider Threat Indicator Review, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Insider Threat Indicator Review failure: turning defensive tradecraft recognition into operational evasion advice.
- Insider Threat Indicator Review failure: producing guidance that would help a requester evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft.
- Insider Threat Indicator Review failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Insider Threat Indicator Review to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Insider Threat Indicator Review into an operational playbook to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Insider Threat Indicator Review to review supplied interactions or processes for deception, elicitation, or insider-risk indicators' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not treat this review as a determination of guilt, intent, or culpability — it is a risk-level referral tool, not an adjudication
- Do not include monitoring or collection of information beyond what is authorized by the organization's insider threat program authorities and applicable law
- Do not allow demographic characteristics, political beliefs, religion, or union activity to factor into the risk rating — indicators must be behavioral and access-specific
- Do not recommend disciplinary or termination action directly — this review informs a referral to the appropriate security or HR program; action authority rests elsewhere
- Do not conflate protective security intent with punitive intent — the goal is early intervention and harm prevention, not punishment

## AGEINT upstream
`docs/ageint/counterintelligence.md`
