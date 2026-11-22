"""Negative inventory tests; no LaTeX or network required."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "compile_arc_ai_manuscripts.py"
spec = importlib.util.spec_from_file_location("arc_ai_compile", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class InventoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "manuscripts"
        self.root.mkdir()
        self.package = self.root / "MSC-TEST-P01"
        self.package.mkdir()
        self.paper = {"id": "MSC-TEST-P01",
                      "manuscript": {"path": "manuscripts/MSC-TEST-P01/main.tex"}}

    def test_valid_package(self):
        module.validate_inventory([self.paper], self.root)

    def test_missing_package(self):
        self.package.rmdir()
        with self.assertRaisesRegex(ValueError, "missing="):
            module.validate_inventory([self.paper], self.root)

    def test_extra_package(self):
        (self.root / "MSC-EXTRA-P02").mkdir()
        with self.assertRaisesRegex(ValueError, "unregistered="):
            module.validate_inventory([self.paper], self.root)

    def test_symlink_package(self):
        target = self.root / "safe-target"
        self.package.rename(target)
        self.package.symlink_to(target, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "Unsafe manuscript package"):
            module.validate_inventory([self.paper], self.root)

    def test_redirected_registry_path(self):
        self.paper["manuscript"]["path"] = "manuscripts/other/main.tex"
        with self.assertRaisesRegex(ValueError, "Unsafe manuscript package"):
            module.validate_inventory([self.paper], self.root)


if __name__ == "__main__":
    unittest.main()
