import importlib.util
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
TOOL_PATH = REPO_ROOT / "tools" / "prompt_injection_tester.py"

spec = importlib.util.spec_from_file_location("prompt_injection_tester", TOOL_PATH)
prompt_injection_tester = importlib.util.module_from_spec(spec)

sys.modules[spec.name] = prompt_injection_tester

if spec.loader is None:
    raise ImportError(f"Could not load module from {TOOL_PATH}")

spec.loader.exec_module(prompt_injection_tester)


class PromptInjectionAnalyzerTests(unittest.TestCase):
    def test_malicious_wallet_fixture_is_high_risk(self):
        fixture = REPO_ROOT / "tests" / "fixtures" / "agent_wallet_injection_001.txt"

        result = prompt_injection_tester.analyze_fixture(fixture)

        self.assertEqual(
            result["classification"],
            "FAIL - HIGH RISK PROMPT INJECTION",
        )

    def test_benign_wallet_fixture_passes(self):
        fixture = REPO_ROOT / "tests" / "fixtures" / "agent_wallet_benign_001.txt"

        result = prompt_injection_tester.analyze_fixture(fixture)

        self.assertEqual(
            result["classification"],
            "PASS - NO HIGH-RISK INJECTION PATTERN DETECTED",
        )


if __name__ == "__main__":
    unittest.main()
