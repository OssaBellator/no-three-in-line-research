#!/usr/bin/env python3
"""Finite checks for CMR1766--CMR1773."""

from __future__ import annotations

from itertools import combinations
from math import comb, gcd
from random import Random


Point = tuple[int, int]
Line = tuple[int, int, int]


def collinear(first: Point, second: Point, third: Point) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def line_key(first: Point, second: Point) -> Line:
    a = second[1] - first[1]
    b = first[0] - second[0]
    c = -(a * first[0] + b * first[1])
    divisor = gcd(gcd(abs(a), abs(b)), abs(c))
    if divisor:
        a //= divisor
        b //= divisor
        c //= divisor
    if a < 0 or (a == 0 and b < 0) or (a == 0 and b == 0 and c < 0):
        a = -a
        b = -b
        c = -c
    return a, b, c


def line_profiles(background: set[Point], response: set[Point]) -> list[tuple[int, int]]:
    points = background.union(response)
    keys = {
        line_key(first, second)
        for first, second in combinations(points, 2)
    }
    profiles: list[tuple[int, int]] = []
    for a, b, c in keys:
        on_line = {
            point for point in points
            if a * point[0] + b * point[1] + c == 0
        }
        profiles.append(
            (len(on_line.intersection(background)), len(on_line.intersection(response)))
        )
    return profiles


def triple_count(points: set[Point]) -> int:
    return sum(collinear(*triple) for triple in combinations(points, 3))


def main() -> None:
    random = Random(1766)
    grid = [(x, y) for x in range(9) for y in range(9)]
    systems = 0
    exact_energy_checks = 0
    rank_decomposition_checks = 0
    response_pair_checks = 0
    response_triple_checks = 0
    charged_profile_checks = 0
    maximum_load_checks = 0
    triple_free_checks = 0

    for _ in range(1_500):
        points = random.sample(grid, random.randint(6, 28))
        split = random.randint(2, len(points) - 2)
        background = set(points[:split])
        response = set(points[split:])
        profiles = line_profiles(background, response)

        direct = triple_count(background.union(response)) - triple_count(background)
        energy = sum(
            comb(height + response_load, 3) - comb(height, 3)
            for height, response_load in profiles
        )
        assert direct == energy
        exact_energy_checks += 1

        expanded = sum(
            response_load * comb(height, 2)
            + comb(response_load, 2) * height
            + comb(response_load, 3)
            for height, response_load in profiles
        )
        assert direct == expanded
        rank_decomposition_checks += 1

        assert sum(comb(response_load, 2) for _, response_load in profiles) == comb(
            len(response), 2
        )
        response_pair_checks += 1

        response_triples = triple_count(response)
        assert sum(comb(response_load, 3) for _, response_load in profiles) == response_triples
        response_triple_checks += 1

        pair_only = sum(
            response_load
            for height, response_load in profiles
            if height == 2
        )
        triple_charge = sum(
            comb(height, 3) * (3 * response_load + comb(response_load, 2))
            for height, response_load in profiles
            if height >= 3
        )
        charged_bound = (
            pair_only
            + 2 * comb(len(response), 2)
            + response_triples
            + triple_charge
        )
        assert direct <= charged_bound
        charged_profile_checks += 1

        maximum_load = max(
            (response_load for height, response_load in profiles if height >= 3),
            default=0,
        )
        background_triples = triple_count(background)
        coarse_bound = (
            pair_only
            + 2 * comb(len(response), 2)
            + response_triples
            + background_triples * (3 * maximum_load + comb(maximum_load, 2))
        )
        assert direct <= coarse_bound
        assert pair_only <= len(response) * (len(background) // 2)
        maximum_load_checks += 1

        if response_triples == 0:
            assert maximum_load <= 2
            assert direct <= pair_only + 2 * comb(len(response), 2) + 7 * background_triples
            triple_free_checks += 1

        systems += 1

    print(
        "verified line-energy profile census: "
        f"{systems} finite point systems, "
        f"{exact_energy_checks} exact binomial energies, "
        f"{rank_decomposition_checks} rank decompositions, "
        f"{response_pair_checks} response-pair identities, "
        f"{response_triple_checks} response-triple identities, "
        f"{charged_profile_checks} linewise charge bounds, "
        f"{maximum_load_checks} maximum-load bounds and "
        f"{triple_free_checks} triple-free specializations"
    )


if __name__ == "__main__":
    main()
