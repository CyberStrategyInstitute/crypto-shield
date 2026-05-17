# Research Note 004: AI Agent Attack Surface in DeFi

**Classification:** Open-Source Intelligence | CSI CryptoSHIELD Framework
**Status:** FORTHCOMING: Track progress at GitHub Issue #004
**Date:** Expected Q3 2026 | **Version:** Stub 0.1
**Threat IDs:** CS-AI-01, CS-AI-02, CS-AI-03, CS-AI-04, CS-AI-05
**Domain:** 07: AI Agent and Autonomous System Security

---

## Scope (Planned)

This research note will provide full-depth analysis of the AI agent attack surface in DeFi environments, including:

- Complete attack surface mapping for AI agents holding or managing crypto assets
- Case study analysis: Step Finance ($40M, January 2026), ClawJacked vulnerability class, Freysa exploit
- Memory poisoning attack methodology and detection indicators
- Prompt injection kill chains for DeFi-connected agents
- AI swarm attack architecture: GTG-1002 campaign anatomy (November 2025)
- Agent wallet architecture recommendations with code examples
- Integration with AI SAFE² v3.0 ACT Capability Tier framework

## Why This Note Matters

By Q1 2026, AI agent wallets represented 8-12% of EVM DeFi transaction volume. The attack surface did not exist at meaningful scale eighteen months ago. The threat models, attack patterns, and governance gaps are all actively being discovered in production: not in academic research. This note will document what is known from real incidents and extrapolate the emerging threat landscape.

## Key Questions This Note Will Answer

1. What percentage of major DeFi losses in 2025-2026 involved an AI agent as a contributing factor?
2. What is the definitive taxonomy of prompt injection attack classes against DeFi agents?
3. How does Freysa-class logic redefinition work and how is it defended?
4. What does a safe keyless agent architecture look like in production?
5. Where does CryptoSHIELD Domain 07 end and AI SAFE² begin for agents at different ACT tiers?

---

## Interim Guidance

Until this research note is published, see:

- [Domain 07: AI Agent Security](../07-ai-agent-security/README.md): current control set
- [AI SAFE² Framework v3.0](https://github.com/CyberStrategyInstitute/ai-safe2-framework): full agentic AI governance
- [taxonomy/registry-table.md](../taxonomy/registry-table.md): CS-AI-01 through CS-AI-05 entries

**To contribute to this research note:** Open an issue with the label `research-004` and provide documented incident analysis, technical findings, or peer-reviewed sources.

---

*Research Note 004 Stub | CSI CryptoSHIELD Framework v1.1*
*Cyber Strategy Institute | Open-Source | Expected Q3 2026*
