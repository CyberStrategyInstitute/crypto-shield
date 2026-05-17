---
name: New Threat Entry
about: Submit a new threat for inclusion in the CryptoSHIELD taxonomy
title: "[THREAT] CS-XXX-00: Threat Name"
labels: new-threat, taxonomy
assignees: ''

---

## Threat Proposal

**Proposed Threat ID:** (follow existing convention: CS-[CATEGORY]-[NUMBER])
**Category:** (PHY / INS / SOC / MAL / WAL / DFI / SC / AI / MKT / SOV / FRD / EXT)
**Threat Name:**

## Threat Description

Describe the attack in concrete terms. What does the attacker do? What is the victim's experience?

## Attack Vector

How is this attack delivered to the victim?

## OODA Phase

Which OODA phase does this attack primarily operate in?
- [ ] Observe
- [ ] Orient
- [ ] Decide
- [ ] Act

## Evidence

**Documented Cases (minimum 2 required):**
1. [Case 1: date, platform/target, loss amount, source link]
2. [Case 2: date, platform/target, loss amount, source link]

**Financial Scale:**
Estimated annual losses or incident volume:

## CTRS Scoring Proposal

Rate each component (0-4):
- Likelihood (L): ___ | Rationale:
- Impact on Sovereignty (I): ___ | Rationale:
- Reach/Scale (R): ___ | Rationale:
- Detection Difficulty (D): ___ | Rationale:
- Recovery Difficulty (RecD): ___ | Rationale:

**Proposed CTRS:** (use formula from taxonomy/ctrs-scoring.md)

## Proposed Controls

What 1-3 controls would mitigate this threat? Refer to existing controls where possible.

1.
2.
3.

## Adversarial Reproduction Test

An independent analyst using the same sources and methodology should arrive at the same threat classification and CTRS score. Provide sufficient documentation for this test to pass.

## Metadata Tags

- `false_flag_prob`: (float 0.0-1.0)
- `insider_vector`: (true/false)
- `ai_assisted`: (true/false)
- `sovereignty_impact`: (LOW/MEDIUM/HIGH/CRITICAL)

---
*CSI CryptoSHIELD Framework | Contributor: @yourhandle*
