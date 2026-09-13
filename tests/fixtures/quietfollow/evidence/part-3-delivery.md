# Part 3 — review freshness and synthetic delivery history

The disposable product history is preserved in a tracked Git bundle. A contains only its README; B
adds the first tested behavior; C adds outcome behavior with a deliberate blank-outcome defect; D is
the minimal correction; M is a synthetic two-parent merge whose tree exactly matches D. The bundle
contains only the named branches and A/B/C/D/M tags.

E12 attempt 2 rejected a stale review after the candidate changed and required a fresh exact-head
review. E14 exercised independent C review, a focused RED observation, the minimal D correction,
GREEN verification, and fresh D review. E13 attempt 2 correctly rejected a stale FINAL for A and
accepted closure only for unchanged local synthetic M; it did not claim release readiness.

Current evaluation SHA-256 values:

- E12 — `1b53646841e272289cb7916fc593235f1b87183bd279a4618dd96120fafefbd7`.
- E14 — `213f295f3a8bcf7c27aab544af6d4ea2aa9385ad9f26e8d97b79a57aab9b6be6`.
- E13 — `8859d2b12e06f64801a3934c008b3080b03a890f0949d3b9a8eea61c0329f413`.

All three current verdicts are PASS. Superseded attempts remain tracked as non-credit history.
