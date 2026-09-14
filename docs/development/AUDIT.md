# Baseline and Recipes Experience Audit

Source for references S1–S7: [SOURCES.md](SOURCES.md).
“Observed” means a specific case; “approved” means an owner decision/accepted workflow;
“proposal” means a new v0.1 construct that still needs validation.

## Strong foundation: preserve

S1 already covers the path from problem to feedback, applicability of commercial economics,
verifiable stage outcomes, separation of facts from hypotheses, failure/recovery/permissions,
the need to update existing artifacts, and continuation from the first incomplete stage.
These capabilities should not be replaced with a new process or reinvented.

S2 adds independent plan and implementation review, a module hierarchy, GitHub evidence,
native handoffs, and recovery. They should be integrated into S1 without duplication.

## Changes for v0.1

| ID | Finding and source | Decision for the harness | Basis |
|---|---|---|---|
| A01 | S1 agentic-development has one orchestrator and a generic builder/reviewer; S2 has the full Task/Work Item/PLAN/FINAL hierarchy | Extend the existing agentic-development; separate the lifecycle gate, product module, and Work Item | Approved S2/S3 |
| A02 | S2 permits escalation to the owner but does not define where to ask; in practice, approval was requested in the wrong place | The owner makes local decisions in the Task coordinator; project changes escalate to Product, without repeated approval or full-transcript relay | Historical S3 correction clarified by the owner on 2026-09-07; SPEC §§6–8 |
| A03 | The S1 task protocol requires a technical plan for every item; S2 excludes new deep design for ordinary code | Provide a short what/why description; technical decisions within the approved architecture belong to the implementer/reviewer. Material architecture changes require a separate decision | Approved S3; conflict with specialist skills must be resolved explicitly |
| A04 | S1 proposes independent review “where practical”; S2 requires a separate Change Review and whole-Task PLAN/FINAL | Keep it mandatory for delivery Work Items and module closure; do not create persistent specialist chats for every early gate | Approved; full FINAL not yet validated |
| A05 | Plan v1 was going to recreate scaling work that was already merged | Before decomposition, reconcile code, requirements, Issue/PR, and the existing manifest; preserve completed work | Observed S4 |
| A06 | v1 omitted permissions and distorted scaling semantics | Independent plan review must read binding sources; an implementer summary does not replace them | Observed S4 |
| A07 | A reviewed commit can change after PASS | Include the full SHA in the recommendation; a new head invalidates the review, and a main change invalidates FINAL | Approved S2; validate E12/E13 |
| A08 | Persistent manual forwarding of completion by the user | Native result → coordinator → next role; include identifiers/plan version/next action in the handoff | Observed S3 |
| A09 | Incompatible GitHub UI/API methods and gh outside PATH | Use one gh service client; the project defines host/repo; use git for transport; discover the local executable path | Observed S2/S3 |
| A10 | Forwarded approval was rejected by auto-review, while direct informed approval succeeded | Separate product mandate, GitHub access, and platform decision; do not guarantee transitive permission | Observed S3; bypasses excluded |
| A11 | A new chat does not yet know its own ID | The initial prompt knows parent/report_to; pass the real self ID after creation; a queued ID is not a usable ID | Corrected in S2, separate regression fixture |
| A12 | Old prompts and heartbeat continue to prescribe the previous process | When changing versions, update active instructions and monitoring in place, obtain ACK, and preserve WIP | Observed S3 |
| A13 | The PROJECT_STATUS baseline lags the actual acceptance of scaling | Status is a pointer; fresh evidence determines the next step. Plan updates within normal reviewed work; do not create endless status-only PRs | Observed S2/S4 |
| A14 | S1 SKILL.md Gate 8 = finance; lifecycle Gate 4.5 refers to a “detailed Gate 10 financial model,” although Gate 10 = security | Correct the reference; use one canonical stage map and validate links/consistency | Direct reading of S1 |
| A15 | SKILL.md requires the Impeccable sequence, while lifecycle permits it “as appropriate”; positioning is more mandatory at the entrypoint than for internal tools in the reference | Clarify one applicability/depth contract; record non-applicability instead of turning it into a fake PASS | Direct reading of S1; proposal |
| A16 | grill-me, product-financial-model, threat-model, attack-path-analysis, and security-diff-scan are absent from this session’s available catalog; mandatory use and a generic fallback coexist | Add a capability/dependency/permitted substitution/blocking matrix. Check availability only for capabilities required by the current stage | Direct comparison of S1 with the catalog; not a claim about the whole disk |
| A17 | RUB 1 million/Month 24 and a minimum 24-month horizon are hard-coded in S1 | Preserve the meaning of the economic gate; retain existing values only as visible, configurable defaults of the original profile for an applicable Gate 8 model. Do not require them in light Gate 3.5; choose goals and depth for the product and investment | Proposal, not a new universal commercial target; early-estimate limitation from S7 |
| A18 | Recipes host/repo, Go/Node commands, IDs, and absolute gh path cannot carry into a new product | Separate general instructions, product configuration, and local runtime details | Proposal based on S2 |
| A19 | Assigning model/reasoning in a prompt does not prove a runtime override | Pass native fields; record requested/accepted values without inventing independent model attestation | Approved S2, confirmed by the limitation in S3 ACK |
| A20 | The global skill is mutable, and the project merely points to the installed copy | Pin release + commit/content identity and check drift before transition; do not silently update existing projects | Proposal |
| A21 | docs-check validates form/links but not correspondence to product behavior | Use its mechanics as a foundation; keep semantic/behavior evaluation separate from lint | Direct reading of S2 |
| A22 | Accidental workarounds can become permanently “mandatory” actions | For each new rule, preserve the problem and usefulness criterion; do not universalize temporary Recipes constraints | Proposal from experience |
| A23 | The owner identified early implementation as too heavy and clarified: design for future architecture in advance, implement in stages, and reassess as the product grows | Five stages; architecture vision/current state/evolution plan; stage-specific evidence and transition reassessment within PLAN review | Direct owner decision on 2026-09-06, S6; evaluation not yet executed |
| A24 | The owner requested a light market/competition/economics assessment between Positioning and Journey; S1 already contains a heavier early Gate 4.5 | Replace 4.5 with 3.5; use Positioning results, pass constraints into Journey/Scope/PRD, and refine economics at Gate 8. Recognize suitable old evidence without repeating research | Direct owner request on 2026-09-06, S7; boundaries clarified by author reconciliation, evaluation not yet executed |

## What belongs in the product profile

Git host/repository, stack and commands, commercial mode and economic targets, supported devices,
requirements sources, owner, release target, current models, and available tools. The Recipes matrix
is preserved as an initially agreed profile, not as a promise that models remain available forever.
The specific branch-protection state does not carry over; it is checked in the target repository.

A separate navigation-only Work Item is preserved as a Recipes decision.
For a new product, it is not a mandatory separate PR: navigation can be included in the planned
documentation scope of an existing Work Item if that does not change its boundaries and passes review.
Independent validation of this simplification’s applicability is included in E18.

## What not to carry over

- Recipes, ingredient scaling, specific actors/APIs/schemas, or the technical stack.
- Historical references to “current” main as a long-term fact.
- Unmotivated wait automation and repeated notifications about normal in_progress state.
- Additional technical approval for every simple step.
- A requirement to copy the entire lifecycle into every product repository.
- An assumption that Recipes private-repository constraints apply to every GitHub plan.
- Runtime IDs, auth credentials, original conversations, or personal-machine settings.

## Not proven by the Recipes experience

A complete new-product run with this harness; suitability of all financial defaults for different
products; a completed whole-Task FINAL under the new process; unattended work while the desktop is
closed; migration to a clean installation; production release; and actual recovery after a failure.
These remain pilot scenarios, not marketing claims of readiness.
