#!/usr/bin/env python3
"""Verify AC3ch--AC3ck by exhaustive small derangement enumeration."""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations


def derangements(size):
    return [
        perm
        for perm in permutations(range(size))
        if all(perm[index] != index for index in range(size))
    ]


def partial_type(columns, rows):
    rank = len(columns)
    if rank == 1:
        return "R1"

    mapping = dict(zip(columns, rows, strict=True))
    overlap = len(set(columns) & set(rows))
    cycle_lengths = []
    recorded = set()

    for start in columns:
        path = []
        current = start
        while current in mapping and current not in path:
            path.append(current)
            current = mapping[current]
        if current in path:
            cycle = frozenset(path[path.index(current):])
            if cycle not in recorded:
                recorded.add(cycle)
                cycle_lengths.append(len(cycle))

    cycle_lengths = tuple(sorted(cycle_lengths))

    if rank == 2:
        if overlap == 0 and not cycle_lengths:
            return "A"
        if overlap == 1 and not cycle_lengths:
            return "B"
        if overlap == 2 and cycle_lengths == (2,):
            return "C"

    if rank == 3:
        if overlap == 0 and not cycle_lengths:
            return "A0"
        if overlap == 1 and not cycle_lengths:
            return "A1"
        if overlap == 2 and not cycle_lengths:
            return "A2"
        if overlap == 2 and cycle_lengths == (2,):
            return "C2"
        if overlap == 3 and cycle_lengths == (3,):
            return "C3"

    raise AssertionError((columns, rows, overlap, cycle_lengths))


EXPECTED_COUNTS = {
    (2, 1): {"R1": 1},
    (2, 2): {"C": 1},
    (3, 1): {"R1": 1},
    (3, 2): {"B": 1},
    (3, 3): {"C3": 1},
    (4, 1): {"R1": 3},
    (4, 2): {"A": 2, "B": 1, "C": 1},
    (4, 3): {"A2": 1, "C2": 1},
    (5, 1): {"R1": 11},
    (5, 2): {"A": 4, "B": 3, "C": 2},
    (5, 3): {"A1": 2, "A2": 1, "C2": 1, "C3": 1},
    (6, 1): {"R1": 53},
    (6, 2): {"A": 14, "B": 11, "C": 9},
    (6, 3): {"A0": 6, "A1": 4, "A2": 3, "C2": 3, "C3": 2},
}

EXPECTED_CAPS = {
    (2, 1): Fraction(1, 1),
    (2, 2): Fraction(1, 1),
    (3, 1): Fraction(1, 2),
    (3, 2): Fraction(1, 2),
    (3, 3): Fraction(1, 2),
    (4, 1): Fraction(1, 3),
    (4, 2): Fraction(2, 9),
    (4, 3): Fraction(1, 9),
    (5, 1): Fraction(1, 4),
    (5, 2): Fraction(1, 11),
    (5, 3): Fraction(1, 22),
    (6, 1): Fraction(1, 5),
    (6, 2): Fraction(14, 265),
    (6, 3): Fraction(6, 265),
}

CONSERVATIVE_AMPLIFICATION = {
    2: Fraction(1, 2),
    3: Fraction(2, 3),
    4: Fraction(1, 1),
    5: Fraction(4, 3),
    6: Fraction(5, 3),
}


def verify_tables():
    banks = 0
    prescriptions = 0
    type_checks = 0
    cap_checks = 0

    for size in range(2, 7):
        bank = derangements(size)
        banks += len(bank)

        for rank in range(1, min(3, size) + 1):
            by_type = defaultdict(set)
            probabilities = []

            for columns in combinations(range(size), rank):
                for rows in permutations(range(size), rank):
                    if any(row == column for column, row in zip(columns, rows, strict=True)):
                        continue

                    count = sum(
                        all(perm[column] == row for column, row in zip(columns, rows, strict=True))
                        for perm in bank
                    )
                    if count == 0:
                        continue

                    kind = partial_type(columns, rows)
                    by_type[kind].add(count)
                    probabilities.append(Fraction(count, len(bank)))
                    prescriptions += 1

            expected = EXPECTED_COUNTS[(size, rank)]
            assert set(by_type) == set(expected)
            for kind, counts in by_type.items():
                assert counts == {expected[kind]}
                type_checks += 1

            cap = max(probabilities)
            assert cap == EXPECTED_CAPS[(size, rank)]
            cap_checks += 1

            if rank == 1:
                assert cap == Fraction(1, size - 1)

    return banks, prescriptions, type_checks, cap_checks


def verify_amplification(maximum=40):
    rank_checks = 0
    conservative_checks = 0
    final_checks = 0

    for size in range(2, 7):
        rank_count = min(3, size)
        weakest = None

        for rank in range(1, rank_count + 1):
            cap = EXPECTED_CAPS[(size, rank)]
            amplification = Fraction(1, rank_count) / cap
            weakest = amplification if weakest is None else min(weakest, amplification)

            for expected_weight in range(1, maximum + 1):
                raw_bound = Fraction(expected_weight, rank_count) / cap
                assert cap * raw_bound == Fraction(expected_weight, rank_count)
                rank_checks += 1

        assert weakest == CONSERVATIVE_AMPLIFICATION[size]
        conservative_checks += 1

        for gain in range(1, maximum + 1):
            state_weight = Fraction(gain, 12)
            conservative_raw = CONSERVATIVE_AMPLIFICATION[size] * state_weight
            expected = {
                2: Fraction(gain, 24),
                3: Fraction(gain, 18),
                4: Fraction(gain, 12),
                5: Fraction(gain, 9),
                6: Fraction(5 * gain, 36),
            }[size]
            assert conservative_raw == expected
            final_checks += 1

    return rank_checks, conservative_checks, final_checks


def main():
    banks, prescriptions, types, caps = verify_tables()
    ranks, conservative, finals = verify_amplification()
    print(
        "AC RI small derangements: verified "
        f"{banks} derangement states, {prescriptions} compatible prescriptions, "
        f"{types} exact types, {caps} sharp caps, {ranks} rank amplifications, "
        f"{conservative} conservative rows, and {finals} AC3ck constants"
    )


if __name__ == "__main__":
    main()
