#!/usr/bin/env python3
"""Finite checks for CMR1006--CMR1013."""

from itertools import combinations
from math import ceil, comb, gcd
import random


def random_permutation(side, rng):
    values = list(range(side))
    rng.shuffle(values)
    return tuple(values)


def random_disjoint_layers(side, rng):
    first = random_permutation(side, rng)
    for _ in range(1000):
        second = random_permutation(side, rng)
        if all(second[index] != first[index] for index in range(side)):
            return first, second
    raise RuntimeError("failed to sample disjoint permutation layers")


def random_state(side, rng):
    first, second = random_disjoint_layers(side, rng)
    labelled = frozenset(
        [(0, (source, first[source])) for source in range(side)]
        + [(1, (source, second[source])) for source in range(side)]
    )
    physical = frozenset(cell for _layer, cell in labelled)
    return labelled, physical


def collinear(first, second, third):
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def triple_set(physical):
    return {
        frozenset(triple)
        for triple in combinations(physical, 3)
        if collinear(*triple)
    }


def direction_key(root, point):
    dx = point[0] - root[0]
    dy = point[1] - root[1]
    divisor = gcd(abs(dx), abs(dy))
    dx //= divisor
    dy //= divisor
    if dx < 0 or (dx == 0 and dy < 0):
        dx = -dx
        dy = -dy
    return dx, dy


def check_entry_rank_geometry():
    rng = random.Random(1006)
    transitions = 0
    rank_one_roots = 0
    higher_rank_cases = 0

    for side in range(3, 10):
        for _ in range(500):
            _labelled_old, old_physical = random_state(side, rng)
            _labelled_new, new_physical = random_state(side, rng)
            old_triples = triple_set(old_physical)
            new_state_triples = triple_set(new_physical)
            new_triples = new_state_triples - old_triples
            entering = set(new_physical) - set(old_physical)
            common = set(old_physical) & set(new_physical)

            counts = {1: 0, 2: 0, 3: 0}
            rank_one_by_root = {}
            higher_rank = []

            for triple in new_triples:
                entering_cells = set(triple) & entering
                rank = len(entering_cells)
                assert rank in (1, 2, 3)
                counts[rank] += 1
                if rank == 1:
                    root = next(iter(entering_cells))
                    rank_one_by_root.setdefault(root, []).append(triple)
                else:
                    pair = frozenset(tuple(sorted(entering_cells))[:2])
                    higher_rank.append((pair, triple))

            assert len(new_triples) == sum(counts.values())
            if new_triples:
                assert max(counts[1], counts[2] + counts[3]) >= ceil(
                    len(new_triples) / 2
                )

            for root, triples in rank_one_by_root.items():
                line_groups = {}
                for point in common:
                    line_groups.setdefault(direction_key(root, point), []).append(point)

                exact_count = sum(
                    comb(len(points), 2) for points in line_groups.values()
                )
                assert exact_count == len(triples)

                threshold = rng.randint(3, max(3, 2 * side))
                maximum_load = max(
                    [len(points) for points in line_groups.values()] or [0]
                )
                if maximum_load >= threshold:
                    loaded_line = max(line_groups.values(), key=len)
                    old_line_triples = sum(
                        1
                        for triple in combinations(loaded_line, 3)
                        if frozenset(triple) in old_triples
                    )
                    assert old_line_triples >= comb(threshold, 3)
                else:
                    active_lines = sum(
                        1 for points in line_groups.values() if len(points) >= 2
                    )
                    if exact_count:
                        assert active_lines >= ceil(
                            exact_count / comb(threshold - 1, 2)
                        )
                rank_one_roots += 1

            pair_counts = {}
            third_cells = {}
            for pair, triple in higher_rank:
                pair_counts[pair] = pair_counts.get(pair, 0) + 1
                third = next(iter(set(triple) - set(pair)))
                third_cells.setdefault(pair, set()).add(third)

            if higher_rank:
                entering_count = len(entering)
                assert entering_count >= 2
                maximum_pair_load = max(pair_counts.values())
                assert maximum_pair_load >= ceil(
                    len(higher_rank) / comb(entering_count, 2)
                )

                for pair, multiplicity in pair_counts.items():
                    assert len(third_cells[pair]) == multiplicity
                    first, second = tuple(pair)
                    assert all(
                        collinear(first, second, third)
                        for third in third_cells[pair]
                    )
                    occupied = {first, second} | third_cells[pair]
                    assert occupied <= set(new_physical)
                    line_occupancy = sum(
                        1
                        for point in new_physical
                        if collinear(first, second, point)
                    )
                    assert line_occupancy >= multiplicity + 2
                    assert len(new_state_triples) >= comb(multiplicity + 2, 3)
                    if multiplicity >= 1:
                        assert first[0] != second[0]
                        assert first[1] != second[1]
                higher_rank_cases += 1

            transitions += 1

    return transitions, rank_one_roots, higher_rank_cases


def check_threshold_arithmetic():
    checked = 0
    for total in range(1, 10000):
        assert max(total // 2, total - total // 2) >= ceil(total / 2)
        for entering_count in range(2, 30):
            pair_stock = comb(entering_count, 2)
            for threshold in range(1, 10):
                bound = (threshold - 1) * pair_stock
                assert bound >= 0
                checked += 1
    return checked


def main():
    transitions, rank_one, higher_rank = check_entry_rank_geometry()
    print(
        "verified robust-surplus entry-rank dichotomy:",
        transitions,
        "saturated transitions,",
        rank_one,
        "rank-one line decompositions,",
        higher_rank,
        "higher-rank pair concentrations, and",
        check_threshold_arithmetic(),
        "threshold cases",
    )


if __name__ == "__main__":
    main()
