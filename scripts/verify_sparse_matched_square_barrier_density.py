#!/usr/bin/env python3
"""Finite audit for SAS5fm--SAS5fq."""

from collections import defaultdict
from fractions import Fraction
import random

SEED = 20260727


def main():
    rng = random.Random(SEED)
    counts = defaultdict(int)

    for _ in range(35000):
        n = rng.randint(3, 14)
        square_count = rng.randint(1, 30)
        density = Fraction(rng.randint(1, 8), rng.randint(1, 5))

        squares = []
        total_matched = 0

        for square_id in range(square_count):
            matched = rng.randint(1, 100)
            total_matched += matched

            negative_weights = [
                rng.randint(1, 30)
                for _ in range(rng.randint(0, 6))
            ]
            negative_total = sum(negative_weights)

            positive_records = []
            positive_total = 0
            for record_index in range(rng.randint(1, 7)):
                weight = rng.randint(1, 30)
                columns = tuple(sorted(rng.sample(range(n), 3)))
                positive_records.append(
                    (f"{square_id}:{record_index}", weight, columns)
                )
                positive_total += weight

            if positive_total < negative_total:
                weight = negative_total - positive_total + rng.randint(0, 20)
                columns = tuple(sorted(rng.sample(range(n), 3)))
                positive_records.append(
                    (f"{square_id}:{len(positive_records)}", weight, columns)
                )
                positive_total += weight

            barrier = positive_total - negative_total
            assert barrier >= 0
            squares.append(
                {
                    "matched": matched,
                    "barrier": barrier,
                    "positive": positive_records,
                    "positive_total": positive_total,
                    "negative_total": negative_total,
                }
            )

        total_barrier = sum(square["barrier"] for square in squares)
        total_positive = sum(square["positive_total"] for square in squares)
        total_negative = sum(square["negative_total"] for square in squares)
        assert total_barrier == total_positive - total_negative

        low = [
            square
            for square in squares
            if Fraction(square["barrier"], 1) <= density * square["matched"]
        ]
        high = [
            square
            for square in squares
            if Fraction(square["barrier"], 1) > density * square["matched"]
        ]

        low_matched = sum(square["matched"] for square in low)
        high_matched = sum(square["matched"] for square in high)
        assert low_matched + high_matched == total_matched

        if 2 * low_matched >= total_matched:
            low_barrier = sum(square["barrier"] for square in low)
            assert Fraction(low_barrier, 1) <= density * low_matched
            counts["low_barrier_branches"] += 1
            counts["low_selected_squares"] += len(low)

        else:
            assert 2 * high_matched > total_matched
            high_barrier = sum(square["barrier"] for square in high)
            high_positive = sum(square["positive_total"] for square in high)
            assert Fraction(high_barrier, 1) > density * high_matched
            assert high_positive >= high_barrier
            assert Fraction(high_positive, 1) > density * total_matched / 2

            records = [
                record
                for square in high
                for record in square["positive"]
            ]
            output_stock = len(records) + rng.randint(0, 20)
            heaviest = max(record[1] for record in records)
            assert heaviest * output_stock >= high_positive
            assert Fraction(heaviest, 1) > (
                density * total_matched / (2 * output_stock)
            )

            incidence = [0] * n
            for _address, weight, columns in records:
                for column in columns:
                    incidence[column] += weight
            assert sum(incidence) == 3 * high_positive
            assert max(incidence) * n >= 3 * high_positive
            assert Fraction(max(incidence), 1) > (
                3 * density * total_matched / (2 * n)
            )

            counts["high_barrier_branches"] += 1
            counts["high_selected_squares"] += len(high)
            counts["positive_output_records"] += len(records)

        # Integrated extraction from an original matched bank.
        degree = rng.randint(0, 20)
        original_matched = rng.randint(1, (degree + 1) * total_matched)
        assert Fraction(total_matched, 1) >= Fraction(
            original_matched,
            degree + 1,
        )

        if 2 * low_matched >= total_matched:
            assert Fraction(low_matched, 1) >= Fraction(
                original_matched,
                2 * (degree + 1),
            )
        else:
            records = [
                record
                for square in high
                for record in square["positive"]
            ]
            output_stock = len(records) + rng.randint(0, 20)
            heaviest = max(record[1] for record in records)
            assert Fraction(heaviest, 1) > (
                density
                * original_matched
                / (2 * (degree + 1) * output_stock)
            )

            incidence = [0] * n
            for _address, weight, columns in records:
                for column in columns:
                    incidence[column] += weight
            assert Fraction(max(incidence), 1) > (
                3
                * density
                * original_matched
                / (2 * n * (degree + 1))
            )

        # Neutral and common-step substitutions.
        neutral_factor = (2 * n - 3) * (4 * rng.randint(0, 5) + 1)
        neutral_weight = rng.randint(
            1,
            2 * neutral_factor * original_matched,
        )
        neutral_matched_lower = Fraction(neutral_weight, 2 * neutral_factor)
        assert Fraction(original_matched, 1) >= neutral_matched_lower

        pair_degree = rng.randint(0, 20)
        pair_weight = rng.randint(
            1,
            2 * (pair_degree + 1) * original_matched,
        )
        pair_matched_lower = Fraction(pair_weight, 2 * (pair_degree + 1))
        assert Fraction(original_matched, 1) >= pair_matched_lower

        counts["systems"] += 1
        counts["square_vertices"] += square_count
        counts["matched_weight"] += total_matched
        counts["barrier_weight"] += total_barrier

    print("SAS matched-square barrier-density audit passed")
    for key in sorted(counts):
        print(f"  {key.replace('_', ' ')}: {counts[key]}")


if __name__ == "__main__":
    main()
