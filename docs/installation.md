# Installation

Install only the `skills/product-development-workflow/` directory, including its
references, assets, and metadata. The rest of this repository develops and tests
the skill; it does not belong in your project's skill installation.

This guide describes a manual, project-local installation for supervised testing.
It does not install plugins, change global settings, or migrate your project's
process automatically. End-to-end discovery and adoption still need verification
in your target Codex environment.

## Before you start

- Use Codex with local skill discovery. Full delivery also needs native task
  coordination, internal agents, and independent reviews; check only the
  capabilities needed for your next step.
- The commands use Git and a POSIX shell on macOS or Linux. On Windows, use
  equivalent file-copy operations or a POSIX environment such as WSL.
- Choose the target project and review its existing instructions and unfinished
  work. Do not replace an existing skill or `AGENTS.md` without checking it.
- Check for another `product-development-workflow` installation and the older
  `product-development-cycle`. Do not activate both for the same work.

Codex's documented project-local discovery directory is `.agents/skills/`.
User-level skills can affect multiple projects, so this guide uses project scope.
Duplicate names are not merged. See the official
[local skill discovery documentation](https://developers.openai.com/codex/skills#where-to-save-skills).

## 1. Select an immutable version

Choose a reviewed full commit SHA from this repository and record it with your
project's existing setup notes. A moving branch name such as `main` is not a
reproducible version. There is no stable release promised by this candidate.

Clone into a new directory outside your target project. Replace the two example
values below before running the commands:

```sh
pdw_source="/absolute/path/to/new/pdw-source"
pdw_revision="FULL_REVIEWED_COMMIT_SHA"
git clone https://github.com/WorkKroG/product-development-harness.git "$pdw_source"
git -C "$pdw_source" checkout --detach "$pdw_revision"
git -C "$pdw_source" rev-parse HEAD
```

Confirm the printed SHA matches your selection and the checkout succeeded before
continuing. Keep this source copy unchanged while testing that version.

## 2. Copy the package into your project

Run from the target project's root in a shell where `pdw_source` still identifies
the checked-out source. The guard refuses to overwrite an existing folder or symlink:

```sh
pdw_destination=".agents/skills/product-development-workflow"
if [ -e "$pdw_destination" ] || [ -L "$pdw_destination" ]; then
  printf '%s\n' "A skill already exists at the destination. Stop and inspect it."
else
  mkdir -p .agents/skills &&
    cp -R "$pdw_source/skills/product-development-workflow" "$pdw_destination"
fi
```

Choose explicitly whether this project-local copy should be committed for the
team or remain local. Installation alone does not authorize a commit or publication.
Do not copy this repository's root `AGENTS.md`, `baseline/`, tests, or development
documents into the target project.

## 3. Verify content and discovery

Compare the installed folder with the selected source:

```sh
diff -qr "$pdw_source/skills/product-development-workflow" \
  .agents/skills/product-development-workflow
```

No differences and exit status `0` confirm the copied files match. This comparison
does not prove that a running Codex task loaded them.

Open the target project in Codex. Select the skill using the available skill
picker or mention `$product-development-workflow`. Ask it to report the resolved
skill path and available identity evidence before using it. Confirm the path is
the project-local copy you compared. If loaded identity cannot be established,
record it as unknown rather than treating the selected SHA as runtime proof.

Codex detects local skill changes automatically; restart it if the skill does not
appear. The official [skills guide](https://developers.openai.com/codex/skills)
describes discovery and invocation for the supported clients. Then follow
[your first audit](usage.md#an-existing-project).

## Update, rollback, or remove

Make changes at a safe task boundary. Preserve unfinished work and the current
version selection before changing skill files; do not change instructions under
an active implementation or review without reconciling that task.

- **Update:** choose a new reviewed SHA and prepare a separate source checkout.
  Compare it with the installed copy, preserving local modifications. Move the
  old skill folder to a named backup outside all skill-discovery directories,
  then copy the new package into the empty destination. Repeat content and
  discovery checks, and update the existing version note.
- **Rollback:** restore that exact saved folder, or reinstall the previous recorded
  SHA into an empty destination. Repeat both checks and reconcile active tasks.
  Rolling back skill instructions does not undo project code or data changes.
- **Remove:** move only `.agents/skills/product-development-workflow` to a backup
  outside discovery directories or to the trash. Restart Codex if necessary.
  Keep your project's work and decisions; they are not disposable installation files.

For an old user-level installation, first identify its actual loaded path. Codex
also documents per-path disabling in its
[skill configuration](https://developers.openai.com/codex/skills#enable-or-disable-local-codex-skills).
Do not disable a shared copy without considering other projects that use it.

## Troubleshooting

| Symptom | Check |
|---|---|
| Skill is missing | Confirm the project root and `.agents/skills/product-development-workflow/SKILL.md`; restart Codex if discovery has not refreshed. |
| Two versions appear | Identify resolved paths, select one, and explicitly disable or move the unwanted copy outside discovery directories. |
| Skill keeps restarting discovery | Ask it to audit and reuse existing decisions; point to the project's current sources of truth. |
| Task coordination is unavailable | Keep independent read-only work in scope; leave the dependent delivery step blocked rather than inventing tasks or approvals. |
| A command or install is denied | Respect the denial and resolve the required permission; do not switch tools or identities to bypass it. |
