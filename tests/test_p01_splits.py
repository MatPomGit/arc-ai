"""Synthetic-only checks for P01 trial splitting and leakage prevention."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "research"))
from p01_splits import leave_one_participant_out, participant_stimulus_block


def fixture():
    return [
        {"participant_id": p, "trial_id": t, "stimulus_id": t}
        for p in ("A", "B", "C")
        for t in ("film1", "film2", "film3")
    ]


class P01SplitTests(unittest.TestCase):
    def test_loso_holds_out_complete_participants(self):
        rows = fixture()
        folds = leave_one_participant_out(rows)
        self.assertEqual(len(folds), 3)
        self.assertEqual({tuple(f.test_indices) for f in folds},
                         {(0, 1, 2), (3, 4, 5), (6, 7, 8)})
        for fold in folds:
            self.assertFalse(set(fold.train_indices) & set(fold.test_indices))
            self.assertEqual(set(fold.train_indices) | set(fold.test_indices), set(range(9)))
            train_p = {rows[i]["participant_id"] for i in fold.train_indices}
            test_p = {rows[i]["participant_id"] for i in fold.test_indices}
            self.assertFalse(train_p & test_p)
            self.assertEqual(fold.excluded_indices, ())

    def test_loso_is_deterministic(self):
        self.assertEqual(leave_one_participant_out(fixture()),
                         leave_one_participant_out(fixture()))

    def test_loso_does_not_emit_identifiers(self):
        folds = leave_one_participant_out(fixture())
        self.assertTrue(all(isinstance(i, int) for f in folds
                            for i in (*f.train_indices, *f.test_indices)))

    def test_joint_block_excludes_cross_cells(self):
        rows = fixture()
        fold = participant_stimulus_block(
            rows, held_out_participant="A", held_out_stimuli=("film1", "film2")
        )
        self.assertEqual(fold.test_indices, (0, 1))
        self.assertEqual(fold.train_indices, (5, 8))
        self.assertEqual(fold.excluded_indices, (2, 3, 4, 6, 7))
        train_p = {rows[i]["participant_id"] for i in fold.train_indices}
        test_p = {rows[i]["participant_id"] for i in fold.test_indices}
        train_s = {rows[i]["stimulus_id"] for i in fold.train_indices}
        test_s = {rows[i]["stimulus_id"] for i in fold.test_indices}
        self.assertFalse(train_p & test_p)
        self.assertFalse(train_s & test_s)

    def test_single_test_trial_cannot_support_ccc(self):
        with self.assertRaises(ValueError):
            participant_stimulus_block(
                fixture(), held_out_participant="A", held_out_stimuli=("film1",)
            )

    def test_duplicate_participant_trial_fails(self):
        rows = fixture()
        with self.assertRaises(ValueError):
            leave_one_participant_out(rows + [dict(rows[0])])

    def test_invalid_metadata_fails(self):
        for rows in ([], [{"participant_id": "A", "trial_id": "x"}],
                     [{"participant_id": "A", "trial_id": "", "stimulus_id": "s"}]):
            with self.subTest(rows=rows), self.assertRaises(ValueError):
                leave_one_participant_out(rows)

    def test_single_participant_fails(self):
        with self.assertRaises(ValueError):
            leave_one_participant_out(fixture()[:3])

    def test_unknown_joint_holdout_fails(self):
        with self.assertRaises(ValueError):
            participant_stimulus_block(fixture(), held_out_participant="Z",
                                       held_out_stimuli=("film1", "film2"))
        with self.assertRaises(ValueError):
            participant_stimulus_block(fixture(), held_out_participant="A",
                                       held_out_stimuli=("missing", "film2"))

    def test_block_with_no_training_trials_fails(self):
        with self.assertRaises(ValueError):
            participant_stimulus_block(fixture(), held_out_participant="A",
                                       held_out_stimuli=("film1", "film2", "film3"))


if __name__ == "__main__":
    unittest.main()
