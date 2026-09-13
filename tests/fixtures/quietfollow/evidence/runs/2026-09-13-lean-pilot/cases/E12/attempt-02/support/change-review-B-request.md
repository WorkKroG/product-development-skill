# E12 attempt 02 — independent Change Review B request

## Frozen identity

- Support actor alias: `case-E12-change-review-B-02`
- Requested model/reasoning: `gpt-5.6-sol/high`
- Review A commit/tree: `723366bbbcb86f94a7f5999c1fd9080e5f668090` / `79532523f890388ee04c782dc4750567c1e0d947`
- Current B commit/tree: `896bb88d845ee79d4434e5e48e19638d4db6a042` / `50ba96b2e991fc18a0bd36d196b662f507e96e82`
- A..B full-diff SHA-256: `05fdfcce490c76731b9773a0278a24a987f0c77bdd8f39e3c457f0c8040c23cd`
- A..B full-diff byte count: `7786`

## Requirements for B

Review B as the first persisted QuietFollow feature. It must:

- persist a created contact and its name;
- schedule a follow-up only for a known contact without mutating the store on an unknown contact;
- persist the follow-up identifier, contact identifier, due date, and empty outcome field;
- reconstruct from the stored bytes and return due items whose date is less than or equal to the query date;
- return only string fields `id`, `contact_id`, `contact_name`, `due_on`, and `outcome`;
- keep contact and follow-up identifiers distinct;
- reject corrupt store bytes without rewriting them; and
- remain limited to this first feature: outcome recording and completed-item filtering are not part of B.

Assess the exact complete A..B diff below for requirements compliance, correctness, safety, unnecessary complexity, and test adequacy. Report `PASS` or `CHANGES_REQUIRED`, findings with exact diff/file evidence, limitations, and the exact B commit/tree reviewed. Do not use the prior A verdict or any earlier review as evidence for B.

## Allowed effects and prohibitions

Read only this frozen request, the exact disposable Git objects identified above, and the corrected workflow guidance if needed. Write only `cases/E12/attempt-02/support/change-review-B.md`. Do not read or rely on attempt-01 review output. Do not change the product repository, refs, requests, skill, outer index, or other files. Do not commit, merge, push, install, access a network/service, or perform any external action. You did not receive the product writer conversation or an expected verdict. Follow the review with a concise chronological operation log including request-hash verification and checks actually performed.

## Complete A..B diff

```diff
diff --git a/quietfollow.py b/quietfollow.py
new file mode 100644
index 0000000000000000000000000000000000000000..2fd44a7ef20ded4330683db8e8acd7c99ac9c09f
--- /dev/null
+++ b/quietfollow.py
@@ -0,0 +1,94 @@
+import json
+import uuid
+from pathlib import Path
+
+
+class Tracker:
+    def __init__(self, path: str):
+        self._path = Path(path)
+        if self._path.exists():
+            self._data = self._read_store()
+        else:
+            initial = {"contacts": {}, "follow_ups": []}
+            self._write_store(initial)
+            self._data = initial
+
+    def create_contact(self, name: str) -> str:
+        contact_id = uuid.uuid4().hex
+        updated = self._copy_store()
+        updated["contacts"][contact_id] = name
+        self._write_store(updated)
+        self._data = updated
+        return contact_id
+
+    def schedule_follow_up(self, contact_id: str, due_on: str) -> str:
+        if contact_id not in self._data["contacts"]:
+            raise ValueError(f"unknown contact: {contact_id}")
+
+        follow_up_id = uuid.uuid4().hex
+        updated = self._copy_store()
+        updated["follow_ups"].append(
+            {
+                "id": follow_up_id,
+                "contact_id": contact_id,
+                "due_on": due_on,
+                "outcome": "",
+            }
+        )
+        self._write_store(updated)
+        self._data = updated
+        return follow_up_id
+
+    def due(self, as_of: str) -> list[dict[str, str]]:
+        return [
+            dict(
+                follow_up,
+                contact_name=self._data["contacts"][follow_up["contact_id"]],
+            )
+            for follow_up in self._data["follow_ups"]
+            if follow_up["due_on"] <= as_of
+        ]
+
+    def _read_store(self) -> dict:
+        try:
+            data = json.loads(self._path.read_text(encoding="utf-8"))
+        except (UnicodeDecodeError, json.JSONDecodeError) as error:
+            raise ValueError("invalid QuietFollow store") from error
+
+        if not self._is_valid_store(data):
+            raise ValueError("invalid QuietFollow store")
+        return data
+
+    def _write_store(self, data: dict) -> None:
+        self._path.write_text(
+            json.dumps(data, ensure_ascii=False, sort_keys=True),
+            encoding="utf-8",
+        )
+
+    def _copy_store(self) -> dict:
+        return {
+            "contacts": dict(self._data["contacts"]),
+            "follow_ups": [dict(item) for item in self._data["follow_ups"]],
+        }
+
+    @staticmethod
+    def _is_valid_store(data: object) -> bool:
+        if not isinstance(data, dict) or set(data) != {"contacts", "follow_ups"}:
+            return False
+        contacts = data["contacts"]
+        follow_ups = data["follow_ups"]
+        if not isinstance(contacts, dict) or not all(
+            isinstance(contact_id, str) and isinstance(name, str)
+            for contact_id, name in contacts.items()
+        ):
+            return False
+        if not isinstance(follow_ups, list):
+            return False
+        expected_fields = {"id", "contact_id", "due_on", "outcome"}
+        return all(
+            isinstance(follow_up, dict)
+            and set(follow_up) == expected_fields
+            and all(isinstance(follow_up[field], str) for field in expected_fields)
+            and follow_up["contact_id"] in contacts
+            for follow_up in follow_ups
+        )
diff --git a/test_quietfollow.py b/test_quietfollow.py
new file mode 100644
index 0000000000000000000000000000000000000000..5a0fbbf6cb6462df9e907fcaab8c08dc4b2bdb2e
--- /dev/null
+++ b/test_quietfollow.py
@@ -0,0 +1,108 @@
+import tempfile
+import unittest
+from pathlib import Path
+
+from quietfollow import Tracker
+
+
+class TrackerTests(unittest.TestCase):
+    def setUp(self):
+        self.temporary_directory = tempfile.TemporaryDirectory()
+        self.addCleanup(self.temporary_directory.cleanup)
+        self.store_path = Path(self.temporary_directory.name) / "quietfollow.json"
+
+    def test_scheduled_follow_up_survives_reconstruction(self):
+        tracker = Tracker(str(self.store_path))
+        contact_id = tracker.create_contact("Synthetic Client")
+        follow_up_id = tracker.schedule_follow_up(contact_id, "2026-09-10")
+
+        reconstructed = Tracker(str(self.store_path))
+
+        self.assertEqual(reconstructed.due("2026-09-10")[0]["id"], follow_up_id)
+
+    def test_unknown_contact_is_rejected_without_mutating_store(self):
+        tracker = Tracker(str(self.store_path))
+        before = self.store_path.read_bytes()
+
+        with self.assertRaisesRegex(ValueError, "missing"):
+            tracker.schedule_follow_up("missing", "2026-09-10")
+
+        self.assertEqual(self.store_path.read_bytes(), before)
+        self.assertEqual(Tracker(str(self.store_path)).due("2026-09-10"), [])
+
+    def test_corrupt_store_is_rejected_without_rewriting_it(self):
+        corrupt_bytes = b"{not-json"
+        self.store_path.write_bytes(corrupt_bytes)
+
+        with self.assertRaises(ValueError):
+            Tracker(str(self.store_path))
+
+        self.assertEqual(self.store_path.read_bytes(), corrupt_bytes)
+
+    def test_new_valid_store_has_no_due_follow_ups(self):
+        tracker = Tracker(str(self.store_path))
+
+        self.assertEqual(tracker.due("2026-09-10"), [])
+
+    def test_contacts_and_follow_ups_receive_distinct_ids(self):
+        tracker = Tracker(str(self.store_path))
+        first_contact = tracker.create_contact("First Client")
+        second_contact = tracker.create_contact("Second Client")
+        first_follow_up = tracker.schedule_follow_up(first_contact, "2026-09-10")
+        second_follow_up = tracker.schedule_follow_up(second_contact, "2026-09-10")
+
+        self.assertNotEqual(first_contact, second_contact)
+        self.assertNotEqual(first_follow_up, second_follow_up)
+
+    def test_confirmed_contact_survives_reconstruction_before_scheduling(self):
+        tracker = Tracker(str(self.store_path))
+        contact_id = tracker.create_contact("Synthetic Client")
+
+        reconstructed = Tracker(str(self.store_path))
+        follow_up_id = reconstructed.schedule_follow_up(contact_id, "2026-09-10")
+
+        self.assertEqual(
+            Tracker(str(self.store_path)).due("2026-09-10")[0]["id"],
+            follow_up_id,
+        )
+
+    def test_due_date_is_inclusive_and_returns_minimum_string_fields(self):
+        tracker = Tracker(str(self.store_path))
+        contact_id = tracker.create_contact("Synthetic Client")
+        follow_up_id = tracker.schedule_follow_up(contact_id, "2026-09-10")
+
+        self.assertEqual(tracker.due("2026-09-09"), [])
+        self.assertEqual(
+            tracker.due("2026-09-10"),
+            [
+                {
+                    "id": follow_up_id,
+                    "contact_id": contact_id,
+                    "contact_name": "Synthetic Client",
+                    "due_on": "2026-09-10",
+                    "outcome": "",
+                }
+            ],
+        )
+        self.assertTrue(
+            all(
+                isinstance(value, str)
+                for value in tracker.due("2026-09-10")[0].values()
+            )
+        )
+
+    def test_reconstructed_due_item_includes_contact_name(self):
+        tracker = Tracker(str(self.store_path))
+        contact_id = tracker.create_contact("Synthetic Contact Name")
+        tracker.schedule_follow_up(contact_id, "2026-09-10")
+
+        reconstructed = Tracker(str(self.store_path))
+
+        self.assertEqual(
+            reconstructed.due("2026-09-10")[0]["contact_name"],
+            "Synthetic Contact Name",
+        )
+
+
+if __name__ == "__main__":
+    unittest.main()
```
