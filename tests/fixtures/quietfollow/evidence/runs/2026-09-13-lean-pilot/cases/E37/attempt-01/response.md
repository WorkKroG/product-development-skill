# E37 attempt 01 — coordinator response

## 1. Current gate

**Gate 11 — Technical plan, for the working-prototype → MVP transition.**

**Decision:** a clean replacement is justified for the bounded MVP path. The supplied evidence says
the current code lacks the persistence and validation boundaries the MVP needs, and adapting it would
cost more than replacing it. Prototype code is therefore not a sunk-cost constraint. This decision
authorizes a non-production replacement/validation slice only; it does not authorize a full rebuild,
data cutover, merge, or release.

The prototype's useful knowledge is separable from its implementation. The synthetic dataset,
recorded decisions, acceptance criteria, experiment results, reminder wording, due-list behavior, and
field meanings remain inputs at their original evidence strength. Synthetic results must not be
relabelled as real-user validation.

## 2. Evidence found

- **Applicable-covered:** the prototype established useful evidence for reminder wording, due-list
  behavior, and data fields, and the request says the associated dataset, decisions, acceptance
  criteria, and experiment results remain valid.
- **Applicable-missing:** the current implementation has no validation boundary and only an in-memory
  notebook, so it does not supply decision-grade evidence for MVP persistence, reload, failure safety,
  or testability.
- **Transition-cost evidence:** on the facts supplied, retrofitting the prototype requires a larger
  rewrite than a clean replacement. That supports replacement rather than compulsory code reuse.
- **Identity:** `cases/E37/attempt-01/request.md` matched its frozen SHA-256, byte count, and read-only
  mode. The corrected skill commit and tree matched the identities stated in that request.

## 3. Missing or assumed

- Assumed: the preserved dataset is synthetic only. If any record is later found to contain real user
  or sensitive data, migration, retention, deletion, access, backup, and rollback become
  **applicable-missing** and block any dependent cutover until explicitly authorized.
- Unknown: the authoritative field-level schema, required/optional fields, timestamp and timezone
  rules, duplicate semantics, update/delete behavior, and corrupt-write recovery expectations.
- Unknown: the measured cost estimate behind “larger rewrite,” the selected persistence mechanism,
  and whether the existing acceptance criteria cover invalid input, restart, retry, and recovery.
- No code, dataset, or test result was inspected under this exercise's read boundary; the replacement
  decision is conditional on the supplied facts and must be revisited if they are contradicted.

## 4. Risks

- Semantic drift could preserve rows while changing wording, due-list classification, or field meaning.
- Silent field dropping or coercion could make a successful import look safer than it is.
- Clock and timezone ambiguity could make due lists nondeterministic.
- Partial writes or retries could lose or duplicate reminders.
- Treating synthetic fixtures as user evidence could overstate product validation.
- Expanding the spike into accounts, sync, notifications, production operations, or generalized
  infrastructure would invalidate the bounded decision and require renewed scope and risk review.

## 5. Recommended next action

Build one **non-production clean-replacement spike** for the complete path:

`validated reminder input → replaceable durable repository → process/repository reopen → due-list query → accepted wording`

Keep the slice deliberately narrow:

1. Preserve the original synthetic dataset and knowledge artifacts unchanged as a read-only baseline.
   Create a field mapping that classifies every source field as mapped, deliberately deferred, or
   rejected with a reason; no field may disappear silently.
2. Define one versioned reminder record and validate it before persistence. Use an injected clock and
   explicit timezone so due-list behavior is deterministic. The particular storage engine is a
   routine implementation choice as long as it sits behind the tested repository boundary.
3. Import only the minimum representative synthetic fixture set needed to cover overdue, due-now,
   and future items plus one invalid boundary case. Keep the full preserved dataset untouched; the
   importer must support a dry run and reconciliation before any write.
4. Add contract tests derived from the preserved acceptance criteria for wording, due-list membership
   and order, durable reload, invalid-input rejection without mutation, failed-write recovery, and
   retry without duplication.
5. Keep rollback simple: the spike is isolated and non-production, the prototype and baseline evidence
   remain recoverable and unchanged, and removing the replacement leaves those inputs intact.

## 6. Exit criteria

Gate 11 closes for this slice only when all of the following identify the exact candidate:

- The record schema, validation boundary, repository interface, clock/timezone rule, and invariants are
  documented and testable.
- Every representative fixture field is reconciled with no unexplained loss; source fixtures remain
  byte-for-byte unchanged.
- A valid reminder survives repository/process reopen and produces the expected due-list result and
  accepted wording under a fixed clock.
- Invalid input produces no write; an injected write failure preserves the last valid state; retry does
  not create a duplicate.
- The dry-run import reports proposed creates/rejections before mutation, and the applied test import
  reconciles counts and stable identifiers with the expected fixture result.
- The rollback procedure is demonstrated in the isolated test environment without modifying the
  preserved prototype evidence.
- Fresh relevant tests pass, limitations are recorded, and an independent review of the exact candidate
  finds neither unsafe future constraints nor premature infrastructure. A test failure or unexplained
  field mismatch keeps Gate 11 open.

## 7. Next gate

**Gate 12 — Delivery plan.** After the Gate 11 exit criteria are met, turn the validated slice into
small implementation work items with stable contracts, review boundaries, non-goals, fresh checks,
and manual integration. Do not enter full implementation or any data cutover merely because the spike
passes.

## Concise operation log

1. Verified `cases/E37/attempt-01/request.md` against its recorded SHA-256, byte count, and mode.
2. Loaded the corrected skill at the bound commit and confirmed the bound tree identity.
3. Applied its lifecycle and evidence-state rules; selected the first affected gate and preserved
   still-valid prototype knowledge separately from the replaceable code.
4. Performed no implementation, migration, evaluation, subagent, network, service, or external action.

## Limits

This response is a coordination decision and validation design, not executed evidence. It does not
verify the prototype, persistence mechanism, dataset contents, acceptance criteria, migration, tests,
security, accessibility, operational readiness, or release readiness. Any material change to product
scope, shared contracts, cost, risk, schedule, or real-data exposure requires the appropriate Product
or owner decision before the affected transition continues.
