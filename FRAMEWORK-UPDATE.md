# CryptoSHIELD 2.0.0 framework update

Proposed major version. This expands the framework from 100 to 112 controls: 105 operational controls plus seven cross-domain governance controls. All 100 existing IDs remain; 12 new IDs make previously embedded or missing requirements independently assessable. The taxonomy retains 44 threats across 12 categories. No replacement CTRS ratings are adopted.

## Why a major version

The framework moves from a key-centric model to explicit financial authority, aggregate exposure, backing, approval independence, and authority lifecycle governance. Registry/event contracts change incompatibly, scoring and assessment contracts change, and several unsafe procedures are replaced. Version 2.0.0 describes a major specification change. It does not claim completion of outstanding research, implementation, or efficacy validation. No release tag is created by the PR.

The version choice follows the [Semantic Versioning rule for incompatible public-contract changes](https://semver.org/). Adding controls alone could justify a minor version; removing or changing scoring, assessment, and data contracts makes this a major update.

## Added controls

| ID | New control | Finding addressed |
|---|---|---|
| [CDG-06](00-cross-domain/README.md#cdg-06-evidence-provenance-and-claim-lifecycle) | Evidence provenance and claim lifecycle | Unsupported incident, loss, attribution, and efficacy claims lack reproducible provenance. |
| [CDG-07](00-cross-domain/README.md#cdg-07-versioned-assessment-and-compatibility-governance) | Versioned assessment and compatibility governance | Conflicting CTRS models, ranges, schemas, and tables produce incompatible decisions. |
| [WKS-11](01-wallet-key-sovereignty/README.md#wks-11-financial-authority-inventory) | Financial authority inventory | Key inventories omit approvals, permits, modules, delegates, sessions, signers, and recovery powers. |
| [WKS-12](01-wallet-key-sovereignty/README.md#wks-12-authority-revocation-and-recovery-verification) | Authority revocation and recovery verification | Revoking an allowance or stopping an app can leave keys, signatures, or delegates active. |
| [WKS-13](01-wallet-key-sovereignty/README.md#wks-13-hardware-procurement-and-whole-device-trust) | Hardware procurement and whole-device trust | Authentic firmware or a secure element does not establish whole-device integrity. |
| [OCM-11](05-on-chain-monitoring/README.md#ocm-11-aggregate-exposure-budget-enforcement) | Aggregate exposure budget enforcement | Per-wallet balances and transaction-count limits do not bound principal-wide financial exposure. |
| [OCM-12](05-on-chain-monitoring/README.md#ocm-12-bridge-backing-and-redemption-invariants) | Bridge backing and redemption invariants | A valid cross-chain message can still create an unbacked or nonredeemable claim. |
| [AAS-11](07-ai-agent-security/README.md#aas-11-independent-human-financial-authorization) | Independent human financial authorization | A human gate is ineffective if the agent controls approval, recovery, or policy administration. |
| [AAS-12](07-ai-agent-security/README.md#aas-12-agent-shutdown-and-persistent-authority-containment) | Agent shutdown and persistent-authority containment | Process shutdown leaves on-chain permissions, signed intents, and signing-service credentials usable. |
| [GCS-11](08-governance-compliance-sovereignty/README.md#gcs-11-bounded-emergency-authority) | Bounded emergency authority | Generic timelock overrides can become unrestricted transfer or upgrade authority. |
| [GCS-12](08-governance-compliance-sovereignty/README.md#gcs-12-governance-capture-and-lasting-authority-review) | Governance capture and lasting-authority review | Temporary voting power or delegated influence may grant lasting control. |
| [GCS-13](08-governance-compliance-sovereignty/README.md#gcs-13-custody-liabilities-and-asset-rights-assessment) | Custody liabilities and asset-rights assessment | On-chain balances and custody labels do not establish liabilities, legal title, or redemption. |

Each new domain definition includes a requirement and acceptance criteria. The registry maps applicable threat IDs to the new controls; CDG-07 governs assessment models across the framework rather than one threat.

## Material updates to existing controls

| Existing IDs | Before | 2.0.0 change |
|---|---|---|
| WKS-01 through WKS-10 | Key custody, multisig, timelock, approval, and cold-storage heuristics | Preserve IDs; qualify hardware and timelock boundaries, require full-intent review, and connect WKS-11/12/13 authority, lifecycle, and hardware evidence |
| EDD-01/02/04/07/08/10 | Universal endpoint guarantees, partial address checks, and incomplete isolation assumptions | Define tested execution boundaries, retain detection, require complete address verification, and document trusted-runtime/network residual risks |
| OPS-05/06/10 | Prescribed decoy/deception and duress actions | Life safety first; decoys optional; signals only when safe; no forced refusal or invented device limits |
| SMS-01/02/12/13/14/15 | Uniform platform capabilities; database clearance, cooling-off, fee/recovery overclaims | Supported authentication and recovery checks; no-report-found is not clearance; distinguish suspicious unlock payments from disclosed fees and lawful recovery |
| OCM-01/02/03/07/08/10 | Simulation, alerting, approvals, bridge and audit checks treated too broadly | Bind to actual payload and authority; cover persistent grants; route aggregate budgets and backing invariants to OCM-11/12 |
| SCD-02/03/07/08/09 | Invalid provenance command, broad script exception, and artifact-safety conflation | Supported signature/provenance checks; isolated build exceptions; separate identity, inventory, and code behavior |
| AAS-01/02/03/06/08/09/10 | Keylessness, hashes, prompts, count caps, and allowlists treated as stronger boundaries | Separate signer policy; treat memory/output as untrusted; AAS-06 applies OCM-11 aggregate policy at the agent gate; AAS-11/12 own independent approval and shutdown lifecycle |
| GCS-03/04/05/06/07 | Broad legal conclusions, custody heuristics, generic response and governance assumptions | Jurisdiction-specific evidence, liability assessment, scenario-specific response, bounded emergency powers, and capture testing |
| CFD-03/04/07/08/10 | Test withdrawals, fees, recovery, video identity, and user addresses treated as conclusive | Separate warning signs from proof; verify identity independently; distinguish custody claims, liabilities, and lawful recovery |

## Framework-wide repairs

- Separate strict registry, event, control, and evidence contracts; version registry/events as 2.0.
- Suspend contradictory CTRS and unvalidated self-assessment tiers; retain historical data.
- Generate control counts, threat/control mappings, and the unscored assessment; block stale or invalid content in CI.
- Replace blanket incident steps with authority-specific response, including sweepers and unused permits.
- Correct research status and qualify unsupported claims and companion mappings; retire contradictory historical artwork.

## Migration and evidence

Use [data migration](metadata/README.md). Existing IDs are preserved; new controls extend each assessment rather than silently replacing earlier IDs. Treat all new control tests as acceptance requirements, not evidence that an implementation has passed. The [review backlog](reviews/2026-11-07-baseline-integrity.md) remains open for original-source research and implementation qualification.
