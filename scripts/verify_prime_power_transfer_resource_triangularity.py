#!/usr/bin/env python3
"""Finite checks for CMR1486--CMR1493."""

from fractions import Fraction
from math import ceil
import random


def translation_arcs(width, height, delta):
    dx, dy = delta
    cells = {(x, y) for x in range(width) for y in range(height)}
    return [
        (a, (a[0] + dx, a[1] + dy))
        for a in cells
        if (a[0] + dx, a[1] + dy) in cells
    ]


def alternating_private_class(arcs, weights):
    successor = {a: b for a, b in arcs}
    predecessor = {b: a for a, b in arcs}
    vertices = {point for arc in arcs for point in arc}
    colour = {}
    for start in vertices:
        if start not in successor or start in predecessor:
            continue
        point = start
        parity = 0
        while point in successor:
            arc = (point, successor[point])
            colour[arc] = parity
            parity ^= 1
            point = successor[point]
    assert len(colour) == len(arcs)
    masses = [
        sum(weights[arc] for arc in arcs if colour[arc] == parity)
        for parity in (0, 1)
    ]
    chosen = 0 if masses[0] >= masses[1] else 1
    return [arc for arc in arcs if colour[arc] == chosen]


def check_private_reserve():
    rng = random.Random(1486)
    forests = 0
    weighted_pairs = 0
    mask_checks = 0
    fresh_additions = 0

    for _ in range(1200):
        width = rng.randint(3, 15)
        height = rng.randint(3, 15)
        while True:
            delta = (rng.randint(-4, 4), rng.randint(-4, 4))
            if delta != (0, 0):
                break
        stock = translation_arcs(width, height, delta)
        if not stock:
            continue
        arcs = rng.sample(stock, rng.randint(1, len(stock)))
        weights = {
            arc: Fraction(rng.randint(1, 12), 12)
            for arc in arcs
        }
        private = alternating_private_class(arcs, weights)
        total = sum(weights.values())
        private_mass = sum(weights[arc] for arc in private)
        assert private_mass >= total / 2

        endpoints = [point for arc in private for point in arc]
        assert len(endpoints) == len(set(endpoints))

        response_partner = bool(rng.randrange(2))
        supports = {
            arc: (set(arc) if response_partner else {arc[0]})
            for arc in private
        }
        universe = list({point for support in supports.values() for point in support})

        for _ in range(8):
            mask = set(rng.sample(universe, rng.randint(0, len(universe))))
            hit_mass = sum(
                weights[arc]
                for arc, support in supports.items()
                if support & mask
            )
            unhit_mass = private_mass - hit_mass
            assert hit_mass <= len(mask)
            assert unhit_mass >= private_mass - len(mask)
            assert max(Fraction(len(mask)), unhit_mass) >= private_mass / 2

            unhit = [
                support
                for support in supports.values()
                if not support & mask
            ]
            assert len(unhit) >= ceil(unhit_mass)
            additions = {next(iter(support)) for support in unhit}
            assert len(additions) == len(unhit)
            assert all(support & additions for support in unhit)
            fresh_additions += len(additions)
            mask_checks += 1

        forests += 1
        weighted_pairs += len(arcs)

    return forests, weighted_pairs, mask_checks, fresh_additions


def check_host_and_monotone_masks():
    rng = random.Random(1488)
    side_checks = 0
    episode_checks = 0
    for side in range(3, 18):
        opposite = {(index, index) for index in range(side)}
        target = (0, 1)
        host = {
            (row, column)
            for row in range(side)
            for column in range(side)
        } - opposite - {target}
        assert len(host) == side * side - side - 1
        side_checks += 1

        remaining = set(host)
        spent = set()
        charges = []
        while remaining and len(charges) < 30:
            charge = rng.randint(1, min(len(remaining), 8))
            added = set(rng.sample(tuple(remaining), charge))
            remaining -= added
            spent |= added
            charges.append(charge)
            assert len(spent) == sum(charges)
            assert len(spent) <= len(host)
            episode_checks += 1
    return side_checks, episode_checks


def check_token_freshness():
    rng = random.Random(1489)
    checks = 0
    fresh_total = 0
    for prime in (2, 3, 5, 7):
        for depth in range(1, 5):
            stock = prime ** (2 * depth)
            for _ in range(180):
                occupied = rng.randint(1, min(stock, 150))
                used = rng.randint(0, stock)
                overlap_min = max(0, occupied - (stock - used))
                overlap_max = min(occupied, used)
                reused = rng.randint(overlap_min, overlap_max)
                fresh = occupied - reused
                assert occupied <= used + fresh
                assert max(used, fresh) >= ceil(occupied / 2)
                fresh_total += fresh
                checks += 1
    return checks, fresh_total


def rank_key(state):
    owner_rank, exponent, depth, used_tokens, used_edges = state
    return owner_rank, -exponent, -depth, used_tokens, used_edges


def check_transfer_dag():
    rng = random.Random(1491)
    transition_checks = 0
    state_systems = 0

    for _ in range(500):
        states = set()
        owner_count = rng.randint(1, 5)
        for owner in range(owner_count):
            for exponent in range(1, rng.randint(2, 6)):
                for depth in range(exponent):
                    for used_tokens in range(rng.randint(1, 4)):
                        for used_edges in range(rng.randint(1, 4)):
                            states.add(
                                (
                                    owner,
                                    exponent,
                                    depth,
                                    used_tokens,
                                    used_edges,
                                )
                            )
        ordered = sorted(states, key=rank_key)
        position = {state: index for index, state in enumerate(ordered)}

        for _ in range(min(400, 3 * len(ordered))):
            source = rng.choice(ordered)
            candidates = [
                target
                for target in ordered
                if target == source or rank_key(source) < rank_key(target)
            ]
            target = rng.choice(candidates)
            assert position[target] >= position[source]
            transition_checks += 1
        state_systems += 1

    return state_systems, transition_checks


def check_rational_gluing():
    rng = random.Random(1492)
    systems = 0
    off_diagonal_entries = 0

    for _ in range(1000):
        size = rng.randint(1, 12)
        diagonal = [
            Fraction(rng.randint(0, 8), 10)
            for _ in range(size)
        ]
        upper = [
            [Fraction(0) for _ in range(size)]
            for _ in range(size)
        ]
        for row in range(size):
            for column in range(row + 1, size):
                upper[row][column] = Fraction(
                    rng.randint(0, 20),
                    rng.randint(1, 10),
                )
                if upper[row][column]:
                    off_diagonal_entries += 1

        scale = [Fraction(0) for _ in range(size)]
        scale[-1] = Fraction(1)
        for row in range(size - 2, -1, -1):
            later = sum(
                upper[row][column] * scale[column]
                for column in range(row + 1, size)
            )
            scale[row] = later / (1 - diagonal[row]) + 1

        for row in range(size):
            image = diagonal[row] * scale[row] + sum(
                upper[row][column] * scale[column]
                for column in range(row + 1, size)
            )
            assert image < scale[row]
        systems += 1

    return systems, off_diagonal_entries


def main():
    private = check_private_reserve()
    masks = check_host_and_monotone_masks()
    tokens = check_token_freshness()
    dag = check_transfer_dag()
    glue = check_rational_gluing()
    print(
        "verified transfer/resource triangularity:",
        private[0],
        "translation forests with",
        private[1],
        "weighted pairs,",
        private[2],
        "private-mask checks and",
        private[3],
        "fresh additions;",
        masks[0],
        "host counts and",
        masks[1],
        "monotone-mask episodes;",
        tokens[0],
        "token-freshness checks;",
        dag[0],
        "transfer systems with",
        dag[1],
        "ordered transitions; and",
        glue[0],
        "rational gluing systems with",
        glue[1],
        "off-diagonal entries",
    )


if __name__ == "__main__":
    main()
