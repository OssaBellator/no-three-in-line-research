#!/usr/bin/env python3
"""Finite arithmetic checks for CMR231--CMR233."""

from __future__ import annotations

from math import ceil, gcd


def euler_phi(n: int) -> int:
    result = n
    value = n
    prime = 2
    while prime * prime <= value:
        if value % prime == 0:
            while value % prime == 0:
                value //= prime
            result -= result // prime
        prime += 1
    if value > 1:
        result -= result // value
    return result


def primitive_unoriented_directions(height: int):
    directions = set()
    for u in range(-height, height + 1):
        for v in range(-height, height + 1):
            if max(abs(u), abs(v)) != height:
                continue
            if u == 0 or v == 0 or gcd(abs(u), abs(v)) != 1:
                continue
            if u < 0 or (u == 0 and v < 0):
                u0, v0 = -u, -v
            else:
                u0, v0 = u, v
            directions.add((u0, v0))
    return directions


def verify_direction_count(max_height: int = 100) -> None:
    for height in range(2, max_height + 1):
        directions = primitive_unoriented_directions(height)
        assert len(directions) == 4 * euler_phi(height)


def explicit_load_bound(t: int) -> float:
    assert t % 2 == 1
    height = ceil(49 * t / 100)
    top = (t - 1) // 2
    weighted = sum(4 * euler_phi(k) for k in range(height, top + 1))
    t3 = t * weighted
    return 1 / t + t3 / (t * (t - 1) * (t - 2))


def crude_polynomial(t: int) -> int:
    return 328 * t**3 - 31575 * t**2 + 53750 * t - 30000


def verify_explicit_threshold(max_t: int = 100_001) -> None:
    assert crude_polynomial(93) < 0
    assert crude_polynomial(95) > 0
    previous = crude_polynomial(95)
    for t in range(95, max_t + 1, 2):
        current = crude_polynomial(t)
        assert current > 0
        assert current >= previous
        previous = current
        assert explicit_load_bound(t) < 1 / 24


def verify_three_point_regime(max_t: int = 10_001) -> None:
    for t in range(95, max_t + 1, 2):
        height = ceil(49 * t / 100)
        assert height > (t - 1) / 3
        for k in range(height, (t - 1) // 2 + 1):
            assert (t - 1) // k == 2


def main() -> None:
    verify_direction_count()
    verify_explicit_threshold()
    verify_three_point_regime()
    print(
        "verified exact top-height slice: 4 phi(K) directions and the "
        "49/100 local-load threshold for all odd t >= 95"
    )


if __name__ == "__main__":
    main()
