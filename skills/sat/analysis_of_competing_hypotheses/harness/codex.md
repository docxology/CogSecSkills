# Codex adapter — Analysis of Competing Hypotheses

Binds the neutral `skill.yaml` tool verbs to a Codex / `codex exec` agent's
tool surface. Follow `../workflow.md`; map each step's verb as below.

| Neutral verb | Codex binding | Notes |
|--------------|---------------|-------|
| `read`   | `shell` (`cat`, `sed`, `rg`) on provided files | Evidence is passed as files or stdin. |
| `search` | `shell` + (optional) web tool | Gather evidence; if no web access, request it from the caller. |
| `reason` | private model reasoning | Matrix construction and scoring with concise rationale in the product. |
| `write`  | `apply_patch` / stdout | Write the matrix + ranking to an output file or stdout. |

## Invocation
Provide this file plus `../workflow.md` and `../skill.yaml` in the task context.
Codex runs the eight steps non-interactively and writes the ACH product to the
path given by the caller (default: stdout as Markdown).

## Output contract
Identical to the neutral spec: matrix table (C/I/N), inconsistency ranking,
indicators, calibrated confidence. Deterministic given the same inputs.
