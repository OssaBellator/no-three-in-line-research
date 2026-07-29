#!/usr/bin/env python3
"""Finite audit for SAS5iw--SAS5ja signed boundary cancellation."""

from __future__ import annotations

from fractions import Fraction
import random


SEED = 90216
SYSTEMS = 10_000
THRESHOLDS = (
    Fraction(1, 4),
    Fraction(1, 3),
    Fraction(1, 2),
    Fraction(2, 3),
)


def main() -> None:
    rng = random.Random(SEED)
    ledger_vectors = 0
    distinct_signed_signatures = 0
    total_variation_units = 0
    net_boundary_units = 0
    exact_cancellation_pairs = 0
    barrier_epochs = 0
    cancellation_epochs = 0

    for _ in range(SYSTEMS):
        dimension = rng.randint(1, 5)
        coordinate_bound = rng.randint(1, 5)
        ledger_count = rng.randint(2, 8)
        vectors = [
            tuple(
                rng.randint(-coordinate_bound, coordinate_bound)
                for _coordinate in range(dimension)
            )
            for _ledger in range(ledger_count)
        ]

        ledger_vectors += ledger_count
        distinct_signed_signatures += len(set(vectors))

        positive = [0] * dimension
        negative = [0] * dimension
        aggregate = [0] * dimension
        for vector in vectors:
            for coordinate, value in enumerate(vector):
                if value >= 0:
                    positive[coordinate] += value
                else:
                    negative[coordinate] += -value
                aggregate[coordinate] += value

        variation = sum(positive) + sum(negative)
        net_mass = sum(abs(value) for value in aggregate)
        cancellation = sum(
            min(positive[coordinate], negative[coordinate])
            for coordinate in range(dimension)
        )
        assert 2 * cancellation == variation - net_mass

        threshold = rng.choice(THRESHOLDS)
        if variation == 0:
            cancellation_epochs += 1
        elif net_mass >= threshold * variation:
            barrier_epochs += 1
            maximum_coordinate = max(abs(value) for value in aggregate)
            assert maximum_coordinate * dimension >= net_mass
            assert (
                maximum_coordinate * dimension
                >= threshold * variation
            )
        else:
            cancellation_epochs += 1
            assert (
                Fraction(cancellation, 1)
                > (1 - threshold) * variation / 2
            )

        total_variation_units += variation
        net_boundary_units += net_mass
        exact_cancellation_pairs += cancellation

    print(f"systems={SYSTEMS}")
    print(f"ledger_vectors={ledger_vectors}")
    print(f"distinct_signed_signatures={distinct_signed_signatures}")
    print(f"total_variation_units={total_variation_units}")
    print(f"net_boundary_units={net_boundary_units}")
    print(f"exact_cancellation_pairs={exact_cancellation_pairs}")
    print(f"barrier_epochs={barrier_epochs}")
    print(f"cancellation_epochs={cancellation_epochs}")


if __name__ == "__main__":
    main()
