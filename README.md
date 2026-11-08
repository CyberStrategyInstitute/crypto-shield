![CryptoSHIELD v2.0.0: assets and authority, systems and agents, people and trust, supported by sovereignty governance](assets/CryptoSHIELD%20v2.0.png)

# CSI CryptoSHIELD v2.0.0

<!-- navigation:start -->
[Home](README.md) | [All pages](REPOSITORY-MAP.md) | [Domains](README.md#domains-and-control-counts) | [v2.0 changes](FRAMEWORK-UPDATE.md) | [Machine-readable index](metadata/repository-index.json) | [Automation guide](AUTOMATION.md)
<!-- navigation:end -->

[![Version: 2.0.0 published](https://img.shields.io/badge/Version-2.0.0_published-orange?style=flat-square)](CHANGELOG.md)
[![Documentation: CC BY-SA 4.0](https://img.shields.io/badge/Docs-CC_BY--SA_4.0-lightgrey?style=flat-square)](LICENSE)
[![Code: MIT](https://img.shields.io/badge/Code-MIT-yellow?style=flat-square)](LICENSE)
[![Scope: 112 controls](https://img.shields.io/badge/Scope-112_controls-2563eb?style=flat-square)](#domains-and-control-counts)
[![Taxonomy: 46 threats, 12 categories](https://img.shields.io/badge/Taxonomy-46_threats_%7C_12_categories-7c3aed?style=flat-square)](taxonomy/registry-table.md)

[![New: 12 controls](https://img.shields.io/badge/NEW-12_controls-15803d?style=flat-square)](FRAMEWORK-UPDATE.md#added-controls)
[![Data contracts: 2.0](https://img.shields.io/badge/Data_contracts-2.0-0891b2?style=flat-square)](metadata/README.md)
[![CTRS: suspended](https://img.shields.io/badge/CTRS-suspended-b45309?style=flat-square)](taxonomy/ctrs-scoring.md)
[![Mappings: verification pending](https://img.shields.io/badge/Mappings-verification_pending-64748b?style=flat-square)](FRAMEWORK-ALIGNMENT.md)
[![Repository checks](https://github.com/CyberStrategyInstitute/crypto-shield/actions/workflows/taxonomy-lint.yml/badge.svg?branch=main)](https://github.com/CyberStrategyInstitute/crypto-shield/actions/workflows/taxonomy-lint.yml)

CryptoSHIELD specifies controls for crypto holders, developers, and protocol teams. It covers wallets and financial authority, endpoint defense, physical exposure, social platforms, on-chain activity, supply chains, agents, governance, and consumer fraud.

<!-- summary:start -->
**CryptoSHIELD v2.0.0:** 46 threats across 12 categories; 105 operational controls in nine domains, plus 7 cross-domain governance controls, for 112 total. CTRS scoring is suspended. Historical scores are unvalidated and must not drive new rankings or protection claims.
<!-- summary:end -->

[Review and remaining work](reviews/2026-11-07-baseline-integrity.md) | [Threat registry](taxonomy/registry-table.md) | [Incident response](OODA-PLAYBOOK.md) | [Hardening sprint](tools/30-day-hardening-sprint.md) | [Self-assessment](tools/sovereignty-self-assessment.md)

## What changed in v2.0.0

**v2.0.0 is published and merged into main.** It is a major framework update: registry, event, scoring, and assessment contracts changed incompatibly. [Full control comparison](FRAMEWORK-UPDATE.md) | [Changelog](CHANGELOG.md) | [Migration guide](metadata/README.md).

The tags below compare v2.0.0 with the prior framework baseline. They describe changes in this version, not continuing publication dates.

| Status | Area | Added or updated in v2.0.0 |
|---|---|---|
| ![NEW](https://img.shields.io/badge/NEW-15803d?style=flat-square) | [12 controls](FRAMEWORK-UPDATE.md#added-controls) | Financial authority, revocation, hardware trust, exposure budgets, bridge backing, independent approval, shutdown, emergency powers, governance capture, custody liabilities, and evidence/version governance. |
| ![UPDATED](https://img.shields.io/badge/UPDATED-b45309?style=flat-square) | [Control framework](FRAMEWORK-UPDATE.md) | All 100 existing IDs retained; requirements revised across nine operational domains and cross-domain governance. Total: 112 controls. |
| ![NEW](https://img.shields.io/badge/NEW-15803d?style=flat-square) | [Threat classes](taxonomy/registry-table.md) | CS-MKT-04 price/collateral manipulation and CS-SOV-03 policy/provider access restrictions. Total: 46 classes across the existing 12 categories. |
| ![NEW](https://img.shields.io/badge/NEW-15803d?style=flat-square) | Framework overview | Three visual groups: Assets & Authority, Systems & Agents, and People & Trust, supported by cross-domain governance. These organize the existing domains. |
| ![NEW](https://img.shields.io/badge/NEW-15803d?style=flat-square) | [Research notes 004-006](research/README.md) | Substantive agent-authority, runtime supply-chain, and investment-fraud notes replaced research stubs. Notes 001-003 and 007 were updated. All seven remain source-checked drafts awaiting independent review. |
| ![NEW](https://img.shields.io/badge/NEW-15803d?style=flat-square) | [Intelligence library](intelligence/README.md) | 13 source-checked historical report/event pairs covering all 12 categories, with source classifications and provisional mappings preserved. |
| ![UPDATED](https://img.shields.io/badge/UPDATED-b45309?style=flat-square) | [Playbooks](playbooks/README.md) | Six added response playbooks; nine total, with a routing guide and authority-specific decisions. |
| ![NEW](https://img.shields.io/badge/NEW-15803d?style=flat-square) | [Exercises and tools](tools/README.md) | 12 synthetic tabletop exercises, three evidence templates, a filled example, and local case lookup. |
| ![UPDATED](https://img.shields.io/badge/UPDATED-b45309?style=flat-square) | [Taxonomy and data contracts](metadata/README.md) | Separate registry/event contracts, migration guidance, generated references, and blocking consistency checks. CTRS suspended; historical scores preserved without replacement rankings. |

## Start here

| Your task | Entry point |
|---|---|
| Respond to immediate physical danger | [Physical coercion](playbooks/physical-coercion.md) |
| Respond to wallet, approval, key, or device exposure | [Wallet decision tree](playbooks/wallet-compromise.md) |
| Respond to suspected investment fraud | [Consumer fraud](playbooks/consumer-fraud.md) |
| Plan holder defenses | [30-day sprint](tools/30-day-hardening-sprint.md) |
| Review protocol or agent authority | [Wallet controls](01-wallet-key-sovereignty/README.md), [agent controls](07-ai-agent-security/README.md), and [bridge boundaries](taxonomy/bridge-risk-appendix.md) |
| Contribute evidence or controls | [Contribution guide](CONTRIBUTING.md) |

## Scope and enforcement boundaries

Sovereignty first means understanding who can move, freeze, upgrade, recover, or redeem assets. Possessing a private key is only one authority path. Approvals, permits, modules, delegates, sessions, signing services, issuers, bridges, custodians, and recovery mechanisms need separate review.

This repository supplies specifications and validation tools. It does not install endpoint protection, operate a signer, or establish compliance, solvency, physical safety, or universal prevention. Default-deny policies can block or contain unapproved execution within a tested scope. Contained code may execute. Valid signatures and approved code can still cause harmful actions.

Physical safety takes priority over assets. Timelocks cover specified paths and cannot guarantee safety under coercion. Use scenario-specific response; blanket revocation and migration instructions can increase loss when keys, permits, delegates, or sweepers are involved.

![Framework responsibility map](assets/framework-architecture.svg)

## Domains and control counts

<!-- inventory:start -->
| Domain | Controls | Scope |
|---|---|---|
| [00-cross-domain](00-cross-domain/README.md) | 7 | Cross-domain governance |
| [01-wallet-key-sovereignty](01-wallet-key-sovereignty/README.md) | 13 | Operational |
| [02-endpoint-device-defense](02-endpoint-device-defense/README.md) | 10 | Operational |
| [03-opsec-physical-security](03-opsec-physical-security/README.md) | 10 | Operational |
| [04-social-media-platform-security](04-social-media-platform-security/README.md) | 15 | Operational |
| [05-on-chain-monitoring](05-on-chain-monitoring/README.md) | 12 | Operational |
| [06-supply-chain-defense](06-supply-chain-defense/README.md) | 10 | Operational |
| [07-ai-agent-security](07-ai-agent-security/README.md) | 12 | Operational |
| [08-governance-compliance-sovereignty](08-governance-compliance-sovereignty/README.md) | 13 | Operational |
| [09-consumer-fraud-defense](09-consumer-fraud-defense/README.md) | 10 | Operational |
| Total | 112 | 105 operational + 7 cross-domain |
<!-- inventory:end -->

The domain files own control definitions. The registry owns threat IDs and candidate control references. Counts, this domain summary, and the [registry table](taxonomy/registry-table.md) are generated and checked by the repository validator. A listed mitigation is not proof it prevented an incident.

## Scoring and evidence

[CTRS is suspended](taxonomy/ctrs-scoring.md) because the baseline contains incompatible component ranges, formulas, and published values. Original scores, component rows, trend claims, attribution probabilities, and case leads remain in [historical data](taxonomy/legacy/README.md) and Git history. No replacement scores or rankings are adopted.

Registry severity is inherited qualitative metadata, separate from a CTRS tier. All registry evidence remains `pending_primary_review`. A November 2026 integrity review is not a November 2026 threat-evidence cutoff. The curated case library is not a complete incident corpus, control-effectiveness study, or calibrated attribution model.

Seven [scoped research notes](research/README.md) now connect control lessons to a [13-report historical case library](intelligence/README.md), covering all 12 categories. These source-checked drafts are not complete empirical studies. Use the [operating guide](OPERATING-GUIDE.md), [playbook routes](playbooks/README.md), and [practical tools](tools/README.md).

## Companion frameworks and governance

[AI SAFE²](https://github.com/CyberStrategyInstitute/ai-safe2-framework) addresses agent governance. [Cognitive Sovereignty](https://github.com/CyberStrategyInstitute/cognitive-sovereignty) addresses human decision autonomy and manipulation. The [alignment document](FRAMEWORK-ALIGNMENT.md) describes intended responsibilities and required mapping evidence. It does not certify current companion IDs, versions, control counts, or implementation behavior.

CSI favors self-custody and privacy. Policy alignment does not establish jurisdiction-specific rights or remove legal obligations. Use a dated primary-source register and qualified review for legal decisions. See [governance controls](08-governance-compliance-sovereignty/README.md).

## Repository contents

- `00-*/` through `09-*/`: control specifications.
- `taxonomy/`: active registry, generated table, suspended scoring, architecture, bridge assessment, and historical data.
- `metadata/`: separate registry and event contracts, migration guidance, and synthetic examples.
- `playbooks/` and `OODA-PLAYBOOK.md`: scenario-specific response.
- `research/`, `reviews/`, and `intelligence/`: research status, integrity findings, evidence records, and event contribution format.
- `tools/`: hardening and assessment checklists, generation and validation scripts.
- `tests/`: rejection and consistency tests for the data and documentation contracts.
- `assets/`: published v2.0 header, SVG responsibility map, and historical artwork.

## Validate and contribute

```sh
python -m pip install -r requirements-validation.txt
python tools/validate_repository.py
python -m unittest discover -s tests -v
```

After intentional definition changes, run `python tools/generate_reference.py`, inspect the diff, and rerun validation. [CI](.github/workflows/taxonomy-lint.yml) checks every push and pull request. Validation proves contract and consistency checks pass; it does not validate historical incident claims or deployed security controls.

The prior MCP-server, handbook, card-deck, campaign, and brief dates were plans. Delivery is not established by this repository. Contribute through the [issue templates](.github/ISSUE_TEMPLATE/) and [contribution guide](CONTRIBUTING.md).

## Star History

<a href="https://www.star-history.com/?repos=cyberstrategyinstitute%2Fcrypto-shield&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=cyberstrategyinstitute/crypto-shield&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=cyberstrategyinstitute/crypto-shield&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=cyberstrategyinstitute/crypto-shield&type=date&legend=top-left" />
 </picture>
</a>

## Licensing and citation

The existing [LICENSE](LICENSE) governs: code under MIT; framework methodology, taxonomy content, and documentation under CC BY-SA 4.0. This update does not relicense existing material. Cite a specific commit when referring to the published framework specification.

Managed by Cyber Strategy Institute.
