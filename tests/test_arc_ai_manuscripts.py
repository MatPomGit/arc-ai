"""Check the complete ARC AI paper inventory and pinned source materials."""
from __future__ import annotations

import hashlib
import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
MANUSCRIPTS = ROOT / "manuscripts"
EXISTING = {
    "MSC-AFFECT-P01", "MSC-AFFECT-P02", "MSC-AFFECT-P03",
    "MSC-AFFECT-P04", "MSC-AFFECT-P06", "MSC-AFFECT-P08",
}


def blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


class AiManuscriptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = json.loads((ROOT / "portfolio/papers.json").read_text(encoding="utf-8"))
        cls.papers = cls.registry["papers"]

    def test_21_real_msc_packages_and_no_public_approval(self):
        ids = {p["id"] for p in self.papers}
        self.assertEqual(len(self.papers), 21)
        self.assertEqual(len(ids), 21)
        self.assertEqual(len(EXISTING & ids), 6)
        self.assertEqual(len(ids - EXISTING), 15)
        self.assertEqual(
            ids,
            {p.name for p in MANUSCRIPTS.iterdir() if p.is_dir() and p.name.startswith("MSC-")}
        )
        for p in self.papers:
            with self.subTest(id=p["id"]):
                base = MANUSCRIPTS / p["id"]
                self.assertRegex(p["id"], r"^MSC-[A-Z0-9]+(?:-[A-Z0-9]+)+$")
                self.assertEqual(p["owner"], {
                    "mode": "local", "repository": "MatPomGit/arc-ai", "project_id": None
                })
                self.assertEqual(p["relation"], "primary")
                self.assertFalse(p["public_listing"])
                self.assertIsNone(p["stage_evidence"])
                self.assertIsNone(p["doi"])
                self.assertEqual(p["manuscript"], {
                    "path": f"manuscripts/{p['id']}/main.tex", "format": "latex"
                })
                self.assertEqual(p["study_plan"], f"manuscripts/{p['id']}/study.yaml")
                for name in ("main.tex", "study.yaml", "references.bib",
                             "README.md", "journal_targets.md"):
                    file = base / name
                    self.assertTrue(file.is_file(), file)
                    self.assertFalse(file.is_symlink(), file)
                    self.assertGreater(file.stat().st_size, 20, file)
                tex = (base / "main.tex").read_text(encoding="utf-8")
                self.assertIn(r"\begin{abstract}", tex)
                self.assertIn(r"\begin{document}", tex)
                self.assertIn(r"\end{document}", tex)
                self.assertIn("No empirical", tex)
                self.assertIn(p["id"], (base / "README.md").read_text(encoding="utf-8"))
                targets = (base / "journal_targets.md").read_text(encoding="utf-8")
                self.assertEqual(len(re.findall(r"(?m)^[123]\. ", targets)), 3)

    def test_candidates_remain_held_and_existing_stages_preserved(self):
        stages = {p["id"]: p["publication_stage"] for p in self.papers}
        self.assertEqual(stages["MSC-AFFECT-P01"], "draft")
        self.assertEqual(stages["MSC-AFFECT-P08"], "draft")
        for record in self.papers:
            if record["id"] not in EXISTING:
                self.assertEqual(record["research_state"], "deferred")
                self.assertEqual(record["publication_stage"], "concept")
        self.assertEqual(len([p for p in self.papers if p["publication_stage"] == "draft"]), 2)

    def test_original_scientific_files_preserved_by_git_blob(self):
        source = json.loads((MANUSCRIPTS / "affective_sources.json").read_text(encoding="utf-8"))
        self.assertEqual(len(source["records"]), 6)
        self.assertEqual(
            {p["id"] for p in source["records"]}, EXISTING
        )
        self.assertEqual(source["source_snapshot_sha"],
                         "0ff5f1531f03270c4f9fdcc7f3af6d2e9aca85dd")
        for record in source["records"]:
            with self.subTest(id=record["id"]):
                copied = MANUSCRIPTS / record["id"] / "source_plan.md"
                self.assertEqual(blob_sha(copied), record["source_blob_sha"])
                self.assertEqual(record["source_license_spdx"], "Apache-2.0")
                provenance = json.loads((MANUSCRIPTS / record["id"] / "provenance.json").read_text(encoding="utf-8"))
                self.assertEqual(provenance, record, "Local provenance differs from canonical source record")
        # Exact blobs verified against the pinned arc-affective snapshot.
        # Check the complete historical source, not only its main.tex.
        expected = {
            "MSC-AFFECT-P01": {
                "main.tex": "3850b11c3b24f575b112334dce565f04b99bd3aa",
                "sections/introduction.tex": "ef19ddad59d7f68a805a1bcf4a49faf078d32833",
                "sections/methods.tex": "94b64ff2730a49b6ecc29694487f415db7a776a5",
                "sections/results.tex": "b0b73f2dd0512affd32f484745c5002e2d47506a",
                "sections/discussion.tex": "d4594337cbe8f70db829ea4cab3c6c3c30b3f51e",
                "protocol.md": "2e01e5fff48851c352dd32e2c65df2eceea0aa49",
                "references.bib": "00e894c8c7c75110a5cddf923c4e2f3f6116cb50",
            },
            "MSC-AFFECT-P08": {
                "main.tex": "4134a2ebcc973d2bb398dbbef4e5d542fba24dfb",
                "sections/introduction.tex": "1478a468d129e0135be792e4934701a52827e74a",
                "sections/methods.tex": "cf170dd7cc6bf01315810201a47847bc6c62545d",
                "sections/results.tex": "9948b78c578ebd133eee585406e5d361e2c7d8b3",
                "sections/discussion.tex": "d7b923df288221972a50ae0539f0d6b21a764c66",
                "protocol.md": "46c1293a4c02d8b7623cc60e2b38edd701dd8a17",
                "references.bib": "fe779b3f8ee776c754e1a4294c792762d80a204d",
            },
        }
        for ident, files in expected.items():
            for rel, source_sha in files.items():
                with self.subTest(id=ident, path=rel):
                    original = MANUSCRIPTS / ident / "original" / rel
                    self.assertTrue(original.is_file(), original)
                    self.assertEqual(blob_sha(original), source_sha)

        self.assertEqual(blob_sha(MANUSCRIPTS / "ORIGINAL_LICENSE_APACHE_2.0"),
                         "261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64")

    def test_substantive_drafts_are_active_not_only_archived(self):
        # The canonical main.tex must use the complete manuscript sections.
        for ident in ("MSC-AFFECT-P01", "MSC-AFFECT-P08"):
            with self.subTest(id=ident):
                base = MANUSCRIPTS / ident
                active = (base / "main.tex").read_text(encoding="utf-8")
                archived = (base / "original/main.tex").read_text(encoding="utf-8")
                self.assertGreater(len(active), 900)
                self.assertIn(r"\bibliography{references}", active)
                self.assertIn("No empirical", active)
                self.assertIn(r"\documentclass[conference]{IEEEtran}", archived)
                self.assertIn(r"\documentclass[11pt,a4paper]{article}", active)
                self.assertNotIn("Author information to be confirmed", active)
                bibliography = (base / "references.bib").read_bytes()
                self.assertEqual(bibliography, (base / "original/references.bib").read_bytes())
                for name in ("introduction", "methods", "results", "discussion"):
                    self.assertIn(r"\input{sections/" + name + "}", active)
                    current_section = (base / "sections" / (name + ".tex")).read_bytes()
                    historical_section = (base / "original/sections" / (name + ".tex")).read_bytes()
                    if ident == "MSC-AFFECT-P01" and name == "results":
                        # Active reporting table corrected in E4; archived bytes remain SHA-pinned.
                        self.assertNotEqual(current_section, historical_section)
                    else:
                        self.assertEqual(current_section, historical_section)

    def test_p01_continuous_endpoint_matches_reporting_contract(self):
        import yaml
        base = MANUSCRIPTS / "MSC-AFFECT-P01"
        plan = yaml.safe_load((base / "study.yaml").read_text(encoding="utf-8"))
        primary = plan["outcomes"]["primary"]
        self.assertEqual(primary["name"], "Lin concordance correlation coefficient (CCC)")
        self.assertEqual(primary["unit"], "unitless")
        self.assertIn("held-out participants", primary["definition"])
        self.assertIn("constant true ratings", primary["definition"])
        self.assertIn("Mean squared error (MSE)",
                      {item["name"] for item in plan["outcomes"]["secondary"]})
        table = (base / "sections/results.tex").read_text(encoding="utf-8")
        self.assertIn("CCC & MSE", table)
        self.assertIn("CCC is undefined rather than zero", table)
        self.assertNotIn("Balanced acc. & Brier", table)
        methods = (base / "sections/methods.tex").read_text(encoding="utf-8")
        self.assertIn("participant-level Lin concordance correlation coefficient", methods)
        self.assertFalse(plan["evidence"]["protocol_frozen"])

    def test_p08_unfrozen_status_and_goodput_contract(self):
        import yaml
        base = MANUSCRIPTS / "MSC-AFFECT-P08"
        plan = yaml.safe_load((base / "study.yaml").read_text(encoding="utf-8"))
        self.assertEqual(plan["outcomes"]["primary"]["name"], "On-time valid-output goodput")
        self.assertEqual(plan["outcomes"]["primary"]["unit"], "fraction of attempted input events")
        self.assertFalse(plan["evidence"]["protocol_frozen"])
        abstract = (base / "main.tex").read_text(encoding="utf-8")
        self.assertIn("unfrozen pre-preregistration methods draft", abstract)
        self.assertNotIn("preregistration-stage draft", abstract)
        methods = (base / "sections/methods.tex").read_text(encoding="utf-8")
        self.assertIn("proportion of attempted input events yielding an on-time", methods)

    def test_program_citation_and_publication_documents_are_consistent(self):
        import yaml
        program = json.loads((ROOT / "program.json").read_text(encoding="utf-8"))
        citation = yaml.safe_load((ROOT / "CITATION.cff").read_text(encoding="utf-8"))
        self.assertEqual(citation["title"], program["title"])
        self.assertEqual(citation["version"], (ROOT / "VERSION").read_text(encoding="utf-8").strip())
        self.assertNotIn("REPLACE", citation["title"])
        publication = (ROOT / "docs/publication-policy.md").read_text(encoding="utf-8")
        releases = (ROOT / "docs/releases.md").read_text(encoding="utf-8")
        self.assertIn("lokalnym ARC albo zewnętrznym", publication)
        self.assertNotIn("Szablon ma status `scaffold`", releases)
        self.assertNotIn("**Stan szablonu:**", releases)

    def test_study_metadata_correspond_to_registry(self):
        import yaml
        from validate_study import validate_study
        for record in self.papers:
            with self.subTest(id=record["id"]):
                plan = MANUSCRIPTS / record["id"] / "study.yaml"
                study = yaml.safe_load(plan.read_text(encoding="utf-8"))
                self.assertEqual(study["paper_id"], record["id"])
                self.assertFalse(study["evidence"]["protocol_frozen"])
                self.assertEqual(study["evidence"]["empirical_results"], "not_available")
                self.assertTrue(study["hypotheses"])
                self.assertEqual(validate_study(ROOT, record["study_plan"], record["id"]), [])


if __name__ == "__main__":
    unittest.main()
