#!/usr/bin/env python3
"""Exact checks for CMR266--CMR270."""

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


def parity_bound(t: int, height: int) -> int:
    top = (t - 1) // 2
    weighted = sum(k * (t - k) for k in range(height, top + 1))
    residual = sum(t - 2 * k for k in range(height, top + 1))
    endpoint = top * (t - top)
    numerator = 3 * weighted + endpoint + 4 * (t - 1) * residual
    assert numerator % 2 == 0
    return numerator // 2


def verify_small_geometric_loads() -> None:
    for t in (7, 9, 11):
        height = (t - 1) // 3 + 1
        source_load, target_load = exact_vertex_loads(t, height)
        bound = parity_bound(t, height)
        assert max(source_load) <= bound
        assert max(target_load) <= bound


def verify_even_mass_pairing(max_t: int = 501) -> None:
    for t in range(7, max_t + 1, 2):
        top = (t - 1) // 2
        for height in range((t - 1) // 3 + 1, top + 1):
            masses = {k: k * (t - k) for k in range(height, top + 1)}
            total = sum(masses.values())
            even_total = sum(value for k, value in masses.items() if k % 2 == 0)
            assert 2 * even_total >= total - masses[top]


def threshold_polynomial(t: int) -> int:
    return 34729 * t**3 - 10246200 * t**2 + 11180000 * t - 2625000


def threshold_derivative(t: int) -> int:
    return 104187 * t**2 - 20492400 * t + 11180000


def reserve_polynomial(t: int) -> int:
    return 22729 * t**3 - 10210200 * t**2 + 11156000 * t - 2625000


def reserve_derivative(t: int) -> int:
    return 68187 * t**2 - 20420400 * t + 11156000


def verify_polynomial_thresholds() -> None:
    assert threshold_polynomial(293) < 0
    assert threshold_polynomial(295) > 0
    assert threshold_derivative(295) > 0
    assert 208374 * 295 - 20492400 > 0

    assert reserve_polynomial(447) < 0
    assert reserve_polynomial(449) > 0
    assert reserve_derivative(449) > 0
    assert 136374 * 449 - 20420400 > 0


def crude_parity_integral_numerator(t: int) -> int:
    # 16 times the integral upper bound in CMR267.
    return (
        16 * 71757 * t**3 // 2000000
        + 16 * 5827 * t**2 // 10000
        + 16 * 61 * t // 50
        - 25
    )


def verify_exact_discrete_sample() -> None:
    for t in range(295, 10_002, 2):
        height = ceil(43 * t / 100)
        high = parity_bound(t, height)
        denominator = t * (t - 1) * (t - 2)
        target = (t - 1) * (t - 2)
        assert 24 * (target + high) < denominator

        if t >= 449:
            reserve = t // 500
            fixed = (reserve + 1) * (t - 1) * (t - 2)
            assert 24 * (fixed + high) < denominator


def main() -> None:
    verify_small_geometric_loads()
    verify_even_mass_pairing()
    verify_polynomial_thresholds()
    verify_exact_discrete_sample()
    print(
        "verified parity-sieved height cleaning: even-height pairing, exact "
        "small-grid loads, the 0.43t threshold, and the floor(t/500) reserve"
    )


if __name__ == "__main__":
    main()
