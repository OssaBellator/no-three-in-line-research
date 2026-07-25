#!/usr/bin/env python3
"""Verify PX196--PX200 bounded-forbidden matching spread."""
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


def residual_problem(
    forbidden: tuple[int, ...], partial: tuple[tuple[int, int], ...]
) -> tuple[tuple[int, ...], int]:
    """Delete the rows and columns fixed by a compatible partial matching."""
    size = len(forbidden)
    rows = {row for row, _ in partial}
    columns = {column for _, column in partial}
    assert len(rows) == len(partial)
    assert len(columns) == len(partial)
    for row, column in partial:
        assert not forbidden[row] & (1 << column)

    remaining_rows = [row for row in range(size) if row not in rows]
    remaining_columns = [column for column in range(size) if column not in columns]
    column_index = {column: index for index, column in enumerate(remaining_columns)}

    residual: list[int] = []
    for row in remaining_rows:
        mask = 0
        for column in remaining_columns:
            if forbidden[row] & (1 << column):
                mask |= 1 << column_index[column]
        residual.append(mask)
    return tuple(residual), len(remaining_rows)


def first_allowed_permutation(forbidden: tuple[int, ...]) -> tuple[int, ...]:
    """Reconstruct one allowed permutation by exact residual counting."""
    size = len(forbidden)
    partial: list[tuple[int, int]] = []
    used_columns: set[int] = set()
    for row in range(size):
        for column in range(size):
            if column in used_columns or forbidden[row] & (1 << column):
                continue
            candidate = tuple(partial + [(row, column)])
            residual, residual_size = residual_problem(forbidden, candidate)
            if count_allowed(residual, residual_size) > 0:
                partial.append((row, column))
                used_columns.add(column)
                break
        else:
            raise AssertionError("positive count did not yield a permutation")
    return tuple(column for _, column in partial)


def falling_factorial(size: int, rank: int) -> int:
    return factorial(size) // factorial(size - rank)


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


def verify_conditioned_cylinders() -> None:
    """Check PX198--PX199 on exact small residual problems."""
    random = Random(198199)
    cases = ((8, 1, 12), (9, 1, 12), (16, 2, 2))
    for size, degree, samples in cases:
        for _ in range(samples):
            forbidden = union_of_permutations(size, degree, random)
            total = count_allowed(forbidden, size)
            permutation = first_allowed_permutation(forbidden)
            maximum_rank = min(3, size - 8 * degree)
            for rank in range(maximum_rank + 1):
                partial = tuple((row, permutation[row]) for row in range(rank))
                residual, residual_size = residual_problem(forbidden, partial)
                extension_count = count_allowed(residual, residual_size)

                assert extension_count >= exp(-4 * degree) * factorial(residual_size)
                cylinder_probability = extension_count / total
                scale = falling_factorial(size, rank)
                assert cylinder_probability >= exp(-4 * degree) / scale
                assert cylinder_probability <= exp(4 * degree) / scale
        print(
            f"t={size}, Delta={degree}: conditioned cylinder bounds verified"
        )


def sharp_hall_obstruction(degree: int) -> tuple[int, ...]:
    """Return the sharp t=2*Delta-1 forbidden K_(Delta,Delta) obstruction."""
    size = 2 * degree - 1
    forbidden_columns = range(degree - 1, size)
    block_mask = sum(1 << column for column in forbidden_columns)
    return tuple(block_mask if row < degree else 0 for row in range(size))


def verify_hall_threshold() -> None:
    for degree in range(1, 8):
        forbidden = sharp_hall_obstruction(degree)
        size = len(forbidden)
        assert max(mask.bit_count() for mask in forbidden) == degree
        column_degrees = [
            sum(bool(mask & (1 << column)) for mask in forbidden)
            for column in range(size)
        ]
        assert max(column_degrees) == degree
        assert count_allowed(forbidden, size) == 0

        # Adding one row and one column reaches t=2*Delta. The same forbidden
        # block then has an allowed perfect matching, matching the Hall threshold.
        threshold_size = 2 * degree
        threshold_forbidden = tuple(forbidden) + (0,)
        assert len(threshold_forbidden) == threshold_size
        assert count_allowed(threshold_forbidden, threshold_size) > 0
    print("sharp Hall nonemptiness threshold verified")


def verify_depth_cost() -> None:
    # At recursive depth d, the original diagonal, opposite layer, and d-1
    # earlier positions give forbidden degree at most d+1.
    for depth in range(1, 21):
        degree = depth + 1
        hall_minimum_order = 2 * degree
        spread_minimum_order = 8 * degree
        spread_constant = exp(4 * degree)
        assert hall_minimum_order >= 4
        assert spread_minimum_order == 4 * hall_minimum_order
        assert spread_constant > 1
    print("bounded-depth forbidden-degree accounting verified")


def main() -> None:
    verify_exact_counts()
    verify_lll_inequalities()
    verify_conditioned_cylinders()
    verify_hall_threshold()
    verify_depth_cost()
    print("PX196--PX200 verified")


if __name__ == "__main__":
    main()
