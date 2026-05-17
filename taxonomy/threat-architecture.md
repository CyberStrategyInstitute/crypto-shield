# CryptoSHIELD Threat Architecture: Five-Layer Causal Stack

**CSI CryptoSHIELD Framework v1.1**
Cyber Strategy Institute | Open-Source

---

## Overview

Crypto threats do not exist in isolation. They operate within a causal architecture: structural conditions create vulnerability, attack techniques exploit that vulnerability, delivery mechanisms amplify reach, and human outcomes result. Defending only at the technique layer leaves the structural conditions intact: which is why the same categories of attacks recur across market cycles, platforms, and technologies.

The CryptoSHIELD threat architecture is modeled on the Cognitive Sovereignty Framework's five-layer causal stack, adapted for the crypto-specific threat environment.

---

## The Five-Layer Stack

```
Layer +2: Economic & Social Outcomes
      ↑ (manifests when attacks succeed)
Layer +1: Delivery & Scale Mechanisms
      ↑ (amplifies and spreads attacks)
Layer  0: Attack Techniques (T-CS)
      ↑ (exploits vulnerabilities)
Layer -1: Substrate Vulnerabilities (VS)
      ↑ (preconditions that enable attacks)
Layer -2: Structural Drivers (SD)
      (root forces generating the threat environment)
```

**Critical Insight:** Controls that operate only at Layer 0 (technique blocking) are permanently reactive. New techniques continuously emerge from the same Layer -2 structural drivers. Addressing Layer -1 substrate vulnerabilities is the minimum effective defense posture.

---

## Layer -2: Structural Drivers (SD)

Root forces that generate the threat environment. These cannot be eliminated by individual action, but understanding them shapes realistic threat expectations.

| ID | Driver | Description |
|---|---|---|
| SD-001 | Irreversibility by Design | Blockchain finality means there are no chargebacks, no fraud departments, no recovery mechanisms. Every theft is permanent. This is a structural vulnerability that all other layers exploit. |
| SD-002 | Pseudonymity Asymmetry | Attackers can operate pseudonymously with very low identity risk. Defenders must often expose identity to participate in the ecosystem (CEX KYC, social media presence). |
| SD-003 | Regulatory Vacuum and Overreach | Regulatory uncertainty creates exploitable gaps (no enforcement) and illegitimate surveillance threats (overreach). Both create adversarial conditions. |
| SD-004 | Wealth Concentration Visibility | On-chain wealth is partially transparent. Large wallets are permanently identifiable OSINT targets. |
| SD-005 | Technical Complexity as Barrier | The cognitive load of safely using crypto is high. This gap is continuously exploited by social engineers, fake support, and malicious interfaces. |
| SD-006 | Speed and 24/7 Operation | Crypto markets never close. Attackers exploit timing mismatches: attacks execute at 3 AM when defenders are asleep; AI agents execute at machine speed when human review is impossible. |

---

## Layer -1: Substrate Vulnerabilities (VS)

Pre-conditions that make attacks succeed. These are addressable by individual and protocol-level action: they are the primary target of CryptoSHIELD controls.

| ID | Vulnerability | Description | Addressing Domain |
|---|---|---|---|
| VS-001 | Key Exposure | Private keys or seed phrases stored digitally, in accessible locations, or shared with third parties | Domain 01 (WKS) |
| VS-002 | OSINT Linkage | Real-world identity linked to on-chain wealth through public data | Domain 03 (OPS) |
| VS-003 | Unverified Code Execution | Unknown or unaudited code running on devices that have crypto access | Domain 02 (EDD), Domain 06 (SCD) |
| VS-004 | Unbounded Token Approvals | Existing token approvals granting permanent, unlimited spend access to protocols | Domain 05 (OCM) |
| VS-005 | Social Trust Exploitation | Tendency to trust authority, urgency, and social proof in financial contexts | Domain 04 (SMS) |
| VS-006 | Insufficient Multisig Design | Multi-signature schemes controlled by non-independent signers; single points of failure | Domain 01 (WKS) |
| VS-007 | AI Agent Privilege Excess | AI agents holding private keys, memory with sensitive data, or unrestricted tool access | Domain 07 (AAS) |
| VS-008 | Unverified Platform Trust | Depositing funds into platforms without independent legitimacy verification | Domain 04 (SMS), Domain 09 (CFD) |
| VS-009 | Cognitive Vulnerability | Human susceptibility to emotional manipulation, fake urgency, social engineering | CSF Domain 3 (Emotional Resilience) |
| VS-010 | Supply Chain Blindspot | Dependency on third-party code that has not been audited or verified | Domain 06 (SCD) |

---

## Layer 0: Attack Techniques (T-CS)

Active exploitation techniques targeting substrate vulnerabilities. Full specifications in `taxonomy/registry.json`.

### Physical Category (CS-PHY)
| ID | Technique | VS Exploited |
|---|---|---|
| CS-PHY-01 | Kidnapping and Physical Coercion | VS-001, VS-002 |
| CS-PHY-02 | Home Invasion | VS-001, VS-002 |

### Insider Threat Category (CS-INS)
| ID | Technique | VS Exploited |
|---|---|---|
| CS-INS-01 | Admin Key Abuse by Trusted Actor | VS-006, VS-003 |
| CS-INS-02 | CEX Support Bribery | VS-008, VS-005 |
| CS-INS-03 | DPRK Wagemole Identity Infiltration | VS-006, VS-005 |

### Social Engineering Category (CS-SOC)
| ID | Technique | VS Exploited |
|---|---|---|
| CS-SOC-01 | Phishing | VS-005, VS-008 |
| CS-SOC-02 | Fake Hardware Wallet | VS-005, VS-001 |
| CS-SOC-03 | Fake Job Offer (Malware Delivery) | VS-005, VS-003 |
| CS-SOC-04 | Fake Meeting App | VS-005, VS-003 |
| CS-SOC-05 | AI Deepfake Impersonation | VS-005, VS-009 |
| CS-SOC-06 | Forced Labor Compound Operations | VS-005, VS-008, VS-009 |
| CS-SOC-07 | Typosquatting / Domain Impersonation | VS-005, VS-008 |

### Malware Category (CS-MAL)
| ID | Technique | VS Exploited |
|---|---|---|
| CS-MAL-01 | Clipboard Hijacking | VS-003, VS-005 |
| CS-MAL-02 | InfoStealer / Remote Access Trojan | VS-003, VS-001 |
| CS-MAL-03 | Fake Cloudflare / Drive-By PowerShell | VS-003, VS-005 |

### Wallet Attack Category (CS-WAL)
| ID | Technique | VS Exploited |
|---|---|---|
| CS-WAL-01 | Seed Phrase Theft | VS-001, VS-005 |
| CS-WAL-02 | Address Poisoning | VS-005, VS-004 |
| CS-WAL-03 | DNS / Frontend Hijack | VS-008, VS-005 |
| CS-WAL-04 | Malicious Signature (Permit2/ERC-20) | VS-004, VS-005 |
| CS-WAL-05 | Low Entropy Seed Generation | VS-001, VS-003 |

### DeFi Protocol Category (CS-DFI)
| ID | Technique | VS Exploited |
|---|---|---|
| CS-DFI-01 | Admin Key Exploit | VS-006, VS-003 |
| CS-DFI-02 | Flash Loan Attack | Protocol design |
| CS-DFI-03 | Bridge Exploit | VS-006 (verifier design) |
| CS-DFI-04 | Oracle Manipulation | Protocol design |
| CS-DFI-05 | Reentrancy | VS-003, VS-010 |

### Supply Chain Category (CS-SC)
| ID | Technique | VS Exploited |
|---|---|---|
| CS-SC-01 | NPM Package Hijacking | VS-010, VS-003 |
| CS-SC-02 | SDK / Library Poisoning | VS-010, VS-003 |
| CS-SC-03 | CI/CD Pipeline Compromise | VS-010, VS-006 |
| CS-SC-04 | AI Model Backdoor | VS-010, VS-007 |

### AI Agent Category (CS-AI)
| ID | Technique | VS Exploited |
|---|---|---|
| CS-AI-01 | Memory Poisoning | VS-007, VS-010 |
| CS-AI-02 | Prompt Injection | VS-007, VS-005 |
| CS-AI-03 | Data Chain Poisoning | VS-007, VS-010 |
| CS-AI-04 | AI Swarm Attack | VS-007, VS-003 |
| CS-AI-05 | Synthetic Identity / Document Fraud | VS-005, VS-009 |

### Market Manipulation Category (CS-MKT)
| ID | Technique | VS Exploited |
|---|---|---|
| CS-MKT-01 | MEV / Sandwich Attack | Protocol design |
| CS-MKT-02 | Tokenomics Weaponization | VS-005, VS-009 |
| CS-MKT-03 | Influence Operation / FUD | VS-005, VS-009 |

### Sovereignty Category (CS-SOV)
| ID | Technique | VS Exploited |
|---|---|---|
| CS-SOV-01 | CBDC Surveillance Architecture | Structural |
| CS-SOV-02 | CEX KYC Overreach | VS-008, Structural |

### Financial Fraud Category (CS-FRD)
| ID | Technique | VS Exploited |
|---|---|---|
| CS-FRD-01 | Pig Butchering / Financial Grooming | VS-005, VS-008, VS-009 |
| CS-FRD-02 | Recovery Re-Victimization | VS-005, VS-009 |
| CS-FRD-03 | Bitcoin ATM / QR Code Coercion | VS-005, VS-009 |
| CS-FRD-04 | Investment Group Scam | VS-005, VS-009 |

### Extortion Category (CS-EXT)
| ID | Technique | VS Exploited |
|---|---|---|
| CS-EXT-01 | Sextortion / Blackmail / Ransomware | VS-005, VS-009 |

---

## Layer +1: Delivery and Scale Mechanisms

How attacks are distributed and amplified:

| ID | Mechanism | Primary Threat IDs Delivered |
|---|---|---|
| DM-001 | AI-Powered Mass Personalization | CS-SOC-01, CS-FRD-01, CS-SOC-05 |
| DM-002 | Social Media Platform Amplification | CS-MKT-03, CS-SOC-01, CS-WAL-03 |
| DM-003 | Compromised Open Source Infrastructure | CS-SC-01, CS-SC-02, CS-SC-04 |
| DM-004 | Messaging App Networks | CS-FRD-01, CS-FRD-04, CS-SOC-03 |
| DM-005 | AI Agent Swarm Coordination | CS-AI-04, CS-MKT-03 |
| DM-006 | Physical World (Mail, In-Person) | CS-PHY-01, CS-PHY-02, CS-SOC-02 |

---

## Layer +2: Economic and Social Outcomes

Observed outcomes when attacks succeed:

| ID | Outcome | Primary Threat Sources |
|---|---|---|
| EO-001 | Individual Wealth Destruction | CS-FRD-01, CS-WAL-04, CS-PHY-01 |
| EO-002 | Protocol Insolvency | CS-DFI-03, CS-INS-01, CS-SC-02 |
| EO-003 | Ecosystem Trust Erosion | CS-MKT-02, CS-MKT-03, CS-FRD-01 |
| EO-004 | Regulatory Overreach Trigger | CS-MKT-02, high-profile hacks |
| EO-005 | Physical Harm | CS-PHY-01, CS-PHY-02 |
| EO-006 | Capital Concentration | CS-MKT-01, CS-MKT-02 (Rotator Effect) |

---

## Relationship to Companion Frameworks

**Cognitive layer:** Layer -1 VS-009 (Cognitive Vulnerability) and VS-005 (Social Trust) are addressed by the Cognitive Sovereignty Framework. CryptoSHIELD provides the technical controls; CSF addresses the human cognition layer that all social engineering attacks exploit.
→ [Cognitive Sovereignty Framework](https://github.com/CyberStrategyInstitute/cognitive-sovereignty)

**AI agent layer:** CS-AI-01 through CS-AI-05, VS-007, and the full AI governance model are addressed in detail by AI SAFE² v3.0. CryptoSHIELD defers to AI SAFE² for comprehensive AI agent governance.
→ [AI SAFE² Framework v3.0](https://github.com/CyberStrategyInstitute/ai-safe2-framework)

---

*Threat Architecture | CSI CryptoSHIELD Framework v1.1*
*Cyber Strategy Institute | Open-Source*
