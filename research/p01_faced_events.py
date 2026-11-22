"""FACED/NEMAR event-table adapter for MSC-AFFECT-P01.

No EEG is loaded. The caller supplies a pinned-version events.tsv string,
an explicitly matched participant pseudonym, and the reviewed BIDS file
provenance. Neither stimulus-level target labels nor demographic fields
are used as participant self-report.
"""
from __future__ import annotations

import csv
import io
import math


EXPECTED = {"onset", "duration", "video_index", "Valence"}
EXPECTED_VIDEOS = frozenset(range(1, 29))


def faced_trials(events_tsv: str, participant_id: str) -> list[dict[str, object]]:
    """Read 28 rated clip events from one FACED BIDS recording.

    Returns internal join keys; do not upload outputs or raw IDs to public CI.
    Technical events without a video index are excluded. Indexed event rows
    must have a valid individual rating: missing labels fail closed.
    """
    if not isinstance(participant_id, str) or not participant_id.strip():
        raise ValueError("Participant ID must be supplied by a trusted BIDS file mapping")
    if not isinstance(events_tsv, str) or not events_tsv.strip():
        raise ValueError("Missing events.tsv")
    reader = csv.DictReader(io.StringIO(events_tsv.lstrip("\ufeff")), delimiter="\t")
    names = reader.fieldnames or []
    if len(names) != len(set(names)) or not EXPECTED.issubset(set(names)):
        raise ValueError("FACED events.tsv mandatory columns missing or duplicated")
    trials = []
    seen = set()
    for row in reader:
        if None in row or any(value is None for value in row.values()):
            raise ValueError("Malformed FACED events.tsv record")
        raw_video = row["video_index"].strip()
        if raw_video.lower() in {"", "n/a"}:
            if row["Valence"].strip().lower() not in {"", "n/a"}:
                raise ValueError("Unindexed event contains a valence rating")
            continue
        if not raw_video.isdecimal():
            raise ValueError("Noninteger FACED video_index")
        video = int(raw_video)
        if video not in EXPECTED_VIDEOS or video in seen:
            raise ValueError("Unknown or repeated FACED video_index")
        seen.add(video)
        try:
            valence = float(row["Valence"])
            onset = float(row["onset"])
            duration = float(row["duration"])
        except (ValueError, TypeError) as exc:
            raise ValueError("Invalid FACED rating or timing") from exc
        if not (math.isfinite(valence) and 0 <= valence <= 7):
            raise ValueError("FACED individual valence must be finite and within 0-7")
        if not (math.isfinite(onset) and math.isfinite(duration) and duration > 0):
            raise ValueError("FACED video span requires finite onset and positive duration")
        trials.append({
            "participant_id": participant_id,
            "trial_id": f"video-{video:02d}",
            "stimulus_id": f"video-{video:02d}",
            "valence": valence,
            "onset": onset,
            "duration": duration,
        })
    if seen != EXPECTED_VIDEOS:
        raise ValueError("Expected exactly 28 rated FACED videos per participant")
    return sorted(trials, key=lambda trial: int(trial["trial_id"].split("-")[1]))
