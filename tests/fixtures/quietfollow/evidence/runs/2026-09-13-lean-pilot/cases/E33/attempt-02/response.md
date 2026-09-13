# E33 attempt 02 — coordinator response

## Current decision

Replace the proposed separate queue and reminder services with a reminder module in the existing
application process, using the existing persistence boundary and a bounded scheduled dispatcher.
Keep the service split as an architecture hypothesis, not current implementation. Preserve the
prototype, domain model, and persistence tests; they remain useful inputs to the simpler design.
No production rollout is authorized.

## Evidence and proportionality

The prior design premise was an estimate of **50,000 simultaneously due reminders**. The new
provenance is a bounded measurement: **240 reminders/day**, a **9-reminder one-minute peak**, and
**18 ms p95 processing in-process**, with no independent scaling or ownership need. These are not
identical units: the measurement does not directly measure simultaneous concurrency. It does,
however, replace an unsupported scale assumption with observed daily volume, peak arrival rate,
and processing latency, none of which currently establishes a mandatory need for two additional
services or their operational cost.

The current architecture is therefore:

- retain the domain model and persistence behavior;
- run due-reminder selection and processing in one application-owned dispatcher;
- retain idempotent persistence semantics covered by the useful existing tests;
- defer a broker, separate queue service, and separately deployed reminder worker.

This revision avoids treating prior effort as a reason to retain complexity. The preserved work is
reused only where it supports observable reminder behavior in the simpler boundary.

## Smallest next validation

Run one bounded, persistence-backed in-process rehearsal that replays the measured profile: 240
reminders across the test day, including 9 due within one minute. Record processed, missed, and
duplicate counts plus end-to-end processing latency. Do not build new orchestration or monitoring
services for this rehearsal.

Exit criteria:

1. All 240 scheduled reminders are processed once: 0 missed and 0 duplicate outcomes.
2. The 9-reminder one-minute peak completes without backlog remaining after that minute.
3. Measured in-process p95 processing latency is at most 18 ms under the replayed profile.
4. The result is reproducible from the preserved persistence tests and a bounded rehearsal record.

If criterion 3 fails narrowly while correctness holds, retain the simple architecture and inspect
the measured bottleneck before changing topology. A failed correctness criterion blocks any rollout.

## Revisit triggers

Reconsider a queue or separately deployed worker only when representative measurements show at
least one of these conditions:

- a one-minute peak of **90 reminders/minute or more** (10 times the observed 9/minute peak);
- in-process p95 processing latency of **180 ms or more** (10 times the observed 18 ms) at the
  observed 9/minute peak; or
- a demonstrated independent scaling or ownership boundary.

The triggering evidence must be an identified rehearsal or operating measurement, not another
forecast. Crossing a threshold triggers architecture reconsideration, not automatic adoption of a
particular service or broker.

## Next gate

The current missing evidence is the bounded rehearsal result. Until it meets the exit criteria, the
simplified architecture remains a measured next hypothesis and production rollout remains closed.

## Chronological operation log

1. Verified the request file SHA-256 as
   `4f8d0c14f9be60eb729b42b416eba0fa843a219ad009bca4a936368c072f94d7`.
2. Inspected only the frozen request and the corrected workflow skill at
   `0070e4c307e785cfeafae41ee4aa70151de1df7c`, including its routed proportionality,
   quality-gate, coordinator-role, and handoff guidance.
3. Compared the estimated concurrency premise with the supplied bounded measurements and selected
   the minimum architecture supported by current evidence.
4. Preserved useful prototype, domain, and persistence-test work; authorized no implementation,
   service, network, rollout, or external action.
5. Wrote the sole response to `cases/E33/attempt-02/response.md`. Its final SHA-256 is computed only
   after the immutable write and handed off with the executor result, because embedding that hash
   in this file would change the file being hashed.

Limitations: the supplied event is synthetic; the measurement method, observation window, failure
distribution, and simultaneous-concurrency count were not provided. The rehearsal was specified,
not executed, and this response is not release-readiness evidence.
