# Account or social-platform takeover

Use during: Unknown posts, sessions, recovery changes, or administrative account reassignment. This is an adaptable response procedure; only authorized responders should operate production controls. Physical safety comes first.

## Observe and classify

Open a decision record using the [incident log](../tools/templates/incident-log.json). Assign incident lead, technical responder, evidence owner, and communication/legal owner as appropriate. One person may cover roles, but preserve independent approval for consequential changes.

## Contain within authority

1. Establish an independent trusted communication path. Warn affected users through a channel the attacker does not control; avoid unverified attribution.
2. From a trusted device, use the platform's authenticated recovery and session-management process. Revoke sessions, OAuth grants, API keys, and compromised recovery methods as supported.
3. Check whether account content requested payments, installations, or wallet signatures. Route resulting financial or device exposure to the wallet or endpoint playbook.

## Stop conditions and escalation

A password reset alone may leave sessions or third-party grants active. A platform administrator can sometimes override ordinary user authentication. If exposure, authorization, or a safe action cannot be established, isolate the uncertain path and escalate to an independently verified qualified responder. Never request or disclose seeds or private keys in a report.

## Verify and hand off

Verify account ownership and recovery, enumerate remaining sessions/grants, confirm malicious posts are addressed, and monitor for recurrence.

Record owner, action, UTC time, evidence, expected result, observed result, residual risk, and approval to resume. Do not mark success merely because an action was attempted. Use the [tabletop pack](../tools/tabletop-exercises.md) to rehearse without live funds or real emergency notifications.

## Related evidence

See the [case library](../intelligence/README.md) for historical sources and their limits. Case-to-playbook routes are retrospective analyst recommendations, not evidence that historical responders followed this procedure.
