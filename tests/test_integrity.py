"""Acceptance and rejection tests for the active data and reference contracts."""
import copy
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'tools'))
from generate_reference import ROOT, controls, generated_files
from validate_repository import diagnostic, event_errors, link_errors, load, registry_errors, schema_errors, validate


class Contracts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = load(ROOT/'taxonomy/registry.json')
        cls.registry_schema = load(ROOT/'metadata/registry-schema.json')
        cls.event_schema = load(ROOT/'metadata/threat-event-schema.json')
        cls.items = controls()
        cls.event = load(ROOT/'metadata/examples/threat-event.json')

    def reject_registry(self, mutate):
        data = copy.deepcopy(self.data)
        mutate(data)
        self.assertTrue(registry_errors(data, self.registry_schema, self.items))

    def reject_event(self, mutate):
        event = copy.deepcopy(self.event)
        mutate(event)
        self.assertTrue(event_errors(event, self.event_schema, self.data, self.items))

    def test_repository_passes(self):
        self.assertEqual(validate(), [])

    def test_registry_is_not_an_event(self):
        self.assertTrue(schema_errors(self.data, self.event_schema))
        self.assertTrue(schema_errors(self.event, self.registry_schema))

    def test_missing_required_field(self):
        self.reject_registry(lambda d: d['threats'][0].pop('id'))

    def test_duplicate_threat(self):
        self.reject_registry(lambda d: d['threats'].append(copy.deepcopy(d['threats'][0])))

    def test_wrong_total(self):
        self.reject_registry(lambda d: d.update(total_threats=42))

    def test_category_drift(self):
        self.reject_registry(lambda d: d.update(threat_categories=d['threat_categories'][:-1]))

    def test_unknown_control(self):
        self.reject_registry(lambda d: d['threats'][0]['candidate_controls'].append('WKS-99'))

    def test_legacy_range(self):
        self.reject_registry(lambda d: d['threats'][0].update(legacy_ctrs_score=90))

    def test_invalid_date(self):
        self.reject_registry(lambda d: d.update(last_updated='2026-02-30'))

    def test_old_fields_are_not_silently_accepted(self):
        self.reject_registry(lambda d: d['threats'][0].update(ctrs_score=15))
        self.reject_event(lambda e: e.update(ctrs_score=90))
        self.reject_event(lambda e: e.update(false_flag_probability=0.75))

    def test_unknown_attribution_and_loss_are_valid(self):
        self.assertEqual(event_errors(self.event, self.event_schema, self.data, self.items), [])

    def test_bad_timestamp_and_negative_loss(self):
        self.reject_event(lambda e: e.update(timestamp='yesterday'))
        self.reject_event(lambda e: e.update(financial_loss_usd=-1))

    def test_event_references_and_attribution(self):
        self.reject_event(lambda e: e.update(evidence_status='reported'))
        self.reject_event(lambda e: e.update(attribution_status='assessed', references=['source']))

    def test_event_reference_integrity(self):
        self.reject_event(lambda e: e.update(threat_id='CS-WAL-99'))
        self.reject_event(lambda e: e.update(category='Physical'))
        self.reject_event(lambda e: e.update(candidate_controls=['OPS-99']))

    def test_generated_table_reacts_to_registry_change(self):
        with tempfile.TemporaryDirectory(dir=ROOT.parent) as directory:
            root = Path(directory)
            shutil.copytree(ROOT, root, dirs_exist_ok=True, ignore=shutil.ignore_patterns('.git', '__pycache__'))
            data = load(root/'taxonomy/registry.json')
            data['threats'][0]['name'] = 'Changed definition'
            (root/'taxonomy/registry.json').write_text(json.dumps(data), encoding='utf-8')
            self.assertNotEqual(generated_files(root)['taxonomy/registry-table.md'], (root/'taxonomy/registry-table.md').read_text(encoding='utf-8'))
            self.assertIn('Stale generated content: taxonomy/registry-table.md', validate(root))

    def test_missing_links_and_anchors_fail(self):
        with tempfile.TemporaryDirectory(dir=ROOT.parent) as directory:
            root = Path(directory)
            (root/'README.md').write_text('# Start\n[missing](absent.md)\n[bad anchor](#missing)', encoding='utf-8')
            self.assertEqual(len(link_errors(root)), 2)

    def test_legacy_diagnostic_is_not_a_replacement_score(self):
        rows = load(ROOT/'taxonomy/legacy/scoring-v1.1.json')['rows']
        self.assertEqual(len(rows), 44)
        self.assertEqual(diagnostic(rows), (36, 12))
        self.assertEqual(self.data['scoring_status'], 'suspended')

    def test_duplicate_json_keys_and_nonfinite_numbers_fail(self):
        with tempfile.TemporaryDirectory(dir=ROOT.parent) as directory:
            path = Path(directory)/'record.json'
            for bad in ['{"id": "first", "id": "second"}', '{"loss": NaN}', '{"loss": Infinity}']:
                path.write_text(bad, encoding='utf-8')
                with self.assertRaises(ValueError):
                    load(path)

    def test_new_threat_can_remain_unscored(self):
        data = copy.deepcopy(self.data)
        new = copy.deepcopy(data['threats'][0])
        new.update(id='CS-PHY-03', legacy_ctrs_score=None)
        data['threats'].append(new)
        data['total_threats'] += 1
        self.assertEqual(registry_errors(data, self.registry_schema, self.items), [])

    def test_event_preserves_separate_financial_effects(self):
        event = copy.deepcopy(self.event)
        event.update(chain=['ethereum'], transaction_hashes=['synthetic-hash'], financial_effects={'affected_usd': 100, 'frozen_usd': 20, 'returned_usd': None})
        self.assertEqual(event_errors(event, self.event_schema, self.data, self.items), [])
        event['financial_effects']['frozen_usd'] = -1
        self.assertTrue(event_errors(event, self.event_schema, self.data, self.items))


if __name__ == '__main__':
    unittest.main()
