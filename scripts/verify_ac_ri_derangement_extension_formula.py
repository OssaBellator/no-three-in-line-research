#!/usr/bin/env python3
"""Verify AC3cl--AC3co by exhaustive and symbolic derangement counts."""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial


def derangements(size):
    return [
        perm
        for perm in permutations(range(size))
        if all(perm[index] != index for index in range(size))
    ]


def derangement_number(size):
    if size == 0:
        return 1
    if size == 1:
        return 0
    previous_previous = 1
    previous = 0
    for value in range(2, size + 1):
        current = (value - 1) * (previous + previous_previous)
        previous_previous, previous = previous, current
    return previous


def falling(value, rank):
    result = 1
    for offset in range(rank):
        result *= value - offset
    return result


def extension_formula(size, rank, overlap):
    free_diagonal = size - 2 * rank + overlap
    assert free_diagonal >= 0
    return sum(
        (-1) ** chosen
        * comb(free_diagonal, chosen)
        * factorial(size - rank - chosen)
        for chosen in range(free_diagonal + 1)
    )


def verify_exhaustive(maximum_size=8):
    bank_checks = 0
    prescription_checks = 0
    formula_checks = 0
    overlap_checks = 0
    sharp_checks = 0

    for size in range(2, maximum_size + 1):
        bank = derangements(size)
        assert len(bank) == derangement_number(size)
        bank_checks += len(bank)

        for rank in range(1, min(3, size) + 1):
            counts = Counter()
            for perm in bank:
                for columns in combinations(range(size), rank):
                    rows = tuple(perm[column] for column in columns)
                    counts[(columns, rows)] += 1

            by_overlap = defaultdict(set)
            for (columns, rows), count in counts.items():
                assert len(set(rows)) == rank
                assert all(
                    row != column
                    for column, row in zip(columns, rows, strict=True)
                )
                overlap = len(set(columns) & set(rows))
                expected = extension_formula(size, rank, overlap)
                assert count == expected
                by_overlap[overlap].add(count)
                prescription_checks += 1
                formula_checks += 1

            for overlap, values in by_overlap.items():
                assert values == {extension_formula(size, rank, overlap)}
                overlap_checks += 1

            minimum_overlap = min(by_overlap)
            sharp_count = max(counts.values())
            assert sharp_count == extension_formula(size, rank, minimum_overlap)
            assert sharp_count == max(next(iter(values)) for values in by_overlap.values())
            sharp_checks += 1

            if size >= 2 * rank:
                assert minimum_overlap == 0

    return (
        bank_checks,
        prescription_checks,
        formula_checks,
        overlap_checks,
        sharp_checks,
    )


def verify_symbolic(maximum_size=30):
    monotonic_checks = 0
    universal_checks = 0
    rank_one_checks = 0
    amplification_checks = 0

    for size in range(2, maximum_size + 1):
        deranged = derangement_number(size)
        assert deranged * 3 >= factorial(size)

        for rank in range(1, min(3, size) + 1):
            minimum_overlap = max(0, 2 * rank - size)
            values = [
                extension_formula(size, rank, overlap)
                for overlap in range(minimum_overlap, rank + 1)
            ]
            assert all(
                earlier >= later
                for earlier, later in zip(values, values[1:])
            )
            monotonic_checks += max(0, len(values) - 1)

            sharp = values[0]
            probability = Fraction(sharp, deranged)
            assert probability <= Fraction(3, falling(size, rank))
            universal_checks += 1

            if rank == 1:
                assert minimum_overlap == 0
                assert probability == Fraction(1, size - 1)
                rank_one_checks += 1

            if size >= 7:
                for expected_numerator in range(1, 31):
                    expected = Fraction(expected_numerator, 1)
                    raw_sharp = expected / (3 * probability)
                    raw_universal = Fraction(falling(size, rank), 9) * expected
                    assert raw_sharp >= raw_universal
                    amplification_checks += 1

                    gain = expected * 12
                    profile_universal = Fraction(falling(size, rank), 108) * gain
                    assert profile_universal == raw_universal
                    amplification_checks += 1

    return monotonic_checks, universal_checks, rank_one_checks, amplification_checks


def main():
    exhaustive = verify_exhaustive()
    symbolic = verify_symbolic()
    print(
        "AC RI derangement formula: verified "
        f"{exhaustive[0]} derangement states, {exhaustive[1]} prescriptions, "
        f"{exhaustive[2]} formula counts, {exhaustive[3]} overlap classes, "
        f"{exhaustive[4]} sharp caps, {symbolic[0]} monotonicity steps, "
        f"{symbolic[1]} universal caps, {symbolic[2]} rank-one identities, "
        f"and {symbolic[3]} large-state amplification constants"
    )


if __name__ == "__main__":
    main()
