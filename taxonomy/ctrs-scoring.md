# Crypto Threat Risk Score (CTRS): Scoring Methodology

**CSI CryptoSHIELD Framework v1.1**
Cyber Strategy Institute | Open-Source

---

## Overview

The Crypto Threat Risk Score (CTRS) is a weighted severity model for prioritizing threats in the CryptoSHIELD taxonomy. It enables consistent comparison across fundamentally different threat types: physical coercion, smart contract exploits, social engineering, AI agent attacks: by normalizing them to a single 0-20 scale.

The CTRS is modeled after the Cognitive Threat Severity Score (CTSS) used in the Cognitive Sovereignty Framework, adapted for the crypto-specific threat landscape.

---

## Formula

```
CTRS = (L × 0.25) + (I × 0.30) + (R × 0.20) + (D × 0.15) + (RecD × 0.10)

Where each component is scored 0-4 (max raw sum = 4.0)
Scale to 0-20 by multiplying by 5.
```

**Full formula with scaling:**
```
CTRS = [(L × 0.25) + (I × 0.30) + (R × 0.20) + (D × 0.15) + (RecD × 0.10)] × 20
Range: 0-20 | Critical ≥ 17 | High ≥ 13 | Elevated ≥ 9 | Low < 9
```

---

## Component Definitions

### Likelihood (L): Weight: 0.25
Probability that the threat will affect a crypto holder with moderate wealth and normal digital hygiene.

| Score | Definition |
|---|---|
| 0 | Theoretical; no documented cases at scale |
| 1 | Rare; fewer than 10 documented incidents per year globally |
| 2 | Occasional; 10-100 incidents per year globally |
| 3 | Common; hundreds of incidents per year; regular CSI reporting |
| 4 | Pervasive; thousands of incidents; systemic threat |

### Impact on Sovereignty (I): Weight: 0.30
Effect on the victim's financial sovereignty, safety, and ability to recover. Highest weight because sovereignty is the framework's primary value.

| Score | Definition |
|---|---|
| 0 | No meaningful impact |
| 1 | Minor financial loss (<$1,000); no safety impact |
| 2 | Moderate loss ($1,000-$50,000); recoverable |
| 3 | Major loss (>$50,000) or significant platform compromise |
| 4 | Catastrophic: total loss, physical harm, or permanent compromise |

### Reach / Scale (R): Weight: 0.20
How broadly the threat can affect populations beyond the individual target.

| Score | Definition |
|---|---|
| 0 | Targeted; affects only specific identified individual |
| 1 | Small group; protocol-level with limited user base |
| 2 | Sector-level; affects users of a category of platforms |
| 3 | Ecosystem-level; affects users of major infrastructure |
| 4 | Civilizational; affects financial system or regulatory framework |

### Detection Difficulty (D): Weight: 0.15
How difficult the attack is to detect before or during execution.

| Score | Definition |
|---|---|
| 0 | Easily detected; clear behavioral indicators |
| 1 | Detectable with standard monitoring |
| 2 | Requires specialized tools or knowledge to detect |
| 3 | Near-undetectable with current consumer tools |
| 4 | Undetectable without forensic analysis; AI-enhanced deception |

### Recovery Difficulty (RecD): Weight: 0.10
How difficult it is to reverse or recover from the impact.

| Score | Definition |
|---|---|
| 0 | Fully recoverable; no lasting harm |
| 1 | Recoverable with effort (technical remediation) |
| 2 | Partial recovery possible (some assets recoverable) |
| 3 | Largely unrecoverable (blockchain finality; physical harm) |
| 4 | Unrecoverable; permanent loss or harm |

---

## Threat Tier Classification

| CTRS Range | Tier | Response Priority |
|---|---|---|
| 17.0-20.0 | CRITICAL | Immediate controls required; no delay |
| 13.0-16.9 | HIGH | Controls required within 30 days |
| 9.0-12.9 | ELEVATED | Controls recommended; include in next review cycle |
| 0-8.9 | LOW | Monitor; address opportunistically |

---

## Scored Threat Registry (Full)

| Threat ID | Threat Name | L | I | R | D | RecD | CTRS | Tier |
|---|---|---|---|---|---|---|---|---|
| CS-PHY-01 | Kidnapping/Coercion | 2 | 4 | 2 | 3 | 4 | 15.0 | HIGH |
| CS-PHY-02 | Home Invasion | 2 | 4 | 2 | 3 | 4 | 15.0 | HIGH |
| CS-INS-01 | Admin Key Abuse | 2 | 4 | 3 | 4 | 4 | 17.0 | CRITICAL |
| CS-INS-02 | CEX Support Bribery | 2 | 3 | 3 | 4 | 3 | 14.5 | HIGH |
| CS-INS-03 | DPRK Wagemole | 2 | 4 | 3 | 4 | 4 | 17.0 | CRITICAL |
| CS-SOC-01 | Phishing | 4 | 3 | 3 | 3 | 3 | 16.0 | CRITICAL |
| CS-SOC-02 | Fake Hardware Wallet | 1 | 4 | 2 | 4 | 4 | 15.5 | HIGH |
| CS-SOC-03 | Fake Job Offer | 3 | 3 | 3 | 4 | 3 | 15.5 | HIGH |
| CS-SOC-04 | Fake Meeting App | 3 | 3 | 3 | 4 | 3 | 15.5 | HIGH |
| CS-SOC-05 | AI Deepfake | 3 | 3 | 3 | 4 | 3 | 15.5 | HIGH |
| CS-SOC-06 | Forced Labor Compound | 4 | 4 | 4 | 4 | 4 | 20.0 | CRITICAL |
| CS-SOC-07 | Typosquatting | 4 | 3 | 3 | 2 | 3 | 15.0 | HIGH |
| CS-MAL-01 | Clipboard Hijacking | 4 | 3 | 3 | 3 | 3 | 16.0 | CRITICAL |
| CS-MAL-02 | InfoStealer/RAT | 3 | 4 | 3 | 4 | 4 | 17.5 | CRITICAL |
| CS-MAL-03 | Fake Cloudflare | 3 | 3 | 3 | 4 | 3 | 15.5 | HIGH |
| CS-WAL-01 | Seed Phrase Theft | 3 | 4 | 2 | 3 | 4 | 16.0 | CRITICAL |
| CS-WAL-02 | Address Poisoning | 4 | 3 | 3 | 4 | 3 | 16.5 | CRITICAL |
| CS-WAL-03 | DNS Hijack | 2 | 4 | 3 | 4 | 4 | 17.0 | CRITICAL |
| CS-WAL-04 | Malicious Signature | 4 | 4 | 3 | 4 | 4 | 19.0 | CRITICAL |
| CS-WAL-05 | Low Entropy Seed | 1 | 4 | 1 | 4 | 4 | 14.5 | HIGH |
| CS-DFI-01 | Admin Key Exploit | 2 | 4 | 3 | 3 | 4 | 16.5 | CRITICAL |
| CS-DFI-02 | Flash Loan Attack | 2 | 3 | 3 | 3 | 4 | 14.5 | HIGH |
| CS-DFI-03 | Bridge Exploit | 2 | 4 | 4 | 3 | 4 | 17.5 | CRITICAL |
| CS-DFI-04 | Oracle Manipulation | 2 | 3 | 3 | 3 | 4 | 14.5 | HIGH |
| CS-DFI-05 | Reentrancy | 1 | 3 | 2 | 3 | 3 | 11.5 | ELEVATED |
| CS-SC-01 | NPM Package Hijack | 3 | 4 | 4 | 4 | 4 | 19.0 | CRITICAL |
| CS-SC-02 | SDK/Library Poisoning | 2 | 4 | 4 | 4 | 4 | 18.0 | CRITICAL |
| CS-SC-03 | CI/CD Compromise | 2 | 4 | 4 | 4 | 4 | 18.0 | CRITICAL |
| CS-SC-04 | AI Model Backdoor | 1 | 4 | 4 | 4 | 4 | 17.5 | CRITICAL |
| CS-AI-01 | Memory Poisoning | 2 | 4 | 3 | 4 | 4 | 17.5 | CRITICAL |
| CS-AI-02 | Prompt Injection | 3 | 4 | 3 | 4 | 4 | 18.0 | CRITICAL |
| CS-AI-03 | Data Chain Poisoning | 2 | 3 | 3 | 4 | 3 | 15.0 | HIGH |
| CS-AI-04 | AI Swarm Attack | 1 | 4 | 4 | 4 | 4 | 17.5 | CRITICAL |
| CS-AI-05 | Synthetic Identity Fraud | 3 | 3 | 3 | 4 | 3 | 15.5 | HIGH |
| CS-MKT-01 | MEV/Sandwich Attack | 4 | 2 | 4 | 4 | 3 | 15.5 | HIGH |
| CS-MKT-02 | Tokenomics Weaponization | 4 | 3 | 4 | 4 | 3 | 17.5 | CRITICAL |
| CS-MKT-03 | Influence Operation | 4 | 2 | 4 | 3 | 2 | 13.5 | HIGH |
| CS-SOV-01 | CBDC Surveillance | 1 | 4 | 4 | 2 | 4 | 15.5 | HIGH |
| CS-SOV-02 | CEX KYC Overreach | 3 | 2 | 4 | 2 | 2 | 12.0 | ELEVATED |
| CS-FRD-01 | Pig Butchering | 4 | 4 | 4 | 4 | 4 | 20.0 | CRITICAL |
| CS-FRD-02 | Recovery Re-Victimization | 3 | 3 | 3 | 4 | 3 | 15.5 | HIGH |
| CS-FRD-03 | Bitcoin ATM Coercion | 3 | 3 | 3 | 3 | 3 | 15.0 | HIGH |
| CS-FRD-04 | Investment Group Scam | 3 | 3 | 3 | 4 | 3 | 15.5 | HIGH |
| CS-EXT-01 | Sextortion/Ransomware | 3 | 3 | 3 | 3 | 3 | 15.0 | HIGH |

---

## Top 10 Critical Threats by CTRS

| Rank | Threat ID | Name | CTRS |
|---|---|---|---|
| 1 | CS-FRD-01 | Pig Butchering / Financial Grooming | 20.0 |
| 1 | CS-SOC-06 | Forced Labor Compound Operations | 20.0 |
| 3 | CS-WAL-04 | Malicious Signature (Permit2/ERC-20) | 19.0 |
| 3 | CS-SC-01 | NPM Package Hijacking | 19.0 |
| 5 | CS-SC-02 | SDK/Library Poisoning | 18.0 |
| 5 | CS-SC-03 | CI/CD Pipeline Compromise | 18.0 |
| 5 | CS-AI-02 | Prompt Injection (AI Agents) | 18.0 |
| 8 | CS-MAL-02 | InfoStealer/RAT | 17.5 |
| 8 | CS-DFI-03 | Bridge Exploit | 17.5 |
| 8 | CS-SC-04 | AI Model Backdoor | 17.5 |

---

## CTRS vs. Raw Dollar Loss

CTRS is intentionally not a financial loss metric. It weights sovereignty impact and recoverability, which can diverge from raw dollar amounts:

- CS-PHY-01 (Kidnapping): CTRS 15.0: relatively low dollar loss in aggregate, but maximum personal impact
- CS-FRD-01 (Pig Butchering): CTRS 20.0: $7.2B in U.S. losses 2025; maximum across all dimensions
- CS-DFI-05 (Reentrancy): CTRS 11.5: historically high dollar losses but declining frequency and improving detection

The CTRS should be used alongside financial loss data from the threat registry, not as a replacement.

---

*CTRS Scoring Methodology | CSI CryptoSHIELD Framework v1.1*
*Cyber Strategy Institute | Open-Source*
