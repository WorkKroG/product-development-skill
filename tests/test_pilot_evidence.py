import json
import hashlib
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "tests/fixtures/quietfollow/evidence"
EXECUTION = EVIDENCE / "execution-record.json"
PUBLIC_EVIDENCE = (
    tuple(EVIDENCE.glob("**/*"))
    + tuple((ROOT / "tests/fixtures/quietfollow/product").glob("*.py"))
    + (
        ROOT / "docs/validation.md",
        ROOT / "docs/PROJECT_STATUS.md",
    )
)
SELECTED_CASES = {
    "E02", "E08", "E10", "E11", "E12", "E13", "E14", "E17",
    "E20", "E21", "E22", "E25", "E27", "E28", "E31", "E33",
    "E34", "E37", "E38", "E39", "E41",
}
REQUIRED_CASE_FIELDS = {
    "id", "input_identities", "mode", "allowed_side_effects",
    "forbidden_side_effects", "executor_alias", "evaluator_alias",
    "requested_assignment", "accepted_assignment",
    "independently_verified_runtime_fact", "output_evidence",
    "transcript_evidence", "actual_outcome", "evaluation_verdict",
    "dependent_action_state", "findings", "rerun_identity",
}
EXPECTED_METRICS = {
    "manual_owner_relay_events", "duplicate_owner_approval_prompts",
    "duplicate_user_owned_task_creations", "duplicate_internal_work_launches",
    "invalid_pass_uses", "incorrect_transitions",
}
IMMUTABLE_INPUTS = {
    "fixture-agents": "tests/fixtures/quietfollow/AGENTS.md",
    "fixture-project-status": "tests/fixtures/quietfollow/PROJECT_STATUS.md",
    "fixture-product-profile": "tests/fixtures/quietfollow/product-profile.md",
    "fixture-positioning": "tests/fixtures/quietfollow/positioning.md",
    "legacy-status": "tests/fixtures/resume-legacy-4-5/PROJECT_STATUS.md",
    "legacy-viability": "tests/fixtures/resume-legacy-4-5/legacy-viability.md",
    "review-events": "tests/fixtures/review-state/events.json",
    "module5-reviewer-rubric": "tests/scenarios.md",
    "active-skill-entrypoint": "skills/product-development-workflow/SKILL.md",
    "workflow-checker": "scripts/check_workflow.py",
}


class PilotEvidenceContractTest(unittest.TestCase):
    def test_execution_record_covers_exact_selected_cases(self):
        record = json.loads(EXECUTION.read_text(encoding="utf-8"))
        self.assertEqual(SELECTED_CASES, {case["id"] for case in record["cases"]})
        self.assertEqual(len(SELECTED_CASES), len(record["cases"]))
        for case in record["cases"]:
            self.assertEqual(REQUIRED_CASE_FIELDS, set(case))
            self.assertIn(case["evaluation_verdict"], {"PASS", "FAIL", "BLOCKED"})
            self.assertNotEqual(case["evaluation_verdict"], case["dependent_action_state"])
            self.assertNotIn(case["actual_outcome"], {"TBD", "TODO", "PLACEHOLDER"})
            for identity in case["input_identities"]:
                self.assertRegex(identity, r"^.+@sha256:[0-9a-f]{64}$")
            for digest in case["output_evidence"]:
                self.assertRegex(digest, r"^sha256:[0-9a-f]{64}$")
            self.assertRegex(
                case["transcript_evidence"]["digest"],
                r"^sha256:[0-9a-f]{64}$",
            )

    def test_manifest_has_five_unique_parts_and_immutable_inputs(self):
        manifest = json.loads((EVIDENCE / "manifest.json").read_text(encoding="utf-8"))
        parts = manifest["parts"]
        self.assertEqual(5, len(parts))
        self.assertEqual(5, len({part["id"] for part in parts}))
        self.assertEqual(5, len({part["path"] for part in parts}))
        for part in parts:
            path = ROOT / part["path"]
            self.assertTrue(path.is_file())
            self.assertEqual(part["sha256"], hashlib.sha256(path.read_bytes()).hexdigest())
        snapshots = {item["alias"]: item["sha256"] for item in manifest["snapshots"]}
        for item in manifest["snapshots"]:
            self.assertRegex(item["sha256"], r"^[0-9a-f]{64}$")
        for alias, relative_path in IMMUTABLE_INPUTS.items():
            digest = hashlib.sha256((ROOT / relative_path).read_bytes()).hexdigest()
            self.assertEqual(digest, snapshots[alias])

    def test_metrics_have_exact_units_boundaries_denominators_and_exclusions(self):
        record = json.loads(EXECUTION.read_text(encoding="utf-8"))
        metrics = {metric["name"]: metric for metric in record["metrics"]}
        self.assertEqual(EXPECTED_METRICS, set(metrics))
        for metric in metrics.values():
            self.assertEqual("event", metric["unit"])
            self.assertIn("value", metric)
            self.assertNotIn(metric["value"], {"TBD", "TODO", "PLACEHOLDER"})
            self.assertTrue(metric["observation_start_evidence"])
            self.assertTrue(metric["observation_end_evidence"])
            self.assertTrue(metric["denominator"])
            self.assertIsInstance(metric["exclusions"], list)

    def test_contract_is_mechanical_not_semantic_pass(self):
        record = json.loads(EXECUTION.read_text(encoding="utf-8"))
        self.assertEqual(
            "Schema and shape checks do not establish semantic behavioral correctness.",
            record["mechanical_test_limitation"],
        )

    def test_declared_product_copy_hashes_match_public_bytes(self):
        manifest = json.loads((EVIDENCE / "manifest.json").read_text(encoding="utf-8"))
        for copy in manifest["repository"]["source_copy_hashes"]:
            digest = hashlib.sha256((ROOT / copy["path"]).read_bytes()).hexdigest()
            self.assertEqual(copy["source_sha256"], copy["copy_sha256"])
            self.assertEqual(copy["copy_sha256"], digest)

    def test_disposable_product_tree_and_e13_use_corrected_current_identity(self):
        manifest = json.loads((EVIDENCE / "manifest.json").read_text(encoding="utf-8"))
        tree = manifest["repository"]["disposable_product_tree"]
        self.assertRegex(tree, r"^[0-9a-f]{40}$")
        self.assertEqual("a5fce7b8a8c7eafae9349a762c28d4ea50709da9", tree)

        record = json.loads(EXECUTION.read_text(encoding="utf-8"))
        case = next(case for case in record["cases"] if case["id"] == "E13")
        self.assertEqual(
            {
                "final-mismatch-v2@sha256:455942df13e29b42ff5cb508854c8cbb261ae037c4c5324633b959f4c9b89752",
                "e13-evaluator-input-v2@sha256:5680630fb33e2a3dbd90e1877bb20a33fd0e4a0fdcd2500e6ea7c7bb3e1edf2c",
            },
            set(case["input_identities"]),
        )
        self.assertEqual(
            [
                "sha256:80f7259ca208dc381d2d649634cd22cc9d4cfbf48fc2b349dcbd298a3c0ae34a",
                "sha256:e957ea4857f395aa784885412d4d486b09f9ce7e875e0dd4ac2a96d79697de4f",
            ],
            case["output_evidence"],
        )
        self.assertEqual("BLOCKED_PENDING_FRESH_FINAL", case["dependent_action_state"])
        self.assertEqual("case-E13-evaluator-2-corrected-tree", case["rerun_identity"])
        self.assertTrue(
            any("superseded non-credit" in finding for finding in case["findings"])
        )

    def test_navigation_tracks_committed_candidate_and_one_next_action(self):
        manifest = json.loads((EVIDENCE / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(
            "local committed candidate; exact head and review state are owned by Task 9 "
            "task-local evidence and final review record; integration and FINAL are unperformed",
            manifest["repository"]["candidate_identity"],
        )

        project_status = (ROOT / "docs/PROJECT_STATUS.md").read_text(encoding="utf-8")
        validation = (ROOT / "docs/validation.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        readme_flat = " ".join(readme.split())
        for text in (project_status, validation):
            self.assertNotIn("uncommitted candidate", text)
            self.assertNotIn("pending Task 9 commit", text)
            self.assertIn("local committed candidate", text)
            self.assertIn("integration", text.lower())
            self.assertIn("FINAL", text)
        self.assertEqual(1, project_status.count("\n## Next action\n"))
        next_action = " ".join(
            project_status.split("\n## Next action\n", 1)[1].split()
        )
        self.assertIn(
            "Owner/Product decides whether to authorize Task 10 integration for the exact "
            "locally reviewed candidate identified by Task 9's final review record.",
            next_action,
        )
        self.assertNotIn("текущий кандидат Module 4", readme_flat)
        self.assertNotIn(
            "E01–E41 и синтетический pilot QuietFollow ещё не выполнены",
            readme_flat,
        )
        self.assertIn("Module 6 — текущий локальный committed candidate", readme_flat)
        self.assertIn("21 выбранного E-case", readme_flat)
        self.assertIn("не интегрирован и не выпущен", readme_flat)
        self.assertIn(
            "не доказывает полное покрытие E01–E41, live-routing или production behavior",
            readme_flat,
        )

    def test_public_evidence_contains_no_private_runtime_bindings(self):
        text = "\n".join(
            path.read_text(encoding="utf-8")
            for path in PUBLIC_EVIDENCE
            if path.is_file()
        )
        self.assertNotRegex(text, r"/Users/|/private/|\.local-handoff")
        self.assertNotRegex(text, r"/tmp/|/var/|[A-Za-z]:\\|\\\\")
        self.assertNotRegex(text, r"01[a-z0-9]{6,}-[a-z0-9-]{20,}")

    def test_role_records_use_only_public_aliases(self):
        manifest = json.loads((EVIDENCE / "manifest.json").read_text(encoding="utf-8"))
        allowed = set(manifest["permissions"]["public_alias_vocabulary"])
        for role in manifest["roles"]:
            self.assertIn(role["alias"], allowed)
            self.assertRegex(role["private_evidence_digest"], r"^sha256:[0-9a-f]{64}$")
            self.assertTrue({"native_id", "task_id", "agent_id"}.isdisjoint(role))
        record = json.loads(EXECUTION.read_text(encoding="utf-8"))
        for case in record["cases"]:
            self.assertIn(case["executor_alias"], allowed)
            self.assertIn(case["evaluator_alias"], allowed)
        self.assertNotRegex(
            json.dumps({"manifest": manifest, "record": record}),
            r'"(?:native_id|task_id|agent_id)"\s*:',
        )
