# CSI-CASE-012: Colonial Pipeline ransom-proceeds seizure

## Report header

Author: Codex-assisted repository research. Status: source-checked draft; independent review pending. Classification: open source. Source publication: 2021-06-07. Source reviewed: 2026-11-07. Historical scope: this cited disclosure only. Category: Extortion. Case type: incident. Mapping: supported_scope. No vendor endorsement or undisclosed paid relationship is asserted.

## Findings

DOJ announced seizure of 63.7 bitcoin from alleged Colonial Pipeline ransom proceeds under a court-authorized warrant. The release describes tracing and access to the destination key.

Source class: official_seizure_account. A seizure is not necessarily completed restitution. It does not reverse the original chain transaction or establish a general recovery success rate.

## Event record

[CSI-CASE-012 JSON](../events/colonial-recovery.json) conforms to the event contract. Its timestamp represents source publication at midnight UTC for indexing, not the incident time. Unknown amounts and involvement remain null.

## Supporting evidence

- [US Department of Justice](https://www.justice.gov/archives/opa/pr/department-justice-seizes-23-million-cryptocurrency-paid-ransomware-extortionists-darkside)

The original publisher material was examined. This is not independent replication of its investigation. No private telemetry, complete court record, transaction trace, or malware execution was obtained. Contradictory or later evidence requires a dated amendment, not silent replacement.

## Financial effects

No comparable direct-loss total is adopted in the event. Amounts described in the source may concern gross funds, combined offenses, ransom, liabilities, seizure, or compensation. These must not be summed or substituted.

## Control review and follow-up

Analyst inference: Prompt reporting and preserved evidence can support lawful seizure. Finality alone does not establish that recovery is impossible.

Candidate controls: GCS-06, EDD-07, CDG-06. The source does not provide an implementation inventory sufficient to prove these controls would have prevented the event. Record protections already present and test their bypasses before claiming effectiveness.

Retrospective response route: [selected playbook](../../playbooks/extortion.md). This is how a responder should classify a comparable situation today, not a claim that historical responders followed it. Start with safety, then establish exposure, select authorized containment, verify the result, and preserve/report evidence.

Review owner: maintainer or designated incident analyst, unassigned. Before closure, obtain underlying technical or judicial artifacts, resolve mapping uncertainty, check later corrections, and document contrary evidence. Use the [case coverage register](../README.md) and [exercise pack](../../tools/tabletop-exercises.md).
