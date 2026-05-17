# Playbook: Physical Coercion Response

**CSI CryptoSHIELD Framework v1.1**
Threats: CS-PHY-01, CS-PHY-02 | Domain: 03 (OPS)

---

## Threat Profile

Physical coercion against crypto holders ranges from home invasion to organized kidnapping. The attacker's goal: force real-time asset transfer while the victim is under physical duress. Unlike digital attacks, there is no "undo." Response must be pre-planned: not improvised under stress.

---

## Pre-Incident Requirements (Must Be Complete Before Incident)

| Requirement | Status Check |
|---|---|
| Decoy wallet funded with believable balance | [ ] Complete |
| Primary holdings in 72h+ timelock | [ ] Complete |
| Multisig with geographically separated co-signer | [ ] Complete |
| Trusted contact established with check-in protocol | [ ] Complete |
| Duress code word/signal agreed with trusted contact | [ ] Complete |
| Family briefed on basic OPSEC | [ ] Complete |
| Law enforcement contact info saved | [ ] Complete |

If any items above are incomplete: stop reading playbooks and go complete those controls first. This playbook is only useful if the pre-conditions exist.

---

## OODA Response: Active Coercion Event

### OBSERVE
- Assess: Are weapons present? Physical harm in progress?
- Assess: What do they want? Transfer? Seed phrase? Device access?
- Assess: Where are family members?
- Assess: Is there communication possible with trusted contact?

### ORIENT
- **Comply to preserve life.** Assets can be replaced. Do not escalate.
- **Route to decoy wallet.** Present the decoy wallet (OPS-06) as your "main" holdings.
- **Use delay tactics:**
  - "The bulk is on a hardware wallet that requires 24 hours to warm up after long storage"
  - "Most of it is in a multisig: I don't have the other signers' keys"
  - "There's a 72-hour timelock on large transactions: the system won't let me send more now"
- **Activate duress signal** if any pre-agreed method is accessible (smart home device, phone with dead-man switch)

### DECIDE
- Transfer from decoy wallet only: maximum loss predetermined
- If unable to activate duress signal: cooperate with attacker demands on decoy wallet while preserving information on true holdings architecture
- Do NOT provide seed phrase or access to main holdings device under any circumstances

### ACT
- Execute transfer from decoy wallet
- Memorize or note any identifying details: voices, physical descriptions, vehicle, accent
- Activate duress signal at first safe opportunity

---

## Post-Incident Response

**Immediate (0-60 minutes post-escape):**
1. Contact law enforcement: 911 (immediate); FBI field office (kidnapping/organized crime)
2. Contact trusted contact: activate emergency protocol
3. Move remaining assets from any potentially exposed wallet to pre-generated cold wallet
4. Revoke all token approvals from any device that was accessed

**Evidence (0-24 hours):**
1. Write down all details of attacker identification before memory fades
2. Record all on-chain transactions made under duress (blockchain forensics evidence)
3. Save all communications
4. Do NOT post on social media: coordinate with law enforcement first

**Recovery:**
- Engage FBI Crypto Unit for investigation support
- Contact Chainalysis or TRM Labs for fund tracing if losses exceed $10,000
- If crypto exchange received coerced funds: contact exchange support immediately with transaction hashes: freezes possible within hours

---

*Playbook: Physical Coercion | CSI CryptoSHIELD v1.1 | Open-Source*
