#!/usr/bin/env python3
"""Finite checks for CMR1374--CMR1381."""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial, gcd
import random


def matching(permutation):
    return frozenset((row, permutation[row]) for row in range(len(permutation)))


def compatible(prescription):
    return (
        len({row for row, _column in prescription}) == len(prescription)
        and len({column for _row, column in prescription}) == len(prescription)
    )


def derangement_table(limit):
    values = [0] * (limit + 1)
    values[0] = 1
    if limit >= 1:
        values[1] = 0
    for side in range(2, limit + 1):
        values[side] = (side - 1) * (values[side - 1] + values[side - 2])
    return values


DERANGEMENTS = derangement_table(8)


def bank_size(side):
    return DERANGEMENTS[side] * (side - 2) // (side - 1)


def partial_derangement_count(size, unrestricted):
    assert 0 <= unrestricted <= size
    return sum(
        (-1) ** index
        * comb(size - unrestricted, index)
        * factorial(size - index)
        for index in range(size - unrestricted + 1)
    )


def cylinder_type(prescription, forbidden_edge):
    rows = {row for row, _column in prescription}
    columns = {column for _row, column in prescription}
    rank = len(prescription)
    overlap = len(rows & columns)
    source, target = forbidden_edge
    survives = int(source not in rows and target not in columns)
    conflict = 0
    if survives:
        conflict += int(source not in columns)
        conflict += int(target not in rows)
    return rank, overlap, survives, conflict


def cylinder_count_from_type(side, kind):
    rank, overlap, survives, conflict = kind
    base = partial_derangement_count(side - rank, rank - overlap)
    if not survives:
        return base
    correction = partial_derangement_count(
        side - rank - 1,
        rank - overlap + conflict - 1,
    )
    return base - correction


def cylinder_count(side, prescription, forbidden_edge):
    return cylinder_count_from_type(
        side, cylinder_type(prescription, forbidden_edge)
    )


def normalized_bank(side, forbidden_edge):
    identity = matching(tuple(range(side)))
    return [
        matching(value)
        for value in permutations(range(side))
        if matching(value).isdisjoint(identity)
        and forbidden_edge not in matching(value)
    ]


def check_all_normalized_cylinders():
    prescriptions_checked = 0
    realized_types = Counter()
    banks = 0

    for side in range(4, 8):
        forbidden_edge = (0, 1)
        bank = normalized_bank(side, forbidden_edge)
        assert len(bank) == bank_size(side)

        empirical = [defaultdict(int) for _rank in range(4)]
        for response in bank:
            for rank in (1, 2, 3):
                for prescription in combinations(tuple(response), rank):
                    empirical[rank][frozenset(prescription)] += 1

        allowed = [
            (row, column)
            for row in range(side)
            for column in range(side)
            if row != column and (row, column) != forbidden_edge
        ]
        for rank in (1, 2, 3):
            for values in combinations(allowed, rank):
                prescription = frozenset(values)
                if not compatible(prescription):
                    continue
                kind = cylinder_type(prescription, forbidden_edge)
                assert cylinder_count_from_type(side, kind) == empirical[rank].get(
                    prescription, 0
                )
                realized_types[kind] += 1
                prescriptions_checked += 1
        banks += 1

    assert len(realized_types) <= 54
    return banks, prescriptions_checked, len(realized_types)


def transform_cell(opposite, cell):
    inverse = {column: row for row, column in opposite}
    return cell[0], inverse[cell[1]]


def check_opposite_normalization():
    rng = random.Random(1374)
    checked = 0
    for side in range(4, 7):
        all_matchings = [matching(value) for value in permutations(range(side))]
        trials = {4: 80, 5: 60, 6: 30}[side]
        for _ in range(trials):
            opposite = rng.choice(all_matchings)
            cells = {
                (row, column)
                for row in range(side)
                for column in range(side)
            }
            edge = rng.choice(tuple(cells - set(opposite)))
            transformed_edge = transform_cell(opposite, edge)
            original_bank = [
                response
                for response in all_matchings
                if response.isdisjoint(opposite) and edge not in response
            ]
            transformed_bank = {
                frozenset(transform_cell(opposite, cell) for cell in response)
                for response in original_bank
            }
            assert transformed_bank == set(normalized_bank(side, transformed_edge))

            response = rng.choice(original_bank)
            rank = rng.randint(1, 3)
            prescription = frozenset(rng.sample(tuple(response), rank))
            transformed = frozenset(
                transform_cell(opposite, cell) for cell in prescription
            )
            observed = sum(prescription <= state for state in original_bank)
            assert observed == cylinder_count(side, transformed, transformed_edge)
            checked += 1
    return checked


def line_key(first, second):
    x1, y1 = first
    x2, y2 = second
    a = y1 - y2
    b = x2 - x1
    c = x1 * y2 - x2 * y1
    divisor = gcd(gcd(abs(a), abs(b)), abs(c))
    if divisor:
        a //= divisor
        b //= divisor
        c //= divisor
    if a < 0 or (a == 0 and b < 0) or (a == 0 and b == 0 and c < 0):
        a, b, c = -a, -b, -c
    return a, b, c


def collinear(triple):
    return line_key(triple[0], triple[1]) == line_key(triple[0], triple[2])


def physical_triples(state):
    return {
        frozenset(triple)
        for triple in combinations(tuple(state), 3)
        if collinear(triple)
    }


def triple_height(triple):
    key = line_key(*tuple(triple)[:2])
    return max(abs(key[0]), abs(key[1]))


def geometric_candidates(side, opposite, current, forbidden_edge):
    cells = {
        (row, column)
        for row in range(side)
        for column in range(side)
    }
    old_state = set(opposite) | set(current)
    graph = cells - set(opposite) - {forbidden_edge}
    candidates = []
    for triple_tuple in combinations(tuple(set(opposite) | graph), 3):
        triple = frozenset(triple_tuple)
        if triple <= old_state or not collinear(triple_tuple):
            continue
        residual = frozenset(triple - set(opposite))
        if residual and compatible(residual):
            candidates.append((triple, residual))
    return candidates


def exact_new_histogram(side, opposite, current, edge):
    inverse = {column: row for row, column in opposite}
    transformed_edge = (edge[0], inverse[edge[1]])
    histogram = Counter()
    numerator = 0

    for triple, residual in geometric_candidates(side, opposite, current, edge):
        transformed = frozenset(
            (row, inverse[column]) for row, column in residual
        )
        kind = cylinder_type(transformed, transformed_edge)
        credit_class = (len(residual), min(triple_height(triple), side))
        histogram[(credit_class, kind)] += 1
        numerator += cylinder_count_from_type(side, kind)

    return Fraction(numerator, bank_size(side)), histogram


def exact_lost_expectation(side, opposite, old_targets, edge):
    inverse = {column: row for row, column in opposite}
    transformed_edge = (edge[0], inverse[edge[1]])
    numerator = 0
    for target in old_targets:
        residual = frozenset(target - set(opposite))
        if not residual:
            continue
        if edge in residual:
            survival = 0
        else:
            transformed = frozenset(
                (row, inverse[column]) for row, column in residual
            )
            survival = cylinder_count(side, transformed, transformed_edge)
        numerator += bank_size(side) - survival
    return Fraction(numerator, bank_size(side))


def check_geometric_expectations():
    rng = random.Random(1378)
    checked = 0
    class_cells = 0

    for side in range(4, 7):
        all_matchings = [matching(value) for value in permutations(range(side))]
        trials = {4: 60, 5: 35, 6: 12}[side]
        for _ in range(trials):
            opposite = rng.choice(all_matchings)
            current = rng.choice(
                [state for state in all_matchings if state.isdisjoint(opposite)]
            )
            edge = rng.choice(tuple(current))
            old_targets = physical_triples(opposite | current)
            bank = [
                response
                for response in all_matchings
                if response.isdisjoint(opposite) and edge not in response
            ]
            response_targets = [
                physical_triples(opposite | response) for response in bank
            ]

            predicted_new, histogram = exact_new_histogram(
                side, opposite, current, edge
            )
            observed_new = Fraction(
                sum(len(targets - old_targets) for targets in response_targets),
                len(bank),
            )
            assert predicted_new == observed_new

            predicted_lost = exact_lost_expectation(
                side, opposite, old_targets, edge
            )
            observed_lost = Fraction(
                sum(len(old_targets - targets) for targets in response_targets),
                len(bank),
            )
            assert predicted_lost == observed_lost

            predicted_weight = sum(
                (3 * credit_class[0] + credit_class[1])
                * multiplicity
                * cylinder_count_from_type(side, kind)
                for (credit_class, kind), multiplicity in histogram.items()
            )
            observed_weight = sum(
                sum(
                    3 * len(target - set(opposite))
                    + min(triple_height(target), side)
                    for target in targets - old_targets
                )
                for targets in response_targets
            )
            assert predicted_weight == observed_weight

            class_cells += len(histogram)
            checked += 1

    return checked, class_cells


def check_side_five_uniform_obstruction():
    side = 5
    current = matching((0, 1, 2, 4, 3))
    opposite = matching((1, 3, 4, 0, 2))
    old_targets = physical_triples(opposite | current)
    expected_new = Fraction(0)
    expected_lost = Fraction(0)

    for fixed, moving in ((opposite, current), (current, opposite)):
        for edge in moving:
            expected_new += exact_new_histogram(side, fixed, moving, edge)[0]
            expected_lost += exact_lost_expectation(
                side, fixed, old_targets, edge
            )

    assert expected_new == Fraction(1102, 33)
    assert expected_lost == Fraction(458, 33)
    assert expected_new > expected_lost
    return expected_new, expected_lost


def main():
    normalized = check_all_normalized_cylinders()
    geometric = check_geometric_expectations()
    obstruction = check_side_five_uniform_obstruction()
    print(
        "verified exact extension-free cylinders:",
        normalized[0],
        "normalized banks with",
        normalized[1],
        "prescriptions in",
        normalized[2],
        "realized types,",
        check_opposite_normalization(),
        "opposite-coordinate checks,",
        geometric[0],
        "geometric rows with",
        geometric[1],
        "weighted class/type cells, and side-five uniform new/lost",
        obstruction[0],
        "/",
        obstruction[1],
    )


if __name__ == "__main__":
    main()
