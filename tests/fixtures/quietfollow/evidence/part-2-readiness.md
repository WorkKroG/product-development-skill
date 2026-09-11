# Part 2 — proportional prototype readiness

The final readiness graph limits the candidate to one Python standard-library `Tracker` module and
a command-line unittest/rehearsal runner using synthetic local data. The observable path is create
contact → schedule follow-up → query due work → record outcome → reconstruct from the same JSON
file. Unknown contacts and follow-ups and unreadable stores fail explicitly without mutation.

The current graph is readiness package v8
(`sha256:9b6b04c25cf5dbc80a26714250f1301f7dc60136a56022882a95398700b4e8b2`),
verification matrix v6
(`sha256:9d491b2d89627bfa0e6908481cc28173a5962c77fd2b7e1bd88d6c427fefc533`),
rehearsal script v6
(`sha256:7a587acc46aad4546ecbfb77a57003bb28d94f9661e76b7ca8dc0d506b7b5334`),
and Challenge v8
(`sha256:9180eb3c16b1ce271d3195e62f0794ca3cdf444ec1407442841d4ba05ee147f4`).
Challenge v8 closed the prior `KeyError`/`ValueError` contract mismatch and returned
CHALLENGE_PASS with no findings.

UX evidence covers local success, empty, invalid, corrupt, interruption, and reload states.
Risk covers synthetic-data privacy, same-file lifecycle, failure without overwrite, and explicit
deferred manual accessibility and backup/restore evidence. The architecture vision allows a future
replaceable multi-user service, but the current design is deliberately one JSON-backed module.
Accounts, servers, databases, queues, caches, sync, analytics, and transports are deferred until a
recorded trigger, evidence, and separately authorized decision. E31 v2 passed at
`sha256:4aefad4e51c82dd7abc650d43eae48fa1faae81970108673fbf89444fb7b83dd`;
the future infrastructure transition remained DEFERRED.

E39 reused the unchanged Gate 3.5 input and refreshed only a seeded encrypted-backup cost delta.
The local range remained 0–5 EUR/month; 10–20 EUR/month was scoped to the optional backup, and a
10–25 EUR/month envelope was only conditional sensitivity. E39 passed at
`sha256:a07886f96850d6f6f1ed1854d3ea6f489be11232618fd27fd97d1c3b7fbfe625`;
Gate 8, payment, and provisioning stayed open or paused.

Seeded decision v2
(`sha256:e019bac301aa57d9352d1ca5ffa21df7c69a3448be96c6ed4701df2018d9bfc8`)
authorized only the exact zero-spend/local/synthetic Task 4 package. It did not authorize MVP,
network access, real data, services, dependencies, GitHub, deployment, or release. Requested
assignments were `gpt-5.6-sol/high`; accepted and independently verified runtime facts are Unknown.
