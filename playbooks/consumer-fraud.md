# Playbook: Consumer Fraud Defense (Pig Butchering / Investment Scam)

**CSI CryptoSHIELD Framework v1.1**
Threats: CS-FRD-01, CS-FRD-02, CS-FRD-03, CS-FRD-04 | Domain: 09 (CFD)

---

## Threat Profile

Consumer fraud is the single largest crypto threat by dollar volume: $7.2 billion in U.S. pig butchering losses in 2025 alone. The attack requires no technical capability: only psychology, time investment, and a fake platform. AI has eliminated the traditional red flags (poor grammar, implausible offers) and extended the trust-building phase indefinitely.

The FBI's Operation Level Up found 78% of active victims had no idea they were being scammed.

---

## The Kill Chain (Pig Butchering)

```
Phase 1: CONTACT
  Random message (WhatsApp, dating app, LinkedIn)
  "Wrong number" / investment opportunity / "old friend"
  
Phase 2: TRUST BUILDING (weeks to months)
  Relationship develops; investment topic introduced
  "My uncle/cousin/mentor manages a profitable fund"
  
Phase 3: BAIT
  Small investment; small profitable withdrawal (TRUST TRAP)
  "See? It works!"
  
Phase 4: ESCALATION
  Pressure to invest more; FOMO manufacturing
  "This window closes tomorrow"
  
Phase 5: LOCK (Withdrawal Block)
  First withdrawal attempt fails
  "You owe X% tax to unlock" / "AML verification required"
  
Phase 6: FEE EXTRACTION LOOP
  Each fee paid generates new fee demand
  Multiple rounds; total fees may exceed original investment
  
Phase 7: EXIT
  Platform disappears; all contact ceases
```

---

## Red Line Indicators (Immediate Stop Conditions)

Any ONE of these is sufficient to classify the situation as fraud and stop all engagement:

| Indicator | Meaning |
|---|---|
| Any platform blocking withdrawals pending fee payment | Confirmed fraud |
| "Tax payment" required to release funds | Confirmed fraud |
| "AML deposit" or "risk deposit" required | Confirmed fraud |
| "Account certification" or "upgrade fee" | Confirmed fraud |
| Support exists only on Telegram/WhatsApp | Fraud signal |
| Platform not findable via independent web search | Fraud signal |
| Cannot verify custody of your funds on-chain | Fraud signal |
| Contact who introduced the platform becomes unavailable | Fraud signal |
| "Recovery service" offers to get your money back for a fee | Secondary fraud (CS-FRD-02) |

**The absolute rule:** No legitimate platform withholds withdrawals pending external fee payment. This is not a feature. It is the mechanism of the fraud.

---

## OODA Response: Active Engagement Suspected

### OBSERVE
- When did this contact originate?
- What is the relationship trajectory?
- When and how was the investment platform introduced?
- Can you independently verify this platform exists? (DFPI, CryptoScamDB, Chainabuse check)

### ORIENT
- Apply the Fee Demand Alert Protocol (SMS-14): has any withdrawal been blocked with a fee demand?
- Apply the 10-Day Rule (SMS-13): have you deposited more than $1,000 within 10 days of first learning about this platform?
- Apply the AI Persona Detection test (CFD-08): can you verify the identity of this contact through out-of-band means?
- Pattern match: Does this contact's behavior match the kill chain phases above?

### DECIDE
- **If any Red Line Indicator above is present:** Stop immediately. Do not pay additional fees. Do not send additional funds.
- **If trust-building phase only:** Apply 10-day rule; do independent verification before any deposit
- **If post-deposit, no withdrawal block yet:** Test with small withdrawal; if blocked: confirmed fraud

### ACT
- Stop all fund transfers immediately
- Document: screenshots of all conversations, platform name and URL, wallet addresses used, all transaction receipts
- Report to: FBI IC3 (ic3.gov), Chainabuse, DFPI (California residents), CFTC (futures/derivatives)
- Do NOT engage any recovery service that contacts you: secondary fraud (CS-FRD-02)
- If funds moved to CEX: contact CEX support with transaction hashes immediately: freezes possible within hours of reporting

---

## If Already Victimized

**Do:**
- Report to FBI IC3 (most important for statistical tracking and investigations)
- Contact Chainabuse with all wallet addresses used by the platform
- Contact DFPI (California): they publish reports that help identify scam platforms
- Contact CFTC if any derivatives or leveraged products were involved
- Engage Chainalysis or TRM Labs if losses exceed $25,000 (professional tracing possible)

**Do Not:**
- Pay any additional fees to anyone for any reason
- Engage any "crypto recovery specialist" who contacts you after the loss (this is CS-FRD-02)
- Share this experience only with law enforcement: social media posts can attract secondary scammers

**Prognosis:** Recovery of funds is rare but not impossible, particularly if CEX landing points are identified quickly. The FBI's Operation Level Up successfully stopped $285 million in pig butchering losses in 2024 by acting on early intervention. Reporting matters even when individual recovery is unlikely.

---

*Playbook: Consumer Fraud Defense | CSI CryptoSHIELD v1.1 | Open-Source*
