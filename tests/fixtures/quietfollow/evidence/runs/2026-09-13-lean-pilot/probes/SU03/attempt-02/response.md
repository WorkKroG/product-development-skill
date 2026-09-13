# SU03 recovery classification

## Current gate

Gate 14 — Verification, limited to recovery of the three behavior-check records whose raw evidence and native result were lost. The loss reopens only those checks; it does not invalidate unrelated evidence that still has an intact, verified identity.

## Evidence found

- The two unrelated raw artifacts remain `applicable-covered` for their own checks because the scenario states that their bytes remain intact and their hashes are verified. Their validity does not extend to any of the three missing checks.
- The prior summary remains useful historical context: it records that an earlier run reported three passes. It is not current decision-grade evidence for those passes because the underlying request, response, evaluation, and native result can no longer be inspected or tied to the claimed outcomes.
- The frozen request states that the three affected checks can be rerun locally with bounded synthetic inputs and no external action.

## Missing or assumed

- Each of the three reported passes is `applicable-missing` for current credit. The summary alone cannot establish the exact input bytes, candidate binding, observed output, evaluation basis, exit status, or result provenance.
- The lost native platform result is `Unknown` and receives no current credit. It must not be reconstructed from the summary or represented as a fresh platform observation.
- No defect in the candidate is implied by evidence loss. The gap is in proof, not automatically in behavior.

## Risks

Crediting the summary would turn an uninspectable claim into a pass. Replaying all checks would needlessly disturb still-valid evidence. Describing a local rerun as recovery of the old native result would invent provenance.

## Recommended next action

Rerun exactly the three missing behavior checks locally against the unchanged frozen candidate, using the same bounded synthetic scenario inputs. Retain each new request, response, and independent evaluation as raw bytes; record their hashes, exact candidate binding, chronological command/result facts, and explicit local exit results. Do not rerun the two unaffected checks and do not seek an external or platform action merely to imitate the missing native record.

Preserve the prior summary unchanged in its historical location. Label its three pass claims as historical and non-credit due to lost underlying evidence, link it to the loss/recovery record and the fresh rerun evidence, and keep the two surviving artifacts separately identified. Do not synthesize missing raw files, backfill old hashes, or assert native platform provenance that was not observed.

## Exit criteria

The affected verification gap closes only when:

1. all three bounded reruns identify the unchanged candidate and exact scenario input;
2. raw request, response, and independent evaluation bytes for every rerun are retained with verifiable hashes;
3. the operation record contains chronological actions, exit facts, and explicit local results;
4. each current verdict is supported by its own fresh evidence, with limitations recorded;
5. the old native result remains explicitly `Unknown`/non-credit rather than reconstructed;
6. the two unrelated verified artifacts remain unchanged and credited only within their original scope; and
7. the prior summary is preserved as historical context and clearly distinguished from current evidence.

After these criteria are met, reassess Gate 14 from the first remaining applicable missing check. Do not infer release readiness; Gate 15 is next only if every other applicable verification exit need is also satisfied.

## Operation log

1. Computed SHA-256 for `tests/fixtures/quietfollow/evidence/runs/2026-09-13-lean-pilot/probes/SU03/attempt-02/request.md`; exit 0; result `b4159f9ed151afc2c9d96d4720a0c6cb232eebe2c781321e3557fd9106197905`, exactly matching the coordinator-supplied dispatch hash.
2. Read `tests/fixtures/quietfollow/evidence/runs/2026-09-13-lean-pilot/probes/SU03/attempt-02/request.md`; exit 0; obtained the frozen scenario, evidence-loss boundary, write restriction, and correction-attempt logging contract.
3. Listed the frozen candidate tree; exit 0; confirmed the active skill and its routed reference files are present under `skills/product-development-workflow/`.
4. Read the frozen candidate's `skills/product-development-workflow/SKILL.md`; exit 0; obtained the evidence-preservation, non-fabrication, gate-routing, recovery, entry-response, and completion rules.
5. Read the frozen candidate's `skills/product-development-workflow/references/quality-gates.md`; exit 0; obtained the four evidence states, decision-grade evidence requirements, and rule that a document or prior result alone does not establish readiness.
6. Read the frozen candidate's `skills/product-development-workflow/references/codex-runtime.md`; exit 0; obtained the fresh-state recovery and provenance rules, including that prompt text does not prove a native runtime fact.
7. Read the frozen candidate's `skills/product-development-workflow/references/agentic-development.md`; exit 0; obtained the recovery rule to identify preserved and lost results, compare restoration with bounded rerun, retain valid evidence, and never reconstruct old hashes from summaries.
8. Read the frozen candidate's `skills/product-development-workflow/references/lifecycle.md`; exit 0; confirmed Gate 14 requires exact-candidate verification evidence and that Gate 15 cannot begin from incomplete verification evidence alone.
