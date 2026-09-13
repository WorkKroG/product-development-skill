import hashlib
import json
import stat
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "tests/fixtures/quietfollow/evidence"
RUN = EVIDENCE / "runs/2026-09-13-lean-pilot"
INDEX = RUN / "index.json"
EXECUTION = EVIDENCE / "execution-record.json"
MANIFEST = EVIDENCE / "manifest.json"

REQUIRED_CASES = [
    "E02", "E08", "E10", "E11", "E12", "E13", "E14", "E17",
    "E20", "E21", "E22", "E25", "E27", "E28", "E31", "E33",
    "E34", "E37", "E38", "E39", "E41",
]
REQUIRED_PROBES = ["SU01", "SU02", "SU03", "SU04", "SU05", "SU06"]
PARTS = [
    "part-1-discovery.md",
    "part-2-readiness.md",
    "part-3-delivery.md",
    "part-4-release-rehearsal.md",
    "part-5-resume-scaling.md",
]


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def recorded_artifacts(value):
    """Yield tracked raw case/probe artifact records from nested index values."""
    if isinstance(value, dict):
        path = value.get("path")
        if isinstance(path, str) and (
            "/cases/" in path or "/probes/" in path
        ) and ("sha256" in value or "whole_sha256" in value):
            yield value
        for nested in value.values():
            yield from recorded_artifacts(nested)
    elif isinstance(value, list):
        for nested in value:
            yield from recorded_artifacts(nested)


class LeanPilotEvidenceContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = json.loads(INDEX.read_text(encoding="utf-8"))
        cls.execution = json.loads(EXECUTION.read_text(encoding="utf-8"))
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    def test_exact_plan_and_candidate_identity(self):
        self.assertEqual("2026-09-13-lean-pilot", self.index["run_id"])
        self.assertEqual("MODULE6-LEAN-PLAN-v1", self.index["plan"]["identity"])
        self.assertEqual(
            "feebad5d67614da5d25439c0ae38c2164becdbf2",
            self.index["plan"]["commit"],
        )
        self.assertEqual("PLAN_PASS", self.index["plan"]["review"]["verdict"])
        self.assertEqual("MODULE6-LEAN-SKILL-v1", self.index["current_skill"]["identity"])
        self.assertEqual("PASS", self.index["current_skill"]["review_verdict"])

    def test_exact_ordered_requirements_and_current_pass_matrix(self):
        self.assertEqual(REQUIRED_CASES, self.index["required_case_ids"])
        self.assertEqual(REQUIRED_PROBES, self.index["required_probe_ids"])
        current = [item for item in self.index["current_attempts"] if item["current"]]
        self.assertEqual(27, len(current))
        self.assertEqual(27, len({(item["kind"], item["id"]) for item in current}))
        self.assertEqual(set(REQUIRED_CASES), {x["id"] for x in current if x["kind"] == "case"})
        self.assertEqual(set(REQUIRED_PROBES), {x["id"] for x in current if x["kind"] == "probe"})
        self.assertTrue(all(x["credit"] == "PASS" for x in current))
        self.assertTrue(all(x["verdict"] == "PASS" for x in current))

    def test_every_recorded_raw_artifact_matches_bytes_hash_and_mode(self):
        records = list(recorded_artifacts(self.index["current_attempts"]))
        by_path = {}
        for record in records:
            relative = record["path"]
            self.assertNotIn(relative, by_path)
            by_path[relative] = record
            path = ROOT / relative
            self.assertTrue(path.is_file(), relative)
            self.assertFalse(path.is_symlink(), relative)
            expected_hash = record.get("sha256", record.get("whole_sha256"))
            self.assertEqual(expected_hash, sha256(path), relative)
            if "bytes" in record or "whole_bytes" in record:
                self.assertEqual(record.get("bytes", record.get("whole_bytes")), path.stat().st_size)
            if "mode" in record:
                actual_mode = format(stat.S_IMODE(path.stat().st_mode), "04o")
                self.assertEqual(record["mode"], actual_mode, relative)

        actual = {
            path.relative_to(ROOT).as_posix()
            for root_name in ("cases", "probes")
            for path in (RUN / root_name).rglob("*")
            if path.is_file()
        }
        self.assertEqual(actual, set(by_path))
        self.assertEqual(111, len(actual))

    def test_evaluator_prefix_boundaries_match(self):
        for item in self.index["current_attempts"]:
            evaluation = item.get("evaluation")
            if not evaluation:
                continue
            raw = (ROOT / evaluation["path"]).read_bytes()
            prefix = raw[: evaluation["prefix_bytes"]]
            self.assertEqual(evaluation["prefix_sha256"], hashlib.sha256(prefix).hexdigest())

    def test_compact_execution_record_matches_current_index(self):
        self.assertEqual(2, self.execution["schema_version"])
        self.assertEqual(REQUIRED_CASES, self.execution["required_case_ids"])
        self.assertEqual(REQUIRED_PROBES, self.execution["required_probe_ids"])
        rows = self.execution["current_evaluations"]
        self.assertEqual(27, len(rows))
        current = {
            (item["kind"], item["id"]): item
            for item in self.index["current_attempts"] if item["current"]
        }
        self.assertEqual(set(current), {(row["kind"], row["id"]) for row in rows})
        for row in rows:
            source = current[(row["kind"], row["id"])]
            self.assertEqual(source["attempt"], row["attempt"])
            self.assertEqual(source["verdict"], row["verdict"])
            self.assertEqual(source["dependent_state"], row["dependent_state"])
            self.assertEqual(source["evaluation"]["whole_sha256"], row["evaluation"]["sha256"])
        self.assertEqual(27, self.execution["summary"]["current_pass"])
        self.assertFalse(self.execution["summary"]["post_pilot_candidate_change"])

    def test_manifest_binds_parts_index_bundle_product_and_skill(self):
        self.assertEqual(2, self.manifest["schema_version"])
        self.assertEqual("MODULE6-LEAN-PLAN-v1", self.manifest["module"])
        self.assertEqual(5, len(self.manifest["parts"]))
        self.assertEqual(PARTS, [Path(x["path"]).name for x in self.manifest["parts"]])
        for entry in self.manifest["parts"]:
            self.assertEqual(entry["sha256"], sha256(ROOT / entry["path"]))
        for key in ("index", "execution_record", "bundle", "product_source", "product_tests", "skill_checksums"):
            entry = self.manifest["bindings"][key]
            self.assertEqual(entry["sha256"], sha256(ROOT / entry["path"]), key)
        self.assertEqual(
            "273a9b38a069f665c73dcfcfc8b5b3c324bd28bc2e52cf4e023e6984ce528f3f",
            self.manifest["bindings"]["bundle"]["sha256"],
        )

    def test_product_bytes_are_canonical_and_suite_has_seven_outcome_tests(self):
        self.assertEqual(
            "ff37f7ab71804c9207995e5451919ecd134a38d5569547f619c22093f9df8347",
            sha256(ROOT / "tests/fixtures/quietfollow/product/quietfollow.py"),
        )
        self.assertEqual(
            "71e63584dcaa2c333b363f8071b376b58d4c954be5b9ba7f0b8331c444d182e9",
            sha256(ROOT / "tests/fixtures/quietfollow/product/test_quietfollow.py"),
        )
        product_tests = (ROOT / "tests/fixtures/quietfollow/product/test_quietfollow.py").read_text()
        self.assertEqual(7, product_tests.count("def test_") - 8)

    def test_navigation_preserves_authority_and_one_next_action(self):
        status = (ROOT / "docs/PROJECT_STATUS.md").read_text(encoding="utf-8")
        validation = (ROOT / "docs/validation.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertEqual(1, status.count("\n## Next action\n"))
        for text in (status, validation, readme):
            flat = " ".join(text.split())
            self.assertIn("21", flat)
            self.assertIn("6", flat)
            self.assertIn("не интегрирован", flat)
        self.assertIn("Task 9", status)
        self.assertIn("Task 10", status)
        self.assertIn("not authorized", status)

    def test_public_evidence_has_no_private_runtime_binding(self):
        paths = [
            *EVIDENCE.glob("*.json"),
            *EVIDENCE.glob("*.md"),
            *RUN.rglob("*"),
            ROOT / "docs/PROJECT_STATUS.md",
            ROOT / "docs/validation.md",
            ROOT / "README.md",
        ]
        text = "\n".join(
            path.read_text(encoding="utf-8", errors="ignore")
            for path in paths if path.is_file() and path.suffix != ".bundle"
        )
        self.assertNotRegex(text, r"/Users/|/private/|/tmp/|[A-Za-z]:\\")

    def test_contract_is_mechanical_not_semantic_pass(self):
        self.assertEqual(
            "Schema, hashes, and shape checks do not establish semantic behavioral correctness.",
            self.execution["mechanical_test_limitation"],
        )


if __name__ == "__main__":
    unittest.main()
