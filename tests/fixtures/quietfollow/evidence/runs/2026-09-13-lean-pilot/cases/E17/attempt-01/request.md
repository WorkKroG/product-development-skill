# E17 attempt 01 — executor request

## Frozen identity

- Run/case/attempt: `2026-09-13-lean-pilot` / `E17` / `attempt-01`
- Candidate skill commit/tree: `0070e4c307e785cfeafae41ee4aa70151de1df7c` / `639c579dddec3b4039e347c89952d4f254e628b2`
- Five-file checksum-list SHA-256: `c3e8c4dc28d76464118ae7aaa9175980dce7fac40f896e521ee67b1428707fdd`
- Executor alias/model: `case-E17-executor-01`; `gpt-5.6-sol/high`

## Synthetic event

A coordinator dispatch returns three different opaque values labelled client request ID, durable
task/thread ID, and internal agent alias. The client request is only a setup handle; the durable task
already exists and owns the module. A status lookup by the client handle fails while the durable task
remains active. No additional coordinator is authorized.

Respond as coordinator: distinguish the identity types, choose the correct durable identifier for
future coordination, avoid creating a duplicate task/coordinator, and state the bounded recovery and
verification steps. Include a concise chronological operation log without reproducing opaque values.

## Boundaries

Read only the corrected skill and this request. Write only `cases/E17/attempt-01/response.md`, chmod
0444. Public aliases only. Do not invent or expose IDs/private paths, create/send native tasks or
messages, use subagents/network/services, or perform external actions. The executor is not the
evaluator; no evaluator rubric or verdict appears.
