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
    if len(papers) != 21 or len({p["id"] for p in papers}) != 21:
        raise ValueError("Expected 21 unique MSC manuscripts")
    for paper in papers:
        source = ROOT / paper["manuscript"]["path"]
        if (source.name != "main.tex" or source.is_symlink()
                or not source.is_file() or not source.resolve().is_relative_to(ROOT.resolve())):
            raise ValueError("Unsafe manuscript source: " + paper["id"])
        with tempfile.TemporaryDirectory(prefix="arc-ai-latex-") as temp:
            dst = Path(temp)
            shutil.copyfile(source, dst / "main.tex")
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
    print("ARC AI 21/21 LaTeX manuscripts compiled in isolated temporary directories.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
