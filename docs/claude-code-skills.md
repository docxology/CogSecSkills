# Installing CogSecSkills As Native Claude Code Skills

This guide installs the library as **native Claude Code skills** — the kind that
appear in the `/` skill menu and are invoked through the Skill tool. It is the
Claude-Code-specific complement to [`harness-installation.md`](harness-installation.md),
which covers the generic "load `SKILL.md` + `workflow.md` + `harness/<name>.md`"
pattern for any harness.

## Why a separate install step is needed

Claude Code discovers a skill only when it finds `SKILL.md` at:

```text
<project>/.claude/skills/<skill-name>/SKILL.md      # project-scoped
~/.claude/skills/<skill-name>/SKILL.md              # personal, all projects
```

The library's on-disk layout does not match that shape directly:

- Skills live two levels deep at `skills/<group>/<slug>/SKILL.md`. Claude Code
  does **not** recurse into grouping subdirectories — each skill folder must be a
  direct child of `.claude/skills/`.
- The skill `name` in frontmatter is the dotted id (e.g.
  `sat.analysis_of_competing_hypotheses`). Claude Code skill names are
  kebab-case (lowercase letters, digits, hyphens), so the dotted/underscored
  form is not a valid Claude Code skill name.

So the skills must be **flattened and renamed** into `.claude/skills/`. The
canonical `skills/` tree stays the source of truth; the `.claude/skills/` copies
are a generated install target.

## Install all skills into a project

Run from the repository root. This installs every skill as
`.claude/skills/cogsec-<slug>/`, copying the full skill folder (so `workflow.md`
and `harness/` stay intact) and rewriting each `SKILL.md` frontmatter `name:` to
the kebab folder name.

```bash
DEST=".claude/skills"
mkdir -p "$DEST"
find skills -name SKILL.md | sort | while IFS= read -r skillmd; do
  dir="$(dirname "$skillmd")"
  slug="$(basename "$dir")"
  name="cogsec-${slug//_/-}"            # group-cluster prefix; underscores -> hyphens
  d="$DEST/$name"
  rm -rf "$d"
  cp -R "$dir" "$d"
  awk -v n="$name" 'BEGIN{done=0} /^name:/ && !done {print "name: " n; done=1; next} {print}' \
    "$d/SKILL.md" > "$d/SKILL.md.tmp" && mv "$d/SKILL.md.tmp" "$d/SKILL.md"
done
echo "Installed $(ls -1 "$DEST" | wc -l) skills into $DEST"
```

To install for **every** project instead, set `DEST="$HOME/.claude/skills"`. The
personal directory is watched live, so skills appear without restarting; a brand
-new project-level `.claude/skills/` directory is only watched after the next
Claude Code start.

## Verify

```bash
ls -1 .claude/skills | head                       # cogsec-<slug> folders
ls -1 .claude/skills | wc -l                      # expect the implemented count
head -4 .claude/skills/cogsec-analysis-of-competing-hypotheses/SKILL.md
```

Then, in a Claude Code session started in this repo, the skills appear in `/`
(for example `/cogsec-analysis-of-competing-hypotheses`). The frontmatter
`description` is what Claude Code uses to decide when to surface each skill.

## Keep the install current

`.claude/skills/` is a generated copy, not a source. After editing canonical
skills (`definitions/<group>/<slug>.yaml` → `definitions --write`), re-run the
install snippet to re-sync. Treat `.claude/skills/` like other regeneratable
outputs: it can be rebuilt from `skills/` at any time.

## Boundary

These are defensive, educational skills. Each `SKILL.md` carries its own
defensive boundary and misuse-redirect section; installing them into Claude Code
does not change that contract. See
[`claim-boundaries.md`](claim-boundaries.md) for what the local gates prove and
do not prove.
