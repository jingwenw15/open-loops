from datetime import date
from pathlib import Path
import re
import unittest


ENTRY = re.compile(r"^### (OL-\d{3,})\s+[—-]\s+(.+)$")
FIELD = re.compile(r"^- \*\*([^*]+):\*\*\s*(.*)$")


def validate(text: str) -> list[str]:
    if not text.startswith("# Open Loops\n"):
        raise ValueError("invalid title")
    section = ""
    entries = []
    fields = {}

    def finish() -> None:
        if not entries:
            return
        entry_id, owner_section = entries[-1]
        required = {"Status", "Kind", "Raised", "Why it matters"}
        if required - fields.keys():
            raise ValueError(f"{entry_id} missing required fields")
        date.fromisoformat(fields["Raised"])
        if owner_section == "Active" and fields["Status"] not in {"open", "blocking", "deferred"}:
            raise ValueError("closed status under Active")
        if owner_section == "Closed":
            if fields["Status"] not in {"resolved", "obsolete"}:
                raise ValueError("active status under Closed")
            if not fields.get("Resolved") or not fields.get("Resolution"):
                raise ValueError("closed entry missing resolution")
            date.fromisoformat(fields["Resolved"])

    for line in text.splitlines():
        if line.startswith("## "):
            section = line[3:].strip()
        elif match := ENTRY.match(line):
            finish()
            entries.append((match[1], section))
            fields = {}
        elif match := FIELD.match(line):
            fields[match[1]] = match[2]
    finish()
    ids = [entry_id for entry_id, _ in entries]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate IDs")
    return ids


class LedgerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.valid = (Path(__file__).parent / "fixtures" / "valid.md").read_text()

    def test_valid_ledger(self) -> None:
        self.assertEqual(validate(self.valid), ["OL-002", "OL-001"])

    def test_rejects_duplicate_ids(self) -> None:
        with self.assertRaisesRegex(ValueError, "duplicate IDs"):
            validate(self.valid.replace("OL-002", "OL-001"))

    def test_rejects_resolved_entry_left_active(self) -> None:
        with self.assertRaisesRegex(ValueError, "closed status under Active"):
            validate(self.valid.replace("**Status:** blocking", "**Status:** resolved"))

    def test_rejects_closed_entry_without_resolution(self) -> None:
        with self.assertRaisesRegex(ValueError, "missing resolution"):
            validate(self.valid.replace("- **Resolution:** Use PostgreSQL for the first release.\n", ""))


if __name__ == "__main__":
    unittest.main()
