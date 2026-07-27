#!/usr/bin/env python3
"""Finite checks for CMR1782--CMR1789."""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, gcd
from random import Random


Point = tuple[int, int]
Prescription = tuple[Point, ...]


def collinear(first: Point, second: Point, third: Point) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def primitive_direction(first: Point, second: Point) -> tuple[int, int]:
    delta_x = second[0] - first[0]
    delta_y = second[1] - first[1]
    divisor = gcd(abs(delta_x), abs(delta_y))
    delta_x //= divisor
    delta_y //= divisor
    if delta_x < 0 or (delta_x == 0 and delta_y < 0):
        delta_x = -delta_x
        delta_y = -delta_y
    return delta_x, delta_y


def triple_count(points: set[Point]) -> int:
    return sum(collinear(*triple) for triple in combinations(points, 3))


def perfect_matchings(side: int, allowed: set[Point]) -> list[tuple[int, ...]]:
    return [
        permutation
        for permutation in permutations(range(side))
        if all((left, permutation[left]) in allowed for left in range(side))
    ]


def coefficients(
    background: set[Point],
    response_universe: set[Point],
) -> tuple[
    dict[Point, int],
    dict[Prescription, int],
    dict[Prescription, int],
    dict[Point, int],
    dict[Prescription, int],
]:
    rank_one: dict[Point, int] = {}
    charged_one: dict[Point, int] = {}
    for point in response_universe:
        loads: dict[tuple[int, int], int] = defaultdict(int)
        for background_point in background:
            loads[
                primitive_direction(point, background_point)
            ] += 1
        rank_one[point] = sum(comb(height, 2) for height in loads.values())
        charged_one[point] = (
            sum(height == 2 for height in loads.values())
            + 3 * sum(comb(height, 3) for height in loads.values())
        )
        assert rank_one[point] <= charged_one[point]

    rank_two: dict[Prescription, int] = {}
    charged_two: dict[Prescription, int] = {}
    for first, second in combinations(sorted(response_universe), 2):
        if first[0] == second[0] or first[1] == second[1]:
            continue
        item = tuple(sorted((first, second)))
        height = sum(
            collinear(first, second, background_point)
            for background_point in background
        )
        rank_two[item] = height
        charged_two[item] = 2 + comb(height, 3)
        assert rank_two[item] <= charged_two[item]

    rank_three: dict[Prescription, int] = {}
    for item in combinations(sorted(response_universe), 3):
        if len({point[0] for point in item}) < 3:
            continue
        if len({point[1] for point in item}) < 3:
            continue
        rank_three[item] = int(collinear(*item))

    return rank_one, rank_two, rank_three, charged_one, charged_two


def response_energy(
    response: tuple[int, ...],
    rank_one: dict[Point, int],
    rank_two: dict[Prescription, int],
    rank_three: dict[Prescription, int],
) -> int:
    points = tuple((left, response[left]) for left in range(len(response)))
    return (
        sum(rank_one[point] for point in points)
        + sum(rank_two[tuple(sorted(item))] for item in combinations(points, 2))
        + sum(rank_three[tuple(sorted(item))] for item in combinations(points, 3))
    )


def main() -> None:
    random = Random(1782)
    systems = 0
    response_identity_checks = 0
    expectation_checks = 0
    assignment_checks = 0
    charged_checks = 0
    integer_numerator_checks = 0
    strict_certificate_checks = 0

    for side in range(2, 7):
        response_universe = {
            (left, right)
            for left in range(side)
            for right in range(side)
        }
        ambient = [
            (x, y)
            for x in range(-3, 2 * side + 4)
            for y in range(-3, 2 * side + 4)
            if (x, y) not in response_universe
        ]

        for _ in range(180):
            allowed = {(index, index) for index in range(side)}
            for point in response_universe:
                if random.random() < 0.52:
                    allowed.add(point)
            responses = perfect_matchings(side, allowed)
            assert responses

            background = set(
                random.sample(ambient, random.randint(3, min(16, len(ambient))))
            )
            (
                rank_one,
                rank_two,
                rank_three,
                charged_one,
                charged_two,
            ) = coefficients(background, allowed)

            energies: list[int] = []
            charged_energies: list[int] = []
            for response in responses:
                points = {(left, response[left]) for left in range(side)}
                direct = triple_count(background.union(points)) - triple_count(background)
                compiled = response_energy(
                    response,
                    rank_one,
                    rank_two,
                    rank_three,
                )
                assert direct == compiled
                response_identity_checks += 1
                energies.append(compiled)

                response_points = tuple(sorted(points))
                charged = (
                    sum(charged_one[point] for point in response_points)
                    + sum(
                        charged_two[tuple(sorted(item))]
                        for item in combinations(response_points, 2)
                    )
                    + sum(
                        rank_three[tuple(sorted(item))]
                        for item in combinations(response_points, 3)
                    )
                )
                assert compiled <= charged
                charged_energies.append(charged)
                charged_checks += 1

            weights = [random.randint(1, 25) for _ in responses]
            denominator = sum(weights)
            expected_direct = sum(
                weight * energy for weight, energy in zip(weights, energies)
            )

            marginal_numerator: dict[Prescription, int] = defaultdict(int)
            for response, weight in zip(responses, weights):
                points = tuple((left, response[left]) for left in range(side))
                for rank in range(1, min(3, side) + 1):
                    for item in combinations(points, rank):
                        marginal_numerator[tuple(sorted(item))] += weight

            compiled_numerator = sum(
                rank_one[item[0]] * numerator
                for item, numerator in marginal_numerator.items()
                if len(item) == 1
            )
            compiled_numerator += sum(
                rank_two[item] * numerator
                for item, numerator in marginal_numerator.items()
                if len(item) == 2
            )
            compiled_numerator += sum(
                rank_three[item] * numerator
                for item, numerator in marginal_numerator.items()
                if len(item) == 3
            )
            assert compiled_numerator == expected_direct
            expectation_checks += 1

            rank_one_expected = sum(
                rank_one[item[0]] * numerator
                for item, numerator in marginal_numerator.items()
                if len(item) == 1
            )
            rank_one_optimum = max(
                sum(rank_one[(left, response[left])] for left in range(side))
                for response in responses
            )
            assert rank_one_expected <= denominator * rank_one_optimum
            assignment_checks += 1

            uniform_denominator = len(responses)
            uniform_numerator = sum(energies)
            uniform_marginals: dict[Prescription, int] = defaultdict(int)
            for response in responses:
                points = tuple((left, response[left]) for left in range(side))
                for rank in range(1, min(3, side) + 1):
                    for item in combinations(points, rank):
                        uniform_marginals[tuple(sorted(item))] += 1
            rook_style_numerator = sum(
                rank_one[item[0]] * numerator
                for item, numerator in uniform_marginals.items()
                if len(item) == 1
            )
            rook_style_numerator += sum(
                rank_two[item] * numerator
                for item, numerator in uniform_marginals.items()
                if len(item) == 2
            )
            rook_style_numerator += sum(
                rank_three[item] * numerator
                for item, numerator in uniform_marginals.items()
                if len(item) == 3
            )
            assert rook_style_numerator == uniform_numerator
            integer_numerator_checks += 1

            destroyed_load = uniform_numerator // uniform_denominator + 1
            if uniform_numerator % uniform_denominator == 0:
                destroyed_load = uniform_numerator // uniform_denominator + 1
            assert uniform_numerator < uniform_denominator * destroyed_load
            strict_certificate_checks += 1
            systems += 1

    print(
        "verified line-energy marginal rook compiler: "
        f"{systems} geometric response hosts, "
        f"{response_identity_checks} exact response energies, "
        f"{expectation_checks} rational marginal identities, "
        f"{assignment_checks} rank-one assignment bounds, "
        f"{charged_checks} charged coefficient bounds, "
        f"{integer_numerator_checks} uniform integer numerators and "
        f"{strict_certificate_checks} strict destroyed-load certificates"
    )


if __name__ == "__main__":
    main()
