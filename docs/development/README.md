# Development documentation

These files explain development of the skill itself. Users should start with the
[repository README](../../README.md), [installation](../installation.md), and
[usage](../usage.md). Do not copy these development records into a consumer project
or load historical plans as current skill instructions.

## Navigation

- [Project direction](PROJECT_STATUS.md): current scope, next step, evidence limits.
- [Repository instructions](../../AGENTS.md): contributor authority, coordination, models, and GitHub access.
- [Specification](SPEC.md): accepted principles and explicitly labeled proposals.
- [Audit](AUDIT.md): A01–A24 findings and proposed treatment.
- [Evaluation program](EVALUATION.md): E01–E41 scenarios, not executed results.
- [Synthetic validation](validation.md): bounded Module 6 outcomes and limitations.
- [Sources and provenance](SOURCES.md): original material and publication boundaries.
- [Historical handoff](HANDOFF.md) and [transfer verification](VERIFICATION.md): dated development context.
- [Historical plans](plans/): plans for earlier implementation stages, not current execution authority.

## Verification

Run from the repository root with Python 3 and `shasum` available:

```sh
python3 -B -m unittest discover -s tests -v
python3 -B -m unittest tests.test_skill_contract -v
shasum -a 256 -c BASELINE.sha256
python3 scripts/check_workflow.py \
  --root . \
  --review-state tests/fixtures/review-state/valid-final.json \
  --json
```

The test suite checks package and structural contracts. The checksum command
checks the exact seven-file historical baseline. Neither establishes behavioral
correctness or successful installation in Codex.

The checker evaluates C01–C12 against supplied inputs. Its synthetic review-state
file is an offline fixture, not an actual review or proof of Git, GitHub, Codex,
reviewer, or model identity. The result includes `revision`, ordered `passed` and
`failed` IDs, and twelve `checks` with relative evidence. `revision` is a SHA-256
identity of selected structural content, excluding review-state and live runtime
state. Without `--json`, the report is equivalent plain text.

- Exit `0`: all structural checks pass.
- Exit `1`: valid inputs, with failed structural checks.
- Exit `2`: unusable arguments or review-state; JSON post-parse errors contain an
  empty result core and stable `code`/`message` fields.

Check Markdown links and changed heading anchors when moving or translating docs.
Review the exact candidate independently before integration; later changes
invalidate that recommendation. Merge remains manual.

On 2026-09-14, the documentation's copy, existing-destination guard, replacement,
and restore operations were exercised in a disposable local repository using the
skill from `83ba5f5a3f4cac6e3cc69f03c22aae5a97266c37`. File comparisons passed.
The source was a local Git clone, not an end-to-end remote installation; no Codex
discovery, loaded runtime identity, or real-project adoption was established.

## Layout and historical records

The active installable skill is `skills/product-development-workflow/`. `baseline/`
is preserved byte-for-byte; `BASELINE.sha256` remains at the root so its original
relative paths stay valid. Tests, fixtures, and the existing checker remain
development tools, not installation requirements.

Project documents were relocated here and translated to English. Historical plans
retain their dates, decisions, and historical file-path examples; those examples
are not instructions to execute against the current layout. Root project records
now live here, `docs/PROJECT_STATUS.md` and `docs/validation.md` moved here, and the
former `docs/superpowers/plans/` is now `docs/development/plans/`.

Ignored private handoff material is not public documentation or active guidance.
Do not add it to Git. No new license is inferred or introduced by this reorganization.
