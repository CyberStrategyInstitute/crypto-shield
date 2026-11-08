# Intelligence report template

<!-- navigation:start -->
[Home](../README.md) | [All pages](../REPOSITORY-MAP.md) | [Domains](../README.md#domains-and-control-counts) | [v2.0 changes](../FRAMEWORK-UPDATE.md) | [Machine-readable index](../metadata/repository-index.json) | [Automation guide](../AUTOMATION.md)
<!-- navigation:end -->

Report ID, author, review status, coverage period, actual source-review dates, and conflicts:

## Findings

State observed facts, official or vendor claims, and analyst inference separately. Record competing explanations and disconfirming evidence. Unknown actor, insider involvement, or AI involvement must remain unknown. No calibrated false-flag probabilities or universal prevention claims are supported.

## Event record

Use one record per JSON file under `intelligence/events/`, validated against [the event schema](../metadata/threat-event-schema.json). This example is synthetic:

```json
{
  "schema_version": "2.0",
  "id": "SYNTHETIC-REPORT-001",
  "timestamp": "2026-11-07T00:00:00Z",
  "threat_id": "CS-WAL-04",
  "category": "Wallet",
  "severity": "HIGH",
  "ooda_phase": "orient",
  "evidence_status": "synthetic",
  "attribution_status": "unknown",
  "attribution": null,
  "insider_vector": null,
  "ai_assisted": null,
  "financial_loss_usd": null,
  "references": [],
  "candidate_controls": ["WKS-07"],
  "control_analysis": "Proposed mitigation only; record mechanism, assumptions, bypasses, and controls already present."
}
```

## Supporting evidence

Primary artifacts and URLs, publisher, event and publication dates, actual review date, population, method, uncertainty, and contrary evidence. Reported or primary-reviewed events require source references. Synthetic examples are not incident evidence.

## Financial effects

Record direct loss, affected assets, frozen assets, seized assets, returns, reimbursement, and estimated future exposure separately, each with currency, source, date, and uncertainty. Avoid combining complaint totals with on-chain incident totals without overlap analysis.

## Control review and follow-up

Controls present; candidate mitigation; enforcement boundary; authority-specific response; bypass tests; residual harm; accountable owner; evidence needed before closure. A model shutdown does not necessarily revoke on-chain authority.
