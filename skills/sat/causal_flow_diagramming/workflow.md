# Workflow — Causal Flow Diagramming

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Define behavior-over-time and boundary (read, reason)
Start by articulating the specific behavior pattern the diagram must explain (e.g., 'disinformation share rate accelerates for 72 hours then plateaus'). Define the scope boundary: what actors, time horizon, and causal chains are inside the model. This prevents scope creep and keeps the diagram tractable. Identify 5–15 key variables as starting nodes.

## Step 2 — Map causal links and polarities (reason)
For each pair of variables that are causally connected, draw a directed arrow and assign polarity: + if an increase in the cause produces an increase in the effect (all else equal), – if it produces a decrease. Work forward from drivers and backward from the target behavior. Flag any link whose polarity is contested or uncertain — these are key analytic uncertainties.

## Step 3 — Identify and type feedback loops (reason)
Trace every closed loop in the diagram (a path that returns to its starting variable). Count the negative (–) links: even number = reinforcing loop (R) — labels it with a behavior tendency (exponential growth or collapse); odd number = balancing loop (B) — labels it with its tendency (goal-seeking or oscillation). Name each loop descriptively ('Credibility Erosion Spiral', 'Correction Saturation Balancer'). In influence-operation contexts, R-loops are the amplification engines to interdict; B-loops are the natural dampeners to reinforce.

## Step 4 — Mark delays and non-obvious paths (reason)
Identify where significant time lags exist between a cause and its effect (e.g., 'policy change → public awareness: 3–6 month lag'). Mark these with delay notation. Non-obvious paths are often the most analytically valuable: a variable affecting a distant node through three intermediaries may be the real driver. Trace all paths ≥3 links long and verify each intermediate link.

## Step 5 — Identify leverage points and produce outputs (reason, write)
Apply Meadows' hierarchy: interventions on numbers (quantities) are weak; on feedback loop structures (adding or removing a link) are strong; on paradigm or goal of the system are strongest. Rank the top 3–5 leverage points by estimated impact and feasibility. Write the loop inventory table. Produce the causal flow diagram in structured markdown notation (indented node list with → links and polarity labels). Write the leverage-point assessment with one paragraph on unintended consequence risks per intervention.

## Anti-criteria (must NOT happen)
- Do not omit polarity labels on causal links — unlabeled arrows make loop typing impossible and reduce the diagram to an influence diagram without behavioral implications
- Do not draw causal links between variables that are merely correlated without a plausible causal mechanism — correlation-as-causation is the primary failure mode of this technique
- Do not let the diagram grow beyond approximately 20 nodes without partitioning into sub-diagrams — cognitive overload defeats the purpose of externalizing the structure
- Do not identify leverage points without also noting the direction of intervention and the risk of reinforcing unintended loops — 'pulling the wrong lever' in a feedback system can accelerate the problem

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
