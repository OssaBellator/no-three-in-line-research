#!/usr/bin/env python3
"""Finite checks for CMR1478--CMR1485."""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import ceil, gcd, isqrt
import random


def valuation(value, prime):
    if value == 0:
        return 10**9
    result = 0
    while value % prime == 0:
        value //= prime
        result += 1
    return result


def depth(delta, prime):
    return min(valuation(abs(delta[0]), prime), valuation(abs(delta[1]), prime))


def pairs_in_board(side, delta):
    dx, dy = delta
    return tuple(
        ((x, y), (x + dx, y + dy))
        for x in range(side)
        for y in range(side)
        if 0 <= x + dx < side and 0 <= y + dy < side
    )


def parity_classes(weights):
    edges = {pair for pair, weight in weights.items() if weight}
    outgoing = {a: b for a, b in edges}
    incoming = {b: a for a, b in edges}
    assert len(outgoing) == len(edges) == len(incoming)
    classes = [[], []]
    seen = set()
    for start in sorted(a for a, _b in edges if a not in incoming):
        current = start
        parity = 0
        while current in outgoing:
            pair = (current, outgoing[current])
            assert pair not in seen
            seen.add(pair)
            classes[parity].append(pair)
            current = pair[1]
            parity ^= 1
    assert seen == edges
    return tuple(map(tuple, classes))


def endpoint_disjoint(pairs):
    cells = [cell for pair in pairs for cell in pair]
    return len(cells) == len(set(cells))


def prefix_classes(pairs, prime, level):
    modulus = prime**level
    result = defaultdict(list)
    for owner, partner in pairs:
        assert owner[0] % modulus == partner[0] % modulus
        assert owner[1] % modulus == partner[1] % modulus
        result[(owner[0] % modulus, owner[1] % modulus)].append((owner, partner))
    return result


def check_forests():
    rng = random.Random(1478)
    systems = pair_count = blocker_checks = 0
    for side in range(3, 15):
        deltas = [
            (dx, dy)
            for dx in range(-(side - 1), side)
            for dy in range(-(side - 1), side)
            if (dx, dy) != (0, 0)
        ]
        for _ in range(90):
            delta = rng.choice(deltas)
            stock = pairs_in_board(side, delta)
            chosen_stock = rng.sample(stock, rng.randint(1, len(stock)))
            weights = {
                pair: Fraction(rng.randint(1, 12), 12) for pair in chosen_stock
            }
            classes = parity_classes(weights)
            assert all(endpoint_disjoint(value) for value in classes)
            masses = [sum(weights[pair] for pair in value) for value in classes]
            total = sum(masses)
            selected = classes[masses.index(max(masses))]
            selected_mass = max(masses)
            assert selected_mass >= total / 2
            assert len(selected) >= ceil(total / 2)

            endpoints = {cell for pair in selected for cell in pair}
            for _trial in range(8):
                blocker = set(
                    rng.sample(
                        tuple(endpoints),
                        rng.randint(0, min(len(endpoints), 8)),
                    )
                )
                hit = [pair for pair in selected if blocker.intersection(pair)]
                assert len(hit) <= len(blocker)
                assert sum(weights[pair] for pair in hit) <= len(blocker)
                assert sum(
                    weights[pair] for pair in selected if pair not in hit
                ) >= selected_mass - len(blocker)
                blocker_checks += 1
            systems += 1
            pair_count += len(weights)
    return systems, pair_count, blocker_checks


def check_prefix_tokens():
    rng = random.Random(1481)
    systems = heavy = dispersed = 0
    for prime, exponent in ((2, 3), (3, 3), (5, 2)):
        side = prime**exponent
        for level in range(1, exponent):
            modulus = prime**level
            deltas = [
                (dx, dy)
                for dx in range(-(side - 1), side)
                for dy in range(-(side - 1), side)
                if (dx, dy) != (0, 0)
                and dx % modulus == 0
                and dy % modulus == 0
                and depth((dx, dy), prime) == level
            ]
            for _ in range(80):
                delta = rng.choice(deltas)
                stock = pairs_in_board(side, delta)
                weights = {
                    pair: Fraction(rng.randint(1, 9), 9)
                    for pair in rng.sample(stock, rng.randint(1, len(stock)))
                }
                parity = parity_classes(weights)
                masses = [sum(weights[pair] for pair in value) for value in parity]
                selected = parity[masses.index(max(masses))]
                cells = prefix_classes(selected, prime, level)
                assert sum(map(len, cells.values())) == len(selected)
                threshold = max(2, isqrt(len(selected)) + 1)
                maximum = max(map(len, cells.values()))
                if maximum >= threshold:
                    heavy += 1
                else:
                    assert len(cells) >= ceil(len(selected) / (threshold - 1))
                    dispersed += 1
                systems += 1
    return systems, heavy, dispersed


def line_key(a, b):
    x1, y1 = a
    x2, y2 = b
    values = [y1 - y2, x2 - x1, x1 * y2 - x2 * y1]
    divisor = gcd(gcd(abs(values[0]), abs(values[1])), abs(values[2]))
    if divisor:
        values = [value // divisor for value in values]
    if values[0] < 0 or (
        values[0] == 0
        and (values[1] < 0 or (values[1] == 0 and values[2] < 0))
    ):
        values = [-value for value in values]
    return tuple(values)


def collinear(values):
    return line_key(values[0], values[1]) == line_key(values[0], values[2])


def matching(value):
    return frozenset((row, value[row]) for row in range(len(value)))


def candidate_family(side, opposite, current, target):
    cells = {(row, column) for row in range(side) for column in range(side)}
    graph = cells - set(opposite) - {target}
    old = set(opposite) | set(current)
    result = []
    for values in combinations(tuple(set(opposite) | graph), 3):
        triple = frozenset(values)
        if triple <= old or not collinear(values):
            continue
        prescription = frozenset(triple - set(opposite))
        if (
            not prescription
            or len({x for x, _y in prescription}) != len(prescription)
            or len({y for _x, y in prescription}) != len(prescription)
        ):
            continue
        entering = prescription - set(current)
        if entering:
            owner = min(entering)
            result.append((prescription, owner, tuple(sorted(triple - {owner}))))
    return tuple(result)


def greedy_packing(candidates, rng):
    residual = defaultdict(lambda: Fraction(1))
    weights = [Fraction(0) for _ in candidates]
    order = list(range(len(candidates)))
    rng.shuffle(order)
    for index in order:
        prescription = candidates[index][0]
        available = min(residual[edge] for edge in prescription)
        if available <= 0:
            continue
        weights[index] = available
        for edge in prescription:
            residual[edge] -= available
    return weights


def check_geometric_classes():
    rng = random.Random(1484)
    banks = classes_checked = private_pairs = 0
    for side, repetitions in ((5, 80), (7, 30)):
        opposite = matching(tuple(range(side)))
        derangements = [
            matching(value)
            for value in permutations(range(side))
            if all(value[index] != index for index in range(side))
        ]
        for _ in range(repetitions):
            current = rng.choice(derangements)
            target = rng.choice(tuple(current))
            candidates = candidate_family(side, opposite, current, target)
            weights = greedy_packing(candidates, rng)
            classes = defaultdict(lambda: defaultdict(Fraction))
            for weight, (_prescription, owner, partners) in zip(weights, candidates):
                for partner in partners:
                    kind = "fixed" if partner in opposite else "response"
                    delta = (partner[0] - owner[0], partner[1] - owner[1])
                    classes[(kind, delta)][(owner, partner)] += weight
            for (kind, _delta), pair_weights in classes.items():
                assert max(pair_weights.values()) <= 1
                parity = parity_classes(pair_weights)
                masses = [
                    sum(pair_weights[pair] for pair in value) for value in parity
                ]
                selected = parity[masses.index(max(masses))]
                assert endpoint_disjoint(selected)
                supports = [
                    {owner} if kind == "fixed" else {owner, partner}
                    for owner, partner in selected
                ]
                used = set()
                for support in supports:
                    assert used.isdisjoint(support)
                    used.update(support)
                classes_checked += 1
                private_pairs += len(selected)
            banks += 1
    return banks, classes_checked, private_pairs


def main():
    forests = check_forests()
    prefix = check_prefix_tokens()
    geometric = check_geometric_classes()
    print(
        "verified exact-displacement private-path payment:",
        forests,
        "forest/blocker counts,",
        prefix,
        "prefix heavy/dispersed counts, and",
        geometric,
        "geometric bank/class/private-pair counts",
    )


if __name__ == "__main__":
    main()
