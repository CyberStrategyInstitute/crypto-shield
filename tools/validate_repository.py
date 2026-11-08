"""Fail closed on malformed data, unresolved references, or stale generated views."""
from collections import Counter
from decimal import Decimal
from datetime import datetime
from pathlib import Path
import hashlib
import json
import re
import sys
from urllib.parse import unquote, urlsplit

from jsonschema import Draft7Validator, FormatChecker
from generate_reference import ROOT, controls, generated_files
from validate_cases import case_errors

FORMATS = FormatChecker()


@FORMATS.checks('date-time', raises=ValueError)
def valid_timestamp(value):
    if not isinstance(value, str):
        return True
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}[Tt]\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:[Zz]|[+-]\d{2}:\d{2})', value):
        return False
    return datetime.fromisoformat(value.upper()).tzinfo is not None


def load(path):
    def object_pairs(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f'Duplicate JSON key: {key}')
            result[key] = value
        return result

    def reject_constant(value):
        raise ValueError(f'Non-finite JSON number: {value}')

    return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=object_pairs, parse_constant=reject_constant)


def schema_errors(instance, schema):
    Draft7Validator.check_schema(schema)
    return [f'{list(e.path)}: {e.message}' for e in Draft7Validator(schema, format_checker=FORMATS).iter_errors(instance)]


def registry_errors(data, schema, items):
    errors = schema_errors(data, schema)
    if errors:
        return errors
    threats = data['threats']
    ids = [t['id'] for t in threats]
    if len(set(ids)) != len(ids):
        errors.append('Duplicate threat ID')
    if data['total_threats'] != len(threats):
        errors.append('Declared total_threats differs from actual threats')
    if set(data['threat_categories']) != {t['category'] for t in threats}:
        errors.append('Declared categories differ from actual threat categories')
    allowed = {c['id'] for c in items}
    for t in threats:
        for cid in t['candidate_controls']:
            if cid not in allowed:
                errors.append(f"{t['id']}: unknown control {cid}")
    return errors


def event_errors(event, schema, data, items):
    errors = schema_errors(event, schema)
    if errors:
        return errors
    indexed = {t['id']: t for t in data['threats']}
    threat = indexed.get(event['threat_id'])
    if threat is None:
        errors.append('Unknown event threat_id')
    elif event['category'] != threat['category']:
        errors.append('Event category does not match threat_id')
    allowed = {c['id'] for c in items}
    for cid in event.get('candidate_controls', []):
        if cid not in allowed:
            errors.append(f'Unknown event control {cid}')
    return errors


def diagnostic(rows):
    """Reproduce the disputed x5 interpretation; never emit replacement ratings."""
    score_mismatches = tier_mismatches = 0
    weights = [Decimal(w) for w in ['0.25', '0.30', '0.20', '0.15', '0.10']]
    for row in rows:
        candidate = sum(Decimal(row[k])*w for k, w in zip(['L', 'I', 'R', 'D', 'RecD'], weights))*5
        score_mismatches += candidate != Decimal(row['score'])
        tier = 'CRITICAL' if candidate >= 17 else 'HIGH' if candidate >= 13 else 'ELEVATED' if candidate >= 9 else 'LOW'
        tier_mismatches += row['tier'] != tier
    return score_mismatches, tier_mismatches


def heading_ids(text):
    result = set()
    seen = Counter()
    for line in text.splitlines():
        match = re.match(r'^#{1,6}\s+(.+?)(?:\s+#+)?$', line)
        if not match:
            continue
        title = re.sub(r'<[^>]+>', '', match[1]).lower()
        title = re.sub(r'[^\w\-\s]', '', title).replace(' ', '-')
        suffix = f'-{seen[title]}' if seen[title] else ''
        seen[title] += 1
        result.add(title+suffix)
    result.update(re.findall(r'\bid=["\']([^"\']+)', text))
    return result


def link_errors(root):
    errors = []
    for path in sorted(root.rglob('*.md')):
        if '.git' in path.parts:
            continue
        text = path.read_text(encoding='utf-8')
        prose = re.sub(r'```.*?```', '', text, flags=re.S)
        destinations = re.findall(r'!?\[[^\]\n]*\]\(([^\n]+?)\)', prose)
        destinations += re.findall(r'\b(?:src|href)=["\']([^"\']+)', prose)
        for raw in destinations:
            raw = raw.strip().strip('<>')
            if urlsplit(raw).scheme or raw.startswith('//'):
                continue
            url = urlsplit(raw)
            target = (path.parent / unquote(url.path)).resolve() if url.path else path.resolve()
            if not target.is_relative_to(root.resolve()):
                errors.append(f'{path.relative_to(root)}: link escapes repository: {raw}')
            elif not target.exists():
                errors.append(f'{path.relative_to(root)}: missing local link: {raw}')
            elif url.fragment and target.suffix == '.md':
                if unquote(url.fragment) not in heading_ids(target.read_text(encoding='utf-8')):
                    errors.append(f'{path.relative_to(root)}: missing heading: {raw}')
    return errors


def validate(root=ROOT):
    errors = []
    for path in root.rglob('*.json'):
        if '.git' not in path.parts:
            load(path)
    data = load(root/'taxonomy/registry.json')
    items = controls(root)
    errors += schema_errors(items, load(root/'metadata/control-schema.json'))
    ids = [c['id'] for c in items]
    if len(ids) != len(set(ids)):
        errors.append('Duplicate domain-owned control ID')
    prefixes = ['CDG', 'WKS', 'EDD', 'OPS', 'SMS', 'OCM', 'SCD', 'AAS', 'GCS', 'CFD']
    expected_counts = [7, 13, 10, 10, 15, 12, 10, 12, 13, 10]
    for num, prefix in enumerate(prefixes):
        expected = expected_counts[num]
        paths = list(root.glob(f'{num:02d}-*/README.md'))
        if len(paths) != 1:
            errors.append(f'Missing or ambiguous domain {num:02d}')
            continue
        found = {c['id'] for c in items if c['path'] == paths[0].relative_to(root).as_posix()}
        if found != {f'{prefix}-{n:02d}' for n in range(1, expected+1)}:
            errors.append(f'Control inventory differs in domain {num:02d}')
    errors += registry_errors(data, load(root/'metadata/registry-schema.json'), items)
    event_schema = load(root/'metadata/threat-event-schema.json')
    event_paths = list((root/'metadata/examples').glob('*.json')) + list((root/'intelligence/events').glob('*.json'))
    event_ids = []
    for path in event_paths:
        event = load(path)
        errors += [f'{path.relative_to(root)}: {e}' for e in event_errors(event, event_schema, data, items)]
        event_ids.append(event.get('id'))
    template = (root/'intelligence/TEMPLATE.md').read_text(encoding='utf-8')
    for block in re.findall(r'```json\s*\n(.*?)```', template, re.S):
        errors += [f'intelligence template: {e}' for e in event_errors(json.loads(block), event_schema, data, items)]
    if len(event_ids) != len(set(event_ids)):
        errors.append('Duplicate event ID')
    ledger = load(root/'reviews/evidence-ledger.json')
    errors += schema_errors(ledger, load(root/'metadata/evidence-schema.json'))
    records = ledger['records']
    if len({r['id'] for r in records}) != len(records):
        errors.append('Duplicate evidence ID')
    for record in records:
        if record['publication_date'] and record['publication_date'] > record['review_date']:
            errors.append(f"{record['id']}: publication date after review date")
    for name, expected_text in generated_files(root).items():
        if (root/name).read_text(encoding='utf-8') != expected_text:
            errors.append(f'Stale generated content: {name}')
    legacy = load(root/'taxonomy/legacy/registry-v1.1.json')
    legacy_scores = {t['id']: t['ctrs_score'] for t in legacy['threats']}
    current_scores = {t['id']: t['legacy_ctrs_score'] for t in data['threats']}
    if any(current_scores.get(tid) != score for tid, score in legacy_scores.items()):
        errors.append('Historical threat removed or legacy score changed without migration')
    if any(score is not None for tid, score in current_scores.items() if tid not in legacy_scores):
        errors.append('New threats must have null legacy_ctrs_score during suspension')
    snapshots = load(root/'reviews/baseline-snapshots.json')
    for name, expected_hash in snapshots['sha256'].items():
        if hashlib.sha256((root/name).read_bytes()).hexdigest() != expected_hash:
            errors.append(f'Historical snapshot changed: {name}')
    rows = load(root/'taxonomy/legacy/scoring-v1.1.json')['rows']
    if len(rows) != 44 or diagnostic(rows) != (36, 12):
        errors.append('Historical arithmetic diagnostic differs from documented baseline')
    change_log = load(root/'reviews/control-changes-v2.json')
    added_ids = {c['id'] for c in change_log['new_controls']}
    baseline_ids = {f'{prefix}-{n:02d}' for num, prefix in enumerate(prefixes) for n in range(1, (5 if num == 0 else 15 if prefix == 'SMS' else 10)+1)}
    if set(ids) != baseline_ids | added_ids or baseline_ids & added_ids or len(added_ids) != 12:
        errors.append('Major-version control additions or retained baseline IDs differ from change register')
    mapped_controls = {cid for t in data['threats'] for cid in t['candidate_controls']}
    for control in change_log['new_controls']:
        text = (root/control['path']).read_text(encoding='utf-8')
        if f"### {control['id']}:" not in text or control['acceptance'] not in text:
            errors.append(f"New control lacks registered acceptance criteria: {control['id']}")
        if control['related_threats'] and control['id'] not in mapped_controls:
            errors.append(f"New control is not mapped to threats: {control['id']}")
    errors += link_errors(root)
    errors += case_errors(root, data, items)
    for path in root.rglob('*.md'):
        if '.git' not in path.parts and '\u2014' in path.read_text(encoding='utf-8'):
            errors.append(f'Em dash in generated prose: {path.relative_to(root)}')
    return errors


if __name__ == '__main__':
    try:
        errors = validate()
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f'Validation failed: {exc}', file=sys.stderr)
        sys.exit(1)
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        sys.exit(1)
    print('Repository validation passed: registry, events, evidence, 112 controls, added-control acceptance criteria, generated views, local links, and historical diagnostics.')
