# Product Development Workflow — Module 6 Evidence-Retention Recovery Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILLS: use
> `superpowers:subagent-driven-development`, `superpowers:test-driven-development`, and
> `superpowers:verification-before-completion` to execute this plan task-by-task. The Task
> coordinator must use distinct internal Implementation, behavioral Evaluation, group Review,
> Module Change Review, and correction sessions. No worker may infer Task 10, integration, FINAL,
> publication, installation, or release authority from this plan.

**Identity:** `MODULE6-RECOVERY-PLAN-v1`.

**Goal:** Rerun all 21 selected Module 6 cases honestly from scratch, retain every current raw
input, executor output, evaluator input/output, and transcript/operation record in a durable
ignored workspace through exact-head Module Change Review and the later Task 10 decision, then
publish only evidence claims whose new SHA-256 identities resolve to those retained bytes.

**Architecture:** This is a Gate 14 verification recovery addendum, not a product-scope change.
It replaces only the accepted predecessor plan's ephemeral `/private/tmp` evidence-retention
design with an append-preserving, content-addressed workspace under
`.superpowers/sdd/2026-09-12-module-6-evidence-retention-recovery/`. Four bounded case groups write
only disjoint durable directories after shared schemas, input snapshots, and product identities
are stable; independent evaluators and reviewers read exact inputs/candidates without the author's
conversation; one later assembler is the sole writer of tracked public evidence.

**Tech Stack:** Markdown, JSON, JSON Lines, Python 3 standard library (`hashlib`, `json`,
`pathlib`, `shutil`, `subprocess`, `unittest`), local Git, and internal Codex agents. No new Python
package, network access, GitHub service action, or external tool is required.

**Spec:** `SPEC.md` §§6–8 and §§10–13; `EVALUATION.md`; reviewer-only
`tests/scenarios.md`; predecessor `MODULE6-PLAN-v1` at exact SHA-256
`6037149b9a70cdeba4b8f1fd4fcce460b9206730665c8aa69f4ee781eb5c4777`; finding
`M6-CR3-I01` and regression gap `M6-CR3-M01` in the ignored review record
`.superpowers/sdd/2026-09-11-module-6-quietfollow-pilot/task9-final-review-v3.json`.

## Recovery identity, predecessor, and authority

- Plan-author base and containing-commit parent:
  `b0e0c85dd0bf50e84ba1ce14ed4a985be7676002`, tree
  `fb7d90cd33b8604a51b53059b7602463f043e5f8`, branch
  `codex/module6-quietfollow-pilot`.
- Predecessor Module 6 implementation base:
  `f47263ce545c5185b3ec836c95fe341d1b3e5715`.
- Predecessor Module 6 accepted plan commit:
  `8614c2d3c465ce86ab4332917bc435d4d2b10754`.
- Predecessor planning/source base:
  `1d9b6f8242fbea8548a423b172534b8c8d20b6e0`.
- The predecessor accepted plan file remains byte-identical and retains identity
  `MODULE6-PLAN-v1`; this addendum supersedes only its temporary-authoritative evidence storage
  and permits honest successor execution/evaluation identities and public digests.
- The vanished artifacts reported by `M6-CR3-I01` are not recoverable evidence. Never recreate
  their hashes from summaries, claim that reconstructed prose is the original byte sequence, or
  reuse their PASS as current credit. Preserve their public identities as `superseded` historical
  records and create new `current` identities from fresh execution.
- The exact triggering finding resolved only 7 of 31 accessible case-input references, 0 of 42
  output-evidence digests, and 0 of 21 transcript-evidence digests. The predecessor v2 review's
  historical attestation of 31/31, 42/42, and 21/21 resolution is not raw evidence and cannot bind
  head `b0e0c85dd0bf50e84ba1ce14ed4a985be7676002`.
- `M6-CR3-M01` separately found that README was outside permanent public-binding coverage and that
  its local-synthetic boundary was not fully asserted. Recovery addresses both without treating
  the intentionally public historical `.local-handoff` name as a leak.
- Owner/Product authorized all 21 selected reruns, durable ignored retention, successor evidence
  identities, and the directly dependent public evidence/test corrections in this plan. That
  authorization does not include Task 10, integration, FINAL, push, PR, GitHub mutation, global
  skill installation, deployment, publication, production release, external research, spend, or
  real-user-data operations.
- The final state of this addendum is a Task 9 recommendation only: `READY_FOR_CHANGE_REVIEW`
  after the stable candidate commit and full verification, then a task-local
  `READY_FOR_INTEGRATION` recommendation only after a clean exact-head Module Change Review.
  Neither state performs integration or satisfies `DONE`. Because a PR is unauthorized and absent,
  the latter is not an upward `READY_FOR_INTEGRATION` event that claims a ready PR.

## Binding sources and review order

Every executor/reviewer brief names these sources, but executor bundles include only the minimum
case-relevant subset described below. Reviewers read binding requirements independently rather
than trusting author or executor summaries.

1. `AGENTS.md` for authority, topology, models, review invalidation, GitHub restrictions, and
   verification rules.
2. `README.md`, `SPEC.md`, `AUDIT.md`, `EVALUATION.md`, `docs/PROJECT_STATUS.md`, and
   `docs/validation.md` for current claims and accepted product boundaries.
3. `docs/superpowers/plans/2026-09-11-module-6-quietfollow-pilot.md`, exact identity above.
4. Active `skills/product-development-workflow/` sources and the immutable Module 5 inputs named
   by the predecessor plan.
5. Reviewer-only `tests/scenarios.md`, current public Module 6 evidence, public product copy, and
   evidence/product tests.
6. Ignored `task-9-report-v3.md` and `task9-final-review-v3.json` as untrusted prior evidence whose
   exact findings must be addressed; their reports do not substitute for raw evidence.

Fresh Git identities, retained raw bytes, and current independent reviews take precedence over
earlier summaries. Any tracked correction after review creates a successor commit and requires a
fresh complete review of the new exact head.

## Global Constraints

- Execute on an isolated `codex/` branch/worktree rooted at the accepted addendum commit. Before
  any write, verify that the addendum commit has sole parent
  `b0e0c85dd0bf50e84ba1ce14ed4a985be7676002`, that the predecessor
  plan hash still matches, and that tracked/index state is clean.
- Do not alter the predecessor plan, active skill, checker semantics, `EVALUATION.md`,
  `tests/scenarios.md`, Module 5 input fixtures, baseline, `BASELINE.sha256`, `CHANGELOG.md`, or
  `.local-handoff/**`.
- Never use `/private/tmp`, `/tmp`, `/var`, a tool session directory, or process memory as the
  authoritative evidence store. Temporary process files may exist only as disposable working
  copies after the durable source bytes have been written and hashed.
- Retain the recovery workspace through Task 9 exact-head Change Review and the later Task 10
  decision. Plan completion must not delete, move, truncate, rewrite, or garbage-collect it.
- One writer owns each directory. Parallel execution is allowed only after Task 1 freezes shared
  schemas/snapshots and only across the four disjoint group directories. No two writers may edit
  root manifests, `product-repo/`, tracked public paths, or the same case attempt concurrently.
- Use regular files, never symlinks, for snapshots and evidence. Reject a file if `is_symlink()`
  is true or its resolved path escapes the recovery root.
- Preserve every attempt. A correction creates a new attempt directory and new hashes; it never
  edits or deletes the failed, blocked, contaminated, or superseded attempt.
- Executor and evaluator are distinct roles. A case executor receives no rubric verdict, expected
  outcome, observable PASS/FAIL text, evaluator notes, prior verdict, or author conversation.
  Evaluators receive the exact case rubric, input bundle manifest, raw output, and operation record,
  but not executor reasoning/conversation beyond the retained submitted output/transcript.
- Requested model/reasoning, platform-accepted native assignment, and independently verified
  runtime model/reasoning are three separate fields. Use `"Unknown"` unless an authoritative
  receipt proves the latter two; never silently substitute.
- `evaluation_verdict` is exactly `PASS`, `FAIL`, or `BLOCKED`. `dependent_action_state` is a
  separate nonempty state. A correctly blocked dependent action may accompany `PASS`; missing
  evidence needed to score the case is `BLOCKED`; an observed rubric violation is `FAIL`.
- Never force 21 PASS. Public totals, prose, case tables, and next action must reflect the actual
  current attempt for every case. A rerun is allowed only after a named observable correction;
  prior attempts remain retained and explicitly `superseded`.
- No expected verdict/rubric content may enter an executor input bundle. The bundle-contamination
  check runs before dispatch, after execution, before evaluation, and again before public assembly.
- Do not claim operating-system isolation. Record shared-filesystem separation as procedural unless
  independently proven otherwise.
- No real task/thread/message/monitor mutation is allowed in offline cases. No network, GitHub,
  external service, credential switch, transport fallback, email, payment, analytics, deployment,
  release, real data, or paid action is allowed anywhere in this recovery.
- `quick_validate.py` remains unavailable if PyYAML is absent. Record its
  `ModuleNotFoundError: No module named 'yaml'` as a limitation; do not install PyYAML without
  separate authorization and do not report the validator as PASS.

## File Map

### This plan-author commit only

- Create:
  `docs/superpowers/plans/2026-09-12-module-6-evidence-retention-recovery.md`.
- Exact changed-path allowlist for the plan commit: the one path above. No candidate path belongs
  in this commit.

### Durable ignored recovery workspace

All paths below live under
`.superpowers/sdd/2026-09-12-module-6-evidence-retention-recovery/` and remain ignored/private:

```text
manifest.json
manifest.sha256
inputs/binding/
inputs/<group>/<EID>/<attempt-id>/
executions/<group>/<EID>/<attempt-id>/
evaluations/<group>/<EID>/<attempt-id>/
transcripts/<group>/<EID>/<attempt-id>/
product-repo/repository/
product-repo/reviews/
product-repo/rehearsals/
checks/archive-validator.py
checks/archive-validator-tests.py
checks/execution-evidence-manifest.json
checks/execution-evidence-manifest.sha256
checks/digest-resolution.json
checks/bundle-contamination.json
checks/private-denylist.txt
checks/private-denylist.sha256
checks/redaction-scan.json
reports/<group>-report.md
reports/<group>-review.json
reports/public-assembly-report.md
reports/module-change-review.json
reports/task9-recommendation.md
```

The root `manifest.json` is regenerated atomically only by the Task coordinator's designated
manifest writer. It lists every retained regular file except `manifest.json` and
`manifest.sha256`; `manifest.sha256` contains the SHA-256 of the exact current manifest bytes.
Before public assembly, freeze the case-evidence subset as immutable
`checks/execution-evidence-manifest.json` plus its sidecar hash. Later review records may advance
the root manifest without changing the frozen execution-evidence identity used by public files.

### Tracked recovery candidate allowlist

The public assembler may modify only these eleven existing paths, and only when fresh retained
evidence justifies the change:

1. `README.md`
2. `docs/PROJECT_STATUS.md`
3. `docs/validation.md`
4. `tests/fixtures/quietfollow/evidence/manifest.json`
5. `tests/fixtures/quietfollow/evidence/execution-record.json`
6. `tests/fixtures/quietfollow/evidence/part-1-discovery.md`
7. `tests/fixtures/quietfollow/evidence/part-2-readiness.md`
8. `tests/fixtures/quietfollow/evidence/part-3-delivery.md`
9. `tests/fixtures/quietfollow/evidence/part-4-release-rehearsal.md`
10. `tests/fixtures/quietfollow/evidence/part-5-resume-scaling.md`
11. `tests/test_pilot_evidence.py`

The two tracked product files
`tests/fixtures/quietfollow/product/quietfollow.py` and
`tests/fixtures/quietfollow/product/test_quietfollow.py` are read-only comparison targets. The
fresh disposable repository must finish with the same externally observable behavior and 15-test
contract; the assembler updates source-repository commit/tree identities while preserving these
tracked product bytes. If an honest rerun exposes a required product correction, stop and escalate
that product-scope change instead of silently expanding this recovery allowlist.

### Explicitly forbidden tracked effects

- No create/delete/rename outside the eleven-path candidate allowlist.
- No edit to the plan artifact in a candidate commit.
- No self-referential tracked candidate head/tree in public files. Exact candidate head/tree and
  review identity belong in ignored Task 9 reports/review records created after commit.
- No raw archive, private path, real task/thread/client/agent ID, private URL, transcript, prompt,
  credential, or `.local-handoff` content enters Git. The stable public historical name
  `.local-handoff` may remain in README; its contents and machine path remain private.

## Artifact contracts

### Root content-addressed manifest

`manifest.json` uses this exact top-level shape:

```json
{
  "schema_version": 2,
  "recovery_plan": "MODULE6-RECOVERY-PLAN-v1",
  "predecessor": {},
  "artifacts": [],
  "cases": [],
  "groups": [],
  "retention": {},
  "limitations": []
}
```

Every `artifacts[]` item contains exactly `logical_id`, `case_id`, `attempt_id`, `kind`,
`relative_path`, `sha256`, `byte_count`, `content_type`, `producer_alias`, `credit_state`, and
`sensitivity`. `logical_id` is unique. `case_id` and `attempt_id` are strings for case evidence and
JSON `null` for shared schema/check/review artifacts. `kind` is one of `raw_input`,
`executor_prompt`, `bundle_manifest`, `executor_output`, `result_record`, `evaluator_input`,
`evaluator_prompt`, `evaluator_output`, `transcript`, `session_receipt`, `product_git`, `check`,
`report`, or `review`. `sha256` matches `^[0-9a-f]{64}$`; `byte_count` is the exact nonnegative
integer file length; `content_type` is the actual MIME-like text label; `producer_alias` is a stable
public-safe role alias; `sensitivity` is `private` or `public-source`.

- `relative_path` is POSIX, relative to the recovery root, contains no `..`, and resolves to a
  regular non-symlink file within the root.
- `credit_state` is `current`, `superseded`, or `non-credit`.
- `byte_count` is the observed positive or zero file length; empty files are allowed only when the
  relevant case contract explicitly expects empty output, and that fact is recorded in its case
  record.
- `sha256` is the digest of exact raw bytes, not normalised text.
- The manifest does not hash itself. `manifest.sha256` is the only self-adjacent digest sidecar.

Each `cases[]` record names `case_id`, `group`, `current_attempt_id`, `attempt_ids`,
`evaluation_verdict`, `dependent_action_state`, `requested_assignment`,
`accepted_native_assignment`, `independently_verified_runtime_fact`, and exact logical IDs for
raw inputs, executor outputs, evaluator inputs, evaluator outputs, and transcript/operation files.
It also contains `current_artifact_kinds`, which must include `raw_input`, `executor_output`,
`evaluator_input`, `evaluator_output`, `transcript`, and `session_receipt`.

### Per-attempt files

For every one of E02, E08, E10, E11, E12, E13, E14, E17, E20, E21, E22, E25, E27, E28,
E31, E33, E34, E37, E38, E39, and E41, retain:

```text
inputs/<group>/<EID>/<attempt-id>/source-manifest.json
inputs/<group>/<EID>/<attempt-id>/executor-bundle-manifest.json
inputs/<group>/<EID>/<attempt-id>/executor-prompt.txt
executions/<group>/<EID>/<attempt-id>/executor-output.txt
executions/<group>/<EID>/<attempt-id>/result-record.json
evaluations/<group>/<EID>/<attempt-id>/evaluator-input.json
evaluations/<group>/<EID>/<attempt-id>/evaluator-prompt.txt
evaluations/<group>/<EID>/<attempt-id>/evaluator-output.json
transcripts/<group>/<EID>/<attempt-id>/operations.jsonl
transcripts/<group>/<EID>/<attempt-id>/session-receipt.json
```

`source-manifest.json` binds the tested harness source, case inputs, permissions, and allowed/
forbidden effects. `executor-bundle-manifest.json` lists every file visible in the intentionally
supplied bundle and its digest. `result-record.json` records the actual outcome without a verdict.
`evaluator-input.json` adds the exact reviewer-only rubric section and raw-evidence logical IDs.
`evaluator-output.json` records findings, `evaluation_verdict`, `dependent_action_state`, and
recommended correction without editing executor output. `operations.jsonl` records ordered
dispatch/tool/file/Git/test operations and results sufficient to verify prohibited-effect claims.
`session-receipt.json` keeps requested, accepted, and independently verified model facts separate.

### Current and superseded identity rules

- Attempt IDs increase monotonically per case: `E02-r1`, `E02-r2`, and so on.
- Exactly one attempt is `current` for each case when public assembly begins. Earlier attempts are
  `superseded` after a corrected rerun or `non-credit` when contaminated/malformed.
- A current `FAIL` or `BLOCKED` attempt remains current until a real correction is made. Do not
  rerun solely to seek PASS.
- Public records name both the new current attempt/digests and the predecessor public identities as
  superseded because their raw bytes vanished. Superseded identities never authorize a transition.
- Every new public case/execution/evaluator/transcript `sha256:` value must resolve to the exact raw
  bytes retained in the ignored recovery workspace. A digest that identifies a public part,
  manifest, product source, or product test resolves to that exact tracked file's bytes. The
  `checks/digest-resolution.json` record contains numerator, denominator, misses, and duplicate
  logical IDs; public assembly is blocked unless resolution is 100% with zero misses.

## Case groups and stable interfaces

| Group | Cases | Private roots owned | Stable inputs before parallel start |
|---|---|---|---|
| `discovery-readiness` | E31, E38, E39 | `inputs/discovery-readiness`, `executions/discovery-readiness`, `evaluations/discovery-readiness`, `transcripts/discovery-readiness`; `reports/discovery-readiness-*` | binding snapshot, QuietFollow four-file bundle, Gate 3.5/PRD cost records |
| `delivery-release` | E12, E13, E14, E27, E28 | `inputs/delivery-release`, `executions/delivery-release`, `evaluations/delivery-release`, `transcripts/delivery-release`, `product-repo/**`; `reports/delivery-release-*` | final tracked product behavior/tests, product requirements, review/release fixtures |
| `resume-scaling` | E02, E25, E33, E34, E37, E41 | `inputs/resume-scaling`, `executions/resume-scaling`, `evaluations/resume-scaling`, `transcripts/resume-scaling`; `reports/resume-scaling-*` | legacy inputs, artifact/WIP maps, load/registration/prototype records |
| `coordination` | E08, E10, E11, E17, E20, E21, E22 | `inputs/coordination`, `executions/coordination`, `evaluations/coordination`, `transcripts/coordination`; `reports/coordination-*` | plan/decision/API/identity/denial/model fixtures |

Each group writer consumes the frozen Task 1 schema and copies case inputs into its own assigned
directories. It produces a `group-manifest.json`, group report, and one independent group-review
record. No group writer updates the root manifest or public files. Parallel dispatch may begin only
after the Task coordinator records the same frozen schema digest and input-snapshot digest in all
four briefs. `delivery-release` is the sole owner of `product-repo/**`; no other group writes there.

The public assembler uses this fixed producer/consumer mapping; it does not need any earlier
conversation to decide where a case belongs:

| Public part | Current case evidence consumed | Subject retained |
|---|---|---|
| `part-1-discovery.md` | E38 | Positioning → proportionate Gate 3.5 boundary → Journey dependency |
| `part-2-readiness.md` | E31, E39 | prototype architecture scope and changed-only Gate 8 economics |
| `part-3-delivery.md` | E12, E14 | WorkItem TDD, independent review/correction, stale-PASS rejection |
| `part-4-release-rehearsal.md` | E13, E27, E28 | exact local merge, stale FINAL routing, rollout/rollback, open manual evidence |
| `part-5-resume-scaling.md` | E02, E25, E33, E34, E37, E41, E08, E10, E11, E17, E20, E21, E22 | resume/scaling plus offline coordination and permission/model boundaries |

## Task 1: Freeze durable schemas, binding inputs, and contamination checks

**Files:**

- Create all durable ignored root directories and the initial files under `checks/`.
- Copy binding inputs to `inputs/binding/` as regular read-only files.
- Do not modify tracked files.

**Interfaces:**

- Consumes: accepted addendum commit, exact predecessor identities, current tracked binding files.
- Produces: schema v2, immutable binding snapshot, group path ownership table, archive validator,
  bundle contamination checker, initial root manifest, and four hash-bound group briefs.

**Allowed effects:** ignored recovery-root writes and read-only Git/filesystem inspection.

**Forbidden effects:** case execution, product-repository creation, tracked writes, evaluator
dispatch, external actions, and cleanup of predecessor evidence.

- [ ] **Step 1.1: Verify execution identity and predecessor immutability.**

  Run:

  ```bash
  git rev-parse HEAD
  git rev-parse HEAD^
  git status --short
  shasum -a 256 docs/superpowers/plans/2026-09-11-module-6-quietfollow-pilot.md
  git diff --name-only b0e0c85dd0bf50e84ba1ce14ed4a985be7676002...HEAD
  ```

  Expected: `HEAD` is the accepted addendum commit; its sole parent is
  `b0e0c85dd0bf50e84ba1ce14ed4a985be7676002`; tracked state is clean; predecessor plan digest is
  `6037149b9a70cdeba4b8f1fd4fcce460b9206730665c8aa69f4ee781eb5c4777`; the
  parent-to-head path set is only this addendum. Stop before writes if any check differs.

- [ ] **Step 1.2: Write archive-validator tests first.**

  Create ignored `checks/archive-validator-tests.py` with tests that reject a missing file,
  digest mismatch, duplicate logical ID, `..` path, absolute path, symlink, two current attempts
  for one case, missing raw artifact category, and an executor bundle containing any forbidden
  evaluator token. Include one all-valid fixture covering the exact 21-case set.

- [ ] **Step 1.3: Run the validator tests RED.**

  Run:

  ```bash
  python3 -B .superpowers/sdd/2026-09-12-module-6-evidence-retention-recovery/checks/archive-validator-tests.py
  ```

  Expected: FAIL because `checks/archive-validator.py` does not yet exist.

- [ ] **Step 1.4: Implement the minimum ignored validator.**

  `archive-validator.py` must expose the following concrete behavior; use these bodies as the
  minimum implementation and extend only to satisfy the RED cases above:

  ```python
  import hashlib
  from pathlib import Path, PurePosixPath

  REQUIRED_KINDS = {
      "raw_input", "executor_output", "evaluator_input",
      "evaluator_output", "transcript", "session_receipt",
  }


  def sha256_file(path: Path) -> str:
      digest = hashlib.sha256()
      with path.open("rb") as stream:
          for block in iter(lambda: stream.read(1024 * 1024), b""):
              digest.update(block)
      return digest.hexdigest()


  def validate_artifact(root: Path, item: dict) -> list[str]:
      errors = []
      relative = item.get("relative_path")
      if not isinstance(relative, str):
          return ["relative_path must be a string"]
      posix = PurePosixPath(relative)
      if posix.is_absolute() or ".." in posix.parts:
          return [f"unsafe relative_path: {relative}"]
      path = root.joinpath(*posix.parts)
      if path.is_symlink() or not path.is_file():
          return [f"not a regular retained file: {relative}"]
      if root.resolve() not in path.resolve().parents:
          return [f"path escapes recovery root: {relative}"]
      if sha256_file(path) != item.get("sha256"):
          errors.append(f"sha256 mismatch: {relative}")
      if path.stat().st_size != item.get("byte_count"):
          errors.append(f"byte_count mismatch: {relative}")
      return errors


  def validate_cases(manifest: dict, selected: set[str]) -> list[str]:
      errors = []
      cases = manifest.get("cases", [])
      ids = [case.get("case_id") for case in cases]
      if set(ids) != selected or len(ids) != len(selected):
          errors.append("case set is not the exact selected set")
      for case in cases:
          if case.get("evaluation_verdict") not in {"PASS", "FAIL", "BLOCKED"}:
              errors.append(f"invalid verdict for {case.get('case_id')}")
          if not case.get("dependent_action_state"):
              errors.append(f"missing dependent state for {case.get('case_id')}")
          kinds = set(case.get("current_artifact_kinds", []))
          if not REQUIRED_KINDS.issubset(kinds):
              errors.append(f"missing raw artifact category for {case.get('case_id')}")
      return errors


  def scan_executor_bundle(root: Path, bundle_manifest: dict) -> list[str]:
      errors = []
      forbidden_paths = bundle_manifest["contamination_contract"]["forbidden_paths"]
      forbidden_labels = bundle_manifest["contamination_contract"]["forbidden_labels"]
      forbidden_kinds = {
          "rubric", "evaluation", "expected_answer",
          "author_conversation", "prior_verdict",
      }
      for item in bundle_manifest["files"]:
          relative = item["relative_path"]
          if item["kind"] in forbidden_kinds:
              errors.append(f"forbidden kind: {item['kind']}")
          if any(value in relative for value in forbidden_paths):
              errors.append(f"forbidden path: {relative}")
          data = root.joinpath(*PurePosixPath(relative).parts).read_bytes()
          for label in forbidden_labels:
              if label.encode("utf-8") in data:
                  errors.append(f"forbidden label in {relative}: {label}")
      return errors


  def validate_manifest(root: Path, manifest: dict) -> list[str]:
      errors = []
      artifacts = manifest.get("artifacts", [])
      logical_ids = [item.get("logical_id") for item in artifacts]
      if len(logical_ids) != len(set(logical_ids)):
          errors.append("duplicate logical_id")
      for item in artifacts:
          errors.extend(validate_artifact(root, item))
      errors.extend(validate_cases(manifest, SELECTED_CASES))
      return errors
  ```

  Define `SELECTED_CASES` in the module as the exact 21-case set already enumerated by this plan.
  The executable entry point writes deterministic JSON with `passed`, `failed`, and `artifacts`
  and exits `0` only when `failed` is empty.

- [ ] **Step 1.5: Run validator tests GREEN and freeze their bytes.**

  Expected: all validator tests PASS. Hash both validator files and add them to the initial root
  manifest before any group dispatch.

- [ ] **Step 1.6: Snapshot binding inputs.**

  Copy as regular files the active skill/references/assets, QuietFollow four-file input, legacy
  package, review events, current product code/tests, and reviewer rubric into named
  `inputs/binding/` subdirectories. Record original tracked path, source commit
  `b0e0c85dd0bf50e84ba1ce14ed4a985be7676002`, source
  digest, copy digest, byte count, and equality. Make copies read-only after hashing.

- [ ] **Step 1.7: Define the exact executor contamination denyset.**

  `checks/bundle-contamination.json` must search executor bundle paths and bytes for:

  ```json
  {
    "forbidden_paths": [
      "tests/scenarios.md",
      "EVALUATION.md",
      "docs/superpowers/plans/2026-09-11-module-6-quietfollow-pilot.md",
      "docs/superpowers/plans/2026-09-12-module-6-evidence-retention-recovery.md"
    ],
    "forbidden_labels": [
      "Observable PASS:",
      "Observable FAIL:",
      "BLOCKED rule:",
      "expected verdict",
      "evaluator notes"
    ]
  }
  ```

  Also reject files whose logical kind is `rubric`, `evaluation`, `expected_answer`,
  `author_conversation`, or `prior_verdict`.

- [ ] **Step 1.8: Review and freeze shared contracts.**

  A distinct read-only reviewer receives this plan, Task 1 files, exact hashes, and path ownership
  table. It verifies schema producer/consumer consistency, no rubric leakage, no absolute manifest
  paths, and all 21 case slots. Store `reports/task1-schema-review.json`. A non-PASS review blocks
  group dispatch; corrections create new schema bytes and a fresh review.

**Commit guidance:** no Git commit; every output is ignored private evidence and is content-bound
in the root manifest.

## Task 2: Rerun discovery/readiness cases E31, E38, and E39

**Files:** only this group's attempt paths and `reports/discovery-readiness-*`.

**Interfaces:**

- Consumes: frozen binding snapshot, four-file QuietFollow bundle, exact E31/E38/E39 rubric
  sections for evaluators only, and execution-only Gate 3.5/PRD cost inputs.
- Produces: one current attempt for each case, per-attempt raw evidence, a group manifest/report,
  and an independent group review.

**Allowed effects:** local durable case artifacts.

**Forbidden effects:** product implementation, external research, fabricated data, spend,
payment/provisioning, public files, and other groups' directories.

- [ ] **Step 2.1: Materialize and hash neutral case inputs.**

  E31 receives the profile and current architecture context; E38 receives the four-file bundle at
  open Gate 3.5; E39 receives fresh byte-stable records with the accepted-plan values: 120
  synthetic consultants, alternatives, payer/value, 3–5 person-days, 0–5 EUR/month, bounded five
  walkthroughs, 4/5 signal, and only the encrypted-backup delta of 10–20 EUR/month. Label every
  value as synthetic fact/hypothesis/Unknown exactly according to its source. Do not include an
  expected decision or verdict.

- [ ] **Step 2.2: Run bundle contamination validation before executor dispatch.**

  Store the complete validator JSON alongside each executor bundle. Any match makes that attempt
  `non-credit`; rebuild a clean bundle under the next attempt ID before dispatch.

- [ ] **Step 2.3: Dispatch distinct executors.**

  Request `gpt-5.6-sol/high` separately for E31, E38, and E39. Preserve raw prompts, outputs,
  session receipts, and operation records. No executor receives another case's output unless it is
  an explicitly hashed input named by the case contract.

- [ ] **Step 2.4: Dispatch distinct evaluators after outputs are immutable.**

  Each evaluator receives only its exact rubric section, source/bundle manifests, executor output,
  and operation record. Request `gpt-5.6-sol/high`. The evaluator writes one JSON verdict bound to
  exact digests and states the dependent gate/action separately.

- [ ] **Step 2.5: Preserve failures and corrections.**

  If a case is `FAIL`, record the violated observable behavior and keep dependent work open or
  blocked according to the rubric. If `BLOCKED`, name the missing artifact/capability. A corrected
  rerun uses the next attempt ID and retains the earlier bytes.

- [ ] **Step 2.6: Run independent group review.**

  A fresh read-only reviewer verifies exact case coverage, rubric isolation, raw digest resolution,
  synthetic/local boundaries, Gate 3.5 versus Gate 8 reuse, and verdict/dependent-state truthfulness.
  Store `reports/discovery-readiness-review.json`; no group PASS is inferred from case count.

**Commit guidance:** no Git commit; group files remain ignored and immutable after review.

## Task 3: Rebuild the disposable Git sequence and rerun E12, E13, E14, E27, and E28

**Files:** only this group's case paths, all `product-repo/**`, and
`reports/delivery-release-*`.

**Interfaces:**

- Consumes: frozen final product behavior/tests, readiness requirements, local review fixtures,
  exact E12/E13/E14/E27/E28 evaluator rubrics, and no prior disposable commit identity.
- Produces: a new honest local Git history, raw product reviews and reruns, exact merge/tree/release
  rehearsal evidence, five current case attempts, group manifest/report, and group review.

**Allowed effects:** sequential writes in the durable disposable local Git repository and durable
private evidence.

**Forbidden effects:** recreating vanished commit hashes, amending commits, rewriting history,
GitHub/service actions, actual release/deploy, tracked product edits, and concurrent writers.

- [ ] **Step 3.1: Initialize a new durable disposable repository.**

  Create `product-repo/repository/` with local branch `main`, synthetic local Git identity, and an
  initial commit containing only a neutral product brief and `.gitignore`. Record the new root
  commit/tree; do not attempt to match any predecessor SHA.

- [ ] **Step 3.2: Build WorkItem 1 with RED/GREEN evidence.**

  On `codex/quietfollow-wi1`, write tests for create/schedule/due/reload, unknown contact, corrupt
  store preservation, IDs, and due-date fields; run RED before implementation; implement the
  minimum `Tracker`; run GREEN; commit. A fresh `gpt-5.6-sol/high` Change Reviewer receives exact
  requirements, base/head, full diff, commands/results, and candidate files without the writer's
  conversation. Correct findings with successor commits and fresh full review. Merge only the
  exact reviewed head to local `main` using `--no-ff` and record commit/tree ancestry.

- [ ] **Step 3.3: Build WorkItem 2 and an authentic forward finding/correction sequence.**

  On `codex/quietfollow-wi2` from reviewed WorkItem 1 main, write RED tests for outcome persistence,
  completed-item filtering, unknown follow-up preservation, reconstruction, blank outcome, and
  exact spaced outcome; implement to GREEN and commit ordinary candidate C. Transfer sole-writer
  ownership to a bounded fixture preparer, create one deterministic seeded defect S without
  revealing its oracle in commit subject or reviewer bundle, and end that writer interval.

- [ ] **Step 3.4: Obtain a clean independent review of S.**

  A fresh Change Reviewer receives requirements, WorkItem base, S head, complete base..S diff,
  tests, and no Implementation/fixture-preparer conversation or expected finding. Record the
  actual verdict. If it misses the seeded violation, E14 may be `FAIL`; reveal the oracle only after
  that verdict, then create a distinct correction attempt. Never rewrite the missed review.

- [ ] **Step 3.5: Correct on the same WorkItem branch and re-review.**

  Forward the actual finding internally to one recorded writer/replacement. First demonstrate the
  focused regression RED on S, then correct to GREEN, run the full product suite, commit R with S
  as parent, and request a fresh full Change Review of exact R. This sequence provides E14 evidence
  only if ordering, branch continuity, role separation, and exact inputs are retained.

- [ ] **Step 3.6: Create E12's stale-PASS event authentically.**

  After PASS(R), deliver the new identity-bound whitespace requirement, add its RED test and
  minimum change, and commit B with R as parent. Record that PASS(R) does not cover B; keep merge
  blocked; request a fresh full Change Review of B. The routing executor receives the identities,
  not the expected stale-review answer.

- [ ] **Step 3.7: Preserve final product behavior and tests.**

  The exact reviewed B tree must satisfy all 15 public product tests. Compare its final
  `quietfollow.py` and `test_quietfollow.py` byte hashes with the two tracked product files. A byte
  mismatch is a review finding: either correct the disposable candidate without changing required
  behavior or escalate a product-scope change. Do not alter tracked product bytes in this recovery.

- [ ] **Step 3.8: Merge and prove local ancestry/tree identity.**

  Merge only reviewed B with `--no-ff` to disposable `main`. Record pre-merge main, B, merge commit,
  tree, `git merge-base --is-ancestor` results, `git diff-tree`, and file blob identities. Run 15/15
  product tests at exact merged main.

- [ ] **Step 3.9: Rerun E13 on an exact stale-FINAL sequence.**

  Create an immutable local FINAL-like review record bound to the reviewed pre-merge main A, then
  present exact current merged main B and tree to a fresh closure executor. The executor must decide
  without an expected answer; evaluator checks refusal/closure behavior and binds its verdict to the
  new A/B identities. This is a local rehearsal record, never Module FINAL.

- [ ] **Step 3.10: Rerun E27/E28 on the exact reviewed merged tree.**

  Create rollout notes, copy a synthetic store, run the smoke path, restore the copy, verify
  byte-identical reload, and record manual accessibility plus manual backup/restore as actually
  observed (`PENDING`/`Unknown` when not performed). Evaluators must not convert green automation
  into release readiness or label the rehearsal production.

- [ ] **Step 3.11: Independently evaluate all five cases and review the group.**

  Use distinct case evaluators requested as `gpt-5.6-sol/high`. Then a fresh group reviewer verifies
  Git ancestry, trees/blobs, review independence, no leaked oracle, all transcript operations,
  stale-review invalidation, rollout/rollback, and actual verdicts. Store
  `reports/delivery-release-review.json`.

**Commit guidance:** disposable repository commits are required and retained; no tracked harness
commit is created by this task.

## Task 4: Rerun resume/scaling cases E02, E25, E33, E34, E37, and E41

**Files:** only this group's case paths and `reports/resume-scaling-*`.

**Interfaces:**

- Consumes: frozen legacy inputs, neutral artifact/WIP inventories, load/registration/prototype
  transition records, and evaluator-only exact case rubrics.
- Produces: six current attempts, raw preservation/diff evidence, group manifest/report, and group
  review.

**Allowed effects:** durable local case files.

**Forbidden effects:** real task/monitor update, data mutation, product implementation, history
rewrite, public files, and other groups' directories.

- [ ] **Step 4.1: Create neutral input records before dispatch.**

  E02's artifact map names differently titled Journey/Requirements and missing Risk. E25's WIP
  inventory names one completed item, one in-progress identity, one existing wait, and absent ACK.
  E33 uses the accepted synthetic load values and a pre-existing neutral baseline. E34 records
  100,000 synthetic registrations with activity/load dimensions Unknown. E37 separates positive
  prototype evidence, unsuitable code, and Unknown data-lifecycle authority. E41 uses byte-exact
  legacy files and a package manifest. None contains evaluator conclusions.

- [ ] **Step 4.2: Run contamination checks and fresh executors.**

  Request `gpt-5.6-sol/high` separately per case. Preserve artifact-change sets for E02, identity/
  ACK update sequence for E25, literal transition-plan diff for E33, gap dimensions for E34,
  preservation/lifecycle state for E37, and byte-preservation diff for E41.

- [ ] **Step 4.3: Evaluate independently.**

  Each evaluator receives exact rubric and immutable raw evidence only after execution closes.
  Record `FAIL` for lifecycle/history loss, `BLOCKED` for missing score-critical evidence, and
  separate dependent state for correctly paused actions.

- [ ] **Step 4.4: Review the group.**

  A fresh reviewer resolves all raw digests, confirms unchanged legacy/tracked inputs, checks that
  synthetic scale is not presented as live load, and verifies no forced reuse/rewrite or duplicate
  lifecycle work. Store `reports/resume-scaling-review.json`.

**Commit guidance:** no Git commit; group files remain ignored and immutable after review.

## Task 5: Rerun coordination cases E08, E10, E11, E17, E20, E21, and E22

**Files:** only this group's case paths and `reports/coordination-*`.

**Interfaces:**

- Consumes: frozen review events plus neutral plan, shared-API, owner-reply, forwarded-mandate, and
  typed-ID records; evaluator-only exact case rubrics.
- Produces: seven current attempts, E10 analysis/review/decision chain, zero-live-effect operation
  evidence, group manifest/report, and group review.

**Allowed effects:** durable offline responses and role records.

**Forbidden effects:** real Task/Architecture-task creation, native message/wait/monitor mutation,
push/retry, credential/transport/executor bypass, model substitution, public writes, and other
groups' directories.

- [ ] **Step 5.1: Materialize neutral case inputs and run contamination checks.**

  E08 contains completed work plus an omitted Risk source; E10 contains a locally accepted plan,
  a shared `ContactStore.save` contract impact, and bounded synthetic commission variant; E11 has
  exact and ambiguous replies; E17 separates queued client, real thread Unknown, and internal-agent
  IDs; E20/E21 use denial/wait/forwarded-mandate facts; E22 records requested Astra, native
  acceptance unavailable, and runtime Unknown. No file states the expected response.

- [ ] **Step 5.2: Run E08, E11, E17, E20, E21, and E22 executors.**

  Request `gpt-5.6-sol/high` per fresh executor. Operation records must show no native/service
  mutation. A proposed wrong-ID, retry, bypass, or silent substitution is recorded as actual output
  and evaluated honestly rather than removed.

- [ ] **Step 5.3: Run E10's bounded role sequence.**

  First a coordination executor writes one escalation/commission-routing response. Then a fresh
  `gpt-6-astra/high` architecture analyst receives only the bounded synthetic commission, affected
  contracts, preserved work, and source hashes. A distinct read-only `gpt-6-astra/high` architecture
  reviewer receives exact requirements and package, without analysis conversation. Only a review
  PASS permits the runner to create an identity-bound synthetic owner decision with sequence `1`
  and `no implementation authorization`; otherwise routing remains blocked. A final fresh routing
  executor receives only the reviewed package/decision and writes revised boundaries.

- [ ] **Step 5.4: Evaluate all seven cases independently.**

  Request `gpt-5.6-sol/high` for each behavioral evaluator. Preserve accepted/runtime assignment
  fields as `Unknown` absent receipts. Keep verdict and dependent permission/task/model state
  separate.

- [ ] **Step 5.5: Review the group.**

  A fresh read-only reviewer verifies one escalation, one bounded architecture decision when
  review passed, no full transcript relay, unaffected work preserved, no duplicate/native action,
  typed IDs, denial compliance, quiet unchanged wait, and model-fact separation. Store
  `reports/coordination-review.json`.

**Commit guidance:** no Git commit; group files remain ignored and immutable after review.

## Task 6: Assemble and independently audit the retained execution evidence

**Files:** root manifest, frozen execution-evidence manifest, digest/contamination checks, group
reports/reviews, and an ignored audit record. No tracked files.

**Interfaces:**

- Consumes: four stable reviewed group directories and product-repository evidence.
- Produces: one canonical current-attempt selection for all 21 cases, frozen content-addressed
  execution manifest, 100% resolution record, and independent archive-audit verdict.

**Allowed effects:** sole-writer root manifest/check/report updates.

**Forbidden effects:** editing group attempt bytes, changing verdicts, running a case again,
tracked/public writes, and cleanup.

- [ ] **Step 6.1: Validate every group independently before aggregation.**

  Run the archive validator separately on each group manifest. Confirm exact case partition with
  no overlap or omission and exactly one current attempt per case. A group-review finding remains
  open; aggregation does not waive it.

- [ ] **Step 6.2: Build the root manifest and freeze execution evidence.**

  Add every raw input/output/evaluator/transcript/product-review artifact. Generate the root
  sidecar hash. Copy the case-evidence subset to `checks/execution-evidence-manifest.json`, set it
  read-only, hash it, and never mutate it afterward.

- [ ] **Step 6.3: Prove 100% exact-byte resolution.**

  Run `archive-validator.py` against the frozen execution manifest. Write
  `checks/digest-resolution.json` with exact counts for current inputs, executor outputs,
  evaluator inputs, evaluator outputs, transcripts, and product-review artifacts. Every category
  must have numerator equal denominator and zero missing/mismatched/symlink/escaped paths before
  public assembly.

- [ ] **Step 6.4: Re-run contamination checks across all current executor bundles.**

  Scan both paths and exact bytes against the denyset. Record per-case results and one aggregate
  zero-match result. An executor bundle match makes that attempt non-credit; return only that case
  to a new attempt and repeat its independent evaluation/review.

- [ ] **Step 6.5: Run a distinct archive audit.**

  A fresh `gpt-5.6-sol/high` read-only reviewer receives this plan, exact requirements, frozen
  manifest, raw retained files, group reviews, and product Git evidence without author/executor
  conversations. It independently resolves 100% of current inputs, outputs, evaluator files,
  transcripts, and product-review records; checks current/superseded states, contamination,
  assignments, verdict truthfulness, Git ancestry, and retention. Any finding blocks Task 7 until a
  successor artifact/attempt and fresh affected review exist.

**Commit guidance:** no Git commit; the frozen execution manifest identity is the public evidence
source for Task 7.

## Task 7: Write public evidence regressions RED, assemble the successor candidate, then GREEN

**Files:** exactly the eleven tracked recovery candidate paths.

**Interfaces:**

- Consumes: clean archive-audit verdict, frozen execution manifest/hash, all actual current case
  verdicts/states, reviewed disposable Git identities, and predecessor public records.
- Produces: public successor evidence, permanent regression coverage, clean tracked candidate, and
  public-assembly report.

**Allowed effects:** one designated public assembler writes only the eleven allowlisted paths.

**Forbidden effects:** parallel tracked writers, public raw evidence/private bindings, product
file edits, plan edits, verdict improvement, self-referential head, and unlisted paths.

- [ ] **Step 7.1: Extend focused tests first.**

  In `tests/test_pilot_evidence.py`, add tests that require:

  - `README.md` is part of permanent public-binding coverage;
  - README retains the exact local-synthetic 21-selected-case boundary while preserving the stable
    historical `.local-handoff` name;
  - README-specific scanning rejects machine paths, Windows paths/UNC, raw runtime-ID shapes, and
    private field keys without rejecting the stable historical name;
  - public records identify predecessor evidence as superseded and exactly one new current attempt
    per case;
  - verdict and dependent state remain separate and totals equal actual records;
  - the public execution-manifest digest is 64 lowercase hex and resolution summary reports 100%
    for each current raw category;
  - public product source/copy hashes equal the retained reviewed final product blobs and current
    tracked bytes;
  - local/synthetic/rehearsal boundaries and no Task 10/FINAL/release claim are present.

- [ ] **Step 7.2: Run focused tests RED before changing public records.**

  Run:

  ```bash
  python3 -B -m unittest tests.test_pilot_evidence -v
  ```

  Expected: the new assertions fail against schema v1/predecessor evidence, including README's
  missing membership in `PUBLIC_EVIDENCE`.

- [ ] **Step 7.3: Assemble public machine-readable records from retained bytes only.**

  Update public `manifest.json` and `execution-record.json` to successor schema/identities. For each
  case copy the actual current verdict, dependent state, findings, rerun history, requested/
  accepted/runtime facts, and public-safe digests. Add a `superseded_predecessor_evidence` section
  explaining that old raw artifacts vanished and receive no current credit. Bind every new digest
  to a retained artifact logical ID and the frozen execution-manifest digest.

- [ ] **Step 7.4: Update five public parts and validation/navigation.**

  Parts 1–5 keep their established responsibilities but use only new current evidence and honest
  results. `docs/validation.md` lists all 21 actual verdicts/states and resolution totals.
  `README.md` and `docs/PROJECT_STATUS.md` state local synthetic recovery, current Task 9 evidence
  state, no full E01–E41/live/production proof, first unmet gate, and one next action. Do not embed
  the candidate commit/tree; ignored Task 9 records own those post-commit identities.

- [ ] **Step 7.5: Build and apply the exact private denylist before staging.**

  Create a sorted UTF-8 newline file containing every actual worktree/archive/disposable/temp path,
  task/thread/client/agent ID, private URL, credential-like value if any, username-bearing path,
  and other runtime binding observed in retained artifacts. Exclude only stable public aliases and
  the historical literal `.local-handoff`. Hash the denylist and scan all eleven public candidate
  paths for exact nonempty byte matches. Separately scan portable patterns `/Users/`, `/private/`,
  `/tmp/`, `/var/`, drive-letter paths, UNC paths, UUID-like raw runtime IDs, and forbidden JSON
  keys. Store only count, denylist digest, scanner digest, and zero-match result publicly.

- [ ] **Step 7.6: Run focused tests GREEN and verify source bindings.**

  Run focused evidence tests, both JSON parsers, the archive validator, and tracked-product versus
  reviewed-product byte comparisons. Expected: focused tests PASS; JSON parses; frozen execution
  evidence remains 100% resolvable; tracked product files remain unchanged.

- [ ] **Step 7.7: Self-review public assembly before commit.**

  Verify all prose/table totals derive from JSON; every public digest resolves; every prior current
  identity is explicitly superseded; no PASS was forced; no private content leaked; and exact
  changed paths are a subset of the eleven-path allowlist. Store
  `reports/public-assembly-report.md` and regenerate the root archive manifest/sidecar.

**Commit guidance:** do not amend predecessor commits. Stage only actually changed allowlisted
paths and create one local successor commit with message
`test: retain and reverify Module 6 pilot evidence`. A later correction is a new commit.

## Task 8: Run full verification and announce READY_FOR_CHANGE_REVIEW

**Files:** ignored check outputs and Task 9 report only; tracked candidate is read-only.

**Interfaces:**

- Consumes: stable tracked candidate commit and durable archive.
- Produces: exact verification package, diff/path/immutability proof, and
  `READY_FOR_CHANGE_REVIEW` evidence pointer.

**Allowed effects:** read-only verification and ignored report/check files.

**Forbidden effects:** tracked edits, review dispatch before failures are resolved, external
actions, cleanup, and integration.

- [ ] **Step 8.1: Run full repository verification at exact candidate head.**

  Run:

  ```bash
  python3 -B -m unittest discover -s tests -v
  python3 -B -m unittest tests.test_pilot_evidence -v
  shasum -a 256 -c BASELINE.sha256
  python3 -B scripts/check_workflow.py --root . --review-state tests/fixtures/review-state/valid-final.json --json
  git diff --check
  ```

  Also run the product suite from `tests/fixtures/quietfollow/product` and from exact disposable
  merged main. Record actual counts, exits, candidate SHA, disposable SHA/tree, and checker
  revision. C01–C12 and schema tests remain mechanical, not semantic proof.

- [ ] **Step 8.2: Verify JSON, digests, redaction, and immutability.**

  Parse every tracked/ignored JSON record; rerun the archive validator and 100% resolver; rerun
  contamination and public redaction scans; compare predecessor plan, active skill, checker,
  rubric, Module 5 inputs, baseline, product public bytes, and forbidden paths against their
  accepted identities.

- [ ] **Step 8.3: Verify exact diff and changed-path allowlists.**

  Check three distinct scopes:

  - plan commit versus `b0e0c85dd0bf50e84ba1ce14ed4a985be7676002`: exactly the one addendum path;
  - recovery candidate commit versus accepted addendum commit: only actually changed paths from
    the eleven-path candidate allowlist;
  - full Module 6 candidate versus `f47263ce545c5185b3ec836c95fe341d1b3e5715`: predecessor
    13-path candidate plus this addendum
    and only justified successor changes, with product files unchanged by recovery.

  Confirm no ignored/private file is tracked and no plan artifact changed after acceptance.

- [ ] **Step 8.4: Verify disposable Git authenticity.**

  Independently resolve every named commit/tree/blob, parent edge, branch base, review head, stale
  review relation, merge ancestor, and final source/test blob. Store commands/results under
  `checks/product-git-verification.json`.

- [ ] **Step 8.5: Attempt quick validation without installing dependencies.**

  Run the existing bundled `quick_validate.py` once. If PyYAML is absent, record the exact import
  failure and limitation. Do not alter environment or success criteria.

- [ ] **Step 8.6: Write the pre-review Task 9 report.**

  Record exact candidate head/tree/parent, plan/addendum identities, frozen execution-manifest
  identity, new public digests, 100% resolution counts, tests/checker/baseline/product/Git results,
  allowlists, redaction results, limitations, and retained workspace pointer. State
  `READY_FOR_CHANGE_REVIEW`, not `READY_FOR_INTEGRATION` or `DONE`.

**Commit guidance:** no commit. If any verification requires a tracked correction, return to Task 7,
create a new successor commit, and rerun all Task 8 checks.

## Task 9: Exact-head Module Change Review and bounded recommendation

**Files:** ignored review package, `reports/module-change-review.json`, and
`reports/task9-recommendation.md`. Candidate bytes remain read-only during review.

**Interfaces:**

- Consumes: exact stable candidate head, complete requirements, public candidate diff, all check
  evidence, frozen raw execution evidence, group reviews, and product Git history.
- Produces: exact-head Change Review verdict and, only when clean, the local
  `READY_FOR_INTEGRATION` recommendation.

**Allowed effects:** read-only review and ignored review/report writes.

**Forbidden effects:** candidate edits by reviewer, author conversation in reviewer context,
Task 10, FINAL, push, PR, integration, merge, publication, install, deployment, release, and cleanup.

- [ ] **Step 9.1: Build the independent review package.**

  Include `AGENTS.md`, README/SPEC/AUDIT/EVALUATION/status/validation, both exact plan files,
  reviewer rubric, current public evidence/tests, exact candidate base/head/tree and full diff,
  verification outputs, frozen execution manifest, raw current/superseded attempts, group reviews,
  redaction checks, and disposable Git repository. Exclude author/assembler/Implementation
  conversations and expected reviewer verdict.

- [ ] **Step 9.2: Dispatch distinct full Module Change Review.**

  Request native `gpt-5.6-sol/high`. Reviewer first verifies clean identity, then independently
  resolves 100% of current input/output/evaluator/transcript digests, checks all 21 semantics
  against exact rubric, validates prohibited side effects and model facts, examines product Git
  candidates/reviews/ancestry, reviews every tracked diff, and checks scope/redaction/retention.

- [ ] **Step 9.3: Handle review findings without invalid identity reuse.**

  Any Critical or Important finding yields `CHANGES_REQUIRED`. A correction uses an authorized
  sole writer, new attempt or tracked successor commit, focused RED/GREEN evidence, full verification,
  and a completely fresh Module Change Review on the new head. Minor findings are recorded and
  corrected when they affect acceptance, evidence retention, truthfulness, or regression safety;
  any tracked byte correction still invalidates the earlier review.

- [ ] **Step 9.4: Record the final bounded state.**

  Only a clean exact-head review with no unresolved required finding may produce a task-local
  `READY_FOR_INTEGRATION` recommendation. It is not an upward ready-PR event while PR creation is
  unauthorized. The recommendation names exact head/tree, review record
  digest, frozen execution-evidence digest, actual PASS/FAIL/BLOCKED totals, first unmet gate,
  limitations, and retained workspace. If the review is not clean, remain
  `READY_FOR_CHANGE_REVIEW` only after a corrected successor is again fully verified; otherwise
  report the actual blocking finding.

- [ ] **Step 9.5: Preserve evidence after finishing.**

  Regenerate the root manifest and sidecar to include final review/recommendation records, make
  case artifacts and frozen manifest read-only, verify their digests once more, and leave the
  entire ignored recovery directory in place for the later Task 10 decision.

**Commit guidance:** no commit for clean review records. Reviewer-requested tracked corrections
use new commits; never amend, squash, reset, or reuse the invalidated review verdict.

## Review responsibilities and gates

| Gate | Independent reviewer must verify | Blocks |
|---|---|---|
| Shared schema review | path containment, schemas, case set, contamination denyset, group ownership | all case dispatch |
| Per-case evaluation | exact rubric, raw input/output/operations, actual verdict and dependent state | current case credit |
| Per-group review | complete group artifacts, evaluator independence, digest resolution, side effects | archive aggregation |
| Product Change Reviews | exact requirements/base/head/full diff/tests without author conversation | local merge and E12/E14 credit |
| Archive audit | 100% current raw evidence resolution, current/superseded identity, Git authenticity | public assembly |
| Public assembly self-review | producer/consumer consistency, truthful totals, bindings, redaction, allowlist | candidate commit |
| Module Change Review | exact full candidate plus retained raw evidence and product history | integration recommendation |

Reviewers are read-only. A reviewer never fixes its own finding, edits a verdict into compliance,
or accepts a summary in place of raw bytes. Review packages always identify requested assignment;
accepted/runtime facts remain independently sourced or `Unknown`.

## Failure, interruption, recovery, and cleanup behavior

- On interruption, stop the affected writer, close its `operations.jsonl` with an interruption
  event, hash all already written regular files, mark the attempt `incomplete`/`non-credit`, and
  retain it. Resume with the next attempt ID after verifying frozen shared inputs.
- On corrupt or digest-mismatched retained evidence, quarantine only the affected attempt by
  marking it `non-credit`; do not delete it. Rerun the case from the frozen source inputs if the
  authorization and rubric still permit it.
- On a case `FAIL`, publish FAIL if it remains current. On `BLOCKED`, publish BLOCKED and the exact
  missing evidence/capability. Do not change the rubric, conceal findings, or create repeated runs
  without a correction.
- On shared schema or binding-input drift, pause all undispatched groups; preserve completed group
  evidence; review a new shared schema/snapshot identity; rerun only cases whose inputs/contracts
  changed.
- On product-repository drift, pause delivery/release only, preserve other groups, and restore a
  clean forward sequence through a new commit/review identity. Never reset away retained history.
- On public redaction failure, do not stage. Correct public sanitisation from retained raw bytes,
  rerun regression/redaction/digest checks, commit a successor, and obtain fresh review.
- The archive is ignored local evidence, not publication scope and not a guaranteed backup. Copying
  it outside this worktree, deleting it, or changing its retention after the Task 10 decision needs
  a separate explicit owner/Product decision. This plan performs no cleanup.

## Full acceptance criteria

`MODULE6-RECOVERY-PLAN-v1` reaches its bounded Task 9 outcome only when:

1. The predecessor plan remains byte-identical at its accepted hash and this addendum is the only
   file in its plan-only commit with sole parent
   `b0e0c85dd0bf50e84ba1ce14ed4a985be7676002`.
2. The durable ignored workspace contains content-addressed raw inputs, executor outputs, evaluator
   inputs/outputs, transcript/operation records, product Git history, checks, reports, and review
   records; `/private/tmp` is not authoritative.
3. All 21 selected cases have fresh from-scratch current attempts, explicit current/superseded
   identities, separate verdict/dependent state, and requested/accepted/runtime fact separation.
4. Executor bundles are hash-bound and free of rubric, expected verdicts, evaluator notes, plan
   content, and author conversation.
5. Distinct evaluators independently score exact retained outputs; case and group failures remain
   visible and no result is forced to PASS.
6. The durable disposable Git repository contains an authentic clean forward E12/E14 sequence and
   exact reviewed merge/release rehearsal for E13/E27/E28; new honest commit/tree identities replace
   vanished identities without pretending to recreate them.
7. Final product behavior and the 15-test contract are preserved; fresh independent product Change
   Reviews bind exact candidates before local merge.
8. The frozen execution manifest resolves 100% of current raw inputs, executor outputs, evaluator
   inputs/outputs, transcripts, and product review artifacts with zero missing or mismatched bytes.
9. One public assembler updates only justified allowlisted paths; README is in permanent redaction
   coverage and asserts the local-synthetic boundary; all new public digests resolve to retained raw
   or tracked bytes.
10. Exact-value denylist and portable-pattern scans find no private path, ID, URL, credential, or
    content in public output; the ignored archive is excluded from publication.
11. Full unit tests, focused evidence tests, product tests, baseline 7/7, C01–C12, JSON, digest,
    allowlist, redaction, immutability, diff, and disposable Git ancestry/tree checks pass at the
    exact candidate head. PyYAML absence remains an explicit quick-validation limitation.
12. A distinct exact-head Module Change Review independently inspects all requirements/candidate
    bytes and resolves 100% of current raw evidence. Corrections create new commits and fresh review.
13. Final reporting stops at the Task 9 local recommendation. Task 10, integration, FINAL, GitHub,
    push/PR/merge, installation, publication, deployment, and release remain unperformed and
    unauthorized.

Structural and schema checks do not establish semantic behavioral correctness. Historical review
reports do not substitute for retained raw evidence.

## PLAN review and acceptance boundary

A distinct read-only PLAN reviewer requested as `gpt-5.6-sol/high` receives this complete addendum,
its exact containing commit/hash/parent, predecessor plan/hash, current head/tree, binding sources,
Task 9 report/review findings, and current public evidence/tests without this author's conversation.
It reviews:

- authority and exact supersession boundary;
- durable retention, manifest self-exclusion/sidecar, and no cleanup through Task 10 decision;
- complete 21-case partition and per-attempt artifact contracts;
- evaluator separation and executor contamination prevention;
- authentic disposable Git sequence and product behavior preservation;
- group path ownership, parallelism boundary, and sole public writer;
- current/superseded truthfulness, FAIL/BLOCKED handling, model-fact separation, and digest
  resolution;
- public allowlist, README boundary/redaction regression, no self-referential head, and private
  publication boundary;
- verification, correction invalidation, Task 9 stopping point, and forbidden Task 10/FINAL actions.

`PLAN_PASS` requires no unresolved Critical or Important finding and binds exact addendum bytes,
containing commit, parent `b0e0c85dd0bf50e84ba1ce14ed4a985be7676002`, and predecessor plan hash. Any addendum correction creates a
new plan-only commit and requires a fresh complete PLAN review. Acceptance authorizes execution only
through the Task 9 bounded recommendation described here.
