# Research Note 005: Runtime dependencies, publishing sessions, and offboarding

Status: scoped primary-source synthesis, source-checked draft; independent review pending. Review date: 2026-11-07. Scope: the linked teaching cases and control-design implications. This replaces the prior placeholder or unvalidated conclusion without declaring the broader research project complete.

## Finding

Supply-chain review must reach the code actually loaded and the credentials that can publish it. A clean source repository and committed lockfile can leave external paths unassessed.

## Method and evidence

Cases were selected for explanatory value, source accessibility, and category coverage, not population representativeness or loss ranking. The reports link original publisher material and record its dates and limitations. Source review is not independent technical replication.

- [Ledger Connect Kit malicious-package distribution](../intelligence/reports/ledger-connect-kit.md)
- [TraderTraitor trojanized-application advisory](../intelligence/reports/tradertraitor-malware.md)

## Analysis

Separate installed packages, runtime CDN loading, build modification, signing, publishing, and model loading. The selected affected-party account supports examining external publisher sessions; the campaign advisory supports examining software installation and follow-on authority. Neither establishes a universal default-deny outcome.

## Control consequences

SCD-02/07 govern artifact identity and dependency review; SCD-03 separates credentials and production signing; SCD-09 constrains install scripts. Extend offboarding to external registries, sessions, and tokens, and use WKS-12 for financial authority affected by credential loss.

## Worked application

Use the runtime-CDN exercise. Inventory the dependency actually delivered, publisher access, cache behavior, deployment versions, and how a clean rebuild will be verified. Compare expected versus observed containment before resuming.

Use the [tabletop pack](../tools/tabletop-exercises.md), [playbook guide](../playbooks/README.md), and [operating guide](../OPERATING-GUIDE.md). Case facts belong in reports; reusable classes belong in taxonomy; operational decisions belong in incident logs.

## Counterexamples and remaining work

Inspect malicious artifacts, versioned loader behavior, registry audit logs, build provenance, and deployed hashes. Distinguish software-package malware from model-weight poisoning. Current package versions and live service health require separate checks.

No CTRS rating, calibrated attribution probability, population statistic, or prevention percentage is established. The [original note](https://github.com/CyberStrategyInstitute/crypto-shield/blob/051a317fb72db38f11d8928fddd5c506d24d468a/research/005_supply_chain_vectors.md) remains in Git history; its unsupported claims are not adopted here.
