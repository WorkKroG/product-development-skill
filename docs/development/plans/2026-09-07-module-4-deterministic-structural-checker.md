# Product Development Workflow — Module 4 Deterministic Structural Checker Implementation Plan

Historical plan. File-path examples describe the layout at the time; see the
[development index](../README.md) for current locations and scope.

> **For agentic implementation:** REQUIRED SUB-SKILL: `superpowers:subagent-driven-development`, with the Task topology from `AGENTS.md` and `SPEC.md` §§6–8. Implementation and Change Review run as separate bounded internal agent sessions under the Module 4 Task coordinator. Do not begin implementation until the owner accepts this exact plan version in the Task.

**Identifier:** `MODULE4-PLAN-v1`. Review identity is the SHA-256 of this file plus the exact base below; any plan-content or base change invalidates `PLAN_PASS`.

**Goal:** add a deterministic structural checker with no external dependencies that reports C01–C12, rejects stale review identities and binding leaks in portable files, and never represents structural fixtures as behavioral or live evidence.

**Architecture:** one Python-standard-library CLI handles input validation, deterministic file selection, twelve independent check functions, and stable text/JSON output. A separate unittest suite copies the repository into temporary isolated trees and applies one controlled mutation at a time. JSON review-state is provided input: the checker compares phase identities but does not attest live GitHub, Codex, or Git state.

**Technologies:** Python 3 standard library (`argparse`, `hashlib`, `json`, `pathlib`, `re`, `unittest`, `subprocess`, `tempfile`, `shutil`), Markdown/YAML text contracts, Git.

**Specification:** `SPEC.md` §§6–10 and §12; `AUDIT.md` A07, A11, A13, A14, A18–A21; `EVALUATION.md` E12, E13, E17–E22, E26–E30, E38–E41; historical Task 4 from `docs/superpowers/plans/2026-09-06-first-working-version.md`, reconciled with the naming and coordination decisions accepted on 2026-09-07.

## General constraints

- Exact base: `f008c78980113f67f5bc73c7e93adcf8ad003423`, freshly obtained from `origin/main` on 2026-09-07; `HEAD`, `FETCH_HEAD`, and `origin/main` matched.
- The active entrypoint and invocation remain `skills/product-development-workflow/SKILL.md` and `$product-development-workflow`; the repository slug and historical baseline retain their old names.
- Replace historical `scripts/check_harness.py` with `scripts/check_workflow.py`. This is the only naming delta; do not reopen the product name.
- Current and target maturity are `working-prototype`: this module adds reproducible structural evidence, not runtime enforcement or proof of release readiness.
- Architecture is the owner-accepted 2026-09-07 design in `SPEC.md` §§6–8, implemented in Module 3 and integrated at the exact base above.
- Python standard library only. Do not install a package, plugin, skill, runtime, or scheduler.
- Preserve `baseline/product-development-cycle/`, `BASELINE.sha256`, `tests/test_skill_contract.py`, the global skill, historical plans, `.local-handoff/`, and unrelated WIP. Fixtures are not the evidence-owning system.
- Out of scope: Task 5, runtime service, telemetry, Hydra, pilot, GitHub mutations, push, PR, merge, installation, publication, CI redesign, or release.
- Required output limitation: `Structural checks do not prove behavioral correctness.`
- Planning/PLAN: `gpt-5.6-sol/high`; Implementation: `gpt-5.6-sol/medium`; Change Review: `gpt-5.6-sol/high`; FINAL: `gpt-6-astra/high`. Record requested assignment, accepted native assignment, and independently confirmed runtime fact separately.

---

## File map and boundaries

### Only the plan changes now

- Create `docs/superpowers/plans/2026-09-07-module-4-deterministic-structural-checker.md` — this reviewed plan, without temporary task/agent IDs or machine-specific paths.

### One future Implementation Work Item

- Create `scripts/check_workflow.py` — CLI, input validation, content revision, C01–C12, deterministic output, and exit codes.
- Create `tests/test_check_workflow.py` — CLI contract, positive/negative cases, input errors, phase identities, and exact C10/C11 isolation.
- Create `tests/fixtures/review-state/valid-final.json` — synthetic FINAL state with equal reviewed/current identities.
- Create `tests/fixtures/review-state/valid-change-review.json` — synthetic Change Review state with equal base/head identities.
- Create `tests/fixtures/invalid/stale-final.json` — differs from `valid-final.json` only in `current.main_sha` and fails exactly C10.
- Create `tests/fixtures/invalid/incomplete-review-state.json` — incomplete phase identity; proves invalid-input handling, not a mechanical FAIL.
- Create `tests/fixtures/invalid/leaked-binding.txt` — inert synthetic leak added only to a copy of an active file; fails exactly C11.
- Modify `README.md` — command, exit codes, review-state boundary, JSON, and result limitation.
- Modify `docs/PROJECT_STATUS.md` — after implementation, replace stale Module 3 next action with a concise Module 4 navigation/evidence pointer, without copying live Issue/PR/CI state.

No other paths may change. `CHANGELOG.md` is a C02/C11/C12 input but is not edited. Needing another active file means changing the plan and obtaining a new PLAN review.

## CLI and data contract

```sh
python3 scripts/check_workflow.py \
  --root . \
  --review-state tests/fixtures/review-state/valid-final.json \
  --json
```

`--root PATH` and `--review-state PATH` are required. A relative review-state resolves from `--root`. An absolute path is accepted only if it remains inside root after resolution; escape is invalid input. `--json` selects machine output; otherwise the CLI prints ordered checks, totals, revision, and limitation.

- Exit `0`: all C01–C12 return `PASS`.
- Exit `1`: inputs are usable, but at least one check returns `FAIL`.
- Exit `2`: invocation or input is unusable—missing arguments; root missing/not a directory; review-state missing, unreadable, malformed, or outside root; unsupported phase/verdict; invalid identity types, keys, or format. Incomplete data is not C10 FAIL.

JSON success/mechanical failure always has four required fields:

```json
{"revision":"sha256:0000000000000000000000000000000000000000000000000000000000000000","passed":["C01"],"failed":["C02"],"checks":[{"id":"C01","status":"PASS","evidence":"baseline manifest: 7/7 matched"}]}
```

The zero revision is a format example. A real `revision` is `sha256:` plus 64 lowercase hex characters. The stream starts with `PDW-STRUCTURAL-REVISION-v1\0`, then encodes, in sorted POSIX-relative order, the union of the C02 manifest, seven hard-coded C01 baseline paths, and optional existing `docs/validation.md`. A malformed `BASELINE.sha256` does not redirect reads.

```text
8-byte big-endian path length | UTF-8 path | 1-byte kind | 8-byte big-endian byte length | raw bytes
```

Kind: `F` regular file, `M` missing, `O` other filesystem type. For `M`/`O`, length is zero; symlinks are not followed. Thus a missing required file has a stable revision, while baseline mutation changes revision and C01. Excluded: review-state, `.git`, tests (except the checker as a distribution file), and runtime/native state. Revision identifies structural content, not a Git commit or live-review attestation; it is not copied from the fixture.

For post-parse exit `2` with `--json`, emit the same four fields with `revision: null`, empty arrays, and `error` with stable `code`/`message`. argparse errors use stderr and exit `2`. Evidence contains only repository-relative paths, never absolute machine paths.

A normal result contains exactly twelve C01–C12 records; `passed`/`failed` retain order; `status` is only `PASS`/`FAIL`. Text output ends with the required limitation; JSON stores that phrase at the end of C12 `evidence`, preserving the four-field success schema.

## Observable C01–C12 contracts

| ID | Name | Mechanical PASS condition | Negative test |
|---|---|---|---|
| C01 | `baseline-hashes` | Strictly parse `BASELINE.sha256`; exactly seven paths, no duplicates/extras; all files exist and hashes match. | Change one baseline byte; C01 appears in `failed`. |
| C02 | `required-active-files` | Every file in the exact manifest below is a regular file, not a symlink. | Remove the checker from a copy; exactly C02 fails, with a nonzero repeatable revision. |
| C03 | `relative-links` | In every active-skill Markdown file, parse destinations only from inline Markdown links. Ignore `http`, `https`, `mailto`, and fragment-only destinations. Strip query/fragment from a local destination, reject absolute paths or escape beyond active skill, and require an existing relative file target. | Existing local target with query/fragment passes; SKILL route to `references/missing.md` fails C03. |
| C04 | `metadata` | SKILL has `name: product-development-workflow` and nonempty description; YAML has the correct display name, short description, and default prompt with `$product-development-workflow`. | Change display name; C04 fails. |
| C05 | `gate-order` | Level-2 gates are exactly `0,1,2,3,3.5,4,5,6,7,8,9,10,11,12,13,14,15,16`, without duplicates. | Swap Gate 8/9; C05 fails. |
| C06 | `single-light-viability` | One `## 3.5. Light viability`, no `## 4.5.`, and SKILL has `light Gate 3.5` between `Positioning`/`Journey`; historical Gate 4.5 migration prose is allowed. | Remove `light`; C06 fails. |
| C07 | `five-maturity-stages` | Lifecycle has `working-prototype`, `mvp`, `scale-1`, `scale-2`, `mature`; SKILL has `working prototype`, `MVP`, `scale 1`, `scale 2`, `mature operation`. | Remove a label; C07 fails. |
| C08 | `required-profile-fields` | Profile contains Process identity, Product, Maturity, Architecture, Load profile, Sources of truth, Runtime, Models, Economics, Applicability, and current decision-bearing labels. `Unknown` is required as a default, not evidence. | Remove `Transition evidence required`; C08 fails. |
| C09 | `required-handoff-fields` | The Work package and Review record sections contain every exact label below. | Table-remove each label, including `Work Item/module identity`, `Report to identity`, `Phase`; C09 fails. |
| C10 | `review-identity-consistency` | Phase schema is valid; all `reviewed == current`. Evidence says `provided input; not live owning-system evidence`. | `stale-final.json` fails exactly C10; PLAN/Change Review/FINAL have equal/stale cases. |
| C11 | `forbidden-private-bindings` | Only the public allowlist is scanned for user paths, Recipes binding, runtime UUID, credential prefix, and client-ID marker; evidence does not reveal the match. | Add the leak fixture to a SKILL copy; exactly C11 fails. |
| C12 | `no-placeholder-markers` | Operational files contain no line markers `TBD`, `TODO`, `FIXME`, `XXX`, `IMPLEMENT ME`, `FILL IN`; intentional `Unknown`/template fields in assets are allowed. | Add `TODO: finish workflow` to a reference copy; C12 fails. |

Exact C02 manifest:

```text
scripts/check_workflow.py
BASELINE.sha256
README.md
CHANGELOG.md
docs/PROJECT_STATUS.md
skills/product-development-workflow/SKILL.md
skills/product-development-workflow/agents/openai.yaml
skills/product-development-workflow/assets/AGENTS.template.md
skills/product-development-workflow/assets/PROJECT_STATUS.template.md
skills/product-development-workflow/assets/project-profile.template.md
skills/product-development-workflow/assets/role-prompts.md
skills/product-development-workflow/assets/work-item-and-review-templates.md
skills/product-development-workflow/references/agentic-development.md
skills/product-development-workflow/references/codex-runtime.md
skills/product-development-workflow/references/dependencies.md
skills/product-development-workflow/references/financial-model.md
skills/product-development-workflow/references/lifecycle.md
skills/product-development-workflow/references/quality-gates.md
```

C11 scans exactly:

```text
skills/product-development-workflow/**/*.md
skills/product-development-workflow/**/*.yaml
README.md
CHANGELOG.md
docs/PROJECT_STATUS.md
docs/validation.md (only when present)
```

C11 does not scan `baseline/`, `.local-handoff/`, `tests/`, `SPEC.md`, `AUDIT.md`, `EVALUATION.md`, `HANDOFF.md`, `SOURCES.md`, `VERIFICATION.md`, or plans. Literal `.local-handoff/` is allowed in public safety prose: C11 seeks private bindings, not mentions of the publication exclusion.

C12 scans `SKILL.md`, `agents/openai.yaml`, active `references/`, `README.md`, `CHANGELOG.md`, `docs/PROJECT_STATUS.md`, and optional `docs/validation.md`; `assets/` are excluded because literal `Unknown` and angle-bracket values are required template placeholders.

Exact section-local C09 labels:

```text
Work package / handoff:
Work Item/module identity; Outcome/why; Scope/non-goals; Binding sources; Dependencies;
Maturity identity; Architecture identity; Process identity; Plan identity; Exact base;
Exact head; Allowed paths; Permissions/data/recovery; Acceptance criteria; Checks; Role;
Executor kind; Native ID; Parent identity; Report to identity; Constraints;
Current state/findings; Next action.

Review record:
Phase; Independent reviewer kind; Independent reviewer Native ID;
Reviewed plan hash or base/head/main; Binding sources; Checks; Findings; Verdict;
Invalidation condition.
```

## Review-state schema

A Git SHA is exactly 40 lowercase hex characters; a plan hash is 64. Only these forms are permitted:

```json
{"phase":"PLAN","verdict":"PLAN_PASS","reviewed":{"plan_hash":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","base_sha":"1111111111111111111111111111111111111111"},"current":{"plan_hash":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","base_sha":"1111111111111111111111111111111111111111"}}
```
```json
{"phase":"CHANGE_REVIEW","verdict":"PASS","reviewed":{"base_sha":"1111111111111111111111111111111111111111","head_sha":"2222222222222222222222222222222222222222"},"current":{"base_sha":"1111111111111111111111111111111111111111","head_sha":"2222222222222222222222222222222222222222"}}
```
```json
{"phase":"FINAL","verdict":"FINAL_PASS","reviewed":{"main_sha":"1111111111111111111111111111111111111111"},"current":{"main_sha":"1111111111111111111111111111111111111111"}}
```

Extra/missing keys or schema/type/format/verdict errors produce exit `2`; a valid form with differing identities is C10 failure and exit `1`. Fixtures use clearly synthetic hex and are identified in README as offline inputs. C10 proves internal consistency of provided data, not provenance from GitHub/Codex/Git, a reviewer, or the assigned model.

---

### Task 1: implement and document the single Module 4 Work Item

**Files:** create `scripts/check_workflow.py`, `tests/test_check_workflow.py`, `tests/fixtures/review-state/valid-final.json`, `tests/fixtures/review-state/valid-change-review.json`, `tests/fixtures/invalid/stale-final.json`, `tests/fixtures/invalid/incomplete-review-state.json`, and `tests/fixtures/invalid/leaked-binding.txt`; modify `README.md` and `docs/PROJECT_STATUS.md`; preserve and run `tests/test_skill_contract.py` and `BASELINE.sha256`.

**Interfaces:** accepts `Path root`, `Path review_state`, and current active-file contracts; produces `main(argv: Sequence[str] | None = None) -> int`, C01–C12, four-field JSON, content revision, and exits 0/1/2; does not use network, GitHub/Codex APIs, task IDs, `.git`, private handoff, behavioral fixtures, or scheduler state.

- [ ] **Step 1: load `skill-creator`, test-driven-development, and repository instructions.** The Implementation session reads `AGENTS.md`, exact plan, active SKILL, and delivery/runtime references/templates; records base, plan hash, requested/accepted model facts, allowed paths, and sole-writer status. This does not authorize installation or GitHub action.
- [ ] **Step 2: add synthetic review-state and leak fixtures.** Use only inert fixed examples. `stale-final.json` changes only `current.main_sha`. `leaked-binding.txt` is read by tests and is outside the production C11 allowlist:
  ```text
  Synthetic private binding: /Users/example/Develop/Projects/recipes-v1
  Synthetic repository binding: WorkKroG/recipes-v1
  Synthetic task identity: 11111111-2222-3333-4444-555555555555
  Synthetic credential prefix: ghp_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
  Synthetic provisional identity: client-new-thread:synthetic-only
  ```
- [ ] **Step 3: write failing unit tests for core/revision/C02.** Import the script directly. Test root, contained review-state path, framed revision, JSON/text renderers, and `check_c02(root)`: missing checker → C02 FAIL with stable revision; baseline mutation changes revision; review-state does not; evidence excludes absolute root.
  ```python
  def load_checker_module():
      spec = importlib.util.spec_from_file_location("check_workflow", SCRIPT)
      module = importlib.util.module_from_spec(spec)
      spec.loader.exec_module(module)
      return module
  ```
- [ ] **Step 4: run core tests and confirm RED.** `python3 -B -m unittest tests.test_check_workflow.WorkflowCheckerCoreTest -v`. Expected FAIL because the script/functions are missing; fixture/dependency failure is not RED.
- [ ] **Step 5: implement core types, input helpers, framed revision, renderers, and C02.** Implement the exact C02 manifest and pure helpers. Do not create fake later-check results or assemble registry/CLI yet.
  ```python
  @dataclass(frozen=True)
  class Check:
      id: str
      status: str
      evidence: str
  CHECK_IDS = tuple(f"C{number:02d}" for number in range(1, 13))
  class InputError(ValueError):
      def __init__(self, code: str, message: str):
          super().__init__(message)
          self.code = code
  ```
  Implement `compute_revision(root: Path) -> str` and `check_c02(root: Path) -> Check` using the full framed algorithm and C02 contract above.
- [ ] **Step 6: run core tests and confirm GREEN.** `python3 -B -m unittest tests.test_check_workflow.WorkflowCheckerCoreTest -v`. Expected PASS for containment, renderers, revision, and C02; unimplemented checks do not count as PASS.
- [ ] **Step 7: write failing direct tests for C01, C03–C09, and C12.** Copy the repo without `.git`, `.local-handoff`, bytecode/caches. Call pure checks separately and apply all table mutations. For C03, add an inline link to an existing local file with query/fragment and confirm PASS, then separately replace the target with a missing one and confirm FAIL. For C09, delete every exact label one at a time. Untouched input passes the same function; mutation returns its ID and FAIL.
  ```python
  def assert_check(self, check, expected_id, expected_status):
      self.assertEqual(expected_id, check.id)
      self.assertEqual(expected_status, check.status)
  ```
- [ ] **Step 8: run C01/C03–C09/C12 and confirm RED.** `python3 -B -m unittest tests.test_check_workflow.WorkflowStructuralChecksTest -v`. Expected FAIL because specific functions are absent; C02 is not in this suite.
- [ ] **Step 9: minimally implement C01, C03–C09, and C12.** Follow exact contracts without a generic Markdown/YAML engine. C06 allows historical 4.5; C08/C09 parse named sections; C12 excludes required template values.
- [ ] **Step 10: rerun and confirm GREEN.** `python3 -B -m unittest tests.test_check_workflow.WorkflowStructuralChecksTest -v`.
- [ ] **Step 11: write failing direct schema/identity tests for C10.** Call `parse_review_state(root, path)` and `check_c10(state, relative_source)`; cover equal/stale PLAN, Change Review, and FINAL; invalid/extra keys → stable `InputError`; evidence is redacted.
- [ ] **Step 12: run C10 tests and confirm RED.** `python3 -B -m unittest tests.test_check_workflow.WorkflowReviewIdentityTest -v`.
- [ ] **Step 13: implement phase-aware C10.** Validate exact forms/verdicts/types/lengths before comparing full maps. Do not call Git/GitHub/Codex.
- [ ] **Step 14: rerun C10 and confirm GREEN.** `python3 -B -m unittest tests.test_check_workflow.WorkflowReviewIdentityTest -v`.
- [ ] **Step 15: write failing direct allowlist/rule/redaction tests for C11.** Call `check_c11(root)`; separately test all five rules, redaction, and ignored paths.
- [ ] **Step 16: run C11 tests and confirm RED.** `python3 -B -m unittest tests.test_check_workflow.WorkflowPrivateBindingTest -v`.
- [ ] **Step 17: implement bounded C11 scan.** Use only the declared allowlist and named regex rules; no symlinks, broad walk, private reads, or echoed match.
- [ ] **Step 18: rerun C11 and confirm GREEN.** `python3 -B -m unittest tests.test_check_workflow.WorkflowPrivateBindingTest -v`.
- [ ] **Step 19: write failing full CLI integration tests.** After pure checks, add a subprocess helper. Validate exact JSON/text, order, exits, determinism, redaction, revision invariance, limitation; stale-final → exactly C10; aggregate leak → exactly C11; post-parse errors → empty core plus stable error.
  ```python
  def run_checker(root: Path, review_state: str | None, *, json_output: bool = True):
      command = [sys.executable, str(SCRIPT), "--root", str(root)]
      if review_state is not None:
          command += ["--review-state", review_state]
      if json_output:
          command.append("--json")
      return subprocess.run(command, text=True, capture_output=True, check=False)
  ```
- [ ] **Step 20: run CLI tests and confirm RED.** `python3 -B -m unittest tests.test_check_workflow.WorkflowCheckerCliTest -v`. Expected FAIL because `main()` has not assembled parsing, registry, and outputs.
- [ ] **Step 21: implement final CLI composition.** Implement `main(argv: Sequence[str] | None = None) -> int`, C01–C12 in exact order, revision before checks, review-state before C10, and exits 0/1/2. No temporary stubs.
- [ ] **Step 22: rerun CLI tests and confirm GREEN.** `python3 -B -m unittest tests.test_check_workflow.WorkflowCheckerCliTest -v`.
- [ ] **Step 23: update README and navigation.** Document command, JSON, IDs, exits, review-state, revision, and limitation. PROJECT_STATUS contains only Module 3 base, Module 4 evidence pointer/limitation, and next gate; no Task 5/pilot/install/release/live GitHub claims.
- [ ] **Step 24: perform focused and full verification.**
  ```sh
  python3 -B -m unittest tests.test_check_workflow -v
  python3 -B -m unittest discover -s tests -v
  python3 scripts/check_workflow.py --root . --review-state tests/fixtures/review-state/valid-final.json --json
  shasum -a 256 -c BASELINE.sha256
  git diff --check
  git status --short
  git rev-parse HEAD
  ```
  Expected: tests PASS; checker exit `0`; `passed` = C01–C12; `failed` empty; baseline 7/7. This is structural evidence, not execution of E01–E41.
- [ ] **Step 25: create one local candidate commit.** Changed paths are exactly the nine Work Item paths above plus the accepted plan if uncommitted. `git commit -m "test: add deterministic workflow checks"`. No push, PR, merge, install, or release.
- [ ] **Step 26: perform independent Change Review of the exact candidate.** A fresh read-only agent receives sources, plan/hash, base/head, full diff, paths, checks/fixtures, but not the Implementation conversation. A new commit invalidates PASS; corrections stay in the Work Item.
- [ ] **Step 27: stop at the integration boundary.** `READY_FOR_INTEGRATION` requires current Change Review PASS and an authorized ready PR. Merge is manual. After merges, separate FINAL checks exact current main; drift invalidates FINAL_PASS. Module 4 is not DONE merely because the checker or plan passed.

## Acceptance criteria and risks

1. C01–C12 PASS on the exact candidate, in stable order, with useful relative evidence.
2. Every check has a positive and meaningful structural/mutation negative test, not merely phrases.
3. Stale FINAL fails exactly C10; injected active-path binding fails exactly C11.
4. Missing/incomplete review-state → exit `2`; valid stale identity → exit `1`.
5. C10 covers PLAN, Change Review, and FINAL.
6. C11 uses only the public allowlist and synthetic leak fixture.
7. C12 preserves intentional `Unknown` and angle-bracket template values.
8. `revision` is deterministic and not copied from review-state.
9. Existing 26 tests and baseline 7/7 remain green and unchanged.
10. README/status make no claims about live state, behavior, installation, release readiness, or Task 5.

Risks and mitigations:

- **False confidence:** limitation in both output modes/docs; behavior/pilot remain later work.
- **Brittle text matching:** exact headings, section-local labels, front matter, links, JSON; no engine.
- **Fixture mistaken for live:** review-state excluded from revision, provided-input label, synthetic identities.
- **False positives/secret echo:** exact allowlist, named rules, exclusions, rule + relative path only.
- **Scope creep:** one Work Item; no Task 5, scheduler, telemetry, pilot, install, or CI redesign.

## Plan review and next authorization

PLAN checks the full file by SHA-256 on base `f008c78980113f67f5bc73c7e93adcf8ad003423` and binding sources. Changing plan/base invalidates `PLAN_PASS`. After PASS, the Task coordinator presents the identity-bound package to the owner. Acceptance authorizes only Implementation of one Work Item and a local candidate/checks; it does not authorize GitHub mutation, push, PR, merge, install, pilot, publication, or release.

**Structural checks do not prove behavioral correctness.**
