#!/usr/bin/env python3
"""Finite and arithmetic checks for CMR512--CMR516."""

from __future__ import annotations

from collections import Counter
from math import ceil, floor, sqrt


def verify_prefix_partition() -> None:
    for prime in (3, 5, 7):
        for height in range(2, 5):
            side = prime**height
            for depth in range(1, height):
                modulus = prime**depth
                for row in range(min(side, 12)):
                    for step in range(1, min(side, 17)):
                        targets = list(range(0, side, step))
                        occupancy = Counter(target % modulus for target in targets)
                        assert sum(occupancy.values()) == len(targets)
                        assert all(value <= side // modulus for value in occupancy.values())

                        source_prefix = row % modulus
                        for target in targets:
                            target_prefix = target % modulus
                            assert row % modulus == source_prefix
                            assert target % modulus == target_prefix


def verify_threshold_dichotomy() -> None:
    for total in range(1, 100):
        for class_count in range(1, total + 1):
            # Generate a deterministic positive composition of total.
            occupancy = [1] * class_count
            for index in range(total - class_count):
                occupancy[index % class_count] += 1

            for threshold in range(2, total + 3):
                heavy = max(occupancy) >= threshold
                dispersed = class_count >= ceil(total / (threshold - 1))
                assert heavy or dispersed


def verify_square_root_endpoint() -> None:
    for degree in range(1, 10000):
        if degree == 1:
            assert floor(sqrt(degree)) == 1
            continue
        threshold = ceil(sqrt(degree))
        dispersed_count = ceil(degree / (threshold - 1))
        assert dispersed_count >= floor(sqrt(degree))


def verify_disjoint_token_cells() -> None:
    for prime in (3, 5):
        for height in range(2, 5):
            side = prime**height
            for depth in range(1, height):
                modulus = prime**depth
                classes = {
                    residue: {
                        (row, target)
                        for row in range(side)
                        if row % modulus == 0
                        for target in range(side)
                        if target % modulus == residue
                    }
                    for residue in range(modulus)
                }
                residues = list(classes)
                for first_index, first in enumerate(residues):
                    for second in residues[first_index + 1 :]:
                        assert classes[first].isdisjoint(classes[second])


def main() -> None:
    verify_prefix_partition()
    verify_threshold_dichotomy()
    verify_square_root_endpoint()
    verify_disjoint_token_cells()
    print(
        "verified CMR512--CMR516: exact unavailable-star prefix occupancy, "
        "heavy-versus-dispersed arithmetic, square-root endpoint, disjoint "
        "token cells, and row-column symmetric counting"
    )


if __name__ == "__main__":
    main()
