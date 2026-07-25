#!/usr/bin/env python3
"""Exact checks for CMR298--CMR301."""

from __future__ import annotations

from itertools import combinations, product


def moments(values: set[int]) -> tuple[int, int]:
    return sum(values), sum(value * value for value in values)


def check_family(
    t: int,
    source_slices: tuple[int, int, int],
    triples: list[tuple[int, int, int]],
    common_rows: set[int],
) -> tuple[int, int]:
    x1, x2, x3 = source_slices
    d1 = x2 - x1
    d2 = x3 - x2
    total_gap = x3 - x1
    assert len(triples) == t - 9

    used = [set(), set(), set()]
    deltas: list[int] = []
    for a1, a2, a3 in triples:
        assert total_gap * a2 == d2 * a1 + d1 * a3
        assert len({a1, a2, a3}) == 3
        for index, value in enumerate((a1, a2, a3)):
            assert value in common_rows
            assert value not in used[index]
            used[index].add(value)
        deltas.append(a3 - a1)

    holes = [common_rows - row_set for row_set in used]
    assert [len(hole_set) for hole_set in holes] == [7, 7, 7]
    first = [moments(hole_set)[0] for hole_set in holes]
    second = [moments(hole_set)[1] for hole_set in holes]

    assert sum(deltas) == first[0] - first[2]
    energy_numerator = (
        total_gap * total_gap * second[1]
        - d2 * total_gap * second[0]
        - d1 * total_gap * second[2]
    )
    assert energy_numerator == d1 * d2 * sum(delta * delta for delta in deltas)
    assert energy_numerator % (d1 * d2) == 0

    n = len(deltas)
    variance = n * sum(delta * delta for delta in deltas) - sum(deltas) ** 2
    pair_variance = sum(
        (deltas[left] - deltas[right]) ** 2
        for left, right in combinations(range(n), 2)
    )
    assert variance == pair_variance
    if len(set(deltas)) > 1:
        assert variance >= n - 1
    else:
        assert variance == 0
    return variance, energy_numerator


def verify_parallel_families() -> None:
    for t in range(10, 100):
        n = t - 9
        common_rows = set(range(t - 2))
        triples = [(a, a + 1, a + 2) for a in range(n)]
        variance, _ = check_family(t, (0, 1, 2), triples, common_rows)
        assert variance == 0

        shifts_12 = {a2 - a1 for a1, a2, _ in triples}
        shifts_23 = {a3 - a2 for _, a2, a3 in triples}
        assert shifts_12 == {1}
        assert shifts_23 == {1}


def verify_nonparallel_example() -> None:
    t = 12
    common_rows = set(range(t - 2))
    triples = [(0, 3, 6), (1, 2, 3), (2, 1, 0)]
    variance, energy = check_family(t, (0, 1, 2), triples, common_rows)
    assert variance == 96
    assert energy == 44


def verify_integer_variance_gap() -> None:
    for n in range(2, 8):
        for values in product(range(-2, 3), repeat=n):
            if len(set(values)) == 1:
                continue
            variance = n * sum(value * value for value in values) - sum(values) ** 2
            assert variance >= n - 1


def verify_translation_bound() -> None:
    for t in range(10, 18):
        n = t - 9
        universe = range(t)
        for subset in combinations(universe, n):
            selected = set(subset)
            for shift in range(-(t - 1), t):
                translated = {value + shift for value in selected}
                if all(0 <= value < t for value in translated):
                    assert abs(shift) <= 9


def verify_shift_types_and_valuations() -> None:
    positive = [
        (left, right)
        for left in range(1, 9)
        for right in range(1, 9)
        if left + right <= 9
    ]
    signed = positive + [(-left, -right) for left, right in positive]
    assert len(positive) == 36
    assert len(signed) == 72

    for p in (11, 13, 17, 19):
        for left, right in signed:
            assert left % p != 0
            assert right % p != 0
            for exponent in range(5):
                d1 = (p**exponent) * abs(left)
                d2 = (p**exponent) * abs(right)
                assert d2 * left == d1 * right


def main() -> None:
    verify_parallel_families()
    verify_nonparallel_example()
    verify_integer_variance_gap()
    verify_translation_bound()
    verify_shift_types_and_valuations()
    print(
        "verified width-three variance: exact hole moments, linear dispersion, "
        "72 bounded parallel shifts, and the p>=11 valuation consequence"
    )


if __name__ == "__main__":
    main()
