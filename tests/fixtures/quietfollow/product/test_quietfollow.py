import tempfile
import unittest
from pathlib import Path

from quietfollow import Tracker


class TrackerTests(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.store_path = Path(self.temporary_directory.name) / "quietfollow.json"

    def test_scheduled_follow_up_survives_reconstruction(self):
        tracker = Tracker(str(self.store_path))
        contact_id = tracker.create_contact("Synthetic Client")
        follow_up_id = tracker.schedule_follow_up(contact_id, "2026-09-10")

        reconstructed = Tracker(str(self.store_path))

        self.assertEqual(reconstructed.due("2026-09-10")[0]["id"], follow_up_id)

    def test_unknown_contact_is_rejected_without_mutating_store(self):
        tracker = Tracker(str(self.store_path))
        before = self.store_path.read_bytes()

        with self.assertRaisesRegex(ValueError, "missing"):
            tracker.schedule_follow_up("missing", "2026-09-10")

        self.assertEqual(self.store_path.read_bytes(), before)
        self.assertEqual(Tracker(str(self.store_path)).due("2026-09-10"), [])

    def test_corrupt_store_is_rejected_without_rewriting_it(self):
        corrupt_bytes = b"{not-json"
        self.store_path.write_bytes(corrupt_bytes)

        with self.assertRaises(ValueError):
            Tracker(str(self.store_path))

        self.assertEqual(self.store_path.read_bytes(), corrupt_bytes)

    def test_new_valid_store_has_no_due_follow_ups(self):
        tracker = Tracker(str(self.store_path))

        self.assertEqual(tracker.due("2026-09-10"), [])

    def test_contacts_and_follow_ups_receive_distinct_ids(self):
        tracker = Tracker(str(self.store_path))
        first_contact = tracker.create_contact("First Client")
        second_contact = tracker.create_contact("Second Client")
        first_follow_up = tracker.schedule_follow_up(first_contact, "2026-09-10")
        second_follow_up = tracker.schedule_follow_up(second_contact, "2026-09-10")

        self.assertNotEqual(first_contact, second_contact)
        self.assertNotEqual(first_follow_up, second_follow_up)

    def test_confirmed_contact_survives_reconstruction_before_scheduling(self):
        tracker = Tracker(str(self.store_path))
        contact_id = tracker.create_contact("Synthetic Client")

        reconstructed = Tracker(str(self.store_path))
        follow_up_id = reconstructed.schedule_follow_up(contact_id, "2026-09-10")

        self.assertEqual(
            Tracker(str(self.store_path)).due("2026-09-10")[0]["id"],
            follow_up_id,
        )

    def test_due_date_is_inclusive_and_returns_minimum_string_fields(self):
        tracker = Tracker(str(self.store_path))
        contact_id = tracker.create_contact("Synthetic Client")
        follow_up_id = tracker.schedule_follow_up(contact_id, "2026-09-10")

        self.assertEqual(tracker.due("2026-09-09"), [])
        self.assertEqual(
            tracker.due("2026-09-10"),
            [
                {
                    "id": follow_up_id,
                    "contact_id": contact_id,
                    "contact_name": "Synthetic Client",
                    "due_on": "2026-09-10",
                    "outcome": "",
                }
            ],
        )
        self.assertTrue(
            all(
                isinstance(value, str)
                for value in tracker.due("2026-09-10")[0].values()
            )
        )

    def test_completed_outcome_survives_reconstruction(self):
        tracker = Tracker(str(self.store_path))
        contact_id = tracker.create_contact("Synthetic Client")
        follow_up_id = tracker.schedule_follow_up(contact_id, "2026-09-10")

        tracker.record_outcome(follow_up_id, "completed")

        reconstructed = Tracker(str(self.store_path))
        self.assertEqual(
            reconstructed.due("2026-09-10", include_completed=True)[0]["outcome"],
            "completed",
        )

    def test_completed_follow_up_is_hidden_by_default(self):
        tracker = Tracker(str(self.store_path))
        contact_id = tracker.create_contact("Synthetic Client")
        follow_up_id = tracker.schedule_follow_up(contact_id, "2026-09-10")

        tracker.record_outcome(follow_up_id, "completed")

        self.assertEqual(tracker.due("2026-09-10"), [])

    def test_inclusive_query_returns_completed_minimum_fields(self):
        tracker = Tracker(str(self.store_path))
        contact_id = tracker.create_contact("Synthetic Client")
        follow_up_id = tracker.schedule_follow_up(contact_id, "2026-09-10")
        tracker.record_outcome(follow_up_id, "completed")

        self.assertEqual(
            tracker.due("2026-09-10", include_completed=True),
            [
                {
                    "id": follow_up_id,
                    "contact_id": contact_id,
                    "contact_name": "Synthetic Client",
                    "due_on": "2026-09-10",
                    "outcome": "completed",
                }
            ],
        )

    def test_unknown_follow_up_outcome_is_rejected_without_mutating_store(self):
        tracker = Tracker(str(self.store_path))
        contact_id = tracker.create_contact("Synthetic Client")
        tracker.schedule_follow_up(contact_id, "2026-09-10")
        before_bytes = self.store_path.read_bytes()
        before_due = tracker.due("2026-09-10", include_completed=True)

        with self.assertRaisesRegex(ValueError, "missing"):
            tracker.record_outcome("missing", "Synthetic impossible outcome")

        self.assertEqual(self.store_path.read_bytes(), before_bytes)
        self.assertEqual(
            Tracker(str(self.store_path)).due(
                "2026-09-10", include_completed=True
            ),
            before_due,
        )

    def test_reconstructed_tracker_filters_persisted_completion_by_default(self):
        tracker = Tracker(str(self.store_path))
        contact_id = tracker.create_contact("Synthetic Client")
        follow_up_id = tracker.schedule_follow_up(contact_id, "2026-09-10")
        tracker.record_outcome(follow_up_id, "completed")

        reconstructed = Tracker(str(self.store_path))

        self.assertEqual(reconstructed.due("2026-09-10"), [])
        self.assertEqual(
            reconstructed.due("2026-09-10", include_completed=True),
            [
                {
                    "id": follow_up_id,
                    "contact_id": contact_id,
                    "contact_name": "Synthetic Client",
                    "due_on": "2026-09-10",
                    "outcome": "completed",
                }
            ],
        )

    def test_blank_outcome_is_rejected_without_mutating_state(self):
        tracker = Tracker(str(self.store_path))
        contact_id = tracker.create_contact("Synthetic Client")
        follow_up_id = tracker.schedule_follow_up(contact_id, "2026-09-10")
        before_bytes = self.store_path.read_bytes()
        before_due = tracker.due("2026-09-10", include_completed=True)

        with self.assertRaises(ValueError):
            tracker.record_outcome(follow_up_id, "   ")

        self.assertEqual(self.store_path.read_bytes(), before_bytes)
        self.assertEqual(
            tracker.due("2026-09-10", include_completed=True),
            before_due,
        )
        self.assertEqual(
            Tracker(str(self.store_path)).due(
                "2026-09-10", include_completed=True
            ),
            before_due,
        )

    def test_reconstructed_due_item_includes_contact_name(self):
        tracker = Tracker(str(self.store_path))
        contact_id = tracker.create_contact("Synthetic Contact Name")
        tracker.schedule_follow_up(contact_id, "2026-09-10")

        reconstructed = Tracker(str(self.store_path))

        self.assertEqual(
            reconstructed.due("2026-09-10")[0]["contact_name"],
            "Synthetic Contact Name",
        )

    def test_spaced_outcome_persists_exactly_across_two_reconstructions(self):
        tracker = Tracker(str(self.store_path))
        contact_id = tracker.create_contact("Synthetic Client")
        follow_up_id = tracker.schedule_follow_up(contact_id, "2026-09-10")
        tracker.record_outcome(follow_up_id, "  Synthetic callback  ")

        first_reconstruction = Tracker(str(self.store_path))
        second_reconstruction = Tracker(str(self.store_path))

        self.assertEqual(
            first_reconstruction.due(
                "2026-09-10", include_completed=True
            )[0]["outcome"],
            "  Synthetic callback  ",
        )
        self.assertEqual(
            second_reconstruction.due(
                "2026-09-10", include_completed=True
            )[0]["outcome"],
            "  Synthetic callback  ",
        )


if __name__ == "__main__":
    unittest.main()
