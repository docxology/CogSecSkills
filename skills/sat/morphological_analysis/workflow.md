# Workflow — Morphological Analysis

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Decompose into parameters (read, reason)
Read the problem statement and identify 3–7 independent parameters that together define the space of possible configurations. For each parameter, enumerate 2–5 discrete values it could take. Record parameters as rows and values as columns in the morphological box.

## Step 2 — Prune impossible combinations (reason)
Cross each parameter value against all values of every other parameter. Mark any combination that is logically impossible, physically infeasible, or ruled out by confirmed evidence. Document the ruling-out reason for every pruned cell. The surviving cells form the feasible scenario inventory.

## Step 3 — Assess surviving scenarios (reason)
For each surviving combination, assess: (a) current evidential support (supported / neutral / contradicted by available reporting), (b) likelihood given base rates and context, (c) consequence if realized, and (d) whether current collection can distinguish this scenario from its neighbors.

## Step 4 — Report findings (write)
Produce the morphological box as a table, the scenario inventory as an annotated list, and priority findings calling out the most-likely scenario, the most-dangerous scenario, and any collection gap that prevents disambiguation of high-consequence cells.

## Anti-criteria (must NOT happen)
- do not prune cells based on intuition or familiarity before documenting the logical or evidential basis for exclusion
- do not allow the parameter list to be dominated by factors whose values are already known — the technique's value is in the under-explored dimensions
- do not report only the most-likely scenario; the most-dangerous scenario must always appear in the output even if assessed as low probability

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
