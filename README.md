# Product Development Workflow

A Codex skill for moving a digital product from an idea or existing codebase to
its next useful, verified result. Identify what is already known, decide what
needs attention next, and coordinate implementation and independent review
without repeating completed work.

**Unreleased candidate — experimental, for supervised testing.** This is
an instruction-based workflow, not an autonomous project-management service.

## Get started

1. Follow the [installation guide](docs/installation.md) to install a pinned copy
   of `skills/product-development-workflow/` into your chosen project.
2. Open that project in Codex and verify that the expected skill is available.
3. Start with an audit before authorizing changes:

```text
$product-development-workflow
Inspect this existing project without changing files. Identify its current
stage, reusable decisions and evidence, and any conflicts with this workflow.
Recommend one bounded next step. Do not restart discovery or overwrite AGENTS.md.
```

For a new product, ongoing development, and resuming interrupted work, see the
[usage guide](docs/usage.md).

## How it works

- **Start where the product is.** Reuse existing research, decisions, code, and
  checks; revisit only what is missing or invalidated.
- **Choose the next decision.** The workflow covers discovery, viability, scope,
  UX, architecture, delivery, verification, release, and learning. A gate means
  a decision supported by evidence, not a requirement to create a document.
- **Keep effort proportional.** Detail the nearest deliverable; treat later
  scale as assumptions and revisit triggers. Reassess unproductive correction loops.
- **Separate delivery roles.** The Product coordinator handles project-wide
  direction. You work with a Task coordinator on an approved module; bounded
  internal agents handle planning, implementation, independent review, and final
  verification when the required native capabilities are available.
- **Keep control.** Installing the skill does not authorize project edits,
  spending, publication, merge, or release. Material decisions stay with you.

The agent instructions live in [SKILL.md](skills/product-development-workflow/SKILL.md).
You do not need to read the development specification to use the skill.

## Requirements and known limitations

The current workflow targets Codex. Full coordination depends on native task,
subagent, messaging, and review capabilities; availability must be checked in
your environment. Missing capabilities must be disclosed, not simulated.
Specialist tools are needed only for the stage that actually requires them.

A bounded synthetic pilot exercised selected workflow behaviors. It did not
prove live cross-task routing, production readiness, or end-to-end installation,
upgrade, and rollback in another project. Start with a supervised, low-risk task;
see the [validation summary](docs/development/validation.md) for the exact limits.

## For contributors

[Development documentation](docs/development/README.md) contains the specification,
project decisions, historical plans, provenance, and verification instructions.
[CHANGELOG.md](CHANGELOG.md) summarizes the current candidate.

This skill evolved from `product-development-cycle`. The historical `baseline/`
is not the package to install. See [sources and provenance](docs/development/SOURCES.md)
for the original materials and redistribution boundaries; no license is inferred
from the repository being public.
