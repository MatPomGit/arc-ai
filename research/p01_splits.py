"""Leakage-resistant, deterministic index splits for MSC-AFFECT-P01.

The interface accepts already-reviewed trial metadata; it never reads raw EEG
and deliberately returns only row indices, not participant identifiers.
No inference about legal data access or protocol freeze is made here.
"""
from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass


@dataclass(frozen=True)
class Split:
    train_indices: tuple[int, ...]
    test_indices: tuple[int, ...]
    excluded_indices: tuple[int, ...] = ()


def _records(rows: Sequence[Mapping[str, object]]) -> list[tuple[str, str, str]]:
    if not rows:
        raise ValueError("Trial metadata must be nonempty")
    normalized: list[tuple[str, str, str]] = []
    seen: set[tuple[str, str]] = set()
    for row in rows:
        parts: list[str] = []
        for name in ("participant_id", "trial_id", "stimulus_id"):
            value = row.get(name)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"Missing or invalid {name}")
            parts.append(value)
        participant, trial, stimulus = parts
        key = (participant, trial)
        if key in seen:
            raise ValueError("Repeated participant/trial identifier")
        seen.add(key)
        normalized.append((participant, trial, stimulus))
    return normalized


def leave_one_participant_out(rows: Sequence[Mapping[str, object]]) -> tuple[Split, ...]:
    """One held-out participant per fold; all their trials stay in test."""
    records = _records(rows)
    participants = sorted({participant for participant, _, _ in records})
    if len(participants) < 2:
        raise ValueError("At least two distinct participants are required")
    folds = []
    for held_out in participants:
        train = tuple(i for i, (p, _, _) in enumerate(records) if p != held_out)
        test = tuple(i for i, (p, _, _) in enumerate(records) if p == held_out)
        folds.append(Split(train_indices=train, test_indices=test))
    return tuple(folds)


def participant_stimulus_block(
    rows: Sequence[Mapping[str, object]],
    *,
    held_out_participant: str,
    held_out_stimuli: Sequence[str],
) -> Split:
    """Joint exclusion: test subject + unseen stimuli, excluding cross-cells.

    Training excludes all trials by the test participant AND all appearances
    of test stimuli in other participants. Unused cross-cells are reported as
    excluded, not silently moved into either partition.
    """
    records = _records(rows)
    stimuli = set(held_out_stimuli)
    if not held_out_participant or not stimuli or any(not s for s in stimuli):
        raise ValueError("Explicit participant and nonempty stimulus block required")
    if held_out_participant not in {p for p, _, _ in records}:
        raise ValueError("Unknown held-out participant")
    if not stimuli.issubset({s for _, _, s in records}):
        raise ValueError("Unknown held-out stimulus")
    train: list[int] = []
    test: list[int] = []
    excluded: list[int] = []
    for index, (participant, _, stimulus) in enumerate(records):
        if participant == held_out_participant and stimulus in stimuli:
            test.append(index)
        elif participant != held_out_participant and stimulus not in stimuli:
            train.append(index)
        else:
            excluded.append(index)
    if not train or len(test) < 2:
        raise ValueError("A valid block needs training data and at least two test trials")
    return Split(tuple(train), tuple(test), tuple(excluded))
