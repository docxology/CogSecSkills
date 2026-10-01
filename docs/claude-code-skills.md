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
canonical definitions own the substance; the rendered `skills/` tree supplies
the install files, and the `.claude/skills/` copies
are a generated install target.

## Install all skills into a project

Run from the repository root. This installs every skill as
`.claude/skills/cogsec-<slug>/`, copying the full skill folder (so `workflow.md`
and `harness/` stay intact) and rewriting each `SKILL.md` frontmatter `name:` to
the kebab folder name.

The first-install procedure below checks every destination before copying and
refuses to replace an existing directory, file, or symlink. Run it in Bash (the
snippet starts Bash explicitly, including on macOS):

```bash
bash <<'BASH'
set -euo pipefail
test -d skills  # run from the library checkout
DEST=".claude/skills"  # personal install: "$HOME/.claude/skills"
# Preflight the complete set before writing any skill folder.
while IFS= read -r skillmd; do
  dir="$(dirname "$skillmd")"
  slug="$(basename "$dir")"
  name="cogsec-${slug//_/-}"
  if [ -e "$DEST/$name" ] || [ -L "$DEST/$name" ]; then
    echo "Existing destination: $DEST/$name; review it before installing." >&2
    exit 1
  fi
done < <(find skills -name SKILL.md | sort)

mkdir -p "$DEST"
count=0
while IFS= read -r skillmd; do
  dir="$(dirname "$skillmd")"
  slug="$(basename "$dir")"
  name="cogsec-${slug//_/-}"
  d="$DEST/$name"
  mkdir "$d"  # fails if a destination appeared after preflight
  cp -R "$dir/." "$d/"
  awk -v n="$name" 'BEGIN{done=0} /^name:/ && !done {print "name: " n; done=1; next} {print}' \
    "$d/SKILL.md" > "$d/SKILL.md.tmp"
  mv "$d/SKILL.md.tmp" "$d/SKILL.md"
  count=$((count + 1))
done < <(find skills -name SKILL.md | sort)
echo "Installed $count skills into $DEST"
BASH
```

For a personal install, change `DEST` inside the script to
`"$HOME/.claude/skills"`. See the [official Claude Code skill
locations](https://code.claude.com/docs/en/skills#choose-where-skills-load) for
current discovery behavior. Start a fresh Claude Code session after installation
and verify the loaded skills there.

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
first-install snippet into a fresh staging directory. Compare the regenerated
files with the existing installed copies, preserve any local changes, and replace
only the specific copies you own after review. The first-install snippet stops
on existing destinations; it never deletes another skill.

## Boundary

These are defensive, educational skills. Each `SKILL.md` carries its own
defensive boundary and misuse-redirect section; installing them into Claude Code
does not change that contract. See
[`claim-boundaries.md`](claim-boundaries.md) for what the local gates prove and
do not prove.
