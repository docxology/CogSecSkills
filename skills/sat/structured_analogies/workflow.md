# Workflow — Structured Analogies

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Characterize the current situation (read)
Read the current situation description. Identify the key attributes that any historical analogue must share: actor type, medium, intent, target, environmental conditions. These become the selection criteria.

## Step 2 — Identify and select candidate cases (search, reason)
Search for historical cases that plausibly match the stated criteria. Aim for at least three to five cases, including at least one that is widely cited (to capture the intuitive analogy) and at least one that is less obvious (to test its boundaries). Exclude cases only if they fail stated criteria, not because their outcomes are inconvenient.

## Step 3 — Map similarities and dissimilarities (reason)
For each case, systematically compare it to the current situation on every dimension. Rate each comparison as strongly similar, partially similar, or dissimilar. Record the key dissimilarity for every case — even the closest analogues will have important disanalogies.

## Step 4 — Derive lessons and bound confidence (reason, write)
Extract lessons that are supported by multiple cases and are robust to the dissimilarities. Note where a lesson rests on a single case or on a weak analogy fit, and reduce confidence accordingly. Write predicted trajectories qualified by the analogy's limitations.

## Step 5 — Produce comparison table and analytic narrative (write)
Emit the multi-case comparison table and the lessons-and-predictions narrative. Flag the single most relied-upon analogy as a potential anchor bias risk.

## Anti-criteria (must NOT happen)
- do not select cases after learning their outcomes in a way that biases toward cases that support the preferred conclusion
- do not treat a close similarity on salient features as confirmation — check structural and contextual dissimilarities before drawing lessons
- do not present a single historical case as 'the' analogy without showing the full comparison set and why others were excluded or downweighted

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
