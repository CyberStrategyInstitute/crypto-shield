# CSI-CASE-009: Mango Markets price and collateral manipulation allegations

## Report header

Author: Codex-assisted repository research. Status: source-checked draft; independent review pending. Classification: open source. Source publication: 2023-01-20. Source reviewed: 2026-11-07. Historical scope: this cited disclosure only. Category: Market Manipulation. Case type: incident. Mapping: supported_scope. No vendor endorsement or undisclosed paid relationship is asserted.

## Findings

The SEC alleged that coordinated positions and purchases raised MNGO prices and collateral values, enabling borrowing and withdrawal from Mango Markets.

Source class: official_allegation. This is a historical allegation summary. It does not state the current litigation outcome or adopt the SEC's asset-classification position as universal law. The full complaint and transactions were not reconstructed.

## Event record

[CSI-CASE-009 JSON](../events/mango-market.json) conforms to the event contract. Its timestamp represents source publication at midnight UTC for indexing, not the incident time. Unknown amounts and involvement remain null.

## Supporting evidence

- [US Securities and Exchange Commission](https://www.sec.gov/newsroom/press-releases/2023-13)

The original publisher material was examined. This is not independent replication of its investigation. No private telemetry, complete court record, transaction trace, or malware execution was obtained. Contradictory or later evidence requires a dated amendment, not silent replacement.

## Financial effects

No comparable direct-loss total is adopted in the event. Amounts described in the source may concern gross funds, combined offenses, ransom, liabilities, seizure, or compensation. These must not be summed or substituted.

## Control review and follow-up

Analyst inference: Collateral liquidity, valuation, concentration, and withdrawal budgets need joint stress tests. A profitable trade alone does not prove manipulation.

Candidate controls: AAS-09, OCM-09, OCM-11. The source does not provide an implementation inventory sufficient to prove these controls would have prevented the event. Record protections already present and test their bypasses before claiming effectiveness.

Retrospective response route: [selected playbook](../../playbooks/protocol-exploit.md). This is how a responder should classify a comparable situation today, not a claim that historical responders followed it. Start with safety, then establish exposure, select authorized containment, verify the result, and preserve/report evidence.

Review owner: maintainer or designated incident analyst, unassigned. Before closure, obtain underlying technical or judicial artifacts, resolve mapping uncertainty, check later corrections, and document contrary evidence. Use the [case coverage register](../README.md) and [exercise pack](../../tools/tabletop-exercises.md).
