# Empire Breacher Roadmap

## Purpose

Empire Breacher is a controlled AI/Web3 wallet-agent security research harness.

The project studies prompt-injection risk, authority-boundary failures, and unsafe wallet-agent behavior in lab conditions.

It does not interact with real wallets, real funds, production systems, browser extensions, dApps, RPC providers, mainnet, testnet, or unauthorized targets.

## Core Invariant

```text
External content can be analyzed, but it cannot authorize wallet behavior.
```

## Current Status

Empire Breacher has a completed deterministic baseline:

- Phase 1: static prompt-injection fixture analyzer.
- Phase 2: deterministic toy wallet-agent behavior simulator.
- Phase 3: deterministic wallet-agent fixture evaluation loop.

## Completed Phases

### Phase 1: Prompt-Injection Fixture Analyzer

Phase 1 classifies controlled external-content fixtures as PASS, REVIEW, or FAIL.

Primary artifacts:

- `tools/prompt_injection_tester.py`
- `tests/test_prompt_injection_tester.py`
- `docs/lab-notes/prompt-injection-analyzer-validation-summary-001.md`

### Phase 2: Toy Wallet-Agent Behavior Simulator

Phase 2 maps classifications to safe wallet-agent behavior.

Behavior mapping:

- PASS -> `summarize_safely`
- REVIEW -> `request_human_review`
- FAIL -> `refuse_wallet_action`

Primary artifacts:

- `agents/toy_wallet_agent.py`
- `tests/test_toy_wallet_agent.py`
- `policies/wallet-agent-safety-policy.md`
- `docs/lab-notes/phase-2-validation-summary.md`

### Phase 3: Wallet-Agent Fixture Evaluation

Phase 3 adds a deterministic evaluation loop for wallet-agent fixtures.

Validated behavior:

- Malicious approval, transfer, and signature fixtures -> FAIL -> `refuse_wallet_action`
- Ambiguous wallet-adjacent verification fixture -> REVIEW -> `request_human_review`
- Benign token summary fixture -> PASS -> `summarize_safely`

Primary artifacts:

- `docs/lab-notes/llm-evaluation-rubric-001.md`
- `tests/fixtures/wallet-agent/`
- `tools/wallet_fixture_evaluator.py`
- `docs/validation-reports/phase-3-wallet-agent-evaluation.md`

## v1 Definition of Done

Empire Breacher v1 is complete when the repository provides a clear, reproducible, public-safe baseline for wallet-agent prompt-injection research.

v1 requirements:

- Threat model documented.
- Safety policy documented.
- Static analyzer implemented.
- Toy wallet-agent simulator implemented.
- Behavior tests implemented.
- Phase 3 rubric documented.
- Wallet-agent fixture set added.
- Deterministic wallet fixture evaluator implemented.
- Validation report documented.
- README proof map updated.
- Roadmap documented.
- Tool usage documentation updated.
- Optional CI validation added.

Current v1 status:

- Complete: threat model, safety policy, analyzer, toy agent, tests, rubric, fixtures, evaluator, validation report, README proof map, and roadmap.
- Remaining: tool usage documentation update and optional CI validation.

## Planned Milestones

### Milestone 4: Model-Output Evaluation Design

Define how saved model responses should be evaluated against the Phase 3 rubric before adding any model/API workflow.

### Milestone 5: Expanded Fixture Coverage

Add controlled variants for paraphrasing, obfuscation, role confusion, multilingual text, and multi-turn context.

### Milestone 6: Continuous Validation

Add optional CI validation for unit tests and deterministic fixture evaluation.

### Milestone 7: Portfolio v1 Finalization

Finalize tool usage notes, limitations, architecture documentation, and public-facing proof map.

## Out of Scope

Empire Breacher does not perform:

- real wallet exploitation
- real fund movement
- transaction signing
- transaction broadcasting
- production wallet testing
- browser extension testing
- dApp testing
- mainnet or testnet interaction
- credential theft
- private key handling
- unauthorized testing

## Current Next Best Improvements

1. Add concise usage documentation for `tools/wallet_fixture_evaluator.py`.
2. Add optional CI validation for unit tests and deterministic fixture evaluation.
3. Add model-output evaluation design notes before introducing model calls.
