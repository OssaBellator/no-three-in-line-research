#!/usr/bin/env python3
"""Exact checks for CMR252--CMR256."""

from __future__ import annotations

from itertools import combinations
from math import ceil, gcd


def euler_phi(n: int) -> int:
    return sum(gcd(a, n) == 1 for a in range(1, n))


def primitive_height(p: tuple[int, int], q: tuple[int, int]) -> int:
    dx = q[0] - p[0]
    dy = q[1] - p[1]
    divisor = gcd(abs(dx), abs(dy))
    return max(abs(dx) // divisor, abs(dy) // divisor)


def exact_vertex_loads(t: int, height: int) -> tuple[list[int], list[int]]:
    points = [(x, y) for x in range(t) for y in range(t)]
    source_load = [0] * t
    target_load = [0] * t

    for p, q, r in combinations(points, 3):
        if len({p[0], q[0], r[0]}) < 3:
            continue
        if len({p[1], q[1], r[1]}) < 3:
            continue
        if (q[0] - p[0]) * (r[1] - p[1]) != (q[1] - p[1]) * (
            r[0] - p[0]
        ):
            continue
        if primitive_height(p, q) < height:
            continue

        for x in {p[0], q[0], r[0]}:
            source_load[x] += 1
        for y in {p[1], q[1], r[1]}:
            target_load[y] += 1

    return source_load, target_load


def cmr252_bound(t: int, height: int) -> int:
    return sum(
        2 * euler_phi(k) * (4 * t - 7 * k)
        for k in range(height, (t - 1) // 2 + 1)
    )


def verify_small_geometric_loads() -> None:
    for t in (7, 9, 11):
        height = (t - 1) // 3 + 1
        source_load, target_load = exact_vertex_loads(t, height)
        bound = cmr252_bound(t, height)
        assert max(source_load) <= bound
        assert max(target_load) <= bound


def first_margin_polynomial(t: int) -> int:
    return 117 * t**3 - 19680 * t**2 + 18400 * t + 25000


def first_margin_derivative(t: int) -> int:
    return 351 * t**2 - 39360 * t + 18400


def reserve_margin_polynomial(t: int) -> int:
    return 57 * t**3 - 19500 * t**2 + 18280 * t + 25000


def reserve_margin_derivative(t: int) -> int:
    return 171 * t**2 - 39000 * t + 18280


def verify_polynomial_margins() -> None:
    assert first_margin_polynomial(167) < 0
    assert first_margin_polynomial(169) > 0
    assert first_margin_derivative(169) > 0
    # The derivative is increasing from this point onward.
    assert 702 * 169 - 39360 > 0

    assert reserve_margin_polynomial(341) < 0
    assert reserve_margin_polynomial(343) > 0
    assert reserve_margin_derivative(343) > 0
    assert 342 * 343 - 39000 > 0


def exact_crude_sum(t: int) -> int:
    height = ceil(9 * t / 20)
    return sum(
        2 * k * (4 * t - 7 * k)
        for k in range(height, (t - 1) // 2 + 1)
    )


def verify_exact_arithmetic_sample() -> None:
    for t in range(169, 20_002, 2):
        denominator = t * (t - 1) * (t - 2)
        high_load = exact_crude_sum(t) / denominator
        assert 1 / t + high_load < 1 / 24
        if t >= 343:
            reserve = (t // 200) / t
            assert reserve + 1 / t + high_load < 1 / 24


def verify_reserve_extraction_arithmetic() -> None:
    for t in range(343, 100_002, 2):
        reserve = t // 200
        assert reserve <= t - 2
        assert ceil(9 * t / 20) > (t - 1) / 3


def main() -> None:
    verify_small_geometric_loads()
    verify_polynomial_margins()
    verify_exact_arithmetic_sample()
    verify_reserve_extraction_arithmetic()
    print(
        "verified refined target-height cleaning: exact small-grid loads, "
        "the 0.45t threshold, and the floor(t/200) line reserve"
    )


if __name__ == "__main__":
    main()
