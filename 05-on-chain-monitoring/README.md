# Domain 05: On-Chain Monitoring and Transaction Defense (OCM)

CSI CryptoSHIELD 1.2 proposal | Integrity review: November 7, 2026

Verify transaction intent and resulting authority before signing; monitor afterward. Simulation observes a particular state and payload. Finality does not prevent every form of restitution, seizure, issuer freeze, or negotiated return.

## Controls

| Control ID | Control | Priority |
|---|---|---|
| OCM-01 | Transaction Simulation | CRITICAL |
| OCM-02 | Real-Time Wallet Monitor | HIGH |
| OCM-03 | Authority monitoring and revocation | HIGH |
| OCM-04 | Mempool Awareness | HIGH |
| OCM-05 | MEV Protection | MEDIUM |
| OCM-06 | Address Poisoning Detection | HIGH |
| OCM-07 | Bridge verification and backing assessment | HIGH |
| OCM-08 | Smart Contract Audit Verification | HIGH |
| OCM-09 | Anomaly Detection | HIGH |
| OCM-10 | Permit/Signature Intelligence | CRITICAL |

## Transaction and authority checks

OCM-01 binds simulation and decoding to the exact payload signed, chain state, contract implementation, and resulting permissions. Check chain, account, nonce, recipient, calldata, value, batch actions, and authority changes independently. Simulation can miss state changes, upgrade behavior, delayed actions, and off-chain signatures. Fail closed when required verification is unavailable.

OCM-02 tests alerts and escalation with safe transactions. An alert does not reverse execution. On suspected compromise, use the [wallet decision tree](../playbooks/wallet-compromise.md), not a universal revoke-and-move sequence.

OCM-03 inventories all spending and delegation authority with WKS-07. Review at least monthly and after a relevant incident or change. Automatic revocation requires explicitly authorized signing capability; a monitor alone cannot revoke. Off-chain signatures and non-ERC-20 authorities require their own invalidation paths.

OCM-04 and OCM-05 assess chain-supported private submission and MEV controls. Private RPC providers and builders remain trust dependencies. Private submission does not remove key compromise or guarantee a rescue.

OCM-06 verifies the complete address independently. OCM-07 uses the [bridge appendix](../taxonomy/bridge-risk-appendix.md), including backing and redemption. Validator counts, audits, age, TVL, and a canonical label cannot establish safety.

OCM-08 matches audit scope and deployed bytecode, dependencies, upgrade authority, unresolved findings, and changes since review. An audit is not an endorsement. OCM-09 records monitoring coverage and false negatives. OCM-10 decodes typed data, domain, chain ID, verifying contract, spender, value, nonce, and expiry. Reject opaque signatures. EIP-712 formatting does not establish benign intent.


These are control specifications, not deployed protections. The [review and evidence backlog](../reviews/2026-11-07-baseline-integrity.md) records verification limits. Historical artwork is retired from active guidance; see the [asset register](../assets/README.md).
