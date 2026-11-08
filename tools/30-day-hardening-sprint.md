# 30-day hardening sprint

<!-- navigation:start -->
[Home](../README.md) | [All pages](../REPOSITORY-MAP.md) | [Domains](../README.md#domains-and-control-counts) | [v2.0 changes](../FRAMEWORK-UPDATE.md) | [Machine-readable index](../metadata/repository-index.json) | [Automation guide](../AUTOMATION.md)
<!-- navigation:end -->

Use this planning checklist for routine improvements. It is not an emergency response sequence. During suspected compromise, use the [wallet decision tree](../playbooks/wallet-compromise.md); during physical danger, prioritize safety. Timing and allocation thresholds are planning choices, not validated loss bounds.

## Week 1: Keys, authority, and recovery

- [ ] Inventory wallets, chains, assets, approvals, permits, modules, delegates, sessions, signing services, and recovery authority (WKS-02, WKS-07, WKS-08).
- [ ] Fill the [authority inventory](templates/authority-inventory.json) under WKS-11/12; verify each invalidation path rather than merely listing keys.
- [ ] Check hardware procurement and supported authenticity mechanisms; generate recovery material only on trusted hardware (WKS-01, WKS-04).
- [ ] Test backup recovery with a supported safe method before moving substantial assets. Never enter recovery material into an ordinary computer or website (WKS-04).
- [ ] Set a hot-wallet and delegated-exposure budget that includes permissions and open positions (WKS-09).
- [ ] For governance roles, verify actual delayed paths, cancellation, monitoring, and emergency powers rather than assuming an ordinary wallet has a timelock (WKS-03).

## Week 2: Devices and dependencies

- [ ] Separate signing from general browsing and development (EDD-02).
- [ ] Patch supported software, restrict execution, and test the configured boundary for interpreters, scripts, and trusted-process abuse (EDD-01, EDD-06, EDD-10).
- [ ] Remove unnecessary extensions and test alerts and logging (EDD-05, EDD-07).
- [ ] Practice full recipient and payload verification on a trusted independent display (EDD-04, WKS-05, WKS-06).
- [ ] For developers, review dependency provenance, lockfiles, install scripts, build artifacts, and credential isolation (SCD-01 through SCD-10).

## Week 3: Account and physical exposure

- [ ] Enable the strongest supported authentication and test independent recovery before removing optional phone recovery (SMS-01, SMS-02, SMS-04).
- [ ] Audit sessions, OAuth grants, API credentials, and recovery methods (SMS-03).
- [ ] Review identity and location exposure using the OPS-04 checklist in [Domain 03](../03-opsec-physical-security/README.md).
- [ ] Write a life-safety plan with emergency contacts, family needs, and safe communication. Decoys are optional and may increase danger (OPS-05 through OPS-10).
- [ ] Review unfamiliar-platform and unlock-payment warning signs with a trusted person (CFD-01 through CFD-09).

## Week 4: Verify and maintain

- [ ] Test monitoring on the chains and authority types actually used (OCM-02, OCM-03).
- [ ] Bind simulation and independent review to the payload actually signed (OCM-01, OCM-10).
- [ ] Review bridge backing, custody liabilities, redemption, and upgrade dependencies (OCM-07, GCS-05, CFD-10).
- [ ] If deploying agents, test independent approval, aggregate budgets, concurrency, replay, stale data, and shutdown effects (AAS-01 through AAS-10).
- [ ] Complete the [exposure-budget specification](templates/exposure-budget.json) for OCM-11 and rehearse AAS-11/12 approval/shutdown with the [synthetic exercises](tabletop-exercises.md).
- [ ] Review one relevant [historical case](../intelligence/README.md), run the [source checklist](source-review-checklist.md), and practice the corresponding playbook using an [incident log](templates/incident-log.json).
- [ ] Complete the [unscored assessment](sovereignty-self-assessment.md), assign owners and dates to gaps, and schedule monthly authority reviews and quarterly reassessment.

Record completed, incomplete, unknown, and not-applicable items with evidence. The previous fixed denominators and readiness tiers are withdrawn; task completion is not a measured security outcome.
