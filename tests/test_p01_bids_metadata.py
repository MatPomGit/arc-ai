"""Synthetic in-memory BIDS TSV tests; no participant records or signals."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "research"))
from p01_bids_metadata import Columns, build_trial_metadata
from p01_splits import leave_one_participant_out


COLUMNS = Columns(trial="trial_id", stimulus="stimulus_id", valence="valence")
PEOPLE = "participant_id\tage\nsub-01\tn/a\nsub-02\tn/a\n"
EVENTS_1 = (
    "onset\tduration\ttrial_id\tstimulus_id\tvalence\n"
    "0\t10\tt1\tfilm1\t2\n"
    "11\t10\tt2\tfilm2\t6\n"
)
EVENTS_2 = (
    "onset\tduration\ttrial_id\tstimulus_id\tvalence\n"
    "0\t10\tt1\tfilm1\t4\n"
    "11\t10\tt2\tfilm2\t5\n"
)


def run(*, people=PEOPLE, events=None, columns=COLUMNS, low=0, high=7):
    return build_trial_metadata(
        people,
        events if events is not None else {"sub-01": EVENTS_1, "sub-02": EVENTS_2},
        columns=columns,
        valence_min=low,
        valence_max=high,
    )


class P01BIDSTests(unittest.TestCase):
    def test_valid_trials_and_loso_integration(self):
        rows = run()
        self.assertEqual(len(rows), 4)
        self.assertEqual(rows[0]["valence"], 2.0)
        self.assertEqual(rows[-1]["participant_id"], "sub-02")
        folds = leave_one_participant_out(rows)
        self.assertEqual(len(folds), 2)
        self.assertEqual(folds[0].test_indices, (0, 1))
        self.assertEqual(folds[1].test_indices, (2, 3))

    def test_deterministic_order(self):
        self.assertEqual(
            run(events={"sub-02": EVENTS_2, "sub-01": EVENTS_1}),
            run(events={"sub-01": EVENTS_1, "sub-02": EVENTS_2}),
        )

    def test_no_implicit_category_to_valence_mapping(self):
        bad = EVENTS_1.replace("\tvalence\n", "\temotion_category\n")
        with self.assertRaises(ValueError):
            run(events={"sub-01": bad})

    def test_duplicate_trial_rejected(self):
        with self.assertRaises(ValueError):
            run(events={"sub-01": EVENTS_1 + "30\t10\tt1\tfilm3\t3\n"})

    def test_missing_participant_events_rejected(self):
        with self.assertRaisesRegex(ValueError, "cover exactly"):
            run(events={"sub-01": EVENTS_1})

    def test_unknown_participant_rejected(self):
        with self.assertRaises(ValueError):
            run(events={"sub-03": EVENTS_1})

    def test_duplicate_participant_rejected(self):
        with self.assertRaises(ValueError):
            run(people=PEOPLE + "sub-02\tn/a\n")

    def test_missing_label_rejected(self):
        with self.assertRaises(ValueError):
            run(events={"sub-01": EVENTS_1.replace("\t2\n", "\tn/a\n")})

    def test_nonfinite_valence_rejected(self):
        with self.assertRaises(ValueError):
            run(events={"sub-01": EVENTS_1.replace("\t2\n", "\tnan\n")})

    def test_outside_scale_rejected(self):
        with self.assertRaises(ValueError):
            run(events={"sub-01": EVENTS_1.replace("\t2\n", "\t8\n")})

    def test_invalid_time_rejected(self):
        with self.assertRaises(ValueError):
            run(events={"sub-01": EVENTS_1.replace("0\t10\t", "-1\t10\t")})

    def test_missing_trial_id_rejected(self):
        with self.assertRaises(ValueError):
            run(events={"sub-01": EVENTS_1.replace("\tt1\t", "\t\t")})

    def test_duplicate_header_rejected(self):
        bad = "onset\tduration\ttrial_id\tstimulus_id\tvalence\tvalence\n0\t10\tx\ty\t1\t2\n"
        with self.assertRaises(ValueError):
            run(events={"sub-01": bad})

    def test_bad_scale_rejected(self):
        with self.assertRaises(ValueError):
            run(low=7, high=7)

    def test_incomplete_row_rejected(self):
        with self.assertRaises(ValueError):
            run(events={"sub-01": EVENTS_1 + "20\t10\tthird\n"})

    def test_no_events_rejected(self):
        with self.assertRaises(ValueError):
            run(events={})


if __name__ == "__main__":
    unittest.main()
