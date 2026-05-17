# CryptoSHIELD Sovereignty Self-Assessment

**CSI CryptoSHIELD Framework v1.1**
Cyber Strategy Institute | Open-Source | Sovereignty-First

**Version:** 1.0 | **Last Updated:** May 2026

---

> **How to use this assessment:**
> Work through each domain. Answer each question honestly: this assessment is for you alone. Mark each item: YES (full credit), PARTIAL (half credit), or NO (zero credit). Add up your domain scores, then total. Find your Sovereignty Tier. The gap analysis at the end tells you exactly where to spend your next hour.
>
> **Time required:** 45-60 minutes for first completion. 15-20 minutes for quarterly re-assessment.
>
> **No tooling required.** Every question is answerable from what you know right now. Where verification requires a tool, the tool is free and linked.

---

## Scoring Key

| Answer | Points | Meaning |
|---|---|---|
| **YES** | Full points | Control is fully implemented and you can verify it today |
| **PARTIAL** | Half points (round down) | Control is partially implemented or you are uncertain |
| **NO** | 0 points | Control is not implemented or definitively absent |

**Score each item before moving to the next domain.** Do not look ahead.

---

---

## DOMAIN 01: Wallet and Key Sovereignty
**Maximum: 20 points**

---

**WKS-01** *(3 pts)* My primary crypto holdings (any amount over $1,000) are stored on a hardware wallet purchased directly from the official manufacturer website (ledger.com, trezor.io, coldcard.com, or equivalent).

- [ ] YES (3): Hardware wallet purchased from official source, actively used for primary storage
- [ ] PARTIAL (1): Hardware wallet owned but some holdings >$1K remain in software wallets
- [ ] NO (0): No hardware wallet, or purchased through third-party seller

**Score:** ___

---

**WKS-02** *(3 pts)* For holdings above $50,000, I use a multisig arrangement (2-of-3 minimum) where the co-signers are physically located in separate cities or countries: not members of the same household.

- [ ] YES (3): Multisig active, signers verified to be geographically and physically independent
- [ ] PARTIAL (1): Multisig exists but signers share a location or household
- [ ] NO (0): No multisig for holdings >$50K, or holdings are below $50K (skip: score YES)

*Skip and score YES if total holdings are below $50,000.*

**Score:** ___

---

**WKS-03** *(2 pts)* Any wallet I use for governance or admin control of a protocol enforces a timelock before transactions execute (72 hours minimum for small protocols; 7 days for protocols with >$10M TVL).

- [ ] YES (2): Timelock is implemented and verified on-chain
- [ ] PARTIAL (1): Timelock exists but below minimum threshold for protocol size
- [ ] NO (0): No timelock, or no governance wallet (skip: score YES)

*Skip and score YES if you have no protocol governance role.*

**Score:** ___

---

**WKS-04** *(4 pts)* My seed phrase(s) are recorded on physical durable media (metal preferred; paper acceptable if fireproof/waterproof), stored in at least two separate physical locations, with zero digital copies anywhere: no photo, no note app, no password manager, no cloud storage.

- [ ] YES (4): Physical backup, two locations, zero digital copies confirmed
- [ ] PARTIAL (2): Physical backup exists but only one location, OR digital copy in a "secure" location
- [ ] NO (0): Seed phrase is digital, stored in a single location, or unknown status

**Score:** ___

---

**WKS-05** *(2 pts)* I never sign a transaction without independently verifying the destination address and transaction details on the hardware wallet screen: not just in the browser UI.

- [ ] YES (2): Always verify on hardware wallet screen before signing
- [ ] PARTIAL (1): Sometimes verify; sometimes trust the browser display
- [ ] NO (0): I sign based on browser display only

**Score:** ___

---

**WKS-07** *(3 pts)* I have audited my token approvals in the past 90 days (using revoke.cash or equivalent) and revoked all approvals for protocols I no longer actively use.

- [ ] YES (3): Audit completed within 90 days; stale approvals revoked (verify now at revoke.cash)
- [ ] PARTIAL (1): Audit done but more than 90 days ago, or some stale approvals remain
- [ ] NO (0): Never audited token approvals, or unsure what token approvals are

**Score:** ___

---

**WKS-09** *(3 pts)* 90% or more of my total crypto holdings (by value) are in cold storage (hardware wallet, not connected to any active session).

- [ ] YES (3): 90%+ in cold storage confirmed
- [ ] PARTIAL (1): 50-89% in cold storage
- [ ] NO (0): Less than 50% in cold storage

**Score:** ___

---

**Domain 01 Total: ___ / 20**

---

---

## DOMAIN 02: Endpoint and Device Defense
**Maximum: 15 points**

---

**EDD-01** *(4 pts)* The device(s) I use for crypto signing and DeFi interactions run kernel-level default-deny endpoint protection: not just antivirus: where unknown executables are contained before running.

- [ ] YES (4): Kernel-level containment (Xcitium/Warden class, or equivalent Zero Trust endpoint) confirmed active
- [ ] PARTIAL (2): Standard antivirus/EDR only; no kernel-level containment
- [ ] NO (0): No endpoint protection, or using standard consumer antivirus as primary defense

**Score:** ___

---

**EDD-02** *(4 pts)* I have a dedicated physical device used exclusively for crypto signing operations: no general browsing, email, social media, gaming, or general-purpose software on this device.

- [ ] YES (4): Dedicated signing device confirmed; no general use
- [ ] PARTIAL (2): Dedicated device exists but also used for some non-crypto activities
- [ ] NO (0): Crypto signing happens on my primary general-purpose device

**Score:** ___

---

**EDD-04** *(3 pts)* Before pasting any wallet address into a transaction field, I visually verify the first 6 and last 6 characters of the pasted address against what I intended to paste: every single time.

- [ ] YES (3): Consistent habit; always verify paste content
- [ ] PARTIAL (1): Sometimes verify; skip when "familiar" with the address
- [ ] NO (0): I paste addresses without verification, or do not know about clipboard hijacking

**Score:** ___

---

**EDD-05** *(2 pts)* I have audited the browser extensions on my crypto-adjacent devices within the past 90 days and removed all extensions that are not essential for crypto operations.

- [ ] YES (2): Audited within 90 days; non-essential extensions removed
- [ ] PARTIAL (1): Some extensions removed but audit not recent or thorough
- [ ] NO (0): No extension audit conducted

**Score:** ___

---

**EDD-10** *(2 pts)* On my signing device (or primary crypto device), only code-signed, verified applications are permitted to run. Application allowlisting is enforced at the OS level.

- [ ] YES (2): Allowlisting enforced (macOS Gatekeeper strict, Windows Defender Application Control, or equivalent)
- [ ] PARTIAL (1): Basic restrictions in place but not full allowlisting
- [ ] NO (0): Any software can run; no allowlisting

**Score:** ___

---

**Domain 02 Total: ___ / 15**

---

---

## DOMAIN 03: OPSEC and Physical Security
**Maximum: 15 points**

---

**OPS-01** *(3 pts)* I have never publicly posted or shared my crypto portfolio balance, specific holdings, or significant gains on any social media platform or public forum, and I have reviewed my existing posts for any such disclosures.

- [ ] YES (3): No public disclosures; past posts reviewed and cleaned
- [ ] PARTIAL (1): Some disclosures exist but I have limited them; older posts may remain
- [ ] NO (0): I have made public disclosures of holdings or gains; posts remain public

**Score:** ___

---

**OPS-02** *(2 pts)* None of my publicly used ENS names, social media handles, or forum usernames are directly linked to my real legal name or tied to wallet addresses containing significant holdings.

- [ ] YES (2): Clean separation: public identity is not linked to significant holdings addresses
- [ ] PARTIAL (1): Partial separation; some linkages exist but are not obvious
- [ ] NO (0): My real name or primary handle is directly linked to significant holdings on-chain

**Score:** ___

---

**OPS-04** *(2 pts)* I have conducted an OSINT self-audit within the past 6 months: searched my name plus "crypto," checked my handles on Etherscan/Arkham, and verified that my home address is not searchable through my crypto identity.

- [ ] YES (2): OSINT self-audit completed within 6 months; results reviewed
- [ ] PARTIAL (1): Partial audit only; some vectors not checked
- [ ] NO (0): No OSINT self-audit conducted

**Score:** ___

---

**OPS-05** *(4 pts)* I have a written or clearly defined physical incident response plan that covers: what to do if someone attempts to coerce a crypto transfer, who to contact, and how to buy time without surrendering primary holdings.

- [ ] YES (4): Plan is written, current, and covers all three elements
- [ ] PARTIAL (2): Plan exists mentally but not written, or missing one of the three elements
- [ ] NO (0): No plan exists

**Score:** ___

---

**OPS-06** *(2 pts)* I maintain a "coercion decoy" wallet: a wallet with a believable but sacrificial balance that I could surrender under physical duress without exposing primary holdings.

- [ ] YES (2): Decoy wallet funded and ready
- [ ] PARTIAL (1): Decoy wallet set up but balance is implausibly small or obviously empty
- [ ] NO (0): No decoy wallet

**Score:** ___

---

**OPS-10** *(2 pts)* I have established a duress protocol with a trusted contact: a pre-agreed signal (word, message pattern, or check-in failure) that triggers an emergency response on their end.

- [ ] YES (2): Protocol established, tested at least once, trusted contact confirmed
- [ ] PARTIAL (1): Protocol discussed but not formally established or tested
- [ ] NO (0): No duress protocol

**Score:** ___

---

**Domain 03 Total: ___ / 15**

---

---

## DOMAIN 04: Social Media and Platform Security
**Maximum: 15 points**

---

**SMS-01** *(3 pts)* All of my cryptocurrency exchange accounts AND my primary social media accounts (X, Discord, Telegram) use hardware security key 2FA (YubiKey, Google Titan, or equivalent FIDO2 device): not SMS 2FA, not authenticator app alone.

- [ ] YES (3): Hardware key on all exchanges and primary social accounts
- [ ] PARTIAL (1): Hardware key on some accounts; authenticator app on others; SMS 2FA eliminated
- [ ] NO (0): Using SMS 2FA on any account, or 2FA not enabled

**Score:** ___

---

**SMS-02** *(2 pts)* My phone number has been removed as a recovery method from all social media accounts (X, Discord, Telegram) and is not used as a 2FA method for any exchange or email account.

- [ ] YES (2): Phone number removed from all accounts; SMS 2FA eliminated everywhere
- [ ] PARTIAL (1): Phone removed from most but not all accounts
- [ ] NO (0): Phone number is still used as recovery or 2FA on any crypto-relevant account

**Score:** ___

---

**SMS-05** *(3 pts)* I never click links to access cryptocurrency platforms, DEXes, or DeFi protocols. I navigate exclusively by typing the URL directly or using bookmarks I created from a verified URL. This is a consistent, never-broken habit.

- [ ] YES (3): Consistent habit; bookmarks used; no link-clicking for crypto sites
- [ ] PARTIAL (1): Usually follow this rule but occasionally click links from trusted sources
- [ ] NO (0): I regularly click links to access crypto platforms

**Score:** ___

---

**SMS-12** *(3 pts)* Before depositing any amount into a new crypto platform or exchange, I verify it against at least two independent sources: DFPI Scam Tracker, CryptoScamDB, or Chainabuse.

- [ ] YES (3): Consistent verification before every new platform deposit
- [ ] PARTIAL (1): Sometimes verify; sometimes rely on reputation or recommendation alone
- [ ] NO (0): No pre-deposit verification conducted for new platforms

**Score:** ___

---

**SMS-14** *(4 pts)* I understand that any platform blocking my withdrawal and requiring a fee, tax, or "verification deposit" to unlock it is committing fraud: and I would stop all deposits immediately, document everything, and report to FBI IC3 rather than paying the fee.

- [ ] YES (4): Fully understand this pattern; would stop and report without paying
- [ ] PARTIAL (2): Understand conceptually but uncertain if I would resist under pressure
- [ ] NO (0): Did not know this, or would likely pay to try to recover funds

**Score:** ___

---

**Domain 04 Total: ___ / 15**

---

---

## DOMAIN 05: On-Chain Monitoring and Transaction Defense
**Maximum: 10 points**

---

**OCM-01** *(3 pts)* I treat transaction simulation as a mandatory gate before signing any DeFi transaction: not an optional check. If a transaction cannot be successfully simulated in Tenderly or equivalent, I do not sign it.

- [ ] YES (3): Mandatory gate discipline; no exceptions
- [ ] PARTIAL (1): Use simulation sometimes; skip for "familiar" transactions
- [ ] NO (0): Do not use transaction simulation

**Score:** ___

---

**OCM-02** *(2 pts)* I have active real-time wallet monitoring set up for all active wallets: email or push alerts trigger on any unexpected outgoing transaction.

- [ ] YES (2): Active alerts on all wallets with outgoing transaction notification
- [ ] PARTIAL (1): Alerts on some wallets; manually check others
- [ ] NO (0): No active wallet monitoring

**Score:** ___

---

**OCM-06** *(3 pts)* Before every outgoing transaction, I verify the full recipient address: not just the first and last four characters: on the hardware wallet screen or on a separate device. This is a consistent, never-broken habit.

- [ ] YES (3): Full address verification on hardware screen for every transaction
- [ ] PARTIAL (1): Verify first/last characters only, or verify most but not all transactions
- [ ] NO (0): Do not verify recipient address independently

**Score:** ___

---

**OCM-10** *(2 pts)* I never sign an `eth_sign` request. I understand `eth_sign` is deprecated and dangerous. For EIP-712 permit signatures, I verify the spender address and value before signing.

- [ ] YES (2): `eth_sign` is rejected on sight; EIP-712 parameters reviewed
- [ ] PARTIAL (1): Reject `eth_sign` but do not review EIP-712 parameters carefully
- [ ] NO (0): Did not know about `eth_sign` risk or sign without reviewing structured data

**Score:** ___

---

**Domain 05 Total: ___ / 10**

---

---

## DOMAIN 06: Supply Chain Defense
**Maximum: 10 points** *(Primarily for developers and protocol teams: individual holders: see note)*

> **Individual holder note:** If you do not write or maintain code, score WKS-01 and EDD-01 as your primary supply chain defense and skip Domains 06-07. Score this domain at 10/10 if you are purely a crypto user with no development role.

---

**SCD-01** *(3 pts)* Every production repository I maintain includes a current SBOM (Software Bill of Materials), generated on every build, and scanned against vulnerability databases before deployment.

- [ ] YES (3): SBOM in CI/CD pipeline, current, scanned
- [ ] PARTIAL (1): SBOM exists but not generated automatically or not scanned
- [ ] NO (0): No SBOM for production code

**Score:** ___

---

**SCD-03** *(3 pts)* No production signing keys, API secrets, or contract admin keys exist in my CI/CD environment. All production secrets are accessed via a vault with ephemeral tokens.

- [ ] YES (3): Secrets in vault; ephemeral tokens; no hardcoded secrets in CI/CD confirmed
- [ ] PARTIAL (1): Most secrets in vault; some legacy hardcoded secrets remain
- [ ] NO (0): Production secrets in environment variables or repository

**Score:** ___

---

**SCD-07** *(2 pts)* All production package dependencies are version-pinned (exact versions, not ranges), `package-lock.json` or equivalent is committed to version control, and CI/CD uses `npm ci` (not `npm install`).

- [ ] YES (2): Exact pinning, lock file committed, `npm ci` in pipeline
- [ ] PARTIAL (1): Partial pinning; ranges still used for some dependencies
- [ ] NO (0): Version ranges throughout; no consistent pinning

**Score:** ___

---

**SCD-09** *(2 pts)* Post-install hooks are blocked globally via `.npmrc` policy (`ignore-scripts=true`). Exceptions for known build-required packages are explicitly allowlisted and reviewed.

- [ ] YES (2): Global `.npmrc` policy confirmed; exceptions documented
- [ ] PARTIAL (1): Using `--ignore-scripts` flag sometimes but not global policy
- [ ] NO (0): Install hooks run by default

**Score:** ___

---

**Domain 06 Total: ___ / 10**

---

---

## DOMAIN 09: Consumer Fraud Defense
**Maximum: 15 points**

*(This domain is for all participants: individual holders and developers.)*

---

**CFD-01** *(4 pts)* I have never deposited funds into a platform I found through an unsolicited message (DM, email, text, dating app, social media ad), no matter how convincing the recommendation or how profitable the returns appeared.

- [ ] YES (4): Never acted on an unsolicited investment recommendation
- [ ] PARTIAL (2): Have investigated such recommendations but have not deposited
- [ ] NO (0): Have deposited into a platform found through unsolicited contact

**Score:** ___

---

**CFD-02** *(3 pts)* I know that any platform blocking my withdrawal and requesting a fee: called a "tax," "AML verification," "risk deposit," "account certification," or any other name: is fraud, and I would report it immediately to FBI IC3 (ic3.gov) without paying.

- [ ] YES (3): Know the pattern cold; would stop and report
- [ ] PARTIAL (1): Know it exists but uncertain about my response under pressure
- [ ] NO (0): Did not know this or would likely pay

**Score:** ___

---

**CFD-03** *(3 pts)* I know that no legitimate service can reverse a blockchain transaction: and that any "recovery specialist" contacting me after a loss who claims they can recover my funds for a fee is running a secondary scam.

- [ ] YES (3): Know this clearly; would not engage any recovery service
- [ ] PARTIAL (1): Know in principle but might investigate a compelling recovery offer
- [ ] NO (0): Did not know blockchain transactions are irreversible or recovery services are fraudulent

**Score:** ___

---

**CFD-04** *(3 pts)* I know that government officials, utility companies, law enforcement, and financial institutions never request cryptocurrency payments: and that any such request is always fraud.

- [ ] YES (3): Know this clearly; would immediately hang up or close communication
- [ ] PARTIAL (1): Know in principle but might hesitate under authority pressure
- [ ] NO (0): Did not know this

**Score:** ___

---

**CFD-05** *(2 pts)* I have briefed at least one family member (parent, grandparent, spouse, sibling) on the basic patterns of crypto fraud: specifically: no one ever needs cryptocurrency to pay a fine, tax, or emergency fee.

- [ ] YES (2): At least one family member briefed on core fraud patterns
- [ ] PARTIAL (1): Mentioned it but not a full briefing
- [ ] NO (0): No family briefing on crypto fraud

**Score:** ___

---

**Domain 09 Total: ___ / 15**

---

---

## TOTAL SOVEREIGNTY SCORE

| Domain | Score | Maximum |
|---|---|---|
| Domain 01: Wallet and Key Sovereignty | ___ | 20 |
| Domain 02: Endpoint and Device Defense | ___ | 15 |
| Domain 03: OPSEC and Physical Security | ___ | 15 |
| Domain 04: Social Media and Platform Security | ___ | 15 |
| Domain 05: On-Chain Monitoring | ___ | 10 |
| Domain 06: Supply Chain Defense | ___ | 10 |
| Domain 09: Consumer Fraud Defense | ___ | 15 |
| **TOTAL** | **___** | **100** |

---

## Sovereignty Tier Classification

| Score | Tier | Status |
|---|---|---|
| 0-24 | **EXPOSURE RISK** | Critical vulnerabilities present. Stop reading. Execute Week 1 of the 30-Day Sprint now. |
| 25-49 | **HARDENING IN PROGRESS** | Foundational controls partially in place. Priority: close Domain 01 and 04 gaps immediately. |
| 50-69 | **HARDENED** | Core posture established. Focus: close partial gaps; establish monitoring and physical OPSEC. |
| 70-84 | **SOVEREIGN** | Strong defense posture. Maintain quarterly review. Consider contributing to the framework. |
| 85-100 | **MISSION-READY** | Exceptional posture. You are the trusted contact for others. Share the framework. |

**Your Tier:** ___________________

---

## Gap Analysis: Where to Spend Your Next Hour

Review your NO and PARTIAL answers. Prioritize by:

**Highest-impact items first (any NO on these = fix today):**
1. WKS-04 (seed phrase): if NO: everything else is irrelevant
2. SMS-14 (fee demand recognition): if NO: you are a primary fraud target
3. OPS-05 (physical incident plan): if NO: physical threat has no response
4. EDD-02 (dedicated signing device): if NO: malware can reach your signing sessions
5. WKS-09 (cold storage 90%): if NO: holdings are unnecessarily hot

**Next priority (PARTIAL → YES within 30 days):**
- WKS-07 (token approval audit): free, 30 minutes at revoke.cash
- SMS-01 (hardware 2FA): $25-$50 investment; most impactful per dollar spent
- OCM-01 (simulation gate discipline): habit change, no cost
- OPS-04 (OSINT self-audit): 1-2 hours; free

**30-Day implementation roadmap:** [tools/30-day-hardening-sprint.md](../tools/30-day-hardening-sprint.md)

---

## Quarterly Re-Assessment Protocol

Run this assessment every 90 days. Track your score progression:

| Date | Score | Tier | Key Gap Closed |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

**Target:** Move up one tier per 90-day cycle until Sovereign (70+).

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | May 2026 | Initial release: 100-point instrument, 7 domains, 4 tiers |

---

*CryptoSHIELD Sovereignty Self-Assessment v1.0*
*Cyber Strategy Institute | Open-Source | CC-BY-SA 4.0*
*github.com/CyberStrategyInstitute/crypto-shield*
