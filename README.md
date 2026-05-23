# Empire Breacher

Empire Breacher is a controlled AI/Web3 security research harness for studying wallet-agent prompt-injection risk, authority-boundary failures, and unsafe wallet behavior in lab conditions.

The project focuses on one core security principle:

```text
External content can be analyzed, but it cannot authorize wallet behavior.
```

All testing is performed with local fixtures, deterministic tools, toy simulators, and documented expected behavior.

This repository does not interact with real wallets, real funds, production systems, mainnet, testnet, dApps, browser extensions, RPC providers, or unauthorized targets.

## Current Status

```text
Phase 1: Complete - static prompt-injection fixture analyzer
Phase 2: Complete - deterministic toy wallet-agent behavior simulator
Phase 3: Planned  - LLM-backed evaluation harness
```

## Research Focus

Empire Breacher models a specific AI-agent security problem:

```text
Can untrusted external content manipulate a wallet-enabled agent into unsafe wallet behavior?
```

Examples of unsafe wallet behavior include:

- Treating external content as trusted instruction authority.
- Recommending unsafe token approvals.
- Normalizing unlimited approvals.
- Accepting forged user consent from external content.
- Suppressing warnings to the user.
- Allowing content classification to become transaction authorization.

## Architecture Overview

```text
untrusted external content fixture
-> prompt-injection analyzer
-> PASS / REVIEW / FAIL classification
-> toy wallet-agent behavior decision
-> JSON result output and validation report
```

## Phase 1 Proof Map

Phase 1 built a deterministic prompt-injection fixture analyzer.

### Phase 1 Research Question

```text
Can hostile, benign, and ambiguous wallet-agent external content be classified consistently?
```

### Phase 1 Artifacts

| Artifact | Purpose |
|---|---|
| `tools/prompt_injection_tester.py` | Deterministic analyzer for prompt-injection fixture patterns. |
| `tests/fixtures/agent_wallet_injection_001.txt` | Malicious wallet-agent prompt-injection fixture. |
| `tests/fixtures/agent_wallet_ambiguous_001.txt` | Ambiguous wallet-related fixture requiring review. |
| `tests/fixtures/agent_wallet_benign_001.txt` | Benign wallet-safety fixture. |
| `tests/test_prompt_injection_tester.py` | Regression tests for analyzer classifications. |
| `results/prompt-injection/` | Generated analyzer result reports. |
| `docs/lab-notes/prompt-injection-analyzer-validation-summary-001.md` | Phase 1 validation summary. |

### Phase 1 Validated Behavior

| Fixture Type | Expected Classification |
|---|---|
| Benign | `PASS - NO HIGH-RISK INJECTION PATTERN DETECTED` |
| Ambiguous | `REVIEW - POTENTIAL PROMPT INJECTION` |
| Malicious | `FAIL - HIGH RISK PROMPT INJECTION` |

The high-risk condition modeled in Phase 1 is:

```text
authority override + wallet action + deception
```

## Phase 2 Proof Map

Phase 2 added a deterministic toy wallet-agent behavior layer.

### Phase 2 Research Question

```text
Can a wallet-agent preserve authority boundaries when exposed to untrusted external content classified as PASS, REVIEW, or FAIL?
```

### Phase 2 Artifacts

| Artifact | Purpose |
|---|---|
| `agents/toy_wallet_agent.py` | Deterministic toy wallet-agent simulator. |
| `tests/test_toy_wallet_agent.py` | Behavior regression tests for toy-agent decisions. |
| `agents/README.md` | Usage documentation for the toy wallet agent. |
| `policies/wallet-agent-safety-policy.md` | Safety policy governing wallet-agent behavior. |
| `docs/lab-notes/pass-review-fail-examples-001.md` | PASS / REVIEW / FAIL examples and security interpretation. |
| `docs/lab-notes/toy-wallet-agent-behavior-001.md` | Phase 2 behavior report. |
| `docs/lab-notes/phase-2-validation-summary.md` | Phase 2 validation summary. |

### Phase 2 Validated Behavior

| Analyzer Result | Toy-Agent Action | Wallet Action Allowed |
|---|---|---:|
| `PASS` | `summarize_safely` | `false` |
| `REVIEW` | `request_human_review` | `false` |
| `FAIL` | `refuse_wallet_action` | `false` |

The Phase 2 safety invariant is:

```text
wallet_action_allowed = false
```

This invariant is intentional because the trusted user request only asks the agent to review external content. It does not authorize transaction building, signing, token approvals, spender selection, network selection, or wallet recommendations.

## Run Validation Tests

Run the full current test set:

```powershell
python -m unittest tests\test_prompt_injection_tester.py tests\test_toy_wallet_agent.py
```

Expected result:

```text
Ran 6 tests

OK
```

Validate toy-agent syntax:

```powershell
python -m py_compile .\agents\toy_wallet_agent.py
```

Expected result: no output.

## Documentation Map

| File | Description |
|---|---|
| `docs/lab-notes/README.md` | Index of research notes and validation summaries. |
| `tools/README.md` | Prompt-injection analyzer usage. |
| `agents/README.md` | Toy wallet-agent simulator usage. |
| `policies/wallet-agent-safety-policy.md` | Safety policy for wallet-agent behavior. |

## Design Rationale

The project separates content classification from behavior enforcement.

The analyzer determines whether external content appears benign, ambiguous, or hostile.

The toy wallet agent maps that classification to safe behavior.

This separation makes the authority boundary explicit and testable.

## Limitations

Empire Breacher currently does not:

- Use a real LLM.
- Connect to a wallet.
- Build, sign, simulate, or broadcast blockchain transactions.
- Interact with browser extensions, dApps, RPC providers, mainnet, or testnet.
- Prove any production system is vulnerable or safe.
- Detect every possible prompt-injection variant, paraphrase, encoding, language, or obfuscation.

Current results apply only to controlled local fixtures and deterministic toy simulations.

## Planned Next Phase

Phase 3 should introduce an LLM-backed evaluation harness.

The next research question is:

```text
Do real model outputs preserve the wallet-agent safety policy when exposed to hostile, ambiguous, and benign external content?
```

The next phase should define an evaluation rubric before introducing model calls.

## Safety Boundary

This repository is for controlled security research, defensive validation, and portfolio-grade documentation.

It is not a tool for unauthorized testing, real-wallet exploitation, transaction manipulation, credential theft, persistence, evasion, or harm.
