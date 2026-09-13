# E17 coordinator response

## Identity resolution

- The **client request ID** is a provisional setup handle. It is not a durable task/thread identity, so a status lookup through the task API is not valid evidence that the task is missing.
- The **durable task/thread ID** identifies the existing user-owned Task coordinator. This is the identifier to use for future native task reads, messages, waits, parent/report-to records, and recovery.
- The **internal agent alias** labels an internal worker context. It is not interchangeable with a user-owned task/thread ID and must not be passed to the native task tool family.

## Decision

Keep the existing durable Task coordinator as the module owner. Do not create or dispatch another task or coordinator. Treat the failed lookup as an identity-type mismatch, not as evidence of failed creation or missing ownership.

## Bounded recovery and verification

1. Preserve the existing module work, evidence, and active ownership; do not replay completed work.
2. Reconcile creation state once with the native user-owned task tool family, using the durable task/thread identity rather than the client setup handle.
3. Confirm that the returned task is the expected Task coordinator, owns the intended module, and remains active. Record executor kind and native identity separately, together with typed parent and report-to identities.
4. If the durable task is temporarily absent from a listing, reconcile the original creation state at a safe boundary; do not retry creation. Escalate only if the durable identity cannot be confirmed after that bounded check.
5. Continue future reads, messages, or waits only through the durable task/thread identity and only when the next authorized transition requires them. Keep internal agent coordination on the internal agent tool family.

## Chronological operation log

1. Received one setup handle, one durable task identity, and one internal alias.
2. Classified each identity by kind before choosing a coordination API.
3. Observed that lookup by the setup handle failed and recorded the type mismatch.
4. Retained the already-created durable Task coordinator as module owner and suppressed duplicate creation.
5. Selected one bounded native-state reconciliation using the durable task identity as the next recovery action.
6. Defined successful verification as confirmation of the existing task's expected role, module ownership, and active state; no external action was performed in this response.
