"""Compile each registered ARC AI main.tex in isolation with no network or source mutations."""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    if not shutil.which("latexmk") or not shutil.which("pdflatex"):
        print("LaTeX toolchain required; refusing to claim success", file=sys.stderr)
        return 2
    papers = json.loads((ROOT / "portfolio/papers.json").read_text(encoding="utf-8"))["papers"]
    if not papers or len({p["id"] for p in papers}) != len(papers):
        raise ValueError("Expected a nonempty set of unique MSC manuscripts")
    registered = {p["id"] for p in papers}
    manuscript_root = ROOT / "manuscripts"
    on_disk = {
        entry.name for entry in manuscript_root.iterdir()
        if entry.name.startswith("MSC-") and (entry.is_dir() or entry.is_symlink())
    }
    if registered != on_disk:
        missing = sorted(registered - on_disk)
        unregistered = sorted(on_disk - registered)
        raise ValueError(
            f"Manuscript inventory mismatch: missing={missing}, unregistered={unregistered}"
        )
    for paper in papers:
        source = ROOT / paper["manuscript"]["path"]
        if (source.name != "main.tex" or source.is_symlink()
                or not source.is_file() or not source.resolve().is_relative_to(ROOT.resolve())):
            raise ValueError("Unsafe manuscript source: " + paper["id"])
        with tempfile.TemporaryDirectory(prefix="arc-ai-latex-") as temp:
            dst = Path(temp)
            # Copy the registered manuscript and its explicit LaTeX inputs only.
            # This prevents hidden dependencies on files from the source tree.
            shutil.copyfile(source, dst / "main.tex")
            latex = source.read_text(encoding="utf-8")
            if r"\input{sections/" in latex:
                section_names = ("introduction", "methods", "results", "discussion")
                section_dir = source.parent / "sections"
                if section_dir.is_symlink():
                    raise ValueError("Symlinked LaTeX sections: " + paper["id"])
                (dst / "sections").mkdir()
                for section_name in section_names:
                    relative = f"sections/{section_name}.tex"
                    if r"\input{sections/" + section_name + "}" not in latex:
                        raise ValueError("Missing LaTeX inclusion: " + paper["id"])
                    section_file = section_dir / (section_name + ".tex")
                    if (not section_file.is_file() or section_file.is_symlink()
                            or not section_file.resolve().is_relative_to(ROOT.resolve())):
                        raise ValueError("Unsafe LaTeX section: " + relative)
                    shutil.copyfile(section_file, dst / relative)
            if r"\bibliography{references}" in latex:
                bibliography = source.parent / "references.bib"
                if (not bibliography.is_file() or bibliography.is_symlink()
                        or not bibliography.resolve().is_relative_to(ROOT.resolve())):
                    raise ValueError("Unsafe references.bib: " + paper["id"])
                shutil.copyfile(bibliography, dst / "references.bib")
            result = subprocess.run(
                ["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error",
                 "-file-line-error", "main.tex"],
                cwd=dst, text=True, capture_output=True, timeout=75, check=False,
            )
            if result.returncode != 0 or not (dst / "main.pdf").is_file():
                print("LaTeX FAIL:", paper["id"], file=sys.stderr)
                print((result.stdout + result.stderr)[-5000:], file=sys.stderr)
                return 1
            if (dst / "main.pdf").stat().st_size < 1000:
                print("PDF too small:", paper["id"], file=sys.stderr)
                return 1
            print("LaTeX PASS:", paper["id"])
    print(f"ARC AI {len(papers)}/{len(papers)} LaTeX manuscripts compiled in isolated temporary directories.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
