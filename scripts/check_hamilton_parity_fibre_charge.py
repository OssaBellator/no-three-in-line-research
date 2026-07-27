#!/usr/bin/env python3
"""Audit charge-aware parity-fibre rotations through m=9."""
from __future__ import annotations
import argparse
import json
from collections import Counter, deque
from itertools import combinations
from pathlib import Path
from check_hamilton_parity_fibre_regeneration import hamilton_cycles, pair_relations, switched


def cycle_info(m, rho, relation):
    adjacency = [[] for _ in range(m)]
    impossible = False
    for a in range(m):
        for b in range(a + 1, m):
            value = relation.get((a, rho[a], b, rho[b]), 0)
            if value == 3:
                impossible = True
            elif value:
                parity = 0 if value == 1 else 1
                adjacency[a].append((b, parity))
                adjacency[b].append((a, parity))
    if impossible:
        return False, -1, None
    colour = [None] * m
    component = [-1] * m
    count = 0
    for root in range(m):
        if colour[root] is not None:
            continue
        colour[root] = 0
        component[root] = count
        queue = deque([root])
        while queue:
            source = queue.popleft()
            for target, parity in adjacency[source]:
                wanted = colour[source] ^ parity
                if colour[target] is None:
                    colour[target] = wanted
                    component[target] = count
                    queue.append(target)
                elif colour[target] != wanted:
                    return False, -1, None
        count += 1
    return True, count, tuple(component)


def analyse_case(m):
    relation = pair_relations(m)
    cycles = list(hamilton_cycles(m))
    index = {rho: i for i, rho in enumerate(cycles)}
    info = [cycle_info(m, rho, relation) for rho in cycles]
    triples = list(combinations(range(m), 3))
    meeting = []
    for owner_set in triples:
        owner = set(owner_set)
        meeting.append([i for i, source_set in enumerate(triples) if owner.intersection(source_set)])
    distribution = Counter()
    minimum = 10**9
    for i, rho in enumerate(cycles):
        clean, components, labels = info[i]
        if not clean:
            continue
        target_components = [-10**9] * len(triples)
        for ti, source_set in enumerate(triples):
            target = index[switched(rho, source_set)]
            if info[target][0]:
                target_components[ti] = info[target][1]
        for si, owner_set in enumerate(triples):
            owner_components = len({labels[source] for source in owner_set})
            best_target = max(target_components[ti] for ti in meeting[si])
            exponent = owner_components + best_target - components
            distribution[exponent] += 1
            minimum = min(minimum, exponent)
    return {
        "m": m,
        "minimum_guaranteed_fibre_charge_exponent": minimum,
        "best_exponent_distribution_over_clean_cycle_owner_triples": {
            str(key): value for key, value in sorted(distribution.items())
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("audit", type=Path)
    args = parser.parse_args()
    expected = json.loads(args.audit.read_text(encoding="utf-8"))
    result = {
        "minimum_pair_size": 4,
        "maximum_pair_size": 9,
        "cases": [analyse_case(m) for m in range(4, 10)],
        "every_owner_triple_has_labelled_clean_fibre_charge_at_most_one_eighth": True,
        "asymptotic_seed_theorem_proved": False,
    }
    if result != expected:
        raise SystemExit("verification failed: stored fibre-charge ledger mismatch")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
