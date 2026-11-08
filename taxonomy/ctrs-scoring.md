# Crypto Threat Risk Score (CTRS): suspended

<!-- navigation:start -->
[Home](../README.md) | [All pages](../REPOSITORY-MAP.md) | [Domains](../README.md#domains-and-control-counts) | [v2.0 changes](../FRAMEWORK-UPDATE.md) | [Machine-readable index](../metadata/repository-index.json) | [Automation guide](../AUTOMATION.md)
<!-- navigation:end -->

CTRS v1.1 is historical, unvalidated data. Do not issue new scores, rank threats with it, or convert its values to another scale. Qualitative severity in the registry is a separate inherited assessment, not a calculated CTRS tier.

The baseline used incompatible instructions: 0-4 components with both a x5 explanation and a x20 formula, while the README used 0-5 components and a 0-100 scale. Historical rows also contain arithmetic and tier mismatches. No replacement model has been adopted.

## Historical records

- [Original registry snapshot](legacy/registry-v1.1.json): all original fields, including scores and uncalibrated attribution probabilities.
- [Original scoring rows](legacy/scoring-v1.1.json): all 44 component rows, scores, and tiers as published.
- [Original methodology at the reviewed commit](https://github.com/CyberStrategyInstitute/crypto-shield/blob/051a317fb72db38f11d8928fddd5c506d24d468a/taxonomy/ctrs-scoring.md).

The current registry exposes `legacy_ctrs_score` solely for migration. It preserves the original registry's 0-20 values without endorsing them. Historical 0-100 examples remain in Git history, outside the active event contract.

## Requirements for a replacement

1. Define a version, target population, assessment scenario, component ranges, weights, scaling, precision, rounding, and exhaustive tier boundaries.
2. Record source dates, input evidence, assessor, uncertainty, and control assumptions for each assessment. Distinguish scenario severity, likelihood, observed loss, and residual exposure.
3. Test zero, maximum, boundary, fractional, missing, and invalid inputs. Publish reproducible calculations and migration rules.
4. Measure inter-rater agreement and sensitivity. Seek cases where high-ranked controls were present and harm still occurred.
5. Obtain maintainer review before publishing a new model. Preserve legacy values rather than silently recalculating them.

Use scenario-specific exposure and control gaps for prioritization during suspension. Physical danger and active theft require response regardless of a numerical rating.
