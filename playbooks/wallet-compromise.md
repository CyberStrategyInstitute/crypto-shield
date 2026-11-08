# Wallet compromise response

Use an independently trusted device. If anyone is physically threatened, follow the [physical-coercion playbook](physical-coercion.md) first. A wallet balance, a seed, a token allowance, and a delegated signer are different authority boundaries.

## Choose the response by exposure

| Suspected exposure | Response | Limit |
|---|---|---|
| Approval only, key remains trusted | Identify chain, token, spender, and grant. Revoke or reduce the affected authority through its verified mechanism; confirm on-chain. | Revocation can race an attacker; a wallet connection or watch-only view cannot authorize it. |
| Unused permit or Permit2 signature | Inspect its domain, scope, nonce, deadline, and supported invalidation or lockdown path. | Resetting an ERC-20 allowance may not invalidate the signed message. |
| Seed or private key | Treat every derived account as exposed. Prepare fresh recovery material on trusted hardware and assess a safe migration. | Revoking approvals does not revoke the attacker's key. Never reuse the seed. |
| Endpoint or account session | Isolate the affected device, preserve evidence, and revoke sessions, API keys, OAuth grants, or signer access from an independent trusted path. | A password change alone may leave delegated access active. |
| Smart-account module, delegate, session key, or recovery authority | Identify each controlling authority and remove or rotate it through the account's supported process. Verify all chains and recovery paths. | Changing owners or moving one asset may leave other authority intact. |
| Sweeper, attacker monitoring, or unknown gas behavior | Do not repeatedly add gas or broadcast rescue attempts. Seek independently verified specialist help for a chain-specific recovery plan. | Deposited gas and publicly visible rescue transactions can be taken or raced. No private submission guarantees success. |
| Address poisoning only | Independently verify the intended recipient, preserve the mistaken transaction, and contact a verified receiving service if relevant. | A mistaken transfer alone does not prove seed compromise. |

If exposure is uncertain, isolate the endpoint and inventory key, signature, session, and delegation exposure before authorizing new transactions. Do not sign unfamiliar rescue payloads or disclose recovery material to a helper.

## Preserve and report

Record chain, account, transaction hashes, UTC times, permissions, suspicious signatures, communications, and observed effects. Do not delay safe containment to produce a complete report. Preserve device and key evidence; do not destroy old backups before checking recovery, remaining positions, and investigation needs.

Contact independently verified exchange or issuer support when assets reach a service that may assist. Report U.S. incidents through [FBI IC3](https://www.ic3.gov/) and relevant local authorities. Recovery is uncertain. Distinguish direct theft from frozen, returned, or reimbursed assets. Unsolicited recovery contacts and guaranteed recovery demands warrant suspicion.

## Re-entry checks

Verify fresh recovery and recipient addresses, all remaining positions and chains, revocation results, device rebuild, and signer independence before resuming. Review the authority inventory in [WKS](../01-wallet-key-sovereignty/README.md). A completed transfer does not establish that the broader incident is contained.
