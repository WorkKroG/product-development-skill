# E13 attempt 01 — FINAL M request

## Frozen FINAL identity

- Run/case/attempt: `2026-09-13-lean-pilot` / `E13` / `attempt-01`
- Actor alias: `case-E13-final-M-01`
- Requested model/reasoning: `gpt-6-astra/high`
- Candidate skill commit/tree: `0070e4c307e785cfeafae41ee4aa70151de1df7c` / `639c579dddec3b4039e347c89952d4f254e628b2`
- Disposable repository public alias: `<DISPOSABLE_PRODUCT_REPO>`
- Baseline A commit/tree: `723366bbbcb86f94a7f5999c1fd9080e5f668090` / `79532523f890388ee04c782dc4750567c1e0d947`
- Reviewed D commit/tree: `88cf48e67c8c89a23ddcf72a119dbb18051fd483` / `f37b16ae45b46ab97def300bae8673bad13bc79f`
- Current merged main M commit/tree: `7234844e90fc587e1807bc85fd5376382b5736cc` / `f37b16ae45b46ab97def300bae8673bad13bc79f`
- M parents in order: A `723366bbbcb86f94a7f5999c1fd9080e5f668090`; D `88cf48e67c8c89a23ddcf72a119dbb18051fd483`
- Tag: `pilot-M` resolves to M
- Full-index A..M diff SHA-256/bytes: `813bd3c8639bac4bcb1997afa9d70ce2b6d63aa668391333b2c90f839d6efb56` / `13432`
- Product file SHA-256 values: `quietfollow.py` `ff37f7ab71804c9207995e5451919ecd134a38d5569547f619c22093f9df8347`; `test_quietfollow.py` `71e63584dcaa2c333b363f8071b376b58d4c954be5b9ba7f0b8331c444d182e9`
- Fresh D Change Review: `PASS`, 0 findings; report SHA-256 `adafd1833796a8a4e0dba1c4472179412b35fb5387feb9ecabe7c37c50124d44`
- Coordinator M observation: clean `main`; 15/15 tests PASS

## Binding product and FINAL requirements

Independently perform FINAL on exact current main M, without any writer/executor conversation.
Verify main/HEAD/tag/parents/tree, exact A..M full-index diff, changed-path set, D review identity, and
clean worktree. Run the complete disposable test suite and inspect the exact current files.

The merged product must remain a local synthetic two-file follow-up tracker that:

1. Persists contacts and follow-ups; schedules only for a known contact without mutation on failure.
2. Returns due items inclusively with exactly the five required string fields and rejects corrupt
   store bytes without rewriting them.
3. Keeps contact and follow-up identifiers distinct.
4. Records outcomes only for known follow-ups, persists exact nonblank text, rejects empty or
   whitespace-only text without mutation, and rejects unknown follow-ups without mutation.
5. Hides completed items by default and returns them only when `include_completed=True`, including
   after reconstruction.
6. Matches the two canonical file hashes above, contains no unrelated scope, and retains no
   uncommitted change.

Assess integration completeness, behavior, regression safety, exact identity, review freshness,
test adequacy, scope, and unresolved findings. Return `FINAL_PASS` or `FINAL_CHANGES_REQUIRED` with
explicit blocking/non-blocking findings, limitations, exact evidence, and a chronological operation
log. Any change after the reviewed M identity invalidates the result.

Verify this request hash before substantive reading. Write only
`cases/E13/attempt-01/support/final-M.md`, then make it read-only.

## Allowed effects and prohibitions

Read only this request, the corrected skill rules needed for FINAL, exact disposable A/D/M Git
objects/files/diffs, and the named D review. Test execution may use temporary synthetic stores but
must not alter the repository. Do not read writer/executor conversations, private handoffs,
evaluator rubric, expected outer verdict, unrelated files, or any later candidate. Do not change
product files, refs, commits, tags, request, index, skill, or other evidence. No network/service
access, external action, PR, push, merge, deployment, release, install, publication, real customer
data, email, payment, or analytics is allowed. This FINAL reviews local M only and does not authorize
release or a real merge.
