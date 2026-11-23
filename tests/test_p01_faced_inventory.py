"""Synthetic-only aggregate BIDS structural audit tests, no subject data."""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "research"))
from p01_faced_inventory import audit_faced_tree


SHA = "a" * 40


def fake_tree(*, people=3, omit=None, truncated=False, bdf_size=104):
    entries = [
        {"path": p, "type": "blob", "size": 20}
        for p in ("participants.tsv", "dataset_description.json", "stimuli/stimuli.tsv")
    ]
    for i in range(people):
        person = f"sub-{i:03d}"
        for name in ("events.tsv", "channels.tsv", "eeg.bdf"):
            path = f"{person}/eeg/{person}_task-watchingVideoClips_{name}"
            if path != omit:
                entries.append({
                    "path": path, "type": "blob",
                    "size": bdf_size if name == "eeg.bdf" else 1200,
                })
    return {"sha": SHA, "truncated": truncated, "tree": entries}


class FacedInventoryTests(unittest.TestCase):
    def test_complete_aggregate_counts_and_no_ids(self):
        out = audit_faced_tree(json.dumps(fake_tree()), expected_participants=3)
        self.assertEqual(out["participant_folders_complete"], 3)
        self.assertEqual(out["event_tables"], 3)
        self.assertEqual(out["channel_tables"], 3)
        self.assertEqual(out["bdf_pointers_only"], 3)
        self.assertEqual(out["structural_gate"], "PASS")
        self.assertEqual(out["event_content_gate"], "NOT_RUN")
        self.assertNotIn("sub-", json.dumps(out))

    def test_incomplete_triad_rejected(self):
        with self.assertRaises(ValueError):
            audit_faced_tree(json.dumps(fake_tree(
                omit="sub-001/eeg/sub-001_task-watchingVideoClips_events.tsv"
            )), expected_participants=3)

    def test_truncated_tree_rejected(self):
        with self.assertRaises(ValueError):
            audit_faced_tree(json.dumps(fake_tree(truncated=True)), expected_participants=3)

    def test_missing_root_metadata_rejected(self):
        obj = fake_tree()
        obj["tree"] = [x for x in obj["tree"] if x["path"] != "participants.tsv"]
        with self.assertRaises(ValueError):
            audit_faced_tree(json.dumps(obj), expected_participants=3)

    def test_invalid_sha_rejected(self):
        obj = fake_tree()
        obj["sha"] = "main"
        with self.assertRaises(ValueError):
            audit_faced_tree(json.dumps(obj), expected_participants=3)

    def test_duplicate_path_rejected(self):
        obj = fake_tree()
        obj["tree"].append(dict(obj["tree"][-1]))
        with self.assertRaises(ValueError):
            audit_faced_tree(json.dumps(obj), expected_participants=3)

    def test_unexpected_participant_count_rejected(self):
        with self.assertRaises(ValueError):
            audit_faced_tree(json.dumps(fake_tree()), expected_participants=123)

    def test_large_bdf_is_rejected_as_possible_raw_data(self):
        with self.assertRaises(ValueError):
            audit_faced_tree(json.dumps(fake_tree(bdf_size=500000)), expected_participants=3)

    def test_invalid_and_missing_tree_rejected(self):
        for obj in ("not json", "{}", '{"sha": "a", "truncated": false, "tree": []}'):
            with self.subTest(obj=obj), self.assertRaises(ValueError):
                audit_faced_tree(obj, expected_participants=3)

    def test_nonblob_required_file_rejected(self):
        obj = fake_tree()
        obj["tree"][0]["type"] = "tree"
        with self.assertRaises(ValueError):
            audit_faced_tree(json.dumps(obj), expected_participants=3)


if __name__ == "__main__":
    unittest.main()
