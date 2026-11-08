# CSI-CASE-007: Ledger Connect Kit malicious-package distribution

<!-- navigation:start -->
[Home](../../README.md) | [All pages](../../REPOSITORY-MAP.md) | [Domains](../../README.md#domains-and-control-counts) | [v2.0 changes](../../FRAMEWORK-UPDATE.md) | [Machine-readable index](../../metadata/repository-index.json) | [Automation guide](../../AUTOMATION.md)
<!-- navigation:end -->

## Report header

Author: Codex-assisted repository research. Status: source-checked draft; independent review pending. Classification: open source. Source publication: 2023-12-20. Source reviewed: 2026-11-07. Historical scope: this cited disclosure only. Category: Supply Chain. Case type: incident. Mapping: supported_scope. No vendor endorsement or undisclosed paid relationship is asserted.

## Findings

Ledger reports that a phished former employee's npm session enabled malicious Connect Kit releases, which DApps loaded dynamically. It identifies incomplete revocation of external package access during offboarding.

Source class: vendor_incident_account. The operator report was read, but packages, transactions, and the reported freeze were not independently replayed. This account concerns a software distribution path, not proof of hardware key extraction.

## Event record

[CSI-CASE-007 JSON](../events/ledger-connect-kit.json) conforms to the event contract. Its timestamp represents source publication at midnight UTC for indexing, not the incident time. Unknown amounts and involvement remain null.

## Supporting evidence

- [Ledger](https://www.ledger.com/blog/security-incident-report)

The original publisher material was examined. This is not independent replication of its investigation. No private telemetry, complete court record, transaction trace, or malware execution was obtained. Contradictory or later evidence requires a dated amendment, not silent replacement.

## Financial effects

No comparable direct-loss total is adopted in the event. Amounts described in the source may concern gross funds, combined offenses, ransom, liabilities, seizure, or compensation. These must not be summed or substituted.

## Control review and follow-up

Analyst inference: Review runtime-loaded dependencies and external publishing access, not only the source repository and lockfile.

Candidate controls: SCD-02, SCD-03, SCD-07, SCD-09, WKS-12. The source does not provide an implementation inventory sufficient to prove these controls would have prevented the event. Record protections already present and test their bypasses before claiming effectiveness.

Retrospective response route: [selected playbook](../../playbooks/endpoint-supply-chain.md). This is how a responder should classify a comparable situation today, not a claim that historical responders followed it. Start with safety, then establish exposure, select authorized containment, verify the result, and preserve/report evidence.

Review owner: maintainer or designated incident analyst, unassigned. Before closure, obtain underlying technical or judicial artifacts, resolve mapping uncertainty, check later corrections, and document contrary evidence. Use the [case coverage register](../README.md) and [exercise pack](../../tools/tabletop-exercises.md).
