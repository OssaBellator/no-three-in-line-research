#!/usr/bin/env python3
"""Finite checks for CMR677--CMR683.

The checker exhausts all matchable child hosts of side one or two in products of
total side at most four.  Candidate atoms are all compatible three-edge sets;
this is stronger than selecting only the collinear atoms of one geometry.
"""

from itertools import combinations, permutations, product


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
            answer.append(edges)
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


def active_atoms(sizes, hosts, matchings):
    answer = []
    for atom in combinations(global_edges(sizes, hosts), 3):
        if not compatible(atom) or len({edge[2] for edge in atom}) < 2:
            continue
        active = True
        for factor in range(len(sizes)):
            prescription = {
                edge[3] for edge in atom if edge[2] == factor
            }
            if prescription and not any(
                prescription.issubset(matching)
                for matching in matchings[factor]
            ):
                active = False
                break
        if active:
            answer.append(atom)
    return answer


def run_recursion(sizes, initial_hosts):
    hosts = [set(edges) for edges in initial_hosts]
    initial_edge_stock = sum(len(edges) for edges in hosts)
    previous_active = None
    deletions = 0

    while True:
        matchings = [
            perfect_matchings(side, hosts[factor])
            for factor, side in enumerate(sizes)
        ]
        assert all(matchings)
        atoms = active_atoms(sizes, hosts, matchings)
        atom_keys = {tuple(atom) for atom in atoms}
        if previous_active is not None:
            assert atom_keys <= previous_active
        previous_active = atom_keys

        essential = [essential_edges(factor_matchings) for factor_matchings in matchings]
        forced = None
        deletable = None
        for atom in atoms:
            if all(edge[3] in essential[edge[2]] for edge in atom):
                forced = atom
                break
            deletable = atom
            break

        if forced is not None:
            # The forced atom belongs to every product state.
            for matching_tuple in product(*matchings):
                assert all(
                    edge[3] in matching_tuple[edge[2]] for edge in forced
                )
            return deletions, True, len(atoms)

        if deletable is None:
            # No active mixed atom remains; all compatible atoms in states are pure.
            offsets = []
            offset = 0
            for side in sizes:
                offsets.append(offset)
                offset += side
            for matching_tuple in product(*matchings):
                state = []
                for factor, matching in enumerate(matching_tuple):
                    for i, j in matching:
                        state.append(
                            (
                                offsets[factor] + i,
                                offsets[factor] + j,
                                factor,
                                (i, j),
                            )
                        )
                for atom in combinations(state, 3):
                    if compatible(atom):
                        assert len({edge[2] for edge in atom}) == 1
            return deletions, False, 0

        edge = next(
            edge
            for edge in deletable
            if edge[3] not in essential[edge[2]]
        )
        factor = edge[2]
        old_prescription = {
            item[3] for item in deletable if item[2] == factor
        }
        hosts[factor].remove(edge[3])
        reduced_matchings = perfect_matchings(sizes[factor], hosts[factor])
        assert reduced_matchings
        assert not any(
            old_prescription.issubset(matching)
            for matching in reduced_matchings
        )
        deletions += 1
        assert deletions <= initial_edge_stock
        assert deletions <= sum(sizes) ** 2


def main():
    host_cache = {1: all_matchable_hosts(1), 2: all_matchable_hosts(2)}
    products = ([2, 1], [2, 1, 1], [2, 2], [1, 1, 1])
    instances = 0
    forced_terminals = 0
    mixed_clean_terminals = 0
    total_deletions = 0
    maximum_deletions = 0

    for sizes in products:
        assert len(sizes) >= 2
        assert max(sizes) <= sum(sizes) - 1
        for hosts in product(*(host_cache[side] for side in sizes)):
            deletions, forced, remaining = run_recursion(sizes, hosts)
            instances += 1
            total_deletions += deletions
            maximum_deletions = max(maximum_deletions, deletions)
            if forced:
                forced_terminals += 1
                assert remaining >= 1
            else:
                mixed_clean_terminals += 1
                assert remaining == 0

    print(
        "verified mixed-child recursion:",
        instances,
        "products,",
        total_deletions,
        "deletions, max",
        maximum_deletions,
        ", forced",
        forced_terminals,
        ", mixed-clean",
        mixed_clean_terminals,
    )


if __name__ == "__main__":
    main()
