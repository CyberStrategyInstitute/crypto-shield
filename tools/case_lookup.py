"""Read the local teaching-case register; no network or financial actions."""
import argparse
import json
from generate_reference import ROOT


def find_cases(category=None, threat=None, root=ROOT):
    cases = json.loads((root/'intelligence/case-register.json').read_text(encoding='utf-8'))['cases']
    return [c for c in cases if (category is None or c['category'].casefold() == category.casefold()) and (threat is None or c['threat_id'] == threat)]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--category')
    parser.add_argument('--threat')
    args = parser.parse_args()
    result = find_cases(args.category, args.threat)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    if not result:
        parser.exit(1, 'No matching case. See intelligence/README.md for supported categories.\n')
