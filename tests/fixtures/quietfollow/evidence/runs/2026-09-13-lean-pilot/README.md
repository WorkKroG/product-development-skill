# Module 6 lean QuietFollow pilot

This run root contains only bounded, local, synthetic pilot evidence. External actions are
forbidden: no GitHub or other service mutation, real user data, spending, installation,
deployment, publication, merge, or release is authorized.

Each case or probe attempt has exactly three primary tracked files:

1. `request.md`, frozen before executor dispatch;
2. `response.md`, containing the executor's answer and concise chronological operation log; and
3. `evaluation.md`, containing a frozen evaluator-request prefix followed by the independent
   evaluation.

`index.json` is the single shared, compact, hand-maintained index for candidate identity, attempt
identities, hashes, byte counts, provenance facts, verdicts, and dependent states. It is ordinary
JSON, not a generated manifest or schema. Later tasks add attempts and named support files only as
specified by the approved plan.

This root makes no readiness claim. Work stops after the approved Task 9 exact-head Change Review
recommendation. Task 10, FINAL integration review, installation, push, pull request, publication,
merge, external service action, real deployment, and release remain outside the authorized scope.
