"""Deterministic, synthetic-testable scoring contract for MSC-AFFECT-P01.

Scores apply to trial-level predictions for a single held-out participant.
No inference, domain validation, or hardware claims follow from these utilities.
"""
from __future__ import annotations

import math
from collections.abc import Mapping, Sequence


def _finite_pairs(y_true: Sequence[float], y_pred: Sequence[float]) -> tuple[list[float], list[float]]:
    """Reject incomplete inputs instead of silently dropping difficult trials."""
    if len(y_true) != len(y_pred) or not y_true:
        raise ValueError("Expected equal, nonempty trial-level sequences")
    actual = [float(value) for value in y_true]
    predicted = [float(value) for value in y_pred]
    if not all(math.isfinite(value) for value in (*actual, *predicted)):
        raise ValueError("All observed and predicted ratings must be finite")
    return actual, predicted


def participant_scores(y_true: Sequence[float], y_pred: Sequence[float]) -> dict[str, float | int | None]:
    """MSE and population-convention Lin CCC; undefined CCC is None.

    P01's prespecified operational convention marks CCC undefined for
    constant true ratings even if software could return a numeric value.
    """
    actual, predicted = _finite_pairs(y_true, y_pred)
    n = len(actual)
    try:
        mse = sum((y - p) ** 2 for y, p in zip(actual, predicted)) / n
    except OverflowError as exc:
        raise ValueError("MSE arithmetic overflow") from exc
    if not math.isfinite(mse):
        raise ValueError("MSE must be finite")
    if n < 2 or min(actual) == max(actual):
        return {"n_trials": n, "ccc": None, "mse": mse}
    try:
        mu_y = sum(actual) / n
        mu_p = sum(predicted) / n
        var_y = sum((y - mu_y) ** 2 for y in actual) / n
        var_p = sum((p - mu_p) ** 2 for p in predicted) / n
        cov = sum((y - mu_y) * (p - mu_p) for y, p in zip(actual, predicted)) / n
        denominator = var_y + var_p + (mu_y - mu_p) ** 2
        ccc = 2 * cov / denominator if denominator > 0 else None
    except OverflowError as exc:
        raise ValueError("CCC arithmetic overflow") from exc
    if not all(math.isfinite(value) for value in (mu_y, mu_p, var_y, var_p, cov, denominator)):
        raise ValueError("CCC intermediate quantities must be finite")
    if ccc is not None and not math.isfinite(ccc):
        raise ValueError("CCC must be finite")
    return {"n_trials": n, "ccc": ccc, "mse": mse}


def paired_montage_scores(
    observed: Mapping[str, float],
    full: Mapping[str, float],
    sparse: Mapping[str, float],
) -> dict[str, float | int | None]:
    """Compare identical trials only; positive CCC loss means sparse is worse.

    Missing or extra trial identifiers are protocol violations and are
    never resolved by intersection or test-label-based imputation.
    """
    keys = set(observed)
    if not keys or keys != set(full) or keys != set(sparse):
        raise ValueError("Observed, full and sparse montages require identical trial IDs")
    ordered = sorted(keys)
    true = [observed[key] for key in ordered]
    score_full = participant_scores(true, [full[key] for key in ordered])
    score_sparse = participant_scores(true, [sparse[key] for key in ordered])
    full_ccc, sparse_ccc = score_full["ccc"], score_sparse["ccc"]
    mse_increase = score_sparse["mse"] - score_full["mse"]
    if not math.isfinite(mse_increase):
        raise ValueError("MSE difference must be finite")
    ccc_loss = None if full_ccc is None or sparse_ccc is None else full_ccc - sparse_ccc
    if ccc_loss is not None and not math.isfinite(ccc_loss):
        raise ValueError("CCC difference must be finite")
    return {
        "n_trials": len(ordered),
        "ccc_full": full_ccc,
        "ccc_sparse": sparse_ccc,
        "ccc_loss": ccc_loss,
        "mse_full": score_full["mse"],
        "mse_sparse": score_sparse["mse"],
        "mse_increase": mse_increase,
    }
