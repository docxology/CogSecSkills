# Workflow — Starbursting

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Frame the topic (read)
Read the topic statement or artifact. Define the boundaries: what is the subject being questioned, and what time frame, actor set, or information environment is in scope?

## Step 2 — Generate questions per interrogative (reason)
Working through each interrogative in turn—Who, What, When, Where, Why, How—generate at least three to five questions per category. Include questions about absences, counterfactuals, and adversary intent. Do not attempt to answer any question at this stage.

## Step 3 — Rate and prioritize (reason)
For each question, estimate its analytic priority: how much would the answer change the assessment? Classify as High / Medium / Low. Flag questions that are currently unanswerable (collection gap) versus those answerable from existing sources.

## Step 4 — Produce the question map and key unknowns summary (write)
Emit the full question table organized by interrogative with priority ratings. Write the key-unknowns summary highlighting the highest-priority unanswered questions and what analytic collection actions they imply.

## Anti-criteria (must NOT happen)
- do not answer questions during the generation phase — answering during generation anchors and prunes the question space
- do not treat a sparse interrogative category (e.g., only one 'Why' question) as complete — push for multiple questions per category
- do not discard awkward or uncomfortable questions; the most uncomfortable are often the most analytically important

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
