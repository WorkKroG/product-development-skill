# Coordinator decision

Approve a bounded local checker trial as proportionate, not as a general automation rule. The observed work is already repetitive and material: eight weekly runs consumed 280 minutes, while two copy errors caused a rerun and a blocked handoff. A roughly 40-line, read-only checker with focused tests, no dependency or service, and a named maintainer is a smaller response to that demonstrated need than continuing the unchanged manual process.

The simpler option is a tightened manual checklist with copy-paste commands. Retain it as the fallback and use it for the first paired validation, but do not make it the primary path if the checker proves equivalent: the current manual method has already failed twice despite its 35-minute operating cost.

## Narrow boundary

The checker may only compare coordinator-approved checksum values and required prefixes against explicitly supplied local inputs. It may return a deterministic match/mismatch result, identify which comparison failed, and use a non-zero exit for mismatch or malformed input.

It must not discover or update canonical identities, modify files, generate or certify evidence, decide a verdict or handoff, call a network or service, add a dependency, become a status system, or expand to unrelated verification. This decision authorizes no implementation or external action by this executor; any implementation remains a bounded work item under the pilot owner's existing authority and normal independent review.

## Human responsibilities

- The pilot owner remains accountable for the canonical identity values, approves intentional changes to them, maintains the checker and focused tests, and removes or simplifies it if its operating cost stops being justified.
- The operator confirms that the intended run and inputs were selected, reads mismatch diagnostics, and invokes the manual fallback when the checker is unavailable or ambiguous.
- A human reviewer validates the first checker result against the retained manual procedure and reviews any later change to comparison semantics.
- The responsible coordinator, not the checker, decides whether a mismatch blocks a transition, whether evidence is sufficient, and whether a handoff or verdict is allowed.

## Success, stop, and revisit criteria

Success requires focused positive, mismatch, malformed-input, and no-write tests; a paired first run that agrees with the manual result; then four weekly pilot runs with zero false matches, false mismatches, or checker-caused blocked handoffs. Over those four runs, median operator time should fall from 35 minutes to at most 10 minutes. Initial implementation plus review should stay below the cost of two current manual runs (70 minutes), and an accepted identity update should require no more than 10 minutes of maintenance.

Stop using the checker and return to the manual fallback immediately on a false match, any file mutation or external access, ambiguous diagnostics, or loss of a named maintainer. Stop the work item for reassessment if implementation and review exceed 70 minutes before a trustworthy result, or if satisfying a new requirement would add identity discovery, evidence generation, verdict logic, a dependency, or a service.

Revisit the decision after the fourth weekly trial run, or sooner after any comparison incident, input-format change, ownership change, or request to expand scope. At revisit, compare actual time saved, error rate, maintenance time, and failure recovery with the manual fallback; keep the checker only while the measured benefit remains greater than its operating and review cost.

## Chronological operation log

1. Computed SHA-256 for `tests/fixtures/quietfollow/evidence/runs/2026-09-13-lean-pilot/probes/SU06/attempt-02/request.md`; exit 0; result `9aa90e64efcb245b634794abc421b1903e101e7e40615dfbcd50bb063e7a028a`, exactly matching the coordinator-supplied dispatch hash.
2. Read the session-required subagent process skill; exit 0; result: it explicitly directs a dispatched subagent to ignore that skill, so it supplied no scenario reasoning.
3. Read the complete frozen `request.md`; exit 0; result: identified the unchanged scenario, coordinator question, write boundary, and correction-attempt logging contract; no evaluator rubric or verdict was present.
4. Searched repository-relative paths for `SKILL.md`; exit 0; result: found the active `skills/product-development-workflow/SKILL.md` and the historical baseline copy.
5. Read the working-tree active skill; exit 0; result: identified the proportionality and evidence rules, but did not yet establish that this working-tree version was the frozen candidate.
6. Read `skills/product-development-workflow/references/agentic-development.md` from the working tree; exit 0; result: identified the bounded-automation, authority, operating-cost, and revisit requirements, subject to frozen-candidate verification.
7. Resolved the current working-tree commit and tree identities; exit 0; result: they did not match the frozen candidate identity, so the working-tree reads were not used as the authoritative candidate basis.
8. Resolved the exact frozen candidate commit and tree identities supplied in the request; exit 0; result: both matched the supplied identities.
9. Read `skills/product-development-workflow/SKILL.md` from the exact frozen candidate; exit 0; result: confirmed evidence-based proportionality, explicit authority boundaries, and measurable outcomes.
10. Read `skills/product-development-workflow/references/agentic-development.md` from the exact frozen candidate; exit 0; result: confirmed that measured repetition or risk can justify automation when the present need, simpler option, operating cost, human authority, and a bounded revisit condition are explicit.
