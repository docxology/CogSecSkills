# CORE-04: render_definition writes definition fields (tags/triggers/inputs/outputs) without validation, so authored skills can fail SkillSpec parsing while the author command exits 0

|Field|Value|
|---|---|
|Audit ID|`CORE-04`|
|Lens|`CORE`|
|Severity|`medium`|
|Red-team verdict|`VALID`|
|Status|Open (validated 2026-09-10)|
|Tracking|[GitHub issue](https://github.com/docxology/CogSecSkills/issues/9)|

## Summary
`render_definition` coerces/validates only the tool verbs; `tags`, `triggers`, `inputs`, and `outputs` from the definition JSON are written into the generated `skill.yaml` with no type or shape checks. A definition with e.g. `tags: [1]`, `inputs: [{name: x, required: "yes"}]`, or an io missing `name` therefore produces a tree that `SkillSpec.from_mapping` rejects — while `cogsecskills author` prints "authored N files" and exits 0, contradicting the module docstring's "every authored skill passes the validator by construction" guarantee.

## Evidence
`src/cogsecskills/authoring/author.py:357-366`:

```python
"tags": list(definition.get("tags") or ["cognitive-security", entry.group]),
"triggers": list(definition.get("triggers") or [entry.name.lower()]),
...
"inputs": definition.get("inputs"),
```

Only verbs are coerced (`author.py:361`: `ToolVerb.coerce(t["verb"]).value`); inputs/outputs are embedded verbatim into the YAML payload (`author.py:366-377`). Compare the module docstring at `author.py:7-8`: "every authored skill passes the validator by construction", and the CLI success path at `cli.py:417-419`: `written = render_definition(...)` / `print(f"authored {len(written)} files for {definition.get('id')}")` / `return 0`.

The verifier confirmed the load-time gates fire only later: `spec.py:113-117` (`SkillIO.from_obj` raises "io {name!r} field 'required' must be a boolean"), `spec.py:126-134` (`_as_str_list` raises "items must be strings"), `spec.py:100` (missing io `name`). Nothing at author time calls `SkillSpec.from_mapping`; the round-trip tests (`tests/authoring/test_cogsecskills_definitions_branches.py:90,118`) only assert success for well-formed definitions.

## Impact
The authoring pipeline's core promise — authored trees that load — is not enforced: users get a green exit code and a written skill tree that fails at first load with a spec error far from the input mistake. Blast radius is bounded (the loader still rejects rather than shipping wrong data, and the input is fixable), but the false success signal is a real contributor footgun.

## Remediation
In `render_definition` (`author.py`), after building the payload in `_skill_yaml`, round-trip it before writing: `SkillSpec.from_mapping(yaml.safe_load(dumped))`, letting the resulting `SpecError` surface as an `AuthorError` naming the definition. Alternatively validate the definition's `tags`/`triggers`/`inputs`/`outputs` up front via `SkillTool`/`SkillIO.from_obj`. Add a test that a definition with `tags: [1]` or `inputs: [{name: x, required: "yes"}]` fails the author command instead of exiting 0.

## Audit trail
- Discovered by the CORE lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `VALID`, confidence `high`.
- Verifier notes: Independently re-derived. (1) Quote and line numbers exact (tags=357, triggers=358, tools verb coercion=361, inputs=366). (2) Mechanism confirmed: only the 'tools' verbs are coerced through ToolVerb.coerce (author.py:361); tags/triggers pass through `list(...)` with no type check, and inputs/outputs are embedded verbatim into the YAML payload (author.py:366-377) with no SkillIO/SkillTool coercion. (3) Spec-side gates exist but only at load time: spec.py:113-117 SkillIO.from_obj raises "io {name!r} field 'required' must be a boolean" for non-bool required; spec.py:126-134 _as_str_list raises "items must be strings" and "must be a string or list of strings"; missing io 'name' raises at spec.py:100. A definition with tags:[1], inputs:[{name:x, required:'yes'}], or an io missing 'name' therefore renders skill.yaml that SkillSpec.from_mapping rejects, while render_definition writes all files without any round-trip validation (author.py:576-607) and cli.py `author` returns 0. (4) Not handled elsewhere: render_definition and rendered_definition_files contain no SkillSpec.from_mapping call; author_batch only catches AuthorError/SpecError/ValueError from rendering itself (author.py:655-662) — the SpecError fires later at loader.py:52, not at author time; the round-trip tests in tests/authoring/test_cogsecskills_definitions_branches.py:90,118 only assert from_mapping succeeds for well-formed definitions, so no test enforces validation of malformed definition fields. (5) One wording nuance, not enough to invalidate: the docstring sentence is scoped to harness verb bindings ('Adapters are generated to bind exactly the declared verbs, so every authored skill passes the validator by construction'), so the 'by construction' guarantee is arguably about verbs only — but the code context (author.py:1-4 'the six conforming files... skill.yaml') plus the total lack of field validation still yields authored trees that cannot load, matching the finding's substance. Severity medium is fair: broken authored artifacts with a false success exit, but limited blast radius (fixable input, loader still rejects rather than shipping wrong data).
<!-- PR and issue links are added to the Tracking field after filing. -->
