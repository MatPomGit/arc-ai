"""Aggregate-only FACED BIDS Git tree inventory validator (no participant IDs).

Consumes a pinned GitHub Git Trees API JSON response supplied as text.
No file content, signals, person identifiers, or network requests are read.
The Git tree must be non-truncated. This is structural verification only.
"""
from __future__ import annotations

import json
import re
from collections.abc import Mapping

_EEG = re.compile(
    r"^sub-([A-Za-z0-9]+?)/eeg/sub-\1_task-watchingVideoClips_"
    r"(events\.tsv|channels\.tsv|eeg\.bdf)$"
)
_EXPECTED = frozenset({"events.tsv", "channels.tsv", "eeg.bdf"})
_ROOT = frozenset({"participants.tsv", "dataset_description.json", "stimuli/stimuli.tsv"})


def audit_faced_tree(tree_json: str, *, expected_participants: int = 123) -> dict[str, object]:
    """Fail closed on absent/ambiguous paths and output aggregate evidence only."""
    try:
        obj = json.loads(tree_json)
    except (TypeError, ValueError) as exc:
        raise ValueError("Invalid Git tree JSON") from exc
    if not isinstance(obj, dict) or obj.get("truncated") is not False:
        raise ValueError("Git tree unavailable or truncated")
    tree_sha = obj.get("sha")
    if not isinstance(tree_sha, str) or not re.fullmatch(r"[0-9a-f]{40}", tree_sha):
        raise ValueError("Require a pinned 40-hex Git tree SHA")
    if not isinstance(expected_participants, int) or isinstance(expected_participants, bool) or expected_participants < 2:
        raise ValueError("Invalid expected participant count")
    entries = obj.get("tree")
    if not isinstance(entries, list) or not entries:
        raise ValueError("Empty or missing tree")
    by_participant: dict[str, set[str]] = {}
    paths: set[str] = set()
    root_files: set[str] = set()
    for entry in entries:
        if not isinstance(entry, Mapping):
            raise ValueError("Malformed tree entry")
        path = entry.get("path")
        kind = entry.get("type")
        if not isinstance(path, str) or not path or path in paths:
            raise ValueError("Missing/duplicate file path")
        paths.add(path)
        if path in _ROOT:
            if kind != "blob":
                raise ValueError("Required root metadata not a blob")
            root_files.add(path)
        match = _EEG.fullmatch(path)
        if match:
            if kind != "blob":
                raise ValueError("EEG metadata/pointer path not a blob")
            person, suffix = match.groups()
            by_participant.setdefault(person, set()).add(suffix)
            if suffix == "eeg.bdf":
                size = entry.get("size")
                if not isinstance(size, int) or size < 0 or size > 1024:
                    raise ValueError("BDF should be a small Git-annex pointer, not signal data")
    if root_files != _ROOT:
        raise ValueError("Required root BIDS files missing")
    if len(by_participant) != expected_participants:
        raise ValueError("Unexpected number of participant folders")
    if any(files != _EXPECTED for files in by_participant.values()):
        raise ValueError("Incomplete event/channel/BDF path triad")
    return {
        "source_tree_sha": tree_sha,
        "expected_participants": expected_participants,
        "participant_folders_complete": len(by_participant),
        "event_tables": len(by_participant),
        "channel_tables": len(by_participant),
        "bdf_pointers_only": len(by_participant),
        "root_metadata_files": len(root_files),
        "structural_gate": "PASS",
        "event_content_gate": "NOT_RUN",
        "eeg_signal_gate": "NOT_RUN",
        "labels_gate": "NOT_RUN",
    }
