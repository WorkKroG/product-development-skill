# Using Product Development Workflow

[Install and verify one version](installation.md) first. The skill provides
instructions to Codex; it does not create a background service or authorize
actions simply because it is present.

## An existing project

Start with a read-only audit:

```text
$product-development-workflow
Audit this existing project without modifying files. Read its current AGENTS.md,
decisions, product documents, task state, and unfinished work. Reuse valid evidence.
Identify conflicting rules and propose only the process changes needed for one
small next task. Do not restart completed discovery or overwrite existing guidance.
```

Review the proposed next step and genuine conflicts. Agree on a safe point to
adopt the workflow, preserve work in progress, and approve only necessary changes
to existing guidance. Templates are starting points when an artifact is missing,
not files that must replace yours.

For the first trial, choose a low-risk real task with a clear outcome. Agree on
its scope, exclusions, relevant checks, and review. Keep the trial supervised;
installation and a plausible response alone do not demonstrate successful adoption.

## A new product

```text
$product-development-workflow
I want to explore a product that helps [users] solve [problem]. We are at the
idea stage. Identify the most important unknown and recommend the smallest useful
next investigation. Do not implement or purchase anything yet.
```

You do not need a full PRD, production architecture, or detailed financial model
to begin. Depth depends on the current stage and actual risk. The workflow
distinguishes a prototype, MVP, two scaling stages, and mature operation; user
counts alone do not establish capacity.

## What the first response should contain

Expect the current gate, evidence found, missing information or assumptions,
risks, one recommended next action, exit criteria, and the next gate. A gate is
a decision checkpoint. Existing evidence can satisfy it; a new document is not
automatically necessary.

The lifecycle covers context and discovery, a light viability decision before
journey mapping, scope and requirements, proportionate finance, UX and risk,
technical and delivery planning, implementation, verification, release, and learning.
The [lifecycle reference](../skills/product-development-workflow/references/lifecycle.md)
contains detailed criteria if you need them.

## Where work and decisions happen

| Role | Responsibility | Where you participate |
|---|---|---|
| Product coordinator | Project direction, shared architecture, dependencies, and cross-task decisions | Agree on project-wide priorities and material changes. |
| Task coordinator | One approved module or bounded delivery scope | Discuss its plan, local requirements, feedback, and acceptance here. |
| Internal agents | Separate PLAN, Implementation, Change Review, and FINAL sessions with bounded inputs | The Task coordinator manages these; you should not relay routine messages. |

A new user-owned task requires your authorization and native platform support.
Internal agents and user-owned tasks are different execution types. Reviewers
receive requirements and the exact candidate independently of the author's
conversation. Changes after review require review of the new candidate.

Task coordinators report only meaningful transitions upward: `ACTIVE`,
`ESCALATION_REQUIRED`, `READY_FOR_INTEGRATION`, `DONE`, or `CANCELLED`, with a short
reason and evidence pointer. Local decisions stay in the Task; changes affecting
shared architecture, scope, dependencies, or material cost/risk/schedule go to
Product. Native capability availability is checked, not assumed.

## Resume without restarting

```text
$product-development-workflow
Resume from the current repository, task, and review state. Preserve unfinished
work, reconcile stale status notes with fresh evidence, and do not replay completed
steps. Report any skill-version ambiguity and recommend one next action.
```

Keep consequential decisions and evidence pointers in the project's existing
artifacts so a resumed task does not depend only on conversation history. Do not
build a second Issue/PR status database in documents.

## Your control and the workflow's limits

- Routine technical decisions stay inside an approved task. Changed scope,
  material risks, spending, installation, publication, and other external actions
  still need their applicable authorization. Merge and release remain human decisions.
- Supporting process should help the current deliverable. After two consecutive
  correction/review cycles without a new accepted result, the coordinator must
  reassess; that is not permission to waive safety or independent review.
- Missing specialist or native capabilities should be disclosed. A requested model
  is not proof of the model actually used; unknown runtime identity stays unknown.
- The skill does not guarantee unattended operation, production readiness, or a
  particular amount of context remaining. A passing structural check is not proof
  of correct end-to-end behavior.

During your trial, record what you asked, the selected skill version, the observable
result, and concrete failures in existing task notes. Do not publish private
project content as feedback without permission. See the
[validation limits](development/validation.md) for what has and has not been tested.
