# Empire Breacher Tools

This folder contains local utilities used to test, document, and validate AI-agent security behaviors in controlled lab environments.

## Prompt Injection Tester

Path:

```text
tools/prompt_injection_tester.py
```

Purpose:

```text
Deterministically scan prompt-injection fixtures for unsafe authority-boundary, wallet-action, and deception patterns.
```

This tool does not call external APIs, models, wallets, or networks.

## Run Against Malicious Wallet Fixture

```powershell
python .\tools\prompt_injection_tester.py `
  --fixture .\tests\fixtures\agent_wallet_injection_001.txt `
  --out .\results\prompt-injection\agent_wallet_injection_001_result.md
```

Expected classification:

```text
FAIL - HIGH RISK PROMPT INJECTION
```

## Run Against Benign Wallet Fixture

```powershell
python .\tools\prompt_injection_tester.py `
  --fixture .\tests\fixtures\agent_wallet_benign_001.txt `
  --out .\results\prompt-injection\agent_wallet_benign_001_result.md
```

Expected classification:

```text
PASS - NO HIGH-RISK INJECTION PATTERN DETECTED
```

## Run Regression Tests

```powershell
python -m unittest tests\test_prompt_injection_tester.py
```

Expected result:

```text
Ran 2 tests

OK
```

## Current Detection Categories

- `AUTHORITY_OVERRIDE`
- `HIDE_RISK_FROM_USER`
- `FALSE_USER_APPROVAL`
- `UNSAFE_WALLET_APPROVAL`
- `MISLEADING_SAFETY_CLAIM`
- `TRANSACTION_CONTEXT`
- `UNTRUSTED_CONTENT_MARKER`

## Current Control Pair

```text
agent_wallet_injection_001.txt -> FAIL
agent_wallet_benign_001.txt -> PASS
```

## Limitation

This is a deterministic fixture scanner. It does not prove how a specific LLM or production agent will behave. It identifies high-risk fixture content for controlled agent-behavior testing.

## Phase 1 Validation Set

```text
agent_wallet_benign_001.txt -> PASS
agent_wallet_ambiguous_001.txt -> REVIEW
agent_wallet_injection_001.txt -> FAIL
```
