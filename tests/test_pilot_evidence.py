import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "tests/fixtures/quietfollow/evidence"
EXECUTION = EVIDENCE / "execution-record.json"
PUBLIC_EVIDENCE = tuple(EVIDENCE.glob("**/*")) + (ROOT / "docs/validation.md",)
SELECTED_CASES = {
    "E02", "E08", "E10", "E11", "E12", "E13", "E14", "E17",
    "E20", "E21", "E22", "E25", "E27", "E28", "E31", "E33",
    "E34", "E37", "E38", "E39", "E41",
}


class PilotEvidenceContractTest(unittest.TestCase):
    def test_execution_record_covers_exact_selected_cases(self):
        record = json.loads(EXECUTION.read_text(encoding="utf-8"))
        self.assertEqual(SELECTED_CASES, {case["id"] for case in record["cases"]})
        self.assertEqual(len(SELECTED_CASES), len(record["cases"]))
        for case in record["cases"]:
            self.assertIn(case["evaluation_verdict"], {"PASS", "FAIL", "BLOCKED"})
            self.assertIn("dependent_action_state", case)

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
