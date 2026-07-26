#!/usr/bin/env python3
"""Finite checks for CMR1302--CMR1309."""

from itertools import permutations
import random


def matching(permutation):
    return frozenset((row, permutation[row]) for row in range(len(permutation)))


def perfect_matchings(side, allowed):
    allowed = set(allowed)
    return {
        matching(permutation)
        for permutation in permutations(range(side))
        if matching(permutation) <= allowed
    }


def check_union_identity():
    rng = random.Random(1303)
    checked = 0
    response_states = 0
    canonical_extensions = 0
    for side in range(3, 8):
        permutations_list = list(permutations(range(side)))
        matchings = [matching(permutation) for permutation in permutations_list]
        complete = {(row, column) for row in range(side) for column in range(side)}
        opposite_indices = range(len(matchings))
        if side >= 6:
            opposite_indices = rng.sample(list(opposite_indices), min(30, len(matchings)))
        for opposite_index in opposite_indices:
            opposite = matchings[opposite_index]
            candidate_edges = list(complete - set(opposite))
            if side >= 6:
                candidate_edges = rng.sample(candidate_edges, min(15, len(candidate_edges)))
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
                    assert edge in canonical
                    assert canonical.isdisjoint(opposite | response)
                    canonical_extensions += 1
                response_states += len(direct)
                checked += 1
    return checked, response_states, canonical_extensions


def check_minimum_equivalence():
    rng = random.Random(1305)
    checked = 0
    for side in range(3, 8):
        permutations_list = list(permutations(range(side)))
        matchings = [matching(permutation) for permutation in permutations_list]
        complete = {(row, column) for row in range(side) for column in range(side)}
        opposite_indices = list(range(len(matchings)))
        if side >= 6:
            opposite_indices = rng.sample(opposite_indices, min(25, len(opposite_indices)))
        values = {state: rng.randint(0, 1000) for state in matchings}
        for opposite_index in opposite_indices:
            opposite = matchings[opposite_index]
            edges = list(complete - set(opposite))
            if side >= 6:
                edges = rng.sample(edges, min(15, len(edges)))
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
    for side in range(3, 9):
        permutations_list = list(permutations(range(side)))
        matchings = [matching(permutation) for permutation in permutations_list]
        pairs = []
        for _ in range(300):
            first = rng.choice(matchings)
            disjoint = [state for state in matchings if state.isdisjoint(first)]
            second = rng.choice(disjoint)
            pairs.append((first, second))
        complete = {(row, column) for row in range(side) for column in range(side)}
        for first, second in pairs:
            residual = complete - set(first) - set(second)
            for edge in rng.sample(tuple(residual), min(15, len(residual))):
                assert any(edge in state and state <= residual for state in matchings)
                checked += 1
    return checked


def check_scope_separation():
    checked = 0
    for side in range(3, 9):
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
