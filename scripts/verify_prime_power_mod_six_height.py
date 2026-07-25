#!/usr/bin/env python3
"""Exact checks for CMR278--CMR283."""

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


def mod_six_bound(t: int, height: int) -> int:
    top = (t - 1) // 2
    weighted = sum(k * (t - k) for k in range(height, top + 1))
    residual = sum(t - 2 * k for k in range(height, top + 1))
    # Ceiling of the rational CMR279 bound.
    numerator = 12 * weighted + 20 * t * t + 18 * (t - 1) * residual
    return (numerator + 8) // 9


def verify_six_block_inequality(max_t: int = 301) -> None:
    for t in range(7, max_t + 1, 2):
        top = (t - 1) // 2
        for height in range(2, top + 1):
            actual = sum(
                euler_phi(k) * (t - k)
                for k in range(height, top + 1)
            )
            weighted = sum(k * (t - k) for k in range(height, top + 1))
            assert 9 * actual <= 6 * weighted + 10 * t * t


def verify_small_geometric_loads() -> None:
    for t in (7, 9, 11):
        height = (t - 1) // 3 + 1
        source_load, target_load = exact_vertex_loads(t, height)
        bound = mod_six_bound(t, height)
        assert max(source_load) <= bound
        assert max(target_load) <= bound


def threshold_polynomial(t: int) -> int:
    return 2731 * t**3 - 4298725 * t**2 + 2141250 * t - 500000


def threshold_derivative(t: int) -> int:
    return 8193 * t**2 - 8597450 * t + 2141250


def reserve_polynomial(t: int) -> int:
    return 4337 * t**3 - 8594075 * t**2 + 4280250 * t - 1000000


def reserve_derivative(t: int) -> int:
    return 13011 * t**2 - 17188150 * t + 4280250


def verify_polynomial_thresholds() -> None:
    assert threshold_polynomial(1573) < 0
    assert threshold_polynomial(1575) > 0
    assert threshold_derivative(1575) > 0
    assert 16386 * 1575 - 8597450 > 0

    assert reserve_polynomial(1981) < 0
    assert reserve_polynomial(1983) > 0
    assert reserve_derivative(1983) > 0
    assert 26022 * 1983 - 17188150 > 0


def verify_exact_discrete_sample() -> None:
    for t in range(1575, 20_002, 2):
        height = ceil(21 * t / 50)
        high = mod_six_bound(t, height)
        denominator = t * (t - 1) * (t - 2)
        target = (t - 1) * (t - 2)
        assert 24 * (target + high) < denominator

        if t >= 1983:
            reserve = t // 2000
            fixed = (reserve + 1) * (t - 1) * (t - 2)
            assert 24 * (fixed + high) < denominator


def main() -> None:
    verify_six_block_inequality()
    verify_small_geometric_loads()
    verify_polynomial_thresholds()
    verify_exact_discrete_sample()
    print(
        "verified mod-six height cleaning: six-residue totient blocks, exact "
        "small-grid loads, the 0.42t threshold, and the floor(t/2000) reserve"
    )


if __name__ == "__main__":
    main()
