# CryptoSHIELD OODA Loop Defensive Playbook

**Military Discipline Applied to Crypto Security**

---

> **If you have reached this playbook, a prevention layer has already failed.**
>
> CryptoSHIELD's engineering thesis is that properly implemented controls prevent the conditions that require a response playbook: no unknown code executes, no coerced transfer completes in real-time, no single insider can drain a protocol. If you are reading this mid-incident, something in the prevention stack was either missing, misconfigured, or bypassed. The playbook below limits damage. It does not undo the architectural failure that created the incident.
>
> **After every incident, the first question is not "how do we respond" but "which control layer failed and why." The OODA cycle ends with a mandatory retrospective that updates your prevention architecture: not just your response procedures.**

---

> The OODA loop (Observe, Orient, Decide, Act) is the decision cycle Colonel John Boyd identified as the fundamental unit of competitive advantage in any adversarial contest. The side that cycles faster: and with less cognitive distortion: wins. CryptoSHIELD applies this to crypto security: every threat response begins with full observation, applies structured orientation (including the false flag filter), executes pre-decided playbook responses under stress, and acts at machine speed where possible and human speed where required.

---

## The False Flag / Fall Guy Filter

**Apply this before accepting any official attribution.**

Every OODA-Orient phase must run the False Flag Assessment before accepting conventional attribution (DPRK, external hacker, smart contract bug, market conditions). CSI's multi-pass research across LNDFi, Radiant Capital, Bybit, Drift Protocol, and BrincFi consistently finds:

**Where admin key access exists, the insider-first hypothesis must be exhausted before any state-actor attribution is accepted.**

The fall-guy pattern: A visible actor is sacrificed to absorb public and regulatory attention while deeper capital extraction operations continue. Sam Bankman-Fried / FTX is the canonical case. LNDFi / DPRK attribution is a more recent example.

**False Flag Assessment Checklist:**

```
Before accepting official attribution, verify:
□ Was admin key or privileged access involved?              → If YES: insider-first
□ Was the initial access vector social engineering?         → If YES: insider-first
□ Does the narrative benefit a specific party financially?  → If YES: fall-guy flag
□ Were affected parties in governance relationships?        → If YES: insider-first
□ Is attribution emerging within 24 hours of incident?     → If YES: premature
□ Is "DPRK/Lazarus" the first-response attribution?        → If YES: verify independently
□ Was the code change deployed weeks/months before exploit? → If YES: insider-confirmed
□ Did auditors review the malicious code pre-exploit?       → If YES: governance failure, not hack
□ Are on-chain flows going to Chinese broker intermediaries?→ Could be DPRK OR domestic cover
□ Does removing DPRK attribution change any liability?      → If YES: false_flag_prob HIGH
```

**Scoring:** 3+ YES answers = false_flag_probability ≥ 0.5. Demand independent chain analysis before accepting attribution.

---

## OODA Phase Reference

### OBSERVE: Cast Wide, Evaluate Nothing

The observe phase collects all available signal without interpretation. Cognitive bias at this phase corrupts every downstream decision. Collect everything.

**Threat Intelligence Sources:**
- Scam Sniffer: real-time wallet drainer and phishing detection
- ZachXBT: on-chain forensics and attribution analysis
- Rekt.news: protocol exploit database
- CertiK Skynet: security monitoring and physical threat tracking
- TRM Labs: blockchain analytics and illicit flow tracking
- CSI Weekly Crypto Security Truths: aggregated weekly intelligence
- DFPI Scam Tracker: consumer fraud complaints (California)
- Chainabuse: victim-reported wallet addresses
- CryptoScamDB: phishing URL database
- FBI IC3: consumer fraud reporting and pattern data

**On-Chain Monitoring Signals:**
- Unexpected outgoing transaction from any monitored wallet
- Token approval granted to unknown contract
- Large address cluster interacting with your wallet history
- Dust transaction from look-alike address (address poisoning indicator)
- Unusual bridge activity related to held assets

**Social / Physical Environment:**
- OSINT self-audit results (quarterly): identifiable geotag presence, on-chain/identity link
- Unusual attention from unknown individuals (surveillance detection)
- Unsolicited contact from recruiters, investors, or "support" agents
- Influencer narrative shifts on held assets (Rotator Effect signal)

**AI and Supply Chain:**
- Dependency version change alerts
- CI/CD anomaly detection
- Agent behavior deviations from baseline (if running AI trading agents)
- Cross-reference any AI-generated code against independent sources before execution

---

### ORIENT: Make Sense, Apply Filters, Detect Patterns

Orientation is where cognitive discipline separates disciplined operators from reactive victims. Apply all three filters before classifying an event:

**Filter 1: False Flag / Fall Guy (see above)**

**Filter 2: Rotator Effect Pattern Check**
Ask: Is this incident part of a coordinated liquidity extraction campaign?
- Coordinated FUD across multiple channels simultaneously = Rotator signal
- Influencer narratives shifting in same direction across competing personalities = Rotator signal
- Regulatory action creating liquidity migration toward specific alternatives = Rotator signal
- Token price collapse benefiting identifiable counterparties = Rotator signal

**Filter 3: Social Engineering Recognition (defer to CSF)**
For cognitive manipulation pattern recognition, deepfake detection, and social engineering resilience: [CSF T-CT framework](https://github.com/CyberStrategyInstitute/cognitive-sovereignty/blob/main/taxonomy/manipulation-techniques.md)

Five universal social engineering signals:
1. Urgency without substantive justification
2. Authority claimed without verifiable identity
3. Unusual channel (contact through non-standard platform)
4. Too-good offer (guaranteed returns, early access, exclusive opportunity)
5. Incremental commitment escalation (small ask, then larger, then larger)

Any three present simultaneously = social engineering in progress. Disengage immediately. Do not resolve within the conversation: verify through independent channels.

---

### DECIDE: Execute Pre-Planned Response, No Improvisation Under Stress

The decision phase applies pre-planned playbooks. Under stress, cognitive function degrades significantly. Improvised decisions under physical or financial coercion have poor outcomes. Every scenario must have a pre-decided protocol.

**Incident Classification Matrix:**

| Threat ID Prefix | Incident Type | Playbook |
|-----------------|--------------|---------|
| CS-PHY-* | Physical coercion / surveillance | [Physical Coercion Response](playbooks/physical-coercion-response.md) |
| CS-WAL-* / CS-INS-* | Wallet compromise | [Wallet Compromise Response](playbooks/wallet-compromise-response.md) |
| CS-SOC-* / CS-MAL-* | Social engineering / malware | [Social Engineering Response](playbooks/social-engineering-response.md) |
| CS-DFI-* / CS-SC-* | Protocol or supply chain exploit | [Protocol Exploit Response](playbooks/protocol-exploit-response.md) |
| CS-AI-* | AI agent compromise | [AI Agent Response](playbooks/ai-agent-compromise-response.md): see also AI SAFE² |
| CS-FRD-* | Consumer fraud | [Consumer Fraud Response](playbooks/consumer-fraud-response.md) |

**Universal Decision Rules:**
- NEVER pay to unlock existing account balances (CS-FRD-01/02 confirmation signal)
- NEVER send crypto to a Bitcoin ATM on government/bank instruction (CS-FRD-03 absolute signal)
- NEVER engage a "recovery service" that proactively contacts you (CS-FRD-02 confirmation)
- ALWAYS move remaining funds to a pre-generated clean cold wallet before any public disclosure
- ALWAYS revoke all token approvals immediately upon any wallet compromise suspicion
- ALWAYS preserve evidence (transaction hashes, communications screenshots) before laundering window closes

---

### ACT: Execute Fast, Precisely, Irreversibly

The action phase is about speed and precision. The laundering window for most on-chain thefts is 15-60 minutes before funds reach mixers or cross-chain bridges. Freezes at CEX landing points require contact within minutes.

**Universal First Actions (any crypto incident):**
1. Revoke all token approvals: go.revoke.cash immediately
2. Move remaining assets to clean pre-generated cold wallet
3. Screenshot all on-chain evidence and communications
4. Record full transaction hashes and timestamps
5. Contact CSI's reporting stack (see below)

---

## Playbook 1: Physical Coercion / Wrench Attack Response

**Threat IDs:** CS-PHY-01, CS-PHY-02

**Pre-Incident (Must Be Set Up Before Need):**
- OPS-05: Written emergency response plan with trusted contact
- OPS-06: Coercion decoy wallet funded with visible but limited amount (e.g., $500-5,000)
- OPS-10: Pre-agreed duress signal: word, phrase, or action understood by trusted contact
- WKS-03: Time-locked primary holdings: cannot be transferred instantly even under coercion
- WKS-02: Multisig geographic diversity: no single location can provide enough keys

**During Incident:**
- Assess: Can you delay? Any signed transaction has a transmission step. Time delays activate timelocks.
- Decoy Wallet: Provide access to coercion wallet. Comply with visible holdings. Primary is inaccessible.
- Duress Signal: Activate with trusted contact per pre-agreed protocol. Do not make it obvious.
- Do Not Escalate: Physical safety is the priority. All crypto is replaceable. Lives are not.
- Document: If safely possible after the fact, document everything for law enforcement.

**Post-Incident:**
- Report to FBI (1-800-CALL-FBI) and local law enforcement immediately
- File with FBI IC3 (ic3.gov)
- Document all transaction hashes from coerced transfers
- Engage TRM Labs or Chainalysis if loss exceeds $10K (fund tracing)
- Conduct OSINT self-audit to understand how you were identified (close the exposure vector)
- Review and update OPS-01 through OPS-10 based on lessons learned

---

## Playbook 2: Wallet Compromise Response

**Threat IDs:** CS-WAL-01 through CS-WAL-05, CS-INS-01

**Observe Signals:**
- Alert: unexpected outgoing transaction
- Token approval granted to unknown contract
- Seed phrase requested by any application or contact
- Hardware wallet displaying different transaction than software

**Immediate Actions (first 15 minutes):**
1. Go to Revoke.cash: revoke ALL token approvals immediately
2. Open pre-generated clean cold wallet (not connected to any network or app)
3. Transfer all remaining assets to clean cold wallet
4. Do not attempt to recover from compromised device/wallet: it is burned

**Evidence Preservation:**
- Screenshot all recent transactions in your wallet explorer
- Record exact transaction hashes of any unauthorized outgoing transactions
- Note timestamps (UTC) of all suspicious activity
- Preserve any suspicious email, Discord, or X communications

**Attribution and Forensics:**
- Apply false flag filter before assigning cause
- For >$10K losses: contact TRM Labs (trmlabs.com/report) or Chainalysis
- Track fund movements using Etherscan/Solscan: identify CEX landing addresses
- Contact exchange compliance teams with transaction hashes if funds hit a CEX

**Reporting:**
- FBI IC3: ic3.gov (primary for all crypto theft)
- Chainabuse: chainabuse.com (submit all attacker wallet addresses)
- CFTC: if DeFi derivatives involved
- SEC: if securities fraud suspected

---

## Playbook 3: Social Engineering / Active Fraud Response

**Threat IDs:** CS-SOC-01 through CS-SOC-07, CS-FRD-01 through CS-FRD-04

**Recognition Triggers:**
- Any contact introducing investment opportunities via DM
- Request to install meeting software you did not initiate
- Any platform requesting fees to "unlock" existing withdrawals
- Unusual urgency around any financial action
- "Professor" or "investment group" introducing trading platform

**In-Progress Response:**
1. STOP: do not execute any further financial transactions
2. Exit the conversation: do not explain or negotiate
3. Do not pay any "unlock fee," "tax," "AML deposit," or "certification fee"
4. Do not install any application or software from the contact
5. Save all communications (screenshots) before exiting

**Post-Event:**
- CFD-01: Run platform through DFPI, CryptoScamDB, Chainabuse immediately
- If funds already sent: FBI IC3, DFPI (California residents), Chainabuse
- Apply false flag filter: who benefits from this specific scam architecture?
- Report typosquatted domains to CryptoScamDB for database inclusion
- For ongoing victim status: FBI Operation Level Up (proactive victim notification program)

**CSF Cognitive Recovery:**
Social engineering attacks exploit cognitive vulnerabilities including urgency, authority, and trust. Recovery includes cognitive decompression per [CSF Domain 3 (Emotional Resilience)](https://github.com/CyberStrategyInstitute/cognitive-sovereignty/tree/main/03-emotional). Do not make any financial decisions for 48-72 hours after a social engineering incident.

---

## Playbook 4: Protocol / Smart Contract Exploit Response

**Threat IDs:** CS-DFI-01 through CS-DFI-05, CS-SC-01 through CS-SC-04

**For Protocol Teams:**

**Immediate (0-60 minutes):**
1. Activate emergency pause function if available
2. Alert all signers simultaneously: do not wait for quorum
3. Deploy timelock override if admin key compromise suspected
4. Post public alert to all official channels (website, X, Discord): do not wait to understand full scope
5. Engage blockchain forensics: TRM Labs or Chainalysis within 30 minutes

**False Flag Assessment (run in parallel with containment):**
- Was any admin key, developer device, or privileged account involved?
- Was a code change deployed in the last 30-90 days?
- Were any new personnel onboarded in the last 6 months with admin access?
- Does any external actor benefit from this specific exploit design?

**Evidence Preservation:**
- All transaction hashes
- Tenderly simulation history from any recent governance transactions
- Git history for all code changes in the last 90 days
- Access logs for all admin/signing accounts

**Disclosure:**
- Publish transparent, factual incident report as soon as exploit is confirmed
- Do not speculate on attribution until forensic evidence is available
- Engage legal counsel before making liability statements
- Report to FBI, CISA if critical infrastructure implications

---

## Reporting Intelligence Stack

Every incident should feed back into the collective intelligence ecosystem. Your report protects the next victim.

| Report To | For | URL |
|-----------|-----|-----|
| FBI IC3 | All crypto theft, fraud, social engineering | ic3.gov |
| Chainabuse | All attacker wallet addresses | chainabuse.com |
| CryptoScamDB | Phishing URLs, fake exchange domains | cryptoscamdb.org |
| DFPI | California consumers: any fraudulent investment platform | dfpi.ca.gov/consumers/crypto/crypto-scam-tracker |
| CFTC Fraud | Commodity/derivatives fraud | cftc.gov/complaint |
| FBI (phone) | Physical threats, kidnapping, extortion | 1-800-CALL-FBI |
| CSI Weekly | Intelligence submissions for community coverage | cyberstrategyinstitute.com |
| Ethereum.org | Ethereum ecosystem-specific scams | ethereum.org/community/support/scams |

---

## OODA Loop Anti-Patterns

The following cognitive failure modes consistently appear in post-mortems across the CSI research corpus. Recognize and eliminate them.

| Anti-Pattern | Description | Correction |
|-------------|-------------|-----------|
| **Attribution Capture** | Accepting first-report attribution (DPRK, external hacker) without applying false flag filter | Run full false flag checklist before any public statement |
| **Urgency Compliance** | Taking financial action due to artificial time pressure | 48-hour no-action rule for any high-pressure financial request |
| **Sunk Cost Compliance** | Paying additional fees to recover already-lost funds | Fee demand = exit signal; all further payments increase losses |
| **Authority Submission** | Complying with requests from figures claiming government or platform authority | No government agency directs Bitcoin ATM transfers; no legitimate platform freezes withdrawals pending tax payment |
| **Recovery Hope Bias** | Engaging recovery services after primary loss | No blockchain transaction can be reversed; recovery service = second scam |
| **Partial Isolation** | Moving some funds to cold wallet but maintaining connections on hot wallet | Complete isolation: all approvals revoked, all funds moved, compromised wallet burned |
| **Premature Disclosure** | Discussing loss publicly before evidence is preserved | Preserve all evidence before any public disclosure; laundering window closes fast |

---

*CryptoSHIELD OODA Playbook | Cyber Strategy Institute | v1.1 | May 2026*
*Cross-reference: [AI SAFE² v3.0](https://github.com/CyberStrategyInstitute/ai-safe2-framework) for AI agent incident response*
*Cross-reference: [Cognitive Sovereignty Framework](https://github.com/CyberStrategyInstitute/cognitive-sovereignty) for cognitive manipulation defense*
