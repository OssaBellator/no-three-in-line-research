#!/usr/bin/env python3
"""Finite checks for CMR1470--CMR1477."""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import ceil, gcd, isqrt
import random


Cell = tuple[int, int]
Pair = tuple[Cell, Cell]


def p_valuation(value: int, prime: int) -> int:
    value = abs(value)
    if value == 0:
        return 10**9
    result = 0
    while value % prime == 0:
        value //= prime
        result += 1
    return result


def displacement_depth(delta: Cell, prime: int) -> int:
    return min(p_valuation(delta[0], prime), p_valuation(delta[1], prime))


def projective_direction(delta: Cell, prime: int, depth: int) -> Cell:
    scale = prime**depth
    x = (delta[0] // scale) % prime
    y = (delta[1] // scale) % prime
    assert (x, y) != (0, 0)
    if x:
        return 1, y * pow(x, -1, prime) % prime
    return 0, 1


def translation_pairs(side: int, delta: Cell) -> tuple[Pair, ...]:
    dx, dy = delta
    result = []
    for x in range(side):
        for y in range(side):
            partner = (x + dx, y + dy)
            if 0 <= partner[0] < side and 0 <= partner[1] < side:
                result.append(((x, y), partner))
    return tuple(result)


def parity_classes(
    weights: dict[Pair, Fraction],
) -> tuple[tuple[Pair, ...], tuple[Pair, ...]]:
    positive = {pair for pair, value in weights.items() if value > 0}
    outgoing = {owner: partner for owner, partner in positive}
    incoming = {partner: owner for owner, partner in positive}
    assert len(outgoing) == len(positive)
    assert len(incoming) == len(positive)

    first: list[Pair] = []
    second: list[Pair] = []
    seen: set[Pair] = set()
    starts = sorted(owner for owner, _partner in positive if owner not in incoming)
    for start in starts:
        current = start
        parity = 0
        while current in outgoing:
            pair = (current, outgoing[current])
            assert pair not in seen
            seen.add(pair)
            (first if parity == 0 else second).append(pair)
            current = pair[1]
            parity ^= 1

    assert seen == positive
    return tuple(first), tuple(second)


def endpoint_disjoint(pairs: tuple[Pair, ...]) -> bool:
    used: set[Cell] = set()
    for owner, partner in pairs:
        if owner in used or partner in used:
            return False
        used.add(owner)
        used.add(partner)
    return True


def prefix_cell(pair: Pair, prime: int, depth: int) -> tuple[int, int]:
    modulus = prime**depth
    owner, partner = pair
    assert owner[0] % modulus == partner[0] % modulus
    assert owner[1] % modulus == partner[1] % modulus
    return owner[0] % modulus, owner[1] % modulus


def heavy_or_dispersed(
    pairs: tuple[Pair, ...], prime: int, depth: int, threshold: int
) -> tuple[str, int, dict[tuple[int, int], list[Pair]]]:
    classes: dict[tuple[int, int], list[Pair]] = defaultdict(list)
    for pair in pairs:
        classes[prefix_cell(pair, prime, depth)].append(pair)
    maximum = max(map(len, classes.values()), default=0)
    if maximum >= threshold:
        return "heavy", maximum, classes
    occupied = len(classes)
    assert occupied >= ceil(len(pairs) / (threshold - 1))
    return "dispersed", occupied, classes


def check_random_translation_forests() -> tuple[int, int, int]:
    rng = random.Random(1470)
    systems = 0
    positive_pairs = 0
    blocker_checks = 0
    for side in range(3, 15):
        deltas = [
            (dx, dy)
            for dx in range(-(side - 1), side)
            for dy in range(-(side - 1), side)
            if (dx, dy) != (0, 0)
        ]
        for _ in range(90):
            delta = rng.choice(deltas)
            stock = translation_pairs(side, delta)
            selected = rng.sample(stock, rng.randint(1, len(stock)))
            weights = {
                pair: Fraction(rng.randint(1, 12), 12) for pair in selected
            }
            classes = parity_classes(weights)
            assert endpoint_disjoint(classes[0])
            assert endpoint_disjoint(classes[1])
            total = sum(weights.values())
            masses = [sum(weights[pair] for pair in value) for value in classes]
            assert max(masses) >= total / 2
            chosen = classes[masses.index(max(masses))]
            chosen_mass = max(masses)
            assert len(chosen) >= ceil(chosen_mass)
            assert len(chosen) >= ceil(total / 2)

            endpoints = {cell for pair in chosen for cell in pair}
            for _trial in range(8):
                sample_size = rng.randint(0, min(len(endpoints), 8))
                blocker = set(rng.sample(tuple(endpoints), sample_size))
                hit = [pair for pair in chosen if blocker.intersection(pair)]
                hit_mass = sum(weights[pair] for pair in hit)
                assert len(hit) <= len(blocker)
                assert hit_mass <= len(blocker)
                assert sum(
                    weights[pair] for pair in chosen if pair not in hit
                ) >= chosen_mass - len(blocker)
                blocker_checks += 1

            systems += 1
            positive_pairs += len(selected)
    return systems, positive_pairs, blocker_checks


def check_prefix_splice() -> tuple[int, int, int]:
    rng = random.Random(1473)
    systems = 0
    heavy = 0
    dispersed = 0
    for prime, exponent in ((2, 3), (3, 3), (5, 2)):
        side = prime**exponent
        for depth in range(1, exponent):
            modulus = prime**depth
            candidates = [
                (dx, dy)
                for dx in range(-(side - 1), side)
                for dy in range(-(side - 1), side)
                if (dx, dy) != (0, 0)
                and dx % modulus == 0
                and dy % modulus == 0
                and displacement_depth((dx, dy), prime) == depth
            ]
            for _ in range(80):
                delta = rng.choice(candidates)
                stock = translation_pairs(side, delta)
                weights = {
                    pair: Fraction(rng.randint(1, 9), 9)
                    for pair in rng.sample(stock, rng.randint(1, len(stock)))
                }
                classes = parity_classes(weights)
                masses = [sum(weights[pair] for pair in value) for value in classes]
                chosen = classes[masses.index(max(masses))]
                direction = projective_direction(delta, prime, depth)
                for pair in chosen:
                    cell = prefix_cell(pair, prime, depth)
                    assert cell[0] < modulus and cell[1] < modulus
                    reduced = (
                        delta[0] // prime**depth,
                        delta[1] // prime**depth,
                    )
                    assert projective_direction(reduced, prime, 0) == direction
                threshold = max(2, isqrt(len(chosen)) + 1)
                branch, value, cells = heavy_or_dispersed(
                    chosen, prime, depth, threshold
                )
                assert sum(map(len, cells.values())) == len(chosen)
                assert len(cells) == len(set(cells))
                if branch == "heavy":
                    assert value >= threshold
                    heavy += 1
                else:
                    assert value >= ceil(len(chosen) / (threshold - 1))
                    dispersed += 1
                systems += 1
    return systems, heavy, dispersed


def line_key(first: Cell, second: Cell) -> tuple[int, int, int]:
    x1, y1 = first
    x2, y2 = second
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


def collinear(triple: tuple[Cell, Cell, Cell]) -> bool:
    return line_key(triple[0], triple[1]) == line_key(triple[0], triple[2])


def compatible(edges: frozenset[Cell]) -> bool:
    return (
        len({row for row, _column in edges}) == len(edges)
        and len({column for _row, column in edges}) == len(edges)
    )


def matching(value: tuple[int, ...]) -> frozenset[Cell]:
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
        if not prescription or not compatible(prescription):
            continue
        entering = prescription - set(current)
        if not entering:
            continue
        owner = min(entering)
        partners = tuple(sorted(triple - {owner}))
        result.append((prescription, owner, partners))
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
        value = available
        if rng.random() >= 0.7:
            units = max(1, int(12 * available))
            value = min(available, Fraction(rng.randint(1, units), 12))
        weights[index] = value
        for edge in prescription:
            residual[edge] -= value
    return tuple(weights)


def check_geometric_packed_classes() -> tuple[int, int, int]:
    rng = random.Random(1476)
    banks = 0
    displacement_classes = 0
    extracted_pairs = 0
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
            classes: dict[tuple[str, Cell], dict[Pair, Fraction]] = defaultdict(
                lambda: defaultdict(Fraction)
            )
            for weight, (_prescription, owner, partners) in zip(weights, candidates):
                if not weight:
                    continue
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
                chosen = parity[masses.index(max(masses))]
                assert endpoint_disjoint(chosen)
                residual_supports = []
                for owner, partner in chosen:
                    support = {owner}
                    if kind == "response":
                        support.add(partner)
                    residual_supports.append(support)
                used = set()
                for support in residual_supports:
                    assert used.isdisjoint(support)
                    used.update(support)
                assert len(used) == len(chosen) * (
                    2 if kind == "response" else 1
                )
                displacement_classes += 1
                extracted_pairs += len(chosen)
            banks += 1
    return banks, displacement_classes, extracted_pairs


def main():
    forests = check_random_translation_forests()
    prefix = check_prefix_splice()
    geometric = check_geometric_packed_classes()
    print(
        "verified exact-displacement path/token payment:",
        forests[0],
        "random translation forests with",
        forests[1],
        "weighted pairs and",
        forests[2],
        "blocker checks,",
        prefix[0],
        "nonroot prefix systems (",
        prefix[1],
        "heavy,",
        prefix[2],
        "dispersed), and",
        geometric[0],
        "geometric packed banks with",
        geometric[1],
        "displacement classes and",
        geometric[2],
        "extracted endpoint-disjoint pairs",
    )


if __name__ == "__main__":
    main()
