# CSI-CASE-003: Twitter administrative-access social engineering

## Report header

Author: Codex-assisted repository research. Status: source-checked draft; independent review pending. Classification: open source. Source publication: 2023-06-23. Source reviewed: 2026-11-07. Historical scope: this cited disclosure only. Category: Social Engineering. Case type: incident. Mapping: supported_scope. No vendor endorsement or undisclosed paid relationship is asserted.

## Findings

DOJ described social engineering that obtained Twitter administrative-tool access and transferred control of accounts during July 2020. The sentencing announcement also covers separate SIM-swap offenses.

Source class: official_judicial_summary. The separate offenses are not one loss event. This summary does not establish that hardware authentication alone could have blocked internal administrative abuse.

## Event record

[CSI-CASE-003 JSON](../events/twitter-account-takeover.json) conforms to the event contract. Its timestamp represents source publication at midnight UTC for indexing, not the incident time. Unknown amounts and involvement remain null.

## Supporting evidence

- [US Department of Justice](https://www.justice.gov/usao-ndca/pr/uk-citizen-sentenced-five-years-cybercrime-offenses)

The original publisher material was examined. This is not independent replication of its investigation. No private telemetry, complete court record, transaction trace, or malware execution was obtained. Contradictory or later evidence requires a dated amendment, not silent replacement.

## Financial effects

No comparable direct-loss total is adopted in the event. Amounts described in the source may concern gross funds, combined offenses, ransom, liabilities, seizure, or compensation. These must not be summed or substituted.

## Control review and follow-up

Analyst inference: A familiar or verified account is not independent confirmation when the platform administration path is compromised.

Candidate controls: SMS-01, SMS-03, SMS-08, SMS-06. The source does not provide an implementation inventory sufficient to prove these controls would have prevented the event. Record protections already present and test their bypasses before claiming effectiveness.

Retrospective response route: [selected playbook](../../playbooks/account-takeover.md). This is how a responder should classify a comparable situation today, not a claim that historical responders followed it. Start with safety, then establish exposure, select authorized containment, verify the result, and preserve/report evidence.

Review owner: maintainer or designated incident analyst, unassigned. Before closure, obtain underlying technical or judicial artifacts, resolve mapping uncertainty, check later corrections, and document contrary evidence. Use the [case coverage register](../README.md) and [exercise pack](../../tools/tabletop-exercises.md).
