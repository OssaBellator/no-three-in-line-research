#!/usr/bin/env python3
"""Finite checks for CMR1502--CMR1509."""

from fractions import Fraction
from collections import defaultdict
from math import ceil
import random


def translation_arcs(width, height, delta):
    cells = {(x, y) for x in range(width) for y in range(height)}
    return [
        (a, (a[0] + delta[0], a[1] + delta[1]))
        for a in cells
        if (a[0] + delta[0], a[1] + delta[1]) in cells
    ]


def private_parity(arcs, weights):
    successor = {a: b for a, b in arcs}
    predecessor = {b: a for a, b in arcs}
    vertices = {point for arc in arcs for point in arc}
    parity = {}
    for start in vertices:
        if start not in successor or start in predecessor:
            continue
        point = start
        colour = 0
        while point in successor:
            arc = (point, successor[point])
            parity[arc] = colour
            colour ^= 1
            point = successor[point]
    assert len(parity) == len(arcs)
    masses = [
        sum(weights[arc] for arc in arcs if parity[arc] == colour)
        for colour in (0, 1)
    ]
    chosen = 0 if masses[0] >= masses[1] else 1
    return [arc for arc in arcs if parity[arc] == chosen]


def check_owner_exclusion():
    rng = random.Random(1502)
    banks = 0
    pairs = 0
    exclusion_checks = 0
    private_pairs = 0

    for _ in range(1400):
        width = rng.randint(3, 20)
        height = rng.randint(3, 20)
        while True:
            delta = (rng.randint(-5, 5), rng.randint(-5, 5))
            if delta != (0, 0):
                break
        stock = translation_arcs(width, height, delta)
        if not stock:
            continue
        arcs = rng.sample(stock, rng.randint(1, len(stock)))
        weights = {
            arc: Fraction(rng.randint(1, 20), 20)
            for arc in arcs
        }
        assert len({arc[0] for arc in arcs}) == len(arcs)
        assert all(weight <= 1 for weight in weights.values())

        owners = [arc[0] for arc in arcs]
        loaded = set(rng.sample(owners, rng.randint(0, len(owners))))
        loaded_mass = sum(
            weights[arc] for arc in arcs if arc[0] in loaded
        )
        outside = [arc for arc in arcs if arc[0] not in loaded]
        outside_mass = sum(weights[arc] for arc in outside)
        total = loaded_mass + outside_mass

        assert loaded_mass <= len(loaded)
        assert outside_mass >= total - len(loaded)
        assert max(Fraction(len(loaded)), outside_mass) >= total / 2

        if outside:
            private = private_parity(outside, weights)
            private_mass = sum(weights[arc] for arc in private)
            assert private_mass >= outside_mass / 2
            endpoints = [point for arc in private for point in arc]
            assert len(endpoints) == len(set(endpoints))
            assert len(private) >= ceil(private_mass)
            private_pairs += len(private)

        banks += 1
        pairs += len(arcs)
        exclusion_checks += 1

    return banks, pairs, exclusion_checks, private_pairs


def check_root_unloaded_channels():
    rng = random.Random(1505)
    checks = 0
    weighted_pairs = 0
    heavy_pairs = 0

    for prime, side, repetitions in (
        (2, 16, 250),
        (3, 27, 220),
        (5, 25, 180),
        (7, 49, 120),
    ):
        for _ in range(repetitions):
            while True:
                delta = (
                    rng.randint(-(side - 1), side - 1),
                    rng.randint(-(side - 1), side - 1),
                )
                if delta != (0, 0) and (
                    delta[0] % prime or delta[1] % prime
                ):
                    break
            stock = translation_arcs(side, side, delta)
            if not stock:
                continue
            arcs = rng.sample(stock, rng.randint(1, min(len(stock), 300)))
            weights = {
                arc: Fraction(rng.randint(1, 16), 16)
                for arc in arcs
            }
            owners = [arc[0] for arc in arcs]
            loaded = set(rng.sample(owners, rng.randint(0, len(owners))))
            outside = [arc for arc in arcs if arc[0] not in loaded]
            total = sum(weights.values())
            outside_mass = sum(weights[arc] for arc in outside)

            if len(loaded) < total / 2:
                assert outside_mass > total / 2
                classes = defaultdict(list)
                for arc in outside:
                    residue = (
                        arc[0][0] % prime,
                        arc[0][1] % prime,
                    )
                    classes[residue].append(arc)
                residue, heavy = max(
                    classes.items(),
                    key=lambda item: sum(weights[arc] for arc in item[1]),
                )
                mass = sum(weights[arc] for arc in heavy)
                assert mass * prime * prime >= outside_mass
                assert mass >= total / (2 * prime * prime)
                endpoints = [point for arc in heavy for point in arc]
                assert len(endpoints) == len(set(endpoints))
                assert all(
                    (arc[0][0] % prime, arc[0][1] % prime) == residue
                    for arc in heavy
                )
                heavy_pairs += len(heavy)

            checks += 1
            weighted_pairs += len(arcs)

    return checks, weighted_pairs, heavy_pairs


def check_many_loaded_owners():
    rng = random.Random(1507)
    checks = 0
    for _ in range(3000):
        owner_count = rng.randint(1, 200)
        masses = [
            Fraction(rng.randint(0, 20), 20)
            for _ in range(owner_count)
        ]
        total = sum(masses)
        threshold = Fraction(rng.randint(1, 20), 20)
        loaded = [mass for mass in masses if mass >= threshold]
        unloaded_mass = sum(mass for mass in masses if mass < threshold)
        assert total == sum(loaded) + unloaded_mass
        if loaded:
            assert len(loaded) >= sum(loaded)
        checks += 1
    return checks


def main():
    excluded = check_owner_exclusion()
    root = check_root_unloaded_channels()
    threshold = check_many_loaded_owners()
    print(
        "verified owner-disjoint packed/loaded split:",
        excluded[0],
        "translation banks with",
        excluded[1],
        "weighted pairs,",
        excluded[2],
        "owner-exclusion checks and",
        excluded[3],
        "private pairs;",
        root[0],
        "root-channel checks with",
        root[1],
        "weighted pairs and",
        root[2],
        "heavy unloaded-channel pairs; and",
        threshold,
        "loaded-owner bookkeeping checks",
    )


if __name__ == "__main__":
    main()
