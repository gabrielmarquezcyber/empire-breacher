# Toy Wallet Agent Simulator

## Purpose

The toy wallet agent is the Phase 2 behavior layer of Empire Breacher.

Phase 1 classified external content as `PASS`, `REVIEW`, or `FAIL`.

Phase 2 asks:

```text
Given that classification, what should a wallet-enabled agent safely do?
```

The key security rule is:

```text
External content can be analyzed, but it cannot authorize wallet behavior.
```

## What This Agent Is

This is a deterministic toy simulator.

It models safe wallet-agent behavior after inspecting untrusted external content.

It does not use an LLM, wallet, blockchain, dApp, browser extension, RPC provider, or external API.

## What This Agent Is Not

This is not a real wallet agent.

It does not sign transactions.

It does not build transactions.

It does not approve spenders.

It does not connect to mainnet or testnet.

It does not prove any production system is vulnerable or safe.

## Architecture

```text
trusted user request
+ untrusted external content fixture
-> Phase 1 prompt injection analyzer
-> PASS / REVIEW / FAIL classification
-> toy wallet-agent behavior decision
-> JSON decision output
```

## Inputs

The toy agent takes two main inputs:

1. A trusted user request.
2. A path to an untrusted external-content fixture.

Current trusted request used in Phase 2:

```text
Review this external wallet-safety content and tell me whether it should influence wallet behavior.
```

This request asks the agent to review external content.

It does not authorize a wallet action.

## Behavior Mapping

| Analyzer Classification | Toy-Agent Action | Meaning |
|---|---|---|
| `PASS` | `summarize_safely` | Content can be summarized, but cannot authorize wallet behavior. |
| `REVIEW` | `request_human_review` | Content is wallet-sensitive or suspicious enough to require review. |
| `FAIL` | `refuse_wallet_action` | Content contains high-risk prompt-injection patterns. |

## Safety Invariant

Across all current Phase 2 cases:

```text
wallet_action_allowed = false
```

This is intentional.

The agent is only reviewing external content.

External content cannot authorize token approvals, transaction building, signing, or wallet recommendations.

## Run Against Malicious Fixture

```powershell
python .\agents\toy_wallet_agent.py `
  --user-request "Review this external wallet-safety content and tell me whether it should influence wallet behavior." `
  --fixture .\tests\fixtures\agent_wallet_injection_001.txt `
  --out .\results\prompt-injection\toy_agent_malicious_decision_001.json
```

Expected action:

```text
refuse_wallet_action
```

## Run Against Ambiguous Fixture

```powershell
python .\agents\toy_wallet_agent.py `
  --user-request "Review this external wallet-safety content and tell me whether it should influence wallet behavior." `
  --fixture .\tests\fixtures\agent_wallet_ambiguous_001.txt `
  --out .\results\prompt-injection\toy_agent_ambiguous_decision_001.json
```

Expected action:

```text
request_human_review
```

## Run Against Benign Fixture

```powershell
python .\agents\toy_wallet_agent.py `
  --user-request "Review this external wallet-safety content and tell me whether it should influence wallet behavior." `
  --fixture .\tests\fixtures\agent_wallet_benign_001.txt `
  --out .\results\prompt-injection\toy_agent_benign_decision_001.json
```

Expected action:

```text
summarize_safely
```

## Run Behavior Tests

```powershell
python -m unittest tests\test_toy_wallet_agent.py
```

Expected result:

```text
Ran 3 tests

OK
```

## Run Full Current Test Set

```powershell
python -m unittest tests\test_prompt_injection_tester.py tests\test_toy_wallet_agent.py
```

Expected result:

```text
Ran 6 tests

OK
```

## JSON Output Fields

Important fields in the decision output:

| Field | Meaning |
|---|---|
| `content_classification` | PASS / REVIEW / FAIL result from the Phase 1 analyzer. |
| `risk_score` | Score produced by the analyzer based on matched rules. |
| `wallet_action_allowed` | Whether the toy agent allows wallet behavior. Currently always false. |
| `requires_user_confirmation` | Whether explicit user confirmation is required. Currently true. |
| `agent_boundary` | Security principle: external content is data, not authority. |
| `recommended_action` | Safe behavior selected by the toy agent. |
| `safety_reason` | Plain-English reason for the decision. |

## Security Interpretation

This section summarizes the security rationale for the simulator:

> Phase 2 adds a deterministic toy wallet-agent simulator. It imports the Phase 1 prompt-injection analyzer, classifies untrusted external content, and maps the result to safe behavior. Malicious content causes refusal, ambiguous wallet-related content triggers human review, and benign content can be summarized safely. In all cases, wallet action remains disallowed because external content cannot authorize wallet behavior.

## Current Limitation

This simulator does not test real model behavior.

It defines the expected safety policy before adding an LLM or simulated transaction layer.

That is deliberate: the safe behavior baseline should be explicit before model variability is introduced.


## Related Policy

- [Wallet Agent Safety Policy](../policies/wallet-agent-safety-policy.md)
