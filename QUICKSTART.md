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
python -m pip install -e .
```

## Validate The Local Library

```bash
PYTHONPATH="src:." python -m cogsecskills validate
PYTHONPATH="src:." python -m cogsecskills doctor
PYTHONPATH="src:." python -m cogsecskills scenarios --check
PYTHONPATH="src:." python -m cogsecskills examples --check
PYTHONPATH="src:." python -m cogsecskills evals --check
PYTHONPATH="src:." python -m cogsecskills dashboard --check
PYTHONPATH="src:." python -m cogsecskills release-metadata --check
```

Expected local state is zero validation errors, zero quality findings, and
scenario, worked-example, offline-eval, dashboard, and release-metadata
fixtures that are current. These gates
prove source and contract coherence; they do not prove live model behavior or
field effectiveness.

## Find And Inspect A Skill

```bash
PYTHONPATH="src:." python -m cogsecskills route "verify a viral claim before sharing it" --limit 5
PYTHONPATH="src:." python -m cogsecskills show osint_integrity.claim_provenance_verification
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
PYTHONPATH="src:." python -m cogsecskills definitions --write
PYTHONPATH="src:." python -m cogsecskills definitions --check
PYTHONPATH="src:." python -m cogsecskills validate
```

The adapter is a binding layer. It should not replace the skill definition or
the neutral workflow.

## Keep Outputs Current

After skill, registry, scenario, or manuscript-source edits:

```bash
PYTHONPATH="src:." python -m cogsecskills definitions --check
PYTHONPATH="src:." python -m cogsecskills scenarios --check
PYTHONPATH="src:." python -m cogsecskills examples --check
PYTHONPATH="src:." python -m cogsecskills evals --check
PYTHONPATH="src:." python -m cogsecskills dashboard --check
PYTHONPATH="src:." python -m cogsecskills release-metadata --check
PYTHONPATH="src:." python -m cogsecskills manuscript-assets --check
```

See `docs/harness-cookbook.md`, `docs/claim-boundaries.md`, and
`docs/skill-worked-examples.md`, and `docs/evaluation-readiness.md` for bounded
examples.
