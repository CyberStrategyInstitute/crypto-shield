"""Check case/report/event links and category exercise coverage."""
from pathlib import Path
import json


def case_errors(root, data, items):
    errors = []
    register = json.loads((root/'intelligence/case-register.json').read_text(encoding='utf-8'))
    cases = register['cases']
    categories = set(data['threat_categories'])
    if {c['category'] for c in cases} != categories:
        errors.append('Teaching cases do not cover all taxonomy categories')
    if len({c['id'] for c in cases}) != len(cases):
        errors.append('Duplicate case ID')
    known_threats = {t['id']: t for t in data['threats']}
    known_controls = {c['id'] for c in items}
    required = ['Report header', 'Findings', 'Event record', 'Supporting evidence', 'Financial effects', 'Control review and follow-up']
    event_paths = set()
    for case in cases:
        for key in ['report_path', 'event_path', 'playbook_path']:
            path = (root/case[key]).resolve()
            if not path.is_relative_to(root.resolve()) or not path.is_file():
                errors.append(f"{case['id']}: missing or unsafe {key}")
        event_path = root/case['event_path']
        report_path = root/case['report_path']
        if not event_path.is_file() or not report_path.is_file():
            continue
        event_paths.add(event_path.relative_to(root).as_posix())
        event = json.loads(event_path.read_text(encoding='utf-8'))
        report = report_path.read_text(encoding='utf-8')
        if any(f'## {heading}' not in report for heading in required):
            errors.append(f"{case['id']}: report does not follow template sections")
        for field in ['id', 'category', 'threat_id']:
            if event[field] != case[field]:
                errors.append(f"{case['id']}: event/register {field} mismatch")
        threat = known_threats.get(case['threat_id'])
        if not threat or threat['category'] != case['category']:
            errors.append(f"{case['id']}: unresolved taxonomy mapping")
        if event.get('timestamp_basis') != 'publication_date' or event['timestamp'][:10] != case['publication_date']:
            errors.append(f"{case['id']}: ambiguous publication timestamp")
        if event.get('source_review_date') != case['source_review_date'] or case['publication_date'] > case['source_review_date']:
            errors.append(f"{case['id']}: invalid source review date")
        if event['references'] != case['source_urls'] or any(url not in report for url in case['source_urls']):
            errors.append(f"{case['id']}: source links differ")
        if event['candidate_controls'] != case['controls'] or any(cid not in known_controls for cid in case['controls']):
            errors.append(f"{case['id']}: unresolved case controls")
        if case['mapping_status'] == 'provisional' and 'provisional' not in report:
            errors.append(f"{case['id']}: provisional mapping hidden")
        if case['case_type'] in ['adjacent', 'policy'] and case['case_type'] not in report:
            errors.append(f"{case['id']}: case type hidden")
    if event_paths != {p.relative_to(root).as_posix() for p in (root/'intelligence/events').glob('*.json')}:
        errors.append('Case register and event file inventory differ')
    exercises = json.loads((root/'tools/tabletop-scenarios.json').read_text(encoding='utf-8'))
    if exercises['classification'] != 'synthetic_not_executed':
        errors.append('Teaching exercises must remain explicitly synthetic and unexecuted')
    if {s['category'] for s in exercises['scenarios']} != categories:
        errors.append('Tabletop exercises do not cover all categories')
    for scenario in exercises['scenarios']:
        if not (root/scenario['playbook_path']).is_file():
            errors.append(f"Missing scenario playbook: {scenario['category']}")
    return errors
