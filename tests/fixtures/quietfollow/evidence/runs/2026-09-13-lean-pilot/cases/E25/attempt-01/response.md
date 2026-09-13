# Coordinator response

## Version and decision state

- Process identity: **matched**. The response uses candidate commit
  `0070e4c307e785cfeafae41ee4aa70151de1df7c`, whose tree is
  `639c579dddec3b4039e347c89952d4f254e628b2`.
- Request identity: SHA-256
  `e7f546c12cc27788476b765346f832d60842dd6a0afefa098610d955ed591a31`.
- Architecture state: contract v2 is the accepted binding direction for the replaced endpoint and
  event field; v1 is superseded for that surface. The immutable identity and complete contents of
  the accepted v2 decision were not supplied, so v2-dependent implementation cannot safely resume
  until that decision is recorded or identified. Contract v1 and v2 must not remain simultaneously
  active for the affected surface.

## Current gate

Delivery coordination has reopened the affected part of **Technical plan**. The first incomplete
transition is an identity-bound architecture return for contract v2, followed by focused replanning
of only the affected work. Unaffected delivery remains active.

## Evidence found

- Module A has useful local validation and tests that do not depend on the changed fields.
- Module B has an unreviewed adapter directly coupled to contract v1.
- Module C uses neither version of the contract.
- The shared decision changes one endpoint and one event field; it does not authorize merge,
  release, or additional implementation scope.

## Missing or assumed

- Missing: the immutable v2 decision/contract identity, its exact endpoint and event-field
  semantics, compatibility or migration rules, affected plan identities, exact branch heads, and
  fresh test results bound to those heads.
- Assumption: “accepted” means Product has authority to make v2 binding, not that implementation,
  migration, PR creation, merge, or release is authorized.
- No review verdict is assumed. Module B is explicitly unreviewed, and any earlier plan or verdict
  whose binding assumptions include v1 is stale only for the affected surface.

## Impact, preservation, and pauses

| Module | Preserve | Pause or change | Work allowed to continue |
|---|---|---|---|
| A | Existing WIP plus validation and tests proven independent of the replaced fields | Pause only code, planning, integration, or review that touches the replaced endpoint or event field. Re-review that slice against v2; do not replay unaffected work. | Independent in-scope work and the unaffected tests/validation; rerun them later on the exact candidate head before relying on them for review. |
| B | The v1 adapter, its branch/diff, and any observations or tests as WIP evidence; preservation is not acceptance | Pause the adapter and every downstream integration or review that assumes its v1 mapping. Replace only the coupled mapping after the v2 identity and semantics are available. | Work demonstrably independent of the adapter; otherwise wait at the dependency boundary. |
| C | All current WIP and evidence | No pause, restart, or re-review caused by this decision | Continue its already-authorized work from its current state. Do not send an unchanged project event. |

No WIP is discarded. No completed independent evidence is recreated. Supersession applies to the
v1-dependent assumptions, not automatically to whole modules.

## Risks

- Coding from an unnamed v2 contract could create two interpretations of the same shared surface.
- Treating Module A’s prior tests as fresh evidence after a new head would overstate what they
  prove.
- Letting Module B enter review unchanged would review a knowingly superseded adapter.
- Broadly restarting A or stopping C would lose valid work without reducing contract risk.
- The decision may hide migration or compatibility consequences; those remain unknown until the
  versioned contract states them.

## Recommended next action

Product should record or point to one immutable contract-v2 architecture decision and issue a
bounded architecture return that names the replaced endpoint and event field, compatibility or
migration expectation, revised A/B dependencies, preserved WIP, invalidated plan/review portions,
and continuation conditions. This is the smallest action that produces the evidence both affected
modules need. It does not authorize implementation by itself.

Once that package exists, the smallest module actions are:

1. Module A maps the v2 delta to its changed-path surface, updates only that slice of its plan, and
   obtains renewed PLAN review for the affected plan identity. Its first implementation evidence is
   a focused v2 contract test plus fresh reruns of the preserved independent tests on the exact new
   head.
2. Module B keeps the v1 adapter intact as recoverable WIP, first adds or updates a focused test that
   expresses the accepted v2 mapping, then makes the minimum adapter change needed to pass it. It
   must receive independent Change Review before integration readiness can be claimed.
3. Module C continues independently; it needs no contract-change action.

## Exit criteria

This coordination gate exits when:

- one immutable v2 architecture identity is binding and v1 is explicitly superseded for the
  affected endpoint and event field;
- A and B have received revised boundaries, dependencies, preserved-work notes, and continuation
  conditions;
- each v1-dependent plan or verdict is identified as affected, while independent evidence remains
  preserved;
- A has an affected-slice plan verdict bound to its revised plan and exact base;
- B has a bounded v2 adapter work item with an exact base, acceptance test, and recovery path; and
- C has continued without an unnecessary restart.

For later integration, each changed module additionally needs fresh v2-focused checks and preserved
independent checks on its exact head, independent Change Review bound to that unchanged head, and no
open required correction. These criteria do not grant PR, merge, or release authority.

## Routing

- **Product coordinator:** owns the shared-contract record and the single architecture return.
- **Module A Task coordinator:** owns affected-slice replanning, preservation of independent
  evidence, and local acceptance within the revised boundary.
- **Module B Task coordinator:** owns the bounded adapter correction and local acceptance within the
  revised boundary.
- **Module C Task coordinator:** continues locally; no duplicate decision or status relay is needed.
- Route back to Product only if the versioned decision leaves a shared semantic, dependency/order,
  migration, or material risk question unresolved. Report `ESCALATION_REQUIRED` once with that
  bounded question and pause only its dependent work. After revised boundaries are acknowledged,
  A and B may report `ACTIVE` with the decision evidence pointer. `READY_FOR_INTEGRATION` requires a
  current Change Review and a ready PR when PR creation is authorized. `DONE` requires manual merge
  and FINAL_PASS on unchanged main. Neither state is currently supported.

## Chronological operation log

1. Verified the request hash and matched the corrected process commit to its recorded tree.
2. Reconciled the accepted direction as v2, with v1 superseded only on the changed shared surface;
   noted that the immutable v2 decision identity is absent.
3. Classified impact: A partially affected, B directly affected, C unaffected.
4. Preserved all WIP and evidence, invalidating only v1-dependent assumptions, plans, or verdicts.
5. Selected the versioned architecture return as the first evidence-producing action and defined
   the smallest subsequent actions and routing for A and B.
6. Performed no repository, task, service, merge, release, or other external action.

## Limitations

This response is based only on the corrected skill and the synthetic request. It did not inspect
the v2 contract, module repositories, diffs, task state, tests, reviews, PRs, or CI, and it executed
no behavioral validation. Therefore it cannot identify exact changed paths, prove that A’s tests
are independent, validate B’s future mapping, or claim integration or release readiness.
