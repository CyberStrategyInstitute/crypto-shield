# Domain 09: Consumer Fraud and Financial Grooming Defense (CFD)

**CSI CryptoSHIELD Framework v1.1 | Added in v1.1 | May 2026**

---

## The Missing $11 Billion

This domain did not exist in CryptoSHIELD v1.0. That was a structural gap.

The FBI IC3 2025 Annual Report documents $11.366 billion in U.S. crypto-related fraud losses in a single year. $7.2 billion of that is pig butchering alone. This total is nearly three times the on-chain protocol exploit total tracked by DefiLlama for the same period.

The gap existed because most crypto security frameworks focus on on-chain protocol security: smart contract bugs, bridge exploits, key compromise. These are real and significant. They are also not the primary vector by which ordinary people lose their life savings to crypto crime.

Consumer fraud: pig butchering, ATM coercion, fake platforms, recovery scams, professor scams: operates almost entirely off-chain, through social engineering, manufactured trust, and psychological manipulation. It does not appear in DefiLlama. It barely appears in crypto security discourse. It accounts for the majority of crypto-related harm.

This domain addresses it.

**For the cognitive manipulation and psychological resilience layer:** See [Cognitive Sovereignty Framework](https://github.com/CyberStrategyInstitute/cognitive-sovereignty): specifically T-CT-004 (Personalized Narrative Injection), T-CT-005 (Social Proof Manipulation), T-CT-007 (Trust Network Infiltration), and Domain 3 (Emotional Resilience).

---

## The Fee Escalation Kill Chain

Every pig butchering and platform fraud follows the same escalating commitment architecture. Understanding it means recognizing it before the final extraction phase:

```
Phase 1: Trust Building (weeks to months)
         ↓  Dating app / WhatsApp / Telegram contact
         ↓  Personal relationship development
         ↓  Introduction of investment opportunity ("I can show you how I do it")

Phase 2: Platform Introduction
         ↓  Introduction to fraudulent trading platform
         ↓  Victim registers; UI shows professional design
         ↓  Small initial deposit; "profits" visible immediately

Phase 3: Trust Bait
         ↓  Small test withdrawal SUCCEEDS (this is the trap)
         ↓  Victim believes platform is legitimate
         ↓  Larger deposits encouraged; profits grow

Phase 4: Escalation and Commitment
         ↓  Victim deposits larger amounts
         ↓  "Profits" shown are fabricated by the platform
         ↓  Withdrawal attempt → BLOCKED

Phase 5: Fee Extraction (the actual profit for scammers)
         ↓  Fee demand 1: "Tax payment required to unlock withdrawal"
         ↓  Victim pays tax
         ↓  Fee demand 2: "AML verification deposit required"
         ↓  Victim pays AML
         ↓  Fee demand 3: "Account upgrade required"
         ↓  Fee demand 4: "Green channel access fee"
         ↓  Platform disappears

Phase 6: Re-Victimization (CS-FRD-02)
         ↓  "Recovery service" contacts victim proactively
         ↓  Second extraction cycle begins
```

**The decisive intervention point:** The test withdrawal that succeeds in Phase 3 is the trust bait. It is not a sign the platform is legitimate. No legitimate platform needs to bait trust with a test withdrawal. The decisive control is CFD-03: pattern recognition before Phase 3 completes.

---

## Controls

### CFD-01: Platform Legitimacy Stack Check

**Priority:** CRITICAL
**Threat IDs:** CS-FRD-01, CS-FRD-04, CS-SOC-07

**The complete stack: run all four before any deposit:**

| Check | Tool | What to Look For |
|-------|------|-----------------|
| Regulatory registration | DFPI (California: dfpi.ca.gov) | Is the platform registered? If not, it is not automatically a scam but warrants extreme caution |
| Scam database | CryptoScamDB (cryptoscamdb.org) | Is the domain or any associated domain listed? |
| Victim reports | Chainabuse (chainabuse.com) | Are any wallet addresses associated with the platform already reported? |
| Complaint search | DFPI Scam Tracker | Search the platform name and any variations |
| CFTC and SEC search | CFTC.gov and SEC EDGAR | Are they registered where required? |

**Implementation:**
- Run the full stack before depositing any amount on any new platform
- Search platform name, domain, and all variations (including typosquatted lookalikes)
- A clean result does not guarantee legitimacy: many fraudulent platforms are too new to have reports
- The 10-Day Rule (CFD-03) applies even if the platform passes the stack check

---

### CFD-02: Unsolicited Investment Offer Zero Trust

**Priority:** CRITICAL
**Threat IDs:** CS-FRD-01, CS-FRD-04, CS-SOC-03

**Absolute rule:** Any investment opportunity that arrives through a direct message, dating app, social media contact, or group chat invitation is treated as a social engineering attempt until independently verified through official channels.

**Implementation:**
- No DM, dating app contact, or random social media connection ever introduces a legitimate investment opportunity
- The more persuasive and personalized the offer, the higher the red flag: AI-generated personas are indistinguishable from real people in text
- Verify: can you find this person's identity through independent, public sources not provided by them?
- Verify: does this platform exist in any legitimate financial industry database?
- Default response to any unsolicited investment introduction: decline

**The AI detection problem:** Traditional detection relied on linguistic signals (poor grammar, spelling errors, unusual phrasing). AI-generated personas produce grammatically flawless, culturally appropriate, personally tailored messages with zero traditional detection signals. The only reliable detection is structural, not linguistic: the pattern of introduction → relationship → investment → platform is the signal, not the quality of the writing.

---

### CFD-03: Profitable Test Withdrawal Recognition

**Priority:** CRITICAL
**Threat IDs:** CS-FRD-01

**The test withdrawal is not evidence of legitimacy.** Fraudulent platforms allow a small test withdrawal in Phase 3 specifically to build trust and justify larger deposits.

**Implementation:**
- Recognize the test withdrawal as the trust bait mechanism, not platform validation
- Apply the following logic: If a platform I did not seek out, on which I am already "earning significant profits" after a short period, is now encouraging me to deposit more money after allowing me to withdraw a small amount: I am in Phase 3 of the pig butchering kill chain
- Do not interpret a successful test withdrawal as platform validation under any circumstances
- The correct response to a "successful" test withdrawal on an unsolicited platform: withdraw everything immediately, not invest more

---

### CFD-04: Fee Demand as Exit Signal

**Priority:** CRITICAL
**Threat IDs:** CS-FRD-01, CS-FRD-02

**Absolute rule:** Any platform that demands payment of a fee, tax, AML deposit, account upgrade charge, certification cost, or any other charge as a precondition for withdrawing funds that are already in the account is engaged in fraud.

**No exceptions:**
- "Government tax" on profits → Fraud. Taxes are paid to governments, not to trading platforms.
- "AML verification deposit" → Fraud. AML compliance does not require deposits from users.
- "Account upgrade fee" → Fraud. Legitimate platforms do not charge to access your own money.
- "Risk collateral" → Fraud.
- "Green channel access" → Fraud.

**Implementation:**
- Upon receipt of any fee demand to unlock existing balances: stop all further engagement
- Do not pay any fee regardless of amount
- Do not believe promises that the platform will "refund the fee" from profits
- Begin documentation immediately and report to IC3, DFPI, and Chainabuse

---

### CFD-05: Bitcoin ATM Transaction Refusal

**Priority:** CRITICAL
**Threat IDs:** CS-FRD-03

**Absolute rule:** No government agency (IRS, FBI, Social Security Administration, FTC), bank, or technology company will ever instruct you to withdraw cash and deposit it at a Bitcoin ATM. This scenario is always fraud, without exception.

**Implementation:**
- If you receive a phone call from anyone claiming to be a government official or bank representative directing you to a Bitcoin ATM: hang up and call the agency's official number directly (found on their official website, not given by the caller)
- If you are at a Bitcoin ATM and there is any question about whether the transaction is legitimate: stop and call a trusted family member or friend before proceeding
- Protect elder family members with explicit conversations about this pattern: adults over 60 represent 86% of Bitcoin ATM fraud losses

**The urgency signal:** These scams always create a false sense of urgency ("your Social Security number has been compromised and you must act now"). Urgency is a social engineering mechanism. Slow down.

---

### CFD-06: Elder Household Protocol

**Priority:** HIGH
**Threat IDs:** CS-FRD-03, CS-FRD-01

**Implementation:**
- Establish explicit agreement with family members over 60: any cryptocurrency transaction over $500 requires a conversation with a trusted adult family member first
- Specific scenarios to brief: Bitcoin ATM coercion (CFD-05), government impersonation calls, grandchild-in-trouble scam
- Create a "buddy system" for any investment activity: no solo investment decisions on unfamiliar platforms
- Remove or limit cryptocurrency app access on devices used by elder family members who do not actively invest

---

### CFD-07: Recovery Scam Firewall

**Priority:** HIGH
**Threat IDs:** CS-FRD-02

**Absolute rule:** No legitimate service can reverse a confirmed blockchain transaction.

**Implementation:**
- After any crypto loss: do not engage with any "recovery service" that contacts you, regardless of how official or professional they appear
- Legitimate recovery assistance options: FBI IC3 (ic3.gov), CFTC, licensed blockchain forensics firms (Chainalysis, TRM Labs): these firms assist law enforcement with tracing; they do not "recover" funds for a fee
- Any entity that promises to recover your crypto for an upfront fee is engaged in CS-FRD-02 re-victimization
- Report any recovery scam contact to: IC3, Chainabuse, and DFPI

---

### CFD-08: AI Persona Detection Protocol

**Priority:** HIGH
**Threat IDs:** CS-AI-05, CS-FRD-01

**Implementation:**
- For any online relationship that introduces investment opportunities: require out-of-band verification
- Out-of-band verification: video call that includes off-script conversation, unexpected topic changes, and specific questions the person should be able to answer based on their claimed background
- A pre-scripted video call or "technical difficulties" preventing video are red flags
- Request a live, unscripted interaction: AI deepfakes and pre-recorded video are distinguishable with specific demands (write a word on paper and hold it up, describe something visible in their current environment, etc.)

**The AI detection arms race:** Deepfake video is improving rapidly. The structural pattern: unsolicited contact introducing investment opportunity: is more reliable than any technical detection method for consumer-facing contexts.

**CSF cognitive resilience layer:** For systematic deepfake resilience and AI persona detection training: [CSF T-CT-016](https://github.com/CyberStrategyInstitute/cognitive-sovereignty/blob/main/taxonomy/manipulation-techniques.md)

---

### CFD-09: Group Chat Investment Protocol

**Priority:** HIGH
**Threat IDs:** CS-FRD-04, CS-MKT-03

**Implementation:**
- No investment decisions based on group chat consensus, regardless of how many members appear to agree
- Recognize that "professor" figures and "assistant" figures in investment groups are role-play personas operated by the scam compound
- Other "successful members" of the group are either fabricated accounts or victims being used as social proof
- Apply the Rotator Effect framework (see [Research Note 002](../research/002_rotator_effect.md)): who benefits from this group's investment behavior?

**The social proof manipulation mechanism:** The group creates the illusion of community validation. Multiple accounts showing "profits," "testimonials," and "gratitude" toward the professor are all operated by the same scam infrastructure. The cognitive vulnerability exploited is social proof: humans are wired to follow group behavior. CFD-09 requires conscious override of this instinct.

---

### CFD-10: Platform Custodial Assessment

**Priority:** CRITICAL
**Threat IDs:** CS-FRD-01, CS-SOV-02

**Implementation:**
- Before depositing to any platform, answer: can you independently verify your balance on-chain?
- For a legitimate exchange: your balance should be verifiable against on-chain transaction records
- For a fraudulent platform: the "balance" displayed in the UI is a fabricated number with no on-chain correspondence
- Ask: what wallet address holds my deposited funds? Can I verify this on a blockchain explorer?

**The custodial fraud signal:** Fraudulent platforms cannot provide a verifiable on-chain wallet address for user funds because the funds do not exist in a segregated wallet: they have already been moved to attacker-controlled addresses. If a platform cannot or will not answer this question, treat it as a fraud signal.

---

## Reporting Stack for CFD Incidents

**First 60 minutes after any CFD incident:**
1. Stop all further engagement with the platform or contact immediately
2. Screenshot all communications, platform interfaces, transaction confirmations
3. Record all wallet addresses used (both yours and the platform's)
4. Record all transaction hashes

**Reporting priority order:**
1. FBI IC3 (ic3.gov): all crypto fraud
2. DFPI Crypto Scam Tracker: California residents; all others use your state financial regulator
3. Chainabuse: submit all attacker/platform wallet addresses
4. CryptoScamDB: submit scam platform URL
5. CFTC: if any futures, options, or derivatives were involved
6. FTC: if impersonation of government agency (CFD-05 pattern)

**Recovery reality check:**
- Blockchain transactions cannot be reversed
- Funds sent to fraudulent platforms are likely gone
- Reporting helps law enforcement build patterns and potentially freeze funds at exchange landing points
- Recovery from secondary scammers (CS-FRD-02) is never possible

---

## Domain 09 Metrics (FBI IC3 2025)

| Fraud Type | U.S. Annual Loss (2025) | Primary Target |
|-----------|------------------------|----------------|
| Pig butchering / investment fraud | $7.2B | 30-60 demographic, DFPI data shows no demographic immunity |
| Asset recovery re-victimization | $1.4B | Previous fraud victims |
| Bitcoin ATM coercion | $333M | Adults 60+ (86% of losses) |
| Investment group / professor scam | $Millions per campaign | All demographics |
| Tech support crypto scam | $1.226B | Adults 60+ disproportionately |
| AI-enabled fraud (all types) | $893M | All demographics |
| **Total consumer crypto fraud** | **~$11.4B** | |

**FBI's own finding:** 78% of active pig butchering victims have no idea they are being scammed. Detection in time to prevent loss requires pattern recognition before Phase 4 of the kill chain (Escalation and Commitment).

---

*Domain 09: Consumer Fraud and Financial Grooming Defense | CryptoSHIELD v1.1*
*Added in v1.1 based on DFPI Scam Tracker, FBI IC3 2025, and Chainabuse cross-analysis*
*Cognitive manipulation layer: [Cognitive Sovereignty Framework](https://github.com/CyberStrategyInstitute/cognitive-sovereignty)*
