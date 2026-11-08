# CryptoSHIELD threat registry

Generated from [registry.json](registry.json). Do not edit this table manually.

44 threat definitions across 12 categories. All evidence is pending primary review. Severity is inherited qualitative metadata, separate from a calculated tier. CTRS is suspended; legacy scores are not current risk ratings. Candidate controls are proposed mitigations, not prevention evidence.

| Threat ID | Name | Category | Severity (inherited) | Legacy CTRS (unvalidated) | Candidate controls |
|---|---|---|---|---|---|
| CS-PHY-01 | Physical Kidnapping and Coercion | Physical | CRITICAL | 15.0 | OPS-01, OPS-02, OPS-05, OPS-06, OPS-10 |
| CS-PHY-02 | Home Invasion and Physical Assault | Physical | CRITICAL | 15.0 | OPS-01, OPS-04, OPS-07, OPS-08, OPS-09 |
| CS-INS-01 | Admin Key Abuse by Trusted Developer | Insider | CRITICAL | 17.0 | WKS-02, WKS-03, WKS-05, SCD-10, GCS-11 |
| CS-INS-02 | CEX Customer Support Bribery | Insider | HIGH | 14.5 | GCS-04, OPS-01, GCS-05 |
| CS-INS-03 | DPRK Wagemole Infiltration | Insider | CRITICAL | 17.0 | SCD-05, GCS-06, SCD-10, CDG-06 |
| CS-SOC-01 | AI-Enhanced Phishing | Social Engineering | HIGH | 16.0 | SMS-05, SMS-06, EDD-01 |
| CS-SOC-02 | Fake Hardware Wallet Mailing | Social Engineering | CRITICAL | 15.5 | WKS-01, EDD-10, GCS-04, WKS-13 |
| CS-SOC-03 | Fake Cryptocurrency Job Offer | Social Engineering | HIGH | 15.5 | EDD-01, EDD-02, SMS-06 |
| CS-SOC-04 | Fake Meeting App Malware | Social Engineering | HIGH | 15.5 | EDD-01, EDD-10, SMS-06 |
| CS-SOC-05 | AI Deepfake Impersonation | Social Engineering | HIGH | 15.5 | CFD-08, SMS-07 |
| CS-SOC-06 | Forced Labor Scam Compound Operations | Social Engineering | HIGH | 20.0 | CFD-01, CFD-02 |
| CS-SOC-07 | Typosquatting and Domain Impersonation | Social Engineering | HIGH | 15.0 | SMS-05, SMS-11, SMS-09 |
| CS-MAL-01 | Clipboard Hijacking (MassJacker Pattern) | Malware | HIGH | 16.0 | EDD-04, EDD-01, EDD-03 |
| CS-MAL-02 | InfoStealer and Remote Access Trojan | Malware | HIGH | 17.5 | EDD-01, EDD-02, EDD-03 |
| CS-MAL-03 | Fake Cloudflare / DEX Verification Page | Malware | HIGH | 15.5 | EDD-01, EDD-05, SMS-05 |
| CS-WAL-01 | Seed Phrase Extraction | Wallet | CRITICAL | 16.0 | WKS-04, WKS-01, EDD-02, WKS-11, WKS-12 |
| CS-WAL-02 | Address Poisoning | Wallet | MEDIUM | 16.5 | OCM-06, WKS-06, EDD-04 |
| CS-WAL-03 | DNS Hijack / Frontend Compromise | Wallet | HIGH | 17.0 | SMS-05, OCM-01, SMS-09 |
| CS-WAL-04 | Malicious Signature / Permit Drain | Wallet | HIGH | 19.0 | WKS-05, WKS-08, OCM-10, OCM-01, WKS-11, WKS-12, AAS-11 |
| CS-WAL-05 | Low Entropy Seed Generation | Wallet | HIGH | 14.5 | WKS-01, EDD-10, GCS-08, WKS-13 |
| CS-DFI-01 | Admin Key Exploit via Access Control Failure | DeFi Protocol | CRITICAL | 16.5 | WKS-02, WKS-03, WKS-05, SCD-10, WKS-11, GCS-11, GCS-12 |
| CS-DFI-02 | Flash Loan Attack | DeFi Protocol | HIGH | 14.5 | AAS-09, OCM-04, GCS-12 |
| CS-DFI-03 | Cross-Chain Bridge Exploit | DeFi Protocol | CRITICAL | 17.5 | OCM-07, OCM-11, OCM-12, GCS-13 |
| CS-DFI-04 | Oracle Price Manipulation | DeFi Protocol | HIGH | 14.5 | AAS-09, OCM-08 |
| CS-DFI-05 | Reentrancy and Smart Contract Logic Exploit | DeFi Protocol | HIGH | 11.5 | OCM-08, SCD-10 |
| CS-SC-01 | NPM Package Hijacking | Supply Chain | CRITICAL | 19.0 | SCD-01, SCD-02, SCD-07 |
| CS-SC-02 | SDK and Framework Poisoning | Supply Chain | CRITICAL | 18.0 | SCD-01, SCD-02, SCD-07 |
| CS-SC-03 | CI/CD Pipeline Compromise | Supply Chain | CRITICAL | 18.0 | SCD-03, SCD-01, SCD-10 |
| CS-SC-04 | AI Model Backdoor | Supply Chain | HIGH | 17.5 | SCD-08, SCD-01 |
| CS-AI-01 | AI Agent Memory Poisoning | AI Agent | CRITICAL | 17.5 | AAS-02, AAS-03, AAS-12 |
| CS-AI-02 | Prompt Injection / Logic Redefinition | AI Agent | HIGH | 18.0 | AAS-03, AAS-08, WKS-12, OCM-11, AAS-11, AAS-12 |
| CS-AI-03 | Data Chain Poisoning via Runtime Browsing | AI Agent | HIGH | 15.0 | AAS-03, AAS-02 |
| CS-AI-04 | AI Swarm Coordinated Attack | AI Agent | CRITICAL | 17.5 | AAS-10, AAS-06, AAS-08, OCM-11, AAS-11, AAS-12 |
| CS-AI-05 | Synthetic Identity and AI Document Fraud | AI Agent | HIGH | 15.5 | CFD-08, SMS-07 |
| CS-MKT-01 | MEV and Sandwich Attack | Market Manipulation | HIGH | 15.5 | OCM-04, OCM-05 |
| CS-MKT-02 | Tokenomics Weaponization | Market Manipulation | HIGH | 17.5 | SMS-10, GCS-12 |
| CS-MKT-03 | Coordinated Influence Operation | Market Manipulation | MEDIUM | 13.5 | SMS-10, CFD-09, CDG-06 |
| CS-FRD-01 | Pig Butchering / Financial Grooming | Financial Fraud | CRITICAL | 20.0 | CFD-01, CFD-02, CFD-03, CFD-04, SMS-13, GCS-13 |
| CS-FRD-02 | Asset Recovery Re-Victimization | Financial Fraud | HIGH | 15.5 | CFD-07, SMS-15 |
| CS-FRD-03 | Bitcoin ATM / QR Code Coercion Fraud | Financial Fraud | HIGH | 15.0 | CFD-05, CFD-06 |
| CS-FRD-04 | Investment Group / Professor Scam | Financial Fraud | HIGH | 15.5 | CFD-02, CFD-09, SMS-06 |
| CS-SOV-01 | CBDC Surveillance Architecture | Sovereignty | CRITICAL | 15.5 | GCS-02, WKS-01, GCS-01 |
| CS-SOV-02 | Regulatory Overreach via CEX KYC Data | Sovereignty | HIGH | 12.0 | GCS-04, OPS-02, GCS-13 |
| CS-EXT-01 | Sextortion, Ransomware, and Crypto Blackmail | Extortion | HIGH | 15.0 | EDD-01, EDD-09 |

See [scoring suspension](ctrs-scoring.md), [migration](../metadata/README.md), and [historical records](legacy/README.md).
