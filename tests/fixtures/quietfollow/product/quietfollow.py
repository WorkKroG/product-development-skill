import json
import uuid
from pathlib import Path


class Tracker:
    def __init__(self, path: str):
        self._path = Path(path)
        if self._path.exists():
            self._data = self._read_store()
        else:
            initial = {"contacts": {}, "follow_ups": []}
            self._write_store(initial)
            self._data = initial

    def create_contact(self, name: str) -> str:
        contact_id = uuid.uuid4().hex
        updated = self._copy_store()
        updated["contacts"][contact_id] = name
        self._write_store(updated)
        self._data = updated
        return contact_id

    def schedule_follow_up(self, contact_id: str, due_on: str) -> str:
        if contact_id not in self._data["contacts"]:
            raise ValueError(f"unknown contact: {contact_id}")

        follow_up_id = uuid.uuid4().hex
        updated = self._copy_store()
        updated["follow_ups"].append(
            {
                "id": follow_up_id,
                "contact_id": contact_id,
                "due_on": due_on,
                "outcome": "",
            }
        )
        self._write_store(updated)
        self._data = updated
        return follow_up_id

    def record_outcome(self, follow_up_id: str, outcome: str) -> None:
        if not outcome.strip():
            raise ValueError("outcome must not be blank")

        updated = self._copy_store()
        for follow_up in updated["follow_ups"]:
            if follow_up["id"] == follow_up_id:
                follow_up["outcome"] = outcome
                self._write_store(updated)
                self._data = updated
                return

        raise ValueError(f"unknown follow-up: {follow_up_id}")

    def due(self, as_of: str, include_completed: bool = False) -> list[dict[str, str]]:
        return [
            dict(
                follow_up,
                contact_name=self._data["contacts"][follow_up["contact_id"]],
            )
            for follow_up in self._data["follow_ups"]
            if follow_up["due_on"] <= as_of
            and (include_completed or not follow_up["outcome"])
        ]

    def _read_store(self) -> dict:
        try:
            data = json.loads(self._path.read_text(encoding="utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise ValueError("invalid QuietFollow store") from error

        if not self._is_valid_store(data):
            raise ValueError("invalid QuietFollow store")
        return data

    def _write_store(self, data: dict) -> None:
        self._path.write_text(
            json.dumps(data, ensure_ascii=False, sort_keys=True),
            encoding="utf-8",
        )

    def _copy_store(self) -> dict:
        return {
            "contacts": dict(self._data["contacts"]),
            "follow_ups": [dict(item) for item in self._data["follow_ups"]],
        }

    @staticmethod
    def _is_valid_store(data: object) -> bool:
        if not isinstance(data, dict) or set(data) != {"contacts", "follow_ups"}:
            return False
        contacts = data["contacts"]
        follow_ups = data["follow_ups"]
        if not isinstance(contacts, dict) or not all(
            isinstance(contact_id, str) and isinstance(name, str)
            for contact_id, name in contacts.items()
        ):
            return False
        if not isinstance(follow_ups, list):
            return False
        expected_fields = {"id", "contact_id", "due_on", "outcome"}
        return all(
            isinstance(follow_up, dict)
            and set(follow_up) == expected_fields
            and all(isinstance(follow_up[field], str) for field in expected_fields)
            and follow_up["contact_id"] in contacts
            for follow_up in follow_ups
        )
