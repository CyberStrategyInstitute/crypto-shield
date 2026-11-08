# CSI-CASE-001: Violent home invasions targeting cryptocurrency

## Report header

Author: Codex-assisted repository research. Status: source-checked draft; independent review pending. Classification: open source. Source publication: 2024-09-13. Source reviewed: 2026-11-07. Historical scope: this cited disclosure only. Category: Physical. Case type: campaign. Mapping: supported_scope. No vendor endorsement or undisclosed paid relationship is asserted.

## Findings

DOJ reported sentences in a scheme combining SIM swapping and violent home invasions to steal cryptocurrency. Its account describes victims being assaulted and restrained.

Source class: official_judicial_summary. The press release summarizes court proceedings; underlying trial evidence was not reconstructed. No claim that a decoy or timelock would have ensured safety is supported.

## Event record

[CSI-CASE-001 JSON](../events/physical-home-invasions.json) conforms to the event contract. Its timestamp represents source publication at midnight UTC for indexing, not the incident time. Unknown amounts and involvement remain null.

## Supporting evidence

- [US Department of Justice](https://www.justice.gov/archives/opa/pr/twelve-defendants-sentenced-violent-home-invasion-robberies-steal-cryptocurrency)

The original publisher material was examined. This is not independent replication of its investigation. No private telemetry, complete court record, transaction trace, or malware execution was obtained. Contradictory or later evidence requires a dated amendment, not silent replacement.

## Financial effects

No comparable direct-loss total is adopted in the event. Amounts described in the source may concern gross funds, combined offenses, ransom, liabilities, seizure, or compensation. These must not be summed or substituted.

## Control review and follow-up

Analyst inference: Digital account protection and physical safety require coordinated planning. Coercion guidance must allow the safest available response.

Candidate controls: OPS-05, OPS-06, OPS-10, SMS-02. The source does not provide an implementation inventory sufficient to prove these controls would have prevented the event. Record protections already present and test their bypasses before claiming effectiveness.

Retrospective response route: [selected playbook](../../playbooks/physical-coercion.md). This is how a responder should classify a comparable situation today, not a claim that historical responders followed it. Start with safety, then establish exposure, select authorized containment, verify the result, and preserve/report evidence.

Review owner: maintainer or designated incident analyst, unassigned. Before closure, obtain underlying technical or judicial artifacts, resolve mapping uncertainty, check later corrections, and document contrary evidence. Use the [case coverage register](../README.md) and [exercise pack](../../tools/tabletop-exercises.md).
