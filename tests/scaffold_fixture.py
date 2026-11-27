"""Restore the original empty ARC scaffold only inside disposable test copies.

The configured public ARC AI repository must never be reinitialized by lifecycle tests.
"""
from __future__ import annotations

import shutil
from pathlib import Path

FILES = (
    "README.md", "RESEARCH.md", "ROADMAP.md", "CITATION.cff",
    "PROJECT_STATE.yaml", "program.json", "config/research-lines.json",
    "config/papers-v2.json", "docs/scientific-scope.md",
)


def restore_scaffold(root: Path) -> Path:
    root = Path(root)
    fixtures = root / "tests" / "fixtures" / "arc-scaffold"
    for name in FILES:
        original = fixtures / name
        target = root / name
        if not original.is_file() or target.is_symlink():
            raise ValueError("Untrusted test scaffold fixture: " + name)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(original.read_bytes())
    manuscript_root = root / "manuscripts"
    if manuscript_root.is_symlink():
        raise ValueError("Unsafe test fixture manuscript root")
    if manuscript_root.exists():
        shutil.rmtree(manuscript_root)
    return root


def copytree_scaffold(*args, **kwargs):
    """Copy the configured ARC into a disposable template test directory."""
    return restore_scaffold(shutil.copytree(*args, **kwargs))
