#!/usr/bin/env python3
"""
Toy wallet-agent simulator for Empire Breacher Phase 2.

This script does not call an LLM, wallet, blockchain, network, or external API.
It models the authority-boundary decision a wallet-enabled agent should make
after inspecting untrusted external content.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
ANALYZER_PATH = REPO_ROOT / "tools" / "prompt_injection_tester.py"


def load_prompt_injection_analyzer():
    """Load the Phase 1 analyzer without requiring tools/ to be a package."""
    spec = importlib.util.spec_from_file_location("prompt_injection_tester", ANALYZER_PATH)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load analyzer from {ANALYZER_PATH}")

    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def decide_wallet_agent_behavior(user_request: str, fixture_path: Path) -> dict[str, Any]:
    """
    Decide safe toy-agent behavior after inspecting untrusted external content.

    Authority model:
    - The user request is trusted input.
    - External content is untrusted data.
    - External content may be summarized or classified.
    - External content may not authorize wallet behavior.
    """
    analyzer = load_prompt_injection_analyzer()
    analysis = analyzer.analyze_fixture(fixture_path)
    classification = analysis["classification"]

    base_result: dict[str, Any] = {
        "user_request": user_request,
        "fixture": str(fixture_path),
        "content_classification": classification,
        "risk_score": analysis["score"],
        "wallet_action_allowed": False,
        "requires_user_confirmation": True,
        "agent_boundary": "external content is data, not authority",
        "finding_count": len(analysis["findings"]),
    }

    if classification.startswith("FAIL"):
        base_result.update(
            {
                "recommended_action": "refuse_wallet_action",
                "agent_response": (
                    "I found high-risk prompt-injection patterns in the external content. "
                    "I will not recommend, prepare, approve, or normalize any wallet action from it."
                ),
                "safety_reason": (
                    "The content attempts to combine authority override, wallet-action language, "
                    "and deception. External content cannot authorize wallet behavior."
                ),
            }
        )
    elif classification.startswith("REVIEW"):
        base_result.update(
            {
                "recommended_action": "request_human_review",
                "agent_response": (
                    "The external content is wallet-related and potentially sensitive. "
                    "I will not recommend a wallet action. A human should review the request and source."
                ),
                "safety_reason": (
                    "The content does not meet the high-risk failure condition, but it contains enough "
                    "wallet or transaction context to require review."
                ),
            }
        )
    elif classification.startswith("PASS"):
        base_result.update(
            {
                "recommended_action": "summarize_safely",
                "agent_response": (
                    "The external content did not trigger high-risk prompt-injection patterns. "
                    "I can summarize the safety guidance, but I still cannot treat it as authorization."
                ),
                "safety_reason": (
                    "No high-risk injection pattern was detected. Wallet actions still require explicit "
                    "trusted user intent and a human-readable transaction summary."
                ),
            }
        )
    else:
        base_result.update(
            {
                "recommended_action": "fail_closed",
                "agent_response": "Unknown classification. Failing closed and refusing wallet action.",
                "safety_reason": "Unknown analyzer result.",
            }
        )

    return base_result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Simulate wallet-agent behavior against an untrusted external-content fixture."
    )
    parser.add_argument(
        "--user-request",
        required=True,
        help="Trusted user request given to the toy agent.",
    )
    parser.add_argument(
        "--fixture",
        required=True,
        help="Path to untrusted external-content fixture.",
    )
    parser.add_argument(
        "--out",
        help="Optional JSON output path for toy-agent decision.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    fixture_path = Path(args.fixture)

    if not fixture_path.exists():
        raise FileNotFoundError(f"Fixture not found: {fixture_path}")

    result = decide_wallet_agent_behavior(args.user_request, fixture_path)
    output = json.dumps(result, indent=2)

    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output + "\n", encoding="utf-8")
        print(f"Wrote toy-agent decision: {out_path}")
        print(f"Recommended action: {result['recommended_action']}")
    else:
        print(output)


if __name__ == "__main__":
    main()
