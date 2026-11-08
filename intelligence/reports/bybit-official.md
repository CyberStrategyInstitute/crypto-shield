# CSI-CASE-013: Bybit major theft: official attribution and response boundary

<!-- navigation:start -->
[Home](../../README.md) | [All pages](../../REPOSITORY-MAP.md) | [Domains](../../README.md#domains-and-control-counts) | [v2.0 changes](../../FRAMEWORK-UPDATE.md) | [Machine-readable index](../../metadata/repository-index.json) | [Automation guide](../../AUTOMATION.md)
<!-- navigation:end -->

## Report header

Author: Codex-assisted repository research. Status: source-checked draft; independent review pending. Classification: open source. Source publication: 2025-02-26. Source reviewed: 2026-11-07. Historical scope: this cited disclosure only. Category: Wallet. Case type: incident. Mapping: provisional. No vendor endorsement or undisclosed paid relationship is asserted.

## Findings

The FBI attributed approximately $1.5 billion in virtual-asset theft from Bybit around February 21, 2025 to North Korean TraderTraitor activity and published associated addresses.

Source class: official_attribution. The advisory does not reconstruct the signing mechanism. CS-WAL-04 is provisional; this report does not infer a malicious approval, compromised hardware, or insider malice from attribution alone.

## Event record

[CSI-CASE-013 JSON](../events/bybit-official.json) conforms to the event contract. Its timestamp represents source publication at midnight UTC for indexing, not the incident time. Unknown amounts and involvement remain null.

## Supporting evidence

- [Federal Bureau of Investigation](https://www.ic3.gov/PSA/2025/PSA250226)

The original publisher material was examined. This is not independent replication of its investigation. No private telemetry, complete court record, transaction trace, or malware execution was obtained. Contradictory or later evidence requires a dated amendment, not silent replacement.

## Financial effects

The FBI reports an approximate $1.5 billion theft; the event labels it estimated. No frozen, seized, returned, or reimbursed amount is adopted.

## Control review and follow-up

Analyst inference: Treat the advisory as an attribution/reporting source while separately obtaining payload, authority, device, and custody evidence.

Candidate controls: WKS-05, WKS-11, WKS-12, OCM-11, CDG-06. The source does not provide an implementation inventory sufficient to prove these controls would have prevented the event. Record protections already present and test their bypasses before claiming effectiveness.

Retrospective response route: [selected playbook](../../playbooks/wallet-compromise.md). This is how a responder should classify a comparable situation today, not a claim that historical responders followed it. Start with safety, then establish exposure, select authorized containment, verify the result, and preserve/report evidence.

Review owner: maintainer or designated incident analyst, unassigned. Before closure, obtain underlying technical or judicial artifacts, resolve mapping uncertainty, check later corrections, and document contrary evidence. Use the [case coverage register](../README.md) and [exercise pack](../../tools/tabletop-exercises.md).
