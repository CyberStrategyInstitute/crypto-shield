# Data contracts and migration

Schema version 2.0.0 deliberately breaks ambiguous v1.1 field semantics.

| v1.1 | v2.0 | Meaning |
|---|---|---|
| Implicit event contract | Required `schema_version: "2.0"` | Consumers explicitly identify the incompatible event format |
| Registry `ctrs_score` | `legacy_ctrs_score` | Historical 0-20 value, unvalidated |
| Registry `deterministic_defense` | `candidate_controls` | Proposed mitigations, not proven prevention |
| Registry attribution probabilities and trend statistics | Historical snapshot only | No calibrated probabilities or verified trend dataset established |
| Event `ctrs_score` | Removed | Numerical scoring suspended |
| Event `deterministic_defense` | `candidate_controls` | Requires incident-specific mechanism and limitations |
| Event forced attribution booleans | Nullable `insider_vector` and `ai_assisted` | Null means unknown, not false |
| Event confidence | `attribution_status` plus evidence | Unknown, reported, or assessed; no invented probability |

The [registry schema](registry-schema.json) validates the taxonomy envelope. The [event schema](threat-event-schema.json) validates one event, not an envelope or registry. Event examples are synthetic and do not represent actual victims or losses. One event is stored per JSON file under `intelligence/events/` when contributed. A curated historical teaching set is supplied; it is not a complete incident corpus.

Validate with `python tools/validate_repository.py`. Unknown fields fail validation so old consumers must migrate explicitly. Format checks are enabled. Event threat IDs, categories, and control references are also checked against current definitions. New threat definitions use `legacy_ctrs_score: null`; they must not invent historical or replacement scores. Existing legacy values remain unchanged.

Source strings inherited in the registry are discovery leads with `pending_primary_review` status. They do not certify the source, incident, attribution, loss, or control efficacy. The unchanged [historical registry](../taxonomy/legacy/registry-v1.1.json) retains every old field for audit and migration.

The framework release proposal is 2.0.0; registry and event contract versions are 2.0. The separate control-inventory and evidence schemas retain their initial contracts. See [added and updated framework controls](../FRAMEWORK-UPDATE.md).


Case events carry `timestamp_basis: "publication_date"` and `source_review_date`. Midnight UTC is an indexing convention, not an asserted occurrence time. The case register distinguishes incidents, campaigns, adjacent examples, and policy actions, records provisional mappings, and links reports, events, controls, sources, and playbooks. `primary_reviewed` means original publisher material was examined; it does not certify the underlying claim.
