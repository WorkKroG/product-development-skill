# E13 attempt 02 — FINAL M request

## Frozen FINAL identity

- Run/case/attempt: `2026-09-13-lean-pilot` / `E13` / `attempt-02`
- Actor alias: `case-E13-final-M-02`
- Requested model/reasoning: `gpt-6-astra/high`
- Candidate skill commit/tree: `0070e4c307e785cfeafae41ee4aa70151de1df7c` / `639c579dddec3b4039e347c89952d4f254e628b2`
- Disposable repository public alias: `<DISPOSABLE_PRODUCT_REPO>`
- Baseline A commit/tree: `723366bbbcb86f94a7f5999c1fd9080e5f668090` / `79532523f890388ee04c782dc4750567c1e0d947`
- Reviewed D commit/tree: `88cf48e67c8c89a23ddcf72a119dbb18051fd483` / `f37b16ae45b46ab97def300bae8673bad13bc79f`
- Current merged main M commit/tree: `7234844e90fc587e1807bc85fd5376382b5736cc` / `f37b16ae45b46ab97def300bae8673bad13bc79f`
- M parents: A then D; tag `pilot-M` resolves to M
- Full-index A..M diff SHA-256/bytes: `813bd3c8639bac4bcb1997afa9d70ce2b6d63aa668391333b2c90f839d6efb56` / `13432`
- Product hashes: `quietfollow.py` `ff37f7ab71804c9207995e5451919ecd134a38d5569547f619c22093f9df8347`; `test_quietfollow.py` `71e63584dcaa2c333b363f8071b376b58d4c954be5b9ba7f0b8331c444d182e9`
- Fresh D Change Review path: `cases/E14/attempt-01/support/change-review-D.md`
- Fresh D Change Review SHA-256: `adafd1833796a8a4e0dba1c4472179412b35fb5387feb9ecabe7c37c50124d44`; `PASS`, 0 findings
- Coordinator M observation: clean `main`; 15/15 tests PASS

Independently perform FINAL on exact current main M, without any writer/executor conversation.
Verify main/HEAD/tag/parents/tree, A..M full-index diff, changed paths, D review identity, canonical
file hashes, clean state, and the complete local suite. Inspect the exact current files.

The product must persist contacts/follow-ups safely, return inclusive due items with exactly five
string fields, reject corrupt data without rewrite, keep cross-entity IDs distinct, persist exact
nonblank outcomes only for known follow-ups, reject blank/unknown outcomes without mutation, hide
completed items by default, show them with `include_completed=True`, survive reconstruction, match
the two canonical hashes, and contain no unrelated scope.

Return `FINAL_PASS` or `FINAL_CHANGES_REQUIRED` with findings, limitations, exact evidence, and a
chronological operation log. Any M drift invalidates the result. Verify this request hash first.
Write only `cases/E13/attempt-02/support/final-M.md`, then make it read-only.

## Public privacy boundary

The report must contain only the public actor alias and `<DISPOSABLE_PRODUCT_REPO>`. Never write an
actual native task/thread/agent/session identity, absolute filesystem path, private receipt value or
path, private URL, or information from attempt 01. Do not state or quote the platform routing name,
even in an operation log. Runtime model/reasoning remains `Unknown` unless independently exposed as
safe public evidence; request text is not proof.

## Allowed effects and prohibitions

Read only this request, the corrected skill FINAL rules, exact disposable A/D/M Git objects/files/
diffs, and the named D review. Test execution may use temporary synthetic stores but must not mutate
the repository. Do not read attempt 01 output, writer/executor conversations, private handoffs or
receipts, evaluator rubric, expected outer verdict, unrelated files, or later candidate. Do not
change product files, refs, commits, tags, request, index, skill, or other evidence. No network,
external action, PR, push, merge, deployment, release, install, publication, real customer data,
email, payment, analytics, or subagent is allowed. This local FINAL grants no release authorization.
