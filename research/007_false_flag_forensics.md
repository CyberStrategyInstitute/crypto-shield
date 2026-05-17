# Research Note 007: False Flag Forensics: Systematic Attribution Analysis for Crypto Incidents

**Classification:** Open-Source Intelligence | CSI CryptoSHIELD Framework
**Date:** May 2026 | **Version:** 1.0 (Seed Document)
**Related Threat IDs:** CS-INS-01, CS-INS-03 (Wagemole), CS-DFI-01
**Domain:** 00: Cross-Domain Governance | Intelligence Layer

> **Note:** This research note is the seed document for the full False Flag Assessment Protocol (FFAP) deliverable. The FFAP will apply this methodology to 10 historical cases and produce a publishable Attribution Accuracy Report. See `research/007_ffap_full.md` (forthcoming).

---

## The Core Problem

The crypto industry has a narrative problem that is also a security problem.

When a protocol is drained, the incident report almost universally reaches one of two conclusions within 48-72 hours:
1. "The hack was executed by North Korean hackers (DPRK/Lazarus Group)"
2. "The exploit was a smart contract vulnerability"

Both attributions are frequently wrong: or incomplete. And the consequences of wrong attribution are severe: the true attacker goes unpunished, the root cause is misidentified, corrective controls target the wrong layer, and victims of insider negligence have no legal recourse because the "DPRK did it" narrative shields the responsible parties.

CSI's multi-pass analysis of major incidents reveals a consistent pattern: **insider-vector attacks are systematically misattributed to external nation-state actors.** The DPRK attribution serves as a convenient "fall guy" that satisfies regulators, journalists, and token holders while protecting the individuals whose operational failures or active malfeasance actually enabled the exploit.

---

## Defining the False Flag

In the context of crypto incident attribution, a "false flag" is not necessarily a deliberate deception operation: though that exists too. It is any attribution conclusion that:

1. **Assigns credit to an actor who did not initiate the attack**, while
2. **Shielding the actor(s) whose failures or actions were the actual root cause**

The practical distinction: Was the exploit technically only possible because someone with privileged access failed to follow security protocols: or actively assisted the attacker? If yes, the "DPRK" attribution is at minimum incomplete, and often materially false.

---

## The False Flag Assessment Protocol (FFAP)

### Indicator Set 1: Access Vector Analysis

The first question in any attribution analysis: **how did the attacker get in?**

| Access Method | Insider Probability | DPRK Probability | Notes |
|---|---|---|---|
| Admin key compromise (EOA, known key holder) | HIGH | MEDIUM | DPRK achieves this via social engineering of keyholder |
| Multi-sig key compromise (multiple key holders) | HIGH | LOW-MEDIUM | Requires compromising multiple independent parties |
| Smart contract bug (audited code) | LOW | LOW | Neither; pure technical failure |
| Smart contract bug (unaudited code) | LOW | LOW | Neither; development failure |
| Frontend/DNS compromise | MEDIUM | MEDIUM | Infrastructure access |
| Malware on developer device | MEDIUM | HIGH | DPRK Wagemole primary vector |
| Insider with direct access | CRITICAL | LOW | DPRK can execute IF insider |
| Supply chain (npm/SDK) | LOW-MEDIUM | HIGH | DPRK actively uses this vector |

**Key Insight:** If the access method required someone with privileged access to have their device compromised, that person's device security practices and the circumstances of the compromise become critical attribution data. "DPRK compromised my laptop" is a claim that must be forensically verified: not accepted as given.

---

### Indicator Set 2: Code Change Timeline

CSI analysis of LNDFi, BrincFi, Radiant Capital, and other insider-vector incidents reveals a consistent pattern:

**The Pre-Exploit Code Change Pattern:**
```
T-90 days to T-30 days: Malicious or enabling code change committed to repository
T-30 to T-7 days: Change passes code review (reviewer does not flag)
T-7 to T-0: Final operational setup (admin role granted, key positioning)
T-0: Exploit execution
```

**Analysis Questions:**
- When was the last code change to the attacked contract/function before the exploit?
- Who committed that change? Was it the same person who controls admin keys?
- Did the change expand any admin role's authority in a non-obvious way?
- Did code reviewers document concerns?
- Was the change timing correlated with any personnel changes (new hire, contractor engagement)?

**LNDFi Case Data Point:** A five-word code change committed 41 days before the exploit granted any "Pool Admin" the ability to drain funds. The change was small, non-obvious, and passed review. The exploit used the exact capability this change enabled. CSI attribution confidence for insider involvement: HIGH.

---

### Indicator Set 3: Fund Flow Analysis

DPRK's laundering methodology is documented, consistent, and traceable:

**DPRK Laundering Signature:**
```
Exploit wallet → Tornado Cash (pre-March 2025) / sanctioned mixers
→ THORChain (chain hop)
→ Multiple hops through Chinese broker intermediaries
→ OTC desk settlement (USDT/BTC)
```

**Insider/Organized Crime Laundering Signature (different):**
```
Exploit wallet → DEX hops (Uniswap, Curve)
→ CEX with lax KYC (offshore)
→ Privacy coin conversion
→ [Often less sophisticated than DPRK; mistakes in fund flow]
```

**Questions:**
- Do the fund flows match DPRK's documented laundering methodology?
- Were THORChain and Chinese broker intermediaries used? (DPRK-consistent)
- Did the attacker make mistakes in fund movement? (Inconsistent with DPRK discipline)
- Was there any interaction with CEXes that would create a KYC trail? (DPRK avoids)
- Did on-chain timing correlate with North Korean business hours? (DPRK-consistent, not conclusive)

---

### Indicator Set 4: The Fall-Guy Pattern Detection

A "fall guy" is an actor: person or organization: who is sacrificed (willingly or unwillingly) to absorb reputational, regulatory, and legal accountability for a deeper operation. In crypto, this manifests as:

**Type A: Willing Fall Guy**
- Individual accepts responsibility for a planned exploit as part of an arrangement
- Typically offered financial compensation held in escrow pending "conviction"
- Example template: developer "goes rogue," accepts arrest while others escape with bulk proceeds

**Type B: Unwilling Fall Guy (Patsy)**
- Individual or organization is positioned to appear responsible without their knowledge
- Example: DPRK attribution used to shield insider who actually provided access
- The Wagemole DPRK operative provides cover story: "we hired a North Korean, it's their fault": when the true failure was inadequate vetting and security controls

**Type C: Sacrificial Entity**
- An organization (exchange, protocol) is allowed to fail publicly, absorbing regulatory and media attention
- Classic example: FTX absorbs the full regulatory response to a broader capital extraction pattern
- Capital that flowed out before FTX collapse is protected by the FTX collapse narrative

**Detection Questions:**
- Who benefits financially from this incident narrative?
- Does the attributed actor's capabilities match the sophistication of the attack?
- Is there a simpler explanation that involves people closer to the protocol?
- Did any key personnel exit with funds, leave the company, or become uncontactable before or after the incident?
- Was the public narrative established suspiciously quickly? (< 24 hours for DPRK attribution suggests pre-positioning)

---

### Indicator Set 5: Personnel Analysis

For any protocol suffering a large exploit, the insider threat checklist:

```
Personnel Analysis Checklist:
[ ] Who had admin key access at time of exploit?
[ ] When was that access granted? By whom?
[ ] Did any of these individuals join within 12 months of the exploit? (Wagemole window)
[ ] Were background checks performed on all key holders?
[ ] Did any key holder have unexplained wealth, behavioral changes, or unusual absence before exploit?
[ ] Who is NOT cooperating with post-incident investigation?
[ ] Were any team members recruited via LinkedIn or recruiter outreach? (Wagemole vector)
[ ] Did any team member review the malicious code change without flagging it?
```

**The Wagemole Indicator Set (DPRK-specific):**
These are indicators of DPRK identity fabrication for insider access. See Research Note 003 for full analysis.

---

## FFAP Scoring Formula

Each incident receives a composite False Flag Probability Score (FFPS) based on weighted indicators:

```
FFPS = (Access_Vector_Score × 0.30) +
       (Code_Change_Score × 0.25) +
       (Fund_Flow_Score × 0.20) +
       (Fall_Guy_Score × 0.15) +
       (Personnel_Score × 0.10)
```

Each component scored 0-1.0:
- 0.0-0.3: Attribution consistent with official narrative
- 0.3-0.6: Material uncertainty; insider probability non-trivial
- 0.6-0.8: Insider vector probable; official attribution likely incomplete
- 0.8-1.0: False flag highly probable; official attribution is covering deeper actors

---

## Priority Cases for FFAP Analysis

The following cases are queued for full FFAP analysis in the forthcoming Attribution Accuracy Report:

| Case | Official Attribution | CSI Preliminary FFPS | Key Anomaly |
|---|---|---|---|
| FTX Collapse (Nov 2022) | "FTX mismanagement" | 0.45 | Capital flow patterns suggest coordinated extraction pre-collapse |
| LNDFi Hack (May 2025) | DPRK Lazarus | 0.72 | 41-day pre-exploit code change, Pool Admin access |
| Radiant Capital (Oct 2024) | DPRK Lazarus | 0.55 | Three developer device compromise; Safe{Wallet} display manipulation |
| Bybit (Feb 2025) | DPRK Lazarus | 0.35 | Fund flow most consistent with DPRK signature |
| Drift Protocol (Apr 2026) | DPRK Lazarus | 0.48 | Six-month fake employee; social engineering primary vector |
| BrincFi (2021) | "Developer theft" | 0.80 | Malicious function in production code by trusted developer |
| Step Finance (Jan 2026) | "Private key compromise" | 0.40 | Device compromise; AI agent amplification |
| Kelp DAO (Apr 2026) | Bridge exploit | 0.20 | Single-verifier design; technical failure primary |

---

## The Structural Problem

Attribution accuracy in crypto has a structural incentive problem:

**Protocols benefit from DPRK attribution because:**
- It removes their legal liability (act of foreign government)
- It satisfies regulators ("we were hacked by nation-states")
- It maintains community trust ("not our fault")
- It preserves investment value longer than "our dev stole it"

**Law enforcement benefits from DPRK attribution because:**
- It produces press-worthy indictments of foreign actors
- It avoids the political difficulty of prosecuting respected industry figures
- It feeds the national security budget justification cycle

**The media benefits from DPRK attribution because:**
- Nation-state hacking makes better headlines than insider access control failures
- The narrative is simpler and more dramatic

**The actual insider or negligent party benefits most of all.**

CSI's mission in this domain: build the analytical tools to interrupt this attribution laundering cycle. Not to protect DPRK from accountability: their thefts are real and significant: but to ensure that the insider-threat population that uses DPRK as cover is also held accountable.

---

## Research Note Series Context

| Note | Topic | Status |
|---|---|---|
| 001 | Wrench Attack Epidemic | Complete |
| 002 | The Rotator Effect | Complete |
| 003 | DPRK Attribution Analysis | Complete |
| 004 | AI Agent Attack Surface | Forthcoming |
| 005 | Supply Chain Vectors | Forthcoming |
| 006 | Pig Butchering Anatomy | Forthcoming |
| 007 | False Flag Forensics (this note) | Seed complete; full FFAP report forthcoming |

---

*Research Note 007 | CSI CryptoSHIELD Framework v1.1*
*Cyber Strategy Institute | May 2026 | Open-Source*
