# CryptoSHIELD Threat Registry: Human-Readable Table

**CSI CryptoSHIELD Framework v1.1**
Source of truth: [registry.json](registry.json) | Scoring methodology: [ctrs-scoring.md](ctrs-scoring.md)

This table is the human-readable view of `registry.json`. It renders in the GitHub UI without tooling. For machine-readable ingestion (SIEM, analytics, automation), use the JSON registry directly.

---

## Complete Threat Registry: 42 Entries

| Threat ID | Name | Category | CTRS | Severity | Trend | AI-Assisted | Insider Vector | False Flag Prob |
|---|---|---|---|---|---|---|---|---|
| CS-PHY-01 | Kidnapping and Physical Coercion | Physical | 15.0 | HIGH | Rising +75% YoY | No | Possible | 0.10 |
| CS-PHY-02 | Home Invasion / Targeted Robbery | Physical | 15.0 | HIGH | Rising | No | No | 0.05 |
| CS-INS-01 | Admin Key Abuse by Trusted Actor | Insider | 17.0 | CRITICAL | Stable (endemic) | Possible | Yes | 0.75 |
| CS-INS-02 | CEX Support Team Bribery | Insider | 14.5 | HIGH | Rising | No | Yes | 0.30 |
| CS-INS-03 | DPRK Wagemole Identity Infiltration | Insider | 17.0 | CRITICAL | Rising | Yes | Yes | 0.65 |
| CS-SOC-01 | Phishing (AI-Enhanced) | Social Engineering | 16.0 | CRITICAL | Rising +1400% AI component | Yes | No | 0.10 |
| CS-SOC-02 | Fake Hardware Wallet Supply | Social Engineering | 15.5 | HIGH | Stable | No | No | 0.05 |
| CS-SOC-03 | Fake Job Offer / Malware Delivery | Social Engineering | 15.5 | HIGH | Rising (DPRK primary) | Yes | Possible | 0.55 |
| CS-SOC-04 | Fake Meeting Application (Meeten) | Social Engineering | 15.5 | HIGH | Rising | Yes | No | 0.15 |
| CS-SOC-05 | AI Deepfake CFO Impersonation | Social Engineering | 15.5 | HIGH | Rising rapidly | Yes | Possible | 0.25 |
| CS-SOC-06 | Forced Labor Compound Operations | Social Engineering | 20.0 | CRITICAL | Rising | Yes | No | 0.10 |
| CS-SOC-07 | Typosquatting / Domain Impersonation | Social Engineering | 15.0 | HIGH | Stable | Partial | No | 0.05 |
| CS-MAL-01 | Clipboard Hijacking | Malware | 16.0 | CRITICAL | Stable | No | No | 0.05 |
| CS-MAL-02 | InfoStealer / Remote Access Trojan | Malware | 17.5 | CRITICAL | Rising (DPRK primary) | Yes | Possible | 0.45 |
| CS-MAL-03 | Fake Cloudflare / Drive-By PowerShell | Malware | 15.5 | HIGH | Rising | Yes | No | 0.10 |
| CS-WAL-01 | Seed Phrase Theft / Extraction | Wallet | 16.0 | CRITICAL | Stable | Partial | Possible | 0.15 |
| CS-WAL-02 | Address Poisoning | Wallet | 16.5 | CRITICAL | Rising | Partial | No | 0.05 |
| CS-WAL-03 | DNS Hijack / Frontend Compromise | Wallet | 17.0 | CRITICAL | Stable | No | Possible | 0.25 |
| CS-WAL-04 | Malicious Signature (Permit2 / ERC-20) | Wallet | 19.0 | CRITICAL | Rising | Yes | No | 0.10 |
| CS-WAL-05 | Low Entropy Seed Generation | Wallet | 14.5 | HIGH | Declining (tooling improving) | No | No | 0.05 |
| CS-DFI-01 | Admin Key Exploit | DeFi Protocol | 16.5 | CRITICAL | Stable | Partial | Yes | 0.60 |
| CS-DFI-02 | Flash Loan Attack | DeFi Protocol | 14.5 | HIGH | Declining (oracle hardening) | Partial | No | 0.10 |
| CS-DFI-03 | Bridge Exploit | DeFi Protocol | 17.5 | CRITICAL | Rising (new bridges) | Partial | Possible | 0.35 |
| CS-DFI-04 | Oracle Manipulation | DeFi Protocol | 14.5 | HIGH | Stable | Partial | No | 0.15 |
| CS-DFI-05 | Reentrancy | DeFi Protocol | 11.5 | ELEVATED | Declining | No | No | 0.05 |
| CS-SC-01 | NPM Package Hijacking | Supply Chain | 19.0 | CRITICAL | Rising | Yes | Possible | 0.30 |
| CS-SC-02 | SDK / Library Poisoning | Supply Chain | 18.0 | CRITICAL | Rising | Yes | Possible | 0.35 |
| CS-SC-03 | CI/CD Pipeline Compromise | Supply Chain | 18.0 | CRITICAL | Rising | Yes | Possible | 0.40 |
| CS-SC-04 | AI Model Backdoor | Supply Chain | 17.5 | CRITICAL | Emerging (new vector) | Yes | Possible | 0.40 |
| CS-AI-01 | Memory Poisoning (Agent Vector DB) | AI Agent | 17.5 | CRITICAL | Emerging | Yes | No | 0.20 |
| CS-AI-02 | Prompt Injection (Agent Logic Override) | AI Agent | 18.0 | CRITICAL | Emerging | Yes | No | 0.15 |
| CS-AI-03 | Data Chain Poisoning (Training/Context) | AI Agent | 15.0 | HIGH | Emerging | Yes | Possible | 0.25 |
| CS-AI-04 | AI Swarm Coordinated Attack | AI Agent | 17.5 | CRITICAL | Emerging | Yes | No | 0.20 |
| CS-AI-05 | Synthetic Identity / Document Fraud | AI Agent | 15.5 | HIGH | Rising rapidly | Yes | No | 0.25 |
| CS-MKT-01 | MEV / Sandwich Attack | Market Manipulation | 15.5 | HIGH | Stable (structural) | Partial | No | 0.05 |
| CS-MKT-02 | Tokenomics Weaponization (Rotator Effect) | Market Manipulation | 17.5 | CRITICAL | Rising with AI | Yes | Yes | 0.55 |
| CS-MKT-03 | Influence Operation / FUD Campaign | Market Manipulation | 13.5 | HIGH | Rising with AI | Yes | Possible | 0.45 |
| CS-SOV-01 | CBDC Surveillance Architecture | Sovereignty | 15.5 | HIGH | Political (dormant in US 2025-26) | No | No | 0.05 |
| CS-SOV-02 | CEX KYC Overreach / Data Breach | Sovereignty | 12.0 | ELEVATED | Rising (Coinbase 2025 incident) | No | Yes | 0.10 |
| CS-FRD-01 | Pig Butchering / Financial Grooming | Financial Fraud | 20.0 | CRITICAL | Rising +50% YoY | Yes | No | 0.05 |
| CS-FRD-02 | Recovery Re-Victimization Scam | Financial Fraud | 15.5 | HIGH | Rising | Yes | No | 0.05 |
| CS-FRD-03 | Bitcoin ATM / QR Code Coercion | Financial Fraud | 15.0 | HIGH | Rising (senior targeting) | Partial | No | 0.05 |
| CS-FRD-04 | Investment Group / Fake Alpha Scam | Financial Fraud | 15.5 | HIGH | Rising | Yes | No | 0.05 |
| CS-EXT-01 | Sextortion / Blackmail / Ransomware | Extortion | 15.0 | HIGH | Stable | Partial | No | 0.05 |

---

## Quick Reference: CTRS Critical Threats (Score 17.0+)

| CTRS | Threat ID | Name | Primary Control |
|---|---|---|---|
| 20.0 | CS-FRD-01 | Pig Butchering | SMS-14 (Fee Demand Stop) |
| 20.0 | CS-SOC-06 | Forced Labor Compounds | CFD-01 (Platform Verification) |
| 19.0 | CS-WAL-04 | Malicious Signature | WKS-08 (Never sign unsolicited) |
| 19.0 | CS-SC-01 | NPM Package Hijacking | SCD-07 (Lock pinning) |
| 18.0 | CS-SC-02 | SDK/Library Poisoning | SCD-01 (SBOM) |
| 18.0 | CS-SC-03 | CI/CD Compromise | SCD-03 (Secret isolation) |
| 18.0 | CS-AI-02 | Prompt Injection | AAS-03 (Immutable instructions) |
| 17.5 | CS-MAL-02 | InfoStealer/RAT | EDD-01 (Kernel default-deny) |
| 17.5 | CS-DFI-03 | Bridge Exploit | OCM-07 (Bridge risk matrix) |
| 17.5 | CS-SC-04 | AI Model Backdoor | SCD-08 (Model provenance) |
| 17.5 | CS-AI-01 | Memory Poisoning | AAS-02 (Memory integrity) |
| 17.5 | CS-AI-04 | AI Swarm Attack | AAS-10 (Swarm isolation) |
| 17.5 | CS-MKT-02 | Tokenomics Weaponization | SMS-10 (Rotator Effect analysis) |
| 17.0 | CS-INS-01 | Admin Key Abuse | WKS-02 + WKS-03 (Multisig + Timelock) |
| 17.0 | CS-INS-03 | DPRK Wagemole | Personnel vetting + WKS-02 |
| 17.0 | CS-WAL-03 | DNS/Frontend Hijack | SMS-05 + SMS-11 (URL verification) |

---

## Column Definitions

| Column | Definition |
|---|---|
| CTRS | Crypto Threat Risk Score (0-20). Formula: `(L×0.25 + I×0.30 + R×0.20 + D×0.15 + RecD×0.10) × 20` |
| Trend | Observed trajectory of this threat category in 2024-2026 |
| AI-Assisted | Whether AI tools are meaningfully used to scale, personalize, or enhance this attack |
| Insider Vector | Whether insider access is required or significantly increases probability |
| False Flag Prob | Probability that official attribution post-incident does not reflect primary responsible actor (0.0-1.0) |

Full methodology: [ctrs-scoring.md](ctrs-scoring.md) | Full architecture: [threat-architecture.md](threat-architecture.md)

---

*Threat Registry Table | CSI CryptoSHIELD Framework v1.1 | Auto-generated from registry.json*
*Cyber Strategy Institute | Open-Source | Sovereignty-First*
