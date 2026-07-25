#!/usr/bin/env python3
"""Exhaust BDA5y on small scalar-slot configurations."""

from itertools import combinations
from math import ceil


def maximum_matching(occupied, jump):
    occupied = set(occupied)
    matched = set()
    count = 0
    for start in sorted(occupied):
        end = start + jump
        if (
            end in occupied
            and start not in matched
            and end not in matched
        ):
            matched.add(start)
            matched.add(end)
            count += 1
    return count


def verify(maximum_slots=12, maximum_g=6):
    subset_checks = 0
    increment_checks = 0

    for slot_count in range(1, maximum_slots + 1):
        slots = tuple(range(slot_count))
        for g in range(1, min(maximum_g, slot_count) + 1):
            for size in range(slot_count + 1):
                for occupied in combinations(slots, size):
                    occupied_set = set(occupied)
                    edges = sum(
                        index + g in occupied_set
                        for index in occupied
                    )
                    lower = max(0, 2 * size - slot_count - g)
                    assert edges >= lower
                    assert maximum_matching(occupied, g) >= ceil(lower / 2)
                    subset_checks += 1

            for m in range(1, 8):
                q = g * m
                for base in range(1, 6):
                    for index in range(max(0, slot_count - g)):
                        h = base + index * m
                        assert base + (index + g) * m == h + q
                        for determinant in range(-8, 9):
                            if determinant == 0:
                                continue
                            assert (
                                (h + q) * determinant
                                - h * determinant
                            ) == q * determinant
                            increment_checks += 1

    return subset_checks, increment_checks


def main():
    subsets, increments = verify()
    print(
        "BDA scalar q-pairs: verified "
        f"{subsets} occupied subsets and {increments} increments"
    )


if __name__ == "__main__":
    main()
