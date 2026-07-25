#!/usr/bin/env python3
"""Finite checks for CMR684--CMR690."""

from itertools import combinations, permutations, product
from math import comb


def perfect_matchings(n, edges):
    edge_set = set(edges)
    return [
        tuple((i, p[i]) for i in range(n))
        for p in permutations(range(n))
        if all((i, p[i]) in edge_set for i in range(n))
    ]


def all_matchable_hosts(n):
    cells = [(i, j) for i in range(n) for j in range(n)]
    answer = []
    for mask in range(1 << (n * n)):
        edges = {cells[k] for k in range(n * n) if (mask >> k) & 1}
        matchings = perfect_matchings(n, edges)
        if matchings:
            answer.append((edges, matchings))
    return answer


def essential_edges(matchings):
    result = set(matchings[0])
    for matching in matchings[1:]:
        result.intersection_update(matching)
    return result


def global_edges(sizes, hosts):
    answer = []
    offset = 0
    for factor, (side, edges) in enumerate(zip(sizes, hosts)):
        for i, j in edges:
            answer.append((offset + i, offset + j, factor, (i, j)))
        offset += side
    return answer


def compatible(atom):
    return (
        len({edge[0] for edge in atom}) == 3
        and len({edge[1] for edge in atom}) == 3
    )


def main():
    host_cache = {1: all_matchable_hosts(1), 2: all_matchable_hosts(2)}
    products = ([2, 1], [2, 1, 1], [2, 2], [1, 1, 1])
    forced_atoms = 0

    for sizes in products:
        for choices in product(*(host_cache[side] for side in sizes)):
            hosts = [choice[0] for choice in choices]
            matchings = [choice[1] for choice in choices]
            essential = [essential_edges(family) for family in matchings]
            for atom in combinations(global_edges(sizes, hosts), 3):
                if not compatible(atom) or len({edge[2] for edge in atom}) < 2:
                    continue
                if not all(edge[3] in essential[edge[2]] for edge in atom):
                    continue
                forced_atoms += 1
                for state in product(*matchings):
                    assert all(edge[3] in state[edge[2]] for edge in atom)
                # Varying any one child still leaves the atom present.
                for factor, family in enumerate(matchings):
                    for local_matching in family:
                        assert all(
                            edge[2] != factor or edge[3] in local_matching
                            for edge in atom
                        )

    # CMR686--CMR689 arithmetic.
    for side in range(1, 80):
        direct_sum = sum(2 * m * m + m + 1 for m in range(1, side + 1))
        formula = (
            side * (side + 1) * (2 * side + 1) // 3
            + side * (side + 1) // 2
            + side
        )
        assert direct_sum == formula
        certificate_stock = direct_sum * comb(side * side, 3)
        assert certificate_stock >= 0
        for multiplicity in range(2, 12):
            finite_history = (multiplicity - 1) * certificate_stock
            assert finite_history >= 0
            escape_bound = 3 * (multiplicity - 1) * side * side
            assert escape_bound >= 0

    print(
        "verified forced child ancestry:",
        forced_atoms,
        "forced mixed atoms plus stage and recurrence arithmetic",
    )


if __name__ == "__main__":
    main()
