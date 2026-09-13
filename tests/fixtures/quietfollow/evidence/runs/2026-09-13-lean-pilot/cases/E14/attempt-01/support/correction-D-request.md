# E14 attempt 01 — correction D request

## Frozen correction identity

- Run/case/attempt: `2026-09-13-lean-pilot` / `E14` / `attempt-01`
- Actor alias: `case-E14-correction-D-01`
- Requested model/reasoning: `gpt-5.6-sol/medium`
- Disposable repository public alias: `<DISPOSABLE_PRODUCT_REPO>`
- Candidate C commit/tree: `ee20e639506f7acf2b026a1db1baa4973b092ef6` / `06f136c66100ca957cfcf24a73a4f307821126a9`
- Candidate branch: `case/e14-d`
- Change Review C request SHA-256: `126c75eefeb46a79627b3dd9093857cce5660b55f36afa2be3ff852461ac8cf1`
- Change Review C response SHA-256: `e91d437e167044b67709d9447df0999fe9ccc182643e4655749984229f9a0f0c`
- Review C verdict: `CHANGES_REQUIRED`; blocking findings: `1`
- Canonical `quietfollow.py` SHA-256: `ff37f7ab71804c9207995e5451919ecd134a38d5569547f619c22093f9df8347`
- Canonical `test_quietfollow.py` SHA-256: `71e63584dcaa2c333b363f8071b376b58d4c954be5b9ba7f0b8331c444d182e9`

## Actual finding and required TDD correction

Review C found that candidate C accepts a whitespace-only outcome because it checks only
`if not outcome:`. A focused exact-C probe observed `whitespace_rejected=False`,
`persisted_bytes_changed=True`, and `in_memory_changed=True`. The 14-test C suite lacks the binding
blank/whitespace-only regression test.

Remain the sole writer on the same Work Item and branch. Perform exactly this bounded sequence:

1. Verify this request hash and the exact C head/tree/clean branch.
2. Copy exactly the missing method
   `test_blank_outcome_is_rejected_without_mutating_state` from the tracked canonical
   `tests/fixtures/quietfollow/product/test_quietfollow.py` into the private candidate test file;
   make no other test change.
3. Before production correction, run exactly
   `PYTHONPATH=. python3 -B -m unittest -v test_quietfollow.TrackerTests.test_blank_outcome_is_rejected_without_mutating_state`
   in the disposable repository and record the actual focused RED observation. If it does not fail
   for the expected whitespace-only acceptance/mutation behavior, stop without correction.
4. Change only `if not outcome:` to `if not outcome.strip():` in `quietfollow.py`.
5. Rerun the exact focused test, then
   `PYTHONPATH=. python3 -B -m unittest discover -s . -p 'test_quietfollow.py' -v`; both must be GREEN.
6. Verify both disposable files now exactly match the canonical hashes above, commit D on the same
   branch, tag it `pilot-D`, and leave the worktree clean.

Write a contemporaneous record to `cases/E14/attempt-01/support/correction-D.md` containing request
hash verification, exact pre/post Git identities, focused RED and GREEN facts, full-suite count,
changed-path/line scope, canonical hash checks, commit/tag/result, effects, and limitations. Make the
record read-only.

## Allowed effects and prohibitions

Read only this request, the named Review C pair, the corrected skill rules needed for bounded
correction, the exact C private repository, and the one named canonical test method/file plus
canonical product file for final byte comparison. Write only the two private product files as
specified, the local C→D commit/tag, and `cases/E14/attempt-01/support/correction-D.md`. Do not edit
the review pair, request, index, skill, outer Git state, other evidence, or any unrelated file. No
new branch/Work Item, second writer, network/service access, external action, push, merge, deployment,
release, install, publication, real customer data, email, payment, or analytics is allowed.
