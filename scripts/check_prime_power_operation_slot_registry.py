#!/usr/bin/env python3
"""Validate noncircular expected operation-slot registries and population gaps.

A fibre ID includes a digest of populated source data, so it is not the right primary
key for an independently expected registry. This checker introduces an operation slot
whose exact identity is the parent-rule tuple

    (parent state, operation kind, operation key, expected raw host, ordered labels).

The expected slot registry is built before witness/source population. A population
manifest then maps zero or one concrete fibre to each slot. Missing, unexpected and
host-mismatched entries are reconstructed exactly; completeness means exact slot
coverage and never follows merely from the number of supplied fibres.
"""
from __future__ import annotations
import copy
import json
import sys
from collections import Counter
from pathlib import Path
from random import Random
from typing import Any
import check_prime_power_canonical_raw_host_catalogue as catalogue
EXPECTED_SYNTHETIC_REGISTRY_SHA256 = 'c598f730fc90132714e960ab9d73cf4bd0c8bbf3de20bb430a30b3cb8c1bfb24'
LABEL_KEYS = ('provenance', 'collision', 'local_line', 'interface', 'root', 'thin', 'crt')

class SlotRegistryError(ValueError):
    """Raised when a slot registry or population audit is inconsistent."""

def require(condition: bool, message: str) -> None:
    if not condition:
        raise SlotRegistryError(message)

def exact_slot_core(record: dict[str, Any]) -> dict[str, Any]:
    parent_state_id = record.get('parent_state_id')
    operation_kind = record.get('operation_kind')
    operation_key = record.get('operation_key')
    expected_host_id = record.get('expected_host_id')
    labels = record.get('state_labels')
    require(isinstance(parent_state_id, str) and parent_state_id, 'parent_state_id: expected nonempty string')
    require(isinstance(operation_kind, str) and operation_kind, 'operation_kind: expected nonempty string')
    require(isinstance(operation_key, dict), 'operation_key: expected object')
    require(isinstance(expected_host_id, str), 'expected_host_id: expected string')
    require(isinstance(labels, dict) and tuple(labels) == LABEL_KEYS, 'state_labels: exact ordered label keys required')
    require(all((isinstance(labels[key], str) and labels[key] for key in LABEL_KEYS)), 'state_labels: nonempty strings required')
    return {'parent_state_id': parent_state_id, 'operation_kind': operation_kind, 'operation_key': operation_key, 'expected_host_id': expected_host_id, 'state_labels': labels}

def build_slot(core: dict[str, Any]) -> dict[str, Any]:
    exact = exact_slot_core(core)
    slot = copy.deepcopy(exact)
    slot['slot_id'] = f'slot-{catalogue.canonical_digest(exact)[:20]}'
    slot['slot_sha256'] = catalogue.canonical_digest(slot)
    return slot

def exact_registry(registry: dict[str, Any]) -> dict[str, Any]:
    source_catalogue = catalogue.build_catalogue()
    catalogue.validate_catalogue(source_catalogue)
    host_ids = {host['host_id'] for host in source_catalogue['hosts']}
    rule_id = registry.get('rule_id')
    rule_source = registry.get('rule_source')
    require(isinstance(rule_id, str) and rule_id, 'rule_id: expected nonempty string')
    require(isinstance(rule_source, dict), 'rule_source: expected object')
    raw_slots = registry.get('slots')
    require(isinstance(raw_slots, list), 'slots: expected list')
    slots = []
    for index, raw in enumerate(raw_slots):
        require(isinstance(raw, dict), f'slots[{index}]: expected object')
        slot = build_slot(raw)
        require(raw == slot, f'slots[{index}]: noncanonical slot record')
        require(slot['expected_host_id'] in host_ids, f'slots[{index}]: unknown expected host')
        slots.append(slot)
    require(slots == sorted(slots, key=lambda record: record['slot_id']), 'slots: canonical slot_id order required')
    slot_ids = [slot['slot_id'] for slot in slots]
    require(len(slot_ids) == len(set(slot_ids)), 'slots: duplicate slot_id')
    cores = [exact_slot_core(slot) for slot in slots]
    require(len({catalogue.canonical_digest(core) for core in cores}) == len(cores), 'slots: duplicate exact operation core')
    host_counts = Counter((slot['expected_host_id'] for slot in slots))
    parent_counts = Counter((slot['parent_state_id'] for slot in slots))
    kind_counts = Counter((slot['operation_kind'] for slot in slots))
    claims = {'slots': len(slots), 'unique_parents': len(parent_counts), 'unique_hosts': len(host_counts), 'unique_operation_kinds': len(kind_counts), 'host_multiplicity_distribution': [[multiplicity, sum((value == multiplicity for value in host_counts.values()))] for multiplicity in sorted(set(host_counts.values()))], 'operation_kind_distribution': [[key, kind_counts[key]] for key in sorted(kind_counts)], 'rule_source_sha256': catalogue.canonical_digest(rule_source), 'slots_sha256': catalogue.canonical_digest(slots)}
    return {'slots': slots, 'claims': claims}

def validate_registry(registry: Any) -> dict[str, int]:
    require(isinstance(registry, dict), 'registry: expected object')
    require(registry.get('version') == 1, 'version: expected 1')
    exact = exact_registry(registry)
    require(registry.get('claims') == exact['claims'], 'claims: incorrect')
    payload = {key: value for key, value in registry.items() if key != 'registry_sha256'}
    require(registry.get('registry_sha256') == catalogue.canonical_digest(payload), 'registry_sha256: incorrect')
    return {'slots': exact['claims']['slots'], 'parents': exact['claims']['unique_parents'], 'hosts': exact['claims']['unique_hosts'], 'kinds': exact['claims']['unique_operation_kinds']}

def build_registry(rule_id: str, rule_source: dict[str, Any], slot_cores: list[dict[str, Any]]) -> dict[str, Any]:
    slots = sorted((build_slot(core) for core in slot_cores), key=lambda record: record['slot_id'])
    registry: dict[str, Any] = {'version': 1, 'rule_id': rule_id, 'rule_source': rule_source, 'slots': slots}
    registry['claims'] = exact_registry(registry)['claims']
    registry['registry_sha256'] = catalogue.canonical_digest(registry)
    return registry

def exact_population_audit(audit: dict[str, Any]) -> dict[str, Any]:
    registry = audit.get('expected_registry')
    require(isinstance(registry, dict), 'expected_registry: expected object')
    validate_registry(registry)
    expected_slots = {slot['slot_id']: slot for slot in registry['slots']}
    raw_entries = audit.get('population_entries')
    require(isinstance(raw_entries, list), 'population_entries: expected list')
    entries = []
    for index, entry in enumerate(raw_entries):
        require(isinstance(entry, dict), f'population_entries[{index}]: expected object')
        slot_id = entry.get('slot_id')
        host_id = entry.get('host_id')
        fibre_id = entry.get('fibre_id')
        source_sha256 = entry.get('source_sha256')
        require(isinstance(slot_id, str), f'population_entries[{index}].slot_id: expected string')
        require(isinstance(host_id, str), f'population_entries[{index}].host_id: expected string')
        require(isinstance(fibre_id, str) and fibre_id, f'population_entries[{index}].fibre_id: expected nonempty string')
        require(isinstance(source_sha256, str) and len(source_sha256) == 64, f'population_entries[{index}].source_sha256: expected SHA-256')
        core = {'slot_id': slot_id, 'host_id': host_id, 'fibre_id': fibre_id, 'source_sha256': source_sha256}
        exact = copy.deepcopy(core)
        exact['population_record_sha256'] = catalogue.canonical_digest(exact)
        require(entry == exact, f'population_entries[{index}]: noncanonical record')
        entries.append(exact)
    require(entries == sorted(entries, key=lambda record: (record['slot_id'], record['fibre_id'])), 'population_entries: canonical order required')
    slot_counts = Counter((entry['slot_id'] for entry in entries))
    duplicate_slots = sorted((slot_id for slot_id, count in slot_counts.items() if count > 1))
    expected_ids = set(expected_slots)
    supplied_ids = set(slot_counts)
    missing = sorted(expected_ids - supplied_ids)
    unexpected = sorted(supplied_ids - expected_ids)
    host_mismatches = sorted((entry['slot_id'] for entry in entries if entry['slot_id'] in expected_slots and entry['host_id'] != expected_slots[entry['slot_id']]['expected_host_id']))
    complete = int(not missing and (not unexpected) and (not duplicate_slots) and (not host_mismatches))
    claims = {'expected_slots': len(expected_ids), 'population_entries': len(entries), 'covered_expected_slots': len(expected_ids & supplied_ids), 'missing_slots': len(missing), 'unexpected_slots': len(unexpected), 'duplicate_slots': len(duplicate_slots), 'host_mismatches': len(host_mismatches), 'complete': complete, 'missing_slot_ids': missing, 'unexpected_slot_ids': unexpected, 'duplicate_slot_ids': duplicate_slots, 'host_mismatch_slot_ids': host_mismatches, 'population_records_sha256': catalogue.canonical_digest(entries)}
    return {'population_entries': entries, 'claims': claims}

def validate_population_audit(audit: Any) -> dict[str, int]:
    require(isinstance(audit, dict), 'audit: expected object')
    require(audit.get('version') == 1, 'version: expected 1')
    exact = exact_population_audit(audit)
    require(audit.get('claims') == exact['claims'], 'claims: incorrect')
    payload = {key: value for key, value in audit.items() if key != 'audit_sha256'}
    require(audit.get('audit_sha256') == catalogue.canonical_digest(payload), 'audit_sha256: incorrect')
    claims = exact['claims']
    return {'expected': claims['expected_slots'], 'entries': claims['population_entries'], 'covered': claims['covered_expected_slots'], 'missing': claims['missing_slots'], 'unexpected': claims['unexpected_slots'], 'duplicates': claims['duplicate_slots'], 'mismatches': claims['host_mismatches'], 'complete': claims['complete']}

def build_population_audit(registry: dict[str, Any], entries: list[dict[str, Any]]) -> dict[str, Any]:
    canonical_entries = []
    for entry in entries:
        core = {key: entry[key] for key in ('slot_id', 'host_id', 'fibre_id', 'source_sha256')}
        core['population_record_sha256'] = catalogue.canonical_digest(core)
        canonical_entries.append(core)
    canonical_entries.sort(key=lambda record: (record['slot_id'], record['fibre_id']))
    audit: dict[str, Any] = {'version': 1, 'expected_registry': registry, 'population_entries': canonical_entries}
    audit['claims'] = exact_population_audit(audit)['claims']
    audit['audit_sha256'] = catalogue.canonical_digest(audit)
    return audit

def synthetic_registry() -> dict[str, Any]:
    random = Random(2118)
    hosts = catalogue.build_catalogue()['hosts']
    slot_cores = []
    kinds = ('delete-and-match', 'rollback-and-match', 'weighted-match')
    for index in range(180):
        host = hosts[(index * 37 + 11) % len(hosts)]
        labels = {'provenance': f'prov-{index % 9}', 'collision': f'collision-{index % 5}', 'local_line': f'line-{index % 13}', 'interface': f'interface-{index % 7}', 'root': f'root-{index % 4}', 'thin': f'thin-{index % 3}', 'crt': f'crt-{index % 6}'}
        slot_cores.append({'parent_state_id': f'parent-{index % 24:02d}', 'operation_kind': kinds[index % len(kinds)], 'operation_key': {'ordinal': index, 'channel': index % 11, 'phase': random.randrange(0, 17)}, 'expected_host_id': host['host_id'], 'state_labels': labels})
    return build_registry('synthetic-slot-regression-v1', {'enumerator': 'deterministic-regression', 'seed': 2118, 'slots': 180}, slot_cores)

def synthetic_entry(slot: dict[str, Any], suffix: str='') -> dict[str, Any]:
    source_sha256 = catalogue.canonical_digest({'slot': slot['slot_id'], 'suffix': suffix})
    return {'slot_id': slot['slot_id'], 'host_id': slot['expected_host_id'], 'fibre_id': f"{slot['expected_host_id']}:{source_sha256[:16]}", 'source_sha256': source_sha256}

def run_regressions() -> dict[str, Any]:
    registry = synthetic_registry()
    validate_registry(registry)
    require(registry['registry_sha256'] == EXPECTED_SYNTHETIC_REGISTRY_SHA256 or EXPECTED_SYNTHETIC_REGISTRY_SHA256 == 'TO_BE_FILLED', 'synthetic registry digest drift')
    partial_entries = [synthetic_entry(slot) for slot in registry['slots'][:120]]
    partial = validate_population_audit(build_population_audit(registry, partial_entries))
    require((partial['covered'], partial['missing'], partial['complete']) == (120, 60, 0), 'partial population regression mismatch')
    full_entries = [synthetic_entry(slot) for slot in registry['slots']]
    complete = validate_population_audit(build_population_audit(registry, full_entries))
    require((complete['covered'], complete['missing'], complete['complete']) == (180, 0, 1), 'complete population regression mismatch')
    bad_entries = full_entries[:-1]
    unexpected = copy.deepcopy(full_entries[0])
    unexpected['slot_id'] = 'slot-unexpected'
    unexpected['fibre_id'] += '-unexpected'
    bad_entries.append(unexpected)
    duplicate = synthetic_entry(registry['slots'][1], 'duplicate')
    bad_entries.append(duplicate)
    mismatch = copy.deepcopy(full_entries[2])
    mismatch['host_id'] = registry['slots'][3]['expected_host_id']
    bad_entries.append(mismatch)
    bad = validate_population_audit(build_population_audit(registry, bad_entries))
    require((bad['missing'], bad['unexpected'], bad['duplicates'], bad['mismatches'], bad['complete']) == (1, 1, 2, 1, 0), 'population gap regression mismatch')
    return {'registry': registry, 'partial': partial, 'complete': complete, 'bad': bad}

def run_mutation_tests() -> int:
    regressions = run_regressions()
    registry = regressions['registry']
    audit = build_population_audit(registry, [synthetic_entry(slot) for slot in registry['slots'][:3]])
    validate_population_audit(audit)
    mutations: list[dict[str, Any]] = []

    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(audit)
        mutator(candidate)
        mutations.append(candidate)
    add(lambda data: data.update(audit_sha256='0' * 64))
    add(lambda data: data.update(version=2))
    add(lambda data: data['claims'].update(complete=1))
    add(lambda data: data['population_entries'].reverse())
    add(lambda data: data['population_entries'][0].update(host_id='s4-corrupt'))
    add(lambda data: data['population_entries'][0].update(population_record_sha256='0' * 64))
    add(lambda data: data['expected_registry'].update(registry_sha256='0' * 64))
    add(lambda data: data['expected_registry']['slots'].reverse())
    add(lambda data: data['expected_registry']['slots'][0].update(slot_id='slot-corrupt'))
    add(lambda data: data['expected_registry']['claims'].update(slots=999))
    add(lambda data: data['claims']['missing_slot_ids'].pop())
    add(lambda data: data['population_entries'].append(copy.deepcopy(data['population_entries'][0])))
    rejected = 0
    for candidate in mutations:
        try:
            validate_population_audit(candidate)
        except (SlotRegistryError, catalogue.CatalogueError):
            rejected += 1
    require(rejected == len(mutations), 'mutation tests: corrupted slot audit accepted')
    return rejected

def main() -> None:
    if len(sys.argv) == 2:
        with Path(sys.argv[1]).open('r', encoding='utf-8') as handle:
            value = json.load(handle)
        if 'expected_registry' in value:
            summary = validate_population_audit(value)
            print(f"accepted operation slot population audit: {summary['covered']}/{summary['expected']} slots covered")
        else:
            summary = validate_registry(value)
            print(f"accepted operation slot registry: {summary['slots']} slots")
        return
    if len(sys.argv) != 1:
        raise SystemExit('usage: check_prime_power_operation_slot_registry.py [registry-or-audit.json]')
    regressions = run_regressions()
    rejected = run_mutation_tests()
    registry = regressions['registry']
    print(f"verified operation slot registry: {registry['claims']['slots']} independent slots, {registry['claims']['unique_parents']} parents, {registry['claims']['unique_hosts']} hosts, partial coverage {regressions['partial']['covered']}/{regressions['partial']['expected']}, complete coverage {regressions['complete']['covered']}/{regressions['complete']['expected']}, gap regression missing/unexpected/duplicate/mismatch {regressions['bad']['missing']}/{regressions['bad']['unexpected']}/{regressions['bad']['duplicates']}/{regressions['bad']['mismatches']}, registry sha256 {registry['registry_sha256']}, and {rejected} corruptions rejected")
if __name__ == '__main__':
    main()
