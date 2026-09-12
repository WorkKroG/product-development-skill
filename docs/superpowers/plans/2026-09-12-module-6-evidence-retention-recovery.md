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
  above. Correction round 1 is `8a9f04bcb2d15a1127dcbd1f354ab66accd2e5b6`, tree
  `7faf24e1f4fe32541ff4e03211a14472be259048`, with sole parent the initial addendum and only this
  addendum changed. Correction round 2 uses `8a9f04bcb2d15a1127dcbd1f354ab66accd2e5b6`
  as its sole parent and again changes only this addendum, producing
  `f40c37e8e2bed1309605b9b0e8f17046699fa6af`, tree
  `ca14a1714100e59e3263059be246fff0723bc6be`. Correction round 3 uses that commit as its sole
  parent and changes only this addendum, producing
  `fde1b8cfe14f526bdd6561ed4309df1975dddc77`, tree
  `b99447187f33848bb31affe108741336c679e316`. Correction round 4 uses that commit as its sole
  parent and changes only this addendum, producing
  `134b90585991ecfa253c3de028142acaea6c301c`, tree
  `f5ecf76ea9b3ae050d7c552ddf3207b58b747902`. Correction round 5 uses that commit as its sole
  parent and changes only this addendum, producing
  `169237b48c36870e9bc7a1defcb3d996958a72d2`, tree
  `fb64c07c1de17e1a60547412c92b336b3b837c63`. Correction round 6 uses that commit as its sole
  parent and changes only this addendum, producing
  `d3c0369ce38142832a7347c1ead1140945b2fedd`, tree
  `b9db5eb86425e5750abb9c0d713bcf592c36af72`. Correction round 7 uses that commit as its sole
  parent and changes only this addendum, producing
  `231638b69051ef52b46902c3d309a52d7852b803`, tree
  `8bc4b812c918b82a39f29fe1fafa9e3c4a38f0ed`. Correction round 8 uses that commit as its sole
  parent and changes only this addendum, producing
  `e5b2ef7af65c5c6381a70e7f0327d2fe8c338b3d`, tree
  `52e4a18c230ee1dab1f6f9817ae2f3047fef4153`. Correction round 9 uses that commit as its sole
  parent and changes only this addendum. The newest containing commit/hash are
  supplied by the plan-author report and exact PLAN-review package, never self-recorded here.
- The addendum identity remains `MODULE6-RECOVERY-PLAN-v1`; each correction supersedes the prior
  addendum bytes only for execution authority. A PLAN reviewer must bind the newest bytes and
  commit explicitly; prior bytes remain immutable Git history and confer no execution credit.
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
7. Superseded ignored `plan-review-v6.json` at SHA-256
   `fef6cb287773eba84099e7cf939519107f0181f7162983a3f5882198d00ac547` and
   `plan-review-v7.json` at SHA-256
   `7d234a640d4d51064a7d0c17485c5166189ab619cd7dc053eff9b6b9b1e65f6b` and
   `plan-review-v8.json` at SHA-256
   `07f37acba8160b362920989ebbfc3af4db2ff4caae7d3a48f6899602e431990b` and
   `plan-review-v9.json` at SHA-256
   `9034740d0111a9edf5b2b47a8e9cd6ca61b1f3082d49f3087381f4f402011c76`; Task 1 reports v1-v3 at
   SHA-256 `e72ad2c3d1dd61e103fc466b6d572bb3cf7c75ae40f817932bf46b987cd1cc1f`,
   `4e87495eca8153949b77648eb37c65a17c4a0ef4379b7442946fb8488c45c14c`, and
   `ce4310bccfab4db4d97182af1bb479c6dfdc6b4855ce84f72bd00e196c5a3ed0`; and schema reviews v1/v2
   at the exact hashes in the recovery-history table. These are historical incident inputs, not
   authority to infer missing candidate bytes, adopt a mutable dependency named inside a review,
   or bypass current joins.
8. Mutable `progress.md` is live coordination context only. Before its next append or mutation,
   Task 1.1 must copy its current 18,640 bytes at exact SHA-256
   `5e50255f613334839560b676c2bf2dbe7a9fe05a2f01bbd135842385d2e22f2b` to the immutable history
   snapshot defined below. Every permanent historical consumer binds that snapshot, never the
   later mutable path.

Fresh Git identities, retained raw bytes, and current independent reviews take precedence over
earlier summaries. Any tracked correction after review creates a successor commit and requires a
fresh complete review of the new exact head.

## Global Constraints

- Execute on an isolated `codex/` branch/worktree rooted at the accepted corrected-addendum commit.
  Before any recovery write, verify that the newest corrected plan commit has sole parent
  `e5b2ef7af65c5c6381a70e7f0327d2fe8c338b3d`, that correction round 8 has sole parent
  `231638b69051ef52b46902c3d309a52d7852b803`, that correction round 7 has sole parent
  `d3c0369ce38142832a7347c1ead1140945b2fedd`, that correction round 6 has sole parent
  `169237b48c36870e9bc7a1defcb3d996958a72d2`, that correction round 5 has sole parent
  `134b90585991ecfa253c3de028142acaea6c301c`, that correction round 4 has sole parent
  `fde1b8cfe14f526bdd6561ed4309df1975dddc77`, that correction round 3 has sole parent
  `f40c37e8e2bed1309605b9b0e8f17046699fa6af`, that correction round 2 has sole parent
  `8a9f04bcb2d15a1127dcbd1f354ab66accd2e5b6`, that correction round 1 has sole parent
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
- Preserve exact schema-review v1/v2 bytes and findings as pre-freeze rejected history. Their only
  join exception is the exact path/digest/JSON-pointer tuple enumerated by the recovery-history
  schema below. It does not apply to another byte, ref, verdict, path, or future review. Missing
  candidate bytes are never reconstructed, and quarantined history never authorizes dispatch or a
  public evidence claim.
- Treat `progress.md` as a mutable append-only live ledger, not permanent exact evidence. Freeze
  its mandatory current bytes at the exact immutable v1 path before any next append; exclude the
  mutable path from every immutable inventory snapshot/generation, and bind only immutable ledger
  snapshots from recovery history or a review. Any append makes the live root manifest stale until
  the root writer regenerates it; no consumer review may run while it is stale.
- Executor and evaluator are distinct roles. A case executor receives no rubric verdict, expected
  outcome, observable PASS/FAIL text, evaluator notes, prior verdict, or author conversation.
  Evaluators receive the exact isolated case-rubric artifact, input bundle manifest, raw output,
  immutable executor-operation snapshot, and immutable executor-session snapshot,
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
- Correction round 2 modifies only that same addendum over sole parent
  `8a9f04bcb2d15a1127dcbd1f354ab66accd2e5b6`; its subject is
  `docs: complete Module 6 evidence schemas`.
- Correction round 3 modifies only that same addendum over sole parent
  `f40c37e8e2bed1309605b9b0e8f17046699fa6af`; its subject is
  `docs: make Module 6 evidence lifecycle reproducible`.
- Correction round 4 modifies only that same addendum over sole parent
  `fde1b8cfe14f526bdd6561ed4309df1975dddc77`; its subject is
  `docs: close Module 6 evidence reference gaps`.
- Correction round 5 modifies only that same addendum over sole parent
  `134b90585991ecfa253c3de028142acaea6c301c`; its subject is
  `docs: make SHA prefix discovery exhaustive`.
- Correction round 6 modifies only that same addendum over sole parent
  `169237b48c36870e9bc7a1defcb3d996958a72d2`; its subject is
  `docs: define schema review recovery contract`.
- Correction round 7 modifies only that same addendum over sole parent
  `d3c0369ce38142832a7347c1ead1140945b2fedd`; its subject is
  `docs: preserve recovery progress history`.
- Correction round 8 modifies only that same addendum over sole parent
  `231638b69051ef52b46902c3d309a52d7852b803`; its subject is
  `docs: correct binding recovery history`.
- Correction round 9 modifies only that same addendum over sole parent
  `e5b2ef7af65c5c6381a70e7f0327d2fe8c338b3d`; its subject is
  `docs: sequence Module 6 binding validation`.
- Exact changed-path allowlist for every plan-history commit is the one path above. No
  recovery-candidate path belongs in a plan-history commit, and no plan path belongs in a candidate
  commit.

### Durable ignored recovery workspace

All paths below live under
`.superpowers/sdd/2026-09-12-module-6-evidence-retention-recovery/` and remain ignored/private:

```text
manifest.json
manifest.sha256
progress.md
history/progress-ledger-snapshot-v<N>.md
task1-brief.md
task1-implementer-report-v<N>.md
plan-author-report*.md
plan-review-v<N>.json
inputs/binding/
inputs/binding/schema/recovery-plan.md
inputs/binding/group-briefs/<group>.json
inputs/binding/schema/recovery-plan-v<N>.md
inputs/binding/binding-snapshot-manifest-v<N>.json
inputs/binding/group-briefs-v<N>/<group>.json
inputs/<group>/<EID>/<attempt-id>/
executions/<group>/<EID>/<attempt-id>/
evaluations/<group>/<EID>/<attempt-id>/
transcripts/<group>/<EID>/<attempt-id>/
evaluations/<group>/<EID>/<attempt-id>/rubric-section.md
transcripts/<group>/<EID>/<attempt-id>/executor-operations.jsonl
transcripts/<group>/<EID>/<attempt-id>/executor-session-receipt.json
transcripts/roles/<role-alias>/<session-alias>/native-receipt.txt
transcripts/metrics/coordination-observation.jsonl
product-repo/repository/
product-repo/reviews/
product-repo/rehearsals/
product-repo/command-streams/<record-id>/<sequence>.stdout
product-repo/command-streams/<record-id>/<sequence>.stderr
checks/archive-validator.py
checks/archive-validator-tests.py
checks/build-live-manifest.py
checks/archive-validator-red-v1.txt
checks/archive-validator-correction-red-v<N>.txt
checks/root-inventory-snapshot-v<N>.json
checks/root-inventory-snapshot-v<N>.sha256
checks/execution-evidence-manifest-v<N>.json
checks/execution-evidence-manifest-v<N>.sha256
checks/execution-evidence-audit-v<N>.json
checks/execution-evidence-current.json
checks/digest-resolution-v<N>.json
checks/bundle-contamination.json
checks/bundle-contamination-scan-v<N>.json
checks/private-denylist-v<N>.txt
checks/private-denylist-v<N>.sha256
checks/public-alias-vocabulary.txt
checks/public-alias-vocabulary.sha256
checks/prebound-public-sessions-v<N>.json
checks/prebound-public-session-receipts/<session-alias>.txt
checks/public-content-hashes-precommit-v<N>.json
checks/redaction-scan-precommit-v<N>.json
checks/public-content-hashes-<candidate-head>.json
checks/redaction-scan-<candidate-head>.json
checks/product-git-verification.json
checks/product-git-verification-<candidate-head>.json
checks/task1-schema-review-recovery-history-v1.json
review-targets/task1-schema-review-v2-forensic/archive-validator.py
review-targets/task1-schema-review-v2-forensic/archive-validator-tests.py
review-targets/task1-schema-review-v2-forensic/build-live-manifest.py
review-targets/task1-schema-review-v<N>/recovery-plan.md
review-targets/task1-schema-review-v<N>/archive-validator.py
review-targets/task1-schema-review-v<N>/archive-validator-tests.py
review-targets/task1-schema-review-v<N>/build-live-manifest.py
review-targets/task1-schema-review-v<N>/bundle-contamination.json
review-targets/task1-schema-review-v<N>/binding-snapshot-manifest.json
review-targets/task1-schema-review-v<N>/public-alias-vocabulary.txt
reports/<group>-report-v<N>.md
reports/<group>-manifest-v<N>.json
reports/<group>-review-v<N>.json
reports/task1-schema-review-v<N>.json
reports/public-assembly-report-v<N>.md
reports/module-change-review-<candidate-head>.json
reports/task9-report-<candidate-head>.md
reports/task9-recommendation-<candidate-head>.md
```

The root `manifest.json` is a mutable live inventory regenerated atomically only by the designated
root writer. It lists every then-existing retained regular file except `manifest.json` and
`manifest.sha256`; its sidecar hashes only those current live-manifest bytes. No immutable artifact
cites the mutable manifest or sidecar. For each execution generation N, first close the evidence
scope and freeze immutable `checks/root-inventory-snapshot-v<N>.json` plus sidecar, then create the
append-only generation from that snapshot, audit the immutable pair, select it in the pointer, and
only then regenerate the live root manifest so it includes snapshot, generation, audit, and pointer.
A correction creates a new snapshot/generation/audit sequence without changing any old bytes. The
live root manifest is also regenerated and exact-inventory-validated after each Task 7, Task 8, and
Task 9 late-record batch and immediately before its next consumer review. Public files bind the
selected generation number/digest, never an ignored path or mutable-root digest.
For report and compliant review-target paths, `N` is that group's or schema review's positive
monotonic sequence; review-target N is closed before schema-review report N is dispatched, and
prior target/report bytes are never overwritten. Compliant schema-review targets begin at N=3;
the literal `task1-schema-review-v2-forensic` directory is a non-credit preservation copy and never
an accepted review target. For the three versioned `inputs/binding/**-v<N>` path patterns, N may be
3 or greater but never 2; the listed patterns do not authorize a sequence-2 file. `<candidate-head>`
is replaced with the exact lowercase 40-hex commit
already created before that ignored report, so it is not a tracked self-reference. `<group>` is one
of the four exact group IDs, `<EID>` is its assigned selected case, and `<attempt-id>` is the
case-derived `EID-r<positive integer>`. `<role-alias>` is an exact ownership-table alias and
`<session-alias>` is the retained globally unique private session alias; angle brackets are notation
only and never literal path bytes.

`history/progress-ledger-snapshot-v1.md` is the mandatory byte-exact pre-append copy of the current
`progress.md`: exactly 18,640 bytes, SHA-256
`5e50255f613334839560b676c2bf2dbe7a9fe05a2f01bbd135842385d2e22f2b`, regular file mode `0444`.
Its root artifact has logical ID `progress-ledger-snapshot-v1`, kind `raw_input`, producer
`root-manifest-writer`, credit state `non-credit`, sensitivity `private`, content type
`text/markdown`, `empty_allowed=false`, and `validation_state=valid`. The mutable `progress.md`
root artifact instead has logical ID `progress-live-ledger`, kind `raw_input`, producer
`task-coordinator`, credit state `non-credit`, and its then-current size/digest; it appears only in
the mutable live manifest and is never a selected-generation member or permanent exact target.
Before any future ledger version is cited as exact evidence and before the next append, the same
exclusive handoff creates `history/progress-ledger-snapshot-v<N>.md` with the next positive N,
logical ID `progress-ledger-snapshot-v<N>`, exact source/copy size and digest equality, and mode
`0444`. Old snapshots are never rewritten. A reviewer or recovery record cites the immutable
snapshot's `LogicalRef`; it never cites a digest of the mutable path. This raw snapshot contains no
manifest or recovery-history reference, so neither its creation nor later inventory membership can
form a digest cycle.

The unversioned `inputs/binding/schema/recovery-plan.md`,
`inputs/binding/binding-snapshot-manifest.json`, and `inputs/binding/group-briefs/<group>.json`
paths are immutable binding-set v1 history for the accepted pre-correction plan; they are never
overwritten. Binding sequence 2 is permanently reserved as `not-materialized`: correction-round-6
plan bytes never achieved `PLAN_PASS`, its future Step 1.6 never executed, and the filesystem has
none of `inputs/binding/schema/recovery-plan-v2.md`,
`inputs/binding/binding-snapshot-manifest-v2.json`, or the four
`inputs/binding/group-briefs-v2/<group>.json` files. Sequence 2 is non-artifact history only; it has
no `LogicalRef`, artifact logical ID, root-inventory entry, generation membership, dispatch credit,
or bytes to reconstruct. Those six reserved paths must remain absent forever.

After correction-round-9 `PLAN_PASS`, Step 1.6 creates binding set v3 directly from the verified
existing v1 copies plus the accepted current plan bytes at
`inputs/binding/schema/recovery-plan-v3.md`,
`inputs/binding/binding-snapshot-manifest-v3.json`, and
`inputs/binding/group-briefs-v3/<group>.json`. Their unique logical IDs are
`recovery-schema-source-v3`, `binding-snapshot-manifest-v3`, and
`inputs-binding-group-briefs-v3-<group>`. A later accepted tracked plan correction increments from
the latest materialized version and creates new paths; it never fills reserved sequence 2. In root
inventory, the materialized v1 schema source, snapshot, and four briefs are kind `raw_input`,
producer `schema-binding-writer`, and credit state `superseded`; the active v3 counterparts are the
same kind/producer with credit state `shared` only after Step 1.6 creates and validates them. No
path/ID for sequence 2 is classified because no
such artifact exists. A later binding set changes the formerly active materialized set to
`superseded` and uses new V-specific IDs; no two actual retained artifacts share a logical ID.

The existing/planned directory `review-targets/task1-schema-review-v2-forensic/` is unrelated to
binding sequence 2. It retains the separately defined validator/test/builder bytes from rejected
schema review v2 under forensic IDs; its name never proves or creates a binding-set-v2 artifact.

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
| `manifest_sequence` | positive integer, incremented on every atomic live-root regeneration |
| `as_of_phase` | one of `initial-schema`, `task1-history-recovered`, `pre-schema-review`, `post-schema-review`, `post-generation-selection`, `post-public-assembly`, `post-exact-head-verification`, `pre-module-review`, `post-module-review` |
| `predecessor` | object with exactly `candidate_head`, `candidate_tree`, `accepted_plan_identity`, `accepted_plan_sha256`, `accepted_plan_commit`, `implementation_base`, all nonempty strings and SHA fields lowercase 40/64 hex as applicable |
| `inventory_exclusions` | array exactly `['manifest.json', 'manifest.sha256']` in that order |
| `artifacts` | array of artifact records defined below |
| `cases` | array of case records defined below |
| `groups` | array of group records defined below |
| `retention` | object with exactly `authoritative_root='recovery-worktree-relative'`, `retain_through='Task 10 decision'`, `cleanup_authorized=false`, `publication_scope=false` |
| `limitations` | array of nonempty strings |

`as_of_phase=task1-history-recovered` has one exact lifecycle meaning: the immutable progress
snapshot, recovery-history record, v2 forensic copies, corrected five fixed working candidates,
complete binding sets v1 and v3, and the absent/non-artifact sequence-2 state all exist; the
schema-binding writer has closed and relinquished them; the root writer has regenerated the actual
live manifest from those bytes; and the full always-invoked archive validator has returned zero
errors on that actual root. It is never a pre-v3 phase, a synthetic-fixture phase, or a validation
bypass. Between the Step 1.1 history/forensic write and this post-v3 PASS, the actual live manifest
is explicitly stale and non-authoritative: no consumer review, case/group/product dispatch,
generation freeze, or current-inventory claim is permitted. The complete physical synthetic CLI
fixture is the only validator target in Step 1.5; it proves the full contract before the actual v3
bytes exist but does not promote the live archive. After this phase is recorded, any mutation makes
the live manifest stale again until its next prescribed regeneration and full validation.

Each artifact record has exactly these keys:

| Key | Type and invariant |
|---|---|
| `logical_id` | unique nonempty string matching `^[A-Za-z0-9][A-Za-z0-9._-]*$` |
| `case_id` | one selected E-case string for case evidence; JSON `null` for shared/product/group/check/review evidence |
| `attempt_id` | `<case_id>-r<sequence>` for case evidence; JSON `null` otherwise |
| `kind` | one of `raw_input`, `executor_prompt`, `bundle_manifest`, `executor_output`, `result_record`, `executor_operation_snapshot`, `executor_session_snapshot`, `rubric_section`, `evaluator_input`, `evaluator_prompt`, `evaluator_output`, `transcript`, `session_receipt`, `product_git`, `check`, `report`, `review`, `recovery_history` |
| `relative_path` | unique canonical POSIX path relative to recovery root |
| `sha256` | lowercase 64-hex digest of exact file bytes |
| `byte_count` | nonnegative integer equal to actual file size |
| `content_type` | one of `application/json`, `application/jsonl`, `text/markdown`, `text/plain`, `application/octet-stream` |
| `producer_alias` | nonempty role alias present in the role/ownership table |
| `credit_state` | one of `current`, `superseded`, `non-credit`, `shared` |
| `sensitivity` | one of `private`, `public-source` |
| `empty_allowed` | boolean; `true` only for a `ProductGitRecord` stdout/stderr stream that actually contains zero bytes; false everywhere else |
| `validation_state` | one of `valid`, `malformed`, or `corrupt`; every current/superseded credit artifact is `valid` |
| `validation_error` | JSON null iff state is `valid`; otherwise a nonempty exact observed parse/digest/structure error |

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

### Immutable root-inventory snapshots

`checks/root-inventory-snapshot-v<N>.json` has exactly `{schema_version, snapshot_sequence,
recovery_plan, scope_closed_sequence, inventory_exclusions, artifacts, cases, groups}`. Version is
integer `1`; snapshot sequence is N; plan identity is `MODULE6-RECOVERY-PLAN-v1`; close sequence is
positive; artifacts/cases/groups use the exact root schemas. Its exclusions are exactly these nine
paths in this order, with N substituted:

```text
manifest.json
manifest.sha256
progress.md
checks/execution-evidence-current.json
checks/root-inventory-snapshot-v<N>.json
checks/root-inventory-snapshot-v<N>.sha256
checks/execution-evidence-manifest-v<N>.json
checks/execution-evidence-manifest-v<N>.sha256
checks/execution-evidence-audit-v<N>.json
```

At scope close, independently enumerate all then-existing regular files. The snapshot artifact set
must equal that actual set minus exactly those exclusions; exclusions may name not-yet-created
snapshot/generation/audit files and the mutable pointer. Reject every other missing, extra,
duplicate, symlink, special, or escaped path. Atomically write the snapshot and its sidecar, mark
both read-only, and never modify them. Before the audit output exists, the auditor recomputes this
equality from current bytes after removing the same nine paths; therefore no unlisted pre-freeze
file can be hidden. The later audit output, pointer replacement, and live-manifest regeneration are
outside snapshot N by construction. No snapshot contains its own digest, generation, or audit.
The mutable live ledger is excluded because it may change after the mandatory immutable
`history/progress-ledger-snapshot-v1.md` closes; every immutable progress snapshot that exists at
scope close is an ordinary included artifact and may not appear in this exclusion list.

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

Each `attempts[]` record has exactly `attempt_id`, `sequence`, `credit_state`, `terminal_phase`,
`terminal_reason`, `supersedes`, `correction_reason`, and `logical_ids`. `sequence` is a positive integer; `attempt_id` equals
`<case_id>-r<sequence>`; sequences are strictly increasing without duplicates. `credit_state` is
`current`, `superseded`, or `non-credit`; exactly one attempt is `current`, and it equals
`current_attempt_id`. Terminal phase is `pre-dispatch`, `executor-running`, `executor-closed`,
`evaluator-prepared`, `evaluator-running`, or `evaluator-closed`. Terminal reason is `complete`,
`pre-dispatch-contamination`, `pre-evaluation-contamination`, `interrupted`, `malformed-artifact`, `corrupt-artifact`, or
`prohibited-effect`. Current/superseded credit requires phase `evaluator-closed`, reason `complete`,
a valid evaluator verdict, and only `valid` artifacts. `non-credit` requires a non-`complete`
reason and may end at any phase. The first attempt has `supersedes=null` and
`correction_reason=null`; a later
attempt names the immediately prior attempt in `supersedes` and a nonempty observed correction
reason. Previous credit-bearing attempts become `superseded`; contaminated/malformed/incomplete
attempts remain `non-credit`. No case artifact can claim `current` unless its attempt is current;
a null-case global artifact may be `current` only when this plan explicitly selects its immutable
version for public-private resolution.

Both attempt `logical_ids` and case `current_logical_ids` have exactly:

```json
{
  "raw_inputs": [],
  "executor_prompts": [],
  "bundle_manifests": [],
  "executor_outputs": [],
  "result_records": [],
  "executor_operation_snapshots": [],
  "executor_session_snapshots": [],
  "rubric_sections": [],
  "evaluator_inputs": [],
  "evaluator_prompts": [],
  "evaluator_outputs": [],
  "transcripts": [],
  "session_receipts": []
}
```

For every attempt, the union of all thirteen arrays equals exactly every actual case-attempt artifact in
the root inventory and selected generation; no logical ID or existing byte may be omitted, and no
missing file may be declared or fabricated. Current/superseded attempts have every array nonempty.
For non-credit attempts, `R` below means nonempty and valid except that the artifact named by a
`malformed-artifact`/`corrupt-artifact` terminal reason may carry that matching validation state;
`O` means list the family iff one or more files actually exist, with no synthesized byte; `—` means
the array must be empty and no file of that family may exist:

| Terminal phase | raw inputs | executor prompt | bundle manifest | executor output | result record | evaluator input | evaluator prompt | evaluator output | final transcript | final session receipt |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `pre-dispatch` | R | R | R | — | — | — | — | — | R | — |
| `executor-running` | R | R | R | O | — | — | — | — | R | R |
| `executor-closed` | R | R | R | R | R | — | — | — | R | R |
| `evaluator-prepared` | R | R | R | R | R | R | R | — | R | R |
| `evaluator-running` | R | R | R | R | R | R | R | O | R | R |
| `evaluator-closed` | R | R | R | R | R | R | R | R | R | R |

The remaining three immutable evaluator-bound families follow this exact matrix:

| Terminal phase | executor operation snapshot | executor session snapshot | rubric section |
|---|---:|---:|---:|
| `pre-dispatch` | — | — | — |
| `executor-running` | — | — | — |
| `executor-closed` | R | R | — |
| `evaluator-prepared` | R | R | R |
| `evaluator-running` | R | R | R |
| `evaluator-closed` | R | R | R |

An attempt ID is opened only after the four `pre-dispatch` families exist durably; a failure before
that boundary is a shared preparation incident, not a case attempt. `pre-dispatch-contamination`
is valid only at `pre-dispatch`; `pre-evaluation-contamination` only at `evaluator-prepared` after
all of that phase's required bytes are retained but before evaluator dispatch; `prohibited-effect`
only after executor dispatch; interruption or
malformation/corruption may close the current phase. A `malformed` JSON/JSONL artifact is retained
and exempt only from its own inner schema parse, never from root path/size/current-byte digest
checks; the terminal error must name it. The validator derives phase-family coverage and actual
files independently. For the current attempt, `current_logical_ids` equals its complete
`logical_ids`. Executor and evaluator receipts identify distinct session aliases; requested,
accepted, and runtime roles join those receipts.

Each root `groups[]` record has exactly `group_id`, `case_ids`, `owned_roots`,
`group_manifest_logical_id`, `group_report_logical_id`, `group_review_logical_id`, and
`review_verdict`. `group_id` and `case_ids` equal the fixed partition; `owned_roots` equals the exact
paths in the group table; the three logical IDs resolve to distinct current/shared artifacts;
`review_verdict` equals the retained group-review bytes and is one of `PASS` or
`CHANGES_REQUIRED`.

### Normative JSON conventions and reusable records

Every valid recovery-produced `.json` file is UTF-8, ends with one LF, contains one JSON object, and is
serialized with sorted object keys and no duplicate keys. Every valid `.jsonl` file is UTF-8, ends with
one LF, and contains one compact JSON object per nonempty line. An "exact" key set rejects missing
and unknown keys. JSON booleans never satisfy an integer field. Every string is nonempty unless a
literal value or nullable rule is stated. `sha256` means lowercase 64-hex; `git_oid` means lowercase
40-hex; `logical_id` and `alias` match `^[A-Za-z0-9][A-Za-z0-9._-]*$`; `case_id` belongs to the
ordered 21-case set; `attempt_id` is exactly `<case_id>-r<positive integer>`; and every relative
path satisfies the root canonical-POSIX rules. Every `.sha256` sidecar has exactly the ASCII bytes
`<digest><two spaces><basename>\n`, where the lowercase digest recomputes the sibling named by the
basename; no absolute or parent path is permitted. Every plan-produced Markdown or text report is
nonempty UTF-8 ending in one LF, and its root artifact record supplies its exact digest/size.
An observed malformed/corrupt non-credit artifact is retained byte-for-byte and may violate only
its own format/schema rule; its root artifact record must carry the exact non-valid state/error,
and every path/digest/size/phase-membership rule still applies. It is never used as a producer input
or credited output.

These reusable records have exact keys:

| Record | Exact keys and rules |
|---|---|
| `AssignmentRequest` | `{role_alias, model, reasoning}`; model is `gpt-5.6-sol`, `gpt-5.6-terra`, or `gpt-6-astra`; reasoning is `medium` or `high`; pair equals the role table |
| `ObservedAssignment` | `{role_alias, value, receipt_logical_id}`; `value` is `Unknown` or a nonempty native assignment string; receipt is null iff value is `Unknown`, otherwise joins the current case or shared non-case `session_receipt` artifact |
| `RuntimeFact` | `{role_alias, value, receipt_logical_id}` with the same null/join rule; requested or self-reported values are not runtime proof |
| `LogicalRef` | `{logical_id, kind, sha256}`; kind is one root artifact-kind enum value and the ID/digest/kind join exactly one artifact |
| `PrivateFinding` | `{id, severity, state, requirement, observed, impact, evidence_logical_ids}`; severity is `Critical`, `Important`, or `Minor`; state is `open` or `resolved`; evidence IDs are a nonempty unique array joining retained artifacts |
| `StringEffectSet` | sorted unique array of nonempty strings; allowed and forbidden sets are disjoint |

No other shape may be called by one of these names.

For the three structural forward joins created before the live root manifest is refreshed—
generation-to-snapshot/sidecar, audit-to-generation/snapshot and both sidecars, and
pointer-to-generation/audit—the
context fixes the target to the version-matched canonical path. Validate the actual retained file
and digest immediately, then require the regenerated live root artifact record to expose the same
logical ID/kind/digest. Absence or disagreement at either check fails; this rule does not permit a
free-standing digest or any other deferred target.

### Exact per-attempt retained schemas

For every complete current/superseded attempt retain all thirteen paths below. A non-credit attempt
retains only the phase-conditional subset that actually exists under the same canonical locations:

```text
inputs/<group>/<EID>/<attempt-id>/source-manifest.json
inputs/<group>/<EID>/<attempt-id>/executor-bundle-manifest.json
inputs/<group>/<EID>/<attempt-id>/executor-prompt.txt
executions/<group>/<EID>/<attempt-id>/executor-output.txt
executions/<group>/<EID>/<attempt-id>/result-record.json
transcripts/<group>/<EID>/<attempt-id>/executor-operations.jsonl
transcripts/<group>/<EID>/<attempt-id>/executor-session-receipt.json
evaluations/<group>/<EID>/<attempt-id>/rubric-section.md
evaluations/<group>/<EID>/<attempt-id>/evaluator-input.json
evaluations/<group>/<EID>/<attempt-id>/evaluator-prompt.txt
evaluations/<group>/<EID>/<attempt-id>/evaluator-output.json
transcripts/<group>/<EID>/<attempt-id>/operations.jsonl
transcripts/<group>/<EID>/<attempt-id>/session-receipt.json
```

`source-manifest.json` has exactly:

| Key | Type and invariant |
|---|---|
| `schema_version` | integer `1` |
| `case_id`, `attempt_id`, `group_id` | exact case/attempt/group identity; group matches fixed partition |
| `bundle_root` | recovery-root-relative canonical directory exactly `inputs/<group>/<case>/<attempt>/bundle` |
| `harness_sources`, `case_inputs` | nonempty arrays of `SourceBinding`; logical IDs are unique across both |
| `permissions` | exact `PermissionBoundary` |
| `executor_assignment` | exact `AssignmentRequest` for the case executor |
| `created_sequence` | positive integer preceding executor dispatch |

`SourceBinding` has exactly `{logical_id, origin_class, origin_alias, sha256, byte_count,
bundle_relative_path}`. `origin_class` is `tracked-binding`, `retained-private`, or
`synthetic-fixture`; `origin_alias` is a stable alias, never a private path; byte count is a
nonnegative integer; bundle path is canonical relative to `bundle_root`. Each binding joins exactly
one listed bundle file with the same path/digest/size. `PermissionBoundary` has exactly `{mode,
allowed_effects, forbidden_effects}`; mode is `offline-simulation`, `local-synthetic-product`, or
`read-only-analysis`, and the two effect values are `StringEffectSet` records.

`executor-bundle-manifest.json` has exactly `{schema_version, case_id, attempt_id, bundle_root,
contamination_contract_ref, files}`. Version is integer `1`; identities/root equal the source
manifest; contamination ref is a `LogicalRef` with kind `check`, null case/attempt, and exact
logical-ID/digest join to `checks/bundle-contamination.json`; `files` is nonempty and
has exact set equality with independently enumerated regular files below `bundle_root`. Each file
record has exactly `{relative_path, kind, sha256, byte_count}`; kind is `harness-source`,
`case-input`, `authority-input`, or `product-fixture`; path is unique canonical bundle-relative;
digest/size equal actual bytes. No rubric, evaluator, plan, prior verdict, author conversation, or
unlisted file is allowed.

`result-record.json` has exactly:

| Key | Type and invariant |
|---|---|
| `schema_version` | integer `1` |
| `case_id`, `attempt_id`, `executor_alias` | exact same-attempt identities; alias equals a session-receipt executor alias |
| `bundle_manifest_logical_id`, `executor_output_logical_id`, `executor_operations_logical_id` | three distinct logical IDs joining the named same-attempt artifacts with that attempt's credit state; the operation ID is the immutable executor snapshot, not the later final transcript |
| `actual_outcome` | nonempty factual string; contains no verdict field or rubric judgment |
| `completion_state` | `completed`, `blocked`, or `interrupted` |
| `observed_effects` | array of exact `ObservedEffect` records ordered by sequence |
| `prohibited_effect_observed` | boolean equal to whether any effect has `authorization='forbidden-observed'` |
| `completed_sequence` | positive integer equal to the terminal executor operation sequence |

`ObservedEffect` has exactly `{sequence, effect_kind, authorization, target_alias, result}`.
Sequence is positive and strictly increasing; effect kind is `file-read`, `file-write`, `local-git`,
`local-test`, `local-tool`, `agent-dispatch`, or `none`; authorization is `allowed`,
`forbidden-blocked`, or `forbidden-observed`; target is a public/private stable alias, not an
absolute path/native ID; result is a nonempty observation.

At executor close, the recorder creates two immutable snapshots before any rubric/evaluator byte.
`executor-operations.jsonl` contains exactly the complete line prefix of final `operations.jsonl`
from sequence 1 through the single terminal executor operation; every line uses the operations
schema below, the last phase is `execution`, and its artifact kind is
`executor_operation_snapshot`. Its exact bytes, including the final LF, must be a byte prefix of
the final transcript; later evaluator/preparation lines may only append and may never change that
prefix. Its logical ID is `<attempt-id>-executor-operations`.

`executor-session-receipt.json` has exactly `{schema_version, case_id, attempt_id,
closed_sequence, sessions}`. Version is integer `1`; close sequence equals the terminal executor
operation; sessions is the nonempty ordered exact executor/analyst/reviewer session prefix known at
that boundary, using the same nested session record defined for the final receipt, and contains no
evaluator. Its logical ID is `<attempt-id>-executor-session-receipt` and artifact kind is
`executor_session_snapshot`. In final `session-receipt.json`, the first N session objects must be
deep-equal to this immutable array in the same order, with evaluator sessions appended only after
evaluator dispatch. Neither snapshot is rewritten after hashing. At `executor-closed` the final
transcript equals the operation snapshot; at later phases it has that exact prefix. The final
receipt's pre-evaluator session prefix always equals the session snapshot. Missing, changed, or
future-event-filled snapshots invalidate the attempt.

Only after both executor snapshots close does the recorder extract
`evaluations/<group>/<EID>/<attempt-id>/rubric-section.md`. From the byte-exact retained binding copy
of `tests/scenarios.md`, concatenate without normalization: (a) bytes from offset zero through the
byte immediately before the first line beginning `### E` followed by exactly two digits and ` — `;
then (b) bytes from the unique line beginning `### <EID> — ` through the byte immediately before
the next such case-heading line, or EOF for E41. Preserve all LF bytes and require exactly one
matching case heading. The resulting nonempty artifact has logical ID
`<attempt-id>-rubric-section`, kind `rubric_section`, and a root digest/size record. It is created
only for the evaluator, never copied into `bundle_root`, never cited by executor artifacts, and is
byte-compared by rerunning this extraction from the frozen binding copy.

`evaluator-input.json` has exactly `{schema_version, case_id, attempt_id, evaluator_alias,
rubric_section_ref, source_manifest_ref, bundle_manifest_ref, result_record_ref,
executor_output_ref, executor_operations_ref, executor_session_receipt_ref, evaluator_assignment,
assembled_sequence}`. Version is integer `1`; evaluator alias differs from every executor alias.
The seven `*_ref` fields are exact `LogicalRef` records with respectively `rubric_section`,
`raw_input`, `bundle_manifest`, `result_record`, `executor_output`,
`executor_operation_snapshot`, and `executor_session_snapshot` kinds and exact same-attempt joins
with that attempt's credit state. Assignment is exact `AssignmentRequest`; sequence is after the two executor
snapshots and rubric extraction are immutable and before evaluator dispatch. It never cites final
`operations.jsonl` or final `session-receipt.json`, so later evaluator events cannot stale the
dispatched input.

`evaluator-output.json` has exactly `{schema_version, case_id, attempt_id, evaluator_alias,
evaluator_input_logical_id, findings, evaluation_verdict, dependent_action_state,
recommended_correction, completed_sequence}`. Version is integer `1`; input ID joins the exact
same-attempt evaluator input with that attempt's credit state; findings is an array of `PrivateFinding`; verdict is `PASS`, `FAIL`, or
`BLOCKED`; dependent state is nonempty and not the verdict; recommended correction is JSON null for
PASS without findings and otherwise a nonempty observable correction/blocker string; sequence is
the terminal evaluator operation. Verdict/state equal the root/public current case records.

Each `operations.jsonl` line has exactly `{schema_version, case_id, attempt_id, sequence,
actor_alias, phase, operation, authorization, target_alias, input_logical_ids, output_logical_ids,
result, exit_code}`. Version is integer `1`; all lines share case/attempt; sequence is exactly
`1..line_count`; actor joins a session; phase is `preparation`, `dispatch`, `execution`,
`evaluation`, or `review`; operation is `file-read`, `file-write`, `agent-dispatch`, `local-git`,
`local-test`, `local-tool`, `review`, or `no-op`; authorization is `allowed`,
`forbidden-blocked`, or `forbidden-observed`; target is a stable alias; logical-ID arrays are sorted
unique and join artifacts already available/created at that sequence; result is nonempty;
`exit_code` is integer or null. At least one executor dispatch, executor terminal event, evaluator
dispatch, and evaluator terminal event is present only for `evaluator-closed`. `pre-dispatch` has no
executor dispatch; `executor-running` ends after dispatch without requiring an executor terminal;
`executor-closed` and later require the executor terminal; `evaluator-prepared` has no evaluator
dispatch; `evaluator-running` requires evaluator dispatch without terminal; and `evaluator-closed`
requires both. Any actually performed prohibited effect closes the attempt non-credit with reason
`prohibited-effect`. An expected denial is instead recorded `forbidden-blocked`; it may close
`complete` only when no prohibited effect occurred and the evaluator's exact rubric supports the
observed denial. Every finding remains visible.

`session-receipt.json` has exactly `{schema_version, case_id, attempt_id, sessions}`. Version is
integer `1`; sessions is a nonempty ordered array of exact `{role_alias, session_alias, role_class,
requested_assignment, accepted_native_assignment, independently_verified_runtime_fact,
start_sequence, end_sequence}` records. Role class is `executor`, `evaluator`, `analyst`, or
`reviewer`; assignment/facts use the reusable records; sequence bounds are positive and join
operations. Session aliases are unique. A receipt exists only from `executor-running` onward; it
contains at least one executor then, and contains exactly one evaluator only from
`evaluator-running` onward. The evaluator session/role aliases differ from every executor. E10 may
have its two routing executors,
analyst, reviewer, and evaluator in the same receipt, still as distinct sessions. Session aliases
are globally unique across all case receipts and non-case role records. A non-case authoritative
native receipt, when one exists, is retained as nonempty UTF-8/LF text under
`transcripts/roles/<role-alias>/<session-alias>/native-receipt.txt`; its logical ID is the only
non-null receipt reference allowed in that role's `ObservedAssignment`/`RuntimeFact`. The exact
prebound-public-role exception is the separately specified
`checks/prebound-public-session-receipts/<session-alias>.txt` path owned by the redaction recorder;
no receipt is duplicated across both locations.

The two `.txt` prompts and executor output are nonempty UTF-8/LF text artifacts. The executor prompt
is outside `bundle_root` but has a required logical ID, digest, and byte count; contamination scans
its exact bytes. The evaluator prompt is hashed but exempt from executor contamination because it
and the isolated rubric section are created only after executor output and both executor snapshots
close. Before dispatch and after output, independently
enumerate the physical bundle, reject symlink/special/escaped nodes, require exact bundle-manifest
set equality, recompute all bytes, and scan them plus the executor prompt. Before evaluation, also
prove that neither the rubric artifact path nor any exact rubric-section byte occurs as a bundle
member; a match closes that attempt as pre-evaluation contamination and non-credit without
dispatching the evaluator.

### Exact group schemas

`reports/<group>-manifest-v<N>.json` has exactly `{schema_version, binding_sequence, group_id, sequence, case_ids,
current_attempts, artifact_logical_ids, group_report_logical_id, schema_source_ref,
binding_snapshot_ref, closed_sequence}`. Version is integer `1`; binding sequence is the positive
active binding-set version accepted by schema review; sequence N is positive;
case IDs equal the group partition; `current_attempts` is an exact object with one key per case and
its complete current attempt ID; artifact IDs are sorted unique and equal every actual case
artifact from all current/superseded/non-credit attempts owned by the
group except this manifest/report/review; report ID joins the version-matched Markdown report;
`schema_source_ref` and `binding_snapshot_ref` are `LogicalRef` records for the exact retained
active binding-set bytes. For this correction they are
`inputs/binding/schema/recovery-plan-v3.md` and
`inputs/binding/binding-snapshot-manifest-v3.json`, logical IDs `recovery-schema-source-v3` and
`binding-snapshot-manifest-v3`, null case/attempt, and kind `raw_input`; closed sequence follows all
case evaluations. The group manifest's `binding_sequence` is integer `3` and equals the fresh
PASS schema review's selected binding set; a later plan correction must increment and consistently
replace all three refs rather than reuse v3.
The referenced artifacts must exist, match logical ID/kind/digest, and be members of the selected
generation. No bare schema or binding digest is permitted.

`reports/<group>-review-v<N>.json` has exactly `{schema_version, review_kind, group_id,
review_sequence, reviewer_alias, reviewer_session_alias, requested_assignment, accepted_native_assignment,
independently_verified_runtime_fact, group_manifest_ref, group_report_ref, case_ids, findings,
verdict, completed_sequence}`. Version is integer `1`; review kind is `group-review`; group/sequence
match the reviewed manifest version; reviewer alias is the exact group reviewer and its globally
unique session alias identifies this dispatch; assignment/facts use reusable records;
manifest/report refs are `LogicalRef`; case IDs match the group; findings are
`PrivateFinding`; verdict is `PASS` or `CHANGES_REQUIRED`, with PASS permitted only when no open
Critical/Important finding remains; completed sequence follows group close. Group Markdown report
is nonempty UTF-8/LF and contains no unannotated private path/native ID. The reviewer independently
enumerates every actual artifact from all group attempts, validates each terminal-phase family
matrix, and grants semantic credit only to the complete current attempt per case.

### Exact shared-input, review, check, and audit schemas

Every recovery-created neutral JSON case input uses `SyntheticInput`: exact keys
`{schema_version, input_identity, case_ids, input_kind, facts, source_refs, created_sequence}`.
Version is integer `1`; identity is a logical ID; case IDs are a nonempty ordered subset of the
fixed partition; input kind is `artifact-map`, `plan-event`, `decision-event`, `permission-event`,
`identity-event`, `model-event`, `load-sample`, `registration-sample`, `prototype-transition`,
`viability-record`, `cost-change`, `release-readiness`, or `rehearsal`; source refs are sorted unique
`LogicalRef` records; sequence is positive. `facts` is a nonempty array of exact `{name,
value_type, value, provenance, certainty}` records. Name is unique; value type is `string`,
`integer`, `boolean`, `string-list`, or `unknown`; value has that exact JSON type and is null only
for `unknown`; provenance is `tracked-source`, `retained-source`, or `seeded-synthetic`; certainty
is `fact`, `hypothesis`, or `Unknown`. This typed fact array replaces open-ended nested fixture
objects. Byte-exact copied tracked/private JSON remains an input blob, not a recovery-created JSON
record; its structure is not reinterpreted, and its source/copy digest is carried by `SourceBinding`.

Binding snapshot v1 is the immutable unversioned path
`inputs/binding/binding-snapshot-manifest.json` and retains its exact v1 keys
`{schema_version, source_head, entries, created_sequence}` with version integer `1`. Sequence 2 is
the exact absent/non-artifact reservation in recovery history and does not instantiate this schema.
Each materialized successor binding set V>=3 is
`inputs/binding/binding-snapshot-manifest-v<V>.json` and has exactly
`{schema_version, binding_sequence, source_head, schema_source_logical_id, entries,
created_sequence}`. Successor schema version is integer `2`; `binding_sequence` is the positive
path-derived V and may not equal 2; head is exact lowercase 40-hex; schema-source ID is
`recovery-schema-source-v<V>` and joins the versioned exact accepted-plan copy. Entries are a
nonempty sorted array of exact `{logical_id, source_alias, source_path, copy_path, sha256,
byte_count, equality}`; paths are canonical tracked/recovery relative paths, equality is boolean and
must be true, and digests/sizes match both bytes. Historical unversioned v1 group briefs retain the
previous exact schema without `binding_sequence`. Each materialized successor group brief V>=3 has exactly `{schema_version,
binding_sequence, group_id, case_ids, schema_source_ref, binding_snapshot_ref, allowed_write_roots,
forbidden_effects, recorder_assignment, created_sequence}` with version integer `2`, exact partition,
canonical disjoint roots, `StringEffectSet`, `AssignmentRequest`, and a pre-dispatch sequence.
Binding sequence V matches path `inputs/binding/group-briefs-v<V>/<group>.json` (the unversioned v1
briefs are retained historical inputs and are not dispatch-eligible); V=2 is invalid and must be
absent. Its two refs are the same
exact V-specific `LogicalRef` joins required by the group manifest; changing either
referenced byte invalidates every brief and requires re-freeze before dispatch.

`checks/prebound-public-sessions-v<N>.json` has exactly `{schema_version, binding_sequence,
sessions, created_sequence}`. Version is integer `1`; binding sequence equals filename N;
`sessions` is exactly two records, in order for `redaction-check-recorder` and `public-assembler`.
Each record has exactly `{role_alias, session_alias, requested_assignment,
accepted_native_assignment, independently_verified_runtime_fact, private_bindings}`. Assignment
records use the reusable schemas; session alias is a stable alias; `private_bindings` is a sorted
unique array of exact `{binding_kind, value}` records, where kind is `task-id`, `thread-id`,
`client-thread-id`, `agent-id`, `host-id`, `session-id`, `worktree-path`, or `private-url`. It contains
every native ID/path/URL disclosed while establishing that role and may be empty only when none was
disclosed. These private values enter the exact denylist, never a public file. Created sequence is
positive and precedes execution-generation freeze and every public write. If an authoritative
assignment/runtime receipt exists, its raw nonempty UTF-8/LF bytes are retained below
`checks/prebound-public-session-receipts/<session-alias>.txt` before this JSON and its logical ID is
used by the nested reusable record; otherwise the value is `Unknown` and reference null.

`checks/public-alias-vocabulary.txt` is the lexicographically sorted, duplicate-free LF-separated
set of every backtick-delimited role alias in the first column of the ownership table; there is one
alias per line and a final LF. No wildcard, native binding, group name, or `.local-handoff` appears
in that file. Its sidecar follows the exact sidecar schema.
`checks/private-denylist-v<N>.txt` is likewise sorted, duplicate-free, one nonempty exact private
value per LF-terminated line; it contains every
value in `private_bindings` plus every private path/ID/URL/credential-like binding observed before
public assembly. N equals the version-matched public-session binding sequence, and old versions are
immutable. The highest version included by the selected generation has artifact credit state
`current`; earlier denylist/session-binding versions are `superseded`; static vocabulary is
`shared`. Its sidecar follows the same schema. The literal `.local-handoff` is an additional
scanner allow-token, not a role-vocabulary entry and never an exemption from exact denylist matches.

`transcripts/metrics/coordination-observation.jsonl` is the sole metric event source. Each line has
exactly `{schema_version, sequence, event_kind, subject_alias, result, evidence_refs}`. Version is
integer `1`; sequence is exactly `1..line_count`; event kind is `observation-start`,
`observation-end`, `manual_owner_relay_events`, `duplicate_owner_approval_prompts`,
`duplicate_user_owned_task_creations`, `duplicate_internal_work_launches`, `invalid_pass_uses`, or
`incorrect_transitions`; subject alias is a stable public alias; result is a nonempty neutral
observation; and evidence refs are a sorted unique array of `LogicalRef` records. The first/last
line are respectively the sole start/end events. No event is backfilled from a public aggregate.
The metric recorder writes the line at observation time and never edits an earlier line.
Its artifact logical ID is exactly `coordination-observation-log-v1`, kind `transcript`, null
case/attempt, and credit state `current` in the selected generation.

`checks/bundle-contamination.json` is the immutable policy and has exactly `{schema_version,
forbidden_paths, forbidden_labels, forbidden_kinds}`. Version is integer `1`; all three values are
sorted unique nonempty-string arrays and equal the literal policy in Task 1.7. Each
`checks/bundle-contamination-scan-v<N>.json` has exactly `{schema_version, scan_sequence,
policy_ref, cases, aggregate}`. Version is integer `1`; `policy_ref` is the same exact check-kind
`LogicalRef` required by every executor bundle manifest; each case record is exact `{case_id,
attempt_id, bundle_manifest_logical_id, executor_prompt_logical_id, scanned_files, exact_matches,
verdict}` with nonnegative integer counts and verdict `PASS` or `CONTAMINATED`; `cases` is the exact
ordered 21 current case/attempt set. Aggregate is exact `{case_count, scanned_files, exact_matches,
verdict}`, is recomputed from case records, has case count 21, and is PASS iff every case is PASS and
total matches are zero.

Every product Change Review in `product-repo/reviews/` has exact keys `{schema_version,
review_kind, review_identity, reviewer_alias, reviewer_session_alias, requested_assignment, accepted_native_assignment,
independently_verified_runtime_fact, requirements_refs, candidate, check_refs, findings, verdict,
completed_sequence}`. Version is integer `1`, kind is `product-change-review`, requirements/checks
are nonempty arrays of `LogicalRef`; review identity and globally unique reviewer session alias bind
one dispatch; findings are `PrivateFinding`, and verdict is `PASS` or
`CHANGES_REQUIRED`. `candidate` has exactly `{branch, base_commit, head_commit, tree, diff_ref}`;
branch is the assigned local branch, Git fields have exact lengths, and `diff_ref` is a
`LogicalRef` to the exact retained stdout bytes of the full binary base..head diff. PASS requires
exact reviewed head unchanged and no open required finding.

`product-repo/rehearsals/seed-oracle-v1.json` has exactly `{schema_version, matrix_version,
c_commit, c_commit_bytes_ref, selected_index, mutation_id, focused_test, s_commit, s_tree}`.
Versions are integer `1`; index is 0, 1, or 2; mutation ID is respectively `unknown-contact`,
`completed-filter`, or `outcome-persistence` according to the fixed matrix; test name must match its
row; `c_commit_bytes_ref` is a `LogicalRef` to the retained stdout bytes of exact `git cat-file
commit C`. Other rehearsal JSON records use exact `ProductGitRecord`: `{schema_version, record_id,
record_kind, sequence, commits, trees, blobs, commands,
relationships, verdict}`. Kind is `workitem-history`, `merge-proof`, `stale-pass`, `stale-final`,
`rollout`, or `rollback`; `record_id` is unique and matches `[a-z0-9][a-z0-9-]*`;
commits/trees/blobs are sorted exact `{alias, git_oid}` arrays; commands are ordered exact
`{sequence, argv, exit_code, stdout_ref, stderr_ref}` records with sequence exactly `1..count`, argv
a nonempty string array, and exit code integer. Each ref is a `LogicalRef` with kind `check`, null
case/attempt, and joins exactly one regular file at
`product-repo/command-streams/<record-id>/<sequence>.stdout` or `.stderr`. Both stream files must
exist even when the command emitted zero bytes; only these command-stream artifacts may use
`empty_allowed=true`, and a legitimate empty stream has byte count zero and the SHA-256 of empty
bytes. Missing streams, declared-but-unwritten streams, or a digest copied from any other command
fail. Their logical IDs are exactly `product-git-<record-id>-command-<sequence>-stdout` and
`product-git-<record-id>-command-<sequence>-stderr`; the seed oracle stdout ref uses the same rule
with record ID `seed-oracle-v1`. Relationships are sorted exact `{left_alias,
relation, right_alias, result}` with relation `parent-of`, `ancestor-of`, `same-tree`,
`same-blob`, `same-diff`, or `different-head` and boolean result; verdict is `PASS`, `FAIL`, or
`BLOCKED`.

`checks/task1-schema-review-recovery-history-v1.json` is the sole legacy-quarantine record and has
exactly `{schema_version, history_identity, incidents, historical_snapshots, binding_history,
dispatch_authority, created_sequence}`.
Version is integer `1`; identity is literal `task1-schema-review-recovery-history-v1`;
`dispatch_authority` is literal `none`; sequence is positive. `incidents` is exactly two records in
v1, v2 order. Each has exactly `{review_path, review_sha256, review_identity, review_kind, verdict,
incident_class, incident_state, gate_credit, findings_retained,
retrospective_reconstruction_forbidden, quarantined_refs, quarantined_finding_labels}`. Review path/identity/digest are the
exact values below; kind is `schema-review`; verdict is `CHANGES_REQUIRED`; incident class is
`pre-freeze-rejected-schema-review`; incident state is `superseded-non-credit`; gate credit is
false; findings retained and reconstruction forbidden are true.

`historical_snapshots` is exactly one record in v1 with exactly `{source_path, source_sha256,
source_byte_count, snapshot_ref, snapshot_path, copy_sha256, copy_byte_count, byte_equal,
file_mode, captured_before}`. Its values are: source path `progress.md`; source/copy SHA-256
`5e50255f613334839560b676c2bf2dbe7a9fe05a2f01bbd135842385d2e22f2b`; source/copy byte count
`18640`; snapshot path `history/progress-ledger-snapshot-v1.md`; `byte_equal=true`; file mode
string `0444`; and `captured_before='first-post-plan-review-v7-progress-append'`. `snapshot_ref` is
the exact `LogicalRef` for `progress-ledger-snapshot-v1`, kind `raw_input`, null case/attempt, and
the same digest. At record creation the validator requires source and copy to be regular files with
equal bytes, size, and digest and the copy to be read-only. On later validation it requires the
immutable snapshot and its root-artifact join but does not require the intentionally advanced live
ledger to retain the old digest. Any other snapshot record, mutable-path ref, reconstructed bytes,
or reverse reference from the raw snapshot is invalid.

`binding_history` is exactly one record with exactly `{binding_sequence, state, reason,
reserved_paths, artifact_count, logical_ids, inventory_classification, generation_membership,
dispatch_credit, retrospective_materialization_forbidden, plan_commit, plan_review_path,
plan_review_sha256, plan_review_verdict, observed_before_sequence}`. Its exact values are:
`binding_sequence=2`; `state='not-materialized'`;
`reason='round-6-plan-did-not-achieve-PLAN_PASS'`; `artifact_count=0`; `logical_ids=[]`;
`inventory_classification='none-non-artifact-history'`; `generation_membership=false`;
`dispatch_credit=false`; `retrospective_materialization_forbidden=true`; plan commit
`d3c0369ce38142832a7347c1ead1140945b2fedd`; review path `plan-review-v7.json`; review SHA-256
`7d234a640d4d51064a7d0c17485c5166189ab619cd7dc053eff9b6b9b1e65f6b`; review verdict
`PLAN_CHANGES_REQUIRED`; and `observed_before_sequence` is a positive integer equal to the root
writer's retained history-closure event and strictly less than v3 snapshot `created_sequence`.
`reserved_paths` is exactly this sorted array:

```json
[
  "inputs/binding/binding-snapshot-manifest-v2.json",
  "inputs/binding/group-briefs-v2/coordination.json",
  "inputs/binding/group-briefs-v2/delivery-release.json",
  "inputs/binding/group-briefs-v2/discovery-readiness.json",
  "inputs/binding/group-briefs-v2/resume-scaling.json",
  "inputs/binding/schema/recovery-plan-v2.md"
]
```

Every reserved path must be absent. This record is
nested non-artifact history: none of its path strings or historical metadata is a `LogicalRef`,
artifact record, digest-resolution claim, or permission to create bytes.

| Review identity | Exact path | Exact retained review SHA-256 | Quarantined JSON pointers |
|---|---|---|---|
| `task1-schema-review-v1` | `reports/task1-schema-review-v1.json` | `4e3dc343dc81795b7d052a3f5fa88ebb9650b5aea2fddab44b0a5c68b843050b` | `/candidate/validator_ref`, `/candidate/validator_tests_ref` |
| `task1-schema-review-v2` | `reports/task1-schema-review-v2.json` | `1fc8086db0efafd623cb8d0bc5ebf27ca1e7cf42dda78d713748923bfabf0020` | `/candidate/validator_ref`, `/candidate/validator_tests_ref`, `/check_refs/2` |

Each `quarantined_refs[]` member has exactly `{json_pointer, declared_logical_id, declared_kind,
declared_sha256, target_availability, retained_target, conflict_reason, join_treatment,
recovery_search}`. The exact ordered members are:

| Review/pointer | Declared logical ID / kind / SHA-256 | Availability and treatment |
|---|---|---|
| v1 `/candidate/validator_ref` | `archive-validator-v1` / `check` / `d4bd48ce7b92e10afef09240c03df86754f8fd0bcf7a05e713138e8b5a640306` | `missing`; target null; reason `missing-target-bytes-after-authorized-search`; treatment `quarantined-missing` |
| v1 `/candidate/validator_tests_ref` | `archive-validator-tests-v1` / `check` / `2889bf9bdfd4ac1956d276aea40838e8f90097d6251e4c6ce799ce5e40bbe031` | `missing`; target null; reason `missing-target-bytes-after-authorized-search`; treatment `quarantined-missing` |
| v2 `/candidate/validator_ref` | `archive-validator-v1` / `check` / `e66c20dadbf1d26df13e654a45b1406fd22062913133a5d89ce027429bdb6392` | `retained-under-different-identity`; forensic target below; reason `logical-id-reused-with-different-bytes`; treatment `quarantined-conflict` |
| v2 `/candidate/validator_tests_ref` | `archive-validator-tests-v1` / `check` / `3b883a5a35e33a3ab325c400096b5eaf7bdbdc4103f652e55aab451cb5038eac` | `retained-under-different-identity`; forensic target below; reason `logical-id-reused-with-different-bytes`; treatment `quarantined-conflict` |
| v2 `/check_refs/2` | `reports-task1-schema-review-v1` / `check` / `4e3dc343dc81795b7d052a3f5fa88ebb9650b5aea2fddab44b0a5c68b843050b` | `retained-under-different-identity`; v1 incident target below; reason `declared-kind-conflicts-with-retained-review`; treatment `quarantined-conflict` |

`retained_target` is null iff availability is `missing`; otherwise it has exactly `{logical_id,
kind, relative_path, sha256}` and joins one actual root artifact. The two v2 candidate targets are
respectively `task1-schema-review-v2-forensic-validator` at
`review-targets/task1-schema-review-v2-forensic/archive-validator.py` and
`task1-schema-review-v2-forensic-validator-tests` at the corresponding
`archive-validator-tests.py`, both kind `check` and with the declared v2 digest. The v2 wrong-kind
ref instead names logical ID `task1-schema-review-v1-incident`, kind `review`, the v1 review path,
and v1 review digest. These targets preserve known bytes under honest identities; they do not
retroactively repair either rejected review.

`recovery_search` has exactly `{performed, scope, methods, network_used, external_action_used,
result, limitation}`. For the two missing v1 targets, performed is true; scope is
`authorized-local-worktree-and-ignored-recovery-artifacts`; methods are exactly
`['content-hash', 'filename-and-reference', 'local-git-object']`; both external flags are false;
result is `not-found`; limitation is a nonempty description of the completed local-only boundary.
For all three v2 conflicts, performed is false; scope is
`not-required-retained-bytes-present`; methods is empty; both external flags are false; result is
`not-run`; limitation states that retained bytes cannot repair the historical ID/kind conflict.
No other value is valid.

`quarantined_finding_labels` is an ordered array of exact `{json_pointer,
declared_logical_id, basis_ref_pointer, join_treatment}` records. Treatment is always
`quarantined-incident-label`; the basis pointer is one of that same incident's `quarantined_refs`
and declares the same historical target identity. The exact v1 set is the ten fully expanded
records `/findings/{0,1,2,3,4}/evidence_logical_ids/0` = `archive-validator-v1`, based on
`/candidate/validator_ref`, and `/findings/{0,1,2,3,4}/evidence_logical_ids/1` =
`archive-validator-tests-v1`, based on `/candidate/validator_tests_ref`. The exact schema-review-v2
label set is the
fourteen fully expanded records `/findings/{0,1,2,3,4,6}/evidence_logical_ids/0` =
`archive-validator-tests-v1`, based on `/candidate/validator_tests_ref`;
`/findings/{0,1,2,3,4,6}/evidence_logical_ids/1` = `archive-validator-v1`, based on
`/candidate/validator_ref`; and `/findings/2/evidence_logical_ids/3` plus
`/findings/5/evidence_logical_ids/2` = `reports-task1-schema-review-v1`, based on `/check_refs/2`.
Braced indices in this paragraph define separate JSON array members, not literal path text; the
stored arrays contain all 24 records individually in ascending numeric JSON-pointer order.

The recovery-history validator first validates the mandatory progress snapshot contract above,
requires every binding-sequence-2 reserved path to be absent and the exact nested non-artifact
record to match plan review v7, then hashes/parses both exact schema-review files and requires every
listed pointer and declared value to byte-equal that review JSON. Only the five exact `LogicalRef`
tuples are removed from normal target joining, and only the 24 exact finding-label tuples use their
incident-local basis instead of the global `PrivateFinding` evidence-ID join. All other candidate,
requirement, check, finding, assignment, identity, and path rules in both review records still
validate. A changed review byte, digest, path, pointer, declared value, missing label, or extra
exception fails. The missing `declared_sha256`
values are preserved historical claims, not `LogicalRef` records or current evidence; they receive
no target, resolution, gate, generation-current, or public credit. Global artifact logical-ID
uniqueness therefore remains strict over actual retained artifacts.

The validator schema-family name for the one exact recovery-history path is
`schema-review-recovery-history`; it rejects that family at every other path. The five quarantined
refs and 24 quarantined finding labels are nested members of this one family, not extra artifact
families or actual artifact IDs.

Starting at N=3, before every schema-review dispatch the `schema-binding-writer` closes and
relinquishes the seven fixed candidate paths. The `root-manifest-writer` then makes byte-exact regular
read-only copies at these paths and assigns these unique root logical IDs/kinds:

| Fixed candidate | Immutable review-specific target | Logical ID | Kind |
|---|---|---|---|
| `inputs/binding/schema/recovery-plan-v3.md` | `review-targets/task1-schema-review-v<N>/recovery-plan.md` | `task1-schema-review-v<N>-schema-source` | `raw_input` |
| `checks/archive-validator.py` | `review-targets/task1-schema-review-v<N>/archive-validator.py` | `task1-schema-review-v<N>-validator` | `check` |
| `checks/archive-validator-tests.py` | `review-targets/task1-schema-review-v<N>/archive-validator-tests.py` | `task1-schema-review-v<N>-validator-tests` | `check` |
| `checks/build-live-manifest.py` | `review-targets/task1-schema-review-v<N>/build-live-manifest.py` | `task1-schema-review-v<N>-live-manifest-builder` | `check` |
| `checks/bundle-contamination.json` | `review-targets/task1-schema-review-v<N>/bundle-contamination.json` | `task1-schema-review-v<N>-contamination-policy` | `check` |
| `inputs/binding/binding-snapshot-manifest-v3.json` | `review-targets/task1-schema-review-v<N>/binding-snapshot-manifest.json` | `task1-schema-review-v<N>-binding-snapshot` | `raw_input` |
| `checks/public-alias-vocabulary.txt` | `review-targets/task1-schema-review-v<N>/public-alias-vocabulary.txt` | `task1-schema-review-v<N>-alias-vocabulary` | `check` |

There is deliberately no directory sidecar or mutable review-package file: the seven root artifact
records and seven candidate `LogicalRef` values bind every target separately. The recorder verifies
source/copy byte equality and digest before making each target read-only, refreshes the live root
manifest at `pre-schema-review`, and never rewrites that target directory. A correction reopens
only the five mutable fixed candidates (validator, tests, builder, policy, and alias vocabulary)
under `schema-binding-writer`; the active plan copy and binding snapshot never reopen. It then
creates N+1 copies of all seven sources and a new review after that writer again relinquishes the
five mutable paths. A finding against plan or binding bytes stops recovery for a new plan-only
correction, fresh PLAN review, and next append-only binding-set version; it is not repaired in place.

For N>=3, `reports/task1-schema-review-v<N>.json` has the same exact keys as a product Change
Review except `review_kind='schema-review'` and `candidate` is exactly `{schema_source_ref,
validator_ref, validator_tests_ref, live_manifest_builder_ref, contamination_policy_ref, binding_snapshot_ref,
alias_vocabulary_ref}`. The seven refs use the exact N-specific IDs/kinds above, null case/attempt,
and exact copy digests. Requirements/check refs and findings use the common records and every ref
must join retained exact bytes regardless of verdict. `requirements_refs` must include the exact
`progress-ledger-snapshot-v1` `LogicalRef`; no schema review may cite `progress-live-ledger` or
`progress.md`. Review identity and path-derived N are
`task1-schema-review-v<N>`; reviewer/session/assignment identities are exact. Verdict is `PASS`,
`CHANGES_REQUIRED`, or `BLOCKED`. PASS requires all joins and zero open Critical/Important finding;
CHANGES_REQUIRED or BLOCKED requires all joins plus at least one open Critical/Important finding.
No Git candidate or mutable-root digest occurs. A non-PASS verdict never disables validation.

Root inventory classifies the two literal review path/digest pairs above as kind `review`, producer
`root-manifest-writer`, credit state `non-credit`, and unique logical IDs
`task1-schema-review-v1-incident`/`task1-schema-review-v2-incident`. Every N>=3 schema review is
kind `review`, producer `root-manifest-writer`, credit state `shared`, logical ID equal to its review
identity. The recovery-history record is kind `recovery_history`, producer
`root-manifest-writer`, credit state `non-credit`. V2 forensic targets are producer
`root-manifest-writer`, credit state `non-credit`; the validator copies use the unique forensic IDs
above, while the preserved builder copy has logical ID `checks-build-live-manifest`, kind `check`,
path `review-targets/task1-schema-review-v2-forensic/build-live-manifest.py`, and exact SHA-256
`5b5df5454edacbbcca5c998bc78c7caa2c5b63e480cad6dfda8649f48b8ccbb9`. The corrected fixed
`checks/build-live-manifest.py` uses logical ID `build-live-manifest-v2`, kind `check`, producer
`schema-binding-writer`, and credit state `shared`. Compliant N>=3 targets use the root writer and
credit state `shared`. All are private, retained in live inventories and every later immutable
generation, and none is eligible for public evidence or case/group dispatch authority except a
fresh N>=3 schema-review PASS.

`checks/execution-evidence-audit-v<N>.json` has exactly `{schema_version, generation,
generation_ref, generation_sidecar_ref, inventory_snapshot_ref, inventory_snapshot_sidecar_ref,
reviewer_alias, reviewer_session_alias, requested_assignment,
accepted_native_assignment, independently_verified_runtime_fact, derived_counts, missing, extra,
duplicates, mismatches, findings, verdict, completed_sequence}`. Version is integer `1`;
generation is N; the four refs are exact `LogicalRef` joins to the version-matched immutable
generation, generation sidecar, root-inventory snapshot, and snapshot sidecar, all kind `check`
with null case/attempt; reviewer session alias is globally unique; assignments use reusable records; four error arrays contain exact `AuditError`
records `{code, logical_id, relative_path, expected, actual}` where nullable logical ID/path are
allowed but expected/actual are nonempty. Code is exactly one of `schema`, `missing-file`,
`extra-file`, `duplicate-logical-id`, `duplicate-path`, `digest`, `size`, `symlink`, `escaped-path`,
`kind-join`, `case-join`, `attempt-join`, `credit-state`, `required-artifact`,
`assignment-receipt`, `review-membership`, `public-context`, `public-resolution`,
`public-conflict`, `public-lexical`, `public-multiple-context`, `public-state`, `phase-join`,
`snapshot-join`, `stream-join`,
`immutable-prefix`, `rubric-extraction`, `mutable-reference`, `metric-boundary`, `live-inventory`,
`history-quarantine`, `progress-snapshot`, `review-target`, `binding-set`, `fixture-coverage`, or `redaction`; findings use `PrivateFinding`; verdict is `PASS` or
`CHANGES_REQUIRED`. `derived_counts` has exactly the keys `selected_cases`, `current_attempts`,
`superseded_attempts`, `non_credit_attempts`, `all_attempt_artifacts`,
`raw_inputs`, `executor_prompts`, `bundle_manifests`, `executor_outputs`, `result_records`,
`executor_operation_snapshots`, `executor_session_snapshots`, `rubric_sections`,
`evaluator_inputs`, `evaluator_prompts`, `evaluator_outputs`, `transcripts`, `session_receipts`,
`product_change_reviews`, `group_manifests`, `group_reports`, `group_reviews`, `schema_reviews`,
`schema_review_targets`, `recovery_history_records`, `historical_progress_snapshots`,
`materialized_binding_sets`, and `reserved_binding_sequences`; each value is exact `{observed, required,
status}` with nonnegative integers and status `complete` iff equal.
For the thirteen artifact-family keys and `all_attempt_artifacts`, observed is derived from all actual artifacts across every
attempt and required is independently derived from every attempt's terminal-phase matrix; it is not
fixed at 21. `superseded_attempts` and `non_credit_attempts` are independently counted from attempt
histories and require those same derived totals. `selected_cases` and `current_attempts` each
require exactly 21 complete current
attempts and are the semantic/current denominator. Thus non-credit partial bytes are audited and
retained without inflating current behavioral credit.
`schema_reviews` equals every actual v1/v2 incident and N>=3 schema-review file;
`schema_review_targets` equals every actual v2 forensic and N>=3 target file; and
`recovery_history_records` requires exactly the one valid recovery-history record.
`historical_progress_snapshots` equals every actual immutable
`history/progress-ledger-snapshot-v<N>.md` artifact and requires at least the valid v1 snapshot;
the mutable `progress.md` artifact is excluded from this count and from every generation. Their required
counts derive from filesystem/path classification, not manifest declarations. Missing, extra,
misclassified, or wrongly credited history/review-target bytes fail the audit.
`materialized_binding_sets` independently requires exactly the complete v1 and active v3 sets
(`observed=required=2`) at initial generation freeze; completeness is derived from the six actual
paths and joins per set, not a declared count. `reserved_binding_sequences` independently requires
exactly the one sequence-2 recovery-history record plus absence of all six reserved v2 paths
(`observed=required=1`). A fabricated v2 byte, artifact/ID/ref/classification, or missing/incomplete
active v3 set fails with `binding-set`.

`checks/digest-resolution-v<N>.json` has exactly `{schema_version, candidate_head,
candidate_tree, selected_generation, selected_generation_sha256, scanned_paths, occurrences,
class_counts, errors, verdict}`. Version is integer `1`; candidate identities are exact Git OIDs;
generation/digest match the pointer; `scanned_paths` is exactly the eleven allowlisted paths in
File Map order. Each occurrence is exact `{public_path, line, column, start_byte, end_byte,
claim_start_byte, claim_end_byte, prefix_spelling, prefix_status, json_pointer, syntax,
discovery_rules, raw_candidate, lexical_status, canonical_sha256,
classification_status, logical_id, claim_state, claim_class, evidence_kind, case_id, attempt_id,
resolved_target_class, resolved_logical_id, resolved_sha256}`. Line/column are positive and identify
`claim_start_byte`; byte
offsets are zero-based and end-exclusive with `end_byte >= start_byte` and
`claim_end_byte == end_byte`. `start_byte..end_byte` is the exact payload span. For prefix
discovery, `claim_start_byte == start_byte - 7` and the source bytes from claim start through payload
end are the full label plus payload; without prefix discovery, `claim_start_byte == start_byte`.
`prefix_spelling` is JSON null
iff prefix discovery did not match; otherwise it is the exact seven ASCII source characters matching
`[sS][hH][aA]256:` and byte-equals the `claim_start_byte..start_byte` source slice.
`prefix_status` is `absent`, `canonical-lowercase`, or `alternate-case`, with
`absent` iff the spelling is null, `canonical-lowercase` only for exact `sha256:`, and
`alternate-case` for every other matched spelling. JSON Pointer is a string and is nonempty only
for a structurally discovered JSON value. `syntax` is `json-value`, `markdown-annotation`,
`python-binding`, or `raw-token`; `discovery_rules` is the sorted nonempty subset of
`boundary-hex64`, `sha256-prefix`, and `json-sha-key`, and contains `sha256-prefix` iff
`prefix_status` is not `absent`; `raw_candidate` is the exact decoded
candidate payload or JSON source lexeme. It may be empty only when `prefix_status` is not `absent`.
Candidates with the same exact path and payload span are one occurrence with merged discovery
rules; if one source
is prefix discovery, that occurrence retains its exact prefix spelling and expanded full-claim span.
Overlapping nonidentical payload spans are separate occurrences ordered by their exact byte spans,
and a multiple-context match is never hidden by deduplication.

`lexical_status` is `canonical`, `uppercase`, `wrong-length`, `nonhex`, or `wrong-type`. A string
is canonical only when it matches exactly `[0-9a-f]{64}`; an otherwise 64-character hexadecimal
string containing `A`–`F` is uppercase; other string lengths are wrong-length; a 64-character
nonhex string is nonhex; and a structurally discovered non-string JSON value is wrong-type.
`canonical_sha256` equals `raw_candidate` only for canonical status and is null otherwise.
`classification_status` is `classified`, `unclassified`, `conflicting`, or `malformed`; every
noncanonical payload or `alternate-case` prefix is malformed. A classified record has non-null
logical ID, state `current`
or `superseded`, class `retained-private`, `tracked-public`, or `superseded-historical`, and a
conditional evidence kind; case/attempt are both null only for a global claim and otherwise the
exact current pair. Its target class is `generation-artifact`, `tracked-blob`, or
`historical-noncredit`; resolved ID/digest equal the target, except historical noncredit permits
both null. An unclassified, conflicting, or malformed record sets every semantic/resolution field
after `classification_status` to null and has respectively a `public-context`, `public-conflict`, or
`public-lexical` error. A candidate matching more than one allowed semantic context is conflicting
and also emits `public-multiple-context`. Errors are `AuditError`; verdict is `PASS` only with zero
errors, every occurrence classified, and every class count complete.

`class_counts` has exactly `retained_private_current`, `tracked_public_current`,
`superseded_historical`, `all_current`, and `all_candidates`. The first, second, and fourth each
have exactly `{resolved, total, status}` with status `complete` iff equal.
`superseded_historical` has exactly `{classified, total, status}` with status `classified` iff
equal. `all_candidates` has exactly `{accepted, total, status}` with status `complete` iff every
discovered occurrence is classified and accepted equals total. Every total, including malformed
and conflicting candidates, is derived from the occurrence scan and is never copied from a public
declaration.

`checks/public-content-hashes-precommit-v<N>.json` and
`checks/public-content-hashes-<candidate-head>.json` have exactly `{schema_version, phase,
candidate_head, candidate_tree, files}`. Version is integer `1`; phase is `precommit` or
`exact-head`; candidate identities and each file's Git blob are null only for precommit. Files are
exactly eleven records `{path, git_blob, sha256, byte_count}` in File Map order; exact-head values
are recomputed from committed blobs; byte count is a nonnegative integer, path is the exact
allowlisted path, and Git blob is a lowercase 40-hex OID when non-null.
`checks/redaction-scan-precommit-v<N>.json` and the exact-head redaction record both have exactly
`{schema_version, scan_kind, candidate_head, candidate_tree, content_manifest_sha256,
denylist_sha256, alias_vocabulary_sha256, scanned_files, exact_matches, portable_matches, matches,
verdict}`. Kind is `precommit` or `exact-head`; candidate values are null only for precommit;
schema version is integer `1`, the three digest fields are lowercase 64-hex, and non-null candidate
identities are lowercase 40-hex;
`scanned_files` is exactly eleven `{path, sha256, byte_count}` records in File Map order matching
the content-hash record; counts are nonnegative integers; matches are exact `{path, match_class,
rule_id, line, matched_sha256}` records with allowlisted path, class `exact` or `portable`, nonempty
rule ID, positive line, and the digest of
the exact matched bytes. `exact_matches` and `portable_matches` equal the corresponding match-class
counts, and verdict is `PASS` only with zero matches. The scan never includes its own digest.

The initial Task 8 exact-head record is `checks/product-git-verification.json`, has
`record_id=product-git-verification`, and is a `ProductGitRecord` with kind `merge-proof`. A later
candidate correction uses the new immutable path
`checks/product-git-verification-<candidate-head>.json` and exact unique
`record_id=product-git-verification-<candidate-head>`; it never overwrites the initial record or a
prior candidate-headed record. Each such record contains the complete fresh Task 8 rerun of every
Step 3.8 command/relationship and owns only streams below
`product-repo/command-streams/<record-id>/`. It cannot cite or reuse a Step 3 stream. These JSON and
stream bytes are late `shared` root artifacts: they are created after the selected generation,
remain outside that immutable generation, are included by the following live-root refresh, remain
retained through the Task 10 decision, and are consumed by the exact-head module review.
`reports/module-change-review-<candidate-head>.json` uses the
product Change Review schema with `review_kind='module-change-review'` and candidate branch
`codex/module6-quietfollow-pilot`; its requirements/check refs include the selected generation,
archive audit, digest-resolution, redaction, and product-Git records. No other recovery-produced
JSON/JSONL shape is permitted. New required JSON needs a plan correction and fresh PLAN review;
untrusted pre-acceptance plan-review JSON files already present in the directory are immutable
historical inputs, tagged `non-credit`, and validated only as exact artifact bytes, never consumed
as a recovery-produced record or execution authority.

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
contains exactly `schema_version=1`, `generation=N`, `recovery_plan`, `inventory_snapshot_ref`,
`inventory_snapshot_sidecar_ref`, `case_ids`, `artifacts`, `current_private_logical_ids`, and
`supersedes_generation`. `case_ids` is the exact
21-case set. `inventory_snapshot_ref` is a `LogicalRef` with kind `check`, null case/attempt, and the
exact logical ID/digest of `checks/root-inventory-snapshot-v<N>.json`;
`inventory_snapshot_sidecar_ref` has the same rules and joins the exact version-matched `.sha256`
sidecar. `artifacts` uses the exact
root artifact schema and equals the immutable snapshot's `artifacts` array byte-for-byte. It thus
includes every actual artifact from every current, superseded, and non-credit attempt (whether
complete or phase-truncated), every Product Change Review/candidate/Git record needed by a public
claim, both quarantined schema-review incidents, the recovery-history record, every forensic and
compliant schema-review target, every N>=3 schema review, and all four group
manifests/reports/reviews. It excludes only the snapshot's exact exclusion
set, including its own bytes/sidecar and the audit that will consume it.
`schema_version`/`generation` are integers, `recovery_plan` is the addendum identity, and `case_ids`
is the fixed sorted array.
`current_private_logical_ids` is the sorted unique array of every generation artifact whose credit
state is `current`; this includes complete current-attempt artifacts and the explicitly current
version of each global retained input/check eligible for later public reference. It contains no
future tracked-public ID or digest: tracked-public claims are created and resolved only against the
later exact candidate blobs. `supersedes_generation` is JSON null for v1 and
integer `N-1` thereafter. Unknown keys, duplicate IDs, wrong ordering, or an artifact outside the
root schema fail validation.

The structural logical IDs are exact: `root-inventory-snapshot-v<N>`,
`root-inventory-snapshot-v<N>-sidecar`, `execution-evidence-manifest-v<N>`,
`execution-evidence-manifest-v<N>-sidecar`, and `execution-evidence-audit-v<N>`. Every structural
ref and pointer uses the corresponding ID; aliases or reused IDs fail.

The exact lifecycle is: (1) close the evidence scope and prohibit further producers; (2) enumerate
and freeze immutable snapshot N plus sidecar using its exact exclusions; (3) create immutable
generation N plus sidecar from only that snapshot; (4) independently audit snapshot N and
generation N; (5) on PASS, replace the pointer to select N; then (6) regenerate the mutable live
root manifest/sidecar so it inventories the snapshot, generation, audit, pointer, and every other
then-current regular file. No step may be reordered. The live manifest is refreshed and validated
again after each Task 7, Task 8, and Task 9 late-record batch and immediately before every consumer
review; it is never an immutable generation input.

After freezing generation N and its exact sidecar, a distinct archive auditor consumes it and writes
`checks/execution-evidence-audit-v<N>.json`; that audit is a separate retained output and is not
required to hash itself or appear in generation N. Its digest never appears publicly. Only after the
audit verdict is PASS may the manifest writer atomically replace `execution-evidence-current.json`,
whose exact keys are `schema_version=1`, `selected_generation=N`, `manifest_sha256`,
`manifest_logical_id`, `audit_logical_id`, `audit_sha256`, and `selected_at_sequence`.
The pointer has no other keys: generation/sequence are positive integers, IDs are unique nonempty
strings joining exact retained generation/audit bytes, and digests are lowercase 64-hex matching
those bytes.
The audit obeys the exhaustive audit schema above.

Any case, product-review, group-review, contamination, or archive-audit correction after freeze
closes a new scope and creates snapshot N+1, generation N+1, and a fresh audit. All N artifacts
remain byte-identical; N+1 includes the new artifacts and all earlier retained attempts/reviews and sets its own
`supersedes_generation=N`. It receives a fresh independent audit. The seven-key mutable pointer is
then replaced to select only N+1 and its exact manifest/audit identities; it stores no supersession
field or history. Public assembly binds only the latest selected generation number/digest. If
public files already exist, a new generation requires a new public assembly commit, a new exact-head
redaction receipt, full checks, and fresh Module Change Review.

### Non-tautological private resolver

At exact candidate head, the private resolver reads the eleven File Map paths from committed Git
blobs and independently scans every byte of all eleven, not only the two JSON records. All files
must be valid UTF-8. The exact raw lexer performs both of these byte-preserving passes over every
blob:

1. emit each case-insensitive boundary-delimited 64-hex candidate matching
   `(?<![0-9A-Fa-f])[0-9A-Fa-f]{64}(?![0-9A-Fa-f])`;
2. at every ASCII case-insensitive label matching `[sS][hH][aA]256:`, emit the maximal immediately
   following payload matching `[A-Za-z0-9._+-]*`, including an empty payload, and retain the exact
   seven-byte label spelling, payload span, and full label-plus-payload claim span. This pass exposes
   alternate-case labels and empty, wrong-length, nonhex, uppercase, or overlong payloads.

JSON blobs additionally undergo a strict structural parse. The resolver visits every value whose
object key is exactly `sha256` or ends in `_sha256`, regardless of its JSON value type, and emits a
`json-sha-key` occurrence from the exact source span. For an unescaped ASCII JSON string, that span
is the payload between quotes and `raw_candidate` is those exact bytes; this lets the raw and
structural discoveries merge. For an escaped string or a non-string value, the span and
`raw_candidate` are the complete JSON value token; an escaped token is `nonhex` and a non-string is
`wrong-type`. Markdown and Python are classified from raw
source bytes; parsing them may locate an allowed annotation or top-level binding but may not discard
any raw candidate. A candidate found by the boundary pass and prefix pass at the same path and exact
payload byte span is one occurrence with merged rules; it retains the prefix pass's exact spelling
and full claim span. Different or overlapping payload spans remain separate. Raw JSON parse failure
is itself an error, but all candidates found by the raw passes are
still reported. Occurrences sort by File Map path order, then `start_byte`, `end_byte`, and
`raw_candidate`. Every lexical/context error identifies its occurrence by public path and exact
span in `AuditError.actual`; parser/schema errors without a candidate still block PASS but do not
invent an occurrence. The complete occurrence list—including uppercase, malformed, unclassified, and
conflicting candidates—is the denominator; public totals, manifest counts, assembler reports, and
deduplicated hash sets are never denominator inputs.

| Public file/context | Required syntax and classification |
|---|---|
| public `manifest.json` | JSON Pointer must match the exhaustive pointer rules below; state/class/logical ID come from the containing record |
| public `execution-record.json` | JSON Pointer must be generation SHA, evidence-ref SHA, predecessor SHA, or another explicitly listed nested SHA field below |
| README, status, validation, five parts | every SHA claim uses exact text ``sha256:<hex> [evidence=<logical-id>;class=<retained-private|tracked-public|superseded-historical>;state=<current|superseded>;kind=<kind>;case=<EID|none>;attempt=<attempt-id|none>]`` on the same line |
| `tests/test_pilot_evidence.py` | a canonical 64-hex literal may occur only as a value in top-level `EXPECTED_PUBLIC_SHA256: dict[str, str]`; its key is the logical ID and its class/state/kind/case/attempt are supplied by top-level `EXPECTED_PUBLIC_SHA256_META` with an exact five-string tuple |

Allowed manifest SHA pointers are `/recovery/plan_sha256`,
`/recovery/evidence_generation_sha256`, `/repository/tracked_product_source_sha256`,
`/repository/tracked_product_test_sha256`, `/snapshots/<index>/sha256`,
`/tracked_bindings/<index>/sha256`, `/parts/<index>/sha256`, `/redaction/denylist_sha256`, and
`/superseded_predecessor_evidence/<index>/sha256`. Allowed execution-record pointers are
`/evidence_generation/sha256`, `/cases/<index>/evidence_refs/<index>/sha256`,
`/cases/<index>/findings/<index>/evidence_refs/<index>/sha256`,
`/cases/<index>/predecessor_evidence/<index>/sha256`, and
`/open_findings/<index>/evidence_refs/<index>/sha256`,
`/metrics/<index>/observation_start/transcript_ref/sha256`, and
`/metrics/<index>/observation_end/transcript_ref/sha256`. Metric pointers must be identical global
retained-private/current/transcript joins to the selected-generation metric log; their sequence
fields must join existing ordered lines and satisfy the public metric arithmetic. No other
JSON/Python/Markdown occurrence is classified. Only a canonical lowercase 64-hex payload may reach
context classification, and any context requiring a prefix additionally requires exact lowercase
`sha256:` spelling. An alternate-case prefix is malformed even when its payload is canonical.
Uppercase bare or prefixed values, prefixed values of the wrong length or with nonhex characters,
and malformed values at SHA-designated JSON keys are
`malformed` even when their surrounding context would otherwise be allowed.

The fixed classification for global JSON fields is: recovery plan =
`tracked-public/current/recovery-plan`; execution generation = `retained-private/current/check`;
tracked product source/test = `tracked-public/current/product-source` or `product-test`; snapshots =
`retained-private/current/raw_input`; each tracked binding and part =
`tracked-public/current/<public_kind>`; denylist = `retained-private/current/check`; and every
predecessor entry = `superseded-historical/superseded/historical-evidence`. All have null
case/attempt. Case/open-finding `EvidenceRef` fields supply their own exact class/state/kind and
case/attempt. Manifest recovery-plan, repository-product, and part logical IDs must be byte-equal to
their corresponding `TrackedBinding.logical_id`; their duplicated digests therefore have one
identical semantic target, not conflicting aliases. Markdown annotations and Python metadata use
the same class/state/kind table; `historical-evidence` is permitted only with
`superseded-historical/superseded`.

For `retained-private/current`, locate exactly one selected generation by recomputing generation
file hashes; join logical ID, case, attempt, private artifact kind, and digest; open its retained
relative path; and recompute size/digest. For `tracked-public/current`, join the public
`tracked_bindings` record and its exact conditional kind/case-attempt mapping, then recompute the
exact candidate blob. For `superseded-historical/superseded`, require presence in the predecessor
array and prohibit current credit; missing historical raw bytes are classified, never counted as
resolved current evidence. Plan/generation/denylist/snapshot/product/global tracked claims follow
their explicit logical ID and class record. The public manifest itself is bound only by the external
exact-head public-content-hash record, avoiding self-hash.

Reject: any malformed or unclassified occurrence; unresolved current occurrence; logical ID with different
digests or semantic tuples across occurrences; one occurrence matching multiple contexts; a
retained-private claim absent from the selected generation; a tracked-public claim absent from the
exact candidate; private path/native ID in public metadata; superseded claim presented as current;
current artifact presented as superseded; wrong kind/case/attempt; or an unreferenced current case
artifact required by the private schema. Equal byte digests under different logical IDs are allowed
only when their semantic mappings remain non-conflicting. Emit the exhaustive
`digest-resolution-v<N>.json` schema above and require both all-current and all-candidates counts
complete.

### Tracked public successor schemas

The tracked `tests/fixtures/quietfollow/evidence/manifest.json` has exactly these top-level keys:
`schema_version`, `module`, `recovery`, `repository`, `snapshots`, `permissions`, `roles`,
`tracked_bindings`, `parts`, `redaction`, `superseded_predecessor_evidence`, and `limitations`.
Unknown keys fail validation. Its exact nested contracts are:

| Field | Exact nested schema |
|---|---|
| `schema_version`, `module` | integer `2`; literal `MODULE6-PLAN-v1` |
| `recovery` | `{plan_identity, plan_logical_id, plan_sha256, predecessor_candidate_head, predecessor_evidence_state, predecessor_evidence_reason, evidence_generation, evidence_generation_logical_id, evidence_generation_sha256}`; identities are nonempty, predecessor head is 40-hex, state is `superseded`, generation positive, digests 64-hex; logical IDs join exact plan/generation bytes |
| `repository` | `{candidate_identity, disposable_repository_kind, disposable_merged_commit, disposable_merged_tree, product_test_result, tracked_product_source_logical_id, tracked_product_source_sha256, tracked_product_test_logical_id, tracked_product_test_sha256}`; kind is `local-synthetic`; Git IDs are 40-hex; `product_test_result` is exactly `{passed, failed, scope}` with nonnegative integers, passed 15, failed 0, and scope `exact-disposable-merged-tree` |
| `snapshots[]` | exactly `{logical_id, source_class, sha256, byte_count}`; class is `tracked-binding`, `legacy-private-input`, or `synthetic-fixture`; size nonnegative; each logical ID joins selected-generation bytes |
| `permissions` | exactly `{allowed, forbidden, external_actions_performed, public_alias_vocabulary}`; allowed/forbidden are disjoint `StringEffectSet`; external flag is false; vocabulary is the sorted unique exact alias set declared in the role table, with no native IDs |
| `roles[]` | exactly `{alias, requested_model, requested_reasoning, accepted_native_assignment, independently_verified_runtime_fact}`; one sorted unique record for every role that produced or reviewed current credited evidence and no unused role; alias is in vocabulary; requested pair equals role table; fact strings are `Unknown` absent authoritative receipts |
| `tracked_bindings[]` | exact `TrackedBinding` below; exactly thirteen bindings for the ten non-manifest candidate files plus corrected addendum and two read-only product files |
| `parts[]` | exactly `{id, logical_id, path, sha256, current_case_attempts}`; IDs/paths are the fixed five-part mapping; case-attempt records match current public cases and the corresponding tracked binding |
| `redaction` | exactly `{policy_version, denylist_logical_id, denylist_value_count, denylist_sha256, exact_value_matches, portable_pattern_matches, final_receipt_scope}`; version 1, counts nonnegative with both matches zero, receipt scope literal `ignored exact-head review evidence`; ID/digest join the selected generation's current versioned denylist and value count equals its independently counted lines; no scan path/digest |
| `superseded_predecessor_evidence[]` | exactly `{logical_id, sha256, state, reason}`; state `superseded`, reason nonempty; these claims never receive current credit |
| `limitations` | array of nonempty unique strings |

`TrackedBinding` has exactly `{logical_id, path, public_kind, sha256, case_attempts}`.
`public_kind` is `public-part`, `execution-record`, `navigation`, `validation`, `evidence-test`,
`recovery-plan`, `product-source`, or `product-test`. `case_attempts` is an ordered array of exact
`{case_id, attempt_id}` records; it is empty only for the global recovery plan and otherwise names
every current case represented by that file. Path/digest resolve the exact candidate blob. The
manifest itself is excluded to avoid a digest fixed point and is bound by the ignored exact-head
content record. The five part bindings have exactly these case sets; every record uses the case's
current attempt:

| Part binding | Exact cases |
|---|---|
| `part-1-discovery` | E38 |
| `part-2-readiness` | E31, E39 |
| `part-3-delivery` | E12, E14 |
| `part-4-release-rehearsal` | E13, E27, E28 |
| `part-5-resume-scaling` | E02, E08, E10, E11, E17, E20, E21, E22, E25, E33, E34, E37, E41 |

README, status, validation, execution-record, and evidence-test bindings map all 21 current
case-attempt pairs; product source/test map E12, E13, E14, E27, E28; recovery plan maps none. A
tracked-public case reference is valid only when its `kind` equals binding `public_kind` and its
case/attempt occurs in that binding. This is the sole tracked-public kind/case/attempt conversion.

The tracked `tests/fixtures/quietfollow/evidence/execution-record.json` has exactly these top-level
keys: `schema_version`, `harness_identity`, `evidence_generation`, `cases`, `verdict_totals`,
`resolution_summary`, `metrics`, `open_findings`, `reruns`, `mechanical_test_limitation`, and
`overall_limitation`. Unknown keys fail validation. Version is integer `2`; `harness_identity` is
exactly `{plan_identity, recovery_plan_identity, predecessor_candidate_head, candidate_state}` with
literal plan identities, 40-hex predecessor, and state `local-synthetic-unintegrated`;
`evidence_generation` is exactly `{number, logical_id, sha256}` matching manifest recovery.

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
`mode_detail`, `actual_outcome`, and `dependent_action_state` are nonempty strings. Side-effect
arrays are disjoint `StringEffectSet`; executor aliases are a nonempty unique subset of public alias
vocabulary; evaluator alias is in vocabulary and absent from executor aliases. Assignment arrays
use public `AssignmentRequest`, `{role_alias, value}` accepted records, and `{role_alias, value}`
runtime records, with identical role sets and `Unknown` defaults. Verdict is `PASS`, `FAIL`, or
`BLOCKED`.

Public `EvidenceRef` has exactly `{logical_id, kind, digest_class, sha256, state, case_id,
attempt_id}`. Digest class is `retained-private` or `tracked-public`; state is always `current`
(historical refs use the separate predecessor schema). For `retained-private`, kind is one of
`raw_input`, `executor_prompt`, `bundle_manifest`, `executor_output`, `result_record`,
`executor_operation_snapshot`, `executor_session_snapshot`, `rubric_section`,
`evaluator_input`, `evaluator_prompt`, `evaluator_output`, `transcript`, or `session_receipt`, and
the full tuple joins one selected-generation artifact. Case and attempt are null only for the one
global metric transcript ref; that ref has kind `transcript` and joins
`transcripts/metrics/coordination-observation.jsonl`. For `tracked-public`, kind is one
`TrackedBinding.public_kind`, and the tuple joins its `case_attempts` mapping. The five kinds
`raw_input`, `executor_output`, `evaluator_input`, `evaluator_output`, and `transcript` are nonempty
per case; the private complete-attempt schema additionally requires all thirteen exact families,
including both immutable executor snapshots and the isolated rubric section.

Each case `findings[]` record has exactly `{id, severity, state, summary, evidence_refs}`; severity
is `Critical`, `Important`, or `Minor`; state is `open` or `resolved`; refs are nonempty
`EvidenceRef` arrays. Each `rerun_history[]` record has exactly `{attempt_id, credit_state,
terminal_phase, terminal_reason, supersedes, correction_reason, evaluation_verdict,
dependent_action_state, retained_artifact_logical_ids}`. State/phase/reason and predecessor fields
equal the private attempt contract. Retained IDs are the sorted union of the attempt's thirteen family
arrays, so every actual artifact is represented and no nonexistent artifact is named.
Verdict/dependent state are non-null and equal valid evaluator-output bytes iff such bytes exist;
both are null when the attempt ended before a valid evaluator result or its result is
malformed/corrupt. Current/superseded entries must be `evaluator-closed`/`complete` with non-null
verdict/state; only non-credit may use a partial terminal phase. The nonempty array lists every
retained attempt in sequence and ends with exactly one current attempt. `predecessor_evidence[]` is
nonempty and has exact
`{logical_id, sha256, state, reason}` records with state `superseded`.

`verdict_totals` has exactly integer `PASS`, `FAIL`, `BLOCKED`, and `total`; tests recompute these
from `cases`. `resolution_summary` has exactly `retained_private_current`,
`tracked_public_current`, `superseded_historical`, and `all_current`. The first, second, and fourth
use exact `{resolved, total, status}` with nonnegative integers and status `complete` iff equal;
the historical record uses exact `{classified, total, status}` with status `classified` iff equal.
These are public consistency claims recomputed from public occurrences, not private proof. `metrics`
is an array with exactly one record for each of `manual_owner_relay_events`,
`duplicate_owner_approval_prompts`, `duplicate_user_owned_task_creations`,
`duplicate_internal_work_launches`, `invalid_pass_uses`, and `incorrect_transitions`; each record
has exactly `{name, value, unit, observation_start, observation_end, denominator, exclusions}`.
Value is a nonnegative integer and `unit='event'`. A `MetricBoundary` is exactly
`{transcript_ref, sequence}`: the ref is the same global retained-private/current/transcript
`EvidenceRef` to `transcripts/metrics/coordination-observation.jsonl`, and sequence is a positive
integer joining an exact line. Start and end share one transcript and start sequence must be less
than or equal to end sequence; their lines have event kinds `observation-start` and
`observation-end`, respectively. `denominator` has exactly `{eligible_event_count, definition}`;
count is nonnegative and definition is the literal `inclusive retained events minus declared
exclusions`. `exclusions` is a sorted unique array of exact `{event_sequence, reason}` records;
each sequence lies inside the interval, joins an actual non-boundary line, and has a nonempty
reason. Eligible count equals non-boundary events in the inclusive interval minus exclusions, and
value equals the remaining events whose `event_kind` is that metric name. A missing/wrong-kind/
wrong-digest transcript, nonexistent line, swapped interval, duplicate exclusion, or arithmetic
mismatch fails the corresponding portable shape/join or exact private byte validation; portable
tests never open the ignored log. `open_findings[]` has exactly `{id, severity, state,
summary, evidence_refs}` with severity `Critical`, `Important`, or `Minor`, state exactly `open`,
and evidence refs exact `EvidenceRef` records (case/attempt may be null only for a
global tracked/private claim). `reruns[]` has exactly `{case_id, current_attempt_id,
prior_attempt_ids}`; it contains exactly the ordered cases with at least one prior attempt, and prior
IDs are ordered and equal that case's non-current rerun-history IDs.
The two limitation fields are nonempty strings.

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
directories. It produces one version-matched `reports/<group>-manifest-v<N>.json`, Markdown group
report, and independent `reports/<group>-review-v<N>.json`. No group writer updates the root
manifest or public files. Parallel dispatch may begin only after a valid fresh N>=3 schema-review
PASS and after the Task coordinator confirms the same exact v3 schema `LogicalRef` and v3
binding-snapshot `LogicalRef` in all four v3 briefs. A quarantined v1/v2 review, forensic target,
test count, or structurally passing CLI fixture never opens this gate. `delivery-release` is the
only group whose workflow may write `product-repo/**`;
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

Every alias below is a stable role alias. Every dispatch receives a new globally unique private
`session_alias`, including a correction or fresh re-review that reuses the same stable role alias;
distinctness is proven by the retained case receipt or review record, never by inventing a new
public alias. Requested assignment is recorded before dispatch. Accepted native assignment and
runtime fact remain `Unknown` unless separate authoritative receipts establish them.

| Role aliases | Requested model/reasoning | Allowed write location | Responsibility and transfer rule |
|---|---|---|---|
| `plan-author` | `gpt-5.6-sol/high` | this tracked addendum during plan-history commits; ignored `plan-author-report*.md` only | Plan-only writer; relinquishes tracked ownership before PLAN review or recovery execution. |
| `task-coordinator` | `gpt-5.6-sol/high` | append-only `progress.md`; otherwise dispatch/state only | Relinquishes `progress.md` before each required immutable pre-append snapshot, resumes append-only ownership only after the root writer closes it, and never cites the mutable ledger as permanent exact evidence. Never materializes another role's output. |
| `schema-binding-writer` | `gpt-5.6-sol/medium` | `inputs/binding/**`, fixed working candidates `checks/archive-validator.py`, `checks/archive-validator-tests.py`, `checks/build-live-manifest.py`, `checks/bundle-contamination.json`, `checks/public-alias-vocabulary.txt` and sidecar, four group briefs | May correct fixed Task 1 candidates only between schema reviews; closes and relinquishes every fixed candidate before the root writer makes an immutable review target. Never writes `review-targets/**`, recovery history, or a review report. |
| `root-manifest-writer` | `gpt-5.6-sol/medium` | root `manifest.json`/`manifest.sha256`, immutable `history/progress-ledger-snapshot-v<N>.md`, `checks/root-inventory-snapshot-*`, `checks/execution-evidence-*`, `checks/digest-resolution-*`, `checks/task1-schema-review-recovery-history-v1.json`, `review-targets/**`, `reports/task1-schema-review-v<N>.json`, and non-case raw receipts under `transcripts/roles/**` | Only root/inventory/snapshot/generation and schema-review-target/history writer. Before ledger ownership returns, copies/verifies/locks the exact pre-append ledger bytes without editing the source. Sequentially receives closed fixed candidates, copies/hashes/locks each review-specific target, refreshes the live inventory, materializes the reviewer return, then refreshes again. Never edits a fixed candidate, mutable ledger, or old target/review. |
| `redaction-check-recorder` | `gpt-5.6-sol/medium` | only versioned `checks/prebound-public-sessions-v<N>.json`, optional `checks/prebound-public-session-receipts/**`, `checks/private-denylist-v<N>.txt` and sidecar, `checks/public-content-hashes-precommit-v<N>.json`, and `checks/redaction-scan-precommit-v<N>.json` | Establishes its own and assembler bindings before generation freeze, records every disclosed private binding, and performs precommit scans; never edits public bytes. |
| `metric-observation-recorder` | `gpt-5.6-sol/medium` | only append-only `transcripts/metrics/coordination-observation.jsonl` | Serializes actual in-scope coordinator-visible events in sequence; writes no aggregate, case, or public byte and relinquishes ownership before evidence-scope close. |
| `discovery-recorder`, `resume-recorder`, `coordination-recorder` | `gpt-5.6-terra/medium` | only their exact disjoint group `inputs/`, `executions/`, `evaluations/`, `transcripts/`, and `reports/*` roots | Materialize neutral fixtures and immutable payloads returned by executors/evaluators/reviewers; never write another group. |
| `delivery-recorder` | `gpt-5.6-terra/medium` | delivery group `inputs/`, `executions/`, `evaluations/`, `transcripts/`, `reports/delivery-release-*`, `product-repo/reviews/**`, `product-repo/rehearsals/**` except `seed-oracle-v1.json`, and `product-repo/command-streams/**` except `seed-oracle-v1/**` | Materializes delivery role/reviewer payloads and exact command streams; never writes `product-repo/repository/**` or the seed oracle paths. |
| `E02-executor`, `E08-executor`, `E10-routing-executor-1`, `E10-routing-executor-2`, `E11-executor`, `E12-executor`, `E13-executor`, `E14-executor`, `E17-executor`, `E20-executor`, `E21-executor`, `E22-executor`, `E25-executor`, `E27-executor`, `E28-executor`, `E31-executor`, `E33-executor`, `E34-executor`, `E37-executor`, `E38-executor`, `E39-executor`, `E41-executor` | `gpt-5.6-sol/high` | no direct workspace write; returns exact prompt-bound payload to owning recorder | Fresh case/discovery/coordination execution; E13, E27, and E28 are necessarily three different sessions/artifacts. |
| `wi1-writer`, `wi2-writer`, `correction-writer`, `whitespace-writer` | `gpt-5.6-sol/medium` | `product-repo/repository/**` on assigned branch interval only | Ordinary product writer. Repository ownership transfers sequentially; no concurrent Git writer. |
| `seeded-fixture-preparer` | `gpt-5.6-terra/medium` | `product-repo/repository/**` during S interval, `product-repo/rehearsals/seed-oracle-v1.json`, and `product-repo/command-streams/seed-oracle-v1/**` | Receives ownership after C and relinquishes it before review; small deliberate test fixture only. |
| `architecture-analyst`, `architecture-reviewer` | `gpt-6-astra/high` | no direct workspace write; returns exact payload to `coordination-recorder` | Analyst and reviewer are distinct; reviewer receives requirements/candidate independently. |
| `E02-evaluator`, `E08-evaluator`, `E10-evaluator`, `E11-evaluator`, `E12-evaluator`, `E13-evaluator`, `E14-evaluator`, `E17-evaluator`, `E20-evaluator`, `E21-evaluator`, `E22-evaluator`, `E25-evaluator`, `E27-evaluator`, `E28-evaluator`, `E31-evaluator`, `E33-evaluator`, `E34-evaluator`, `E37-evaluator`, `E38-evaluator`, `E39-evaluator`, `E41-evaluator` | `gpt-5.6-sol/high` | no direct workspace write; returns exact JSON payload to owning recorder | One distinct evaluator per case, never its executor; specifically E13/E27/E28 have three distinct evaluators. |
| `wi1-change-reviewer`, `S-change-reviewer`, `R-change-reviewer`, `B-change-reviewer` | `gpt-5.6-sol/high` | no direct workspace write; returns review payload to `delivery-recorder` | Fresh full product Change Review of the exact named head. |
| `schema-reviewer`, `discovery-group-reviewer`, `delivery-group-reviewer`, `resume-group-reviewer`, `coordination-group-reviewer`, `archive-auditor`, `module-change-reviewer`, `plan-reviewer` | `gpt-5.6-sol/high` | no direct workspace write; return payload to current recorder/root writer | Independent requirements/candidate review; no author conversation. |
| `public-assembler` | `gpt-5.6-sol/medium` | only eleven tracked candidate paths plus `reports/public-assembly-report-v<N>.md` | Sole tracked writer; its session is prebound before generation freeze, but tracked ownership begins only after selected archive audit PASS and ends at candidate commit. |
| `exact-head-check-recorder` | `gpt-5.6-sol/medium` | ignored `checks/public-content-hashes-<candidate-head>.json`, `checks/redaction-scan-<candidate-head>.json`, initial `checks/product-git-verification.json` or successor `checks/product-git-verification-<candidate-head>.json`, respectively `product-repo/command-streams/product-git-verification/**` or `product-repo/command-streams/product-git-verification-<candidate-head>/**`, `reports/task9-report-<candidate-head>.md`, `reports/module-change-review-<candidate-head>.json`, `reports/task9-recommendation-<candidate-head>.md` | Sole sequential Task 8 recorder; reruns read-only Git commands, materializes their new exact streams/record after the selected generation, closes all late bytes before live-root refresh, and cannot edit tracked or frozen-generation bytes. |

Agent payloads are immutable return values; only the designated recorder materializes them under
its allowed directory and hashes the exact bytes. Each ownership handoff is an ordered event in the
relevant `operations.jsonl` or product Git record. A writer must close, hash, and relinquish its
scope before the next sequential owner begins. Parallel work is limited to the four recorders'
disjoint directories after Task 1; reviews, root aggregation, public assembly, and product Git
ownership are sequential.

## Task 1: Freeze durable schemas, binding inputs, and contamination checks

**Files:**

- Preserve every existing Task 1 byte; create only versioned binding-set v3, forensic/review
  targets, the mandatory immutable progress-ledger snapshot, recovery history, new RED evidence,
  and successor review records at the paths above.
- Correct the validator, validator tests, and live-manifest builder fixed working files only after
  their current bytes have been preserved in the v2 forensic target.
- Do not modify tracked files.

**Interfaces:**

- Consumes: accepted correction-round-9 addendum commit, exact predecessor identities, current
  tracked binding files, Task 1 reports v1-v3, schema reviews v1/v2, and current fixed validator/
  live-manifest-builder bytes, the exact pre-append `progress.md` precondition, and verified absence
  of binding sequence 2.
- Produces: honest quarantined history, immutable forensic and N>=3 review targets, corrected exact
  schemas, binding set v3, four v3 briefs, a complete physical CLI fixture, and a fresh schema-review
  PASS gate before any group dispatch.

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
  git rev-parse 8a9f04bcb2d15a1127dcbd1f354ab66accd2e5b6^
  git rev-parse f40c37e8e2bed1309605b9b0e8f17046699fa6af^
  git rev-parse fde1b8cfe14f526bdd6561ed4309df1975dddc77^
  git rev-parse 134b90585991ecfa253c3de028142acaea6c301c^
  git rev-parse 169237b48c36870e9bc7a1defcb3d996958a72d2^
  git rev-parse d3c0369ce38142832a7347c1ead1140945b2fedd^
  git rev-parse 231638b69051ef52b46902c3d309a52d7852b803^
  git rev-parse e5b2ef7af65c5c6381a70e7f0327d2fe8c338b3d^
  git diff --name-only e5b2ef7af65c5c6381a70e7f0327d2fe8c338b3d...HEAD
  ```

  Expected: `HEAD` is the accepted addendum commit; its sole parent is
  `e5b2ef7af65c5c6381a70e7f0327d2fe8c338b3d`; correction round 8's sole parent is
  `231638b69051ef52b46902c3d309a52d7852b803`; correction round 7's sole parent is
  `d3c0369ce38142832a7347c1ead1140945b2fedd`; correction round 6's sole parent is
  `169237b48c36870e9bc7a1defcb3d996958a72d2`; correction round 5's sole parent is
  `134b90585991ecfa253c3de028142acaea6c301c`; correction round 4's sole parent is
  `fde1b8cfe14f526bdd6561ed4309df1975dddc77`; correction round 3's sole parent is
  `f40c37e8e2bed1309605b9b0e8f17046699fa6af`; correction round 2's sole parent is
  `8a9f04bcb2d15a1127dcbd1f354ab66accd2e5b6`; correction round 1's sole parent is
  `21c1509dce231069e1ec49dd36d751ff85999e08`; the initial addendum's sole parent is
  `b0e0c85dd0bf50e84ba1ce14ed4a985be7676002`; tracked state is clean; predecessor plan digest is
  `6037149b9a70cdeba4b8f1fd4fcce460b9206730665c8aa69f4ee781eb5c4777`; the
  parent-to-head path set is only this addendum. Stop before writes if any check differs.

  This is the first recovery write and precedes every progress append or other mutation. Verify
  `plan-review-v7.json` at SHA-256
  `7d234a640d4d51064a7d0c17485c5166189ab619cd7dc053eff9b6b9b1e65f6b` and
  `plan-review-v8.json` at SHA-256
  `07f37acba8160b362920989ebbfc3af4db2ff4caae7d3a48f6899602e431990b` and
  `plan-review-v9.json` at SHA-256
  `9034740d0111a9edf5b2b47a8e9cd6ca61b1f3082d49f3087381f4f402011c76`. Before writing any
  recovery byte, independently require all six reserved binding-v2 paths in the exact recovery-
  history array to be absent; any present v2 path blocks as fabricated history and must not be
  deleted or adopted. The task coordinator
  relinquishes `progress.md`; the root writer requires it to be a regular 18,640-byte file at
  SHA-256 `5e50255f613334839560b676c2bf2dbe7a9fe05a2f01bbd135842385d2e22f2b`, copies its exact bytes
  to `history/progress-ledger-snapshot-v1.md`, verifies source/copy byte equality, size, and digest,
  assigns the exact `progress-ledger-snapshot-v1` artifact record above, and changes only the copy
  to mode `0444`. It then writes the snapshot binding into the recovery-history record. Any source
  mismatch blocks without reconstruction or progress mutation. Only after the immutable copy is
  closed may append-only ownership of `progress.md` return to the coordinator; the mutable file is
  never again an exact historical target.

  Before any fixed Task 1 candidate is edited, verify exact current hashes
  `e66c20dadbf1d26df13e654a45b1406fd22062913133a5d89ce027429bdb6392` for
  `checks/archive-validator.py` and
  `3b883a5a35e33a3ab325c400096b5eaf7bdbdc4103f652e55aab451cb5038eac` for
  `checks/archive-validator-tests.py`, plus
  `5b5df5454edacbbcca5c998bc78c7caa2c5b63e480cad6dfda8649f48b8ccbb9` for
  `checks/build-live-manifest.py`. Transfer ownership to `root-manifest-writer`; copy those exact
  bytes to the three v2 forensic target paths, verify byte equality, assign the two unique validator
  forensic IDs and the preserved builder ID defined above, make the copies read-only, and write the
  exact recovery-history record. Also verify the two
  historical review digests, all five declared ref-pointer values, and all 24 finding-label pointer
  values. Do not invoke the known-defective
  live-manifest builder or claim an honest refreshed inventory yet; no consumer may use the stale
  live manifest during this closed correction interval. After the root writer relinquishes its
  forensic/history output roots, the task coordinator transfers the three fixed code paths to
  `schema-binding-writer` for Step 1.2. A hash mismatch is `PLAN_BLOCKED`; do not overwrite or infer
  replacement bytes.

- [ ] **Step 1.2: Extend archive-validator tests with recovery and exhaustive fixture cases first.**

  Extend ignored `checks/archive-validator-tests.py`. Its valid physical CLI fixture must contain
  `inputs/binding/binding-snapshot-manifest-v3.json` and its exact source/copy bytes; all 21 cases;
  every required per-attempt filename/category; all four groups; a fully enumerated actual tree;
  a valid sidecar; all thirty previously defined recovery JSON/JSONL families plus the new
  recovery-history family (31 total); and a valid instance of every nested record and every
  producer/consumer join defined above. A fixture missing either the binding snapshot or any
  registered family is invalid and must exercise the same validation path, never a reduced mode.
  Write separate negative tests for: unknown/missing/wrong-type keys at every
  schema level; an actual unlisted file; a declared missing file; duplicate path; duplicate logical
  ID; absolute, empty, backslash, `//`, `.`, and `..` paths; symlink file; symlink ancestor; FIFO or
  other special node where the platform permits; escaped root; digest, byte-count, empty-file, and
  sidecar mismatch; duplicate/missing case; wrong group; zero/two current attempts; skipped or
  duplicate attempt sequence; bad supersedes edge; current logical ID joining wrong case, attempt,
  kind, or credit state; every terminal-phase/reason combination; a missing `R` family, an invented
  `O` family, a forbidden later-phase family, a current/superseded incomplete attempt, a non-credit
  `complete` attempt, an omitted actual non-credit artifact, and a fabricated output/evaluator/
  receipt file; a missing executor operation/session snapshot; evaluator input referencing the
  later mutable final transcript/receipt; stale snapshots whose declared closure sequence precedes
  the actual executor terminal event; a final transcript whose executor prefix differs by one
  byte; a final session prefix that changes/reorders an executor session; a snapshot containing a
  future evaluator event; missing/wrong-kind/wrong-digest rubric ref; non-unique/wrong rubric
  heading extraction; normalized or altered rubric bytes; rubric path or exact bytes inside the
  executor bundle; receipt aliases that are not
  distinct; accepted/runtime receipt mismatch; bundle unlisted/missing/symlink file; bundle and
  prompt digest mismatch; forbidden logical kind; forbidden exact bytes in any listed or unlisted
  bundle file and in `executor-prompt.txt`; selected-generation digest/number mismatch; and public
  resolution whose summary count lies or whose logical reference has no exact filesystem byte.
  For public contracts, mutate every nested record once, every enum once, every required
  resolution-summary key once, retained/tracked conditional kinds, tracked part case/attempt maps,
  public finding/rerun/evidence refs, and all eleven allowed SHA contexts. Add failures for an
  unclassified Markdown/Python/JSON digest, conflicting duplicate logical ID, and
  superseded-as-current claim. Define exact test constants `L64 = "a" * 64`, `U64 = "A" * 64`,
  `G64 = "g" * 64`, and `L65 = "a" * 65`. In each Markdown, JSON raw-text/string, and Python
  source context add exactly `SHA256:abc`, `Sha256:`, `sHa256:` + `L64`, `SHA256:` + `U64`,
  `Sha256:` + `G64`, and `SHA256:` + `L65`. The expected prefix status is `alternate-case` for
  every form; payload statuses are respectively `wrong-length`, `wrong-length`, `canonical`,
  `uppercase`, `nonhex`, and `wrong-length`. Also retain the lowercase-label cases for an uppercase
  payload and wrong-length/nonhex/empty payloads, an uppercase boundary-delimited bare digest, and
  uppercase/malformed strings and non-string values at every SHA-designated JSON key shape. Assert
  every form creates an occurrence with exact original prefix/payload/full-claim spans, emits at
  least one error, and increments `all_candidates.total`; assert alternate-case plus a canonical
  64-hex payload merges with the independent boundary-pass occurrence but remains malformed.
  Add the paired alias
  allow/reject corpus from Task 7.1.
  Add failures for a nonexistent/wrong-kind/wrong-digest schema or binding ref; generation/snapshot
  mismatch; stale mutable live manifest after every late-record phase; missing ProductGit stdout or
  stderr, a fabricated stream declaration, wrong command-stream digest, and a legitimate empty
  stream incorrectly rejected; reused Step 3 streams or duplicate Task 8 record ID; and metric nonexistent/wrong-kind/wrong-digest transcript,
  nonexistent line, swapped boundaries, duplicate exclusion, or mismatched denominator/value.

  Add `HistoricalSchemaReviewRecoveryTests` with exact tests that: the two review files match the
  fixed incident digests; v1's two missing targets are represented without invented files; v2's
  two present candidates join only the forensic identities; v2's `/check_refs/2` retains its wrong
  historical kind but joins the review incident only through the exact quarantine metadata; the 24
  enumerated finding labels use only their incident-local basis and all other v1/v2 refs and finding
  labels still join globally; a changed path/digest/pointer/value, omitted label, or extra exception
  fails; deleting or changing the recovery-history record fails; and duplicate declared historical
  IDs do not enter the actual artifact-ID set. Add the general no-bypass matrix: for each verdict `PASS`, `CHANGES_REQUIRED`,
  and `BLOCKED`, a synthetic N>=3 review with one missing, wrong-kind, or wrong-digest candidate,
  requirement, check, or finding-evidence ref must fail. The only passing legacy exceptions are the
  five exact path/review-digest/JSON-pointer/ref tuples and their 24 exact incident-local finding
  labels above.

  Add `ProgressLedgerSnapshotTests`: v1 passes only with the exact source/copy digest and byte
  count, byte equality captured before mutation, `0444` mode, prescribed root ID/kind/producer/
  credit state, recovery-history and N>=3 requirements-ref joins, inventory/generation/audit
  membership, and absence of mutable `progress.md` from an immutable snapshot. Separately fail a
  missing, changed, writable, wrong-size, wrong-digest, duplicate-ID, or reconstructed v1 copy; a
  source changed before capture; a recovery/review ref to `progress.md` or `progress-live-ledger`;
  an immutable inventory that includes the mutable ledger or excludes the immutable copy; and any
  selected generation/audit that omits the copy. After capture, advancing only the live ledger must
  pass historical validation and make the live manifest stale until its next regeneration.

  Add `BindingSequenceHistoryTests`: the only valid sequence-2 state is the exact
  `not-materialized` nested recovery-history record with zero artifacts/IDs, no dispatch or
  generation credit, the exact plan-review-v7 binding, and all six reserved paths absent. Fail any
  missing/extra/wrong-key record, different reason/state/review binding, nonzero count, nonempty ID
  list, phantom `LogicalRef`, root classification, generation member, inventory declaration, or
  any fabricated v2 path/byte. The positive fixture builds complete active v3 directly from the
  verified v1 snapshot entries plus accepted-plan v3 source/copy bytes, generates four v3 briefs
  from the exact partition and v3 refs, requires every v3 snapshot-entry equality and all six v3
  root-artifact joins, and makes every schema/group/downstream ref use binding sequence 3. Fail
  incomplete v3, a v3 ref aimed at v1/v2, or an attempt to backfill sequence 2. The
  `task1-schema-review-v2-forensic` paths remain valid forensic review targets and must not match the
  binding-v2 reserved-path rule.

  Add `Task1BindingLifecycleOrderTests` with two separate roots, never a phase switch in one
  validator invocation. The synthetic root is a complete physical fixture containing valid v1/v3,
  absent sequence 2, every one of the 31 families, and every join consumer; the ordinary CLI and
  every validator run against it and must pass. The actual-root sequence must prove: the strict CLI
  returns a required-artifact/binding error before v3 exists; Step 1.5 neither invokes that actual-
  root validation nor marks its live manifest current; no consumer review or dispatch is admitted
  in the closed pre-v3 interval; a complete source/copy/brief-joined v3 followed by a regenerated
  `task1-history-recovered` live manifest passes the same always-invoked CLI; and this post-v3 PASS
  is required before target freeze. Fail an incomplete v3, a phase value set to
  `task1-history-recovered` before v3, a review/dispatch attempt in the closed interval, any skipped
  validator, or any fixed/history/binding/live-root mutation between the post-v3 PASS and Step 1.8.
  There is no `pre-v3`, `fixture-only`, or other relaxed `as_of_phase` enum and no conditional
  validator bypass.

  Add one focused regression for each of the seven schema-review-v2 findings: freeze-time complete
  set/symlink-ancestor containment; every nested semantic and cross-artifact join; all verdict
  review/audit identity and target joins; complete public current/history/metric/global-binding
  resolution; all twelve forbidden JSON keys; schema-review root kind/producer/logical ID; and
  wholly plan-valid positive/end-to-end fixtures. The end-to-end physical CLI fixture must invoke
  `validate_root_schema`, `validate_inventory`, `validate_case_joins`,
  `validate_attempt_artifact_contracts`, `validate_recovery_files`, and
  `validate_selected_generation` unconditionally; assert a missing binding snapshot is a
  `required-artifact` error rather than a branch that skips the latter three validators.
  Add a live-manifest-builder regression that assigns the exact incident IDs/kinds/producers above,
  gives every later N>=3 target/review its prescribed classification, and never reuses
  `checks-build-live-manifest` for the corrected fixed builder.

- [ ] **Step 1.3: Run and retain the correction-round RED.**

  Run:

  ```bash
  python3 -B .superpowers/sdd/2026-09-12-module-6-evidence-retention-recovery/checks/archive-validator-tests.py
  ```

  Expected: FAIL because the current validator still bypasses full recovery validation when the
  binding snapshot is absent, has no exact recovery-history/review-target schema, permits a broad
  non-PASS review-ref bypass, has no absent-sequence-2/direct-v1-to-v3 binding contract,
  misclassifies schema review/builder evidence, and retains the seven v2
  review defects. Capture exact stdout/stderr
  and exit in new immutable `checks/archive-validator-correction-red-v4.txt`; do not overwrite the
  three existing RED logs or any report/review byte.

- [ ] **Step 1.4: Repair the ignored validator, resolver, and live-manifest builder to the exact contract.**

  `archive-validator.py` defines constants for the exact 21-case set, fixed group partition, exact
  key sets, enums, terminal-phase/reason family matrix, the live-root two exclusions, the immutable
  snapshot nine exclusions, the mandatory progress-snapshot identity, the two exact historical
  incidents/five quarantined refs, and contamination
  denyset. Implement concrete functions named `actual_inventory`, `validate_root_schema`,
  `validate_inventory`, `validate_case_joins`, `validate_executor_snapshots`,
  `extract_rubric_section`, `validate_bundle`, `validate_generation`,
  `validate_progress_ledger_snapshot`, `validate_binding_sequence_history`,
  `validate_schema_review_recovery_history`,
  `validate_schema_review_target`,
  `discover_public_sha_candidates`, and `resolve_public_current`, with these mandatory algorithms
  and no manifest-derived shortcuts.
  `actual_inventory`
  recursively uses `os.scandir` plus `lstat`, errors on every symlink/special/unresolved/escaped
  node, hashes all regular files except exactly the applicable live-root or snapshot exclusion set,
  and returns the independently
  observed path/size/digest map. `validate_root_schema` enforces every exact key/type/enum in this
  plan. `validate_inventory` requires exact equality of actual and declared path sets plus unique
  logical IDs/paths and exact byte count/digest/nonempty policy. `validate_case_joins` derives the
  current attempt, phase-conditional kind coverage, every actual attempt's files, and role/session
  relationships by joining each logical
  ID to exactly one artifact; it never reads a declared count or kind summary.
  `validate_executor_snapshots` enforces the exact transcript byte-prefix and receipt array-prefix
  relationships and rejects any evaluator event in either immutable snapshot.
  `extract_rubric_section` implements the exact byte-offset algorithm above and compares those
  bytes/digest/path to the declared rubric artifact. `validate_bundle`
  enumerates its physical root independently and scans every actual byte plus the separately hashed
  prompt. `validate_generation` recomputes snapshot, generation, and sidecar identities; requires
  generation artifacts to equal snapshot artifacts; and checks every current/superseded/non-credit
  attempt's actual membership while deriving semantic counts only from complete current attempts.
  `validate_progress_ledger_snapshot` requires the immutable copy's exact v1 identity, bytes, size,
  mode, artifact join, recovery-history binding, N>=3 schema-review requirements join, and selected
  generation/audit membership while forbidding the mutable ledger from immutable inventories or
  permanent refs; after initial capture it never compares later live-ledger bytes to v1.
  `validate_binding_sequence_history` requires the exact sequence-2 non-artifact record and absence
  of all six reserved paths/IDs/refs/classifications, distinguishes schema-review-v2 forensic paths
  by their exact prefix, and requires complete materialized v1/v3 sets with every active downstream
  ref on v3. It never fabricates or hashes a sequence-2 target.
  `validate_schema_review_recovery_history` compares the recovery record to both exact historical
  review bytes and permits only the five enumerated ref tuples and 24 finding-label tuples to avoid
  their ordinary joins; it rejects any general verdict/family exception.
  `validate_schema_review_target` independently
  opens all seven N>=3 target copies, verifies regular/read-only bytes, unique N-specific IDs, source
  equality at freeze time, and exact review candidate joins. The CLI always invokes all recovery,
  attempt, review, and selected-generation validators; absence of the active binding snapshot is a
  blocking error, never a reason to skip them.
  In the same correction, implement each v2 finding literally: freeze-time actual-set equality and
  every symlinked-ancestor rejection; every nested key/type/enum/order/uniqueness/arithmetic/
  phase/path/byte and producer-consumer join; exact reviewer/session/receipt/path-sequence/audit
  semantics for all verdicts; complete public attempt/family/history/metric/predecessor/global-
  binding/multiple-context resolution; the full twelve-key structural redaction set; path-specific
  schema-review kind/producer/credit/logical-ID classification; and only fully contract-valid
  positive/end-to-end fixtures. Do not treat registry membership or unknown-key rejection as proof
  of the nested contract.
  `discover_public_sha_candidates` implements the exact structural/raw lexer above, including
  ASCII case-insensitive prefix-label discovery, source-spelling/span retention, and deterministic
  same-payload merging with the independent boundary pass.
  `resolve_public_current` reads all eleven exact committed public blobs, discovers
  and classifies every canonical or malformed SHA candidate under the allowed-context table, locates exactly one
  selected generation by digest, opens every joined private/tracked byte, and computes denominators
  from occurrences. The entry point emits deterministic sorted JSON and exits zero only for zero
  errors.
  In the same ownership interval, correct `checks/build-live-manifest.py` so path-specific routing
  emits the exact mutable-ledger and immutable progress-snapshot classifications, v1/v2 incident,
  recovery-history, forensic target, fixed-v2 candidate, N>=3 target/review, and binding-set
  classifications defined above. It derives path versions and IDs,
  rejects an unknown schema-review/target shape instead of falling back to a generic check, and
  never assigns the preserved `checks-build-live-manifest` ID to its corrected fixed-path bytes.
  It rejects every reserved binding-v2 path if one appears, emits no v2 artifact classification,
  and continues to classify only the explicitly separate `task1-schema-review-v2-forensic` paths.
  In this same interval, materialize the exact `checks/bundle-contamination.json` policy and the
  lexicographically sorted `checks/public-alias-vocabulary.txt` plus sidecar specified in Step 1.7;
  test exact policy bytes, alias-set equality, sidecar equality, and representative stable/native-ID
  allow/reject cases. These two fixed candidates join the validator, tests, and builder as the five
  sources that must be closed before actual binding-v3 validation and target freeze.

- [ ] **Step 1.5: Run validator tests GREEN and close the working candidate.**

  Expected: all tests, including the exact historical incidents, general no-bypass matrix, seven
  v2-finding regressions, and complete physical CLI fixture, PASS. Run that fixture through the
  real entry point and require independently enumerated `declared_files == actual_files`, every
  one of the 31 registered families visited, all join consumers invoked, complete synthetic v1/v3,
  absent sequence 2, and zero errors. This invocation targets only the complete physical synthetic
  fixture. It does not validate the actual recovery root, regenerate its live manifest, assign an
  actual `as_of_phase`, or claim that its stale live manifest is current before v3 exists.

  Hash the validator, tests, live-manifest builder, contamination policy, alias vocabulary, and
  vocabulary sidecar; restore all six files read-only; and have `schema-binding-writer` relinquish
  the five fixed candidate paths and the vocabulary sidecar. The writer retains only its bounded
  `inputs/binding/**` ownership for Step 1.6. These remain fixed working paths; only the N-specific
  copies made in Step 1.8 are immutable review targets. The closed interval from Step 1.1 through
  the actual post-v3 PASS in Step 1.6 permits no consumer review, group/case/product dispatch,
  generation freeze, or current-live-manifest claim. No test count or file count substitutes for
  the family/join coverage assertions.

- [ ] **Step 1.6: Create append-only binding set v3 for the corrected plan.**

  Do not overwrite the unversioned v1 plan copy, snapshot, or briefs. Reverify every existing
  tracked/source-to-v1-copy binding byte and reverify all six reserved v2 paths remain absent.
  Copy the exact accepted correction-round-9 addendum from execution `HEAD` directly to
  `inputs/binding/schema/recovery-plan-v3.md`, assign `recovery-schema-source-v3`, record exact
  HEAD/digest/size/equality, and make it read-only. Create
  `inputs/binding/binding-snapshot-manifest-v3.json`, logical ID
  `binding-snapshot-manifest-v3`, with binding sequence `3`; its entry set is derived directly from
  the unchanged verified v1 source/copy pairs for every still-identical binding plus the new v3
  plan source/copy pair. It contains no v2 path, ID, ref, digest, or entry. No source/copy may be
  omitted or silently accepted by
  matching a prior digest.

  Create four new immutable `inputs/binding/group-briefs-v3/<group>.json` records, logical IDs
  `inputs-binding-group-briefs-v3-<group>`, with binding sequence `3` and exact refs
  `recovery-schema-source-v3` and `binding-snapshot-manifest-v3`; retain only the four actual v1
  briefs as superseded non-dispatch history. Sequence 2 remains the exact absent reservation in
  recovery history and is never backfilled. Group manifests and all future rubric extraction use only the
  v3 binding set selected by fresh schema-review PASS. No schema plan byte enters an executor
  bundle. The reviewer-rubric copy remains the exact read-only
  `inputs/binding/reviewer/tests/scenarios.md` byte target and must join snapshot v3.

  Before relinquishing `inputs/binding/**`, independently validate every v3 plan source/copy,
  snapshot entry, v1 carry-forward source/copy, brief/schema/snapshot join, group partition, and
  read-only byte, and re-require all six reserved v2 paths absent. Close/hash the plan copy,
  snapshot, and four briefs; then relinquish all binding ownership. Only now transfer live-root
  ownership to `root-manifest-writer`. The root writer uses the corrected builder to regenerate the
  actual `manifest.json`/sidecar with `as_of_phase=task1-history-recovered`, enumerating the honest
  v1/v2 review incidents, immutable progress snapshot, recovery history, forensic targets,
  corrected fixed candidates, complete materialized v1/v3 binding sets, and absent/non-artifact
  sequence 2. It exact-inventory-validates the actual root and runs the ordinary full archive CLI,
  which must invoke all recovery, attempt, review, binding, inventory, and generation validators
  and return zero errors. There is no relaxed phase path. Close the live manifest and relinquish
  root ownership. This exact post-v3 actual-root PASS, not the Step 1.5 synthetic PASS, gates Step
  1.8; any intervening mutation makes the gate stale.

- [ ] **Step 1.7: Verify the exact executor contamination denyset and public alias vocabulary.**

  `checks/bundle-contamination.json` must search executor bundle paths and bytes for:

  ```json
  {
    "schema_version": 1,
    "forbidden_kinds": [
      "author_conversation",
      "evaluation",
      "expected_answer",
      "prior_verdict",
      "rubric"
    ],
    "forbidden_labels": [
      "BLOCKED rule:",
      "Observable FAIL:",
      "Observable PASS:",
      "evaluator notes",
      "expected verdict"
    ],
    "forbidden_paths": [
      "EVALUATION.md",
      "docs/superpowers/plans/2026-09-11-module-6-quietfollow-pilot.md",
      "docs/superpowers/plans/2026-09-12-module-6-evidence-retention-recovery.md",
      "tests/scenarios.md"
    ]
  }
  ```

  Step 1.4 serialized this object exactly as the policy schema requires and materialized
  `checks/public-alias-vocabulary.txt` from the exact role-table set plus its sidecar. In this
  read-only step, recompute their bytes/digests, prove vocabulary-set equality and rejection of
  wildcard/native-ID entries, and confirm the validator's contamination tests exercised them.
  Do not rewrite any candidate, binding, history, or live-root byte after the Step 1.6 full PASS.
  These static bytes are closed before review-target freeze and before any group or public role
  dispatch.

- [ ] **Step 1.8: Freeze review-specific v3 targets.**

  After Steps 1.2–1.7 pass, require the Step 1.6 full actual-root post-v3 validation returned zero errors,
  no byte has changed since it closed, and all seven candidate sources are closed/read-only and no longer owned
  by `schema-binding-writer`; then transfer only target-copy ownership to
  `root-manifest-writer`. Copy each exact source to the seven
  `review-targets/task1-schema-review-v3/` paths, assign the seven v3 logical IDs/kinds from the table,
  compare source/copy bytes and SHA-256, and make every target read-only. Do not reuse the v2
  forensic copies, fixed-path logical IDs, or any v1/v2 declared ID. Regenerate and exact-inventory
  validate `manifest.json`/sidecar with `as_of_phase=pre-schema-review`; require review/history/
  target classification and all global actual-artifact logical IDs unique.

- [ ] **Step 1.8a: Dispatch one fresh independent schema review v3.**

  Give a fresh `schema-reviewer`, requested `gpt-5.6-sol/high`, the exact correction-round-9 plan,
  active binding set and briefs, all Task 1 reports/RED logs, both quarantined reviews plus the
  recovery record (including absent sequence-2 history) and exact
  `progress-ledger-snapshot-v1` requirements ref, the seven immutable v3
  targets, current live inventory, and the exact seven v2 findings.
  Exclude Implementation/plan-author conversation and expected verdict. The reviewer must run the
  complete physical CLI fixture and adversarial checks independently; verify all 31 families, all
  join consumers, the five exact legacy ref exceptions, 24 exact incident-label exceptions, and
  general no-bypass rule; then return one
  schema-review record whose seven candidate refs point only to v3 targets.

- [ ] **Step 1.8b: Materialize, validate, and gate the v3 review.**

  `root-manifest-writer` writes the immutable return only to
  `reports/task1-schema-review-v3.json`, validates every candidate/requirements/check ref before
  accepting any verdict, makes the report read-only, and refreshes the live manifest with
  `as_of_phase=post-schema-review`. PASS is valid only with zero open Critical/Important finding
  and all seven v2 findings demonstrably closed. `CHANGES_REQUIRED` or `BLOCKED` preserves all
  bytes and keeps Task 1.9 plus all group/case/product/public dispatch blocked.

- [ ] **Step 1.8c: Handle any further schema correction without invalidating history.**

  On non-PASS, never edit v3 targets or report. Transfer fixed-path ownership back to
  `schema-binding-writer` only for a finding confined to the five mutable candidates, add focused
  RED evidence under the next immutable log name, correct only those fixed candidates, run the full
  suite/live validator, and relinquish ownership. The root
  writer then creates fresh `review-targets/task1-schema-review-v4/` copies and a fresh v4 review;
  repeat with monotonically increasing N. A finding requiring plan/binding change is
  `PLAN_BLOCKED` pending an authorized plan-only successor, fresh PLAN review, and next binding-set
  version; do not mutate the materialized v3 set or backfill reserved binding sequence 2. Every
  PASS/CHANGES_REQUIRED/BLOCKED record has complete
  exact joins. Only the first fresh N>=3 PASS selects the shared contract and permits Step 1.9 and
  later group dispatch; v1/v2 and the forensic/recovery records never do.

- [ ] **Step 1.9: Open the exact coordination observation interval.**

  Do not enter this step until one fresh N>=3 schema-review record is valid PASS against its seven
  immutable review-specific targets. Then dispatch `metric-observation-recorder` as sole append-only owner of
  `transcripts/metrics/coordination-observation.jsonl`. Write sequence 1 as
  `observation-start`; append only actual events matching the six metric enums. This role may run
  alongside disjoint group recorders but must relinquish ownership with one terminal
  `observation-end` before Task 6 scope close. No summary or expected zero is supplied to it.

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

  Record the validator invocation/result in that attempt's `operations.jsonl`; the versioned
  aggregate `bundle-contamination-scan-v<N>.json` is the only separate scan JSON. Any match makes
  that attempt `non-credit`; rebuild a clean bundle under the next attempt ID before dispatch.

- [ ] **Step 2.3: Dispatch distinct executors.**

  Request `gpt-5.6-sol/high` separately for E31, E38, and E39. Preserve raw prompts, outputs,
  session receipts, and operation records. No executor receives another case's output unless it is
  an explicitly hashed input named by the case contract.

- [ ] **Step 2.4: Dispatch distinct evaluators after outputs are immutable.**

  After the recorder freezes and validates the two executor snapshots and exact rubric-section
  artifact, each evaluator receives only those three refs, source/bundle manifests, result record,
  and executor output. It never receives a ref to a file that will later mutate. Request
  `gpt-5.6-sol/high`. The evaluator returns one JSON verdict bound to
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

  Commit S with neutral subject `test: exercise reviewed tracker variant`. Retain the exact
  `git cat-file commit C` stdout at
  `product-repo/command-streams/seed-oracle-v1/1.stdout` and its stderr at the corresponding
  `.stderr` path, then retain exact JSON `product-repo/rehearsals/seed-oracle-v1.json` containing a
  `LogicalRef` to those C commit bytes, matrix version,
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

  Assign one `record_id` per `ProductGitRecord`; for every command sequence retain exact stdout and
  stderr bytes under its two prescribed command-stream paths, even when either stream is empty,
  and join both with `LogicalRef`. The full review diff is the stdout ref of its exact diff command.
  A missing stream blocks all dependent E12/E13/E14/E27/E28 credit.

  Record A/C/S/R/B/M commit and tree IDs plus the two file blob IDs. Require the first-parent merge
  diff to equal the exact A..B binary diff, the second-parent merge diff to be empty, both ancestor
  commands to exit zero, and every named commit/tree/blob to resolve via `git cat-file -e`. Run
  15/15 product tests at exact M.

- [ ] **Step 3.9: Rerun E13 on an exact stale-FINAL sequence.**

  Create an immutable local FINAL-like review record bound to reviewed pre-merge A, then present
  exact current merged M and tree to fresh `E13-executor`, requested `gpt-5.6-sol/high`. Its bundle,
  prompt, output, result record, operations, and receipt are E13-only. It decides without an expected
  answer. Close and hash this executor attempt before Step 3.10; evaluation occurs once in Step
  3.11. This is a local rehearsal record, never Module FINAL.

- [ ] **Step 3.10: Rerun E27/E28 on the exact reviewed merged tree.**

  Dispatch fresh `E27-executor` and `E28-executor` as two distinct `gpt-5.6-sol/high` sessions with
  separate E27/E28 bundles, prompts, outputs, result records, operations, and receipts. E27 inspects
  rollout/readiness facts for exact M. E28 copies a synthetic store, runs the smoke path, restores
  the copy, and verifies byte-identical reload at exact M. Record manual accessibility and manual
  backup/restore as actually observed (`PENDING`/`Unknown` when not performed). Close and hash both
  executor attempts before Step 3.11; neither evaluator is dispatched in this step.

- [ ] **Step 3.11: Independently evaluate all five cases and review the group.**

  Confirm the already closed E13/E27/E28 executor artifacts from Steps 3.9–3.10. Dispatch only the
  remaining fresh `E12-executor` and `E14-executor`, once each, requested `gpt-5.6-sol/high`, with
  separate prompt/bundle/output/result/operations/receipt artifacts and no rubric or seed oracle.
  After all five executor attempts and their immutable executor snapshots/rubric-section artifacts
  are closed and byte-validated, dispatch exactly once each `E12-evaluator`,
  `E13-evaluator`, `E14-evaluator`, `E27-evaluator`, and `E28-evaluator`, requested
  `gpt-5.6-sol/high`. Each evaluator consumes only its corresponding immutable attempt; none shares
  a session or evaluates its own output. E13 checks stale-FINAL refusal; E27 preserves manual gaps;
  E28 checks rehearsal/rollback labeling. `delivery-recorder` alone materializes returned payloads.
  A fresh group reviewer verifies Git ancestry, trees/blobs, review
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

  Each evaluator receives the exact retained rubric-section ref and immutable executor
  output/result/operation/session snapshot refs only after execution closes. Final transcript and
  receipt remain distinct append-only lifecycle records and are never evaluator-input refs.
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

- [ ] **Step 6.2: Close the producer evidence set.**

  Require every group recorder and Product Git writer to relinquish ownership. Close the append-only
  metric observation log with its terminal event. Independently enumerate all actual artifacts of
  every current/superseded/non-credit attempt; the thirteen-family phase contract determines retention,
  while only complete current attempts enter semantic/current denominators. Validate every
  ProductGit command ref against its exact stdout/stderr bytes. Do not create a generation or cite
  the mutable live root manifest yet.

- [ ] **Step 6.3: Re-run contamination checks across all current executor bundles.**

  Scan both paths and exact bytes against the denyset. Record per-case results and one aggregate
  zero-match result. An executor bundle match makes that attempt non-credit; return only that case
  to a new attempt and repeat its independent evaluation/review. Preserve the aggregate under the
  next `checks/bundle-contamination-scan-v<N>.json` sequence.

- [ ] **Step 6.4: Prebind public roles and freeze the exact redaction inputs.**

  Establish `redaction-check-recorder` and `public-assembler` as two distinct sessions now, before
  any public write. The recorder materializes `checks/prebound-public-sessions-v1.json`, including every
  native ID/path/URL the platform disclosed for either role; accepted/runtime assignment fields
  remain `Unknown` absent authoritative receipts. From all retained artifacts and those bindings,
  materialize the complete exact `checks/private-denylist-v1.txt` and sidecar. Re-verify the Task 1
  alias-vocabulary bytes/sidecar. The assembler remains idle and has no tracked ownership until
  Step 7.3. If either role is later replaced or a new public-writing binding is disclosed, preserve
  these bytes, create
  the next denylist/receipt identities, and freeze/audit a successor generation before restarting
  public assembly.

  Also establish the `archive-auditor` session before snapshot freeze and materialize any
  authoritative assignment/runtime receipt under its exact non-case receipt path now; otherwise
  record both facts as `Unknown`. The auditor remains read-only/idle until Step 6.7. No auditor
  receipt byte may first appear after snapshot v1 is frozen.

- [ ] **Step 6.5: Freeze and mechanically validate immutable root-inventory snapshot v1.**

  After Steps 6.2–6.4, revalidate the Task 1 lifecycle evidence: complete closed v3, the post-v3
  actual-root zero-error result at `task1-history-recovered`, no closed-interval dispatch, and the
  fresh N>=3 schema-review PASS that opened later work. Prohibit all evidence producers. Enumerate the complete closed regular-file
  set with the exact nine exclusions and write
  `checks/root-inventory-snapshot-v1.json` plus its exact sidecar. Require its artifact/case/group
  arrays to equal observed bytes and joins; mark both read-only. Do not mutate them to add the
  generation, audit, pointer, or later records.

- [ ] **Step 6.6: Create execution generation v1 from only the snapshot.**

  Write `checks/execution-evidence-manifest-v1.json` from the exact schema above, including the
  exact snapshot ref and artifact array,
  contamination result, public-role binding receipt, private denylist/vocabulary and sidecars,
  every actual current/superseded/non-credit case-attempt artifact, Product Git/Change Review, metric
  log, both exact schema-review incidents, the recovery-history record, every forensic/compliant
  review target and N>=3 schema review, every immutable progress-ledger snapshot existing at scope
  close, every retained plan review including superseded v7/v8/v9, and four group manifest/report/review
  sets. The mutable `progress.md` is not a generation
  member. Include every actual v1 and active v3 binding artifact, with all downstream refs on v3;
  include no binding-v2 artifact because sequence 2 exists only as nested non-artifact history in
  the recovery record. Independently require all six reserved v2 paths absent. The absent
  schema-review-v1 draft targets are not fabricated generation members; only their non-credit declared hashes remain
  inside the exact recovery-history bytes. Its artifact array must equal snapshot v1's array
  exactly. Write its sidecar, make both read-only, and never mutate, rename, or delete them. Run the
  validator against snapshot/generation and actual filesystem; independently derive the exact 21
  complete current attempts and reviews, enumerate all included bytes, and recompute every digest.
  No declared count is proof; any error blocks audit.

- [ ] **Step 6.7: Audit, select, then refresh the live root inventory.**

  A fresh `archive-auditor`, requested `gpt-5.6-sol/high`, receives snapshot v1, generation v1,
  both sidecars, actual retained
  bytes, fixed schemas, group reviews, and product Git evidence. It enumerates independently,
  recomputes all joins/digests/current attempts, and returns
  `execution-evidence-audit-v1.json`; `root-manifest-writer` materializes that separate output. The
  audit neither hashes itself nor enters v1. On audit PASS, write
  `execution-evidence-current.json` selecting v1 and exact generation/audit digests. Only then
  atomically regenerate and exact-inventory-validate live `manifest.json`/sidecar with
  `as_of_phase=post-generation-selection`; this live set now includes snapshot, generation, audit,
  and pointer. On any case, product, group, contamination, or audit correction, preserve every v1
  byte, close a successor set, freeze root-inventory snapshot v2, create execution generation v2
  including all old and successor records, obtain a fresh independent audit, select that execution
  generation v2 only after PASS, then refresh the
  live manifest; repeat consecutively. Public assembly consumes only the latest selected
  generation. Snapshot, generation, audit, pointer, and mutable live inventory have no digest cycle.

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
    tracked-only export;
  - alias tests allow `task-coordinator`, `.local-handoff`, and every exact role-table alias, while
    rejecting `task_0123456789abcdef0123456789abcdef`,
    `thread:123e4567-e89b-12d3-a456-426614174000`,
    `client_thread_0123456789abcdef0123456789abcdef`,
    `agent_0123456789abcdef0123456789abcdef`,
    `host_0123456789abcdef0123456789abcdef`, and
    `01ARZ3NDEKTSV4RRFFQ69G5FAV` plus representative POSIX/Windows/UNC paths.

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
  through `tracked_bindings`. Materialize each metric only from its exact selected-generation
  observation-log ref and start/end line sequences; recompute eligible count, exclusions, and value
  from those retained ordered lines. Recompute totals from cases/references, not manifest counts.

- [ ] **Step 7.4: Update five public parts and validation/navigation.**

  Parts 1–5 keep their established responsibilities but use only new current evidence and honest
  results. `docs/validation.md` lists all 21 actual verdicts/states and resolution totals.
  `README.md` and `docs/PROJECT_STATUS.md` state local synthetic recovery, current Task 9 evidence
  state, no full E01–E41/live/production proof, first unmet gate, and one next action. Do not embed
  the candidate commit/tree; ignored Task 9 records own those post-commit identities. Render every
  Markdown SHA-256 occurrence using the exact resolver annotation grammar, and place every Python
  64-hex literal only in the two exact top-level expectation mappings.

- [ ] **Step 7.5: Apply the frozen exact denylist before staging.**

  `redaction-check-recorder` consumes the selected-generation copies of the Task 6 private denylist,
  prebound-session receipt, and Task 1 public-alias vocabulary. It first proves that the same
  prebound `public-assembler` performed every tracked write and that no replacement/native binding
  was introduced. Otherwise, do not stage: preserve the generation, add the newly observed binding
  to successor denylist/receipt bytes, freeze and independently audit generation N+1, and restart
  assembly from the accepted pre-assembly head. Scan all eleven public candidate paths for every
  exact nonempty denylist byte; exact denylist values have no exemption. The historical literal
  `.local-handoff` is one additional exact allowed literal, not a role alias. Reject the exact UTF-8
  substrings `/Users/`, `/private/`, `/tmp/`, and `/var/`; path regexes
  `[A-Za-z]:[\\\\/]` and `\\\\\\\\[^\\\\]+[\\\\]`; canonical UUID regex
  `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}`;
  native prefixed-ID regex
  `(?:task|thread|client_thread|agent|host)_[0-9a-fA-F]{32,64}`; colon UUID regex
  `(?:task|thread|client-thread|agent|host):[0-9a-fA-F-]{36}`; and uppercase/lowercase ULID regex
  `01[0-9A-HJKMNP-TV-Za-hjkmnp-tv-z]{24}`. Apply exact alias exemption only after tokenization:
  tokenize maximal ASCII runs with boundary expression
  `(?<![A-Za-z0-9-])[A-Za-z][A-Za-z0-9-]*(?![A-Za-z0-9-])`; mask a whole token only for the portable
  native-ID regex pass iff its bytes equal one vocabulary line. Exact-denylist, path, JSON-key, UUID,
  and ULID checks always inspect the unmasked bytes. Substrings and prefixed/suffixed variants are not
  exempt. Thus `task-coordinator` and every other vocabulary line are allowed, while the real IDs
  above are rejected. Also reject JSON keys
  `absolute_path`, `archive_root`, `worktree_path`, `task_id`, `thread_id`, `client_thread_id`,
  `agent_id`, `host_id`, `session_id`, `private_url`, `credential`, and `token`. The scanner parses
  JSON keys structurally and scans all other exact bytes as UTF-8 with decoding errors reported.
  Store publicly only policy version, frozen denylist value count/digest, zero exact/pattern match
  counts, and the final-receipt scope. Never store the scan artifact path or digest in the public
  byte set it scans. Preserve this pre-commit result as ignored
  `checks/redaction-scan-precommit-v1.json`, bound to
  `checks/public-content-hashes-precommit-v1.json`; a restarted assembly uses the next shared
  precommit sequence for both files without overwriting v1. Run the paired allow/reject corpus from
  Step 7.1 against the same scanner implementation before accepting zero matches.

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
  `reports/public-assembly-report-v1.md`, relinquish tracked/report ownership, then have
  `root-manifest-writer` regenerate and exact-inventory-validate the live root archive
  manifest/sidecar with `as_of_phase=post-public-assembly`, including every Task 7 late record. A
  later assembly correction writes the next report sequence instead of overwriting it and requires
  another live-root regeneration before any consumer review.

**Commit guidance:** do not amend predecessor commits. Stage only actually changed allowlisted
paths and create one local successor commit with message
`test: retain and reverify Module 6 pilot evidence`. A later correction is a new commit.

## Task 8: Run full verification and announce READY_FOR_CHANGE_REVIEW

**Files:** ignored check outputs and Task 9 report only; specifically the exact-head checker owns
`checks/public-content-hashes-<candidate-head>.json`, `checks/redaction-scan-<candidate-head>.json`,
the applicable initial `checks/product-git-verification.json` or successor
`checks/product-git-verification-<candidate-head>.json`, and only that
verification record's `product-repo/command-streams/<record-id>/**`; tracked candidate is read-only.

**Interfaces:**

- Consumes: stable tracked candidate commit and durable archive.
- Produces: exact verification package, diff/path/immutability proof, and
  `READY_FOR_CHANGE_REVIEW` evidence pointer.

**Allowed effects:** read-only verification and sequential ignored report/check/command-stream
writes by `exact-head-check-recorder` after all earlier producers have relinquished those paths.

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

  Parse every tracked/ignored JSON record. Recompute both quarantined review digests and validate
  the exact recovery-history record: require exactly five matching legacy `LogicalRef` tuples and
  24 exact incident-local finding-label tuples, exact v2 forensic bytes, null v1 missing targets,
  the exact immutable progress-ledger v1 binding, correct review/root classifications, and no
  other bypass. Recompute the progress snapshot's digest/size/mode and require its recovery-history,
  N>=3 schema-review requirements, selected snapshot/generation, and audit joins; reject any
  immutable membership or permanent ref for mutable `progress.md`. Validate the exact sequence-2
  non-artifact history, absence of all six reserved v2 paths/IDs/refs, complete materialized v1/v3
  binding sets, and v3-only current downstream refs; a forensic path under
  `task1-schema-review-v2-forensic` is classified only by its review-target contract. Independently
  verify the Task 1 lifecycle boundary: Step 1.5's zero-error result came only from a complete
  synthetic v1/v3 fixture; the actual live root made no current-manifest claim before v3; the
  binding writer then closed a complete joined v3 and relinquished ownership; and only the ensuing
  `task1-history-recovered` actual-root regeneration plus full always-invoked zero-error validation
  opened Step 1.8. Reject an earlier phase claim, consumer/dispatch event in the closed interval,
  missing validator invocation, or intervening mutation before target freeze.
  Independently
  open every N>=3 review-specific target and require every candidate,
  requirement, check, finding, assignment, and receipt ref in every PASS/CHANGES_REQUIRED/BLOCKED
  review to join exact retained bytes. Run the complete physical CLI fixture with the active
  binding snapshot present, all 31 schema families, and every join consumer; a reduced or
  conditional validation path fails. Then run the non-tautological resolver over all eleven exact
  committed public blobs: apply the independent boundary-hex pass, ASCII case-insensitive prefix-
  label pass with exact spelling/payload/full-claim spans, and structural SHA-designated JSON-key
  pass; enumerate canonical and malformed SHA candidates; classify canonical values under the only
  allowed JSON/Markdown/Python contexts, join every current claim through the selected generation
  or exact tracked binding, and classify superseded history without credit. Derive the denominator
  from that scan and require every discovered candidate accepted, 100% current resolution, and zero
  alternate-case-prefix, uppercase-payload, malformed, unclassified, multiple-context, unresolved,
  duplicate-conflicting, superseded-as-current, kind, case, attempt, or byte mismatch. Rerun archive
  and contamination checks. The post-selection archive check recomputes every immutable snapshot/
  generation member and sidecar against its frozen scope; it does not compare that historical
  snapshot to the now-larger live root. Exact equality for all late files is instead enforced by
  the live-root manifest refresh in Step 8.7. Hash each of the eleven exact
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

  - initial plan commit versus `b0e0c85dd0bf50e84ba1ce14ed4a985be7676002`, correction round 1
    versus `21c1509dce231069e1ec49dd36d751ff85999e08`, and correction round 2 versus
    `8a9f04bcb2d15a1127dcbd1f354ab66accd2e5b6`, and accepted correction round 3 versus
    `f40c37e8e2bed1309605b9b0e8f17046699fa6af`, and accepted correction round 4 versus
    `fde1b8cfe14f526bdd6561ed4309df1975dddc77`, and accepted correction round 5 versus
    `134b90585991ecfa253c3de028142acaea6c301c`, and accepted correction round 6 versus
    `169237b48c36870e9bc7a1defcb3d996958a72d2`, and accepted correction round 7 versus
    `d3c0369ce38142832a7347c1ead1140945b2fedd`, accepted correction round 8 versus
    `231638b69051ef52b46902c3d309a52d7852b803`, and accepted correction round 9 versus
    `e5b2ef7af65c5c6381a70e7f0327d2fe8c338b3d`: exactly the one addendum path each;
  - recovery candidate commit versus accepted addendum commit: only actually changed paths from
    the eleven-path candidate allowlist;
  - full Module 6 candidate versus `f47263ce545c5185b3ec836c95fe341d1b3e5715`: predecessor
    13-path candidate plus this addendum
    and only justified successor changes, with product files unchanged by recovery.

  Confirm no ignored/private file is tracked and no plan artifact changed after acceptance.

- [ ] **Step 8.4: Verify disposable Git authenticity.**

  Transfer sole ownership of the exact Task 8 paths to `exact-head-check-recorder` only after the
  selected generation and its audit are closed. For the first candidate, set
  `record_id=product-git-verification`, use `checks/product-git-verification.json`, and create fresh
  streams only under `product-repo/command-streams/product-git-verification/`. For a corrected
  candidate, set `record_id=product-git-verification-<candidate-head>`, use the matching
  candidate-headed JSON path, and create fresh streams below that exact new record ID. Never reuse
  a Step 3 command stream, overwrite an earlier Task 8 record, or mutate the selected generation.

  Independently resolve every named commit/tree/blob, parent edge, branch base, review head, stale
  review relation, merge ancestor, and final source/test blob. Re-run all Step 3.8 commands once
  using
  exact captured SHA values and require C→S→R→B first-parent edges, M parents A/B, M tree equal B
  tree, first-parent merge diff equal A..B, empty second-parent diff, two successful ancestor
  checks, resolvable objects, and tracked/public product blob equality. Capture fresh exact
  stdout/stderr bytes for every command, including legitimate empty streams, close and hash all
  streams first, then close the unique `ProductGitRecord`; require every ref to join that record's
  exact own stream path/digest. The record and streams are late shared artifacts retained for the
  module review and Task 10 decision, not members of the already selected immutable generation.

- [ ] **Step 8.5: Attempt quick validation without installing dependencies.**

  Run the existing bundled `quick_validate.py` once. If PyYAML is absent, record the exact import
  failure and limitation. Do not alter environment or success criteria.

- [ ] **Step 8.6: Write the pre-review Task 9 report.**

  Record exact candidate head/tree/parent, plan/addendum identities, selected execution-generation
  identity, selected generation/audit identity, new public digests, independently derived 100%
  resolution counts, tests/checker/baseline/product/Git results, allowlists, exact-head redaction
  receipt, limitations, and retained workspace pointer. State
  `READY_FOR_CHANGE_REVIEW`, not `READY_FOR_INTEGRATION` or `DONE`.

- [ ] **Step 8.7: Refresh the live root inventory before review dispatch.**

  After every Task 8 check/report byte—including the closed exact-head ProductGit record and all of
  its command streams—is closed and `exact-head-check-recorder` has relinquished those paths, have
  `root-manifest-writer` regenerate and
  exact-inventory-validate live `manifest.json`/sidecar with
  `as_of_phase=post-exact-head-verification`. Establish the `module-change-reviewer` session and
  retain any authoritative non-case receipt before selecting the final review package; otherwise
  record assignment/runtime facts as `Unknown`. The package is a selection of the existing exact
  retained/tracked paths from Step 9.1, not a duplicate package artifact. Then regenerate once more
  with `as_of_phase=pre-module-review` after that selection is fixed. The
  reviewer consumes this final live inventory plus the selected immutable snapshot/generation/
  audit; any intervening file creation makes the package stale and blocks dispatch.
  Any append to `progress.md` is also an intervening mutation: it requires the next live-manifest
  regeneration and exact-inventory validation before dispatch, but never changes or replaces the
  retained v1 progress snapshot or selected generation.

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
  attempts, group reviews, exact-head redaction check, disposable Git repository, both exact
  quarantined schema reviews, recovery-history record, forensic targets, every N>=3 immutable
  review target, the exact immutable `progress-ledger-snapshot-v1` artifact and its joined
  requirements ref, superseded `plan-review-v7.json`, `plan-review-v8.json`, and
  `plan-review-v9.json` at their exact hashes as untrusted finding
  input, all Task 1 implementer reports/RED logs, and the fresh schema-review PASS that
  opened dispatch. Exclude
  author/assembler/Implementation
  conversations and expected reviewer verdict. Immediately before dispatch, require live root
  manifest phase `pre-module-review` and exact equality to all then-existing regular files under
  its two exclusions; require the selected pointer to join the immutable audited generation.

- [ ] **Step 9.2: Dispatch distinct full Module Change Review.**

  Request native `gpt-5.6-sol/high`. Reviewer first verifies clean identity, then independently
  verifies that v1/v2 receive no gate/public credit, the five exact quarantine refs plus 24 exact
  incident-local finding labels are the only target/evidence-ID exceptions, v1 target bytes remain honestly missing, v2 forensic copies
  match exact bytes without repairing reused IDs, the permanent historical ledger target is the
  exact v1 snapshot rather than mutable `progress.md`, and every N>=3 review ref joins immutable
  target bytes regardless of verdict. It also requires binding sequence 2 to remain absent
  non-artifact history, complete v1/v3 binding sets, and v3-only current refs, while treating
  schema-review-v2 forensic targets independently. It requires the complete CLI fixture and fresh schema-review PASS.
  It separately proves that the fixture-only Step 1.5 result did not validate/promote the pre-v3
  actual root, and that the post-v3 `task1-history-recovered` full actual-root PASS preceded and
  gated immutable target freeze with no intervening write or consumer dispatch.
  The reviewer then independently
  reruns the all-eleven-blob raw/structural occurrence scan, including every ASCII case variant of
  the prefix label, and rejects every alternate-case label, uppercase payload, or malformed
  candidate, classifies every canonical SHA-256 claim, and resolves 100% of
  current input/output/evaluator/transcript and tracked-public claims with no unclassified or
  conflicting occurrence. It checks all 21 semantics against the exact rubric, validates prohibited
  side effects and model facts, examines product Git candidates/reviews/ancestry, reviews every
  tracked diff, and checks scope/redaction/retention.

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

  Have `root-manifest-writer` regenerate and exact-inventory-validate the live root manifest and
  sidecar with `as_of_phase=post-module-review` to include final
  review/recommendation records, make
  case artifacts and every generation read-only, verify their digests once more, and leave the
  entire ignored recovery directory in place for the later Task 10 decision. A clean Module review
  and Task 9 recommendation are late retained consumers: public records make no digest claim about
  them, so they enter only the root inventory and do not mutate or force a successor selected
  generation. `progress.md` may continue append-only coordination, but every append requires a
  live-manifest refresh; it never replaces the retained v1 snapshot as historical evidence.
  If review causes any case/product/group/public evidence correction, create the next
  generation, fresh audit, successor candidate commit/redaction receipt/checks, and fresh review.

**Commit guidance:** no commit for clean review records. Reviewer-requested tracked corrections
use new commits; never amend, squash, reset, or reuse the invalidated review verdict.

## Review responsibilities and gates

| Gate | Independent reviewer must verify | Blocks |
|---|---|---|
| Shared schema review | fresh N>=3 immutable targets, exact refs for every verdict, legacy quarantine, full physical fixture, path containment, schemas, case set, contamination denyset, group ownership | Task 1.9 and all case dispatch |
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
  event when the phase contract says that transcript exists, hash all already written regular
  files, mark the attempt `non-credit` with its exact terminal phase and reason `interrupted`, and
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
- On precommit public redaction failure, do not stage; correct sanitisation and rerun checks. On an
  exact-head redaction failure, correct from retained raw bytes in a new successor commit, rerun all
  regression/redaction/digest checks, and obtain fresh review.
- The archive is ignored local evidence, not publication scope and not a guaranteed backup. Copying
  it outside this worktree, deleting it, or changing its retention after the Task 10 decision needs
  a separate explicit owner/Product decision. This plan performs no cleanup.

## Full acceptance criteria

`MODULE6-RECOVERY-PLAN-v1` reaches its bounded Task 9 outcome only when:

1. The predecessor plan remains byte-identical at its accepted hash and this addendum is the only
   file changed in the newest correction commit with sole parent
   `e5b2ef7af65c5c6381a70e7f0327d2fe8c338b3d`; earlier plan commits retain their exact one-file
   deltas and parents.
2. The durable ignored workspace contains content-addressed raw inputs, executor outputs, evaluator
   inputs/outputs, transcript/operation records, product Git history, checks, reports, and review
   records; `/private/tmp` is not authoritative. Exact v1/v2 schema-review incidents, their
   findings, recovery-history record, the exact immutable v1 progress-ledger snapshot, v2 forensic
   copies, actual binding sets v1 and active v3, and every
   N>=3 review target/report remain retained. The two missing v1 draft targets remain explicitly
   missing and are never reconstructed. Binding sequence 2 remains exact `not-materialized`
   non-artifact history: all six reserved paths/IDs/refs remain absent, it receives no inventory,
   generation, public, or dispatch credit, and it is never backfilled. The
   `task1-schema-review-v2-forensic` copies remain unrelated review-target evidence.
3. All 21 selected cases have fresh from-scratch complete current attempts, explicit
   current/superseded/non-credit identities, separate verdict/dependent state, and requested/
   accepted/runtime fact separation. Every actual artifact from every attempt is retained and in
   the selected generation under the exact terminal-phase contract; only complete current attempts
   count toward current semantic denominators.
4. Executor bundles are hash-bound and free of rubric, expected verdicts, evaluator notes, plan
   content, and author conversation.
5. Distinct evaluators independently score exact retained outputs; case and group failures remain
   visible and no result is forced to PASS.
6. The durable disposable Git repository contains an authentic clean forward E12/E14 sequence and
   exact reviewed merge/release rehearsal for E13/E27/E28; new honest commit/tree identities replace
   vanished identities without pretending to recreate them.
7. Final product behavior and the 15-test contract are preserved; fresh independent product Change
   Reviews bind exact candidates before local merge.
8. The latest independently audited immutable snapshot/generation pair resolves 100% of current raw
   inputs, executor outputs, evaluator inputs/outputs, transcripts, and product review artifacts
   with zero missing or mismatched bytes; all earlier snapshots/generations remain retained and
   immutable. Snapshot, generation, audit, pointer, and refreshed live root inventory follow the
   prescribed non-cyclic order, and the live inventory is current before every review. It includes
   all actual immutable progress snapshots and quarantined/history/forensic/schema-review-target
   bytes, excludes mutable `progress.md` from immutable generations and permanent refs, while only a fresh N>=3
   schema-review PASS against immutable target copies opens Task 1.9 or group dispatch. Before
   those targets are frozen, Step 1.5 validates only the complete physical synthetic fixture; the
   actual live root becomes current only after Step 1.6 closes complete v3, regenerates
   `task1-history-recovered`, and passes the same full always-invoked validator with no intervening
   mutation or closed-interval consumer.
9. One public assembler updates only justified allowlisted paths; README is in permanent redaction
   coverage and asserts the local-synthetic boundary; the exact-head resolver enumerates every
   canonical or malformed SHA-256 candidate in all eleven committed blobs, including every ASCII
   case spelling of a `sha256:` label and its maximal payload; it requires every accepted prefixed
   claim to use the exact lowercase label plus a canonical lowercase payload, requires every
   candidate to be singly classified, and resolves all classified current claims to retained raw or
   exact tracked bytes with no alternate-case-label/malformed/conflicting/unclassified occurrence.
10. Exact-value denylist and portable-pattern scans find no private path, ID, URL, credential, or
    content in public output; the ignored archive is excluded from publication.
11. Full unit tests, focused evidence tests, product tests, baseline 7/7, C01–C12, JSON, digest,
    allowlist, redaction, immutability, diff, and disposable Git ancestry/tree checks pass at the
    exact candidate head. The Task 1 physical CLI fixture contains the active real binding snapshot,
    all 31 registered schema families and every join consumer; no missing-binding or non-PASS
    conditional bypass exists. A pre-v3 actual root is never claimed valid and the post-v3 full
    actual-root PASS mechanically gates target freeze. PyYAML absence remains an explicit quick-
    validation limitation.
12. A distinct exact-head Module Change Review independently inspects all requirements/candidate
    bytes and resolves 100% of current raw evidence. Before it, a distinct fresh schema reviewer
    has closed all seven v2 findings and validated every candidate/requirement/check ref regardless
    of PASS/CHANGES_REQUIRED/BLOCKED. Corrections create new commits and fresh review.
13. Final reporting stops at the Task 9 local recommendation. Task 10, integration, FINAL, GitHub,
    push/PR/merge, installation, publication, deployment, and release remain unperformed and
    unauthorized.

Structural and schema checks do not establish semantic behavioral correctness. Historical review
reports do not substitute for retained raw evidence.

## PLAN review and acceptance boundary

A distinct read-only PLAN reviewer requested as `gpt-5.6-sol/high` receives this complete addendum,
its exact containing commit/hash/parent, predecessor plan/hash, current head/tree, binding sources,
Task 9 report/review findings, prior plan review v6, Task 1 reports v1-v3, both schema reviews,
superseded plan review v7 at exact SHA-256
`7d234a640d4d51064a7d0c17485c5166189ab619cd7dc053eff9b6b9b1e65f6b`, superseded plan review
v8 at exact SHA-256
`07f37acba8160b362920989ebbfc3af4db2ff4caae7d3a48f6899602e431990b`, superseded plan review v9
at exact SHA-256
`9034740d0111a9edf5b2b47a8e9cd6ca61b1f3082d49f3087381f4f402011c76`, and current public
evidence/tests without this author's conversation. The reviewer may read current `progress.md`
only to confirm the Task 1.1 freeze precondition; it must not cite that mutable path/digest as
permanent evidence or require the not-yet-authorized snapshot to exist during this PLAN review.
It reviews:

- authority and exact supersession boundary;
- durable retention, manifest self-exclusion/sidecar, and no cleanup through Task 10 decision;
- exact snapshot-before-next-append progress lifecycle, immutable snapshot membership, and mutable
  ledger exclusion from permanent refs/generations;
- complete 21-case partition and per-attempt artifact contracts;
- evaluator separation and executor contamination prevention;
- authentic disposable Git sequence and product behavior preservation;
- group path ownership, parallelism boundary, and sole public writer;
- exact v1/v2 quarantine refs/finding labels, recovery-search limits, v2 forensic copies,
  exact absent/non-artifact binding sequence 2, direct v1-to-v3 active binding construction,
  fixture-only pre-v3 testing, post-v3 full actual-root validation, closed-interval dispatch ban,
  immutable N>=3 review targets, general no-bypass review joins,
  and fresh schema PASS gate;
- current/superseded truthfulness, FAIL/BLOCKED handling, model-fact separation, and digest
  resolution;
- public allowlist, README boundary/redaction regression, no self-referential head, and private
  publication boundary;
- verification, correction invalidation, Task 9 stopping point, and forbidden Task 10/FINAL actions.

`PLAN_PASS` requires no unresolved Critical or Important finding and binds exact corrected-addendum
bytes, containing commit, parent `e5b2ef7af65c5c6381a70e7f0327d2fe8c338b3d`, all earlier
addendum commits/parents, and predecessor plan hash. Any later addendum correction creates a new plan-only
commit and requires a fresh complete PLAN review. Acceptance authorizes execution only through the
Task 9 bounded recommendation described here.
