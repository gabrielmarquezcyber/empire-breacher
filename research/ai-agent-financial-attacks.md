# AI Agent Financial Attack Taxonomy

This document is the initial seed for a structured taxonomy of financial attacks against AI-agent–powered wallets, assistants, and automated transaction systems.

It will grow over time as the research expands.

---

## 🧩 Attack Class 1: Guardrail Over‑Enforcement / Business Logic Denial

**Description:**  
AI agents refuse to perform valid, authorized actions due to overly cautious, ambiguous, or incorrectly structured system prompts or safety rules.

**Symptoms:**  
- Legitimate transfers denied  
- Overreliance on shallow linguistic cues ("this is a test")  
- False positives for “malicious intent”  
- Agent loops asking for unnecessary reconfirmation  
- Blocking user operations without technical justification  

**Security Impact:**  
- Users locked out of their own funds  
- Denial-of-service on financial workflows  
- Inconsistent execution behavior  
- Creates a false sense of safety while still being exploitable elsewhere  

**Example Triggers:**  
- Phrases such as “test,” “similar,” “looks like,” etc.  
- Instructions referencing security concepts  
- Ambiguous multi‑step approvals  

---

## 🧩 Attack Class 2: Tool Misuse via Prompt Injection (Wallet Transfers)

**Description:**  
An attacker manipulates natural-language prompts to cause the AI agent to call a tool (e.g., `safe_transfer`) in a way that performs or attempts unauthorized financial actions.

**Mechanism:**  
- The agent *believes* the user is authorizing the transfer  
- Loopholes in system-level “approval rules”  
- Tool functions accept parameters without hard enforcement  
- Manipulated language used to create “pseudo‑approval”  

**Security Impact:**  
- Unauthorized testnet or mainnet transfers  
- Funds drained from user wallets  
- Signing of malicious transactions  
- Potential downstream smart contract triggers  

**Example Techniques:**  
- “I approve this transfer: …” phrasing  
- Reframing approval as confirmation  
- Using chain-of-thought bait  
- Slight wording changes to bypass safety heuristics  

---

## 📌 Upcoming Attack Classes (Placeholders)

These will be developed as the research expands:

### Attack Class 3: Semantic Authorization Collisions  
### Attack Class 4: Transaction Metadata Manipulation  
### Attack Class 5: Invisible Function Call Injection  
### Attack Class 6: Cross-Message Multi-Step Coercion  
### Attack Class 7: Goal Hijacking via Agent Memory Drift  
### Attack Class 8: Safety Rule Confusion Attacks  
### Attack Class 9: Delegated Tool Abuse by Multi-Agent Chains  

---

## 🧪 Notes  
This is an evolving document.  
Additional PoCs, reproduction steps, and dataset examples will be added as they are collected.

