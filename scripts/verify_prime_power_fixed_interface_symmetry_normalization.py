#!/usr/bin/env python3
"""Finite checks for CMR1654--CMR1661."""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations
from random import Random


Edge = tuple[int, int]


def transform_edge(edge: Edge, source: list[int], target: list[int]) -> Edge:
    return source[edge[0]], target[edge[1]]


def transform_set(
    edges: set[Edge], source: list[int], target: list[int]
) -> set[Edge]:
    return {transform_edge(edge, source, target) for edge in edges}


def perfect_matchings(side: int, forbidden: set[Edge]) -> list[tuple[int, ...]]:
    return [
        permutation
        for permutation in permutations(range(side))
        if all((left, permutation[left]) not in forbidden for left in range(side))
    ]


def prescription_probability(
    side: int, forbidden: set[Edge], prescription: set[Edge]
) -> Fraction | None:
    response_matchings = perfect_matchings(side, forbidden)
    if not response_matchings:
        return None
    numerator = sum(
        all(permutation[left] == right for left, right in prescription)
        for permutation in response_matchings
    )
    return Fraction(numerator, len(response_matchings))


def random_partial_matching(random: Random, edges: set[Edge]) -> set[Edge]:
    chosen: set[Edge] = set()
    used_left: set[int] = set()
    used_right: set[int] = set()
    edge_list = list(edges)
    random.shuffle(edge_list)
    for edge in edge_list:
        left, right = edge
        if (
            random.random() < 0.3
            and left not in used_left
            and right not in used_right
        ):
            chosen.add(edge)
            used_left.add(left)
            used_right.add(right)
    return chosen


def canonical_code(
    side: int, deleted: set[Edge], prescription: set[Edge]
) -> tuple[tuple[Edge, ...], tuple[Edge, ...]]:
    tail = list(range(2, side))
    best: tuple[tuple[Edge, ...], tuple[Edge, ...]] | None = None
    for image in permutations(tail):
        permutation = list(range(side))
        for old, new in zip(tail, image):
            permutation[old] = new
        code = (
            tuple(sorted(transform_set(deleted, permutation, permutation))),
            tuple(sorted(transform_set(prescription, permutation, permutation))),
        )
        if best is None or code < best:
            best = code
    assert best is not None
    return best


def normalize_opposite_target(
    side: int,
    opposite_permutation: list[int],
    target_edge: Edge,
    edges: set[Edge],
) -> tuple[tuple[int, ...], Edge, set[Edge]]:
    inverse = [0] * side
    for left, right in enumerate(opposite_permutation):
        inverse[right] = left

    target_left, target_right = target_edge
    normalized_right = inverse[target_right]
    assert normalized_right != target_left

    simultaneous: list[int | None] = [None] * side
    simultaneous[target_left] = 0
    simultaneous[normalized_right] = 1
    remaining_old = [
        vertex
        for vertex in range(side)
        if vertex not in (target_left, normalized_right)
    ]
    remaining_new = list(range(2, side))
    for old, new in zip(remaining_old, remaining_new):
        simultaneous[old] = new
    final = [int(value) for value in simultaneous]

    def normalize_edge(edge: Edge) -> Edge:
        left, right = edge
        return final[left], final[inverse[right]]

    return (
        tuple(range(side)),
        normalize_edge(target_edge),
        {normalize_edge(edge) for edge in edges},
    )


def main() -> None:
    random = Random(1654)
    systems = 0
    canonical_checks = 0
    probability_checks = 0
    normalization_checks = 0

    for _ in range(3_000):
        side = random.randint(3, 7)
        opposite = {(index, index) for index in range(side)}
        target = (0, 1)
        allowed = {
            (left, right)
            for left in range(side)
            for right in range(side)
        } - opposite - {target}
        deleted = random_partial_matching(random, allowed)
        forbidden = opposite | {target} | deleted
        response_matchings = perfect_matchings(side, forbidden)
        if not response_matchings:
            continue

        chosen_response = random.choice(response_matchings)
        rank = random.choice([1, 2])
        rows = random.sample(range(side), rank)
        prescription = {(left, chosen_response[left]) for left in rows}
        base_probability = prescription_probability(side, forbidden, prescription)
        assert base_probability is not None

        tail = list(range(2, side))
        image = tail[:]
        random.shuffle(image)
        stabilizer = list(range(side))
        for old, new in zip(tail, image):
            stabilizer[old] = new

        transformed_deleted = transform_set(deleted, stabilizer, stabilizer)
        transformed_prescription = transform_set(
            prescription, stabilizer, stabilizer
        )
        transformed_forbidden = (
            opposite | {target} | transformed_deleted
        )

        assert canonical_code(side, deleted, prescription) == canonical_code(
            side, transformed_deleted, transformed_prescription
        )
        assert len(perfect_matchings(side, forbidden)) == len(
            perfect_matchings(side, transformed_forbidden)
        )
        assert (
            prescription_probability(
                side, transformed_forbidden, transformed_prescription
            )
            == base_probability
        )
        canonical_checks += 1
        probability_checks += 1

        opposite_permutation = list(range(side))
        random.shuffle(opposite_permutation)
        target_left = random.randrange(side)
        target_choices = [
            right
            for right in range(side)
            if right != opposite_permutation[target_left]
        ]
        arbitrary_target = (target_left, random.choice(target_choices))
        normalized_opposite, normalized_target, _normalized_edges = (
            normalize_opposite_target(
                side, opposite_permutation, arbitrary_target, deleted
            )
        )
        assert normalized_opposite == tuple(range(side))
        assert normalized_target == (0, 1)
        normalization_checks += 1
        systems += 1

    print(
        "verified symmetry-reduced interface tables: "
        f"{systems} normalized host systems, "
        f"{canonical_checks} stabilizer-canonical checks, "
        f"{probability_checks} exact rook-probability invariances and "
        f"{normalization_checks} opposite-target normalizations"
    )


if __name__ == "__main__":
    main()
