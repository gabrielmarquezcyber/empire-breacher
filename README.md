# Empire Breacher

Empire Breacher is a controlled AI/Web3 security research harness for studying wallet-agent prompt-injection risk, authority-boundary failures, and unsafe wallet behavior in lab conditions.

The project focuses on one core security principle:

```text
External content can be analyzed, but it cannot authorize wallet behavior.
```

All testing is performed with local fixtures, deterministic tools, toy simulators, and documented expected behavior.

This repository does not interact with real wallets, real funds, production systems, mainnet, testnet, dApps, browser extensions, RPC providers, or unauthorized targets.

## Reviewer Proof Map

This repository is designed to be reviewed quickly. Start here:

| Proof Area | What It Shows | Start Here |
|---|---|---|
| Safety Boundary | External content can be analyzed, but it cannot authorize wallet behavior. | [Wallet-agent safety policy](policies/wallet-agent-safety-policy.md), [Phase 2 validation summary](docs/lab-notes/phase-2-validation-summary.md) |
| Prompt-Injection Detection | Hostile, benign, and ambiguous wallet-agent content can be classified with deterministic fixture analysis. | [Prompt-injection tester](tools/prompt_injection_tester.py), [Phase 1 validation summary](docs/lab-notes/prompt-injection-analyzer-validation-summary-001.md) |
| Wallet-Agent Behavior | PASS / REVIEW / FAIL classifications map to safe wallet-agent behavior. | [Toy wallet agent](agents/toy_wallet_agent.py), [PASS / REVIEW / FAIL examples](docs/lab-notes/pass-review-fail-examples-001.md) |
| Fixture Evaluation | Controlled wallet-agent fixtures are evaluated against expected safe, review, and refusal outcomes. | [Wallet fixture evaluator](tools/wallet_fixture_evaluator.py), [Phase 3 validation report](docs/validation-reports/phase-3-wallet-agent-evaluation.md) |
| Threat Framework Mapping | Wallet-agent risks are mapped to OWASP LLM Top 10, MITRE ATLAS concepts, and detection ideas. | [Threat framework and detection mapping](docs/lab-notes/threat-framework-detection-mapping-001.md) |
| Project Roadmap | The repo has a v1 definition of done, milestones, and out-of-scope boundaries. | [Roadmap](docs/ROADMAP.md) |

## What This Proves

Empire Breacher demonstrates practical security reasoning for AI-assisted wallet workflows:

- Untrusted external content is treated as data, not authority.
- Wallet behavior is constrained by explicit safety policy.
- Malicious, ambiguous, and benign fixtures are separated into PASS, REVIEW, and FAIL outcomes.
- Unsafe wallet-related content maps to refusal behavior.
- Ambiguous wallet-adjacent content maps to human review.
- The project connects AI-agent risk to defensive detection and monitoring concepts.
- The repository is intentionally local, deterministic, and public-safe.


## Current Status

```text
Phase 1: Complete - static prompt-injection fixture analyzer
Phase 2: Complete - deterministic toy wallet-agent behavior simulator
Phase 3: Complete - deterministic wallet-agent fixture evaluation
Phase 4: Complete - threat framework and detection mapping
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
| [`tools/prompt_injection_tester.py`](tools/prompt_injection_tester.py) | Deterministic analyzer for prompt-injection fixture patterns. |
| [`tests/fixtures/agent_wallet_injection_001.txt`](tests/fixtures/agent_wallet_injection_001.txt) | Malicious wallet-agent prompt-injection fixture. |
| [`tests/fixtures/agent_wallet_ambiguous_001.txt`](tests/fixtures/agent_wallet_ambiguous_001.txt) | Ambiguous wallet-related fixture requiring review. |
| [`tests/fixtures/agent_wallet_benign_001.txt`](tests/fixtures/agent_wallet_benign_001.txt) | Benign wallet-safety fixture. |
| [`tests/test_prompt_injection_tester.py`](tests/test_prompt_injection_tester.py) | Regression tests for analyzer classifications. |
| [`results/prompt-injection/`](results/prompt-injection/) | Generated analyzer result reports. |
| [`docs/lab-notes/prompt-injection-analyzer-validation-summary-001.md`](docs/lab-notes/prompt-injection-analyzer-validation-summary-001.md) | Phase 1 validation summary. |

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
| [`agents/toy_wallet_agent.py`](agents/toy_wallet_agent.py) | Deterministic toy wallet-agent simulator. |
| [`tests/test_toy_wallet_agent.py`](tests/test_toy_wallet_agent.py) | Behavior regression tests for toy-agent decisions. |
| [`agents/README.md`](agents/README.md) | Usage documentation for the toy wallet agent. |
| [`policies/wallet-agent-safety-policy.md`](policies/wallet-agent-safety-policy.md) | Safety policy governing wallet-agent behavior. |
| [`docs/lab-notes/pass-review-fail-examples-001.md`](docs/lab-notes/pass-review-fail-examples-001.md) | PASS / REVIEW / FAIL examples and security interpretation. |
| [`docs/lab-notes/toy-wallet-agent-behavior-001.md`](docs/lab-notes/toy-wallet-agent-behavior-001.md) | Phase 2 behavior report. |
| [`docs/lab-notes/phase-2-validation-summary.md`](docs/lab-notes/phase-2-validation-summary.md) | Phase 2 validation summary. |

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

## Phase 3 Proof Map

Phase 3 added a deterministic wallet-agent fixture evaluation loop.

### Phase 3 Research Question

```text
Can controlled wallet-agent fixtures be evaluated against a rubric to confirm expected safe, review, and refusal behavior?
```

### Phase 3 Artifacts

- [`docs/lab-notes/llm-evaluation-rubric-001.md`](docs/lab-notes/llm-evaluation-rubric-001.md) defines PASS, REVIEW, and FAIL criteria for wallet-agent evaluation.
- [`tests/fixtures/wallet-agent/`](tests/fixtures/wallet-agent/) contains controlled malicious, benign, and ambiguous wallet-agent fixtures.
- [`tools/wallet_fixture_evaluator.py`](tools/wallet_fixture_evaluator.py) evaluates Phase 3 wallet-agent fixtures deterministically.
- [`docs/validation-reports/phase-3-wallet-agent-evaluation.md`](docs/validation-reports/phase-3-wallet-agent-evaluation.md) documents the Phase 3 evaluation results.

### Phase 3 Validated Behavior

- Malicious approval, transfer, and signature fixtures are expected to produce `FAIL` and map to `refuse_wallet_action`.
- Ambiguous wallet-adjacent verification content is expected to produce `REVIEW` and map to `request_human_review`.
- Benign token summary content is expected to produce `PASS` and map to `summarize_safely`.

Phase 3 preserves the same core invariant:

```text
wallet_action_allowed = false
```


## Phase 4 Proof Map

Phase 4 added threat-framework and detection mapping for wallet-agent safety behavior.

### Phase 4 Research Question

How can wallet-agent prompt-injection and unsafe tool-use risks be mapped to public AI security frameworks and practical detection ideas?

### Phase 4 Artifacts

- [Threat framework and detection mapping](docs/lab-notes/threat-framework-detection-mapping-001.md)
- [Lab notes index](docs/lab-notes/README.md)
- [Project roadmap](docs/ROADMAP.md)

### Phase 4 Validated Value

- Maps wallet-agent risk to OWASP LLM Top 10 concepts.
- Maps agent behavior patterns to MITRE ATLAS-style security reasoning.
- Defines detection and monitoring ideas for unsafe agent behavior.
- Connects the project to employer-relevant AI security, AppSec, detection engineering, and product-security discussions.


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
| [`docs/lab-notes/README.md`](docs/lab-notes/README.md) | Index of research notes and validation summaries. |
| [`docs/ROADMAP.md`](docs/ROADMAP.md) | Current phase status, v1 definition of done, planned milestones, and out-of-scope boundaries. |
| [`tools/README.md`](tools/README.md) | Prompt-injection analyzer usage. |
| [`agents/README.md`](agents/README.md) | Toy wallet-agent simulator usage. |
| [`policies/wallet-agent-safety-policy.md`](policies/wallet-agent-safety-policy.md) | Safety policy for wallet-agent behavior. |

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


## Safety Boundary

This repository is for controlled security research, defensive validation, and portfolio-grade documentation.

It is not a tool for unauthorized testing, real-wallet exploitation, transaction manipulation, credential theft, persistence, evasion, or harm.
