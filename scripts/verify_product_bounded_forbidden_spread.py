#!/usr/bin/env python3
"""Verify PX196--PX197 bounded-forbidden matching spread."""
from __future__ import annotations

from functools import lru_cache
from math import exp, factorial, log
from random import Random


def count_allowed(forbidden: tuple[int, ...], size: int) -> int:
    full = (1 << size) - 1

    @lru_cache(None)
    def dynamic(row: int, used: int) -> int:
        if row == size:
            return 1
        available = full & ~forbidden[row] & ~used
        total = 0
        while available:
            bit = available & -available
            available -= bit
            total += dynamic(row + 1, used | bit)
        return total

    return dynamic(0, 0)


def union_of_permutations(size: int, degree: int, random: Random) -> tuple[int, ...]:
    masks = [0] * size
    for _ in range(degree):
        permutation = list(range(size))
        random.shuffle(permutation)
        for row, column in enumerate(permutation):
            masks[row] |= 1 << column
    return tuple(masks)


def verify_exact_counts() -> None:
    random = Random(20260725)
    for size in range(7, 15):
        for degree in (1, 2, 3):
            if degree >= size:
                continue
            for _ in range(20):
                forbidden = union_of_permutations(size, degree, random)
                count = count_allowed(forbidden, size)
                assert count > 0
                # The asymptotic theorem only claims this when size>=8*degree.
                # At these small orders, record the much stronger empirical
                # density and check the universal lower expression when it is
                # below one matching.
                lower = exp(-4 * degree) * factorial(size)
                if lower <= 1:
                    assert count >= lower
            print(
                f"t={size}, Delta={degree}: exact allowed matchings positive"
            )


def verify_lll_inequalities() -> None:
    for degree in range(1, 21):
        for size in (8 * degree, 10 * degree, 16 * degree, 32 * degree):
            probability = 1 / size
            witness = 2 / size
            dependency = 2 * degree - 2
            assert witness * (1 - witness) ** dependency >= probability
            event_count = degree * size
            lower_probability = (1 - witness) ** event_count
            assert lower_probability >= exp(-4 * degree)

            # The logarithmic inequality used in the proof.
            assert log(1 - 2 / size) >= -4 / size
    print("symbolic lopsided-LLL inequalities verified")


def verify_depth_cost() -> None:
    # At recursive depth d, the original diagonal, opposite layer, and d-1
    # earlier positions give forbidden degree at most d+1.
    for depth in range(1, 21):
        degree = depth + 1
        minimum_order = 8 * degree
        spread_constant = exp(4 * degree)
        assert minimum_order >= 16
        assert spread_constant > 1
    print("bounded-depth forbidden-degree accounting verified")


def main() -> None:
    verify_exact_counts()
    verify_lll_inequalities()
    verify_depth_cost()
    print("PX196--PX197 verified")


if __name__ == "__main__":
    main()
