# Domain 07: AI Agent and Autonomous System Security (AAS)

**CSI CryptoSHIELD Framework v1.1 | May 2026**

---

## Scope and Companion Framework Reference

This domain provides **crypto-specific AI agent security controls** for DeFi environments. It covers the immediate, wallet-facing risks of AI agents transacting on-chain.

**Full agentic AI governance is maintained by [AI SAFE² v3.0](https://github.com/CyberStrategyInstitute/ai-safe2-framework).** When deploying a DeFi AI agent beyond the controls in this domain, navigate to AI SAFE² as follows:

| Your Governance Need | AI SAFE² Destination |
|---|---|
| Classify what your agent is allowed to do autonomously | **ACT Capability Tiers (1-4)**: determines which governance requirements apply |
| Harden agent inputs against poisoned data | **Pillar 1: Sanitize and Isolate (S)**: input validation, context boundary enforcement |
| Secure your MCP server integration | **CP.5.MCP**: STDIO transport security, bearer token auth, supply chain attestation |
| Ensure a human can always override / kill-switch | **CP.10: HEAR Doctrine**: cryptographically enforced Human Ethical Agent of Record |
| Prevent agent self-replication or unauthorized spawning | **CP.9: Agent Replication Governance**: first-in-field control for this threat class |
| Map controls to ISO 42001, NIST AI RMF, EU AI Act | **Compliance Crosswalk**: 32-framework mapping in the AI SAFE² appendix |
| Govern Non-Human Identity (NHI) lifecycle | **Pillar 2: Audit and Inventory (A)**: NHI enumeration, access control, deprovisioning |

If your DeFi agent is ACT-3 or ACT-4 (material autonomous financial decisions or swarm coordination), the HEAR Doctrine (CP.10) is mandatory: not optional. An agent that can drain a wallet must have a cryptographically enforced human override that cannot be social-engineered away. CryptoSHIELD AAS controls alone are insufficient at that capability tier.

**Full agentic AI governance covers:**

- ACT Capability Tier classification (ACT-1 through ACT-4)
- CP.10: HEAR Doctrine (Human Ethical Agent of Record: cryptographically enforced fail-closed)
- CP.9: Agent Replication Governance (first-in-field control for agent self-replication scenarios)
- 151 pillar controls across five operational pillars
- 10 cross-pillar governance controls (CP.1-CP.10)
- OWASP AIVSS v0.8 AAF composite risk scoring
- NEXUS-A2A protocol governance
- Non-Human Identity (NHI) full lifecycle management
- 32-framework compliance mapping including ISO 42001, NIST AI RMF, EU AI Act

---

## Current Threat Context (2026)

By Q1 2026, AI agent wallets represented 8-12% of EVM DeFi transaction volume. This is not a future risk. It is the current attack surface.

**Confirmed operational threats:**
- **Memory poisoning**: Vector database injection creating sleeper agents (CS-AI-01)
- **Prompt injection / logic redefinition**: Freysa exploit: hardcoded "never transfer funds" directive overridden by redefining function logic (CS-AI-02)
- **Data chain poisoning**: GitHub documentation poisoned causing AI coding agent to generate private key-stealing code (CS-AI-03)
- **AI swarm attacks**: GTG-1002 (November 2025): 30 organizations simultaneously, 80-90% human-out-of-loop (CS-AI-04)
- **ClawJacked class**: Remote takeover of self-hosted trading agents via WebSocket vulnerabilities
- **Step Finance ($40M, January 2026)**: Device compromise + AI trading agent amplification

---

## Controls

| Control ID | Control | Priority |
|-----------|---------|---------|
| AAS-01 | Keyless agent architecture: AI agents never hold private keys; authenticated signing only | CRITICAL |
| AAS-02 | Memory integrity monitoring: regular hash verification of vector database contents | CRITICAL |
| AAS-03 | Prompt injection hardening: immutable core instructions; multi-layer validation | CRITICAL |
| AAS-04 | Agent wallet isolation: minimal-balance dedicated wallets per strategy | HIGH |
| AAS-05 | Testnet simulation first: no mainnet deployment without sandbox validation | HIGH |
| AAS-06 | Hard transaction rate limits per time window | CRITICAL |
| AAS-07 | Real-time agent behavior anomaly detection | HIGH |
| AAS-08 | Tool call allowlisting: permitted smart contracts and endpoints only | CRITICAL |
| AAS-09 | Oracle diversity: minimum three independent sources | HIGH |
| AAS-10 | Swarm isolation: no shared memory between swarm agent instances | HIGH |

Full control specifications and AI SAFE² cross-references: [FRAMEWORK-ALIGNMENT.md](../FRAMEWORK-ALIGNMENT.md)

---

*Domain 07: AI Agent and Autonomous System Security | CryptoSHIELD v1.1*
*Full agentic governance: [AI SAFE² v3.0](https://github.com/CyberStrategyInstitute/ai-safe2-framework)*
