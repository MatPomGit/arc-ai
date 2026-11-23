"""Strict in-memory BIDS TSV adapter for the P01 candidate EEG benchmark.

Consumes *explicitly mapped* metadata tables, never EEG signal files.
FACED-specific field names must be audited before supplying column mapping.
Returned IDs are sensitive internal join keys and must not be committed.
"""
from __future__ import annotations

import csv
import io
import math
from collections.abc import Mapping
from dataclasses import dataclass


@dataclass(frozen=True)
class Columns:
    trial: str
    stimulus: str
    valence: str
    onset: str = "onset"
    duration: str = "duration"


def _tsv(text: str, required: tuple[str, ...]) -> list[dict[str, str]]:
    reader = csv.DictReader(io.StringIO(text), delimiter="\t")
    names = reader.fieldnames
    if not names or len(set(names)) != len(names) or any(col not in names for col in required):
        raise ValueError("Missing or duplicated mandatory TSV headers")
    output = []
    for row in reader:
        if None in row or any(value is None for value in row.values()):
            raise ValueError("Malformed TSV row or inconsistent column count")
        output.append(row)
    if not output:
        raise ValueError("Empty TSV table")
    return output


def _required(value: str | None, field: str) -> str:
    if not isinstance(value, str) or not value.strip() or value.strip().lower() == "n/a":
        raise ValueError(f"Missing mandatory {field}")
    return value.strip()


def _real(value: str | None, field: str, *, minimum: float | None = None) -> float:
    raw = _required(value, field)
    try:
        parsed = float(raw)
    except ValueError as exc:
        raise ValueError(f"Non-numeric {field}") from exc
    if not math.isfinite(parsed) or (minimum is not None and parsed < minimum):
        raise ValueError(f"Out-of-range {field}")
    return parsed


def build_trial_metadata(
    participants_tsv: str,
    events_tsv_by_participant: Mapping[str, str],
    *,
    columns: Columns,
    valence_min: float,
    valence_max: float,
) -> list[dict[str, object]]:
    """Return validated trial metadata usable by P01 split/score functions.

    The caller supplies exact participant->events.tsv pairing and a reviewed
    column mapping; this function cannot infer labels from stimulus categories.
    One event row is one unique rated trial. In particular, EEG epochs are
    not reinterpreted as independent self-report observations.
    """
    if not math.isfinite(valence_min) or not math.isfinite(valence_max) or valence_min >= valence_max:
        raise ValueError("Invalid declared valence scale")
    fields = (columns.trial, columns.stimulus, columns.valence, columns.onset, columns.duration)
    if any(not field for field in fields) or len(set(fields)) != len(fields):
        raise ValueError("Event columns must be unique and explicitly specified")
    people = _tsv(participants_tsv, ("participant_id",))
    person_ids = [_required(row["participant_id"], "participant_id") for row in people]
    if len(person_ids) != len(set(person_ids)):
        raise ValueError("Duplicate participant entry")
    if set(events_tsv_by_participant) != set(person_ids):
        raise ValueError("Events must cover exactly the declared participant roster")
    trials: list[dict[str, object]] = []
    seen: set[tuple[str, str]] = set()
    for participant in sorted(events_tsv_by_participant):
        rows = _tsv(events_tsv_by_participant[participant], fields)
        for row in rows:
            trial = _required(row[columns.trial], "trial ID")
            stimulus = _required(row[columns.stimulus], "stimulus ID")
            onset = _real(row[columns.onset], "onset", minimum=0)
            duration = _real(row[columns.duration], "duration", minimum=0)
            valence = _real(row[columns.valence], "valence")
            if not valence_min <= valence <= valence_max:
                raise ValueError("Valence outside declared original scale")
            key = (participant, trial)
            if key in seen:
                raise ValueError("Duplicate trial in participant")
            seen.add(key)
            trials.append({
                "participant_id": participant,
                "trial_id": trial,
                "stimulus_id": stimulus,
                "valence": valence,
                "onset": onset,
                "duration": duration,
            })
    return trials
