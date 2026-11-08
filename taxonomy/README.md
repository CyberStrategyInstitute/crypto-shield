# Taxonomy and case mapping

<!-- navigation:start -->
[Home](../README.md) | [All pages](../REPOSITORY-MAP.md) | [Domains](../README.md#domains-and-control-counts) | [v2.0 changes](../FRAMEWORK-UPDATE.md) | [Machine-readable index](../metadata/repository-index.json) | [Automation guide](../AUTOMATION.md)
<!-- navigation:end -->

The registry defines threat classes; it is not an incident database. Event records belong in `intelligence/events/`, with human reports under `intelligence/reports/`. Mapping a case to a class does not validate every assertion inherited by that class.

| File | Role |
|---|---|
| [registry.json](registry.json) | Canonical 46 classes across 12 categories, descriptions and candidate controls |
| [registry-table.md](registry-table.md) | Generated human-readable class view |
| [threat-architecture.md](threat-architecture.md) | Conceptual causal layers; not a proved causal model |
| [bridge-risk-appendix.md](bridge-risk-appendix.md) | Bridge validity, backing, liability and exposure questions |
| [ctrs-scoring.md](ctrs-scoring.md) | Scoring suspension and replacement-model requirements |
| [legacy](legacy/README.md) | Unchanged historical 44-row registry and scoring data |

The case library identified two class gaps: CS-MKT-04 covers price/collateral manipulation; CS-SOV-03 covers policy/provider access restrictions without presuming unlawful conduct. Both remain unscored. An official policy action is not classified as a theft or proof of overreach.

Use `python tools/case_lookup.py --threat CS-MKT-04` or the [case coverage index](../intelligence/README.md). Provisional wallet mappings remain explicitly provisional when source evidence does not establish the mechanism. Do not force an unknown incident into a confirmed seed-extraction or approval narrative.
