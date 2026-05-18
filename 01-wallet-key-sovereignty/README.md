<div align="center">

<img src="../assets/Domain 01 Wallet and Key Sovereignty (WKS).png" alt="Domain 01 Wallet and Key Sovereignty (WKS)" width="100%" />
</div>

# Domain 01: Wallet and Key Sovereignty (WKS)

**CSI CryptoSHIELD Framework v1.1 | May 2026**

---

## Philosophy

> Not your keys. Not your crypto. Full stop.

Every other security domain in CryptoSHIELD supports this one. The endpoint can be perfectly hardened. The OPSEC can be flawless. The supply chain can be fully verified. None of it matters if your seed phrase is in a cloud note, your hardware wallet is the only one on a 2-of-3 multisig, or you are signing transactions you cannot independently verify.

Wallet and key sovereignty is the terminal defense. If this layer fails, nothing else saves you.

---

## Controls

### WKS-01: Hardware Wallet for All Holdings Above $1,000

**Priority:** CRITICAL
**Threat IDs:** CS-WAL-01, CS-WAL-04

**Implementation:**
- Ledger, Trezor, or Coldcard for all holdings exceeding $1,000 USD equivalent
- Hardware wallet must be purchased directly from manufacturer: never secondhand or through marketplace resellers
- Verify firmware authenticity on first connection (manufacturer verification protocol)
- Enable PIN with sufficient entropy (8+ characters, not birthday or sequential)

**Why this matters:** Software wallets on internet-connected devices expose private keys to any malware with memory access. Hardware wallets maintain the private key in isolated secure element storage that never exposes the key to the connected machine: the transaction is signed inside the hardware and only the signature (not the key) is transmitted.

**Edge case:** Hardware wallets are physical objects that can be physically seized. WKS-01 solves the digital attack surface but increases physical coercion risk if holdings are visible. Pair with OPS-01 and OPS-06.

---

### WKS-02: Multisig with Geographic Diversity

**Priority:** CRITICAL
**Threat IDs:** CS-INS-01, CS-DFI-01

**Implementation:**
- Minimum 2-of-3 multisig for holdings above $50,000
- Signers must be in physically separate locations: not the same building, city, or household
- At least one signer should be jurisdictionally separate (different country preferred for large holdings)
- Hardware wallets used for all signing positions: no software-only signers

**The multisig masquerade failure mode:** WKS-02 is not sufficient alone if all three devices are on the same network or reachable through the same social engineering campaign. The Radiant Capital exploit (three developers, same Telegram social engineering campaign, all compromised) demonstrates that geographic diversity of hardware is not geographic diversity of trust if all signers share the same communication channels.

**Correct implementation:** Geographic diversity + communication channel diversity + independent verification on separate devices (WKS-05).

---

### WKS-03: Tiered Timelock on Governance Transactions

**Priority:** CRITICAL
**Threat IDs:** CS-DFI-01, CS-INS-01, CS-AI-04

**Implementation: Tiered by Protocol TVL:**

| Protocol Size | Minimum Timelock | Rationale |
|---|---|---|
| Individual governance wallet | 72 hours | Baseline detection window for personal transactions |
| Protocol TVL $0-$10M | 72 hours | Standard: covers most monitoring cycles and time zones |
| Protocol TVL $10M-$100M | 7 days | Extended window for community review of material changes |
| Protocol TVL >$100M | 14 days | Full governance cycle; mandatory community vote period |

The 72-hour baseline is not sufficient for major protocols. The Euler Finance governance (2023) and several 2025 incidents demonstrated that community-identified threats require multiple days of communication, coordination, and legal review before a response can mobilize. A 72-hour window at $100M TVL gives attackers who discover the pending transaction 72 hours to front-run or counter: not 72 hours for defenders to respond.

**Additional requirements:**
- Timelock smart contracts must be audited and independently deployed
- No timelock override capability except through a separate N-of-M key ceremony with quorum requirements exceeding the standard signing threshold
- Timelock events must trigger automated alerts to all stakeholders with sufficient detail to evaluate the pending action
- Every queued transaction should be publicly verifiable on-chain before execution

**Why this exists:** Retrospective application of WKS-03 to the 10 largest DeFi exploits in 2024-2025 shows that 7 of 10 would have been either prevented or significantly mitigated by a protocol-appropriate timelock: including Radiant Capital, LNDFi, and multiple admin key drains. In each case, the malicious or negligent action completed in minutes. The window to detect and stop it: zero.

---

### WKS-04: Seed Phrase Offline Sovereignty

**Priority:** CRITICAL
**Threat IDs:** CS-WAL-01

**Implementation:**
- Seed phrase must be recorded on durable physical media: engraved metal (Cryptosteel, Billodr, or equivalent) is preferred over paper
- No digital copy ever: no photograph, no note, no cloud storage, no email, no password manager
- Seed phrase must be stored in at least two separate physical locations with access controls (fireproof safe, safety deposit box, trusted custodian arrangement)
- Split the seed phrase across locations using Shamir's Secret Sharing or geographic distribution if holdings are significant

**What kills this control:**
- Photographing seed phrase during setup (cloud photo sync catches this)
- Typing seed phrase into any application claiming to "verify" or "check" it (any such application is a scam)
- Storing seed phrase in a password manager (password managers are high-value attack targets)
- Telling any other person the seed phrase

**Absolute rule:** No legitimate hardware wallet, exchange, or application will ever ask you to enter your seed phrase after initial setup. Any request for seed phrase entry is an attack.

---

### WKS-05: No Blind Signing

**Priority:** CRITICAL
**Threat IDs:** CS-WAL-04, CS-INS-01

**Implementation:**
- Verify the raw transaction payload independently before signing: not just the UI display
- Use Tenderly, Etherscan transaction decoder, or equivalent to decode the actual calldata before signing
- Verify: contract address, function being called, parameters, value being transferred
- For protocol governance transactions: match transaction hash against what was proposed in governance forum

**The Safe{Wallet} display manipulation:** The Radiant Capital exploit succeeded because attackers manipulated what the Safe{Wallet} interface displayed while the underlying malicious transaction was what actually got signed. Independent verification on a separate, clean device would have caught the discrepancy.

**Practice drill:** Before signing any transaction over $1,000 in value, decode it on a device that was not used to generate the transaction request. The values must match exactly.

---

### WKS-06: Independent Address Verification Protocol

**Priority:** HIGH
**Threat IDs:** CS-WAL-02, CS-WAL-03

**Implementation:**
- Cross-check receiving address on an independent device before every outgoing transaction
- Never rely solely on the device that generated the transaction request to verify the address
- For large transactions (>$10,000): verify full address character by character, not just first/last 4-6 characters
- Verify address on the hardware wallet's own screen before confirming: the screen on the hardware wallet cannot be spoofed by computer malware

**Address poisoning defense:** Attackers generate vanity addresses that match the first 4 and last 4 characters of your frequently-used receiving addresses, then send dust to create the poisoned address in your transaction history. Copy-pasting from history instead of full character verification is the failure mode.

---

### WKS-07: Token Approval Revocation Protocol

**Priority:** HIGH
**Threat IDs:** CS-WAL-04

**Implementation:**
- Monthly audit of all token approvals on all active wallet addresses using Revoke.cash or equivalent
- Revoke all approvals that are not actively required
- After any DeFi interaction with an unfamiliar protocol: immediate approval revocation as final step
- Set a calendar reminder: first day of each month, approval audit and revocation session

**Why this matters:** ERC-20 approvals are persistent: an approval granted to a contract remains valid indefinitely unless explicitly revoked. A protocol that is later exploited or compromised can drain your wallet through a previously granted approval even if you have not interacted with it in months.

---

### WKS-08: Permit Scam Recognition

**Priority:** HIGH
**Threat IDs:** CS-WAL-04

**Implementation:**
- Never sign an EIP-2612 "permit" request from an unsolicited source
- Understand that permit signatures are off-chain signatures that grant the same authority as on-chain approvals but do not show up in the approval history visible on Revoke.cash until used
- When interacting with unfamiliar protocols, explicitly check whether any permit signature is requested
- If unsure about any signature request: reject, research the protocol independently, then return if legitimate

**The permit scam kill chain:**
1. User visits legitimate-looking site (often via typosquatted URL or compromised DNS)
2. Site requests an off-chain EIP-2612 permit signature (appears harmless: no gas required)
3. Attacker holds the signature
4. Attacker submits the permit on-chain when ready, granting themselves spend authority
5. Token drain executed

---

### WKS-09: Cold Wallet for 90%+ of Holdings

**Priority:** CRITICAL
**Threat IDs:** CS-WAL-01, CS-MAL-02

**Implementation:**
- Maintain maximum 10% of total holdings in any hot wallet (actively connected to internet/applications)
- Hot wallet holding should be limited to amounts needed for active DeFi participation
- Cold wallet: hardware wallet + seed phrase metal backup + air gap or minimal connectivity
- Regular rebalancing: if hot wallet grows beyond 10% threshold through trading profits, rebalance to cold storage

**Operational discipline:** The 90/10 rule contains the blast radius. If a hot wallet is compromised through any attack vector, maximum loss is bounded at 10% of total holdings.

---

### WKS-10: Watch-Only Wallet for Household Members

**Priority:** HIGH
**Threat IDs:** CS-PHY-01, CS-SOC-01

**Implementation:**
- Create watch-only wallet configurations for family members who need to monitor holdings (estate planning, shared finances)
- Watch-only wallets have viewing capability only: no signing capability
- Household members with watch-only access should not be aware of full key management structure
- Under OPS-07 (Family OPSEC): family members' knowledge of holdings should be need-to-know

**Physical coercion consideration:** Under coercion, attackers may target family members as leverage. If family members cannot sign transactions, they cannot be coerced into executing transfers. WKS-10 + OPS-07 provide structural protection against this attack vector.

---

## Domain 01 Threat Coverage Matrix

| Threat ID | Threat Name | Controlling WKS Controls |
|-----------|-------------|--------------------------|
| CS-WAL-01 | Seed Phrase Extraction | WKS-01, WKS-04, WKS-09 |
| CS-WAL-02 | Address Poisoning | WKS-06 |
| CS-WAL-03 | DNS Hijack / Frontend Compromise | WKS-05 |
| CS-WAL-04 | Malicious Signature / Permit Drain | WKS-05, WKS-07, WKS-08 |
| CS-WAL-05 | Low Entropy Seed Generation | WKS-01 |
| CS-INS-01 | Admin Key Abuse | WKS-02, WKS-03, WKS-05 |
| CS-DFI-01 | Admin Key Exploit | WKS-02, WKS-03 |
| CS-PHY-01 | Physical Coercion | WKS-03, WKS-09 (limits accessible holdings) |

---

## 30-Day WKS Hardening Sprint

**Week 1:**
- [ ] Purchase hardware wallet from manufacturer directly (WKS-01)
- [ ] Generate seed phrase on offline device and record on metal backup (WKS-04)
- [ ] Transfer all holdings exceeding $1,000 to hardware wallet cold storage (WKS-09)
- [ ] Run Revoke.cash audit on all existing wallet addresses (WKS-07)

**Week 2:**
- [ ] Set up 2-of-3 multisig with geographic diversity for holdings >$50K (WKS-02)
- [ ] Practice WKS-05: decode a transaction before signing (practice run with small amount)
- [ ] Enable 72-hour timelock on any protocol governance involvement (WKS-03)

**Week 3-4:**
- [ ] Establish monthly calendar reminder for approval revocation (WKS-07)
- [ ] Set up watch-only wallet for relevant family members (WKS-10)
- [ ] Verify: seed phrase exists on metal in two separate locations (WKS-04)

---

*Domain 01: Wallet and Key Sovereignty | CryptoSHIELD v1.1*
*Threat taxonomy: [../taxonomy/registry.json](../taxonomy/registry.json)*
*Related domains: [../02-endpoint-device-defense/](../02-endpoint-device-defense/) | [../03-opsec-physical-security/](../03-opsec-physical-security/)*
