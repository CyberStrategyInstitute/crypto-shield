# CryptoSHIELD control self-assessment

This checklist records implementation evidence and gaps. The former 100-point instrument and assurance tiers are withdrawn: weights and applicability handling were unvalidated, several fraud questions referenced the wrong controls, and inapplicable controls could receive automatic credit.

For each applicable control, record **verified**, **partial**, **absent**, or **unknown**, evidence and date, owner, residual exposure, and next action. Use **not applicable** only with a rationale. Do not award points for inapplicability. Optional decoys must not be a condition for a favorable result.

## Control inventory

<!-- assessment:start -->
| Control | Definition | Evidence/status, owner, date, next action |
|---|---|---|
| [CDG-01](../00-cross-domain/README.md) | Sovereignty-First Policy Declaration: explicit written commitment to self-custody as the default | |
| [CDG-02](../00-cross-domain/README.md) | U.S. Constitutional Alignment Protocol: framework review against applicable court rulings quarterly | |
| [CDG-03](../00-cross-domain/README.md) | CBDC Non-Adoption Commitment: documented organizational policy against CBDC participation | |
| [CDG-04](../00-cross-domain/README.md) | Self-Custody Rights Documentation: maintain documented record of self-custody rights per jurisdiction | |
| [CDG-05](../00-cross-domain/README.md) | Annual Sovereignty Architecture Review: annual comprehensive review of all framework controls against updated threat and regulatory landscape | |
| [CDG-06](../00-cross-domain/README.md) | Evidence provenance and claim lifecycle | |
| [CDG-07](../00-cross-domain/README.md) | Versioned assessment and compatibility governance | |
| [WKS-01](../01-wallet-key-sovereignty/README.md) | Hardware wallet and device-integrity review | |
| [WKS-02](../01-wallet-key-sovereignty/README.md) | Multisig with Geographic Diversity | |
| [WKS-03](../01-wallet-key-sovereignty/README.md) | Tiered Timelock on Governance Transactions | |
| [WKS-04](../01-wallet-key-sovereignty/README.md) | Seed Phrase Offline Sovereignty | |
| [WKS-05](../01-wallet-key-sovereignty/README.md) | No Blind Signing | |
| [WKS-06](../01-wallet-key-sovereignty/README.md) | Independent Address Verification Protocol | |
| [WKS-07](../01-wallet-key-sovereignty/README.md) | Token Approval Revocation Protocol | |
| [WKS-08](../01-wallet-key-sovereignty/README.md) | Permit Scam Recognition | |
| [WKS-09](../01-wallet-key-sovereignty/README.md) | Cold storage and total accessible exposure | |
| [WKS-10](../01-wallet-key-sovereignty/README.md) | Watch-Only Wallet for Household Members | |
| [WKS-11](../01-wallet-key-sovereignty/README.md) | Financial authority inventory | |
| [WKS-12](../01-wallet-key-sovereignty/README.md) | Authority revocation and recovery verification | |
| [WKS-13](../01-wallet-key-sovereignty/README.md) | Hardware procurement and whole-device trust | |
| [EDD-01](../02-endpoint-device-defense/README.md) | Kernel-Level Default-Deny Endpoint Protection | |
| [EDD-02](../02-endpoint-device-defense/README.md) | Dedicated Signing Device | |
| [EDD-03](../02-endpoint-device-defense/README.md) | Verified Software and SBOM for Developers | |
| [EDD-04](../02-endpoint-device-defense/README.md) | Anti-Clipboard-Hijack Protocol | |
| [EDD-05](../02-endpoint-device-defense/README.md) | Browser Extension Minimization | |
| [EDD-06](../02-endpoint-device-defense/README.md) | Operating System Hardening | |
| [EDD-07](../02-endpoint-device-defense/README.md) | EDR as Supplemental Detection Layer | |
| [EDD-08](../02-endpoint-device-defense/README.md) | Network Isolation for Signing Operations | |
| [EDD-09](../02-endpoint-device-defense/README.md) | Physical Security of Signing Device | |
| [EDD-10](../02-endpoint-device-defense/README.md) | Application Allowlisting | |
| [OPS-01](../03-opsec-physical-security/README.md) | Zero Public Disclosure of Holdings | |
| [OPS-02](../03-opsec-physical-security/README.md) | Decouple Identity from On-Chain | |
| [OPS-03](../03-opsec-physical-security/README.md) | Chain-aware address privacy | |
| [OPS-04](../03-opsec-physical-security/README.md) | OSINT Self-Audit | |
| [OPS-05](../03-opsec-physical-security/README.md) | Physical Incident Response Plan | |
| [OPS-06](../03-opsec-physical-security/README.md) | Optional decoy risk assessment | |
| [OPS-07](../03-opsec-physical-security/README.md) | Family OPSEC | |
| [OPS-08](../03-opsec-physical-security/README.md) | Geolocation Hygiene | |
| [OPS-09](../03-opsec-physical-security/README.md) | Surveillance Detection | |
| [OPS-10](../03-opsec-physical-security/README.md) | Duress Protocol | |
| [SMS-01](../04-social-media-platform-security/README.md) | Phishing-resistant authentication where supported | |
| [SMS-02](../04-social-media-platform-security/README.md) | Reduce phone-based recovery exposure | |
| [SMS-03](../04-social-media-platform-security/README.md) | OAuth Audit | |
| [SMS-04](../04-social-media-platform-security/README.md) | Dedicated Recovery Email | |
| [SMS-05](../04-social-media-platform-security/README.md) | URL Verification | |
| [SMS-06](../04-social-media-platform-security/README.md) | No Unsolicited DM Trust | |
| [SMS-07](../04-social-media-platform-security/README.md) | Social Engineering Drill | |
| [SMS-08](../04-social-media-platform-security/README.md) | Official Channel Verification | |
| [SMS-09](../04-social-media-platform-security/README.md) | DNS/Frontend Alert System | |
| [SMS-10](../04-social-media-platform-security/README.md) | Influencer Skepticism Protocol | |
| [SMS-11](../04-social-media-platform-security/README.md) | Manual URL Entry Protocol | |
| [SMS-12](../04-social-media-platform-security/README.md) | Pre-Transaction Platform Verification | |
| [SMS-13](../04-social-media-platform-security/README.md) | 10-Day Rule for New Platforms | |
| [SMS-14](../04-social-media-platform-security/README.md) | Independently verify withdrawal fee demands | |
| [SMS-15](../04-social-media-platform-security/README.md) | Recovery scam awareness | |
| [OCM-01](../05-on-chain-monitoring/README.md) | Transaction Simulation | |
| [OCM-02](../05-on-chain-monitoring/README.md) | Real-Time Wallet Monitor | |
| [OCM-03](../05-on-chain-monitoring/README.md) | Authority monitoring and revocation | |
| [OCM-04](../05-on-chain-monitoring/README.md) | Mempool Awareness | |
| [OCM-05](../05-on-chain-monitoring/README.md) | MEV Protection | |
| [OCM-06](../05-on-chain-monitoring/README.md) | Address Poisoning Detection | |
| [OCM-07](../05-on-chain-monitoring/README.md) | Bridge verification and backing assessment | |
| [OCM-08](../05-on-chain-monitoring/README.md) | Smart Contract Audit Verification | |
| [OCM-09](../05-on-chain-monitoring/README.md) | Anomaly Detection | |
| [OCM-10](../05-on-chain-monitoring/README.md) | Permit/Signature Intelligence | |
| [OCM-11](../05-on-chain-monitoring/README.md) | Aggregate exposure budget enforcement | |
| [OCM-12](../05-on-chain-monitoring/README.md) | Bridge backing and redemption invariants | |
| [SCD-01](../06-supply-chain-defense/README.md) | SBOM Enforcement | |
| [SCD-02](../06-supply-chain-defense/README.md) | Dependency Allowlisting | |
| [SCD-03](../06-supply-chain-defense/README.md) | CI/CD Secret Isolation | |
| [SCD-04](../06-supply-chain-defense/README.md) | Binary Analysis | |
| [SCD-05](../06-supply-chain-defense/README.md) | Third-Party Risk Assessment | |
| [SCD-06](../06-supply-chain-defense/README.md) | Adversarial Supply Chain Simulation | |
| [SCD-07](../06-supply-chain-defense/README.md) | Package Lock Pinning | |
| [SCD-08](../06-supply-chain-defense/README.md) | AI Model Provenance | |
| [SCD-09](../06-supply-chain-defense/README.md) | Post-Install Hook Blocking | |
| [SCD-10](../06-supply-chain-defense/README.md) | Critical Release Exam | |
| [AAS-01](../07-ai-agent-security/README.md) | Separate agent decisions from signing authority | |
| [AAS-02](../07-ai-agent-security/README.md) | Memory provenance and integrity | |
| [AAS-03](../07-ai-agent-security/README.md) | Prompt injection containment | |
| [AAS-04](../07-ai-agent-security/README.md) | Agent wallet isolation: minimal-balance dedicated wallets per strategy | |
| [AAS-05](../07-ai-agent-security/README.md) | Testnet simulation first: no mainnet deployment without sandbox validation | |
| [AAS-06](../07-ai-agent-security/README.md) | Aggregate financial exposure limits | |
| [AAS-07](../07-ai-agent-security/README.md) | Real-time agent behavior anomaly detection | |
| [AAS-08](../07-ai-agent-security/README.md) | Tool call allowlisting: permitted smart contracts and endpoints only | |
| [AAS-09](../07-ai-agent-security/README.md) | Independent oracle inputs and outage policy | |
| [AAS-10](../07-ai-agent-security/README.md) | Swarm isolation and shared exposure limits | |
| [AAS-11](../07-ai-agent-security/README.md) | Independent human financial authorization | |
| [AAS-12](../07-ai-agent-security/README.md) | Agent shutdown and persistent-authority containment | |
| [GCS-01](../08-governance-compliance-sovereignty/README.md) | Self-Custody First Policy | |
| [GCS-02](../08-governance-compliance-sovereignty/README.md) | CBDC Resistance Protocol | |
| [GCS-03](../08-governance-compliance-sovereignty/README.md) | Legal Awareness | |
| [GCS-04](../08-governance-compliance-sovereignty/README.md) | Minimize identity data within applicable law | |
| [GCS-05](../08-governance-compliance-sovereignty/README.md) | Vendor Sovereignty Assessment | |
| [GCS-06](../08-governance-compliance-sovereignty/README.md) | Incident Response Plan | |
| [GCS-07](../08-governance-compliance-sovereignty/README.md) | Decentralized Governance Participation | |
| [GCS-08](../08-governance-compliance-sovereignty/README.md) | Open Source Preference | |
| [GCS-09](../08-governance-compliance-sovereignty/README.md) | Privacy Tool Assessment | |
| [GCS-10](../08-governance-compliance-sovereignty/README.md) | Annual Framework Review | |
| [GCS-11](../08-governance-compliance-sovereignty/README.md) | Bounded emergency authority | |
| [GCS-12](../08-governance-compliance-sovereignty/README.md) | Governance capture and lasting-authority review | |
| [GCS-13](../08-governance-compliance-sovereignty/README.md) | Custody liabilities and asset-rights assessment | |
| [CFD-01](../09-consumer-fraud-defense/README.md) | Platform Legitimacy Stack Check | |
| [CFD-02](../09-consumer-fraud-defense/README.md) | Unsolicited Investment Offer Zero Trust | |
| [CFD-03](../09-consumer-fraud-defense/README.md) | Profitable Test Withdrawal Recognition | |
| [CFD-04](../09-consumer-fraud-defense/README.md) | Fee Demand as Exit Signal | |
| [CFD-05](../09-consumer-fraud-defense/README.md) | Bitcoin ATM Transaction Refusal | |
| [CFD-06](../09-consumer-fraud-defense/README.md) | Elder Household Protocol | |
| [CFD-07](../09-consumer-fraud-defense/README.md) | Recovery Scam Firewall | |
| [CFD-08](../09-consumer-fraud-defense/README.md) | Independent identity verification | |
| [CFD-09](../09-consumer-fraud-defense/README.md) | Group Chat Investment Protocol | |
| [CFD-10](../09-consumer-fraud-defense/README.md) | Custody, liabilities, and withdrawal assessment | |
<!-- assessment:end -->

## Review decisions

Prioritize immediate physical danger and active compromise first. Then address exposed keys or authority, unsafe recovery paths, unbounded budgets, shared trust dependencies, and unverified transaction effects. Use the [wallet decision tree](../playbooks/wallet-compromise.md) during an incident.

A verified item requires implementation evidence, not a vendor name or a checked box alone. Record unsupported platforms and paths. Reassess after incidents, permission or dependency changes, and at least quarterly. This checklist provides no maturity certification, risk probability, protection guarantee, or aggregate safety score.
