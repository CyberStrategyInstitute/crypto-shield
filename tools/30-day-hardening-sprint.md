# Tool: 30-Day Sovereignty Hardening Sprint

**CSI CryptoSHIELD Framework v1.1**
A prescriptive, time-boxed implementation plan for individual crypto holders.

---

## Who This Is For

Any individual holding more than $5,000 in crypto who has not systematically implemented security controls. Complete all four weeks in sequence. Do not skip weeks: each builds on the previous.

**Time commitment:** 2-4 hours per week.
**Prerequisite:** A hardware wallet. If you don't have one, buy one (Ledger or Trezor from the official vendor only, never third-party sellers) before starting Week 1.

---

## Week 1: Wallet Sovereignty

**Goal:** Your keys. Your crypto. No exceptions.

**Day 1-2: Hardware Wallet Setup**
- [ ] Purchase hardware wallet from official vendor only (ledger.com, trezor.io, coldcard.com)
- [ ] Initialize on a dedicated device (not your primary computer if possible)
- [ ] Generate new seed phrase on device; never digitize it
- [ ] Record seed phrase on metal backup (Cryptosteel, Bilodeau, or equivalent)
- [ ] Verify: can you recover from seed phrase alone? Test on a second device.

**Day 3-4: Cold Storage Migration**
- [ ] Move 90%+ of holdings to hardware wallet cold storage (WKS-09)
- [ ] For holdings >$50,000: set up 2-of-3 multisig with a co-signer in a different city (WKS-02)
- [ ] Leave only a transactional float (10% maximum) in hot wallets

**Day 5-6: Token Approval Audit**
- [ ] Go to revoke.cash
- [ ] Connect each of your active wallets
- [ ] Revoke all approvals for protocols you no longer actively use (WKS-07)
- [ ] Document: what remains approved? Why?

**Day 7: Timelock and Governance**
- [ ] If you control any protocol governance wallet: implement 72-hour timelock on all admin transactions (WKS-03)
- [ ] Review: does any wallet have an "unlimited" approval outstanding? Revoke and replace with specific amount.

**Week 1 Sovereignty Score:** Count checked boxes / 10 = ___

---

## Week 2: Device and Endpoint Defense

**Goal:** Zero unknown code runs on any device that touches crypto.

**Day 8-9: Dedicated Device Setup**
- [ ] Designate one device exclusively for crypto signing (no gaming, no browsing, no social media) (EDD-02)
- [ ] Fresh OS install on dedicated device if possible
- [ ] Install ONLY: hardware wallet companion app (official), browser for DEX (hardened), no extensions

**Day 10-11: Endpoint Hardening**
- [ ] Install kernel-level Zero Trust endpoint protection (Xcitium/Warden model) on primary devices (EDD-01)
- [ ] Audit browser extensions on all devices: remove all non-essential extensions (EDD-05)
- [ ] Enable clipboard verification habit: before pasting any wallet address, verify it matches what you copied (EDD-04)

**Day 12-13: Software Hygiene**
- [ ] Audit all software installed on crypto-adjacent devices
- [ ] Remove pirated software and any software from non-official sources (EDD-03)
- [ ] For developers: run `npm audit` on all crypto-related projects; check SBOM (SCD-01)

**Day 14: Network Isolation**
- [ ] For large transactions: configure Flashbots Protect RPC in MetaMask (OCM-04)
- [ ] For signing device: consider dedicated network VLAN or air-gap mode during signing sessions (EDD-08)

**Week 2 Sovereignty Score:** Count checked boxes / 8 = ___

---

## Week 3: Social and Physical OPSEC

**Goal:** Your digital footprint does not lead to your front door.

**Day 15-16: Social Media Hardening**
- [ ] X: Remove phone number; enable hardware 2FA (YubiKey) (SMS-01, SMS-02)
- [ ] Discord: Enable TOTP 2FA; remove phone number (SMS-01)
- [ ] Telegram: Enable Two-Step Verification; set phone number privacy to "Nobody" (SMS-02)
- [ ] All exchanges: enable hardware 2FA (SMS-01)
- [ ] Monthly OAuth audit: revoke non-essential connected apps on all accounts (SMS-03)
- [ ] Set up dedicated recovery email for all crypto accounts (SMS-04)

**Day 17-18: Identity Decoupling**
- [ ] Audit: are any of your wallet addresses publicly linked to your real name or primary handle?
- [ ] Remove or archive any public posts showing portfolio balances, gains, or specific holdings (OPS-01)
- [ ] Check ENS names: any tied to your real name? (OPS-02)
- [ ] Conduct OSINT self-audit (see tools/osint-self-audit-checklist.md) (OPS-04)

**Day 19-20: Physical Incident Plan**
- [ ] Fund decoy wallet with believable balance (OPS-06)
- [ ] Write your physical incident response plan (OPS-05): what do you do if coerced?
- [ ] Brief family members on basic OPSEC: what they should/should not say (OPS-07)
- [ ] Establish trusted contact with daily check-in protocol (OPS-10)
- [ ] Save FBI field office number and local cyber crime unit number

**Day 21: Geolocation Audit**
- [ ] Install ExifTool; audit recent photos for geolocation data
- [ ] Disable location services on all crypto apps (OPS-08)
- [ ] Check Telegram: is location sharing on? Disable.

**Week 3 Sovereignty Score:** Count checked boxes / 12 = ___

---

## Week 4: Monitoring and Intelligence

**Goal:** Full visibility; no surprises.

**Day 22-23: Wallet Monitoring**
- [ ] Set up Etherscan email alerts for all active wallets (OCM-02)
- [ ] Add wallet monitoring via Nansen, Hal.app, or equivalent
- [ ] Test: send small transaction; confirm alert arrives within 5 minutes

**Day 24-25: Transaction Defense**
- [ ] Test Tenderly simulation: simulate any transaction you've done recently (OCM-01)
- [ ] Add Flashbots Protect RPC as a network in MetaMask (OCM-04)
- [ ] Install and test Scam Sniffer browser extension (SMS-09)
- [ ] Set bookmarks for all crypto platforms you use; delete or ignore all non-bookmarked links

**Day 26-27: Intelligence Subscriptions**
- [ ] Subscribe to CSI Weekly Digest (cyberstrategyinstitute.com)
- [ ] Follow ZachXBT, Scam Sniffer, CertiK Skynet on X
- [ ] Set up Google Alerts: [your name + crypto], [your primary protocols + hack], [DPRK crypto]
- [ ] Bookmark: ic3.gov, chainabuse.com, revoke.cash, dfpi.ca.gov/consumers/crypto

**Day 28-30: Review and Test**
- [ ] Review all four weeks: any gaps?
- [ ] Run OSINT self-audit one more time with fresh eyes
- [ ] Test your incident response plan mentally: what would you do if your phone showed $50K leaving your wallet right now?
- [ ] Schedule: calendar the next quarterly OSINT self-audit and token approval audit

**Week 4 Sovereignty Score:** Count checked boxes / 10 = ___

---

## Sovereignty Tier Assessment

Add up all checked boxes across four weeks (max: 40):

| Score | Tier | Assessment |
|---|---|---|
| 0-15 | Exposure Risk | Significant vulnerabilities; prioritize Week 1-2 immediately |
| 16-25 | Hardened | Core defenses in place; complete remaining controls |
| 26-33 | Sovereign | Strong posture; maintain quarterly review cycle |
| 34-40 | Mission-Ready | Full implementation; contribute to community |

**Your Score:** ___ / 40 | **Tier:** ___

---

*Tool: 30-Day Sovereignty Hardening Sprint | CSI CryptoSHIELD Framework v1.1*
*Cyber Strategy Institute | Open-Source*
