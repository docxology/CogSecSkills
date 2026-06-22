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
- For Insider Threat Indicator Review, map each categorized indicator and the aggregate risk rating to concrete evidence from the supplied behavioral observations, authorized access logs, or contextual background, weigh a competing benign explanation for every cluster, and use only evidence obtainable within the program's legal monitoring authorities.
- For Insider Threat Indicator Review, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the insider threat indicator review report.
- Before recommending any Insider Threat Indicator Review action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Insider Threat Indicator Review: specific, articulable indicators converge across multiple framework categories with few benign explanations remaining, each rests on access or behavior obtained within authorized monitoring, the aggregate risk rating is stable, and no unresolved contradiction would change the referral recommendation.
- Medium for Insider Threat Indicator Review: the insider threat indicator review report is plausible, but one important behavioral observations source, comparison case, or alternative explanation remains incomplete.
- Low for Insider Threat Indicator Review: the insider threat indicator review report rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Insider Threat Indicator Review cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating counterintelligence evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Insider Threat Indicator Review, use only authorized behavioral observations, access and technical indicators, and contextual background, public or source-approved records, and caller-provided context needed for the defensive task.
- For Insider Threat Indicator Review, minimize person-level detail in the insider threat indicator review report; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Insider Threat Indicator Review, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Insider Threat Indicator Review: treating the review as a determination of guilt rather than a referral, elevating risk from common benign behaviors without pattern and context, or letting demographic, political, or protected traits factor in, so the rating reflects bias or overreach instead of authorized behavioral evidence.
- Insider Threat Indicator Review: producing advice that would help a requester evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft.
- Insider Threat Indicator Review: reporting the insider threat indicator review report without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Insider Threat Indicator Review outputs to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the insider threat indicator review report from Insider Threat Indicator Review into an operational playbook to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Insider Threat Indicator Review to review supplied interactions or processes for deception, elicitation, or insider-risk indicators with behavioral observations, access and technical indicators, and contextual background' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not treat this review as a determination of guilt, intent, or culpability — it is a risk-level referral tool, not an adjudication
- Do not include monitoring or collection of information beyond what is authorized by the organization's insider threat program authorities and applicable law
- Do not allow demographic characteristics, political beliefs, religion, or union activity to factor into the risk rating — indicators must be behavioral and access-specific
- Do not recommend disciplinary or termination action directly — this review informs a referral to the appropriate security or HR program; action authority rests elsewhere
- Do not conflate protective security intent with punitive intent — the goal is early intervention and harm prevention, not punishment

## AGEINT upstream
`docs/ageint/counterintelligence.md`
