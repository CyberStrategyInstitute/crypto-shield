# Endpoint and supply-chain compromise

Use during: Suspicious installation, dependency change, publishing access, build output, extension, or credential use. This is an adaptable response procedure; only authorized responders should operate production controls. Physical safety comes first.

## Observe and classify

Open a decision record using the [incident log](../tools/templates/incident-log.json). Assign incident lead, technical responder, evidence owner, and communication/legal owner as appropriate. One person may cover roles, but preserve independent approval for consequential changes.

## Contain within authority

1. Stop using the affected endpoint for signing. Isolate it when safe and preserve logs and artifacts; coordinate forensics before wiping.
2. Separate developer, publisher, build, deployer, signer, and recovery exposure. Revoke scoped credentials from independent trusted systems; inspect external registries and runtime-loaded dependencies.
3. Quarantine affected artifacts and builds. Verify source, exact versions, integrity, provenance, executed scripts, CDN loading, and release permissions before a reviewed rebuild.

## Stop conditions and escalation

Removing a package or stopping a process does not revoke stolen credentials or on-chain authority. A lockfile does not govern every runtime CDN fetch. If exposure, authorization, or a safe action cannot be established, isolate the uncertain path and escalate to an independently verified qualified responder. Never request or disclose seeds or private keys in a report.

## Verify and hand off

Verify rotated credentials, revoked sessions, clean build provenance, deployed artifact identity, wallet authority, and monitoring before reopening the workflow.

Record owner, action, UTC time, evidence, expected result, observed result, residual risk, and approval to resume. Do not mark success merely because an action was attempted. Use the [tabletop pack](../tools/tabletop-exercises.md) to rehearse without live funds or real emergency notifications.

## Related evidence

See the [case library](../intelligence/README.md) for historical sources and their limits. Case-to-playbook routes are retrospective analyst recommendations, not evidence that historical responders followed this procedure.
