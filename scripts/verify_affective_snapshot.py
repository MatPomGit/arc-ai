"""Fail-closed offline proof of source-byte integrity for imported ARC Affective code.

Verifies exact Git blob SHA, names and no symbolic links. Does not execute imported code.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "research" / "affective"
MANIFEST = SOURCE / "source_manifest.json"


def inspect() -> dict:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if (data.get("schema_version") != 1 or
            data.get("source_repository") != "MatPomGit/arc-affective" or
            data.get("source_commit_sha") != "0ff5f1531f03270c4f9fdcc7f3af6d2e9aca85dd" or
            data.get("reproduced_empirical_results") is not False or
            data.get("real_hardware_validation") is not False):
        raise ValueError("Invalid source provenance metadata")
    records = data.get("files")
    if not isinstance(records, list) or len(records) != 52:
        raise ValueError("Expected exactly 52 pinned source files")
    checked = set()
    counts = {"src": 0, "tests": 0, "reports": 0, "pyproject.toml": 0}
    for row in records:
        if not isinstance(row, dict):
            raise ValueError("Invalid source record")
        original = row.get("source_path")
        destination = row.get("destination_path")
        expected = row.get("blob_sha")
        if not isinstance(original, str) or not isinstance(destination, str):
            raise ValueError("Malformed source path")
        parts = PurePosixPath(original).parts
        if (not parts or original.startswith("/") or
                any(x in {"", ".", ".."} for x in parts) or
                "\\" in original or "//" in original or
                destination != "research/affective/" + original or
                destination in checked):
            raise ValueError("Untrusted source path: " + original)
        checked.add(destination)
        if not isinstance(expected, str) or len(expected) != 40 or any(ch not in "0123456789abcdef" for ch in expected):
            raise ValueError("Invalid source blob SHA")
        file = ROOT / destination
        if not file.is_file() or file.is_symlink():
            raise ValueError("Missing or symlinked imported source: " + original)
        if any((ROOT / "/".join(PurePosixPath(destination).parts[:i])).is_symlink()
               for i in range(1, len(PurePosixPath(destination).parts))):
            raise ValueError("Symlink in imported source ancestry: " + original)
        raw = file.read_bytes()
        actual = hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()
        if actual != expected:
            raise ValueError("Pinned source blob mismatch: " + original)
        if original.startswith("src/arc_affective/"):
            counts["src"] += 1
        elif original.startswith("tests/test_p0"):
            counts["tests"] += 1
        elif original.startswith("reports/P0"):
            counts["reports"] += 1
        elif original == "pyproject.toml":
            counts["pyproject.toml"] += 1
        else:
            raise ValueError("Unapproved source path: " + original)
    if counts != {"src": 19, "tests": 15, "reports": 17, "pyproject.toml": 1}:
        raise ValueError("Incorrect source inventory: " + repr(counts))
    for group, folder, suffix in (
            ("src", SOURCE / "src/arc_affective", "*.py"),
            ("tests", SOURCE / "tests", "*.py"),
            ("reports", SOURCE / "reports", "*.md")):
        for path in folder.glob(suffix):
            if path.relative_to(ROOT).as_posix() not in checked:
                raise ValueError("Untracked source " + group + ": " + path.name)
    return {"status": "PASS", "files": len(checked), "source_sha": data["source_commit_sha"],
            "counts": counts, "evidence": "E0_synthetic_only"}


def main() -> int:
    try:
        print(json.dumps(inspect(), indent=2, sort_keys=True))
        return 0
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print("SOURCE_SNAPSHOT_FAIL:", str(exc))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
