# CSI-CASE-002: Coinbase support-data theft and extortion disclosure

<!-- navigation:start -->
[Home](../../README.md) | [All pages](../../REPOSITORY-MAP.md) | [Domains](../../README.md#domains-and-control-counts) | [v2.0 changes](../../FRAMEWORK-UPDATE.md) | [Machine-readable index](../../metadata/repository-index.json) | [Automation guide](../../AUTOMATION.md)
<!-- navigation:end -->

## Report header

Author: Codex-assisted repository research. Status: source-checked draft; independent review pending. Classification: open source. Source publication: 2025-05-15. Source reviewed: 2026-11-07. Historical scope: this cited disclosure only. Category: Insider. Case type: incident. Mapping: supported_scope. No vendor endorsement or undisclosed paid relationship is asserted.

## Findings

Coinbase reported bribed support agents copying customer information for impersonation attacks. It said the disclosed access did not expose private keys or enable direct movement of customer funds.

Source class: vendor_incident_account. This is the affected company's account, not independent forensics. The ransom demand, reward, remediation costs, and customer losses must not be combined as direct theft.

## Event record

[CSI-CASE-002 JSON](../events/coinbase-support.json) conforms to the event contract. Its timestamp represents source publication at midnight UTC for indexing, not the incident time. Unknown amounts and involvement remain null.

## Supporting evidence

- [Coinbase](https://www.coinbase.com/blog/protecting-our-customers-standing-up-to-extortionists)

The original publisher material was examined. This is not independent replication of its investigation. No private telemetry, complete court record, transaction trace, or malware execution was obtained. Contradictory or later evidence requires a dated amendment, not silent replacement.

## Financial effects

No comparable direct-loss total is adopted in the event. Amounts described in the source may concern gross funds, combined offenses, ransom, liabilities, seizure, or compensation. These must not be summed or substituted.

## Control review and follow-up

Analyst inference: Access to customer identity data can enable downstream fraud without possession of signing keys.

Candidate controls: GCS-04, GCS-05, SMS-06, CDG-06. The source does not provide an implementation inventory sufficient to prove these controls would have prevented the event. Record protections already present and test their bypasses before claiming effectiveness.

Retrospective response route: [selected playbook](../../playbooks/consumer-fraud.md). This is how a responder should classify a comparable situation today, not a claim that historical responders followed it. Start with safety, then establish exposure, select authorized containment, verify the result, and preserve/report evidence.

Review owner: maintainer or designated incident analyst, unassigned. Before closure, obtain underlying technical or judicial artifacts, resolve mapping uncertainty, check later corrections, and document contrary evidence. Use the [case coverage register](../README.md) and [exercise pack](../../tools/tabletop-exercises.md).
