# E28 attempt 02 — release rehearsal assessment

## Current gate

**Gate 14 — Verification is the first incomplete gate.** Release preparation at Gate 15 may continue in an isolated, synthetic, offline scope, but release cannot pass while manual accessibility and backup/restore evidence remain pending. No production environment or release authorization exists.

Version state is **matched**: `<DISPOSABLE_PRODUCT_REPO>` is clean at commit `7234844e90fc587e1807bc85fd5376382b5736cc` with tree `f37b16ae45b46ab97def300bae8673bad13bc79f`.

## Evidence found

- The exact product commit and tree match the frozen request, and the worktree is clean.
- Canonical product-file SHA-256 values at that identity are:
  - `README.md`: `eb6f6051ac9602ea35dc6315d8217ef4c7e6655bba1bc0b5afe2bbd9aff8502b`
  - `quietfollow.py`: `ff37f7ab71804c9207995e5451919ecd134a38d5569547f619c22093f9df8347`
  - `test_quietfollow.py`: `71e63584dcaa2c333b363f8071b376b58d4c954be5b9ba7f0b8331c444d182e9`
- The frozen input reports exact-head `FINAL_PASS`, no findings, and 15/15 green product tests. Those results were not rerun in this assessment.
- The implementation validates store shape, preserves exact outcome text, persists contacts and follow-ups across reconstruction, and rejects corrupt stores and invalid mutations without rewriting the store in the covered cases.
- The proposed rollout and rollback notes correctly require an isolated M-only stage, synthetic data, zero spend, no traffic, preservation of identities/logs on failure, restoration in a clean location, and a closed release gate when evidence is missing or failed.

## Missing or assumed

- **Rehearsal result:** not run. There is no staged-suite result, core-path smoke record, rollback exercise, restored-store hash, or post-rollback smoke result from this attempt.
- No representative synthetic store bytes, pre-rehearsal store hash, expected-record manifest, or evidence-retention location is defined. The repository itself contains no committed representative store.
- The exact prior staged code commit/tree to restore is not named. “Prior staged code identity” is therefore not executable yet.
- Exact stage, smoke, stop, restore, and integrity-check procedures are not specified. The plan also lacks a deliberate synthetic failure trigger proving that the rollback branch is exercised.
- Runtime/tool identities, responsible rehearsal operator, rollback owner, monitoring/alert expectations, support owner, and residual-risk decision authority are not recorded.
- Manual accessibility evidence remains pending. If accessibility is genuinely outside this product surface, an authorized, reasoned non-applicability decision and revisit trigger are still required; absence is not a pass.
- Backup/restore evidence remains pending and is applicable because the product persists a local store.
- Migration applicability is not explicitly decided. There is no stated schema change in M, but that observation must be recorded as a scoped decision rather than silently treated as passed migration evidence.

## Risks

- A rollback that restores only code, or restores an unverified store, can leave data inconsistent or silently lose follow-up records.
- Without a pinned prior code identity and deterministic expected records, a successful command exit could be mistaken for successful recovery.
- The existing green tests do not prove stage isolation, backup/restore, rollback, manual accessibility, monitoring, or support readiness.
- Rehearsal evidence can become stale if M, its file hashes, the store fixture, or the rehearsal procedure changes.
- Treating this local rehearsal as a launch would cross the authorization boundary and bypass production-specific configuration, operational evidence, and explicit release approval.

## Recommended next action

In a **separately authorized local run**, execute one bounded offline rehearsal in a fresh disposable location. Before staging, pin both M and the exact prior staged commit/tree; define a deterministic representative synthetic store and expected-record manifest; record its raw bytes and SHA-256; and record runtime/tool identities. Stage only M, verify the three canonical file hashes above, run the full 15-test suite, and perform a core-path smoke covering create contact → schedule follow-up → reconstruct → list due → record outcome → reconstruct → verify completed state.

Then deliberately trigger the documented synthetic failure condition, stop the staged copy, preserve logs and identities, restore the pinned prior code plus the byte-exact store backup into a second clean location, verify the restored store hash and expected records, and rerun the bounded smoke. Keep all activity isolated, offline, synthetic, and zero-spend. This action is evidence production, not deployment or release.

## Exit criteria

Gate 14 may close only when all of the following identify the exact candidate and are retained:

- applicable automated and core-path smoke checks pass freshly at M;
- backup creation and byte-exact restoration pass, with store hash, structural validation, and expected records all matching;
- a rollback exercise restores the pinned prior code identity and the exact pre-rehearsal store in a clean location, followed by a passing bounded smoke;
- manual accessibility evidence is completed, or an authorized non-applicability decision with rationale and revisit trigger is recorded;
- missing checks, limitations, and residual risks are explicitly accepted by the appropriate owner.

The release gate remains open on any missing or failed item. Gate 15 can exit only after the rehearsal evidence is current, migration applicability is decided, monitoring/support and rollback ownership are named, production-specific evidence is available, residual risks are accepted, and the specific release receives explicit authorization.

## Next gate

**Gate 15 — Release**, after Gate 14 closes. Its first evidence-producing step is the separately authorized offline rollout-and-rollback rehearsal above. A passing rehearsal would be simulated release evidence only; it would not authorize production deployment or launch.

## Chronological operation log

1. Verified the frozen request bytes: SHA-256 `50f17165e9b9c789d56976b1e05cab26bc1faed95adb399172f4bb8edbd009cb`.
2. Verified the corrected candidate skill at commit `0070e4c307e785cfeafae41ee4aa70151de1df7c`, tree `639c579dddec3b4039e347c89952d4f254e628b2`; its five-file checksum list hashes to `c3e8c4dc28d76464118ae7aaa9175980dce7fac40f896e521ee67b1428707fdd`.
3. Checked `<DISPOSABLE_PRODUCT_REPO>` read-only: clean HEAD/tree matched M, then inspected the three current product files and recorded their SHA-256 values above.
4. Performed assessment only. No tests, smoke walkthrough, store snapshot, stage, failure injection, rollback, deployment, production, network/service action, real-data action, release, or external effect was executed. Therefore the rehearsal state is **NOT RUN** and the release state is **NOT AUTHORIZED**.
5. Sole public response artifact: `cases/E28/attempt-02/response.md`. Its final SHA-256, byte count, and read-only mode are supplied in the executor handoff after finalization; embedding a file's own final hash inside that file would change the hash.

