# Bridge and cross-chain risk

<!-- navigation:start -->
[Home](../README.md) | [All pages](../REPOSITORY-MAP.md) | [Domains](../README.md#domains-and-control-counts) | [v2.0 changes](../FRAMEWORK-UPDATE.md) | [Machine-readable index](../metadata/repository-index.json) | [Automation guide](../AUTOMATION.md)
<!-- navigation:end -->

Related control: OCM-07. Related threat: CS-DFI-03. Numerical bridge ratings and the previous approved-bridge list are withdrawn pending a defined model and deployment-specific evidence. Validator count, TVL, audit count, age, and a canonical label cannot establish safety.

## Review each deployed route

| Boundary | Required evidence |
|---|---|
| Message validity | Source and destination contracts, finality assumptions, replay protection, proof or quorum rules, message scope |
| Verifier independence | Actual required and optional thresholds, common operators, keys, infrastructure, and configuration authority |
| Backing and redemption | Locked collateral, mint/burn accounting, liabilities, custody, redemption rights, freeze powers, depeg and insolvency paths |
| Upgrades and emergency access | Owners, modules, upgrade keys, delays, cancellation, pause scope, and bypass paths |
| Optimistic verification | Challenge window, data availability, active watchers, incentives, and censorship or outage behavior |
| Light-client or proof verification | Verifier correctness, source consensus assumptions, implementation, upgrade authority, and failure response |
| Operational dependencies | Relayers, RPCs, sequencers, fee markets, recovery paths, alerts, and independent response owners |

For DVN-style configurations, examine the complete acceptance rule and both directions of the route. Required-list length alone does not establish the effective quorum or independence. No trust model is universally trustless or immune to implementation defects.

## Exposure policy

Aggregate gross outstanding claims and pending transfers across routes, assets, wallets, chains, sessions, and time windows. Define conservative valuation, stale-price and outage handling, atomic reservations, settlement, expiry, and idempotency. Prevent split requests and concurrent calls from exceeding the budget. Separate ordinary limits from exceptional approval.

Test message forgery, replay, conflicting finality, unbacked minting, malicious upgrades, emergency bypasses, unavailable watchers, and correlated verifiers. Test two individually permitted requests whose combined exposure exceeds the cap. A daily counter in one contract does not establish a portfolio-wide loss bound.

## Evidence limits

Historical case amounts and causal classifications remain discovery leads in the [legacy registry](legacy/registry-v1.1.json). Reconstruct primary disclosures, deployed configuration, transactions, affected value, direct loss, frozen funds, and recovery before using any case as validation. This document supplies no current bridge recommendation or production contract implementation.


## Worked case and exercise

The [Ronin reopening account](../intelligence/reports/ronin-bridge.md) illustrates why user backing, DAO liabilities, replacement capital, and stolen-fund recovery need separate accounting. It is an operator account, not independent solvency validation or a current bridge recommendation. Use the DeFi tabletop and [exposure-budget template](../tools/templates/exposure-budget.json) to record an invariant, authorization, expected block, and verification result.
