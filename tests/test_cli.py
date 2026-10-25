import subprocess
import sys
import unittest


class CliTests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run([sys.executable, "-m", "playground", *args], capture_output=True, text=True)

    def test_success(self):
        result = self.run_cli("Ada")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "Hello, Ada!\n")
        self.assertEqual(result.stderr, "")

    def test_blank_name(self):
        result = self.run_cli(" ")
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertIn("name must not be empty", result.stderr)

    def test_missing_name(self):
        self.assertEqual(self.run_cli().returncode, 2)
