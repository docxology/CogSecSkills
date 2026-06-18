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

## Anti-criteria (must NOT happen)
- Do not treat this review as a determination of guilt, intent, or culpability — it is a risk-level referral tool, not an adjudication
- Do not include monitoring or collection of information beyond what is authorized by the organization's insider threat program authorities and applicable law
- Do not allow demographic characteristics, political beliefs, religion, or union activity to factor into the risk rating — indicators must be behavioral and access-specific
- Do not recommend disciplinary or termination action directly — this review informs a referral to the appropriate security or HR program; action authority rests elsewhere
- Do not conflate protective security intent with punitive intent — the goal is early intervention and harm prevention, not punishment

## AGEINT upstream
`docs/ageint/counterintelligence.md`
