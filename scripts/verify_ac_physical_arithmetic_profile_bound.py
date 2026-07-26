#!/usr/bin/env python3
"""Finite audit for AC3mr--AC3mv."""

from collections import Counter
from math import gcd


def primitive_directions(n):
    bound = n - 1
    return [
        (x, y)
        for x in range(1, bound + 1)
        for y in range(-bound, bound + 1)
        if gcd(x, abs(y)) == 1
    ]


def determinant(first, second):
    return first[0] * second[1] - first[1] * second[0]


def main():
    counts = Counter()

    for n in range(2, 9):
        bound = n - 1
        directions = primitive_directions(n)
        direction_ceiling = bound * (2 * bound + 1)
        assert len(directions) <= direction_ceiling
        counts["boards"] += 1
        counts["primitive directions"] += len(directions)

        determinants = set()
        for first in directions:
            for second in directions:
                value = determinant(first, second)
                assert abs(value) <= 2 * bound * bound
                counts["ordered direction pairs"] += 1
                if value:
                    determinants.add(value)

        denominator_ceiling = 2 * bound * bound
        reduced_denominators = set()
        for numerator in determinants:
            for denominator in determinants:
                common = gcd(abs(numerator), abs(denominator))
                reduced_numerator = abs(numerator) // common
                reduced_denominator = abs(denominator) // common
                assert reduced_numerator <= denominator_ceiling
                assert reduced_denominator <= denominator_ceiling
                reduced_denominators.add(reduced_denominator)
                counts["determinant ratios"] += 1

        if reduced_denominators:
            assert max(reduced_denominators) <= denominator_ceiling

        exact_profile_count = (
            len(directions) ** 2
            * sum(range(2, denominator_ceiling + 1))
        )
        profile_bound = (
            direction_ceiling ** 2
            * denominator_ceiling
            * (denominator_ceiling + 1)
            // 2
        )
        assert exact_profile_count <= profile_bound
        counts["profile formula systems"] += 1

        external_roles = 7
        fixed_q = max(2, denominator_ceiling)
        exact_fixed_address_count = (
            n * n * external_roles * fixed_q * len(directions) ** 2
        )
        fixed_address_bound = (
            n * n * external_roles * fixed_q * direction_ceiling ** 2
        )
        assert exact_fixed_address_count <= fixed_address_bound
        counts["fixed denominator address systems"] += 1

        exact_total_address_count = n * n * external_roles * exact_profile_count
        total_address_bound = n * n * external_roles * profile_bound
        assert exact_total_address_count <= total_address_bound
        counts["total address systems"] += 1

    print("AC3mr--AC3mv finite audit passed")
    for label in sorted(counts):
        print(f"{label}: {counts[label]:,}")


if __name__ == "__main__":
    main()
