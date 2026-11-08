"""Generate accessible domain headers, navigation, and machine-readable discovery."""
from html import escape
import json
import posixpath
from urllib.parse import quote

# Statuses compare the published v2.0 specification with the v1.1 baseline.
# Materially updated IDs follow FRAMEWORK-UPDATE.md; retained does not mean tested.
DOMAINS = [
 ('CDG', 'f6921e', 'Sovereignty Governance', 5, [], 'policy-custody-event', '007_false_flag_forensics'),
 ('WKS', '60a5fa', 'Wallet & Key Sovereignty', 10, list(range(1,11)), 'wallet-compromise', '005_supply_chain_vectors'),
 ('EDD', '38bdf8', 'Endpoint & Device Defense', 10, [1,2,4,7,8,10], 'endpoint-supply-chain', '005_supply_chain_vectors'),
 ('OPS', 'fb7185', 'OPSEC & Physical Security', 10, [5,6,10], 'physical-coercion', '001_wrench_attack_epidemic'),
 ('SMS', '2dd4bf', 'Social & Platform Security', 15, [1,2,12,13,14,15], 'account-takeover', '006_pig_butchering_anatomy'),
 ('OCM', '818cf8', 'On-Chain Monitoring', 10, [1,2,3,7,8,10], 'protocol-exploit', '002_rotator_effect'),
 ('SCD', 'c084fc', 'Supply Chain Defense', 10, [2,3,7,8,9], 'endpoint-supply-chain', '005_supply_chain_vectors'),
 ('AAS', 'e879f9', 'AI Agent Security', 10, [1,2,3,6,8,9,10], 'ai-agent-compromise', '004_ai_agent_attack_surface'),
 ('GCS', 'fbbf24', 'Governance & Compliance', 10, [3,4,5,6,7], 'policy-custody-event', '006_pig_butchering_anatomy'),
 ('CFD', '34d399', 'Consumer Fraud Defense', 10, [3,4,7,8,10], 'consumer-fraud', '006_pig_butchering_anatomy'),
]


def status(cid, baseline, updated):
    number = int(cid.split('-')[1])
    return 'new' if number > baseline else 'updated' if number in updated else 'retained'


def badge(label, color):
    return f'![{label}](https://img.shields.io/badge/{quote(label)}-{color}?style=flat-square)'


def relative(path, target):
    return quote(posixpath.relpath(target, posixpath.dirname(path) or '.'), safe='/.-_#')


def nav(path):
    return ' | '.join(f'[{label}]({relative(path, target)})' for label,target in [
        ('Home','README.md'), ('All pages','REPOSITORY-MAP.md'),
        ('Domains','README.md#domains-and-control-counts'), ('v2.0 changes','FRAMEWORK-UPDATE.md'),
        ('Machine-readable index','metadata/repository-index.json'), ('Automation guide','AUTOMATION.md')])


def region(text, name, body):
    start, end = f'<!-- {name}:start -->', f'<!-- {name}:end -->'
    if start in text:
        before, rest = text.split(start)
        _, after = rest.split(end)
        return before + start + '\n' + body + '\n' + end + after
    lines = text.splitlines()
    # Preserve the requested banner as the first element of the main README.
    title = next((i for i,line in enumerate(lines) if line.lstrip('\ufeff').startswith(('# ', '## ', '### '))), len(lines)-1)
    lines[title+1:title+1] = ['', start, body, end]
    return '\n'.join(lines)+'\n'


def header_svg(number, prefix, title, color, count):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="220" viewBox="0 0 1200 220" role="img" aria-labelledby="title desc">
<title id="title">Domain {number}: {escape(title)} ({prefix})</title>
<desc id="desc">CryptoSHIELD v2.0.0. {count} control specifications. Domain definitions and evidence limits are available in the accompanying Markdown.</desc>
<defs><linearGradient id="bg" x2="1" y2="1"><stop stop-color="#111827"/><stop offset="1" stop-color="#24272e"/></linearGradient></defs>
<rect width="1200" height="220" rx="20" fill="url(#bg)"/>
<rect x="0" y="0" width="9" height="220" rx="4" fill="#{color}"/>
<path d="M1070 35 1140 62V118Q1140 163 1070 193Q1000 163 1000 118V62Z" fill="#{color}" fill-opacity=".12" stroke="#{color}" stroke-width="2"/>
<text x="1070" y="128" text-anchor="middle" fill="#{color}" font-family="sans-serif" font-size="42" font-weight="700">{number}</text>
<text x="42" y="48" fill="#{color}" font-family="sans-serif" font-size="18" letter-spacing="2">CRYPTOSHIELD / DOMAIN {number} / {prefix}</text>
<text x="42" y="103" fill="#f8fafc" font-family="sans-serif" font-size="38" font-weight="700">{escape(title)}</text>
<text x="42" y="151" fill="#cbd5e1" font-family="sans-serif" font-size="21">Published v2.0.0  |  {count} controls  |  Evidence before assurance</text>
<path d="M42 181H930" stroke="#{color}" stroke-opacity=".5"/>
</svg>
'''


def generated_navigation(root, items, current):
    output = dict(current)
    domain_records = []
    control_records = []
    for number, (prefix,color,title,baseline,updated,playbook,note) in enumerate(DOMAINS):
        path = next(p for p in sorted({c['path'] for c in items}) if p.startswith(f'{number:02}-'))
        owned = [c for c in items if c['path']==path]
        added = [c['id'] for c in owned if status(c['id'],baseline,updated)=='new']
        revised = [c['id'] for c in owned if status(c['id'],baseline,updated)=='updated']
        art = f'assets/domain-headers/{number:02}-{prefix.lower()}.svg'
        output[art] = header_svg(f'{number:02}',prefix,title,color,len(owned))
        body = [f'![Domain {number:02}: {title}, {len(owned)} control specifications](../{art})', '',
                f'[![Version 2.0.0](https://img.shields.io/badge/Version-2.0.0-{color}?style=flat-square)](../CHANGELOG.md) '+
                f'[![{len(owned)} controls](https://img.shields.io/badge/Controls-{len(owned)}-{color}?style=flat-square)](#controls) '+
                f'[![{len(added)} new controls](https://img.shields.io/badge/NEW-{len(added)}-15803d?style=flat-square)](../FRAMEWORK-UPDATE.md#added-controls) '+
                f'[![{len(revised)} materially updated controls](https://img.shields.io/badge/UPDATED-{len(revised)}-b45309?style=flat-square)](../FRAMEWORK-UPDATE.md#material-updates-to-existing-controls)', '',
                nav(path), '', '## Review this domain', '',
                f'- Apply the controls below, then record evidence in the [self-assessment](../tools/sovereignty-self-assessment.md).',
                f'- Respond using the [{playbook.replace("-", " ")} playbook](../playbooks/{playbook}.md); read the [related research note](../research/{note}.md).',
                '- Trace threat definitions in the [taxonomy](../taxonomy/README.md), cases in the [intelligence library](../intelligence/README.md), and practice in the [tabletop exercises](../tools/tabletop-exercises.md).', '',
                '### Control changes in v2.0.0', '',
                'NEW identifies added IDs. UPDATED identifies material revisions listed in the [framework comparison](../FRAMEWORK-UPDATE.md). RETAINED identifies an existing ID outside that material-update list; it does not mean the wording is unchanged or the control has been tested. Colors repeat the written labels.', '',
                '| Control | v2.0 status |', '|---|---|']
        for c in owned:
            change = status(c['id'],baseline,updated)
            color_status = {'new':'15803d','updated':'b45309','retained':'64748b'}[change]
            body.append(f"| {c['id']} | {badge(change.upper(),color_status)} |")
            control_records.append({**c,'change_in_2_0':change})
        text = output.get(path, (root/path).read_text(encoding='utf-8'))
        output[path] = region(text,'domain-overview','\n'.join(body))
        domain_records.append(dict(id=f'{number:02}',prefix=prefix,title=title,path=path,color=f'#{color}',control_count=len(owned),new_controls=added,materially_updated_controls=revised,playbook=f'playbooks/{playbook}.md',research=f'research/{note}.md'))
    paths = {p.relative_to(root).as_posix() for p in root.rglob('*.md') if '.git' not in p.parts}
    paths.update(p for p in output if p.endswith('.md'))
    paths.update(['REPOSITORY-MAP.md','AUTOMATION.md'])
    pages=[]
    for path in sorted(paths):
        text = output.get(path, (root/path).read_text(encoding='utf-8') if (root/path).exists() else '')
        title = 'Repository map' if path=='REPOSITORY-MAP.md' else next((line.lstrip('#').strip() for line in text.splitlines() if line.startswith(('# ', '## ', '### '))),path)
        kind = 'historical' if '/legacy/' in path else 'review' if path.startswith('reviews/') else 'research-draft' if path.startswith('research/') and path!='research/README.md' else 'template' if path=='intelligence/TEMPLATE.md' else 'guidance'
        pages.append(dict(path=path,title=title,content_type=kind))
        if path not in {'REPOSITORY-MAP.md', *(d['path'] for d in domain_records)}:
            output[path] = region(text,'navigation',nav(path))
    lines=['# Repository map','','Every Markdown page is listed below, including historical records and review proposals. Use the content type to distinguish current guidance from drafts, templates, and historical material. This index is generated; page titles are read from the files.','',nav('REPOSITORY-MAP.md'),'','## Domains','','| Domain | Controls | New | Materially updated |','|---|---|---|---|']
    for d in domain_records:
        lines.append(f"| [{d['id']} {d['title']}]({d['path']}) | {d['control_count']} | {len(d['new_controls'])} | {len(d['materially_updated_controls'])} |")
    lines+=['','## All pages','','| Page | Content type |','|---|---|']
    for p in pages:
        lines.append(f"| [{p['title']}]({quote(p['path'],safe='/.-_#')}) | {p['content_type']} |")
    lines+=['','## Structured data and source files','','- [Machine-readable repository index](metadata/repository-index.json): page paths, domain metadata, control IDs, priorities, and v2.0 change labels.','- [Threat registry](taxonomy/registry.json), [schema and migration guide](metadata/README.md), and [case register](intelligence/case-register.json).','- [Source and validation tools](tools/README.md), [workflow](.github/workflows/taxonomy-lint.yml), [tests](tests/test_integrity.py), and [license](LICENSE).','- [Asset register](assets/README.md).','']
    output['REPOSITORY-MAP.md']='\n'.join(lines)
    output['metadata/repository-index.json']=json.dumps(dict(index_version='1.0',framework_version='2.0.0',comparison_baseline='v1.1 (051a317fb72db38f11d8928fddd5c506d24d468a)',status_legend=dict(new='Added control ID in v2.0.0',updated='Material revision documented in FRAMEWORK-UPDATE.md',retained='Existing ID outside the documented material-revision list; wording may have changed'),entry_points=dict(human='REPOSITORY-MAP.md',automation='AUTOMATION.md',registry='taxonomy/registry.json',cases='intelligence/case-register.json'),pages=pages,domains=domain_records,controls=control_records),indent=2,ensure_ascii=False)+'\n'
    return output
