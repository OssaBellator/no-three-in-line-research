#!/usr/bin/env python3
"""Exact checks for CMR261--CMR265."""

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


def role_count_bound(t: int, height: int) -> int:
    return sum(
        2 * euler_phi(k) * (t - k) + 2 * (t - 1) * (t - 2 * k)
        for k in range(height, (t - 1) // 2 + 1)
    )


def verify_small_geometric_loads() -> None:
    for t in (7, 9, 11):
        height = (t - 1) // 3 + 1
        source_load, target_load = exact_vertex_loads(t, height)
        bound = role_count_bound(t, height)
        assert max(source_load) <= bound
        assert max(target_load) <= bound


def threshold_polynomial(t: int) -> int:
    return 1729 * t**3 - 600225 * t**2 + 728750 * t + 31250


def threshold_derivative(t: int) -> int:
    return 5187 * t**2 - 1200450 * t + 728750


def reserve_polynomial(t: int) -> int:
    return 979 * t**3 - 597975 * t**2 + 727250 * t + 31250


def reserve_derivative(t: int) -> int:
    return 2937 * t**2 - 1195950 * t + 727250


def verify_polynomial_thresholds() -> None:
    assert threshold_polynomial(345) < 0
    assert threshold_polynomial(347) > 0
    assert threshold_derivative(347) > 0
    assert 10374 * 347 - 1200450 > 0

    assert reserve_polynomial(609) < 0
    assert reserve_polynomial(611) > 0
    assert reserve_derivative(611) > 0
    assert 5874 * 611 - 1195950 > 0


def crude_role_sum(t: int) -> int:
    height = ceil(11 * t / 25)
    return sum(
        2 * k * (t - k) + 2 * (t - 1) * (t - 2 * k)
        for k in range(height, (t - 1) // 2 + 1)
    )


def verify_exact_arithmetic_sample() -> None:
    for t in range(347, 20_002, 2):
        denominator = t * (t - 1) * (t - 2)
        high_load = crude_role_sum(t) / denominator
        assert 1 / t + high_load < 1 / 24
        if t >= 611:
            reserve_load = (t // 500) / t
            assert reserve_load + 1 / t + high_load < 1 / 24


def verify_placement_sum(max_t: int = 500) -> None:
    for t in range(7, max_t + 1, 2):
        for x0 in range(t):
            for k in range((t - 1) // 3 + 1, (t - 1) // 2 + 1):
                placement_sum = 0
                for u in range(1, k):
                    if gcd(u, k) != 1:
                        continue
                    placement_sum += int(2 * u <= x0)
                    placement_sum += int(u <= x0 <= t - 1 - u)
                    placement_sum += int(2 * u <= t - 1 - x0)
                assert placement_sum <= t - 1


def main() -> None:
    verify_small_geometric_loads()
    verify_polynomial_thresholds()
    verify_exact_arithmetic_sample()
    verify_placement_sum()
    print(
        "verified role-count height cleaning: placement sums, exact small-grid "
        "loads, the 0.44t threshold, and the floor(t/500) reserve"
    )


if __name__ == "__main__":
    main()
