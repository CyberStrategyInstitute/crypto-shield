# Contributing to CSI CryptoSHIELD

CryptoSHIELD is a living framework. The threat landscape evolves weekly. Contributions must meet the same adversarial-reproduction standard applied to the initial framework: independent analysts using the same data and methodology must arrive at comparable assessments.

## Contribution Types

### New Threat Entry
Use the issue template: `.github/ISSUE_TEMPLATE/new-threat-entry.md`

Required for all new threat submissions:
- Proposed Threat ID (CS-[CATEGORY]-[##])
- CTRS scoring with component breakdown (L, Ia, R, D, RecD)
- Documented evidence (at minimum: 2 independent sources)
- OODA phase classification
- At least one deterministic defense control reference
- False flag probability with justification

### Control Update
Use the issue template: `.github/ISSUE_TEMPLATE/control-update.md`

For modifications to existing controls:
- Specify control ID and current text
- Evidence that current control is insufficient or incorrect
- Proposed revision with implementation guidance

### Research Submission
- Add peer-testable evidence to `/research/` with full sourcing
- Must include JSON metadata block with threat IDs covered
- Must pass the adversarial reproduction test: state your methodology explicitly

### Intelligence Contribution
- Weekly intelligence submissions: format per `/intelligence/TEMPLATE.md`
- Must specify threat ID, date range, and source references

## Standards

**No speculation.** Every threat entry must be backed by documented incidents, not hypothetical scenarios.

**No undisclosed conflicts.** If you have a financial interest in any platform, protocol, or product mentioned, disclose it.

**No promotional content.** Framework contributions are security analysis, not marketing.

**Adversarial reproduction test:** Before submitting, ask: "Could an independent analyst with the same evidence arrive at the same CTRS score and control recommendations within ±15%?" If not, strengthen the evidence base.

## Licensing

All contributions are submitted under the same dual license as the framework:
- Code: MIT License
- Documentation and methodology: CC-BY-SA 4.0

By submitting a pull request, you confirm you have the right to contribute the material under these licenses.

---

*Cyber Strategy Institute | CryptoSHIELD Contributing Guide*
