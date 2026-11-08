# Operating CryptoSHIELD

<!-- navigation:start -->
[Home](README.md) | [All pages](REPOSITORY-MAP.md) | [Domains](README.md#domains-and-control-counts) | [v2.0 changes](FRAMEWORK-UPDATE.md) | [Machine-readable index](metadata/repository-index.json) | [Automation guide](AUTOMATION.md)
<!-- navigation:end -->

The framework is useful when evidence leads to a decision that can be verified. Reading a control or completing a template does not install protection.

| Layer | Purpose | Example/output |
|---|---|---|
| Research | Explain a pattern, test alternatives, identify gaps | [Seven scoped notes](research/README.md) |
| Intelligence | Record one case or campaign and its evidence | [Case reports and event JSON](intelligence/README.md) |
| Taxonomy | Give reusable classes stable IDs and candidate controls | [Registry](taxonomy/registry-table.md) |
| Controls | Define requirements and acceptance criteria | [Added/updated controls](FRAMEWORK-UPDATE.md) |
| Playbooks | Route a current observation through conditional response | [Response guide](playbooks/README.md) |
| Tools | Capture implementation, authority, decisions, and verification | [Tools index](tools/README.md) |

## Worked example: suspicious wallet activity

1. Read a wallet case and its limitations. The source may establish theft without establishing seed compromise.
2. Use WKS-11 and the authority inventory to list keys, allowances, unused signatures, delegates, sessions, signers, and recovery paths.
3. Select the wallet playbook branch. An unused permit, exposed seed, endpoint compromise, and gas sweeper require different decisions.
4. Open the incident log. Record trusted device, observation, authority to act, chosen action, expected result, actual result, and stop condition. Do not add gas or sign a rescue merely because a teaching example mentions it.
5. Verify WKS-12 invalidation or recovery, identify uncancellable actions, preserve evidence, and assign the next owner. Unknown results remain unknown.
6. After containment, document the case using the intelligence template and reassess the controls. Promote only supported lessons to research and taxonomy.

## Rehearsal and routine use

Use [12 synthetic tabletops](tools/tabletop-exercises.md) before an incident and [the sprint](tools/30-day-hardening-sprint.md) for planned work. The [self-assessment](tools/sovereignty-self-assessment.md) tracks evidence for all 112 controls. Templates and lookup tools work locally and contain no transaction or notification capability.

## Evidence boundary

The library is a historical teaching sample. The adjacent AI case does not establish crypto loss; the policy case is not a criminal incident; provisional mappings are not confirmed techniques. Report publication time is distinct from occurrence. A source-checked draft needs independent review before final publication. Implementation tests, fresh legal decisions, complete recent research, and live control effectiveness remain separate work.
