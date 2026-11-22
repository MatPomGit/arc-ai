"""Synthetic-only contract tests; do not treat as empirical EEG validation."""
from __future__ import annotations

import math
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research"))
from p01_metrics import paired_montage_scores, participant_scores  # noqa: E402


class ParticipantMetricTests(unittest.TestCase):
    def test_perfect_agreement(self):
        result = participant_scores([0, 1, 2, 3], [0, 1, 2, 3])
        self.assertAlmostEqual(result["ccc"], 1.0)
        self.assertEqual(result["mse"], 0.0)
        self.assertEqual(result["n_trials"], 4)

    def test_constant_target_is_undefined(self):
        result = participant_scores([3, 3, 3], [2, 3, 4])
        self.assertIsNone(result["ccc"])
        self.assertAlmostEqual(result["mse"], 2 / 3)

    def test_single_trial_retains_mse(self):
        result = participant_scores([2], [4])
        self.assertIsNone(result["ccc"])
        self.assertEqual(result["mse"], 4.0)

    def test_sign_reversal(self):
        result = participant_scores([-1, 0, 1], [1, 0, -1])
        self.assertAlmostEqual(result["ccc"], -1.0)

    def test_shift_penalizes_concordance(self):
        result = participant_scores([1, 2, 3], [2, 3, 4])
        self.assertTrue(0 < result["ccc"] < 1)
        self.assertAlmostEqual(result["mse"], 1.0)

    def test_rejects_invalid_trials(self):
        for truth, prediction in [
            ([], []),
            ([1, 2], [1]),
            ([1, float("nan")], [1, 2]),
            ([1, 2], [1, float("inf")]),
        ]:
            with self.subTest(truth=truth, prediction=prediction):
                with self.assertRaises(ValueError):
                    participant_scores(truth, prediction)

    def test_paired_montage_trial_order_independent(self):
        observed = {"trial_b": 2.0, "trial_a": 1.0, "trial_c": 3.0}
        full = {"trial_c": 3.0, "trial_a": 1.0, "trial_b": 2.0}
        sparse = {"trial_a": 1.2, "trial_c": 2.8, "trial_b": 2.0}
        result = paired_montage_scores(observed, full, sparse)
        self.assertEqual(result["n_trials"], 3)
        self.assertAlmostEqual(result["ccc_full"], 1.0)
        self.assertGreater(result["ccc_loss"], 0)
        self.assertGreater(result["mse_increase"], 0)

    def test_paired_montage_missing_trial_fails_closed(self):
        with self.assertRaises(ValueError):
            paired_montage_scores({"a": 1, "b": 2}, {"a": 1, "b": 2}, {"a": 1})
        with self.assertRaises(ValueError):
            paired_montage_scores({"a": 1}, {"a": 1, "b": 2}, {"a": 1})

    def test_paired_constant_target_yields_no_ccc_loss(self):
        result = paired_montage_scores({"a": 2, "b": 2}, {"a": 2, "b": 2}, {"a": 1, "b": 3})
        self.assertIsNone(result["ccc_loss"])
        self.assertEqual(result["mse_full"], 0.0)
        self.assertEqual(result["mse_increase"], 1.0)


if __name__ == "__main__":
    unittest.main()
