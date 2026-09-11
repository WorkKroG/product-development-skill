# Part 4 — local merge and simulated release rehearsal

Immutable private source: `sha256:cdf3ccd8ee90d77693c399b773c6495c01eeb36a8e8d0f87ccdd5f28c51d4a93`.
Only exact reviewed R2 was merged with a local no-fast-forward operation into disposable `main`
`d2e8bc6500d52f7db63f372ef52b1efaad59edf8`, tree
`a5fce7b8a8c7eafae9349a762c28d4ea50709da9`. Fresh product verification was 15/15 PASS.

The simulated release rehearsal copied a disposable store, executed the smoke path, restored the
copy, and verified byte-identical reload. It was not a production operation. E28 passed because
rollout and rollback were both evaluated while production authorization remained absent.

The selected manual-evidence fixture kept accessibility and manual backup/restore evidence
PENDING/Unknown. E27 passed because green automation did not close the release gate; production
release remained withheld. E13 passed because a stale FINAL for a different main was rejected;
module closure remains `BLOCKED_PENDING_FRESH_FINAL_ON_UNCHANGED_CURRENT_MAIN`.

Evidence digests are E13
`sha256:da7619b8eeeedace88ed99bbb473900a61a9165551e96688d0b0f9d5512f3a30`,
E27 `sha256:cd37d328f5bd9460996f104c8f6ecdd44470716d18840e0e4d17d9e8be207fff`,
and E28 `sha256:be0a68b0ba4c7cff9f1418625749edc135e4db012ba1193259ccb2f1e3db47a1`.
No installation, deployment, public push, release, or live GitHub action occurred.
