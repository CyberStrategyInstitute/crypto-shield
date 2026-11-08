# CSI-CASE-011: Tornado Cash delisting: policy-dependency example

## Report header

Author: Codex-assisted repository research. Status: source-checked draft; independent review pending. Classification: open source. Source publication: 2025-03-21. Source reviewed: 2026-11-07. Historical scope: this cited disclosure only. Category: Sovereignty. Case type: policy. Mapping: supported_scope. No vendor endorsement or undisclosed paid relationship is asserted.

## Findings

Treasury announced removal of economic sanctions against Tornado Cash after reviewing legal and policy issues. It retained warnings about illicit-finance risks.

Source class: official_policy_action. This is a dated policy action, not a theft or a finding that every related activity is lawful. Current sanctions, criminal cases, transaction facts, and jurisdiction need separate review.

## Event record

[CSI-CASE-011 JSON](../events/tornado-policy.json) conforms to the event contract. Its timestamp represents source publication at midnight UTC for indexing, not the incident time. Unknown amounts and involvement remain null.

## Supporting evidence

- [US Department of the Treasury](https://home.treasury.gov/news/press-releases/sb0057)

The original publisher material was examined. This is not independent replication of its investigation. No private telemetry, complete court record, transaction trace, or malware execution was obtained. Contradictory or later evidence requires a dated amendment, not silent replacement.

## Financial effects

No comparable direct-loss total is adopted in the event. Amounts described in the source may concern gross funds, combined offenses, ransom, liabilities, seizure, or compensation. These must not be summed or substituted.

## Control review and follow-up

Analyst inference: Operational access may depend on legal and third-party decisions even when key custody remains unchanged.

Candidate controls: GCS-03, GCS-09, GCS-13, CDG-04. The source does not provide an implementation inventory sufficient to prove these controls would have prevented the event. Record protections already present and test their bypasses before claiming effectiveness.

Retrospective response route: [selected playbook](../../playbooks/policy-custody-event.md). This is how a responder should classify a comparable situation today, not a claim that historical responders followed it. Start with safety, then establish exposure, select authorized containment, verify the result, and preserve/report evidence.

Review owner: maintainer or designated incident analyst, unassigned. Before closure, obtain underlying technical or judicial artifacts, resolve mapping uncertainty, check later corrections, and document contrary evidence. Use the [case coverage register](../README.md) and [exercise pack](../../tools/tabletop-exercises.md).
