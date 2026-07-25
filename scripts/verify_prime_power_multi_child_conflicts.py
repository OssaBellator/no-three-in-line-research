#!/usr/bin/env python3
"""Finite checks for CMR664--CMR670.

The structural assertions do not use special arithmetic beyond compatibility,
so the checker treats every compatible three-edge set as a candidate atom.  It
exhausts all matchable child hosts of side one or two in the listed products.
"""

from itertools import combinations, permutations, product
from collections import defaultdict


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
        pms = perfect_matchings(n, edges)
        if pms:
            answer.append((edges, pms))
    return answer


def global_edges(sizes, hosts):
    answer = []
    offset = 0
    for factor, (side, edges) in enumerate(zip(sizes, hosts)):
        for i, j in edges:
            answer.append((offset + i, offset + j, factor, (i, j)))
        offset += side
    return answer


def compatible(triple):
    return (
        len({edge[0] for edge in triple}) == 3
        and len({edge[1] for edge in triple}) == 3
    )


def essential_edges(matchings):
    result = set(matchings[0])
    for matching in matchings[1:]:
        result.intersection_update(matching)
    return result


def main():
    hosts = {1: all_matchable_hosts(1), 2: all_matchable_hosts(2)}
    active_atoms = 0
    forced_atoms = 0
    deletable_atoms = 0

    products = ([2, 1], [2, 1, 1], [2, 2], [1, 1, 1])
    for sizes in products:
        for choices in product(*(hosts[side] for side in sizes)):
            factor_edges = [set(choice[0]) for choice in choices]
            factor_matchings = [choice[1] for choice in choices]
            edges = global_edges(sizes, factor_edges)
            total_side = sum(sizes)

            for atom in combinations(edges, 3):
                if not compatible(atom):
                    continue
                support = {edge[2] for edge in atom}
                if len(support) < 2:
                    continue

                ranks = sorted(
                    (sum(edge[2] == factor for edge in atom) for factor in support),
                    reverse=True,
                )
                assert ranks in ([2, 1], [1, 1, 1])

                local_occurrence = []
                is_active = True
                for factor, matchings in enumerate(factor_matchings):
                    prescription = {
                        edge[3] for edge in atom if edge[2] == factor
                    }
                    indices = {
                        index
                        for index, matching in enumerate(matchings)
                        if prescription.issubset(matching)
                    }
                    local_occurrence.append(indices)
                    if prescription and not indices:
                        is_active = False

                # CMR666: exact box occurrence.
                offsets = []
                offset = 0
                for side in sizes:
                    offsets.append(offset)
                    offset += side
                for index_tuple in product(
                    *(range(len(matchings)) for matchings in factor_matchings)
                ):
                    state = set()
                    for factor, matching_index in enumerate(index_tuple):
                        for i, j in factor_matchings[factor][matching_index]:
                            state.add(
                                (
                                    offsets[factor] + i,
                                    offsets[factor] + j,
                                    factor,
                                    (i, j),
                                )
                            )
                    occurs = set(atom).issubset(state)
                    in_box = all(
                        matching_index in local_occurrence[factor]
                        for factor, matching_index in enumerate(index_tuple)
                    )
                    assert occurs == in_box

                if not is_active:
                    continue
                active_atoms += 1

                # CMR667 relative to every distinguished child.
                for distinguished, distinguished_side in enumerate(sizes):
                    outside_side = total_side - distinguished_side
                    assert any(edge[2] != distinguished for edge in atom)
                    outside_stock = sum(
                        len(factor_edges[factor])
                        for factor in range(len(sizes))
                        if factor != distinguished
                    )
                    assert outside_stock <= outside_side * outside_side

                essential = [
                    essential_edges(matchings) for matchings in factor_matchings
                ]
                if all(edge[3] in essential[edge[2]] for edge in atom):
                    forced_atoms += 1
                    for index_tuple in product(
                        *(range(len(matchings)) for matchings in factor_matchings)
                    ):
                        assert all(
                            edge[3]
                            in factor_matchings[edge[2]][index_tuple[edge[2]]]
                            for edge in atom
                        )
                else:
                    deletable_atoms += 1
                    edge = next(
                        edge
                        for edge in atom
                        if edge[3] not in essential[edge[2]]
                    )
                    factor = edge[2]
                    reduced = factor_edges[factor] - {edge[3]}
                    reduced_matchings = perfect_matchings(sizes[factor], reduced)
                    assert reduced_matchings
                    prescription = {
                        item[3] for item in atom if item[2] == factor
                    }
                    assert not any(
                        prescription.issubset(matching)
                        for matching in reduced_matchings
                    )

    assert active_atoms == forced_atoms + deletable_atoms
    print(
        "verified multi-child boxes:",
        active_atoms,
        "active atoms,",
        forced_atoms,
        "forced,",
        deletable_atoms,
        "deletable",
    )


if __name__ == "__main__":
    main()
