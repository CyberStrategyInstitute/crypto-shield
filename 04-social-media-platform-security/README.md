<div align="center">

<img src="../assets/Domain 04 Social Media and Platform Security (SMS).png" alt="Domain 04 Social Media and Platform Security (SMS)" width="100%" />
</div>


# Domain 04: Social Media and Platform Security (SMS)

**CSI CryptoSHIELD Framework v1.1**
Cyber Strategy Institute | Classification: Open-Source | Sovereignty-First

---

## Domain Philosophy

Every crypto platform interaction is a potential attack surface. Every social media account is a credential under siege.

The era of detecting scams by spotting grammatical errors is over. AI impersonation attacks surged 1,400% year-over-year in 2025. The "Nigerian prince" spelling test is dead. What replaced it: flawlessly written, contextually aware, psychologically calibrated social engineering delivered at scale by AI-powered threat actors who have studied your public profile before sending the first message.

This domain governs the security posture for every account, platform, and social channel a crypto holder touches: from X account security to platform legitimacy verification to URL hygiene. The attack surface is vast. The controls are specific, executable, and effective.

---

## Controls (v1.1: 15 Controls)

| Control ID | Control | Implementation | Priority |
|---|---|---|---|
| SMS-01 | Hardware 2FA | YubiKey or equivalent for all exchange, social, and crypto accounts | CRITICAL |
| SMS-02 | Remove Phone Number from Social | Eliminate SMS-based recovery attack surface entirely | CRITICAL |
| SMS-03 | OAuth Audit | Monthly audit of connected third-party apps; revoke all non-essential | HIGH |
| SMS-04 | Dedicated Recovery Email | Separate email for crypto account recovery; own strong 2FA; never publicized | HIGH |
| SMS-05 | URL Verification | Full URL inspection before interacting with any crypto frontend | CRITICAL |
| SMS-06 | No Unsolicited DM Trust | Never act on DMs offering jobs, partnerships, or "giveaways" | CRITICAL |
| SMS-07 | Social Engineering Drill | Monthly awareness test for team/family; recognize urgency/authority patterns | HIGH |
| SMS-08 | Official Channel Verification | Cross-verify announcements on-chain, not via social posts alone | HIGH |
| SMS-09 | DNS/Frontend Alert System | Use Scam Sniffer or equivalent for real-time phishing detection | HIGH |
| SMS-10 | Influencer Skepticism Protocol | Apply Rotator Effect analysis before acting on influencer calls | MEDIUM |
| SMS-11 | Manual URL Entry Protocol | Never click crypto site links; bookmark directly or type manually | HIGH |
| SMS-12 | Pre-Transaction Platform Verification | Run any new platform through DFPI, CryptoScamDB, Chainabuse before first deposit | CRITICAL |
| SMS-13 | 10-Day Rule for New Platforms | Mandatory 10-day waiting period before depositing >$1,000 on any unfamiliar platform | HIGH |
| SMS-14 | Fee Demand Alert Protocol | Any platform demanding fees to unlock withdrawals = immediate cease and report | CRITICAL |
| SMS-15 | Recovery Scam Awareness | No legitimate service can reverse blockchain transactions; all recovery fee demands = scam | CRITICAL |

---

## Control Implementation Detail

### SMS-01: Hardware 2FA

**Why SMS 2FA is Insufficient:**
SIM swapping attacks allow attackers to port your phone number to a device they control, intercepting all SMS codes. In 2024-2025, SIM swap attacks against crypto holders resulted in tens of millions in losses. Coinbase alone documented hundreds of SIM-swap-facilitated account takeovers.

**Implementation:**
- YubiKey 5 Series (FIDO2/WebAuthn) for all accounts that support it
- Google Titan Key as backup for YubiKey-compatible accounts
- TOTP authenticator app (Aegis on Android, Raivo OTP on iOS) as tertiary layer
- Store backup hardware key in a physically secure location separate from primary

**Account Priority List:**
1. All cryptocurrency exchanges (Coinbase, Binance, Kraken, etc.)
2. X (Twitter): primary vector for account takeover + crypto scam amplification
3. Gmail/ProtonMail (recovery email)
4. Discord (project communities, DMs)
5. Telegram (trading groups, project channels)
6. GitHub (developers)

---

### SMS-02: Remove Phone Number from Social

**The Attack Chain:**
Phone number on social account → SIM swap attack → SMS 2FA bypass → account takeover → impersonation for crypto scams or credential harvesting

**Implementation:**
- X: Settings → Security → Two-factor authentication → Remove phone number; use authenticator app or security key only
- Discord: Remove phone number from account settings; enable TOTP 2FA
- Telegram: Settings → Privacy and Security → Phone Number → set to "Nobody"; enable Two-Step Verification
- Google: Remove phone as recovery method; use backup codes and authenticator

**Note:** Some platforms require a phone number at account creation but allow removal after verification. Complete this removal step immediately after setup.

---

### SMS-03: OAuth Audit

**Why It Matters:**
Third-party apps authorized to your social accounts can post on your behalf, read your DMs, and access account details. Compromised OAuth-authorized apps become persistent backdoors even after you change your password.

**Monthly Audit Process:**
- X: Settings → Security → Apps and sessions → Connected apps: revoke anything not actively used
- Discord: User Settings → Authorized Apps: revoke any app not in active use
- Telegram: Settings → Privacy and Security → Active Sessions: terminate unknown sessions

**Red Flags:**
- Apps you don't recognize
- Apps with "post on my behalf" permissions
- Apps authorized more than 90 days ago with no recent use

---

### SMS-05: URL Verification

**Full Verification Protocol (execute every time):**
1. Check the top-level domain (TLD): `uniswap.org` vs `uniswap.io` vs `uniswap-app.com`: only one is legitimate
2. Verify there are no Unicode lookalike characters in the domain (e.g., `сoinbase.com` with a Cyrillic 'с')
3. Confirm HTTPS with valid certificate from the expected issuer
4. Cross-reference the URL against CryptoScamDB before first use
5. If accessing via a link (from Discord, X, email): don't. Navigate directly.

**Browser Bookmarks Are Sacred:**
Create verified bookmarks for every crypto platform you use. The bookmark was created by you, from a verified URL. Use it every time. Never click a link to a crypto platform from any external source.

---

### SMS-06: No Unsolicited DM Trust

**Threat Profile:**
Unsolicited DMs are the primary delivery mechanism for:
- Fake job offers (CS-SOC-03) delivering malware via "test assignments"
- Fake meeting app invitations (CS-SOC-04) delivering Meeten malware
- "Alpha" investment calls delivering pig butchering setups
- "Giveaway" links capturing wallet credentials
- "Support team" impersonations requesting seed phrases

**The Zero-Trust Rule:**
Any DM received without a prior, established relationship is adversarial by default until proven otherwise through out-of-band verification. Period.

**Verification Protocol for Legitimate-Seeming DMs:**
1. Do not click any links in the DM
2. Do not download any attachments
3. Navigate independently to the entity's official website
4. Verify the contact through official channels listed on that website
5. If it was real, they'll verify. If they insist on the DM channel only: adversarial.

---

### SMS-08: Official Channel Verification

**The Attack Pattern:**
Fake announcements on social channels (X, Discord, Telegram) claiming: emergency migration, token upgrade, "claim your airdrop," security breach requiring wallet reconnection. These are consistently timed around real protocol events to maximize credibility.

**Verification Hierarchy (highest to lowest trust):**
1. On-chain governance proposals at the protocol's verified contract address
2. Protocol's GitHub repository commit history
3. Official website (directly navigated, not linked)
4. Protocol's verified Twitter account (blue checkmark alone is insufficient: verify via website cross-reference)
5. Discord announcements: only in verified servers where you joined via official website link

**Rule:** If you cannot verify an announcement on-chain or via the official website you navigated to directly, it is unverified.

---

### SMS-12: Pre-Transaction Platform Verification

**Mandatory Checks Before First Deposit:**
```
Platform: [NAME]
DFPI Lookup: https://dfpi.ca.gov/consumers/crypto/crypto-scam-tracker/
CryptoScamDB: https://cryptoscamdb.org/
Chainabuse: https://www.chainabuse.com/
SEC Action: https://www.sec.gov/litigation/actions/
CFTC: https://www.cftc.gov/LearnAndProtect/AdvisoryViewer/
Result: CLEAR / FLAGGED / BLOCKED
```

**Red Flags That Override Any Passing Check:**
- Platform cannot be found via independent web search (search results only show its own domain)
- No verifiable physical address or corporate registration
- Support exists only via Telegram or WhatsApp: no email, no ticket system
- Promises of guaranteed returns or specific profit percentages
- Withdrawal fees or "verification deposits" required

---

### SMS-14: Fee Demand Alert Protocol

The fee escalation cycle is the defining characteristic of pig butchering and related investment fraud:

```
Deposit → "Profits" accumulate → Withdrawal attempt
→ BLOCKED: "Pay X% tax to unlock"
→ Tax paid → BLOCKED: "Pay AML verification fee"
→ Fee paid → BLOCKED: "Account upgrade required"
→ Fee paid → Platform disappears
```

**Absolute Rule:** Any platform blocking a withdrawal pending payment of any fee: regardless of the stated justification: is committing fraud. The fee is not unlocking your withdrawal. It is extracting additional funds from you before the exit.

**Response:**
1. Stop all deposits immediately
2. Document: all wallet addresses used, all communications, all transaction receipts
3. Report: FBI IC3 (ic3.gov), Chainabuse, DFPI (if in California), CFTC
4. Do NOT pay additional fees: you will not recover your funds; you will only lose more
5. Do NOT engage a "recovery service" that contacts you afterward (CS-FRD-02)

---

## Threat Coverage Matrix

| Threat ID | Threat | Controls Applied |
|---|---|---|
| CS-SOC-01 | Phishing | SMS-05, SMS-08, SMS-09, SMS-11 |
| CS-SOC-03 | Fake Job Offer | SMS-06, SMS-07 |
| CS-SOC-04 | Fake Meeting App | SMS-06, SMS-07 |
| CS-SOC-05 | AI Deepfake | SMS-06, SMS-07, SMS-08 |
| CS-SOC-07 | Typosquatting | SMS-05, SMS-09, SMS-11 |
| CS-FRD-01 | Pig Butchering | SMS-06, SMS-12, SMS-13, SMS-14 |
| CS-FRD-02 | Recovery Scam | SMS-15 |
| CS-WAL-03 | DNS Hijack | SMS-05, SMS-09, SMS-11 |
| CS-MKT-03 | Influence Operation | SMS-10 |

---

## X (Twitter) Account Hardening: Full Protocol

X accounts are consistently the highest-value social media target for crypto attackers. A compromised X account enables: credential phishing via announcement posts, NFT/token drain scams, influencer impersonation, and social engineering of your followers.

**Complete X Hardening Checklist:**
- [ ] Remove phone number from account (Settings → Security → Two-factor authentication)
- [ ] Enable Security Key (hardware FIDO2) as primary 2FA
- [ ] Enable "Password reset protect" (requires email confirmation before password reset)
- [ ] Enable "Two-factor authentication app" as backup to hardware key
- [ ] Review and revoke all connected apps (Settings → Security → Apps and sessions)
- [ ] Enable "Protect your Tweets" if your account is not intentionally public
- [ ] Check login history for unrecognized sessions; log out all other sessions
- [ ] Set a strong, unique password stored in a password manager
- [ ] Review email address on file: ensure it points to your dedicated recovery email (SMS-04)

---

## AI-Enhanced Deception: Detection Framework

Traditional red flags (typos, bad grammar, urgency) are obsolete. New framework:

| Old Red Flag | AI-Defeated? | New Detection Method |
|---|---|---|
| Grammatical errors | Yes | Verify identity out-of-band |
| Generic address ("Dear User") | Yes | Verify via official channel |
| Suspicious URL | Partially | Full URL verification protocol |
| Urgency/pressure tactics | No | Slow down; urgency = adversarial |
| Implausible offer | Partially | Research independently |
| Requests for seed phrase | Never legitimate | Absolute: no |

The one detection method AI cannot defeat: **out-of-band verification**. If someone contacts you claiming to be a known entity, hang up or close the chat, navigate independently to that entity's official contact, and verify from there. No AI persona survives that test.

---

*CSI CryptoSHIELD Framework v1.1 | Domain 04: Social Media and Platform Security*
*Cyber Strategy Institute | Open-Source | Sovereignty-First*
