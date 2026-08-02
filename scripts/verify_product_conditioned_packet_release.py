#!/usr/bin/env python3
"""Verify PX213--PX214 conditioned common-product packet release."""
from __future__ import annotations

from itertools import combinations, permutations
from math import exp, factorial
from random import Random


def has_two_cycle(permutation: tuple[int, ...]) -> bool:
    return any(
        permutation[first] == second and permutation[second] == first
        for first, second in combinations(range(len(permutation)), 2)
    )


def released_permutations(
    forbidden: tuple[int, ...],
) -> tuple[tuple[int, ...], ...]:
    size = len(forbidden)
    return tuple(
        permutation
        for permutation in permutations(range(size))
        if not has_two_cycle(permutation)
        and all(
            not forbidden[row] & (1 << permutation[row])
            for row in range(size)
        )
    )


def union_of_permutations(
    size: int, degree: int, random: Random
) -> tuple[int, ...]:
    masks = [0] * size
    for _ in range(degree):
        permutation = list(range(size))
        random.shuffle(permutation)
        for row, column in enumerate(permutation):
            masks[row] |= 1 << column
    return tuple(masks)


def contains_partial(
    permutation: tuple[int, ...],
    partial: tuple[tuple[int, int], ...],
) -> bool:
    return all(permutation[row] == column for row, column in partial)


def falling_factorial(size: int, rank: int) -> int:
    return factorial(size) // factorial(size - rank)


def reverse_positions(
    size: int,
    partial: tuple[tuple[int, int], ...],
) -> tuple[tuple[int, int], ...]:
    used_rows = {row for row, _ in partial}
    used_columns = {column for _, column in partial}
    return tuple(
        (column, row)
        for row, column in partial
        if row != column
        and column not in used_rows
        and row not in used_columns
    )


def verify_reverse_matching() -> None:
    random = Random(213)
    for size in range(5, 13):
        for rank in range(1, min(4, size)):
            for _ in range(100):
                rows = random.sample(range(size), rank)
                columns = random.sample(range(size), rank)
                partial = tuple(zip(rows, columns))
                reverse = reverse_positions(size, partial)
                assert len({row for row, _ in reverse}) == len(reverse)
                assert len({column for _, column in reverse}) == len(reverse)
    print("conditioning reverse positions form one partial matching")


def verify_conditional_cylinders() -> None:
    random = Random(214)
    for size in range(6, 9):
        for degree in (1, 2):
            for _ in range(8):
                forbidden = union_of_permutations(size, degree, random)
                family = released_permutations(forbidden)
                assert family
                model = random.choice(family)
                for exposed_rank in range(0, min(3, size - 1)):
                    exposed = tuple(
                        (row, model[row]) for row in range(exposed_rank)
                    )
                    conditioned = tuple(
                        permutation
                        for permutation in family
                        if contains_partial(permutation, exposed)
                    )
                    assert conditioned
                    residual_order = size - exposed_rank

                    lower_extensions = (
                        exp(-4 * degree - 8) * factorial(residual_order)
                    )
                    if lower_extensions <= 1:
                        assert len(conditioned) >= lower_extensions

                    if residual_order >= 2:
                        row = exposed_rank
                        extension = ((row, model[row]),)
                        probability = sum(
                            contains_partial(permutation, extension)
                            for permutation in conditioned
                        ) / len(conditioned)
                        upper = exp(4 * degree + 8) / residual_order
                        assert probability <= upper
            print(
                f"h={size}, Delta={degree}: "
                "conditional release cylinders verified"
            )


def verify_conditioned_lll_budget() -> None:
    for degree in range(1, 21):
        residual_degree = degree + 1
        for order in (
            max(32, 32 * residual_degree),
            48 * residual_degree,
            64 * residual_degree,
        ):
            singleton_witness = 2 / order
            cycle_witness = 4 / order**2
            assert (
                singleton_witness
                * (1 - singleton_witness) ** (2 * residual_degree)
                * (1 - cycle_witness) ** (2 * order)
                >= 1 / order
            )
            assert (
                cycle_witness
                * (1 - singleton_witness) ** (4 * residual_degree)
                * (1 - cycle_witness) ** (2 * order)
                >= 1 / (order * (order - 1))
            )
            density = (
                (1 - singleton_witness) ** (residual_degree * order)
                * (1 - cycle_witness) ** (order * (order - 1) // 2)
            )
            assert density >= exp(-4 * degree - 8)
    print("conditioned packet-release LLL budget verified")


def verify_weighted_load_transfer() -> None:
    random = Random(215)
    size = 8
    degree = 1
    forbidden = union_of_permutations(size, degree, random)
    family = released_permutations(forbidden)
    assert family

    for first, second in combinations(range(size), 2):
        event = ((first, second), (second, first))
        assert not any(
            contains_partial(permutation, event)
            for permutation in family
        )

    for rank in (1, 2, 3):
        partials = []
        for rows in combinations(range(size), rank):
            for columns in combinations(range(size), rank):
                for image in permutations(columns):
                    partial = tuple(zip(rows, image))
                    if any(
                        partial[first]
                        == (partial[second][1], partial[second][0])
                        for first in range(rank)
                        for second in range(first + 1, rank)
                    ):
                        continue
                    partials.append((partial, 1 + random.randrange(5)))
                    if len(partials) >= 80:
                        break
                if len(partials) >= 80:
                    break
            if len(partials) >= 80:
                break

        exact = sum(
            weight
            * sum(
                contains_partial(permutation, partial)
                for permutation in family
            )
            / len(family)
            for partial, weight in partials
        )
        total_weight = sum(weight for _, weight in partials)
        bound = (
            exp(4 * degree + 4)
            * total_weight
            / falling_factorial(size, rank)
        )
        assert exact <= bound
    print("released-bank weighted load transfer verified")


def main() -> None:
    verify_reverse_matching()
    verify_conditional_cylinders()
    verify_conditioned_lll_budget()
    verify_weighted_load_transfer()
    print("PX213--PX214 verified")


if __name__ == "__main__":
    main()
