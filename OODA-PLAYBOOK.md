# CryptoSHIELD OODA response playbook

Observe, Orient, Decide, Act. Incidents may expose missing controls, bypasses, flawed assumptions, or gaps in control design. Preserve those possibilities in the retrospective. Framework adoption does not establish prevention.

## Observe

Record what happened: chain, accounts, hashes, times, permissions, devices, alerts, communications, and financial effects. Preserve original evidence and its source. Do not execute suspicious samples on a signing device or delay safety to gather evidence.

## Orient

Classify exposure separately from actor attribution. Compare external compromise, malicious insiders, deceived insiders, supply-chain compromise, design defects, and operational mistakes against the same evidence. Privileged access does not establish malicious intent. A code change, rapid attribution, or financial benefit does not prove a false flag.

Use qualitative uncertainty and competing hypotheses. Record official allegations, vendor statements, observed facts, and analyst inference separately. The former three-YES probability rule and insider-first requirement are withdrawn. No calibrated false-flag probability is established.

## Decide

| Incident | Procedure |
|---|---|
| Physical coercion or immediate threat | [Physical coercion](playbooks/physical-coercion.md) |
| Wallet, key, approval, delegation, or endpoint exposure | [Wallet compromise decision tree](playbooks/wallet-compromise.md) |
| Social engineering or investment fraud | [Consumer fraud](playbooks/consumer-fraud.md) |
| Protocol or supply-chain compromise | [Protocol and supply-chain response](#protocol-and-supply-chain-response) |
| Agent or signing-service compromise | [AI agent response](#ai-agent-response) |

There is no universal revoke-and-migrate sequence. Revocation may not invalidate keys or unused permits; migration can race a sweeper. Use the wallet decision tree from a trusted device.

## Act

Execute the selected procedure, verify the result, and reassess exposure. Preserve evidence when safe, use independently verified support channels, and report relevant incidents. Neither a 15-minute window nor an asset-recovery outcome is guaranteed. Do not delay urgent containment for attribution or public relations.

## Protocol and supply-chain response

Use preauthorized pause or cancellation powers only within their audited scope. Alert signers through independent channels. Preserve build artifacts, deployment and access logs, queued actions, and source history. Isolate affected build or signing infrastructure and revoke scoped credentials from a trusted environment.

Do not deploy a generic timelock override. Emergency powers need independent authorization, least privilege, expiry, audit, and restoration tests. Check that they cannot transfer arbitrary assets or bypass upgrade restrictions. Communicate confirmed facts and safe user actions through authenticated channels; protect sensitive victim data and coordinate exploit details with responders.

## AI agent response

Stop new authorizations and revoke agent sessions, delegates, API credentials, and signing-service permissions. Halt spawning and shared workflows. Inspect pending and already signed intents, approvals, and all affected chains. Stopping a process does not cancel a broadcast transaction or revoke a permit. Apply the wallet decision tree to remaining authority. Preserve policy versions, prompts, memory changes, tool calls, approval records, and chain effects.

Use AAS-12 for shutdown scope, WKS-11/12 for authority inventory and invalidation, and GCS-11 for bounded emergency powers. Their domain definitions provide acceptance criteria; an incident responder must verify the actual implementation and residual authority.

## Review and reporting

For U.S. theft or fraud, report through [FBI IC3](https://www.ic3.gov/) and relevant authorities. Seek emergency help for immediate physical danger. Verify receiving-service contacts independently. Do not disclose seeds, private keys, or victim details publicly. No tracing provider or reporting path guarantees recovery.

Review control design as well as implementation. Record protections present, bypass paths, residual harm, alternative causes, and specific acceptance tests. Use [the intelligence template](intelligence/TEMPLATE.md), and keep uncertain attribution unknown.
