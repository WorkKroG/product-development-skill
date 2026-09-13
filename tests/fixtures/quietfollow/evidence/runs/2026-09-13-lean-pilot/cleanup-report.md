# Task 1 cleanup report

## Authority and boundary

Cleanup was performed under approved plan `MODULE6-LEAN-PLAN-v1` at commit
`feebad5d67614da5d25439c0ae38c2164becdbf2`, tree
`db52321f6fe978a03953f0ed6c5c3e2d6bd88370`. Only the nine exact ignored regular files below were
deleted. No wildcard or recursive deletion was used.

## Deleted targets

All paths are below `.superpowers/sdd/2026-09-12-module-6-evidence-retention-recovery/`.

| Target | Classification | Pre-SHA-256 | Mode | Bytes | Action |
|---|---|---|---:|---:|---|
| `checks/archive-validator.py` | cancelled infrastructure code, not history/result/product | `e66c20dadbf1d26df13e654a45b1406fd22062913133a5d89ce027429bdb6392` | `0444` | 192771 | deleted after exact type/hash check |
| `checks/archive-validator-tests.py` | cancelled infrastructure test, not history/result/product | `6f8f08cbfc4680d4e76d8b318c24039b933e4add740b261b8296a080f9a5bb1b` | `0644` | 197350 | deleted after exact type/hash check |
| `checks/build-live-manifest.py` | cancelled infrastructure code, not history/result/product | `5b5df5454edacbbcca5c998bc78c7caa2c5b63e480cad6dfda8649f48b8ccbb9` | `0444` | 6957 | deleted after exact type/hash check |
| `checks/materialize-task1.py` | cancelled infrastructure code, not history/result/product | `472e520b687564c304ac3ecb67fb75ec1d9dcce5c45ff60d8e25b89d64673aa4` | `0444` | 9515 | deleted after exact type/hash check |
| `checks/bundle-contamination.json` | cancelled infrastructure config, not history/result/product | `21f8b0132630ecc5bbbec0871a6ab401248f735711d8c75e1f101a360a581248` | `0444` | 526 | deleted after exact type/hash check |
| `checks/public-alias-vocabulary.txt` | cancelled infrastructure config, not history/result/product | `807217e878f2576649eabecdf59ad48b101ca3fb165e265761afbd0dad87d642` | `0444` | 1210 | deleted after exact type/hash check |
| `checks/public-alias-vocabulary.sha256` | cancelled infrastructure sidecar, not history/result/product | `a56d49af3115126648a416c45b41cdefd179fdbda8dc28446eceab8961a51b86` | `0444` | 94 | deleted after exact type/hash check |
| `manifest.json` | cancelled generated live-root index, not history/result/product | `dedb75fcbd97945aa4f7fc7c1cbbc8527eb20b59e2021e0c1db210484bccd3ac` | `0644` | 36251 | deleted after exact type/hash check |
| `manifest.sha256` | cancelled generated live-root sidecar, not history/result/product | `940e6b7939f73e16bd20c32c0b8bbf251a37c629583596fe493cff30e1b76564` | `0644` | 80 | deleted after exact type/hash check |

## Preservation proof

- Before cleanup, the original historical root
  `.superpowers/sdd/2026-09-11-module-6-quietfollow-pilot/` contained 61 regular files, no symlinks,
  and aggregate sorted per-file inventory digest
  `6c7165e066a3190f68e5baf5d35a68bc51a918a0a89b08b221a1e5bdafa04d5e`.
- After cleanup, that root still contains 61 regular files, no symlinks, and the same aggregate
  digest.
- Before cleanup, the recovery root contained 81 regular files and no symlinks. Its 72 non-target
  files had aggregate sorted per-file inventory digest
  `718898fb1e578cabaeb431848cc60adc0a01428ff9d0fd5ff21a4d6bb7bdbc39`.
- After cleanup, the recovery root contains exactly 72 regular files, no symlinks, and aggregate
  digest `718898fb1e578cabaeb431848cc60adc0a01428ff9d0fd5ff21a4d6bb7bdbc39`.
- Every one of the nine exact targets was checked absent after cleanup. The count and identical
  sorted per-file hash inventory prove every non-target recovery file remains byte-for-byte.

The aggregate inventory digest is SHA-256 over the C-locale-sorted full `shasum -a 256` output for
all regular files in the named root.

## Recovery limitation

The deleted targets were ignored and untracked, so Git cannot restore their contents. This report
preserves their identity, classification, pre-delete hash, mode, and size only; it is not a content
backup. Existing committed history was not altered.
