# Part 4 — release evidence remains distinct from verification

E27 passed because it did not convert green automated checks into release authority: manual
accessibility and backup/restore evidence remained missing, so the release transition stayed blocked.
E28 attempt 2 passed because it identified the missing rehearsal and rollout/rollback gates without
claiming that a rehearsal or production release had occurred.

The current E27 evaluation is bound by
`4d33e04fcb2f8ae68b3a89dedca08ea418dd89ab1b0ca5b9e8e3e4b403ee6c74`.
The current E28 evaluation is bound by
`b287261456e46cf033ff06eb130b7c53c6364db781795a0bba392037361df03b`.
Both verdicts are PASS; production release remains unauthorized and unperformed.
