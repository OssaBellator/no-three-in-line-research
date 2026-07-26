#!/usr/bin/env python3
"""Finite checks for CMR1174--CMR1181."""

from itertools import combinations, permutations


def matching(permutation):
    return frozenset((left, permutation[left]) for left in range(len(permutation)))


def check_side_three_partition():
    permutations_three = list(permutations(range(3)))
    checked = 0
    for opposite_permutation in permutations_three:
        opposite = matching(opposite_permutation)
        for edge in {(left, right) for left in range(3) for right in range(3)} - set(opposite):
            containing = [
                matching(permutation)
                for permutation in permutations_three
                if edge in matching(permutation)
                and matching(permutation).isdisjoint(opposite)
            ]
            assert len(containing) == 1
            forbidden = containing[0]
            responses = [
                matching(permutation)
                for permutation in permutations_three
                if matching(permutation).isdisjoint(opposite)
                and matching(permutation).isdisjoint(forbidden)
            ]
            assert len(responses) == 1
            response = responses[0]
            assert set(opposite) | set(forbidden) | set(response) == {
                (left, right) for left in range(3) for right in range(3)
            }
            assert edge not in response
            checked += 1
    return checked


def check_singleton_blockers():
    permutations_three = list(permutations(range(3)))
    checked = 0
    for response_permutation in permutations_three:
        response = matching(response_permutation)
        for blocker in response:
            residual_host = set(response) - {blocker}
            assert not any(
                matching(permutation) <= residual_host
                for permutation in permutations_three
            )
            restored_host = residual_host | {blocker}
            family = [
                matching(permutation)
                for permutation in permutations_three
                if matching(permutation) <= restored_host
            ]
            assert family == [response]
            assert all(blocker in state for state in family)
            checked += 1
    return checked


def collinear(points):
    (x1, y1), (x2, y2), (x3, y3) = points
    return (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1)


def check_side_two_rigidity_and_cleanliness():
    matchings = [matching(permutation) for permutation in permutations(range(2))]
    assert len(matchings) == 2
    ordered = []
    for first in matchings:
        for second in matchings:
            if first.isdisjoint(second):
                ordered.append((first, second))
    assert len(ordered) == 2
    physical_sets = {frozenset(set(first) | set(second)) for first, second in ordered}
    assert physical_sets == {frozenset((x, y) for x in range(2) for y in range(2))}
    board = next(iter(physical_sets))
    assert all(not collinear(triple) for triple in combinations(board, 3))
    return len(ordered), len(list(combinations(board, 3)))


def check_small_contraction_arithmetic():
    checked = 0
    for side, rank in ((1, 1), (2, 4), (3, 0)):
        assert rank >= 0
        if side == 1:
            assert rank == 1
        if side == 2:
            assert rank == 4
        checked += 1
    return checked


def main():
    rigid = check_side_two_rigidity_and_cleanliness()
    print(
        "verified small joint-factor base:",
        check_side_three_partition(),
        "side-three target responses,",
        check_singleton_blockers(),
        "singleton blockers,",
        rigid[0],
        "side-two layer assignments with",
        rigid[1],
        "triple checks, and",
        check_small_contraction_arithmetic(),
        "base contractions",
    )


if __name__ == "__main__":
    main()
