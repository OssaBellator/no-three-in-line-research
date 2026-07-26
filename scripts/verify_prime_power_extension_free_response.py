#!/usr/bin/env python3
"""Finite checks for CMR1302--CMR1309."""

from itertools import permutations
import random


def matching(permutation):
    return frozenset((row, permutation[row]) for row in range(len(permutation)))


def check_union_identity():
    rng = random.Random(1303)
    checked = 0
    response_states = 0
    canonical_extensions = 0
    for side in range(3, 7):
        matchings = [matching(permutation) for permutation in permutations(range(side))]
        complete = {(row, column) for row in range(side) for column in range(side)}
        opposite_indices = list(range(len(matchings)))
        if side == 6:
            opposite_indices = rng.sample(opposite_indices, 10)
        for opposite_index in opposite_indices:
            opposite = matchings[opposite_index]
            candidate_edges = list(complete - set(opposite))
            if side == 6:
                candidate_edges = rng.sample(candidate_edges, 8)
            for edge in candidate_edges:
                extensions = [
                    extension
                    for extension in matchings
                    if edge in extension and extension.isdisjoint(opposite)
                ]
                assert extensions
                union = set()
                for extension in extensions:
                    union.update(
                        response
                        for response in matchings
                        if response.isdisjoint(opposite | extension)
                    )
                direct = {
                    response
                    for response in matchings
                    if response.isdisjoint(opposite) and edge not in response
                }
                assert union == direct
                for response in direct:
                    complement = complete - set(opposite) - set(response)
                    containing = [
                        extension
                        for extension in matchings
                        if edge in extension and extension <= complement
                    ]
                    assert containing
                    canonical = min(containing, key=lambda state: tuple(sorted(state)))
                    assert canonical.isdisjoint(opposite | response)
                    canonical_extensions += 1
                response_states += len(direct)
                checked += 1
    return checked, response_states, canonical_extensions


def check_minimum_equivalence():
    rng = random.Random(1305)
    checked = 0
    for side in range(3, 7):
        matchings = [matching(permutation) for permutation in permutations(range(side))]
        complete = {(row, column) for row in range(side) for column in range(side)}
        opposite_indices = list(range(len(matchings)))
        if side == 6:
            opposite_indices = rng.sample(opposite_indices, 6)
        values = {state: rng.randint(0, 1000) for state in matchings}
        for opposite_index in opposite_indices:
            opposite = matchings[opposite_index]
            edges = list(complete - set(opposite))
            if side == 6:
                edges = rng.sample(edges, 5)
            for edge in edges:
                direct = [
                    response
                    for response in matchings
                    if response.isdisjoint(opposite) and edge not in response
                ]
                via_extensions = []
                for extension in matchings:
                    if edge not in extension or not extension.isdisjoint(opposite):
                        continue
                    via_extensions.extend(
                        response
                        for response in matchings
                        if response.isdisjoint(opposite | extension)
                    )
                assert min(values[state] for state in direct) == min(
                    values[state] for state in via_extensions
                )
                checked += 1
    return checked


def check_regular_edge_factorization():
    rng = random.Random(1302)
    checked = 0
    for side in range(3, 7):
        matchings = [matching(permutation) for permutation in permutations(range(side))]
        complete = {(row, column) for row in range(side) for column in range(side)}
        for _ in range(120):
            first = rng.choice(matchings)
            second = rng.choice([state for state in matchings if state.isdisjoint(first)])
            residual = complete - set(first) - set(second)
            for edge in rng.sample(tuple(residual), min(10, len(residual))):
                assert any(edge in state and state <= residual for state in matchings)
                checked += 1
    return checked


def check_scope_separation():
    checked = 0
    for side in range(3, 1000):
        complete_edge_count = side * side
        one_bank_forbidden = 2 * side
        extension_free_forbidden = side + 1
        assert complete_edge_count - extension_free_forbidden >= complete_edge_count - one_bank_forbidden
        checked += 1
    return checked


def main():
    union = check_union_identity()
    print(
        "verified extension-free responses:",
        union[0],
        "union identities over",
        union[1],
        "response states and",
        union[2],
        "canonical extensions,",
        check_minimum_equivalence(),
        "minimum equivalences,",
        check_regular_edge_factorization(),
        "regular edge-factor cases, and",
        check_scope_separation(),
        "scope checks",
    )


if __name__ == "__main__":
    main()
