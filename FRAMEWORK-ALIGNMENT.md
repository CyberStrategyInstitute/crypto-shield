# CryptoSHIELD Framework Alignment Map

**Cross-Framework Integration Reference | v1.1 | May 2026**

---

## The Three-Framework Stack: Scope Boundaries

CryptoSHIELD does not attempt to replace or duplicate its companion frameworks. The three-framework model has strict scope boundaries that prevent redundancy and ensure each framework maintains deep expertise in its domain.

| Question | Framework | Scope |
|----------|-----------|-------|
| Is my wallet secure? | **CryptoSHIELD** | WKS domain |
| Is my endpoint deterministically protected? | **CryptoSHIELD** | EDD domain |
| Is my on-chain behavior safe? | **CryptoSHIELD** | OCM, WKS domains |
| Am I being physically targeted? | **CryptoSHIELD** | OPS domain |
| Is my supply chain clean? | **CryptoSHIELD** | SCD domain |
| Am I falling for a scam? | **CryptoSHIELD** + CSF | CFD, SMS domains + CSF T-CT layer |
| Is my AI agent governed? | **AI SAFE² v3.0** | All 5 pillars + CP.1-CP.10 |
| Is my crypto AI agent safe from manipulation? | **Both** | CryptoSHIELD AAS + AI SAFE² P1-P4 |
| Am I being cognitively manipulated? | **CSF** | All 6 domains, T-CT taxonomy |
| Am I maintaining decision autonomy with AI? | **CSF** | Domain 6: Digital & AI Symbiosis |
| Is my organization compliant? | **AI SAFE² v3.0** | 32 frameworks mapped |

---

## CryptoSHIELD Domain Alignment to Companion Frameworks

### Domains with AI SAFE² Cross-Reference

**Domain 07: AI Agent and Autonomous System Security (AAS)**

CryptoSHIELD AAS provides crypto-specific controls for AI agents operating in DeFi environments. For complete agentic AI governance, refer to AI SAFE² v3.0:

| CryptoSHIELD Control | AI SAFE² Cross-Reference | Coverage |
|---------------------|--------------------------|---------|
| AAS-01: Keyless agent architecture | AI SAFE² CP.4: Agentic Control Plane | Identity and permission architecture |
| AAS-02: Memory integrity monitoring | AI SAFE² S1.5: Memory Governance; A2.6: RAG Corpus Diff Tracking | Full memory lifecycle |
| AAS-03: Prompt injection hardening | AI SAFE² P1.T1.1-P1.T1.10: Input defense suite | 10-control injection defense |
| AAS-04: Agent wallet isolation | AI SAFE² CP.4: Permission scoping | Privilege minimization |
| AAS-05: Testnet first | AI SAFE² E5.1-E5.4: Adversarial evaluation | Full red team protocol |
| AAS-06: Transaction rate limiting | AI SAFE² F3.2: Circuit breakers | Cascade containment |
| AAS-07: Behavior monitoring | AI SAFE² M4.1-M4.8: Detection pipeline | Full detection suite |
| AAS-08: Tool call allowlisting | AI SAFE² S1.7: No-code platform security | Policy enforcement |
| AAS-09: Oracle diversity | AI SAFE² A2.9: External data integrity | Data source governance |
| AAS-10: Swarm isolation | AI SAFE² CP.9: Agent Replication Governance | First-in-field replication control |

**AI SAFE² capabilities not duplicated in CryptoSHIELD AAS:**
- CP.10: HEAR Doctrine (Human Ethical Agent of Record: cryptographically enforced)
- ACT Capability Tier Classification (ACT-1 through ACT-4)
- OWASP AIVSS v0.8 AAF risk scoring integration
- 151 full pillar controls across P1-P5
- 32-framework compliance mapping
- NEXUS-A2A protocol governance
- Non-Human Identity (NHI) full lifecycle management

→ [AI SAFE² v3.0 Repository](https://github.com/CyberStrategyInstitute/ai-safe2-framework)

---

### Domains with Cognitive Sovereignty Framework Cross-Reference

**Domain 04: Social Media and Platform Security (SMS): Partial CSF Integration**

Social engineering attacks exploit cognitive vulnerabilities. CryptoSHIELD SMS provides the technical controls. CSF provides the cognitive resilience architecture:

| CryptoSHIELD Control | CSF Cross-Reference | What CSF Adds |
|---------------------|---------------------|---------------|
| SMS-06: No unsolicited DM trust | CSF T-CT-007: Trust Network Infiltration | Cognitive pattern recognition for trust exploitation |
| SMS-07: Social engineering drill | CSF Domain 2: Cognitive Resilience | Attention training, deception recognition |
| SMS-10: Influencer skepticism | CSF T-CT-003: Algorithmic Amplification | Structural media manipulation analysis |
| CFD-08: AI persona detection | CSF T-CT-016: Synthetic Identity Fabrication | Full CSF deepfake resilience framework |
| CFD-09: Group chat investment protocol | CSF T-CT-005: Social Proof Manipulation | Cognitive defenses for manufactured consensus |

**CSF capabilities not duplicated in CryptoSHIELD:**
- Six-domain resilience model (Biological, Cognitive, Emotional, Social, Purpose/Moral, Digital & AI Symbiosis)
- 41-entry threat taxonomy across five causal layers
- CTSS scoring model for cognitive threat prioritization
- T-CT-008: Memetic Swarm Orchestration (CTSS 90: highest-scoring threat)
- Domain 6: Digital & AI Symbiosis: maintaining agency while working with AI
- EFA/E7 Protocol Stack for human-AI interface governance
- CSI threat classes TC-01 through TC-10

→ [Cognitive Sovereignty Framework Repository](https://github.com/CyberStrategyInstitute/cognitive-sovereignty)

---

## Mapping to External Standards

### NIST Cybersecurity Framework 2.0

| NIST CSF Function | CryptoSHIELD Domains |
|-------------------|---------------------|
| GOVERN | GCS, CDG (00-cross-domain) |
| IDENTIFY | OCM (asset monitoring), SCD (inventory) |
| PROTECT | WKS, EDD, OPS, SMS, SCD |
| DETECT | OCM, SMS (phishing detection), AAS (agent monitoring) |
| RESPOND | OODA Playbook, playbooks/ directory |
| RECOVER | GCS-06 (incident response plan), OODA Act phase |

### OWASP Top 10 for Web3

| OWASP Web3 Risk | CryptoSHIELD Control |
|----------------|---------------------|
| SC01: Reentrancy | CS-DFI-05; OCM-08 |
| SC02: Integer overflow | CS-DFI-05; OCM-08 |
| SC03: Timestamp manipulation | OCM-08 |
| SC04: Access control | CS-DFI-01; WKS-02, WKS-03 |
| SC05: Front-running | CS-MKT-01; OCM-04, OCM-05 |
| SC06: Oracle manipulation | CS-DFI-04; AAS-09 |
| SC07: Signature replay | CS-WAL-04; OCM-10 |
| SC08: Logic errors | CS-DFI-05; SCD-10 |
| SC09: Governance attacks | CS-DFI-01; WKS-03; GCS-07 |
| SC10: Flash loans | CS-DFI-02 |

### OWASP Agentic AI Top 10 (2026): Crypto-Specific Mapping

| OWASP AI Risk | CryptoSHIELD Control | AI SAFE² Reference |
|--------------|---------------------|-------------------|
| ASI01: Prompt injection | AAS-03 | AI SAFE² P1.T1 suite |
| ASI02: Memory poisoning | AAS-02 | AI SAFE² S1.5 |
| ASI03: Agent identity abuse | AAS-01, AAS-04 | AI SAFE² CP.9 |
| ASI04: Tool misuse | AAS-08 | AI SAFE² M4.x |
| ASI05: Swarm attacks | AAS-10, AAS-06 | AI SAFE² CP.9 |
| ASI09: Loss of human control | AAS-06, AAS-07 | AI SAFE² CP.10 HEAR |

### MITRE ATT&CK: Crypto-Relevant Technique Mapping

| MITRE Technique | Threat ID | Control |
|----------------|-----------|---------|
| T1591 (Gather Victim Identity) | CS-PHY-01 | OPS-02, OPS-04 |
| T1589 (Gather Victim Network Info) | CS-PHY-01, CS-PHY-02 | OPS-03, OPS-08 |
| T1566 (Phishing) | CS-SOC-01, CS-SOC-03, CS-SOC-04 | SMS-05, SMS-06, EDD-01 |
| T1195 (Supply Chain Compromise) | CS-SC-01, CS-SC-02, CS-SC-03 | SCD-01 through SCD-10 |
| T1056 (Input Capture) | CS-MAL-01, CS-MAL-02 | EDD-04, EDD-01 |
| T1583 (Acquire Infrastructure) | CS-SOC-07 | SMS-11, SMS-09 |
| T1601 (Modify System Image) | CS-MAL-03 | EDD-01, EDD-10 |

### U.S. Regulatory Alignment

| Regulation / Order | CryptoSHIELD Alignment | Domain |
|--------------------|----------------------|--------|
| Trump EO January 2025 (self-custody, no CBDC) | Full alignment: GCS-01, GCS-02 | GCS |
| Fifth Circuit: Tornado Cash ruling | Supports GCS sovereignty position | GCS, CDG |
| GENIUS Act (stablecoin framework) | AML at CEX boundary only: consistent with GCS-04 | GCS |
| CLARITY Act (pending Senate) | Reduces regulatory overlap: monitors for impact on GCS controls | GCS |
| FinCEN CTA blocked by courts | Validates GCS-01/02 sovereignty-first approach | GCS |

---

## Integration Guidance for Teams

**If your team is deploying AI trading agents:**
1. Start with AI SAFE² v3.0: full agentic AI governance
2. Apply CryptoSHIELD Domain 07 (AAS) for crypto-specific wallet isolation
3. Apply CryptoSHIELD Domain 05 (OCM) for on-chain monitoring of agent activity
4. Apply CryptoSHIELD Domain 02 (EDD) for the execution environment

**If your team is defending against social engineering:**
1. Start with CryptoSHIELD Domain 04 (SMS) and Domain 09 (CFD) for technical controls
2. Apply CSF Domain 2 (Cognitive Resilience) and Domain 3 (Emotional Resilience) for operator training
3. Apply CSF T-CT taxonomy to identify the specific manipulation technique in use
4. Apply CryptoSHIELD OODA Playbook, Playbook 3 for response protocol

**If your team is a DeFi protocol:**
1. CryptoSHIELD Domain 06 (SCD): supply chain defense
2. CryptoSHIELD Domain 01 (WKS): signing key governance with WKS-02 and WKS-03
3. CryptoSHIELD Domain 05 (OCM): on-chain monitoring
4. AI SAFE² for any AI-integrated features
5. CryptoSHIELD taxonomy CS-DFI-01 through CS-DFI-05 for protocol-specific threat coverage

---

*CryptoSHIELD Framework Alignment | Cyber Strategy Institute | v1.1*
