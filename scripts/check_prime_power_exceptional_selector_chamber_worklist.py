#!/usr/bin/env python3
"""Publish exact full-selector chambers for all 89 rank-three-exceptional hosts.

For each critical or excess raw host, this checker links the canonical exceptional
priority record to the affine selector-row library. Hosts admitting rank-three-free
responses receive the exact union of lexicographic chambers in which a zero-rank-three
response is the full background-dependent selector. The eleven positive-minimum hosts
receive the complete full-selector chamber atlas instead.
"""
from __future__ import annotations
import copy
import json
import sys
from collections import Counter
from functools import lru_cache
from pathlib import Path
from random import Random
from typing import Any
import check_prime_power_background_signature as signature
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_exceptional_host_priority_manifest as priority
import check_prime_power_selector_chamber_manifest as chamber
EXPECTED_WORKLIST_SHA256 = '113fe7949eab855927e1f1756a52df2a2c6e0871afc87cfe3e8bd325fe010044'

class WorklistError(ValueError):
    """Raised when the exceptional selector chamber worklist is inconsistent."""

def require(condition: bool, message: str) -> None:
    if not condition:
        raise WorklistError(message)

def row_difference(selected: dict[str, Any], other: dict[str, Any]) -> dict[str, Any]:
    cross = Counter(other['rank1_cross_unit_indices'])
    cross.subtract(selected['rank1_cross_unit_indices'])
    line = Counter({index: value for index, value in other['rank2_line_coefficients']})
    line.subtract({index: value for index, value in selected['rank2_line_coefficients']})
    return {'rank1_cross_coefficients': [[index, value] for index, value in sorted(cross.items()) if value], 'rank2_line_coefficients': [[index, value] for index, value in sorted(line.items()) if value], 'constant': other['rank3_constant'] - selected['rank3_constant']}

def chamber_record(host_record: dict[str, Any], selected_index: int, rows: dict[str, dict[str, Any]]) -> dict[str, Any]:
    selected_id = host_record['response_row_sha256s'][selected_index]
    selected = rows[selected_id]
    inequalities = []
    for index, other_id in enumerate(host_record['response_row_sha256s']):
        if index == selected_index:
            continue
        other = rows[other_id]
        difference = row_difference(selected, other)
        record = {'other_row_sha256': other_id, 'other_permutation': other['permutation'], 'strict': int(index < selected_index), 'difference': difference}
        record['inequality_sha256'] = catalogue.canonical_digest(record)
        inequalities.append(record)
    output: dict[str, Any] = {'selected_index': selected_index, 'selected_row_sha256': selected_id, 'selected_permutation': selected['permutation'], 'selected_rank3_triples': selected['rank3_constant'], 'inequalities': inequalities}
    output['selector_chamber_sha256'] = catalogue.canonical_digest(output)
    return output

@lru_cache(maxsize=1)
def _build_worklist_cached() -> dict[str, Any]:
    source = catalogue.build_catalogue()
    catalogue.validate_catalogue(source)
    priority_manifest = priority.build_priority_manifest()
    priority.validate_priority_manifest(priority_manifest)
    chamber_manifest = chamber.build_manifest()
    chamber.validate_manifest(chamber_manifest)
    hosts = {host['host_id']: host for host in source['hosts']}
    chamber_hosts = {record['host_id']: record for record in chamber_manifest['host_chambers']}
    rows = {row['row_sha256']: row for row in chamber_manifest['affine_rows']}
    records = []
    unique_zero_pairs: set[tuple[str, str, int]] = set()
    unique_hard_pairs: set[tuple[str, str, int]] = set()
    zero_response_occurrences = 0
    minimum_response_occurrences = 0
    zero_inequalities = 0
    hard_inequalities = 0
    for exceptional in sorted(priority_manifest['exceptional_hosts'], key=lambda record: record['host_id']):
        host = hosts[exceptional['host_id']]
        host_chamber = chamber_hosts[host['host_id']]
        require(len(host['responses']) == len(host_chamber['response_row_sha256s']), 'host response/chamber count mismatch')
        rank3_values = [response['triple_count'] for response in host['responses']]
        minimum = min(rank3_values)
        zero_indices = [index for index, value in enumerate(rank3_values) if value == 0]
        minimum_indices = [index for index, value in enumerate(rank3_values) if value == minimum]
        selected_indices = zero_indices if zero_indices else list(range(len(rank3_values)))
        selector_chambers = [chamber_record(host_chamber, index, rows) for index in selected_indices]
        for selector_record in selector_chambers:
            selector_record['rank3_minimum'] = int(selector_record['selected_rank3_triples'] == minimum)
            selector_record['selector_chamber_sha256'] = catalogue.canonical_digest({key: value for key, value in selector_record.items() if key != 'selector_chamber_sha256'})
        for selector_record in selector_chambers:
            for inequality in selector_record['inequalities']:
                pair = (selector_record['selected_row_sha256'], inequality['other_row_sha256'], inequality['strict'])
                if zero_indices:
                    unique_zero_pairs.add(pair)
                    zero_inequalities += 1
                else:
                    unique_hard_pairs.add(pair)
                    hard_inequalities += 1
        zero_response_occurrences += len(zero_indices)
        minimum_response_occurrences += len(minimum_indices)
        record: dict[str, Any] = {'host_id': host['host_id'], 'catalogue_record_sha256': host['record_sha256'], 'priority_signature_class_id': exceptional['signature_class_id'], 'side': host['side'], 'rank3_slack': host['rank3_slack'], 'rank3_reduction_required': exceptional['rank3_reduction_required'], 'minimum_rank3_triples': minimum, 'zero_rank3_responses': len(zero_indices), 'minimum_rank3_responses': len(minimum_indices), 'worklist_kind': 'zero-rank3-selector-union' if zero_indices else 'positive-minimum-hard-core', 'selector_chambers': selector_chambers}
        record['host_worklist_sha256'] = catalogue.canonical_digest(record)
        records.append(record)
    payload: dict[str, Any] = {'version': 1, 'source_catalogue_sha256': source['catalogue_sha256'], 'source_priority_sha256': priority_manifest['priority_sha256'], 'source_chamber_sha256': chamber_manifest['chamber_sha256'], 'hosts': records}
    payload['claims'] = {'exceptional_hosts': len(records), 'zero_rank3_hosts': sum((record['zero_rank3_responses'] > 0 for record in records)), 'hard_core_hosts': sum((record['zero_rank3_responses'] == 0 for record in records)), 'zero_rank3_response_occurrences': zero_response_occurrences, 'minimum_rank3_response_occurrences': minimum_response_occurrences, 'zero_selector_chambers': sum((len(record['selector_chambers']) for record in records if record['zero_rank3_responses'] > 0)), 'hard_core_selector_chambers': sum((len(record['selector_chambers']) for record in records if record['zero_rank3_responses'] == 0)), 'hard_core_minimum_rank3_chambers': sum((selector_record['rank3_minimum'] for record in records if record['zero_rank3_responses'] == 0 for selector_record in record['selector_chambers'])), 'zero_chamber_inequalities': zero_inequalities, 'hard_core_chamber_inequalities': hard_inequalities, 'unique_zero_ordered_row_conditions': len(unique_zero_pairs), 'unique_hard_ordered_row_conditions': len(unique_hard_pairs), 'zero_chamber_distribution': [[count, sum((record['zero_rank3_responses'] == count for record in records))] for count in sorted({record['zero_rank3_responses'] for record in records if record['zero_rank3_responses'] > 0})], 'hard_minimum_distribution': [[minimum, sum((record['minimum_rank3_triples'] == minimum and record['zero_rank3_responses'] == 0 for record in records))] for minimum in sorted({record['minimum_rank3_triples'] for record in records if record['zero_rank3_responses'] == 0})]}
    payload['worklist_sha256'] = catalogue.canonical_digest(payload)
    return payload

def build_worklist() -> dict[str, Any]:
    return copy.deepcopy(_build_worklist_cached())

def validate_worklist(worklist: Any) -> dict[str, Any]:
    require(isinstance(worklist, dict), 'worklist: expected object')
    expected = _build_worklist_cached()
    for key in ('version', 'source_catalogue_sha256', 'source_priority_sha256', 'source_chamber_sha256', 'hosts', 'claims', 'worklist_sha256'):
        require(worklist.get(key) == expected[key], f'{key}: canonical mismatch')
    claims = expected['claims']
    require((claims['exceptional_hosts'], claims['zero_rank3_hosts'], claims['hard_core_hosts']) == (89, 78, 11), 'exceptional selector host census mismatch')
    require(claims['hard_minimum_distribution'] == [[1, 9], [4, 2]], 'hard-core minimum distribution mismatch')
    if EXPECTED_WORKLIST_SHA256 != 'TO_BE_FILLED':
        require(expected['worklist_sha256'] == EXPECTED_WORKLIST_SHA256, 'built-in worklist digest drift')
    return copy.deepcopy(claims)

def evaluate_difference(difference: dict[str, Any], survivor_signature: dict[str, Any]) -> int:
    return sum((value * survivor_signature['rank1_cross_differences'][index] for index, value in difference['rank1_cross_coefficients'])) + sum((value * survivor_signature['response_line_background_counts'][index] for index, value in difference['rank2_line_coefficients'])) + difference['constant']

def chamber_holds(selector_chamber: dict[str, Any], survivor_signature: dict[str, Any]) -> bool:
    for inequality in selector_chamber['inequalities']:
        difference = evaluate_difference(inequality['difference'], survivor_signature)
        if inequality['strict']:
            if not difference > 0:
                return False
        elif difference < 0:
            return False
    return True

def run_random_tests() -> tuple[int, Counter[str], Counter[int]]:
    random = Random(2110)
    source = catalogue.build_catalogue()
    hosts = {host['host_id']: host for host in source['hosts']}
    records = _build_worklist_cached()['hosts']
    totals: Counter[str] = Counter()
    selected_rank3_distribution: Counter[int] = Counter()
    for _ in range(500):
        work_record = random.choice(records)
        host = hosts[work_record['host_id']]
        background = signature.random_background(host['side'], random)
        certificate = signature.build_certificate(host, background)
        signature.validate_certificate(certificate)
        selected, _values = chamber.selected_row(host['host_id'], certificate['signature'])
        holding = [record for record in work_record['selector_chambers'] if chamber_holds(record, certificate['signature'])]
        selected_is_worklist = any((record['selected_row_sha256'] == selected['row_sha256'] for record in holding))
        selected_rank3 = selected['rank3_constant']
        selected_rank3_distribution[selected_rank3] += 1
        totals['systems'] += 1
        totals['zero_host'] += int(work_record['zero_rank3_responses'] > 0)
        totals['hard_host'] += int(work_record['zero_rank3_responses'] == 0)
        totals['selected_zero'] += int(selected_rank3 == 0)
        totals['selected_in_worklist'] += int(selected_is_worklist)
        if work_record['zero_rank3_responses'] > 0:
            require(selected_is_worklist == (selected_rank3 == 0), 'zero-selector chamber union mismatch')
        else:
            require(selected_is_worklist, 'hard-core chamber atlas did not contain full selector')
    return (500, totals, selected_rank3_distribution)

def run_mutation_tests() -> int:
    worklist = build_worklist()
    validate_worklist(worklist)
    mutations: list[dict[str, Any]] = []

    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(worklist)
        mutator(candidate)
        mutations.append(candidate)
    add(lambda data: data.update(worklist_sha256='0' * 64))
    add(lambda data: data.update(source_chamber_sha256='0' * 64))
    add(lambda data: data.update(version=2))
    add(lambda data: data['claims'].update(exceptional_hosts=88))
    add(lambda data: data['hosts'].reverse())
    add(lambda data: data['hosts'][0].update(host_id='s5-corrupt'))
    add(lambda data: data['hosts'][0].update(worklist_kind='corrupt'))
    add(lambda data: data['hosts'][0]['selector_chambers'].pop())

    def reverse_nontrivial_inequalities(data: dict[str, Any]) -> None:
        for host in data['hosts']:
            for selector_record in host['selector_chambers']:
                if len(selector_record['inequalities']) >= 2:
                    selector_record['inequalities'].reverse()
                    return
        raise AssertionError('no nontrivial selector chamber')
    add(reverse_nontrivial_inequalities)
    add(lambda data: data['hosts'][0]['selector_chambers'][0].update(selected_rank3_triples=999))
    add(lambda data: data['hosts'][0]['selector_chambers'][0]['inequalities'][0].update(strict=2))
    add(lambda data: data['hosts'][0].update(host_worklist_sha256='0' * 64))
    rejected = 0
    for candidate in mutations:
        try:
            validate_worklist(candidate)
        except (WorklistError, priority.PriorityError, chamber.ChamberError, catalogue.CatalogueError):
            rejected += 1
    require(rejected == len(mutations), 'mutation tests: corrupted worklist accepted')
    return rejected

def main() -> None:
    if len(sys.argv) == 3 and sys.argv[1] == '--write':
        worklist = build_worklist()
        validate_worklist(worklist)
        Path(sys.argv[2]).write_text(json.dumps(worklist, sort_keys=True, indent=2) + '\n', encoding='utf-8')
        print(f"wrote exceptional selector chamber worklist: sha256 {worklist['worklist_sha256']}")
        return
    if len(sys.argv) == 2:
        with Path(sys.argv[1]).open('r', encoding='utf-8') as handle:
            worklist = json.load(handle)
        claims = validate_worklist(worklist)
        print(f"accepted exceptional selector chamber worklist: {claims['zero_selector_chambers']} zero chambers")
        return
    if len(sys.argv) != 1:
        raise SystemExit('usage: check_prime_power_exceptional_selector_chamber_worklist.py [worklist.json | --write worklist.json]')
    worklist = build_worklist()
    claims = validate_worklist(worklist)
    systems, totals, selected_distribution = run_random_tests()
    rejected = run_mutation_tests()
    print(f"verified exceptional selector chambers: {claims['exceptional_hosts']} hosts, {claims['zero_rank3_hosts']} zero-capable and {claims['hard_core_hosts']} hard-core, {claims['zero_selector_chambers']} zero chambers, {claims['hard_core_selector_chambers']} hard chambers, {claims['zero_chamber_inequalities']}/{claims['hard_core_chamber_inequalities']} inequalities, {claims['unique_zero_ordered_row_conditions']}/{claims['unique_hard_ordered_row_conditions']} unique conditions, zero-chamber distribution {claims['zero_chamber_distribution']}, {systems} regression systems with selected rank3 distribution {sorted(selected_distribution.items())}, worklist sha256 {worklist['worklist_sha256']}, and {rejected} corruptions rejected")
if __name__ == '__main__':
    main()
