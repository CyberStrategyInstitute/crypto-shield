# Using the response playbooks

The OODA document routes an incident. A playbook supplies conditional actions. The incident log records the decision, authorization, result, and next owner. A case report explains historical evidence; a tabletop is a synthetic rehearsal. None substitutes for a verified implementation or a qualified responder.

1. Prioritize safety, establish a trusted device/channel, and assign response roles.
2. Observe the actual exposure and select a route below. Several routes may apply.
3. Use only supported, authorized containment. Follow stop conditions when the mechanism is uncertain.
4. Verify resulting authority and financial state; record residual exposure and handoff.
5. Preserve/report evidence and obtain independent approval before resuming consequential activity.

| Signal or category | Route | Verification artifact |
|---|---|---|
| Physical danger | [Physical coercion](physical-coercion.md) | Safe contact and investigator handoff; no required decoy |
| Wallet, key, approval, permit, delegate, or sweeper | [Wallet compromise](wallet-compromise.md) | Authority-specific invalidation/migration result |
| Account or social-platform takeover | [Account takeover](account-takeover.md) | Ownership, sessions, recovery, and grant review |
| Malware or supply chain | [Endpoint/supply chain](endpoint-supply-chain.md) | Credential, artifact, deployment, and signer verification |
| DeFi, bridge, oracle, governance, or market signal | [Protocol exploit](protocol-exploit.md) | Invariant, backing, valuation, role, and exposure reconciliation |
| Agent misuse | [AI agent](ai-agent-compromise.md) | New authorization denied; persistent authority and pending actions reviewed |
| Investment or recovery fraud | [Consumer fraud](consumer-fraud.md) | Payments paused, independent verification and reports |
| Policy, sovereignty, custody, or redemption | [Policy/custody event](policy-custody-event.md) | Dated source, legal scope, rights, and permitted action |
| Extortion | [Extortion](extortion.md) | Safety, system containment, evidence, and qualified review |

The [case register](../intelligence/README.md) covers all 12 categories. The [tabletop pack](../tools/tabletop-exercises.md) gives synthetic prompts and expected decisions. Completion of a rehearsal does not establish live control effectiveness.
