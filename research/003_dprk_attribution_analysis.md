# Research Note 003: Actor attribution and privileged access are separate questions

<!-- navigation:start -->
[Home](../README.md) | [All pages](../REPOSITORY-MAP.md) | [Domains](../README.md#domains-and-control-counts) | [v2.0 changes](../FRAMEWORK-UPDATE.md) | [Machine-readable index](../metadata/repository-index.json) | [Automation guide](../AUTOMATION.md)
<!-- navigation:end -->

Status: scoped primary-source synthesis, source-checked draft; independent review pending. Review date: 2026-11-07. Scope: the linked teaching cases and control-design implications. This replaces the prior placeholder or unvalidated conclusion without declaring the broader research project complete.

## Finding

An actor assessment does not establish the exact compromised authority, the intent of an employee, or the control that would have prevented harm.

## Method and evidence

Cases were selected for explanatory value, source accessibility, and category coverage, not population representativeness or loss ranking. The reports link original publisher material and record its dates and limitations. Source review is not independent technical replication.

- [Bybit major theft: official attribution and response boundary](../intelligence/reports/bybit-official.md)
- [Atomic Wallet unauthorized transfers: unresolved mechanism](../intelligence/reports/atomic-wallet.md)
- [TraderTraitor trojanized-application advisory](../intelligence/reports/tradertraitor-malware.md)

## Analysis

Maintain separate fields for actor, access path, financial authority, observed effect, control weakness, and confidence basis. The inspected advisories supply official assessments and different levels of technical detail. Do not backfill a specific wallet mechanism from an actor label or from another campaign.

## Control consequences

CDG-06 owns provenance. WKS-11/12 own authority inventory and invalidation. EDD controls apply to evidenced endpoint paths. Neither insider-first nor state-actor-first reasoning is required; compare hypotheses with the same standard.

## Worked application

Use the wallet exercise. Leave the cause unknown while identifying exposed authority and safe containment. A report with unknown mechanism can still support useful response without a fabricated attribution probability.

Use the [tabletop pack](../tools/tabletop-exercises.md), [playbook guide](../playbooks/README.md), and [operating guide](../OPERATING-GUIDE.md). Case facts belong in reports; reusable classes belong in taxonomy; operational decisions belong in incident logs.

## Counterexamples and remaining work

Obtain original payloads, logs, transactions, device evidence, and official technical appendices. Reconcile source-date differences and assess whether later disclosures narrow the mechanism. Do not treat shared laundering routes as unique attribution proof.

No CTRS rating, calibrated attribution probability, population statistic, or prevention percentage is established. The [original note](https://github.com/CyberStrategyInstitute/crypto-shield/blob/051a317fb72db38f11d8928fddd5c506d24d468a/research/003_dprk_attribution_analysis.md) remains in Git history; its unsupported claims are not adopted here.
