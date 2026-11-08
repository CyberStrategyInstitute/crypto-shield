# Domain 01: Wallet and Key Sovereignty (WKS)

CSI CryptoSHIELD 1.2 proposal | Integrity review: November 7, 2026

Protect keys, verify what is signed, and inventory every authority that can move assets. An uncompromised key does not prevent misuse of a valid approval, compromised delegate, or unsafe contract.

## Controls

| Control ID | Control | Priority |
|---|---|---|
| WKS-01 | Hardware wallet and device-integrity review | CRITICAL |
| WKS-02 | Multisig with Geographic Diversity | CRITICAL |
| WKS-03 | Tiered Timelock on Governance Transactions | CRITICAL |
| WKS-04 | Seed Phrase Offline Sovereignty | CRITICAL |
| WKS-05 | No Blind Signing | CRITICAL |
| WKS-06 | Independent Address Verification Protocol | HIGH |
| WKS-07 | Token Approval Revocation Protocol | HIGH |
| WKS-08 | Permit Scam Recognition | HIGH |
| WKS-09 | Cold storage and total accessible exposure | CRITICAL |
| WKS-10 | Watch-Only Wallet for Household Members | HIGH |

## Wallet implementation boundaries

WKS-01: Buy through an authenticated manufacturer channel. Initialize fresh recovery material on the device and follow its supported authenticity checks. Never accept a supplied seed. Distinguish procurement provenance, firmware signature, secure-element attestation where available, and whole-device integrity. No single check establishes all four. PIN capabilities and key-storage designs vary by device.

WKS-02: Separate signing devices, locations, operators, communication channels, and recovery paths. Inventory owners, threshold, modules, delegates, session keys, and emergency authorities. Geographic separation alone does not establish independent trust.

WKS-03: Apply audited delays to specified governance paths. The historical 72-hour, 7-day, and 14-day thresholds are planning defaults, not validated efficacy thresholds. Verify queue monitoring, cancellation, and all upgrade or bypass paths. A governance timelock does not delay ordinary wallet transfers or already-granted spending authority. Emergency powers may pause or cancel within a bounded scope; they must not silently permit arbitrary transfers or upgrades.

WKS-04: Generate recovery material on a trusted device and keep it offline with controlled physical access. Use only a supported, tested threshold-backup scheme rather than manually splitting words. Verify recovery on trusted hardware before migration. Recovery may legitimately require seed entry into the device itself. Never enter it into a website, chat, unsolicited app, or ordinary computer form.

WKS-05 and WKS-06: Bind review to the exact chain, account, contract, function, calldata, value, nonce, and resulting permissions. Verify the complete recipient on an independent trusted display. A compromised device or firmware remains a risk. Inspect batches, upgrades, modules, delegatecalls, and approvals, not just transfer amounts.

WKS-07 and WKS-08: Inventory ERC-20 allowances, NFT operator grants, permits, Permit2 permissions, smart-account modules, delegates, sessions, signing services, and recovery authority on every chain used. Record principal, scope, limits, expiry, revocation method, owner, and test evidence. Off-chain signatures may not appear in an allowance viewer. Ordinary allowance revocation may not invalidate an unused permit. Use the mechanism's supported nonce, expiry, lockdown, or authority-removal path and verify the result.

WKS-09: Set an explicit exposure budget for hot wallets, approvals, delegated authority, open positions, bridges, and custody. The historical 90/10 allocation is a planning heuristic. It bounds loss only if every accessible authority is inside that allocation; cold balances with live approvals may remain exposed.

WKS-10: Watch-only access avoids granting signing authority but can expose balances and relationships. Preserve a documented, tested estate and recovery process for authorized successors. Limited knowledge does not prevent threats against family members.

## Verification

Test setup and recovery with non-production funds. Demonstrate that a compromised ordinary signer cannot bypass threshold, delay, revocation, or recovery boundaries. Record unsupported paths and residual exposure. For an active incident, use the [wallet decision tree](../playbooks/wallet-compromise.md).


These are control specifications, not deployed protections. The [review and evidence backlog](../reviews/2026-11-07-baseline-integrity.md) records verification limits. Historical artwork is retired from active guidance; see the [asset register](../assets/README.md).
