# CSI-CASE-005: Atomic Wallet unauthorized transfers: unresolved mechanism

<!-- navigation:start -->
[Home](../../README.md) | [All pages](../../REPOSITORY-MAP.md) | [Domains](../../README.md#domains-and-control-counts) | [v2.0 changes](../../FRAMEWORK-UPDATE.md) | [Machine-readable index](../../metadata/repository-index.json) | [Automation guide](../../AUTOMATION.md)
<!-- navigation:end -->

## Report header

Author: Codex-assisted repository research. Status: source-checked draft; independent review pending. Classification: open source. Source publication: 2023-08-22. Source reviewed: 2026-11-07. Historical scope: this cited disclosure only. Category: Wallet. Case type: incident. Mapping: provisional. No vendor endorsement or undisclosed paid relationship is asserted.

## Findings

The FBI attributed an Atomic Wallet theft to TraderTraitor-affiliated actors. The wallet provider separately acknowledged user reports of unauthorized transactions and said its investigated root-cause possibilities were unconfirmed.

Source class: official_attribution. The FBI names June 2 while the provider describes June 3 reports. Neither source establishes seed extraction as the cause here. CS-WAL-01 is a provisional triage hypothesis, not a confirmed mechanism.

## Event record

[CSI-CASE-005 JSON](../events/atomic-wallet.json) conforms to the event contract. Its timestamp represents source publication at midnight UTC for indexing, not the incident time. Unknown amounts and involvement remain null.

## Supporting evidence

- [Federal Bureau of Investigation](https://www.fbi.gov/news/press-releases/fbi-identifies-cryptocurrency-funds-stolen-by-dprk)
- [Atomic Wallet provider statement](https://atomicwallet.io/blog/articles/june-3rd-event-statement)

The original publisher material was examined. This is not independent replication of its investigation. No private telemetry, complete court record, transaction trace, or malware execution was obtained. Contradictory or later evidence requires a dated amendment, not silent replacement.

## Financial effects

No comparable direct-loss total is adopted in the event. Amounts described in the source may concern gross funds, combined offenses, ransom, liabilities, seizure, or compensation. These must not be summed or substituted.

## Control review and follow-up

Analyst inference: An unexplained transfer requires authority triage; incident existence and actor attribution do not establish how access occurred.

Candidate controls: WKS-11, WKS-12, EDD-02. The source does not provide an implementation inventory sufficient to prove these controls would have prevented the event. Record protections already present and test their bypasses before claiming effectiveness.

Retrospective response route: [selected playbook](../../playbooks/wallet-compromise.md). This is how a responder should classify a comparable situation today, not a claim that historical responders followed it. Start with safety, then establish exposure, select authorized containment, verify the result, and preserve/report evidence.

Review owner: maintainer or designated incident analyst, unassigned. Before closure, obtain underlying technical or judicial artifacts, resolve mapping uncertainty, check later corrections, and document contrary evidence. Use the [case coverage register](../README.md) and [exercise pack](../../tools/tabletop-exercises.md).
