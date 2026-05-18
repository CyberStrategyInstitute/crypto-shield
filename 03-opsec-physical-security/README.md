<div align="center">

<img src="assets/Domain 03 OPSEC and Physical Security (OPS).png" alt="Domain 03 OPSEC and Physical Security (OPS)" width="100%" />
</div>


# Domain 03: OPSEC and Physical Security (OPS)

**CSI CryptoSHIELD Framework v1.1**
Cyber Strategy Institute | Classification: Open-Source | Sovereignty-First

---

## Domain Philosophy

Your on-chain signature is invisible. Your physical presence is not.

The most technically sophisticated wallet setup in the world is neutralized by a wrench, a zip-tie, and thirty seconds of access to the wrong person. Domain 03 treats physical OPSEC as a first-class security domain: not an afterthought. If you are publicly identifiable as a crypto holder, you are a target for the fastest, most reliable attack vector in 2025: your own body under coercion.

CertiK documented 72 verified physical coercion incidents in 2025. Losses: $40.9 million. Trajectory: +75% year-over-year. The attack pattern is consistent: OSINT → Identity Mapping → Physical Surveillance → Coercion. Every step of that chain is preventable. None of it requires defeating cryptography.

**CSI Position:** Operational security is not paranoia. It is the minimum viable defense posture for anyone holding material crypto wealth.

---

## Controls

| Control ID | Control | Implementation | Priority |
|---|---|---|---|
| OPS-01 | Zero Public Disclosure of Holdings | Never post wallet balances, gains, or luxury flex tied to crypto identity | CRITICAL |
| OPS-02 | Decouple Identity from On-Chain | No ENS names tied to real name; separate social identity from wallet addresses | CRITICAL |
| OPS-03 | Address Non-Reuse | Generate new receiving address for every transaction | HIGH |
| OPS-04 | OSINT Self-Audit | Quarterly: remove identifiable geotags, home references, employer information | HIGH |
| OPS-05 | Physical Incident Response Plan | Pre-scripted emergency plan; trusted contact; know when to delay vs. comply | CRITICAL |
| OPS-06 | Coercion Wallet (Decoy Wallet) | Maintain a visible wallet with small balance as coercion decoy; bulk held in inaccessible timelock | HIGH |
| OPS-07 | Family OPSEC | Separate accounts, devices; limited family knowledge of full holdings structure | CRITICAL |
| OPS-08 | Geolocation Hygiene | Strip EXIF from photos; disable location services on all crypto-related apps | HIGH |
| OPS-09 | Surveillance Detection | Know surveillance indicator patterns; vary routes; report unusual attention | MEDIUM |
| OPS-10 | Duress Protocol | Pre-agreed distress signal to trusted contact if under physical coercion | HIGH |

---

## Control Implementation Detail

### OPS-01: Zero Public Disclosure of Holdings

**Problem:** Social media posts displaying hardware wallets, screenshots of portfolio balances, mentions of specific token positions, or luxury purchases funded by crypto gains create an OSINT trail linking a real-world identity to crypto wealth.

**Realization:** The September 2025 Minnesota kidnapping ($8M coerced transfer) was preceded by OSINT surveillance linking on-chain wallet activity to a physical address. The attacker required no technical capability: only public data.

**Implementation:**
- Apply the "Would I post my bank balance?" test before any crypto-adjacent social post
- Remove or audit existing posts containing wallet screenshots, gains, or luxury purchases linked to crypto narrative
- Use separate social accounts for crypto discussion; never tie to legal name or photo
- Treat all media appearances discussing crypto wealth with operational caution: use rounded figures, avoid specific holdings, decline to disclose wallet addresses

**Failure Modes:**
- "Flexing" on CT (Crypto Twitter) with paper gains
- ENS names that match your legal name or known handle (e.g., vince.eth)
- LinkedIn describing yourself as "profitable DeFi investor since 2020"
- Posting hardware wallet unboxing photos showing your home or purchase history

---

### OPS-02: Decouple Identity from On-Chain

**Problem:** ENS names, on-chain donations, public wallet addresses used for business payments, and forum handle → wallet linkages allow any attacker to map your on-chain wealth to your physical identity.

**Implementation:**
- Use different wallets for different contexts: trading wallet, NFT wallet, public-facing tip wallet, primary cold storage (never publicized)
- Never register an ENS name under your real name or primary social handle
- For public tips/donations: use a dedicated, low-balance hot wallet specifically for public receipt; never the same wallet holding significant assets
- Rotate public-facing addresses annually at minimum

**Edge Case:** Blockchain analytics firms (Chainalysis, TRM Labs) can link wallets with high confidence through co-spend analysis. True identity decoupling requires discipline from first transaction: retroactive unlinking is difficult and often incomplete.

---

### OPS-03: Address Non-Reuse

**Problem:** Address reuse creates a permanent, searchable on-chain history that links all your transactions to a single identity node. OSINT tools like Etherscan, Arkham, and Nansen build "address intelligence" profiles from reuse patterns.

**Implementation:**
- Modern HD wallets (BIP32/44) generate unique addresses for every receive operation: use this feature
- Never publish your "primary" address anywhere; provide fresh addresses per requestor
- For DeFi interactions: use interaction wallets funded from cold storage; don't interact directly from cold storage
- Monitor your addresses with a privacy-oriented analytics tool to understand what your on-chain footprint reveals

---

### OPS-04: OSINT Self-Audit

**Problem:** Most crypto holders have already created an OSINT footprint that an attacker can leverage. The audit is not about perfection: it is about reducing the attack surface.

**Quarterly Audit Checklist:**
- [ ] Google your legal name + "crypto": what surfaces?
- [ ] Search your primary social handles on Etherscan/Arkham: any wallet linkages?
- [ ] Check LinkedIn for mentions of crypto holdings, specific protocols, or investment success
- [ ] Review forum posts (Reddit, Discord, Telegram) for wallet address mentions
- [ ] Audit EXIF data on publicly posted photos: strip geolocation data
- [ ] Search your home address on property records: is it connectable to your crypto identity?
- [ ] Review exchange KYC data exposure: which platforms hold your government ID?

**Tools:** HaveIBeenPwned (data breach exposure), IntelTechniques (manual OSINT), Google Alerts (ongoing monitoring)

---

### OPS-05: Physical Incident Response Plan

**Problem:** Physical coercion situations are high-stress, rapid-onset events. Anyone who has not pre-planned their response will improvise: and improvisation under duress leads to full asset surrender.

**Pre-Plan Components:**
1. **Decoy wallet** with convincing balance (OPS-06): your primary "surrender" option
2. **Trusted contact** who receives a daily check-in; non-check-in triggers a response protocol
3. **Delay tactics**: claim device is in a timelock, claim 2FA is on a separate device at a distant location, claim hardware wallet requires 24-hour warm-up period after 30 days
4. **Geographic split**: primary holdings physically inaccessible from your location (multisig keys with geographically separate co-signers; WKS-02)
5. **Law enforcement contact info**: FBI Crypto Unit, local cyber crime unit

**The Fundamental Principle:** Holdings that cannot be transferred without a co-signer in another city cannot be coerced from you. This is the most effective physical security control in the framework.

---

### OPS-06: Coercion Wallet (Decoy Wallet)

**Purpose:** Provide a convincing, accessible wallet to surrender under physical coercion, limiting losses while preserving primary holdings.

**Implementation:**
- Maintain a wallet with a balance that is "believable" relative to your perceived wealth: enough to satisfy a coercer, low enough to be an acceptable sacrifice
- The wallet should have a visible transaction history showing "normal" activity
- Seed phrase stored in a location that is physically accessible under coercion (but not near primary hardware wallet storage)
- Primary holdings held under 72-hour+ timelock (WKS-03): even if coercer gains access, transfers cannot execute immediately

**Critical Note:** Do not present a wallet that is obviously too small: this creates escalation risk. The decoy must be credible.

---

### OPS-07: Family OPSEC

**Problem:** Family members are the softest target in your security posture. Attackers who cannot defeat your security directly will target your spouse, children, or parents: who have no security training and may not understand the risk.

**Implementation:**
- Family members should not know the full structure of your holdings: only that "most of it is locked away and takes days to access"
- Do not store any access information (seed phrases, hardware wallets, PINs) in family-shared spaces
- Family devices should never have crypto wallets installed
- Brief family members on the basics: never discuss family wealth with strangers; "dad doesn't carry crypto on him"; call immediately if approached by strangers asking about dad's finances
- Establish a family duress code word that, when spoken, means "I am under coercion; call law enforcement"

---

### OPS-08: Geolocation Hygiene

**Implementation:**
- Strip EXIF data from all photos before posting (tool: ExifTool, iOS/Android built-in options)
- Disable location services on all crypto-related apps (wallets, exchanges, portfolio trackers)
- Do not check in to locations on social media: especially from home, regular hangouts, or crypto conference venues
- For high-value holders: use a VPN; avoid consistent IP geolocation from the same home address appearing in CEX login records

---

### OPS-09: Surveillance Detection

**Basic Indicators:**
- Same vehicle or individual observed in multiple locations over multiple days
- Unexpected contact from individuals seeking information about your finances or schedule
- Social media interactions from new accounts asking specific questions about your holdings or daily routine
- Unusual activity at your residence (drive-by photography, unfamiliar vehicles parked for extended periods)

**Response:** Do not confront; document (time, location, description); alert trusted contact; vary your routine; consider temporary relocation for high-threat periods.

---

### OPS-10: Duress Protocol

**Implementation:**
- Establish a pre-agreed phrase or signal with a trusted contact that means "I am under coercion; initiate emergency protocol"
- The protocol: trusted contact calls law enforcement; alerts family; does NOT transfer any funds or provide any information to anyone claiming to be acting on your behalf
- Test the protocol at least once per year
- Consider a panic word that, when spoken to a smart home device, triggers a silent alarm to the trusted contact

---

## Threat Coverage Matrix

| Threat ID | Threat Name | Controls Applied |
|---|---|---|
| CS-PHY-01 | Kidnapping/Coercion | OPS-01, OPS-02, OPS-05, OPS-06, OPS-07, OPS-10 |
| CS-PHY-02 | Home Invasion | OPS-01, OPS-04, OPS-07, OPS-08 |
| CS-SOC-01 | Phishing | OPS-02, OPS-03 |
| CS-SOC-03 | Fake Job Offer | OPS-01, OPS-04 |

---

## CTRS Risk Assessment: Physical Domain

| Threat | Likelihood | Impact | Detectability | CTRS Score |
|---|---|---|---|---|
| CS-PHY-01 (Kidnapping) | 3 | 5 | 2 | 18.4 |
| CS-PHY-02 (Home Invasion) | 3 | 5 | 2 | 18.4 |

Both physical threats score at maximum CTRS impact because: losses are total and immediate, recovery is impossible, and the attack requires no technical capability: only OSINT and opportunity.

---

## 30-Day Physical OPSEC Sprint

**Week 1: Identity Decoupling**
- [ ] Conduct OSINT self-audit (OPS-04)
- [ ] Identify and document all wallet addresses linked to your identity
- [ ] Remove or edit social posts disclosing crypto holdings

**Week 2: Holdings Architecture**
- [ ] Implement 72-hour timelock on governance wallet (WKS-03)
- [ ] Establish geographically split multisig (WKS-02)
- [ ] Fund and configure decoy wallet (OPS-06)

**Week 3: Family and Physical Plan**
- [ ] Brief family on basic OPSEC (OPS-07)
- [ ] Draft written incident response plan (OPS-05)
- [ ] Establish trusted contact and daily check-in protocol

**Week 4: Hygiene and Monitoring**
- [ ] Enable EXIF stripping; audit past photos (OPS-08)
- [ ] Set up Google Alerts for your name + crypto keywords
- [ ] Test duress protocol with trusted contact (OPS-10)

---

## Research References

- Research Note 001: The Wrench Attack Epidemic → `research/001_wrench_attack_epidemic.md`
- CertiK Skynet Wrench Attacks Report, February 2026
- CSI Weekly Issue 46: Minnesota Kidnapping Case Analysis
- CSI Weekly Issue 43: Ledger Co-Founder Kidnapping (France, January 2025)

---

*CSI CryptoSHIELD Framework v1.1 | Domain 03: OPSEC and Physical Security*
*Cyber Strategy Institute | Open-Source | Sovereignty-First*
