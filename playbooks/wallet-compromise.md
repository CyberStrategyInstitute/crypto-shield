# Playbook: Wallet Compromise Response

**CSI CryptoSHIELD Framework v1.1**
Threats: CS-WAL-01 through CS-WAL-05, CS-MAL-01, CS-MAL-02 | Domains: 01 (WKS), 02 (EDD), 05 (OCM)

---

## Threat Profile

Wallet compromise is the most common high-impact crypto attack: seed phrase theft, malicious signature grants, clipboard hijacking, address poisoning, and DNS hijacks collectively account for the majority of individual holder losses. The attack surface ranges from the physical (hardware wallet recovery phrase) to the digital (browser-based malicious approval).

**68% of DeFi losses involve exploitation of pre-existing token approvals**: not active transaction attacks. Many victims don't know they've been compromised until the drain occurs.

---

## Attack Type Identification

| Attack Type | Indicator | Threat ID |
|---|---|---|
| Seed phrase exposure | Funds drained from multiple wallets; HD wallet entirely emptied | CS-WAL-01 |
| Address poisoning | Funds sent to slightly-wrong address; poisoned address in TX history | CS-WAL-02 |
| DNS/frontend hijack | Wallet connection request on known protocol site; unexpected contract address | CS-WAL-03 |
| Malicious signature | Approval granted unknowingly; specific token/amount drained | CS-WAL-04 |
| Clipboard hijacking | Pasted address differs from copied address | CS-MAL-01 |
| InfoStealer | Funds drained; device shows unusual network activity | CS-MAL-02 |

---

## OODA Response: Wallet Compromise Suspected

### OBSERVE
- Is there an unexpected outgoing transaction in your wallet history?
- Did you receive an unexpected alert (OCM-02)?
- Did the amount sent go to an address you did not intend?
- Are any token approvals shown in revoke.cash that you did not knowingly grant?

### ORIENT
- **Speed matters.** Every minute of delay allows the attacker to move funds further from recovery.
- Do NOT use the potentially compromised device for response: use a second, clean device.
- Identify: What is the likely attack type? (Table above)
- Identify: What wallets/devices might share exposure? (If seed phrase: all wallets from that seed)

### DECIDE

**If funds are still in compromised wallet (not yet drained):**
- Immediate priority: move remaining funds to a pre-generated cold wallet address
- This requires having a pre-generated cold wallet address ready: if you don't: generate on a clean device first

**If funds are draining or have been drained:**
- Accept the loss from compromised wallet
- Contain: ensure remaining funds in unaffected wallets are isolated from compromised device/seed

**For malicious approval (not yet drained):**
- Immediate: revoke the approval at revoke.cash from a clean device
- If approval involved a front-running risk: use private RPC (Flashbots Protect) for the revoke transaction

### ACT

**Step 1: Emergency Containment (0-5 minutes)**
```
From a clean device:
1. Navigate to revoke.cash
2. Connect the compromised wallet (read-only, watch mode if available)
3. Identify and revoke ALL active token approvals
4. If seed compromise suspected: generate new wallet on clean device; do NOT reuse any address from compromised seed
```

**Step 2: Asset Migration (5-30 minutes)**
```
1. Send all remaining funds from compromised wallet to new clean wallet address
2. Verify recipient address on hardware wallet screen (independent device if possible)
3. Confirm transaction via OCM-02 alert
4. Once confirmed: treat compromised wallet/seed as burned; never use again
```

**Step 3: Device Isolation**
```
1. Disconnect compromised device from all networks
2. Do NOT use it for any crypto operations again until forensic wipe
3. For InfoStealer: full OS reinstall required; do not trust partial cleanup
```

**Step 4: Reporting and Forensics**
```
1. Record all transaction hashes related to the attack
2. Report to FBI IC3 (ic3.gov)
3. Report attacker wallet address to Chainabuse
4. If losses >$10,000: contact TRM Labs or Chainalysis for tracing
5. If exchange received stolen funds: contact exchange support immediately
```

---

## Address Poisoning: Special Response

If you discover you sent funds to a poisoned address (slightly-wrong address in TX history):

1. Verify the actual intended recipient's address via out-of-band communication
2. Confirm the funds are NOT at your intended destination
3. Record the poisoned address and report to Chainabuse
4. If destination was a CEX deposit address: contact CEX support: possible recovery within hours
5. If on-chain to an EOA: contact ZachXBT or blockchain forensics firms; public exposure can sometimes create pressure for return (rare)

---

## Post-Incident Hardening

After any wallet compromise, these controls must be implemented before resuming operations:

| Control | Action |
|---|---|
| WKS-01 | New hardware wallet for primary storage (not the same device) |
| WKS-04 | New seed phrase; destroy and verify destruction of old backup |
| EDD-01 | Reinstall OS or use new dedicated device |
| EDD-04 | Establish clipboard verification habit |
| OCM-03 | Establish token approval monitoring for new wallet |
| SMS-05 | Full URL verification protocol refresh |

---

*Playbook: Wallet Compromise | CSI CryptoSHIELD v1.1 | Open-Source*
