# CSI-CASE-006: Ronin bridge reopening and backing account

<!-- navigation:start -->
[Home](../../README.md) | [All pages](../../REPOSITORY-MAP.md) | [Domains](../../README.md#domains-and-control-counts) | [v2.0 changes](../../FRAMEWORK-UPDATE.md) | [Machine-readable index](../../metadata/repository-index.json) | [Automation guide](../../AUTOMATION.md)
<!-- navigation:end -->

## Report header

Author: Codex-assisted repository research. Status: source-checked draft; independent review pending. Classification: open source. Source publication: 2022-06-28. Source reviewed: 2026-11-07. Historical scope: this cited disclosure only. Category: DeFi Protocol. Case type: incident. Mapping: supported_scope. No vendor endorsement or undisclosed paid relationship is asserted.

## Findings

Ronin's reopening post describes bridge losses, replacement backing for user balances, and a circuit-breaker design. It separately discusses an undercollateralized DAO treasury amount.

Source class: vendor_incident_account. These are operator statements. User reimbursement, backing, DAO liabilities, and recovered stolen funds are different quantities. The post's March 29 incident wording does not resolve exploit-versus-discovery timing.

## Event record

[CSI-CASE-006 JSON](../events/ronin-bridge.json) conforms to the event contract. Its timestamp represents source publication at midnight UTC for indexing, not the incident time. Unknown amounts and involvement remain null.

## Supporting evidence

- [Ronin Network](https://blog.roninchain.com/p/the-ronin-bridge-is-open-)

The original publisher material was examined. This is not independent replication of its investigation. No private telemetry, complete court record, transaction trace, or malware execution was obtained. Contradictory or later evidence requires a dated amendment, not silent replacement.

## Financial effects

No comparable direct-loss total is adopted in the event. Amounts described in the source may concern gross funds, combined offenses, ransom, liabilities, seizure, or compensation. These must not be summed or substituted.

## Control review and follow-up

Analyst inference: Message security, economic backing, liability scope, and post-incident reimbursement require separate evidence.

Candidate controls: OCM-07, OCM-11, OCM-12, GCS-11. The source does not provide an implementation inventory sufficient to prove these controls would have prevented the event. Record protections already present and test their bypasses before claiming effectiveness.

Retrospective response route: [selected playbook](../../playbooks/protocol-exploit.md). This is how a responder should classify a comparable situation today, not a claim that historical responders followed it. Start with safety, then establish exposure, select authorized containment, verify the result, and preserve/report evidence.

Review owner: maintainer or designated incident analyst, unassigned. Before closure, obtain underlying technical or judicial artifacts, resolve mapping uncertainty, check later corrections, and document contrary evidence. Use the [case coverage register](../README.md) and [exercise pack](../../tools/tabletop-exercises.md).
