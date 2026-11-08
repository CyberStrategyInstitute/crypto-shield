# Historical assessments

<!-- navigation:start -->
[Home](../../README.md) | [All pages](../../REPOSITORY-MAP.md) | [Domains](../../README.md#domains-and-control-counts) | [v2.0 changes](../../FRAMEWORK-UPDATE.md) | [Machine-readable index](../../metadata/repository-index.json) | [Automation guide](../../AUTOMATION.md)
<!-- navigation:end -->

`registry-v1.1.json` preserves the complete registry at `051a317fb72db38f11d8928fddd5c506d24d468a`, including its incorrect declared total of 42, original scores, trend assertions, attribution probabilities, and source leads. It is historical data and intentionally does not conform to the active registry schema.

`scoring-v1.1.json` preserves the 44 scoring-table rows at that commit. Strings retain the published component, score, and tier representations. No arithmetic correction is applied to these records.

Use [the suspended-scoring policy](../ctrs-scoring.md). No legacy value is a current calibrated rating, verified attribution, legal conclusion, efficacy result, or incident statistic. The validator checks snapshot identity against the recorded baseline hashes and ensures active legacy scores still match the original registry.
