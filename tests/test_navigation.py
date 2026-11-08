"""Regression checks for discoverability and accessible generated domain headers."""
import json
from pathlib import Path
import sys
import unittest
import xml.etree.ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'tools'))
from generate_reference import ROOT, generated_files


class Navigation(unittest.TestCase):
    def test_every_page_is_discoverable_and_has_return_navigation(self):
        index=json.loads((ROOT/'metadata/repository-index.json').read_text(encoding='utf-8'))
        actual={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*.md') if '.git' not in p.parts}
        self.assertEqual(actual, {p['path'] for p in index['pages']})
        for page in index['pages']:
            text=(ROOT/page['path']).read_text(encoding='utf-8')
            self.assertIn('All pages](', text, page['path'])
            self.assertIn('Automation guide](', text, page['path'])

    def test_control_statuses_and_accessible_headers(self):
        index=json.loads((ROOT/'metadata/repository-index.json').read_text(encoding='utf-8'))
        controls=index['controls']
        self.assertEqual(112, len({c['id'] for c in controls}))
        self.assertEqual(12, sum(c['change_in_2_0']=='new' for c in controls))
        self.assertEqual({'new','updated','retained'}, {c['change_in_2_0'] for c in controls})
        colors=set()
        ns={'s':'http://www.w3.org/2000/svg'}
        for domain in index['domains']:
            colors.add(domain['color'])
            image=ROOT/f"assets/domain-headers/{domain['id']}-{domain['prefix'].lower()}.svg"
            svg=ET.fromstring(image.read_text(encoding='utf-8'))
            self.assertEqual('img',svg.attrib['role'])
            self.assertIn(domain['prefix'],svg.find('s:title',ns).text)
            self.assertIn(str(domain['control_count']),svg.find('s:desc',ns).text)
        self.assertEqual(10,len(colors))

    def test_generation_is_stable_and_preserves_star_history(self):
        for path,text in generated_files().items():
            self.assertEqual((ROOT/path).read_text(encoding='utf-8'),text,path)
        readme=generated_files()['README.md']
        self.assertIn('## Star History',readme)
        self.assertIn('prefers-color-scheme: dark',readme)
        self.assertIn('https://api.star-history.com/chart?',readme)
