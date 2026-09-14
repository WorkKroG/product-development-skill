# Transfer Package Verification

Initial verification: 2026-09-05. Package update: 2026-09-06.

Verified during preparation:

- All seven baseline files matched the source installed product-development-cycle: checksums and direct directory comparison succeeded.
- All seven source-skill files were read.
- Nine Recipes files were extracted from the specified immutable commit, not from an old working checkout.
- All 22 local links in the seven package documents were rechecked; no targets were missing.
- AUDIT.md contains 24 entries A01–A24; EVALUATION.md contains 41 unique scenarios E01–E41.
- No unfilled operational markers remain in the documents; remaining decisions are explicit.
- The independent PLAN_PASS for Task 6 was reread through gh as a historical source.
- The Recipes working tree remained unchanged.

An author reconciliation covered scope, provenance, the distinction between proposals and accepted
rules, permissions, temporary placement, and evidence limitations.

During the update, the agreed architecture evolution was propagated through SPEC, README, AUDIT,
SOURCES, HANDOFF, and EVALUATION. The distinction between future vision and current scope, revision
of the growth plan, load measurability, preservation of reusable code, and permissibility of replacing
the first prototype without a mandatory rewrite were checked.

In addition, the early assessment was moved before Journey and made lighter: the former 4.5 was
replaced with 3.5 in the future-process map. Gate order, Positioning/3.5/Journey/8 boundaries, reuse
of research, and transfer of existing evidence were checked. The change is reflected in the
specification, audit, sources, handoff, and four new scenarios E38–E41. Rechecking the seven baseline
checksums, 22 local links, and ID sequences succeeded.

Not performed: independent review of this specification, harness implementation, execution of
E01–E41, a pilot, or a new installation/update of the global skill. Link and checksum validation is
not evidence of the quality of future runtime behavior.

## Transfer to the permanent project, 2026-09-06

The owner provided the `WorkKroG/product-development-harness` repository, and it was checked through
authenticated gh: it was public and empty when cloned. The source skill was preserved in the first
local bootstrap commit. The specification and instructions were prepared separately.

In the adapted portion, nine documents, 15 local links, uniqueness of A01–A24 and E01–E41, the
Positioning → 3.5 → Journey order, and invariance of the seven baseline hashes were checked. Private
URLs/local paths/IDs from the source coordination were removed from published documents; the exact
source package was preserved in `.local-handoff/`, excluded from Git. A Git ignore check confirmed
exclusion of the private SOURCES.md and historical files.

AGENTS.md and docs/PROJECT_STATUS.md were added with the accepted decisions, models, single gh access,
and next step: the first-working-version plan. Bootstrap does not include public push, scenario
execution, installation, or harness implementation.
