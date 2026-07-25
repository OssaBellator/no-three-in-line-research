#!/usr/bin/env python3
"""Finite checks for CMR734--CMR740."""

from itertools import combinations, permutations
import random


def edges(permutation):
    return {(index, permutation[index]) for index in range(len(permutation))}


def perfect_matchings(side, host):
    return [
        permutation
        for permutation in permutations(range(side))
        if edges(permutation) <= host
    ]


def hall_witnesses(side, host):
    for size in range(1, side + 1):
        for source_tuple in combinations(range(side), size):
            sources = set(source_tuple)
            targets = {
                target
                for source, target in host
                if source in sources
            }
            if len(targets) < len(sources):
                yield sources, targets


def canonical_minimal_hall(side, host):
    witnesses = list(hall_witnesses(side, host))
    minimal = [
        (sources, targets)
        for sources, targets in witnesses
        if not any(
            other_sources < sources
            for other_sources, _ in witnesses
        )
    ]
    return min(
        minimal,
        key=lambda item: (len(item[0]), tuple(sorted(item[0]))),
    )


def factor_matchings(sources, targets, host):
    sources = sorted(sources)
    targets = sorted(targets)
    if not sources:
        return [frozenset()]
    output = []
    for target_order in permutations(targets):
        matching = frozenset(zip(sources, target_order))
        if matching <= host:
            output.append(matching)
    return output


def common_edges(matchings):
    if not matchings:
        return set()
    return set.intersection(*(set(matching) for matching in matchings))


def check_case(side, host, essential_edge):
    full_permutations = perfect_matchings(side, host)
    full_matchings = {
        frozenset(edges(permutation))
        for permutation in full_permutations
    }
    assert full_matchings
    assert all(
        essential_edge in matching
        for matching in full_matchings
    )

    reduced = set(host)
    reduced.remove(essential_edge)
    sources, targets = canonical_minimal_hall(side, reduced)
    source_endpoint, target_endpoint = essential_edge

    a_sources = sources - {source_endpoint}
    a_targets = targets
    b_sources = set(range(side)) - sources
    b_targets = set(range(side)) - (targets | {target_endpoint})

    factor_a = factor_matchings(a_sources, a_targets, host)
    factor_b = factor_matchings(b_sources, b_targets, host)
    assert factor_a and factor_b

    product_matchings = {
        frozenset({essential_edge}) | matching_a | matching_b
        for matching_a in factor_a
        for matching_b in factor_b
    }
    assert product_matchings == full_matchings
    assert len(full_matchings) == len(factor_a) * len(factor_b)
    assert len(a_sources) + len(b_sources) == side - 1

    factor_a_edges = {
        edge
        for edge in host
        if edge[0] in a_sources and edge[1] in a_targets
    }
    factor_b_edges = {
        edge
        for edge in host
        if edge[0] in b_sources and edge[1] in b_targets
    }
    essential_a = common_edges(factor_a)
    essential_b = common_edges(factor_b)

    for other_edges in combinations(
        sorted(set(host) - {essential_edge}),
        2,
    ):
        target = frozenset((essential_edge,) + other_edges)
        if len({source for source, _ in target}) < 3:
            continue
        if len({right for _, right in target}) < 3:
            continue

        occurrences = [
            matching
            for matching in full_matchings
            if target <= matching
        ]
        if not occurrences:
            continue

        target_a = set(target) & factor_a_edges
        target_b = set(target) & factor_b_edges
        assert len(target_a) + len(target_b) == 2
        assert (len(target_a), len(target_b)) in {
            (2, 0),
            (1, 1),
            (0, 2),
        }

        occurrences_a = [
            matching
            for matching in factor_a
            if target_a <= matching
        ]
        occurrences_b = [
            matching
            for matching in factor_b
            if target_b <= matching
        ]
        assert len(occurrences) == (
            len(occurrences_a) * len(occurrences_b)
        )

        local_target = target_a | target_b
        local_essential = essential_a | essential_b
        if local_target <= local_essential:
            assert len(occurrences) == len(full_matchings)
        else:
            deletable = next(
                edge
                for edge in local_target
                if edge not in local_essential
            )
            if deletable in factor_a_edges:
                assert any(
                    deletable not in matching
                    for matching in factor_a
                )
            else:
                assert any(
                    deletable not in matching
                    for matching in factor_b
                )


def exhaustive_small():
    checked = 0
    for side in range(1, 4):
        universe = [
            (source, target)
            for source in range(side)
            for target in range(side)
        ]
        for mask in range(1 << len(universe)):
            host = {
                universe[index]
                for index in range(len(universe))
                if (mask >> index) & 1
            }
            matchings = perfect_matchings(side, host)
            if not matchings:
                continue
            common = set.intersection(
                *(edges(permutation) for permutation in matchings)
            )
            for essential_edge in common:
                check_case(side, host, essential_edge)
                checked += 1
    return checked


def sampled_side_four():
    rng = random.Random(20260726)
    side = 4
    universe = [
        (source, target)
        for source in range(side)
        for target in range(side)
    ]
    checked = 0
    for _ in range(5000):
        host = {
            edge
            for edge in universe
            if rng.random() < 0.5
        }
        matchings = perfect_matchings(side, host)
        if not matchings:
            continue
        common = set.intersection(
            *(edges(permutation) for permutation in matchings)
        )
        if not common:
            continue
        essential_edge = rng.choice(list(common))
        check_case(side, host, essential_edge)
        checked += 1
    return checked


def main():
    exhaustive = exhaustive_small()
    sampled = sampled_side_four()
    print(
        "verified unit Hall wall factorization:",
        exhaustive,
        "exhaustive essential-edge cases and",
        sampled,
        "sampled side-four cases",
    )


if __name__ == "__main__":
    main()
