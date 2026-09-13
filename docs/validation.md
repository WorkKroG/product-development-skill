# QuietFollow lean pilot validation

Date: 2026-09-13. Plan: `MODULE6-LEAN-PLAN-v1`. Candidate skill:
`MODULE6-LEAN-SKILL-v1`.

## Outcome

The local synthetic pilot has exactly 27 current results: 21 selected E-cases and six
proportionality probes. Every current evaluation and credit verdict is PASS. Superseded, failed, or
blocked attempts remain tracked as non-credit history and were not relabelled.

The first exact-head review found incomplete request-hash/action logs in 11 results. New independent
attempts corrected the evidence boundary without changing the candidate or scenario. Ten passed on
attempt 2; E41 preserved its attempt-2 FAIL and passed the focused attempt 3.

This is behavioral evidence for the tested boundaries. It does not establish full E01–E41 coverage,
live routing, installation, integration, release readiness, or production behavior. A PASS may
correctly coexist with a blocked dependent action.

## Evidence chain

1. [Discovery and entry gates](../tests/fixtures/quietfollow/evidence/part-1-discovery.md) — E38,
   E31, and E39.
2. [Readiness and recovery](../tests/fixtures/quietfollow/evidence/part-2-readiness.md) — E02,
   E34, E37, E41, and SU01.
3. [Delivery history](../tests/fixtures/quietfollow/evidence/part-3-delivery.md) — E12, E14, and E13.
4. [Release boundary](../tests/fixtures/quietfollow/evidence/part-4-release-rehearsal.md) — E27 and E28.
5. [Coordination and stress probes](../tests/fixtures/quietfollow/evidence/part-5-resume-scaling.md)
   — E08, E10, E11, E17, E20, E21, E22, E25, E33, and SU02–SU06.

The [manifest](../tests/fixtures/quietfollow/evidence/manifest.json) binds the current plan, skill,
product, bundle, run index, execution record, and part hashes. The
[execution record](../tests/fixtures/quietfollow/evidence/execution-record.json) provides a compact
27-row view. The [run index](../tests/fixtures/quietfollow/evidence/runs/2026-09-13-lean-pilot/index.json)
is authoritative for raw tracked request, response, evaluation, evaluator-prefix, and support bytes.

## Product history

The tracked bundle preserves only the allowed local synthetic refs: `main`, `case/e12-b`,
`case/e14-d`, and tags `pilot-A`, `pilot-B`, `pilot-C`, `pilot-D`, and `pilot-M`.
Independent clone verification established that M has two parents, D is an ancestor of M, and D/M
have identical trees. The canonical product and product-test SHA-256 values match the tracked fixture.

## Checks and limitations

The assembly retains results for the full Python suite, the 15-test product suite, the seven-file
baseline, skill checks, Git diff checks, bundle verification, file enumeration, and public-data scans.
PyYAML-dependent quick validation remains unavailable without a separately authorized installation;
no installation was attempted.

Requested model/reasoning assignments do not prove accepted or runtime identity. Unavailable native
facts remain Unknown. No real user data, external service action, public push, PR, integration,
installation, deployment, or release occurred. Кандидат не интегрирован, and Task 10 is not
authorized.
