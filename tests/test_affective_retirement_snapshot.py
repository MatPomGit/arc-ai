"""Pre-deletion audit must not silently lose archived issue discussions."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "archive/arc-affective"


class RetirementSnapshotTests(unittest.TestCase):
    def test_complete_issue_text_snapshot(self):
        data = json.loads((ARCHIVE / "issues-and-comments.json").read_text(encoding="utf-8"))
        items = data["issues"]
        self.assertEqual(len(items), 73)
        self.assertEqual(sum(x["state"] == "open" for x in items), 69)
        self.assertEqual(sum(x["state"] == "closed" for x in items), 4)
        self.assertEqual(len({x["number"] for x in items}), 73)
        self.assertEqual(sum(x["comments"] for x in items), 61)
        self.assertEqual(sum(len(t["comments"]) for t in data["comment_threads"]), 61)
        self.assertTrue(all(x["original_url"].startswith(
            "https://github.com/MatPomGit/arc-affective/issues/") for x in items))
        self.assertEqual(data["export_status"], "ISSUES_AND_COMMENTS_ONLY_NOT_GIT_HISTORY")

    def test_pr_snapshot_does_not_claim_git_backup(self):
        data = json.loads((ARCHIVE / "prs-and-tree.json").read_text(encoding="utf-8"))
        self.assertEqual(len(data["closed_pull_requests"]), 33)
        self.assertEqual(len(data["source_tree"]), 118)
        self.assertEqual(len({x["path"] for x in data["source_tree"]}), 118)
        self.assertIn("NOT backed up", data["notes"])
        report = (ARCHIVE / "README.md").read_text(encoding="utf-8")
        self.assertIn("DELETE_NOT_SAFE", report)
        self.assertIn("git bundle", report)


if __name__ == "__main__":
    unittest.main()
