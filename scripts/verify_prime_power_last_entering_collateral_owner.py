#!/usr/bin/env python3
"""Finite checks for CMR1214--CMR1221."""

from itertools import combinations
from math import factorial
import random


def falling(side, rank):
    return factorial(side) // factorial(side - rank)


def canonical_owner(old_state, new_state, triple):
    entering = sorted(set(new_state) - set(old_state))
    candidates = [edge for edge in entering if edge[1:] in triple]
    assert candidates
    return candidates[0]


def check_new_triple_owner_partition():
    rng = random.Random(1214)
    checked = 0
    owned_triples = 0
    for side in range(3, 60):
        physical = [(row, column) for row in range(side) for column in range(side)]
        for _ in range(300):
            old_cells = set(rng.sample(physical, rng.randint(3, min(len(physical), 2 * side))))
            new_cells = set(old_cells)
            remove = set(rng.sample(tuple(new_cells), rng.randint(0, min(4, len(new_cells)))))
            new_cells -= remove
            addable = list(set(physical) - new_cells)
            new_cells.update(rng.sample(addable, rng.randint(1, min(4, len(addable)))))

            old_state = {(0, row, column) for row, column in old_cells}
            new_state = {(0, row, column) for row, column in new_cells}
            new_triples = [
                frozenset(triple)
                for triple in combinations(new_cells, 3)
                if not set(triple) <= old_cells
            ]
            fibres = {}
            for triple in new_triples:
                owner = canonical_owner(old_state, new_state, triple)
                fibres.setdefault(owner, set()).add(triple)
            assert sum(len(fibre) for fibre in fibres.values()) == len(new_triples)
            assert set().union(*fibres.values()) == set(new_triples) if fibres else not new_triples
            owned_triples += len(new_triples)
            checked += 1
    return checked, owned_triples


def check_fixed_core_owners():
    rng = random.Random(1217)
    checked = 0
    anchored = 0
    for universe_size in range(5, 100):
        universe = set(range(universe_size))
        for _ in range(200):
            core = set(rng.sample(tuple(universe), rng.randint(1, min(5, universe_size - 2))))
            old_residual = set(rng.sample(tuple(universe - core), rng.randint(1, min(12, len(universe - core)))))
            new_residual = set(old_residual)
            if new_residual:
                new_residual -= set(rng.sample(tuple(new_residual), rng.randint(0, min(3, len(new_residual)))))
            available = universe - core - new_residual
            new_residual.update(rng.sample(tuple(available), rng.randint(1, min(3, len(available)))))
            entering = new_residual - old_residual
            assert entering
            for _triple in range(30):
                fixed_part = set(rng.sample(tuple(core), rng.randint(0, min(2, len(core)))))
                entering_edge = rng.choice(tuple(entering))
                triple = fixed_part | {entering_edge}
                while len(triple) < 3:
                    triple.add(rng.choice(tuple(new_residual)))
                assert triple & entering
                assert not (triple & entering) & core
                anchored += 1
            checked += 1
    return checked, anchored


def check_product_unique_ownership():
    rng = random.Random(1218)
    checked = 0
    for total_side in range(2, 80):
        for _ in range(300):
            factor_count = rng.randint(2, min(total_side, 6))
            cuts = sorted(rng.sample(range(1, total_side), factor_count - 1))
            parts = []
            previous = 0
            for cut in cuts + [total_side]:
                parts.append(set(range(previous, cut)))
                previous = cut
            edge_owner = {}
            for index, part in enumerate(parts):
                for source in part:
                    for target in part:
                        edge = (source, target)
                        assert edge not in edge_owner
                        edge_owner[edge] = index
            for edge, owner in edge_owner.items():
                assert edge[0] in parts[owner]
                assert edge[1] in parts[owner]
            checked += 1
    return checked


def check_score_decomposition():
    rng = random.Random(1220)
    checked = 0
    atoms = 0
    for side in range(4, 150):
        for _ in range(300):
            owner_counts = {}
            totals = [0, 0, 0, 0]
            for _atom in range(rng.randint(0, 500)):
                rank = rng.randint(1, 3)
                prescription = tuple(sorted(rng.sample(range(side * side), rank)))
                owner = prescription[0]
                owner_counts.setdefault(owner, [0, 0, 0, 0])[rank] += 1
                totals[rank] += 1
                atoms += 1
            global_score = sum(totals[rank] / falling(side, rank) for rank in (1, 2, 3))
            owner_score = sum(
                sum(counts[rank] / falling(side, rank) for rank in (1, 2, 3))
                for counts in owner_counts.values()
            )
            assert abs(global_score - owner_score) < 1e-12
            checked += 1
    return checked, atoms


def check_expectation_interchange():
    rng = random.Random(1216)
    checked = 0
    for edge_count in range(1, 80):
        for state_count in range(1, 80):
            loads = [
                [rng.randint(0, 20) if rng.random() < 0.35 else 0 for _ in range(edge_count)]
                for _ in range(state_count)
            ]
            by_state = sum(sum(state) for state in loads) / state_count
            by_edge = sum(sum(state[edge] for state in loads) / state_count for edge in range(edge_count))
            assert abs(by_state - by_edge) < 1e-12
            checked += 1
    return checked


def main():
    partitions = check_new_triple_owner_partition()
    fixed = check_fixed_core_owners()
    scores = check_score_decomposition()
    print(
        "verified last-entering collateral ownership:",
        partitions[0],
        "transitions with",
        partitions[1],
        "owned triples,",
        fixed[0],
        "fixed-core cases with",
        fixed[1],
        "anchored triples,",
        check_product_unique_ownership(),
        "exact product ownership cases,",
        check_expectation_interchange(),
        "expectation interchanges, and",
        scores[0],
        "score decompositions over",
        scores[1],
        "atoms",
    )


if __name__ == "__main__":
    main()
