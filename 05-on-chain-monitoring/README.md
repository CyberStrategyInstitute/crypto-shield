<div align="center">

<img src="../assets/Domain 05 On-Chain Monitoring and Transaction Defense (OCM).png" alt="Domain 05 On-Chain Monitoring and Transaction Defense (OCM)" width="100%" />
</div>


# Domain 05: On-Chain Monitoring and Transaction Defense (OCM)

**CSI CryptoSHIELD Framework v1.1**
Cyber Strategy Institute | Classification: Open-Source | Sovereignty-First

---

## Domain Philosophy

Every blockchain transaction is permanent, public, and irreversible. There are no chargebacks. There is no fraud department. The only defense is prevention: and the only way to prevent what you cannot see is to make everything visible before it executes.

Domain 05 establishes the monitoring, simulation, and transaction hygiene stack that closes the gap between "I think I'm transacting safely" and "I have verified every byte of this transaction on an independent device before signing." That gap is where $3.4 billion walked out the door in 2025.

---

## Controls

| Control ID | Control | Implementation | Priority |
|---|---|---|---|
| OCM-01 | Transaction Simulation | Simulate every transaction in Tenderly/Revoke.cash before signing | CRITICAL |
| OCM-02 | Real-Time Wallet Monitor | Alerts on any unexpected outgoing transaction; immediate notification | HIGH |
| OCM-03 | Token Approval Monitoring | Monitor all open approvals; auto-revoke after 30 days of inactivity | HIGH |
| OCM-04 | Mempool Awareness | Understand transaction mempool exposure; use private RPC for large transactions | HIGH |
| OCM-05 | MEV Protection | Use MEV-resistant routing (Flashbots Protect, private mempool) | MEDIUM |
| OCM-06 | Address Poisoning Detection | Verify full address hex before every outgoing transaction | HIGH |
| OCM-07 | Bridge Risk Assessment | Evaluate verifier design for any bridge before use; single-verifier = avoid | HIGH |
| OCM-08 | Smart Contract Audit Verification | Only interact with audited contracts from reputable firms; check audit recency | HIGH |
| OCM-09 | Anomaly Detection | Deploy behavioral monitoring for unusual transaction patterns | HIGH |
| OCM-10 | Permit/Signature Intelligence | Understand all EIP-712 structured data before signing | CRITICAL |

---

## Control Implementation Detail

### OCM-01: Transaction Simulation: Mandatory Execution Gate

**Problem:** Transactions submitted to a hardware wallet for signing display only high-level summaries. The raw calldata: which determines what actually executes: is invisible to the user without simulation.

**The Gate Principle:** This is not a pre-signing check you can skip when you're confident. It is a mandatory execution gate. The rule: **if you cannot simulate it, you cannot sign it.** No exceptions. No "I trust this protocol." No "I've done this before." Every unsigned transaction that cannot be simulated is an unsigned transaction that does not get signed.

Why the gate framing matters: A "check" is optional by definition. Security culture built around optional checks produces systematic failures when stress, urgency, or routine override the check. A gate is architectural. It is either open or it is not. CryptoSHIELD treats OCM-01 as a gate: the last technical verification before value leaves your control.

**Realization:** The Radiant Capital $50M exploit succeeded despite Tenderly simulation and manual review because attackers manipulated the displayed values while the actual signed payload was malicious. Simulation reduces risk but requires independent verification of the simulation output itself.

**Implementation Tools:**
- **Tenderly:** Simulate before signing at `tenderly.co/simulator`
- **Revoke.cash:** Check and revoke existing approvals at `revoke.cash`
- **Phalcon Block Sec:** Transaction simulation with decoded calldata
- **Etherscan Transaction Decoder:** Manually decode calldata for any transaction

**Simulation Checklist:**
```
Before signing any transaction: this is the gate:
[ ] Simulated in Tenderly: outcome matches expectation
[ ] Token transfers in simulation match your intent exactly
[ ] No unexpected contract interactions in simulation trace
[ ] Gas usage is within expected range for this operation type
[ ] Recipient address verified on independent device (not browser copy-paste)
[ ] If simulation fails to run: do not sign. No exceptions.
```

---

### OCM-02: Real-Time Wallet Monitor

**Setup:**
- **Etherscan/Polygonscan Alerts:** Free email alerts on any transaction from your address
- **Nansen Portfolio:** Real-time push notifications for wallet activity
- **Hal.app:** Custom on-chain monitoring with complex trigger logic
- **Chainpatrol:** Protocol-level monitoring for DeFi positions

**Alert Thresholds:**
- Any outgoing transaction over $100: immediate notification
- Any token approval: immediate notification
- Any interaction with a new (unverified) contract: immediate notification
- Large incoming transaction: notification for reconciliation

**Response Protocol on Unexpected Alert:**
1. Do NOT interact with anything until investigation is complete
2. From a separate device: check Etherscan for the transaction details
3. Identify the contract interacted with; check its audit status and age
4. If compromise suspected: execute emergency cold wallet migration immediately (Revoke all approvals → Move remaining funds to pre-generated cold address)

---

### OCM-03: Token Approval Monitoring

**Why Approvals Are Dangerous:**
When you interact with a DeFi protocol, you typically grant it permission to spend your tokens up to a specified amount (often unlimited). These approvals persist indefinitely after the interaction. A protocol exploit, upgrade, or admin key compromise can drain all approved tokens at any time.

CSI research finding: 68% of DeFi losses involve exploitation of existing token approvals rather than exploitation of active transactions.

**Implementation:**
- Monthly audit at revoke.cash (Ethereum), bscscan.com/tokenapprovalchecker (BSC), or equivalent
- Revoke all approvals for protocols you no longer actively use
- Set specific approval amounts instead of "unlimited" when DeFi UI allows it
- After any DeFi interaction, revoke the approval if you don't expect to use the protocol again within 30 days

**Tools by Chain:**
| Chain | Tool |
|---|---|
| Ethereum | revoke.cash |
| Polygon | revoke.cash (multi-chain) |
| Arbitrum | revoke.cash (multi-chain) |
| Solana | sol-incinerator.com / Phantom built-in |
| BNB Chain | bscscan.com/tokenapprovalchecker |

---

### OCM-04: Mempool Awareness

**What the Mempool Is:**
Before a transaction is included in a block, it sits in the public mempool: visible to anyone, including MEV bots. Large transactions in the mempool are frontrun, sandwiched, and exploited before they finalize.

**Private RPC Endpoints:**
For any transaction over $10,000, use a private RPC to bypass the public mempool:
- **Flashbots Protect RPC:** `rpc.flashbots.net`: sends transactions directly to block builders
- **MEV Blocker:** `mev-blocker.io`: open source MEV protection
- **Alchemy Private:** Available on Alchemy's RPC tier

**Configuration:** In MetaMask or other wallet, add the private RPC as a custom network endpoint and switch to it before large transactions.

---

### OCM-06: Address Poisoning Detection

**The Attack:**
An attacker sends you a tiny transaction (often 0 USDC or 0.0001 ETH) from an address that looks nearly identical to an address you've recently transacted with. The goal: when you copy a recipient from your transaction history, you accidentally copy the attacker's address instead.

**Detection Protocol:**
```
Before EVERY outgoing transaction:
1. Write down or display the first 6 and last 6 characters of the intended recipient
2. Compare against the address displayed in your hardware wallet SCREEN (not browser)
3. Verify all characters: not just the first/last few
4. If transaction history contains a near-identical address you didn't initiate: poisoning detected
```

**Never:**
- Copy recipient addresses from transaction history without full hex verification
- Assume your browser's clipboard contains what you last copied (clipboard hijacking: CS-MAL-01)

---

### OCM-07: Bridge Risk Assessment

**The Bridge Risk Framework:**
Cross-chain bridges are the single highest-loss attack surface in DeFi history: $2.88 billion stolen cumulatively through April 2026.

**Risk Assessment Matrix:**
| Risk Factor | Safe | Caution | Avoid |
|---|---|---|---|
| Verifier count | 15+ diverse validators | 5-14 validators | 1-3 validators |
| Time since deployment | 2+ years | 6-24 months | Less than 6 months |
| Audit count | 3+ from reputable firms | 1-2 audits | Unaudited |
| TVL (proxy for battle-testing) | >$500M | $50M-$500M | <$50M |
| Admin key design | Multi-sig, timelocked | Multi-sig, no timelock | EOA or opaque |
| Incident history | None | Minor, resolved | Major exploit |

**High-Profile Bridge Failures (for reference):**
- Ronin Network: $625M (March 2022): 5 of 9 validators compromised
- Wormhole: $320M (February 2022): signature verification bug
- Nomad: $190M (August 2022): initialization error
- KelpDAO: $292M (April 2026): single-verifier LayerZero bridge

**Rule:** If a bridge uses a single verifier or has fewer than 5 independent validators, do not bridge assets through it regardless of TVL or marketing.

---

### OCM-10: Permit/Signature Intelligence

**`eth_sign`: Fully Deprecated. Never Use. Never Approve.**

Before covering EIP-712, a hard rule: `eth_sign` is a legacy signing method that signs arbitrary byte sequences with zero human-readable context. Any dApp requesting an `eth_sign` signature is either extremely outdated or malicious. MetaMask displays a warning for `eth_sign` and recommends rejection. Ledger and Trezor display no transaction details for `eth_sign`: you are signing blind.

**Rule:** If a dApp requests `eth_sign`, reject the request and close the site. Report the URL to Scam Sniffer (scamsniffer.io) and Chainabuse (chainabuse.com). Do not attempt to verify whether the request is legitimate: legitimate protocols do not use `eth_sign`.

**What EIP-2612 Permit Signatures Do:**
Unlike a standard token approval (which requires a gas-paying transaction), a permit signature is an off-chain signature that grants spending permissions. It can be submitted by anyone: meaning you can sign a malicious permit without ever sending a transaction yourself.

**What to Look For Before Signing Any EIP-712 Message:**
```
{
  "domain": {
    "name": "[Should match the protocol you're interacting with]",
    "verifyingContract": "[Should match the protocol's known contract address]"
  },
  "message": {
    "spender": "[WHO will be able to spend your tokens: verify this address]",
    "value": "[HOW MUCH they can spend: should never be MAX_UINT256 unless understood]",
    "deadline": "[WHEN does this permission expire: short deadline preferred]"
  }
}
```

**Red Flags:**
- `spender` address you don't recognize
- `value` set to `115792089237316195423570985008687907853269984665640564039457584007913129639935` (unlimited)
- `deadline` far in the future (months or years)
- Permit request arriving via DM or unsolicited interaction

**Rule:** Permit requests from unsolicited sources (DMs, emails, popup sites) are always adversarial. Never sign them.

---

## Transaction Defense Stack: Full Architecture

```
TRANSACTION INITIATION
        │
        ▼
[ OCM-04: Private RPC? ] → If large: yes
        │
        ▼
[ OCM-10: Decode signature/calldata ]
        │
        ▼
[ OCM-01: Simulate in Tenderly ]
        │
        ▼
[ OCM-06: Address poisoning check ]
        │
        ▼
[ Hardware wallet screen verification ]
        │
        ▼
SIGN AND BROADCAST
        │
        ▼
[ OCM-02: Confirm alert received ]
```

Every layer is bypass-resistant only if the previous layer is also applied. Simulation without address verification is not full defense.

---

## Research References

- DefiLlama Hacks Database: lifetime $11.81B across 518 incidents
- CS-DFI-03 (Bridge Exploit): $2.88B cumulative, largest single attack surface
- OCM-03 data: 68% of losses involve pre-existing token approvals
- Research Note 004: AI Agent Attack Surface → `research/004_ai_agent_attack_surface.md`

---

*CSI CryptoSHIELD Framework v1.1 | Domain 05: On-Chain Monitoring and Transaction Defense*
*Cyber Strategy Institute | Open-Source | Sovereignty-First*
