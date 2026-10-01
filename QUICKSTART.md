# CogSecSkills Quickstart

CogSecSkills is the defensive skill library at
`https://github.com/docxology/CogSecSkills`. This page gets a reader from clone
to one bounded harness invocation.

## Install

```bash
git clone https://github.com/docxology/CogSecSkills.git
cd CogSecSkills
uv sync
```

Without `uv`:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

Regenerating the docs/manuscript/release **figures** (`manuscript-assets --write`)
additionally needs the optional `figures` extra:

```bash
uv sync --extra figures        # or: python -m pip install -e ".[figures]"
```

## Validate The Local Library

```bash
uv run python -m cogsecskills validate
uv run python -m cogsecskills doctor
uv run python -m cogsecskills scenarios --check
uv run python -m cogsecskills examples --check
uv run python -m cogsecskills evals --check
uv run python -m cogsecskills dashboard --check
uv run python -m cogsecskills release-metadata --check
uv run python -m cogsecskills manuscript-assets --check

# Opt-in, never a gate: run scenarios through a live harness (exploratory screening).
# See docs/live-eval.md — uv run python -m cogsecskills eval-live --harness claude
```

`uv run` uses the project environment without requiring shell activation. If
you used the pip setup above, replace `uv run python` with `python`. Figure
regeneration needs the `figures` extra; checking committed PNGs does not.

Most `--check` gates compare committed generated files under `docs/` and
`skills/` against what the current sources regenerate; only run the matching
`--write` after editing a source surface (see "Keep Outputs Current" below).

Expected local state is zero validation errors, zero quality findings, and
scenario, worked-example, offline-eval, dashboard, and release-metadata
fixtures that are current. These gates
prove source and contract coherence; they do not prove live model behavior or
field effectiveness.

For a visual scan after validation, open `docs/quality-dashboard.html` locally
or read the Markdown mirror at `docs/quality-dashboard.md`.

## Find And Inspect A Skill

```bash
uv run python -m cogsecskills route "verify a viral claim before sharing it" --limit 5
uv run python -m cogsecskills show osint_integrity.claim_provenance_verification
```

The route command suggests candidate skills. The show command prints the
harness-neutral contract for the selected skill.

## Bind A Skill Into An Agent Harness

For the selected skill, load these files together:

```text
skills/osint_integrity/claim_provenance_verification/SKILL.md
skills/osint_integrity/claim_provenance_verification/workflow.md
skills/osint_integrity/claim_provenance_verification/harness/codex.md
```

Use `harness/claude.md`, `harness/codex.md`, or `harness/hermes.md` for the
default harnesses. If `cogsecskills.yaml` configures another harness, regenerate
adapters with:

```bash
uv run python -m cogsecskills definitions --write
uv run python -m cogsecskills definitions --check
uv run python -m cogsecskills validate
```

The adapter is a binding layer. It should not replace the skill definition or
the neutral workflow.

## Keep Outputs Current

After skill, registry, scenario, or manuscript-source edits:

```bash
uv run python -m cogsecskills definitions --check
uv run python -m cogsecskills scenarios --check
uv run python -m cogsecskills examples --check
uv run python -m cogsecskills evals --check
uv run python -m cogsecskills dashboard --check
uv run python -m cogsecskills release-metadata --check
uv run python -m cogsecskills manuscript-assets --check
```

See `docs/harness-cookbook.md`, `docs/claim-boundaries.md`,
`docs/skill-worked-examples.md`, and `docs/evaluation-readiness.md` for bounded
examples.
