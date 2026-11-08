# Contributing to CryptoSHIELD

Contributions need evidence that another reviewer can inspect and reproduce. Distinguish documented facts, publisher allegations, hypotheses, proposed controls, and tested results. Disclose conflicts of interest.

## Threats and controls

Use the [new-threat template](.github/ISSUE_TEMPLATE/new-threat-entry.md) or [control-update template](.github/ISSUE_TEMPLATE/control-update.md). Supply primary artifacts where available, dates, scope, contrary evidence, and limitations. Two articles repeating one disclosure are one evidence chain. A proposed threat class may be submitted as a hypothesis, but must not be called an observed incident.

Do not submit new CTRS scores during [suspension](taxonomy/ctrs-scoring.md). Qualitative priority needs a scenario and rationale. Do not invent attribution probabilities, forced binary involvement labels, or prevention guarantees. Keep unknowns explicit.

Domain READMEs own control IDs and priorities. The registry owns threat IDs, categories, and candidate control references. Explain implementation, authority boundaries, recovery, bypasses, residual harm, and acceptance tests for any control revision. Pin companion and standard references before claiming exact alignment.

## Events and evidence

Use the [intelligence template](intelligence/TEMPLATE.md) and [event contract](metadata/README.md). One JSON event per file belongs in `intelligence/events/`. Do not place event records in the threat-definition registry. Separate direct loss, affected value, freezes, compensation, and recovery. Omit victim secrets and unnecessary personal details.

For source verification, extend the [evidence ledger](reviews/evidence-ledger.json) with an exact supported claim, primary source URL, publisher, publication and review dates, evidence class, method, population, limits, and status. Discovery leads remain pending until the original artifact is examined. A source title is not verification.

## Checks

```sh
python -m pip install -r requirements-validation.txt
python tools/generate_reference.py
python tools/validate_repository.py
python -m unittest discover -s tests -v
```

Review generated diffs. Invalid schemas, unresolved IDs, missing local links, stale generated tables, invalid dates, and regression-test failures block CI. These checks do not validate external claims or deployed controls.

## Licensing

The existing [LICENSE](LICENSE) applies: code under MIT; framework and documentation under CC BY-SA 4.0. Confirm your right to contribute the material. Do not change licensing through a metadata cleanup.
