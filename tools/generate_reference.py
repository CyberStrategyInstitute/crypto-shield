"""Generate reference views from domain definitions and the threat registry."""
from pathlib import Path
import json
import re
from generate_navigation import generated_navigation

ROOT = Path(__file__).resolve().parents[1]


def controls(root=ROOT):
    result = []
    for path in sorted(root.glob('[0-9][0-9]-*/README.md')):
        for line in path.read_text(encoding='utf-8').splitlines():
            cols = [c.strip() for c in line.strip('|').split('|')]
            if line.startswith('| ') and len(cols) == 3 and re.fullmatch(r'[A-Z]{3}-\d{2}', cols[0]):
                result.append(dict(zip(['id', 'name', 'priority'], cols), path=path.relative_to(root).as_posix()))
    return result


def cell(value):
    return str(value).replace('|', '\\|').replace('\n', ' ')


def registry_table(data):
    lines = ['# CryptoSHIELD threat registry', '',
             'Generated from [registry.json](registry.json). Do not edit this table manually.', '',
             f"{len(data['threats'])} threat definitions across {len(data['threat_categories'])} categories. All evidence is pending primary review. Severity is inherited qualitative metadata, separate from a calculated tier. CTRS is suspended; legacy scores are not current risk ratings. Candidate controls are proposed mitigations, not prevention evidence.", '',
             '| Threat ID | Name | Category | Severity (inherited) | Legacy CTRS (unvalidated) | Candidate controls |',
             '|---|---|---|---|---|---|']
    for t in data['threats']:
        score = t['legacy_ctrs_score'] if t['legacy_ctrs_score'] is not None else 'Not scored'
        lines.append('| ' + ' | '.join(cell(v) for v in [t['id'], t['name'], t['category'], t['severity'], score, ', '.join(t['candidate_controls'])]) + ' |')
    lines += ['', 'See [scoring suspension](ctrs-scoring.md), [migration](../metadata/README.md), and [historical records](legacy/README.md).', '']
    return '\n'.join(lines)


def inventory_table(items):
    lines = ['| Domain | Controls | Scope |', '|---|---|---|']
    paths = sorted({c['path'] for c in items})
    for path in paths:
        label = path.split('/')[0]
        count = sum(c['path'] == path for c in items)
        lines.append(f'| [{label}]({path}) | {count} | {"Cross-domain governance" if label.startswith("00") else "Operational"} |')
    operational = sum(not c['path'].startswith('00-') for c in items)
    lines.append(f'| Total | {len(items)} | {operational} operational + {len(items)-operational} cross-domain |')
    return '\n'.join(lines)


def assessment_table(items):
    lines = ['| Control | Definition | Evidence/status, owner, date, next action |', '|---|---|---|']
    for c in items:
        lines.append(f"| [{c['id']}](../{c['path']}) | {cell(c['name'])} | |")
    return '\n'.join(lines)


def replace_region(text, region, content):
    start, end = f'<!-- {region}:start -->', f'<!-- {region}:end -->'
    if text.count(start) != 1 or text.count(end) != 1:
        raise ValueError(f'Missing or duplicate {region} markers')
    before, rest = text.split(start)
    _, after = rest.split(end)
    return before + start + '\n' + content + '\n' + end + after


def generated_files(root=ROOT):
    data = json.loads((root/'taxonomy/registry.json').read_text(encoding='utf-8'))
    items = controls(root)
    operational = sum(not c['path'].startswith('00-') for c in items)
    governance = len(items) - operational
    summary = f"**CryptoSHIELD v2.0.0:** {len(data['threats'])} threats across {len(data['threat_categories'])} categories; {operational} operational controls in nine domains, plus {governance} cross-domain governance controls, for {len(items)} total. CTRS scoring is suspended. Historical scores are unvalidated and must not drive new rankings or protection claims."
    readme = replace_region((root/'README.md').read_text(encoding='utf-8'), 'summary', summary)
    return generated_navigation(root, items, {
        'taxonomy/registry-table.md': registry_table(data),
        'README.md': replace_region(readme, 'inventory', inventory_table(items)),
        'tools/sovereignty-self-assessment.md': replace_region((root/'tools/sovereignty-self-assessment.md').read_text(encoding='utf-8'), 'assessment', assessment_table(items)),
    })


if __name__ == '__main__':
    for name, text in generated_files().items():
        (ROOT/name).parent.mkdir(parents=True, exist_ok=True)
        (ROOT/name).write_text(text, encoding='utf-8', newline='\n')
        print(f'Generated {name}')
