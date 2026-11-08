# Research Note 004: Agent authority, independent approval, and shutdown

Status: scoped primary-source synthesis, source-checked draft; independent review pending. Review date: 2026-11-07. Scope: the linked teaching cases and control-design implications. This replaces the prior placeholder or unvalidated conclusion without declaring the broader research project complete.

## Finding

Agentic cyber misuse is relevant to crypto governance, but a non-crypto espionage disclosure does not demonstrate a financial-agent loss mechanism.

## Method and evidence

Cases were selected for explanatory value, source accessibility, and category coverage, not population representativeness or loss ranking. The reports link original publisher material and record its dates and limitations. Source review is not independent technical replication.

- [Anthropic agentic espionage disclosure: adjacent example](../intelligence/reports/anthropic-agent-misuse.md)

## Analysis

Use the adjacent vendor disclosure only for its stated tool/agent workflow and limits. Crypto exposure depends on the agent's actual signing-service access, sessions, modules, policy administration, recovery permissions, and pending intents. A model can lack a private key while retaining the ability to request harmful actions.

## Control consequences

AAS-11 binds separate human approval to exact intent. AAS-12 constrains persistent authority during shutdown. OCM-11 supplies a common exposure budget; per-agent request counts do not replace it. Memory hashes authenticate a state, not the trustworthiness of the content.

## Worked application

The agent tabletop uses two 60-unit requests against a shared 100-unit limit. Expected implementation behavior is one atomic admission or another policy-consistent refusal, never both admissions. Also test changed calldata, replay, stale valuation, approver recovery, and workers surviving shutdown. The supplied sample is synthetic and not run.

Use the [tabletop pack](../tools/tabletop-exercises.md), [playbook guide](../playbooks/README.md), and [operating guide](../OPERATING-GUIDE.md). Case facts belong in reports; reusable classes belong in taxonomy; operational decisions belong in incident logs.

## Counterexamples and remaining work

Obtain primary financial-agent incidents and implementation-specific artifacts. Measure bypasses and residual authority under real failure paths; do not publish a market-share or efficacy statistic from this teaching set.

No CTRS rating, calibrated attribution probability, population statistic, or prevention percentage is established. The [original note](https://github.com/CyberStrategyInstitute/crypto-shield/blob/051a317fb72db38f11d8928fddd5c506d24d468a/research/004_ai_agent_attack_surface.md) remains in Git history; its unsupported claims are not adopted here.
