# QuietFollow architecture revision

## Current gate

Technical plan — the reminder architecture decision is reopened because measured load no longer supports the prior scaling premise.

## Evidence found

| Evidence | Units and provenance | Implication |
|---|---|---|
| Prior load assumption | 50,000 simultaneously due reminders; an estimate with no measurement provenance supplied | It justified exploring separate queue and reminder services, but is not decision-grade capacity evidence. |
| Bounded current measurement | 240 reminders/day and a peak of 9 reminders in one minute | The observed load is a low daily volume with a modest short peak. The one-minute rate does not establish simultaneous concurrency, so it should not be converted into or directly compared as a concurrency count. |
| Bounded current measurement | p95 processing time of 18 ms per reminder in-process | The current path has substantial apparent processing headroom at the observed peak, although p95 is neither a maximum nor an end-to-end reliability result. |
| Current organizational evidence | No independent scaling or ownership need | Separate deployment boundaries currently add coordination and operational cost without an evidenced benefit. |
| Existing implementation evidence | Prototype, domain model, and persistence tests remain useful | The architecture can be simplified without discarding validated domain and persistence work. |

## Decision

For the nearest stage, withdraw the proposal for separate queue and reminder services. Keep reminders in one deployable application, using the existing domain model and persistence-backed in-process processing path. Preserve the prototype and persistence tests, and retain reusable business logic from any service-oriented exploration, but stop investing in separate deployment, queue, and ownership boundaries.

This is an architecture-plan revision only. It does not authorize production rollout.

## Missing or assumed

- The measurement window, environment, sampling method, raw distribution, and end-to-end delivery latency are not supplied.
- Crash recovery, retry, duplicate handling, and reminder-loss behavior have not been demonstrated by the stated measurements.
- No latency or reliability target, cost boundary, backlog threshold, or sustained-load profile is provided.
- The bounded measurement is treated as valid for the present decision, not as proof of future production capacity.

## Risks

- A single process can lose or duplicate work if persistence, claiming, retry, and restart behavior are incomplete.
- A short measurement window may miss seasonal or campaign-driven bursts.
- Simplification could accidentally discard useful tested logic; preservation should be deliberate even when deployment complexity is removed.

## Recommended next action

Run one bounded restart-and-retry validation against the persistence-backed in-process path: create due reminders, interrupt processing at the claim/completion boundary, restart, and record whether every reminder reaches a defined terminal state and whether duplicates follow an explicit rule. Reuse the existing persistence tests and prototype fixtures; do not introduce a queue or new service for this check.

## Exit criteria

Exit this architecture revalidation when the bounded check provides reproducible evidence that:

- no persisted due reminder is silently lost across interruption and restart;
- duplicate behavior is prevented or explicitly defined and accepted;
- the observed completion timing is recorded in the same units as the test load; and
- the technical plan identifies the single-deployable design as current, preserves the useful prototype/domain/persistence assets, and keeps rollout unapproved.

The next gate is delivery planning for the simplified prototype path, limited to non-production validation.

## Revisit triggers

Reconsider a queue or separate reminder service only when evidence shows at least one of the following:

- measured peaks, backlog growth, or end-to-end latency approach an agreed capacity or service-level boundary;
- restart/retry correctness cannot be achieved proportionally in the single deployable;
- reminder processing requires independent scaling, release cadence, fault isolation, or ownership;
- a materially different load profile, including evidenced high concurrency, invalidates the bounded measurement; or
- an approved production stage introduces reliability or operational requirements the current design cannot meet.

## Operation log

1. Verified the frozen request checksum and matched the loaded candidate identity to it.
2. Separated the prior estimate from the bounded measurement and kept their differing units explicit.
3. Revised the nearest-stage architecture proportionally, preserving useful artifacts while removing unsupported service complexity.
4. Selected one recovery-focused validation and stated exit and revisit triggers.
5. Performed no network, service, production, rollout, or other external action.

## Limitations

This response relies only on the supplied synthetic event and corrected workflow skill. It does not inspect raw measurement data, execute the proposed validation, establish production readiness, or approve rollout.
