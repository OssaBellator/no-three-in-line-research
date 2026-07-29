#!/usr/bin/env python3
"""Deterministic adequacy audit for the RI logical compatibility schema."""
from math import prod
from random import Random

SYSTEMS = 2500
SEED = 29001
LOGICAL_FIELDS = ('repair_type', 'field_element_data', 'host_context', 'secant_line_address', 'coherence', 'collateral_class', 'epoch')
AUDIT_RADICES = (2, 4, 3, 5)
EXPECTED = {'systems': 2500, 'capacity_obstructions': 2500, 'capacity_feasible': 0, 'omission_witnesses': 2500, 'lossless_separations': 2500, 'packed_samples': 0, 'total_logical_states': 5364330}


def pack_index(index):
    out = []
    for radix in AUDIT_RADICES:
        out.append(index % radix)
        index //= radix
    assert index == 0
    return tuple(out)


def audit():
    rng = Random(SEED)
    out = {k: 0 for k in EXPECTED}
    audit_capacity = prod(AUDIT_RADICES)
    buckets = [[] for _ in AUDIT_RADICES]
    for i in range(len(LOGICAL_FIELDS)):
        buckets[i % len(AUDIT_RADICES)].append(i)

    for _ in range(SYSTEMS):
        domains = [rng.randint(2, 4) for _ in LOGICAL_FIELDS]
        total = prod(domains)
        out['systems'] += 1
        out['total_logical_states'] += total
        out['capacity_obstructions' if total > audit_capacity else 'capacity_feasible'] += 1

        omitted = rng.randrange(len(LOGICAL_FIELDS))
        left = [rng.randrange(d) for d in domains]
        right = left.copy()
        right[omitted] = (right[omitted] + 1) % domains[omitted]
        lossless = lambda record: tuple(tuple(record[i] for i in bucket) for bucket in buckets)
        without = lambda record: tuple(record[i] for i in range(len(record)) if i != omitted)
        assert lossless(left) != lossless(right)
        assert without(left) == without(right)
        out['omission_witnesses'] += 1
        out['lossless_separations'] += 1

        if total <= audit_capacity:
            index = 0
            multiplier = 1
            for value, domain in zip(left, domains):
                index += value * multiplier
                multiplier *= domain
            pack_index(index)
            out['packed_samples'] += 1
    return out


def main():
    got = audit()
    assert got == EXPECTED
    capacity = prod(AUDIT_RADICES)
    binary = 2 ** len(LOGICAL_FIELDS)
    print(f'track=RI logical_blocks={len(LOGICAL_FIELDS)} audit_coordinates=4 audit_capacity={capacity} binary_states={binary} binary_status=obstruction')
    print(f"systems={got['systems']} capacity_obstructions={got['capacity_obstructions']} capacity_feasible={got['capacity_feasible']} omission_witnesses={got['omission_witnesses']} total_logical_states={got['total_logical_states']}")


if __name__ == '__main__':
    main()
