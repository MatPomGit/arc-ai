"""Synthetic-only tests for version-pinned FACED events parsing."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "research"))
from p01_faced_events import faced_trials
from p01_splits import leave_one_participant_out


HEADER = "onset\tduration\ttrial_type\tvideo_index\tValence\temotion_label\n"


def synthetic_events(*, bom=False):
    technical = "0\t0\tExperiment start\tn/a\tn/a\tn/a\n"
    rated = "".join(
        f"{i*100}\t50\tVideo\t{i}\t{i % 8}\tTargeted category\n"
        for i in range(1, 29)
    )
    return ("\ufeff" if bom else "") + HEADER + technical + rated


class FacedEventsTests(unittest.TestCase):
    def test_exactly_28_rated_events_technical_discarded(self):
        records = faced_trials(synthetic_events(bom=True), "synthetic-person")
        self.assertEqual(len(records), 28)
        self.assertEqual(records[0]["trial_id"], "video-01")
        self.assertEqual(records[-1]["stimulus_id"], "video-28")
        self.assertEqual(records[0]["valence"], 1.0)

    def test_repeat_video_rejected(self):
        with self.assertRaises(ValueError):
            faced_trials(synthetic_events() + "3000\t50\tVideo\t1\t5\tx\n", "synthetic")

    def test_missing_video_rejected(self):
        data = synthetic_events().replace("100\t50\tVideo\t1\t1\t", "")
        with self.assertRaises(ValueError):
            faced_trials(data, "synthetic")

    def test_unrated_index_rejected(self):
        with self.assertRaises(ValueError):
            faced_trials(synthetic_events().replace("200\t50\tVideo\t2\t2\t", "200\t50\tVideo\t2\tn/a\t"), "synthetic")

    def test_unindexed_rating_rejected(self):
        with self.assertRaises(ValueError):
            faced_trials(synthetic_events().replace("Experiment start\tn/a\tn/a", "Experiment start\tn/a\t4"), "synthetic")

    def test_outside_scale_rejected(self):
        with self.assertRaises(ValueError):
            faced_trials(synthetic_events().replace("300\t50\tVideo\t3\t3\t", "300\t50\tVideo\t3\t8\t"), "synthetic")

    def test_technical_event_cannot_substitute_trial(self):
        data = synthetic_events().replace("100\t50\tVideo\t1\t1\t", "100\t50\tVideo\tn/a\tn/a\t")
        with self.assertRaises(ValueError):
            faced_trials(data, "synthetic")

    def test_invalid_span_rejected(self):
        with self.assertRaises(ValueError):
            faced_trials(synthetic_events().replace("400\t50\tVideo\t4", "400\t0\tVideo\t4"), "synthetic")

    def test_missing_headers_rejected(self):
        with self.assertRaises(ValueError):
            faced_trials(synthetic_events().replace("\tValence\t", "\tStimulusTarget\t", 1), "synthetic")

    def test_missing_participant_rejected(self):
        with self.assertRaises(ValueError):
            faced_trials(synthetic_events(), "")

    def test_deterministic_and_loso_compatible(self):
        person_a = faced_trials(synthetic_events(), "synthetic-A")
        person_b = faced_trials(synthetic_events(), "synthetic-B")
        self.assertEqual(person_a, faced_trials(synthetic_events(), "synthetic-A"))
        folds = leave_one_participant_out(person_a + person_b)
        self.assertEqual(len(folds), 2)
        self.assertEqual(len(folds[0].test_indices), 28)


if __name__ == "__main__":
    unittest.main()
