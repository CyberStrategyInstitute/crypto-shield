# Tabletop exercises

Twelve synthetic exercises, one per category. These prompts are not historical claims or executed validation results. Use simulated values and local copies of the templates. No live funds, attack payloads, secrets, real notifications, or emergency calls.

For each exercise, assign roles, open an incident log, record the chosen route, authority to act, stop condition, expected/observed result, residual exposure, and next owner. Mark not-run until the exercise is actually completed.

## 1. Physical

Inject: A trusted person reports an immediate threat during a transfer demand.

Expected decision: Choose safety and qualified emergency help when safe; no required refusal, deception, decoy, or evidence collection under danger.

Controls: OPS-05, OPS-10. [Playbook](../playbooks/physical-coercion.md).

Pass evidence: a completed decision record identifies the stated boundary and a safe next action. A verbal claim of containment without verification is insufficient.

## 2. Insider

Inject: A support operator exports identity records without a business need.

Expected decision: Restrict the affected access, preserve audit evidence, assess downstream fraud, and avoid assuming signing keys were stolen.

Controls: GCS-04, CDG-06. [Playbook](../playbooks/consumer-fraud.md).

Pass evidence: a completed decision record identifies the stated boundary and a safe next action. A verbal claim of containment without verification is insufficient.

## 3. Social Engineering

Inject: A familiar official account posts an urgent wallet-reconnect request.

Expected decision: Verify independently; inspect administrative takeover and sessions; reject the request until authenticated.

Controls: SMS-03, SMS-08. [Playbook](../playbooks/account-takeover.md).

Pass evidence: a completed decision record identifies the stated boundary and a safe next action. A verbal claim of containment without verification is insufficient.

## 4. Malware

Inject: A recruiter assignment was executed on a machine used for signing.

Expected decision: Isolate safely, preserve evidence, inventory credentials and financial authority, and use a trusted response device.

Controls: EDD-02, WKS-11. [Playbook](../playbooks/endpoint-supply-chain.md).

Pass evidence: a completed decision record identifies the stated boundary and a safe next action. A verbal claim of containment without verification is insufficient.

## 5. Wallet

Inject: An unused permit exists and added gas is immediately swept.

Expected decision: Do not repeat gas deposits or assume allowance reset invalidates the permit; obtain a chain-specific authority and recovery plan.

Controls: WKS-08, WKS-12. [Playbook](../playbooks/wallet-compromise.md).

Pass evidence: a completed decision record identifies the stated boundary and a safe next action. A verbal claim of containment without verification is insufficient.

## 6. DeFi Protocol

Inject: A valid bridge message would mint claims beyond recorded backing.

Expected decision: Fail the backing/exposure gate and escalate through bounded pause authority; do not accept message validity as economic safety.

Controls: OCM-12, GCS-11. [Playbook](../playbooks/protocol-exploit.md).

Pass evidence: a completed decision record identifies the stated boundary and a safe next action. A verbal claim of containment without verification is insufficient.

## 7. Supply Chain

Inject: A pinned application fetches an unpinned runtime CDN library.

Expected decision: Inventory the runtime dependency and publishing access; quarantine/review the artifact rather than relying only on the lockfile.

Controls: SCD-02, SCD-07. [Playbook](../playbooks/endpoint-supply-chain.md).

Pass evidence: a completed decision record identifies the stated boundary and a safe next action. A verbal claim of containment without verification is insufficient.

## 8. AI Agent

Inject: Two agents concurrently request 60 units against a shared 100-unit budget.

Expected decision: Atomic reservations prevent both requests being authorized; shutdown must also address sessions, delegates, and queued work.

Controls: OCM-11, AAS-12. [Playbook](../playbooks/ai-agent-compromise.md).

Pass evidence: a completed decision record identifies the stated boundary and a safe next action. A verbal claim of containment without verification is insufficient.

## 9. Market Manipulation

Inject: Thin-market collateral rises sharply while a large borrower requests withdrawal.

Expected decision: Stress valuation, liquidity, concentration, and aggregate exposure; preserve evidence without declaring a crime from price movement alone.

Controls: AAS-09, OCM-11. [Playbook](../playbooks/protocol-exploit.md).

Pass evidence: a completed decision record identifies the stated boundary and a safe next action. A verbal claim of containment without verification is insufficient.

## 10. Financial Fraud

Inject: A small withdrawal succeeds, followed by a demand for an AML deposit.

Expected decision: Pause new payments and permissions, verify independently, preserve communications, and report suspected fraud.

Controls: CFD-03, CFD-04. [Playbook](../playbooks/consumer-fraud.md).

Pass evidence: a completed decision record identifies the stated boundary and a safe next action. A verbal claim of containment without verification is insufficient.

## 11. Sovereignty

Inject: A provider restricts redemption and supplies a policy notice.

Expected decision: Authenticate the notice, distinguish key control from legal/redemption rights, obtain scoped review, and do not assume either legality or overreach.

Controls: GCS-03, GCS-13. [Playbook](../playbooks/policy-custody-event.md).

Pass evidence: a completed decision record identifies the stated boundary and a safe next action. A verbal claim of containment without verification is insufficient.

## 12. Extortion

Inject: A contact promises recovery after a ransom and requests another fee.

Expected decision: Preserve evidence, verify assistance independently, and separate tracing/seizure from guaranteed return or restitution.

Controls: GCS-06, CDG-06. [Playbook](../playbooks/extortion.md).

Pass evidence: a completed decision record identifies the stated boundary and a safe next action. A verbal claim of containment without verification is insufficient.

Use the [filled synthetic authority inventory](samples/authority-inventory.synthetic.json) for the agent exercise. Its verification field is deliberately NOT RUN. These exercises test reasoning and workflow; deployed-control acceptance tests remain separate.
