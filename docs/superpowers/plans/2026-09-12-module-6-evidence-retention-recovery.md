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

- Recovery source/candidate predecessor:
  `b0e0c85dd0bf50e84ba1ce14ed4a985be7676002`, tree
  `fb7d90cd33b8604a51b53059b7602463f043e5f8`, branch
  `codex/module6-quietfollow-pilot`.
- Initial addendum commit: `21c1509dce231069e1ec49dd36d751ff85999e08`, tree
  `b85abfd07edcd56f2ec1b410796b1101c7ea5057`, sole parent the recovery predecessor
  above. Correction round 1 uses that initial addendum commit as its sole parent and changes only
  this addendum. The corrected containing commit/hash are supplied by the plan-author report and
  exact PLAN-review package, never self-recorded in these tracked bytes.
- The addendum identity remains `MODULE6-RECOVERY-PLAN-v1`; correction round 1 supersedes only the
  initial addendum bytes for execution authority. A PLAN reviewer must bind the corrected bytes and
  commit explicitly; the initial bytes remain immutable Git history and confer no execution credit.
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

- Execute on an isolated `codex/` branch/worktree rooted at the accepted corrected-addendum commit.
  Before any recovery write, verify that the corrected plan commit has sole parent
  `21c1509dce231069e1ec49dd36d751ff85999e08`, that the initial addendum has sole parent
  `b0e0c85dd0bf50e84ba1ce14ed4a985be7676002`, that the predecessor plan hash still matches, and
  that tracked/index state is clean.
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

### Plan-history commits only

- Initial addendum commit `21c1509dce231069e1ec49dd36d751ff85999e08` created
  `docs/superpowers/plans/2026-09-12-module-6-evidence-retention-recovery.md` over sole parent
  `b0e0c85dd0bf50e84ba1ce14ed4a985be7676002`.
- Correction round 1 modifies only that same addendum over sole parent
  `21c1509dce231069e1ec49dd36d751ff85999e08`; its required subject is
  `docs: harden Module 6 recovery plan`.
- Exact changed-path allowlist for either plan commit is the one path above. No recovery-candidate
  path belongs in either plan-history commit, and no plan path belongs in a candidate commit.

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
checks/execution-evidence-manifest-v<N>.json
checks/execution-evidence-manifest-v<N>.sha256
checks/execution-evidence-audit-v<N>.json
checks/execution-evidence-current.json
checks/digest-resolution-v<N>.json
checks/bundle-contamination.json
checks/private-denylist.txt
checks/private-denylist.sha256
checks/redaction-scan-precommit-v1.json
checks/public-content-hashes-<candidate-head>.json
checks/redaction-scan-<candidate-head>.json
checks/product-git-verification.json
reports/<group>-report-v<N>.md
reports/<group>-manifest-v<N>.json
reports/<group>-review-v<N>.json
reports/task1-schema-review-v<N>.json
reports/public-assembly-report-v<N>.md
reports/module-change-review-<candidate-head>.json
reports/task9-report-<candidate-head>.md
reports/task9-recommendation-<candidate-head>.md
```

The root `manifest.json` is regenerated atomically only by the Task coordinator's designated
manifest writer. It lists every retained regular file except `manifest.json` and
`manifest.sha256`; `manifest.sha256` contains the SHA-256 of the exact current manifest bytes.
Before public assembly, freeze the evidence set as append-only generation
`checks/execution-evidence-manifest-v1.json` plus its sidecar. A correction creates v2, then v3;
old generation bytes and sidecars remain unchanged. Only `checks/execution-evidence-current.json`
is the manifest-writer-owned mutable selection record, and it may select a generation only after a
distinct archive audit passes. Public files bind the selected generation number and digest, never
an ignored path. Later review records may advance the root manifest without changing a selected
execution generation.
For report paths, `N` is that group's or schema review's positive monotonic sequence; prior report
bytes are never overwritten. `<candidate-head>` is replaced with the exact lowercase 40-hex commit
already created before that ignored report, so it is not a tracked self-reference.

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

The exact ordered case set is `E02, E08, E10, E11, E12, E13, E14, E17, E20, E21, E22, E25,
E27, E28, E31, E33, E34, E37, E38, E39, E41`. Every schema and derived count uses this order; no
case may be added, omitted, or reordered.

### Root content-addressed manifest

`manifest.json` has exactly these top-level keys and types:

| Key | Type and invariant |
|---|---|
| `schema_version` | integer `3` |
| `recovery_plan` | string `MODULE6-RECOVERY-PLAN-v1` |
| `predecessor` | object with exactly `candidate_head`, `candidate_tree`, `accepted_plan_identity`, `accepted_plan_sha256`, `accepted_plan_commit`, `implementation_base`, all nonempty strings and SHA fields lowercase 40/64 hex as applicable |
| `inventory_exclusions` | array exactly `['manifest.json', 'manifest.sha256']` in that order |
| `artifacts` | array of artifact records defined below |
| `cases` | array of case records defined below |
| `groups` | array of group records defined below |
| `retention` | object with exactly `authoritative_root='recovery-worktree-relative'`, `retain_through='Task 10 decision'`, `cleanup_authorized=false`, `publication_scope=false` |
| `limitations` | array of nonempty strings |

Each artifact record has exactly these keys:

| Key | Type and invariant |
|---|---|
| `logical_id` | unique nonempty string matching `^[A-Za-z0-9][A-Za-z0-9._-]*$` |
| `case_id` | one selected E-case string for case evidence; JSON `null` for shared/product/group/check/review evidence |
| `attempt_id` | `<case_id>-r<sequence>` for case evidence; JSON `null` otherwise |
| `kind` | one of `raw_input`, `executor_prompt`, `bundle_manifest`, `executor_output`, `result_record`, `evaluator_input`, `evaluator_prompt`, `evaluator_output`, `transcript`, `session_receipt`, `product_git`, `check`, `report`, `review` |
| `relative_path` | unique canonical POSIX path relative to recovery root |
| `sha256` | lowercase 64-hex digest of exact file bytes |
| `byte_count` | nonnegative integer equal to actual file size |
| `content_type` | one of `application/json`, `application/jsonl`, `text/markdown`, `text/plain`, `application/octet-stream` |
| `producer_alias` | nonempty role alias present in the role/ownership table |
| `credit_state` | one of `current`, `superseded`, `non-credit`, `shared` |
| `sensitivity` | one of `private`, `public-source` |
| `empty_allowed` | boolean; `true` only for a case contract that explicitly expects an empty file |

The manifest writer enumerates the recovery root with `os.scandir`/`lstat`, including every
regular file under `product-repo/repository/.git/**`. The actual inventory is the sorted canonical
POSIX relative path of every regular file except exactly `manifest.json` and `manifest.sha256`.
Any symlink node, symlinked ancestor, socket, device, FIFO, unresolved node, or path outside the
root is an error. The declared set of `artifacts[].relative_path` must equal the actual inventory:
no unlisted, missing, duplicate, or extra file. A path is rejected if it is empty, absolute,
contains `\`, contains an empty/`.`/`..` component, begins or ends with `/`, contains `//`, differs
from `PurePosixPath(path).as_posix()`, or if any component's `lstat` is a symlink. The validator
recomputes every size/digest and separately verifies that `manifest.sha256` is exactly one line
`<64 lowercase hex><two spaces>manifest.json\n` matching the current manifest bytes.

### Root case and group schemas

Each root `cases[]` record has exactly:

| Key | Type and invariant |
|---|---|
| `case_id` | unique member of the exact 21-case set |
| `group` | one of `discovery-readiness`, `delivery-release`, `resume-scaling`, `coordination`; must match the fixed partition |
| `current_attempt_id` | string matching `<case_id>-r<positive integer>` |
| `attempts` | nonempty array of attempt records, ordered by sequence |
| `evaluation_verdict` | one of `PASS`, `FAIL`, `BLOCKED`; equals current evaluator-output bytes |
| `dependent_action_state` | nonempty string; differs from the verdict token and equals current evaluator-output bytes |
| `requested_assignments` | nonempty array of exact role/model/reasoning records |
| `accepted_native_assignments` | same role set, each value nonempty string or `Unknown` |
| `independently_verified_runtime_facts` | same role set, each `value` nonempty string or `Unknown` and `receipt_logical_id` null when Unknown |
| `current_logical_ids` | object with the exact evidence-reference keys below |

Each `requested_assignments[]` item has exactly `role_alias`, `model`, and `reasoning`; the latter
two equal the role table. Each `accepted_native_assignments[]` item has exactly `role_alias`,
`value`, and `receipt_logical_id`; each runtime-fact item has those same exact keys. Role aliases
are unique and the three arrays have the identical role set. A receipt logical ID is JSON null
when `value` is `Unknown`; otherwise it joins exactly one current `session_receipt` artifact whose
exact bytes prove that value. Unsupported inferences from prose, model self-report, or request are
rejected.

Each `attempts[]` record has exactly `attempt_id`, `sequence`, `credit_state`, `supersedes`,
`correction_reason`, and `logical_ids`. `sequence` is a positive integer; `attempt_id` equals
`<case_id>-r<sequence>`; sequences are strictly increasing without duplicates. `credit_state` is
`current`, `superseded`, or `non-credit`; exactly one attempt is `current`, and it equals
`current_attempt_id`. The first attempt has `supersedes=null` and `correction_reason=null`; a later
attempt names the immediately prior attempt in `supersedes` and a nonempty observed correction
reason. Previous credit-bearing attempts become `superseded`; contaminated/malformed/incomplete
attempts remain `non-credit`. No artifact can claim `current` unless its attempt is current.

Both attempt `logical_ids` and case `current_logical_ids` have exactly:

```json
{
  "raw_inputs": [],
  "executor_prompts": [],
  "bundle_manifests": [],
  "executor_outputs": [],
  "result_records": [],
  "evaluator_inputs": [],
  "evaluator_prompts": [],
  "evaluator_outputs": [],
  "transcripts": [],
  "session_receipts": []
}
```

Every array is nonempty. Each logical ID resolves to exactly one artifact record with matching
`case_id`, `attempt_id`, expected `kind`, and credit state. For the current attempt, the union of
these arrays equals every current artifact for that case and contains the required exact filenames
listed below. The validator derives artifact kinds from those joined records; it does not accept a
declared `current_artifact_kinds` shortcut. Executor and evaluator receipts must identify distinct
session aliases; requested/accepted/runtime roles must join to those receipts.

Each root `groups[]` record has exactly `group_id`, `case_ids`, `owned_roots`,
`group_manifest_logical_id`, `group_report_logical_id`, `group_review_logical_id`, and
`review_verdict`. `group_id` and `case_ids` equal the fixed partition; `owned_roots` equals the exact
paths in the group table; the three logical IDs resolve to distinct current/shared artifacts;
`review_verdict` equals the retained group-review bytes and is one of `PASS` or
`CHANGES_REQUIRED`.

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

The physical executor bundle is the directory named by `source-manifest.json.bundle_root`. Its
bundle manifest has exactly `schema_version=1`, `case_id`, `attempt_id`,
`contamination_contract_sha256`, and `files`. Each `files[]` record has exactly `relative_path`,
`kind`, `sha256`, and `byte_count`. Before dispatch and again after output, the recorder recursively
enumerates every regular bundle file, rejects every symlink/special/escaped path, and requires exact
set equality with `files[].relative_path`. It recomputes every file digest/size and scans every exact
byte sequence. `executor-prompt.txt` is outside the bundle directory but is always separately
hashed and scanned by its required logical ID. An unlisted contaminated file or contaminated prompt
therefore fails the attempt.

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
  selected `checks/digest-resolution-v<N>.json` record contains independently derived numerator,
  denominator, misses, and duplicate logical IDs; public assembly is blocked unless resolution is
  100% with zero misses.

### Append-only execution-manifest generations

`N` in `execution-evidence-manifest-v<N>.json` is a positive integer without leading zero.
Generation files and sidecars are append-only and never edited, renamed, or deleted. A generation
contains exactly `schema_version=1`, `generation=N`, `recovery_plan`, `created_from_root_manifest_sha256`,
`case_ids`, `artifacts`, `public_digest_classes`, and `supersedes_generation`. `case_ids` is the exact
21-case set. `artifacts` uses the exact root artifact schema and includes all current/superseded case
artifacts, every product Change Review/candidate/Git record needed by a public claim, and all four
group manifests/reports/reviews. It excludes its own bytes/sidecar and the audit that will consume
it. `schema_version`/`generation` are integers, `recovery_plan` is the addendum identity,
`created_from_root_manifest_sha256` is lowercase 64-hex, and `case_ids` is the fixed sorted array.
`public_digest_classes` is exactly an object whose keys are `retained-private` and `tracked-public`
and whose values are sorted unique logical-ID arrays; private IDs join generation artifacts and
tracked IDs resolve from public tracked bindings. `supersedes_generation` is JSON null for v1 and
integer `N-1` thereafter. Unknown keys, duplicate IDs, wrong ordering, or an artifact outside the
root schema fail validation.

After freezing generation N and its exact sidecar, a distinct archive auditor consumes it and writes
`checks/execution-evidence-audit-v<N>.json`; that audit is a separate retained output and is not
required to hash itself or appear in generation N. Its digest never appears publicly. Only after the
audit verdict is PASS may the manifest writer atomically replace `execution-evidence-current.json`,
whose exact keys are `schema_version=1`, `selected_generation=N`, `manifest_sha256`,
`manifest_logical_id`, `audit_logical_id`, `audit_sha256`, and `selected_at_sequence`.
The pointer has no other keys: generation/sequence are positive integers, IDs are unique nonempty
strings joining root-manifest artifacts, and digests are lowercase 64-hex matching actual bytes.
The audit has exactly `schema_version=1`, integer `generation`, `manifest_sha256`,
`root_manifest_sha256`, `reviewer_alias`, requested/accepted/runtime assignment objects,
`derived_counts`, arrays `missing`, `extra`, `duplicates`, `mismatches`, and `verdict`; its verdict is
`PASS` only when all four error arrays are empty and every derived required-kind numerator equals
its independently observed denominator.

Any case, product-review, group-review, contamination, or archive-audit correction after freeze
creates generation N+1. Generation N and its sidecar remain byte-identical; N+1 includes the new
artifacts and all earlier retained attempts/reviews, records N as superseded in the mutable selection
record, receives a fresh independent audit, and becomes selected only after PASS. Public assembly
binds only the latest selected generation number/digest. If public files already exist, a new
generation requires a new public assembly commit, a new exact-head redaction receipt, full checks,
and fresh Module Change Review.

### Non-tautological private resolver

The private resolver starts from actual tracked public bytes, not root-manifest or public summary
counts. It parses both public JSON files, collects every current evidence reference and every other
current SHA-256 claim, and derives denominators by `digest_class`/`kind`. Superseded predecessor
records are excluded only because their explicit state is `superseded`; no current digest may be
unresolved. For each
`retained-private` reference it loads the selected generation by recomputing candidate generation
file hashes until exactly one matches the public generation digest; joins `logical_id`, `case_id`,
`attempt_id`, `kind`, and SHA-256 to exactly one generation artifact; then opens the retained file
via its private relative path and recomputes bytes/size/digest. For each `tracked-public` reference
it maps the declared stable tracked path, reads the actual tracked file, and recomputes its digest.
It independently verifies required reference categories per public-current case and rejects a
public reference missing from the selected generation, an unreferenced claimed current artifact,
duplicate logical ID, mismatched digest/class/kind/case/attempt, or public private-path field.
Generation, denylist, snapshot, plan, public-part, execution-record, navigation, evidence-test, and
product digests are separately joined through their stable logical ID or tracked path and exact
bytes; the public manifest itself is bound by the external exact-head content-hash record.
`digest-resolution-v<N>.json` reports recomputed numerator/denominator/misses per category; no
manifest/public declared count is used as an input to those totals.

### Tracked public successor schemas

The tracked `tests/fixtures/quietfollow/evidence/manifest.json` has exactly these top-level keys:
`schema_version`, `module`, `recovery`, `repository`, `snapshots`, `permissions`, `roles`,
`tracked_bindings`, `parts`, `redaction`, `superseded_predecessor_evidence`, and `limitations`.
Unknown keys fail validation. Required shapes are:

- `schema_version` is integer `2`; `module` is string `MODULE6-PLAN-v1`.
- `recovery` has exactly `plan_identity`, `plan_sha256`, `predecessor_candidate_head`,
  `predecessor_evidence_state`, `predecessor_evidence_reason`, `evidence_generation`,
  `evidence_generation_logical_id`, and `evidence_generation_sha256`. The state is `superseded`,
  generation is a positive integer, SHA values are lowercase 64-hex, the logical ID joins the root
  manifest generation artifact during private review, and no ignored/private path appears.
- `repository` has exactly `candidate_identity`, `disposable_repository_kind`,
  `disposable_merged_commit`, `disposable_merged_tree`, `product_test_result`,
  `tracked_product_source_sha256`, and `tracked_product_test_sha256`. The kind is
  `local-synthetic`; commit/tree values are lowercase 40-hex identities of the retained repository,
  not the self-referential harness candidate head; `product_test_result` has exactly integer
  `passed`, integer `failed`, and string `scope`.
- `snapshots` is a nonempty array of exact records `{id, source_class, sha256, byte_count}` where
  `source_class` is `tracked-binding`, `legacy-private-input`, or `synthetic-fixture`; `id` is a
  stable public alias, never a private path. `permissions` has exactly arrays `allowed`, `forbidden`
  and boolean `external_actions_performed=false`.
- `roles` is a nonempty array of exact records `{alias, requested_model, requested_reasoning,
  accepted_native_assignment, independently_verified_runtime_fact}`. The requested pair must
  match the role table below; the last two strings are `Unknown` absent authoritative receipts.
- `tracked_bindings` is an array of exact records `{logical_id, path, kind, sha256}`. `path` is a
  unique canonical repository-relative POSIX path in the tracked candidate; `kind` is
  `public_part`, `execution_record`, `navigation`, `product_source`, `product_test`,
  `evidence_test`, or `validation`; each digest resolves from the exact candidate blob during
  exact-head review. This array does not list `manifest.json` itself; its bytes are bound externally
  by the exact-head public-content-hash and redaction records, avoiding a digest fixed point.
- `parts` is exactly five records `{id, path, sha256, current_case_ids}` for part IDs 1–5 and the
  file/case mapping in this plan. Paths join one `tracked_bindings` record and digests match.
- `redaction` has exactly `policy_version=1`, nonempty `denylist_logical_id`, integer
  `denylist_value_count`, lowercase-64-hex `denylist_sha256`, integer `exact_value_matches=0`,
  integer `portable_pattern_matches=0`, and
  `final_receipt_scope='ignored exact-head review evidence'`. The logical ID resolves the retained
  denylist during private review. It contains no scan artifact path or digest, so the public scan
  set is not self-referential.
- `superseded_predecessor_evidence` is a nonempty array of exact records `{logical_id, sha256,
  state, reason}` where `state='superseded'`; `limitations` is an array of nonempty strings.

The tracked `tests/fixtures/quietfollow/evidence/execution-record.json` has exactly these top-level
keys: `schema_version`, `harness_identity`, `evidence_generation`, `cases`, `verdict_totals`,
`resolution_summary`, `metrics`, `open_findings`, `reruns`, `mechanical_test_limitation`, and
`overall_limitation`. Unknown keys fail validation. `schema_version` is integer `2`;
`harness_identity` is a nonempty stable label rather than a self-head; `evidence_generation` has
exactly integer `number` and lowercase-64-hex `sha256` matching public manifest `recovery`.

`cases` is the exact 21-case set, one record per ID, and each record has exactly:

```text
id, current_attempt_id, mode, mode_detail, allowed_side_effects,
forbidden_side_effects, executor_aliases, evaluator_alias,
requested_assignments, accepted_native_assignments,
independently_verified_runtime_facts, evidence_refs, actual_outcome,
evaluation_verdict, dependent_action_state, findings, rerun_history,
predecessor_evidence
```

`mode` is one of `offline-simulation`, `local-synthetic-product`, or `read-only-analysis`;
`mode_detail`, `actual_outcome`, and `dependent_action_state` are nonempty strings; allowed/
forbidden side effects, executor aliases, findings, and rerun history are arrays; evaluator alias is
nonempty; verdict is `PASS`, `FAIL`, or `BLOCKED`. Assignment fields use the same exact role/value
records as the root case schema. `predecessor_evidence` is a nonempty array of exact records
`{logical_id, sha256, state, reason}` with state `superseded`.

Each `evidence_refs[]` record has exactly `{logical_id, kind, digest_class, sha256, case_id,
attempt_id}`. `digest_class` is `retained-private` or `tracked-public`; other fields must match the
current case/attempt and the exact artifact-kind enum. A retained-private reference joins the
selected ignored generation during exact-head review through logical ID plus digest, without
publishing its path. A tracked-public reference joins `manifest.json.tracked_bindings` by logical
ID and digest. The five evidence-reference classes `raw_input`, `executor_output`,
`evaluator_input`, `evaluator_output`, and `transcript` are nonempty for every case; session and
result records are also required by the private archive schema.

`verdict_totals` has exactly integer `PASS`, `FAIL`, `BLOCKED`, and `total`; tests recompute these
from `cases`. `resolution_summary` is an object keyed by each public evidence kind, each value
exactly `{resolved, total, result}` with nonnegative integers and `result='complete'` only when
equal. These public counts are derived consistency claims, not private resolution proof. `metrics`
is an array with exactly one record for each of `manual_owner_relay_events`,
`duplicate_owner_approval_prompts`, `duplicate_user_owned_task_creations`,
`duplicate_internal_work_launches`, `invalid_pass_uses`, and `incorrect_transitions`; each record
has exactly `{name, value, unit, observation_start_ref, observation_end_ref, denominator,
exclusions}`, with integer value, `unit='event'`, two stable evidence logical IDs, nonempty
denominator, and string-array exclusions. `open_findings[]` has exactly `{id, severity, state,
summary, evidence_refs}` with severity `Critical`, `Important`, or `Minor` and state `open` or
`resolved`. `reruns[]` has exactly `{case_id, attempt_id, supersedes, correction_reason, state}`
with state `current`, `superseded`, or `non-credit`. The two limitation fields are nonempty strings.

Permanent tests are portable: they read only tracked files, validate the two schemas and internal
tracked joins, and work in a clean clone. They must neither open nor mention the ignored recovery
root. Exact private resolution is a separate Task 8 review check: the review package supplies the
ignored selected-generation file out of band, recomputes the public generation digest, and joins
public stable logical IDs to private paths internally. Public files therefore expose digests and
portable aliases, never private paths.

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
four briefs. `delivery-release` is the only group whose workflow may write `product-repo/**`;
within that group, recorder and Git writers use only the disjoint/sequential paths in the role table.
No other group writes there.

The public assembler uses this fixed producer/consumer mapping; it does not need any earlier
conversation to decide where a case belongs:

| Public part | Current case evidence consumed | Subject retained |
|---|---|---|
| `part-1-discovery.md` | E38 | Positioning → proportionate Gate 3.5 boundary → Journey dependency |
| `part-2-readiness.md` | E31, E39 | prototype architecture scope and changed-only Gate 8 economics |
| `part-3-delivery.md` | E12, E14 | WorkItem TDD, independent review/correction, stale-PASS rejection |
| `part-4-release-rehearsal.md` | E13, E27, E28 | exact local merge, stale FINAL routing, rollout/rollback, open manual evidence |
| `part-5-resume-scaling.md` | E02, E25, E33, E34, E37, E41, E08, E10, E11, E17, E20, E21, E22 | resume/scaling plus offline coordination and permission/model boundaries |

### Exact role, model, and write ownership

Every alias below is a distinct session unless a row explicitly says it is the same sequential
owner. Requested assignment is recorded before dispatch. Accepted native assignment and runtime
fact remain `Unknown` unless separate authoritative receipts establish them.

| Role aliases | Requested model/reasoning | Allowed write location | Responsibility and transfer rule |
|---|---|---|---|
| `plan-author` | `gpt-5.6-sol/high` | this tracked addendum during plan-history commits; ignored `plan-author-report*.md` only | Plan-only writer; relinquishes tracked ownership before PLAN review or recovery execution. |
| `task-coordinator` | `gpt-5.6-sol/high` | no artifact bytes; dispatch/state only | Sequences roles and never materializes another role's output. |
| `schema-binding-writer` | `gpt-5.6-sol/medium` | `inputs/binding/**`, `checks/archive-validator.py`, `checks/archive-validator-tests.py`, `checks/bundle-contamination.json`, four group briefs | Ends ownership before group dispatch. |
| `root-manifest-writer` | `gpt-5.6-sol/medium` | root `manifest.json`/`manifest.sha256`, `checks/execution-evidence-*`, `checks/digest-resolution-*`, `reports/task1-schema-review-v<N>.json` | Only root/inventory/generation writer; receives closed role/group records sequentially. |
| `discovery-recorder`, `resume-recorder`, `coordination-recorder` | `gpt-5.6-terra/medium` | only their exact disjoint group `inputs/`, `executions/`, `evaluations/`, `transcripts/`, and `reports/*` roots | Materialize neutral fixtures and immutable payloads returned by executors/evaluators/reviewers; never write another group. |
| `delivery-recorder` | `gpt-5.6-terra/medium` | delivery group `inputs/`, `executions/`, `evaluations/`, `transcripts/`, `reports/delivery-release-*`, `product-repo/reviews/**`, and `product-repo/rehearsals/**` except `seed-oracle-v1.json` | Materializes delivery role/reviewer payloads; never writes `product-repo/repository/**` or the seed oracle. |
| `E02-executor`, `E08-executor`, `E10-routing-executor-1`, `E10-routing-executor-2`, `E11-executor`, `E12-executor`, `E13-executor`, `E14-executor`, `E17-executor`, `E20-executor`, `E21-executor`, `E22-executor`, `E25-executor`, `E27-executor`, `E28-executor`, `E31-executor`, `E33-executor`, `E34-executor`, `E37-executor`, `E38-executor`, `E39-executor`, `E41-executor` | `gpt-5.6-sol/high` | no direct workspace write; returns exact prompt-bound payload to owning recorder | Fresh case/discovery/coordination execution; E13, E27, and E28 are necessarily three different sessions/artifacts. |
| `wi1-writer`, `wi2-writer`, `correction-writer`, `whitespace-writer` | `gpt-5.6-sol/medium` | `product-repo/repository/**` on assigned branch interval only | Ordinary product writer. Repository ownership transfers sequentially; no concurrent Git writer. |
| `seeded-fixture-preparer` | `gpt-5.6-terra/medium` | `product-repo/repository/**` during S interval and `product-repo/rehearsals/seed-oracle-v1.json` | Receives ownership after C and relinquishes it before review; small deliberate test fixture only. |
| `architecture-analyst`, `architecture-reviewer` | `gpt-6-astra/high` | no direct workspace write; returns exact payload to `coordination-recorder` | Analyst and reviewer are distinct; reviewer receives requirements/candidate independently. |
| `E02-evaluator`, `E08-evaluator`, `E10-evaluator`, `E11-evaluator`, `E12-evaluator`, `E13-evaluator`, `E14-evaluator`, `E17-evaluator`, `E20-evaluator`, `E21-evaluator`, `E22-evaluator`, `E25-evaluator`, `E27-evaluator`, `E28-evaluator`, `E31-evaluator`, `E33-evaluator`, `E34-evaluator`, `E37-evaluator`, `E38-evaluator`, `E39-evaluator`, `E41-evaluator` | `gpt-5.6-sol/high` | no direct workspace write; returns exact JSON payload to owning recorder | One distinct evaluator per case, never its executor; specifically E13/E27/E28 have three distinct evaluators. |
| `wi1-change-reviewer`, `S-change-reviewer`, `R-change-reviewer`, `B-change-reviewer` | `gpt-5.6-sol/high` | no direct workspace write; returns review payload to `delivery-recorder` | Fresh full product Change Review of the exact named head. |
| `schema-reviewer`, `discovery-group-reviewer`, `delivery-group-reviewer`, `resume-group-reviewer`, `coordination-group-reviewer`, `archive-auditor`, `module-change-reviewer`, `plan-reviewer` | `gpt-5.6-sol/high` | no direct workspace write; return payload to current recorder/root writer | Independent requirements/candidate review; no author conversation. |
| `public-assembler` | `gpt-5.6-sol/medium` | only eleven tracked candidate paths plus `reports/public-assembly-report-v<N>.md` | Sole tracked writer; ownership begins only after selected archive audit PASS and ends at candidate commit. |
| `exact-head-check-recorder` | `gpt-5.6-sol/medium` | ignored `checks/public-content-hashes-<candidate-head>.json`, `checks/redaction-scan-<candidate-head>.json`, `reports/task9-report-<candidate-head>.md`, `reports/module-change-review-<candidate-head>.json`, `reports/task9-recommendation-<candidate-head>.md` | Records post-commit read-only checks/review payloads; cannot edit tracked bytes. |

Agent payloads are immutable return values; only the designated recorder materializes them under
its allowed directory and hashes the exact bytes. Each ownership handoff is an ordered event in the
relevant `operations.jsonl` or product Git record. A writer must close, hash, and relinquish its
scope before the next sequential owner begins. Parallel work is limited to the four recorders'
disjoint directories after Task 1; reviews, root aggregation, public assembly, and product Git
ownership are sequential.

## Task 1: Freeze durable schemas, binding inputs, and contamination checks

**Files:**

- Create all durable ignored root directories and the initial files under `checks/`.
- Copy binding inputs to `inputs/binding/` as regular read-only files.
- Do not modify tracked files.

**Interfaces:**

- Consumes: accepted addendum commit, exact predecessor identities, current tracked binding files.
- Produces: schema v3, immutable binding snapshot, group path ownership table, archive validator,
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
  git rev-parse 21c1509dce231069e1ec49dd36d751ff85999e08^
  git diff --name-only 21c1509dce231069e1ec49dd36d751ff85999e08...HEAD
  ```

  Expected: `HEAD` is the accepted addendum commit; its sole parent is
  `21c1509dce231069e1ec49dd36d751ff85999e08`; the initial addendum's sole parent is
  `b0e0c85dd0bf50e84ba1ce14ed4a985be7676002`; tracked state is clean; predecessor plan digest is
  `6037149b9a70cdeba4b8f1fd4fcce460b9206730665c8aa69f4ee781eb5c4777`; the
  parent-to-head path set is only this addendum. Stop before writes if any check differs.

- [ ] **Step 1.2: Write archive-validator tests first.**

  Create ignored `checks/archive-validator-tests.py`. Its valid fixture contains all 21 cases,
  every required per-attempt filename/category, all four groups, a fully enumerated actual tree,
  and a valid sidecar. Write separate negative tests for: unknown/missing/wrong-type keys at every
  schema level; an actual unlisted file; a declared missing file; duplicate path; duplicate logical
  ID; absolute, empty, backslash, `//`, `.`, and `..` paths; symlink file; symlink ancestor; FIFO or
  other special node where the platform permits; escaped root; digest, byte-count, empty-file, and
  sidecar mismatch; duplicate/missing case; wrong group; zero/two current attempts; skipped or
  duplicate attempt sequence; bad supersedes edge; current logical ID joining wrong case, attempt,
  kind, or credit state; a missing required filename/category; receipt aliases that are not
  distinct; accepted/runtime receipt mismatch; bundle unlisted/missing/symlink file; bundle and
  prompt digest mismatch; forbidden logical kind; forbidden exact bytes in any listed or unlisted
  bundle file and in `executor-prompt.txt`; selected-generation digest/number mismatch; and public
  resolution whose summary count lies or whose logical reference has no exact filesystem byte.

- [ ] **Step 1.3: Run the validator tests RED.**

  Run:

  ```bash
  python3 -B .superpowers/sdd/2026-09-12-module-6-evidence-retention-recovery/checks/archive-validator-tests.py
  ```

  Expected: FAIL because `checks/archive-validator.py` does not yet exist.

- [ ] **Step 1.4: Implement the minimum ignored validator and resolver.**

  `archive-validator.py` defines constants for the exact 21-case set, fixed group partition, exact
  key sets, enums, per-attempt filename/category map, two inventory exclusions, and contamination
  denyset. Implement concrete functions named `actual_inventory`, `validate_root_schema`,
  `validate_inventory`, `validate_case_joins`, `validate_bundle`, `validate_generation`, and
  `resolve_public_current`, with these mandatory algorithms and no manifest-derived shortcuts.
  `actual_inventory`
  recursively uses `os.scandir` plus `lstat`, errors on every symlink/special/unresolved/escaped
  node, hashes all regular files except exactly the two exclusions, and returns the independently
  observed path/size/digest map. `validate_root_schema` enforces every exact key/type/enum in this
  plan. `validate_inventory` requires exact equality of actual and declared path sets plus unique
  logical IDs/paths and exact byte count/digest/nonempty policy. `validate_case_joins` derives the
  current attempt, kind coverage, filenames, and role/session relationships by joining each logical
  ID to exactly one artifact; it never reads a declared count or kind summary. `validate_bundle`
  enumerates its physical root independently and scans every actual byte plus the separately hashed
  prompt. `validate_generation` recomputes the generation and sidecar identities and its required
  artifact set. `resolve_public_current` starts only from actual public case references and public
  tracked bindings, locates exactly one selected generation by digest, opens every joined byte, and
  computes its own denominators. The entry point emits deterministic sorted JSON and exits zero
  only for zero errors.

- [ ] **Step 1.5: Run validator tests GREEN and freeze their bytes.**

  Expected: all validator tests PASS. Run the valid fixture once through the command-line entry
  point and require independently enumerated `declared_files == actual_files` and zero errors.
  Hash both validator files and add them to the initial root manifest before any group dispatch.

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
  paths, and all 21 case slots. Store `reports/task1-schema-review-v1.json`. A non-PASS review blocks
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
  and operation record. Request `gpt-5.6-sol/high`. The evaluator returns one JSON verdict bound to
  exact digests and states the dependent gate/action separately; `discovery-recorder` materializes
  and hashes it without alteration.

- [ ] **Step 2.5: Preserve failures and corrections.**

  If a case is `FAIL`, record the violated observable behavior and keep dependent work open or
  blocked according to the rubric. If `BLOCKED`, name the missing artifact/capability. A corrected
  rerun uses the next attempt ID and retains the earlier bytes.

- [ ] **Step 2.6: Run independent group review.**

  A fresh read-only reviewer verifies exact case coverage, rubric isolation, raw digest resolution,
  synthetic/local boundaries, Gate 3.5 versus Gate 8 reuse, and verdict/dependent-state truthfulness.
  Store `reports/discovery-readiness-review-v1.json`; no group PASS is inferred from case count.

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
  minimum `Tracker`; run GREEN; commit. Request `gpt-5.6-sol/medium` for `wi1-writer`. A fresh
  `gpt-5.6-sol/high` Change Reviewer receives exact
  requirements, base/head, full diff, commands/results, and candidate files without the writer's
  conversation. Correct findings with successor commits and fresh full review. Merge only the
  exact reviewed head to local `main` using `--no-ff` and record commit/tree ancestry.

- [ ] **Step 3.3: Build WorkItem 2 and an authentic forward finding/correction sequence.**

  On `codex/quietfollow-wi2` from reviewed WorkItem 1 main, write RED tests for outcome persistence,
  completed-item filtering, unknown follow-up preservation, reconstruction, blank outcome, and
  exact spaced outcome; request `gpt-5.6-sol/medium` for `wi2-writer`, implement to GREEN, and
  commit ordinary candidate C. Transfer sole-writer
  ownership to a bounded fixture preparer, create one deterministic seeded defect S without
  revealing its oracle in commit subject or reviewer bundle, and end that writer interval.

  The fixture preparer is requested as `gpt-5.6-terra/medium`. Save the exact bytes from
  `git cat-file commit C` and compute `seed_sha256 = SHA-256(those exact bytes)`. Let
  `seed_index = int(seed_sha256[0:16], 16) % 3`; select from this fixed ordered matrix:

  | Index | Exact mutation in S | Private oracle focused test |
  |---|---|---|
  | 0 | Remove the guard that rejects an unknown `contact_id`, so an unknown contact is accepted | `test_unknown_contact_is_rejected_without_mutating_store` |
  | 1 | Reverse the default completed-item predicate, so completed follow-ups appear in the default list | `test_completed_follow_up_is_hidden_by_default` |
  | 2 | Remove the completed-outcome store write, so the result disappears after reconstruction | `test_completed_outcome_survives_reconstruction` |

  Commit S with neutral subject `test: exercise reviewed tracker variant`. Retain exact JSON
  `product-repo/rehearsals/seed-oracle-v1.json` containing C commit-byte digest, matrix version,
  selected index, mutation, focused test, S commit/tree, and its own schema version. Hash the oracle
  file, but exclude its path, digest, selected index, mutation, and focused test from S reviewer
  inputs and from all case executor bundles until the S review verdict bytes are closed and hashed.

- [ ] **Step 3.4: Obtain a clean independent review of S.**

  A fresh Change Reviewer receives requirements, WorkItem base, S head, complete base..S diff,
  tests, and no Implementation/fixture-preparer conversation or expected finding. Record the
  actual verdict. The reviewer is `S-change-reviewer`, requested `gpt-5.6-sol/high`. If it misses
  the seeded violation, E14 may be `FAIL`; reveal the oracle only after that verdict, then create a
  distinct correction attempt. Never rewrite the missed review.

- [ ] **Step 3.5: Correct on the same WorkItem branch and re-review.**

  Forward the actual finding internally to one recorded writer/replacement. First demonstrate the
  focused regression RED on S, then correct to GREEN, run the full product suite, commit R with S
  as parent, and request a fresh full Change Review of exact R. Request
  `gpt-5.6-sol/medium` for `correction-writer` and `gpt-5.6-sol/high` for
  `R-change-reviewer`. This sequence provides E14 evidence only if ordering, branch continuity,
  role separation, and exact inputs are retained.

- [ ] **Step 3.6: Create E12's stale-PASS event authentically.**

  After PASS(R), deliver the new identity-bound whitespace requirement, add its RED test and
  minimum change, and commit B with R as parent. Record that PASS(R) does not cover B; keep merge
  blocked; request `gpt-5.6-sol/medium` for `whitespace-writer` and a fresh full Change Review from
  `B-change-reviewer` requested as `gpt-5.6-sol/high`. The E12 executor receives the identities,
  not the expected stale-review answer.

- [ ] **Step 3.7: Preserve final product behavior and tests.**

  The exact reviewed B tree must satisfy all 15 public product tests. Compare its final
  `quietfollow.py` and `test_quietfollow.py` byte hashes with the two tracked product files. A byte
  mismatch is a review finding: either correct the disposable candidate without changing required
  behavior or escalate a product-scope change. Do not alter tracked product bytes in this recovery.

- [ ] **Step 3.8: Merge and prove local ancestry/tree identity.**

  Let A be pre-merge main and merge only reviewed B with `git merge --no-ff B` to disposable
  `main`, producing M. Require `C^=A`, `S^=C`, `R^=S`, `B^=R`, `M^1=A`, `M^2=B`, and
  `M^{tree}=B^{tree}`. Capture exact stdout/stderr/exit and results for:

  ```bash
  git rev-parse C^ S^ R^ B^ M^1 M^2 M^{tree} B^{tree}
  git merge-base --is-ancestor A M
  git merge-base --is-ancestor B M
  git diff --binary --full-index A..B
  git diff-tree -r --no-commit-id --binary --full-index M^1 M
  git diff-tree -r --no-commit-id --binary --full-index M^2 M
  git ls-tree -r M -- quietfollow.py test_quietfollow.py
  git cat-file -e A^{commit}
  git cat-file -e B^{commit}
  git cat-file -e M^{commit}
  git cat-file -e M^{tree}
  ```

  Record A/C/S/R/B/M commit and tree IDs plus the two file blob IDs. Require the first-parent merge
  diff to equal the exact A..B binary diff, the second-parent merge diff to be empty, both ancestor
  commands to exit zero, and every named commit/tree/blob to resolve via `git cat-file -e`. Run
  15/15 product tests at exact M.

- [ ] **Step 3.9: Rerun E13 on an exact stale-FINAL sequence.**

  Create an immutable local FINAL-like review record bound to reviewed pre-merge A, then present
  exact current merged M and tree to fresh `E13-executor`, requested `gpt-5.6-sol/high`. Its bundle,
  prompt, output, result record, operations, and receipt are E13-only. It decides without an expected
  answer; distinct `E13-evaluator`, requested `gpt-5.6-sol/high`, checks refusal/closure behavior
  and binds its verdict to new A/M identities. This is a local rehearsal record, never Module FINAL.

- [ ] **Step 3.10: Rerun E27/E28 on the exact reviewed merged tree.**

  Dispatch fresh `E27-executor` and `E28-executor` as two distinct `gpt-5.6-sol/high` sessions with
  separate E27/E28 bundles, prompts, outputs, result records, operations, and receipts. E27 inspects
  rollout/readiness facts for exact M. E28 copies a synthetic store, runs the smoke path, restores
  the copy, and verifies byte-identical reload at exact M. Record manual accessibility and manual
  backup/restore as actually observed (`PENDING`/`Unknown` when not performed). Distinct
  `E27-evaluator` and `E28-evaluator`, both requested `gpt-5.6-sol/high`, must not convert green
  automation into release readiness or label the rehearsal production.

- [ ] **Step 3.11: Independently evaluate all five cases and review the group.**

  First dispatch five distinct case executors: E12 routing, E13 closure, E14 review/correction
  coordination, E27 readiness, and E28 rollback rehearsal. Each is requested
  `gpt-5.6-sol/high`, has its own complete per-attempt artifacts, and receives no evaluator rubric
  or seed oracle. Then use five distinct case evaluators, also requested `gpt-5.6-sol/high`; none
  evaluates its own output and E13/E27/E28 do not share a session. `delivery-recorder` alone
  materializes returned payloads. A fresh group reviewer verifies Git ancestry, trees/blobs, review
  independence, no leaked oracle, all transcript operations, stale-review invalidation,
  rollout/rollback, and actual verdicts. Store
  `reports/delivery-release-review-v1.json`.

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
  separate dependent state for correctly paused actions. `resume-recorder` alone materializes the
  returned evaluator payload.

- [ ] **Step 4.4: Review the group.**

  A fresh reviewer resolves all raw digests, confirms unchanged legacy/tracked inputs, checks that
  synthetic scale is not presented as live load, and verifies no forced reuse/rewrite or duplicate
  lifecycle work. Store `reports/resume-scaling-review-v1.json`.

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

  First a coordination executor returns one escalation/commission-routing response. Then a fresh
  `gpt-6-astra/high` architecture analyst receives only the bounded synthetic commission, affected
  contracts, preserved work, and source hashes. A distinct read-only `gpt-6-astra/high` architecture
  reviewer receives exact requirements and package, without analysis conversation. Only a review
  PASS permits the runner to create an identity-bound synthetic owner decision with sequence `1`
  and `no implementation authorization`; otherwise routing remains blocked. A final fresh routing
  executor receives only the reviewed package/decision and returns revised boundaries. Every role
  returns an immutable payload; `coordination-recorder` alone materializes it.

- [ ] **Step 5.4: Evaluate all seven cases independently.**

  Request `gpt-5.6-sol/high` for each behavioral evaluator. Preserve accepted/runtime assignment
  fields as `Unknown` absent receipts. Keep verdict and dependent permission/task/model state
  separate.

- [ ] **Step 5.5: Review the group.**

  A fresh read-only reviewer verifies one escalation, one bounded architecture decision when
  review passed, no full transcript relay, unaffected work preserved, no duplicate/native action,
  typed IDs, denial compliance, quiet unchanged wait, and model-fact separation. Store
  `reports/coordination-review-v1.json`.

**Commit guidance:** no Git commit; group files remain ignored and immutable after review.

## Task 6: Assemble and independently audit the retained execution evidence

**Files:** root manifest, versioned execution-evidence generations, digest/contamination checks, group
reports/reviews, and an ignored audit record. No tracked files.

**Interfaces:**

- Consumes: four stable reviewed group directories and product-repository evidence.
- Produces: one canonical current-attempt selection for all 21 cases, append-only content-addressed
  execution generation, and independent archive-audit verdict.

**Allowed effects:** sole-writer root manifest/check/report updates.

**Forbidden effects:** editing group attempt bytes, changing verdicts, running a case again,
tracked/public writes, and cleanup.

- [ ] **Step 6.1: Validate every group independently before aggregation.**

  Run the archive validator separately on each group manifest. Confirm exact case partition with
  no overlap or omission and exactly one current attempt per case. A group-review finding remains
  open; aggregation does not waive it.

- [ ] **Step 6.2: Build the root manifest and freeze generation v1.**

  Independently enumerate every actual regular file and require exact equality with root artifacts.
  Include every case attempt artifact, product Git record and Change Review needed by a public
  claim, and all four group manifests/reports/reviews. Generate the root sidecar. Write
  `checks/execution-evidence-manifest-v1.json` from the exact schema above, write its sidecar, make
  both read-only, and never mutate, rename, or delete them. The generation excludes itself, its
  sidecar, its future audit, its mutable selection pointer, and later Module review records.

- [ ] **Step 6.3: Validate generation v1 mechanically.**

  Run the validator against v1 and the actual filesystem. It must independently derive the exact
  21 current attempts, required categories, product-review and four group-review membership, and
  recompute all bytes/digests; no declared count is accepted as proof. Any error blocks audit.

- [ ] **Step 6.4: Re-run contamination checks across all current executor bundles.**

  Scan both paths and exact bytes against the denyset. Record per-case results and one aggregate
  zero-match result. An executor bundle match makes that attempt non-credit; return only that case
  to a new attempt and repeat its independent evaluation/review.

- [ ] **Step 6.5: Audit and select only an audited append-only generation.**

  A fresh `archive-auditor`, requested `gpt-5.6-sol/high`, receives v1, its sidecar, actual retained
  bytes, fixed schemas, group reviews, and product Git evidence. It enumerates independently,
  recomputes all joins/digests/current attempts, and returns
  `execution-evidence-audit-v1.json`; `root-manifest-writer` materializes that separate output. The
  audit neither hashes itself nor enters v1. On audit PASS, write
  `execution-evidence-current.json` selecting v1 and exact manifest/audit digests. On any case,
  product, group, contamination, or audit correction, preserve v1 byte-for-byte, create v2 including
  all old and successor records, obtain new independent `execution-evidence-audit-v2.json`, and
  select v2 only after PASS; repeat by consecutive integer generation. Public assembly consumes
  only the latest selected generation. Audit and pointer remain separate retained outputs.

**Commit guidance:** no Git commit; the selected append-only generation identity is the public evidence
source for Task 7.

## Task 7: Write public evidence regressions RED, assemble the successor candidate, then GREEN

**Files:** exactly the eleven tracked recovery candidate paths.

**Interfaces:**

- Consumes: clean archive-audit verdict, selected execution generation/hash, all actual current case
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
  - local/synthetic/rehearsal boundaries and no Task 10/FINAL/release claim are present;
  - both public records have exactly the schema-v2 keys/types/enums above, public-current refs join
    by stable logical ID/digest, and verdict/resolution totals are recomputed; and
  - permanent test source contains no ignored recovery-root dependency and passes in a clean
    tracked-only export.

- [ ] **Step 7.2: Run focused tests RED before changing public records.**

  Run:

  ```bash
  python3 -B -m unittest tests.test_pilot_evidence -v
  ```

  Expected: the new assertions fail against schema v1/predecessor evidence, including README's
  missing membership in `PUBLIC_EVIDENCE`.

- [ ] **Step 7.3: Assemble public machine-readable records from retained bytes only.**

  Update public `manifest.json` and `execution-record.json` to exact successor schema v2. For each
  case copy the actual current verdict, dependent state, findings, rerun history, requested/
  accepted/runtime facts, and public-safe digests. Add a `superseded_predecessor_evidence` section
  explaining that old raw artifacts vanished and receive no current credit. Bind private evidence
  by stable logical ID and selected generation digest without a private path; bind tracked evidence
  through `tracked_bindings`. Recompute totals from cases/references, not manifest counts.

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
  paths for exact nonempty byte matches. Reject the exact UTF-8 substrings `/Users/`, `/private/`,
  `/tmp/`, and `/var/`; regexes `[A-Za-z]:[\\\\/]`, `\\\\\\\\[^\\\\]+[\\\\]`,
  `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}`,
  and `(?:thread|task|client|agent|host)[_-]?[A-Za-z0-9]{8,}`; and JSON keys
  `absolute_path`, `archive_root`, `worktree_path`, `task_id`, `thread_id`, `client_thread_id`,
  `agent_id`, `host_id`, `session_id`, `private_url`, `credential`, and `token`. The scanner parses
  JSON keys structurally and scans all other exact bytes as UTF-8 with decoding errors reported.
  Store publicly only policy version, denylist value count/digest, zero exact/pattern match
  counts, and the final-receipt scope. Never store the scan artifact path or digest in the public
  byte set it scans. Preserve this pre-commit result as ignored
  `checks/redaction-scan-precommit-v1.json`.

- [ ] **Step 7.6: Run focused tests GREEN and verify source bindings.**

  Run focused evidence tests, both JSON parsers, the archive validator, and tracked-product versus
  reviewed-product byte comparisons. Create a tracked-only export with `git archive`, apply the
  candidate diff inside it, and run permanent evidence tests there with no ignored archive present.
  Expected: focused tests PASS in both locations; JSON parses; selected execution generation is
  valid; tracked product files remain unchanged.

- [ ] **Step 7.7: Self-review public assembly before commit.**

  Verify all prose/table totals derive from JSON; every public digest resolves; every prior current
  identity is explicitly superseded; no PASS was forced; no private content leaked; and exact
  changed paths are a subset of the eleven-path allowlist. Store
  `reports/public-assembly-report-v1.md` and regenerate the root archive manifest/sidecar. A later
  assembly correction writes the next sequence instead of overwriting it.

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

  Parse every tracked/ignored JSON record. Run the non-tautological resolver from the 21 actual
  public-current case references through the selected generation and actual filesystem bytes;
  require independently derived 100% resolution for every required kind with zero missing,
  duplicate, or mismatch. Rerun archive and contamination checks. Hash each of the eleven exact
  committed public blobs into ignored `checks/public-content-hashes-<head>.json`, binding exact
  candidate head/tree and per-file path/hash. Scan exactly those bytes using the exact denylist and
  portable patterns, then write ignored `checks/redaction-scan-<head>.json` with schema/policy,
  candidate head/tree, public-content-hash-record digest, scanned path/hash set, denylist digest,
  counts, matches, and verdict. The scan does not scan/hash itself and no public file cites it.
  Any candidate byte change requires a new commit, new content-hash record, new scan, all checks,
  and fresh review. Compare predecessor plan, active skill, checker, rubric, Module 5 inputs,
  baseline, product public bytes, and forbidden paths against accepted identities.

- [ ] **Step 8.3: Verify exact diff and changed-path allowlists.**

  Check three distinct scopes:

  - initial plan commit versus `b0e0c85dd0bf50e84ba1ce14ed4a985be7676002`, and corrected plan
    commit versus `21c1509dce231069e1ec49dd36d751ff85999e08`: exactly the one addendum path each;
  - recovery candidate commit versus accepted addendum commit: only actually changed paths from
    the eleven-path candidate allowlist;
  - full Module 6 candidate versus `f47263ce545c5185b3ec836c95fe341d1b3e5715`: predecessor
    13-path candidate plus this addendum
    and only justified successor changes, with product files unchanged by recovery.

  Confirm no ignored/private file is tracked and no plan artifact changed after acceptance.

- [ ] **Step 8.4: Verify disposable Git authenticity.**

  Independently resolve every named commit/tree/blob, parent edge, branch base, review head, stale
  review relation, merge ancestor, and final source/test blob. Re-run all Step 3.8 commands using
  exact captured SHA values and require C→S→R→B first-parent edges, M parents A/B, M tree equal B
  tree, first-parent merge diff equal A..B, empty second-parent diff, two successful ancestor
  checks, resolvable objects, and tracked/public product blob equality. Store commands/results under
  `checks/product-git-verification.json`.

- [ ] **Step 8.5: Attempt quick validation without installing dependencies.**

  Run the existing bundled `quick_validate.py` once. If PyYAML is absent, record the exact import
  failure and limitation. Do not alter environment or success criteria.

- [ ] **Step 8.6: Write the pre-review Task 9 report.**

  Record exact candidate head/tree/parent, plan/addendum identities, selected execution-generation
  identity, selected generation/audit identity, new public digests, independently derived 100%
  resolution counts, tests/checker/baseline/product/Git results, allowlists, exact-head redaction
  receipt, limitations, and retained workspace pointer. State
  `READY_FOR_CHANGE_REVIEW`, not `READY_FOR_INTEGRATION` or `DONE`.

**Commit guidance:** no commit. If any verification requires a tracked correction, return to Task 7,
create a new successor commit, and rerun all Task 8 checks.

## Task 9: Exact-head Module Change Review and bounded recommendation

**Files:** ignored review package, `reports/module-change-review-<candidate-head>.json`, and
`reports/task9-recommendation-<candidate-head>.md`. Candidate bytes remain read-only during review.

**Interfaces:**

- Consumes: exact stable candidate head, complete requirements, public candidate diff, all check
  evidence, selected append-only execution generation, group reviews, and product Git history.
- Produces: exact-head Change Review verdict and, only when clean, the local
  `READY_FOR_INTEGRATION` recommendation.

**Allowed effects:** read-only review and ignored review/report writes.

**Forbidden effects:** candidate edits by reviewer, author conversation in reviewer context,
Task 10, FINAL, push, PR, integration, merge, publication, install, deployment, release, and cleanup.

- [ ] **Step 9.1: Build the independent review package.**

  Include `AGENTS.md`, README/SPEC/AUDIT/EVALUATION/status/validation, both exact plan files,
  reviewer rubric, current public evidence/tests, exact candidate base/head/tree and full diff,
  verification outputs, selected generation plus its separate audit, raw current/superseded
  attempts, group reviews, exact-head redaction check, and disposable Git repository. Exclude
  author/assembler/Implementation
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
  digest, selected execution-generation digest, actual PASS/FAIL/BLOCKED totals, first unmet gate,
  limitations, and retained workspace. If the review is not clean, remain
  `READY_FOR_CHANGE_REVIEW` only after a corrected successor is again fully verified; otherwise
  report the actual blocking finding.

- [ ] **Step 9.5: Preserve evidence after finishing.**

  Regenerate the root manifest and sidecar to include final review/recommendation records, make
  case artifacts and every generation read-only, verify their digests once more, and leave the
  entire ignored recovery directory in place for the later Task 10 decision. A clean Module review
  and Task 9 recommendation are late retained consumers: public records make no digest claim about
  them, so they enter only the root inventory and do not mutate or force a successor selected
  generation. If review causes any case/product/group/public evidence correction, create the next
  generation, fresh audit, successor candidate commit/redaction receipt/checks, and fresh review.

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
   file changed in correction-round commit with sole parent
   `21c1509dce231069e1ec49dd36d751ff85999e08`; the initial addendum commit remains the only file
   changed over `b0e0c85dd0bf50e84ba1ce14ed4a985be7676002`.
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
8. The latest independently audited append-only execution generation resolves 100% of current raw
   inputs, executor outputs, evaluator inputs/outputs, transcripts, and product review artifacts
   with zero missing or mismatched bytes; all earlier generations remain retained and immutable.
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

`PLAN_PASS` requires no unresolved Critical or Important finding and binds exact corrected-addendum
bytes, containing commit, parent `21c1509dce231069e1ec49dd36d751ff85999e08`, initial addendum
commit/parent, and predecessor plan hash. Any later addendum correction creates a new plan-only
commit and requires a fresh complete PLAN review. Acceptance authorizes execution only through the
Task 9 bounded recommendation described here.
