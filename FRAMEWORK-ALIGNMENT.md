# CryptoSHIELD framework alignment

<!-- navigation:start -->
[Home](README.md) | [All pages](REPOSITORY-MAP.md) | [Domains](README.md#domains-and-control-counts) | [v2.0 changes](FRAMEWORK-UPDATE.md) | [Machine-readable index](metadata/repository-index.json) | [Automation guide](AUTOMATION.md)
<!-- navigation:end -->

This is a proposed allocation of responsibilities, not a verified current control crosswalk or compliance determination. The previous companion and external-standard tables lacked version-pinned source evidence; their specific IDs, counts, and coverage assurances are withdrawn pending verification. The [baseline document](https://github.com/CyberStrategyInstitute/crypto-shield/blob/051a317fb72db38f11d8928fddd5c506d24d468a/FRAMEWORK-ALIGNMENT.md) remains available for comparison.

| Responsibility | Primary specification | Integration evidence required |
|---|---|---|
| Financial authority, custody, budgets, bridges, recovery | CryptoSHIELD WKS, OCM, AAS, GCS | Authority inventory and financial-effect tests |
| Agent identity, tools, memory, delegation, stopping | [AI SAFE²](https://github.com/CyberStrategyInstitute/ai-safe2-framework) | Version-pinned requirements and implementation evidence |
| Human manipulation and decision autonomy | [Cognitive Sovereignty](https://github.com/CyberStrategyInstitute/cognitive-sovereignty) | Current human-facing requirements, scope, and limitations |
| Independent financial approval | CryptoSHIELD semantics; agent-governance implementation | Exact intent binding, independent authentication and recovery, replay and bypass tests |
| Physical coercion | CryptoSHIELD OPS, informed by qualified practice | Life-safety assessment; no mandatory decoy, deception, or refusal |
| Legal and standards obligations | Applicable primary authority | Jurisdiction, entity, activity, edition, effective date, and qualified review |

## Mapping acceptance contract

Each accepted mapping must record source repository or publisher, immutable commit or edition, source section and exact ID, local control, accountable owner, semantic match, gaps, implementation dependency, acceptance tests, and review date. Mark unmatched or inaccessible requirements pending. A title match or a similar paragraph is insufficient.

The supplied analysis identifies AI SAFE² commit `3dd7ecc8bc0f19a0c737f01a91b9bde68d0a20d3` and Cognitive Sovereignty commit `6125cbd252d785efdbc27fc05fe677ff7a8288e1` as research baselines. Their complete current specifications were not reconstructed in this update; no individual companion mapping is certified.

## Integration tests

Verify that the agent cannot approve its own request, change policy, recover the approver account, or replay an approval after a material intent change. Verify that shutdown revokes or constrains persistent authority and pending actions. Test financial effects across bridges, accounts, and concurrent requests. Record one owner for shared requirements and reference its evidence from each framework.

External standards, including NIST, OWASP, and MITRE, require the same version and exact-ID checks before publication as an authoritative crosswalk. A mapping never establishes certification, legal approval, or tested enforcement.
