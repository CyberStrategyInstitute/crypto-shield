# Operational tools

<!-- navigation:start -->
[Home](../README.md) | [All pages](../REPOSITORY-MAP.md) | [Domains](../README.md#domains-and-control-counts) | [v2.0 changes](../FRAMEWORK-UPDATE.md) | [Machine-readable index](../metadata/repository-index.json) | [Automation guide](../AUTOMATION.md)
<!-- navigation:end -->

| Task | Tool | Output |
|---|---|---|
| Plan improvements | [30-day sprint](30-day-hardening-sprint.md) | Assigned implementation work |
| Assess controls | [Self-assessment](sovereignty-self-assessment.md) | Evidence/status for all 112 controls |
| Inventory financial authority | [Authority template](templates/authority-inventory.json) | Principals, scopes, limits, invalidation and evidence |
| Manage an incident | [Incident log](templates/incident-log.json) | Decisions, authority, verification and handoff |
| Specify combined exposure | [Budget template](templates/exposure-budget.json) | Valuation, reservations, limits, outages and tests |
| Review a case | [Source checklist](source-review-checklist.md) | Source and claim-quality decision |
| Rehearse response | [Tabletop pack](tabletop-exercises.md) | Completed exercise records, not live test results |
| Find linked cases | `python tools/case_lookup.py --category Wallet` | Matching reports, events, controls and playbook paths |
| Regenerate references | `python tools/generate_reference.py` | Current tables, domain headers, page map, discovery JSON, and assessment references |
| Check the repository | `python tools/validate_repository.py` | Contract, link, reference and coverage errors |

Templates contain no secrets and do not send transactions or contact services. Copy and fill them locally. The [synthetic sample](samples/authority-inventory.synthetic.json) demonstrates the intended detail without pretending a test passed. Read the [operating guide](../OPERATING-GUIDE.md) before treating a checked box as verified protection.

## Repository discovery

Use the [complete page map](../REPOSITORY-MAP.md) for browsing and the [automation guide](../AUTOMATION.md) for structured access. The [repository index](../metadata/repository-index.json) lists all Markdown pages, domain routes, control IDs, priorities, and v2.0 change labels. The existing validator rejects stale generated navigation as well as stale reference tables.
