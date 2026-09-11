# Part 3 — two WorkItems, TDD, correction, and current review

Immutable private source: `sha256:10d6b00443ad5a5abc795bb22e1269ef92fd2ea7ec9e2a556129760184ed3394`.
The work ran only in a disposable local repository.

WorkItem 1 observed RED before the product module existed, implemented create/schedule/due/reload,
passed 7/7 tests, received independent review with no findings, and was merged locally. WorkItem 2
observed RED for outcome behavior and produced an ordinary 11/11 candidate.

The first seeded-defect exercise found an outcome-persistence defect, but its review package leaked
defect-revealing commit metadata. A later clean review reproduced the defect only retrospectively;
E14 correctly rejected that sequence. Neither attempt receives procedural credit.

The forward rerun used stable candidate S2, a metadata-clean independent review, one actual Important
persistence finding, an internal finding relay with zero owner relay, and correction by the same
WorkItem writer to R2 `b22898391ba2d7d5e377567368b80ccee18e1a97`. A fresh exact-R2 review
returned APPROVED with no findings. The independent rehearsal produced M00–M09 10/10 PASS,
the supplemental whitespace check PASS, and 15/15 product tests PASS. E14 v4 passed at
`sha256:dca74fb51eeb10080de80a75198b3de2a6c68e7f9a00300c502c155a4c690374`.

E12 separately showed that PASS(R) was rejected when the later whitespace requirement changed the
candidate. Merge stayed prohibited until a fresh review covered the new exact head; E12 passed at
`sha256:88f0452617c3f9a83927d5a5e95fb1c86b2a794e9a978f8c1fc88ae8994832ac`.
Detection and rejection of a stale verdict is not an invalid PASS use.

The final reviewed product tree is `a5fce7b8a8c7eafae9349a762c28d4ea50709da9`. Requested
implementation assignments were `gpt-5.6-sol/medium` and review/evaluation assignments were
`gpt-5.6-sol/high`; accepted native assignments and independently verified runtime facts are Unknown.
