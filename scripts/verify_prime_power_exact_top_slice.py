#!/usr/bin/env python3
"""Finite arithmetic checks for CMR231--CMR233."""

from __future__ import annotations

from math import ceil, gcd


def phi_sieve(limit: int) -> list[int]:
    phi = list(range(limit + 1))
    for prime in range(2, limit + 1):
        if phi[prime] != prime:
            continue
        for multiple in range(prime, limit + 1, prime):
            phi[multiple] -= phi[multiple] // prime
    return phi


def primitive_unoriented_directions(height: int):
    directions = set()
    for u in range(-height, height + 1):
        for v in range(-height, height + 1):
            if max(abs(u), abs(v)) != height:
                continue
            if u == 0 or v == 0 or gcd(abs(u), abs(v)) != 1:
                continue
            if u < 0 or (u == 0 and v < 0):
                directions.add((-u, -v))
            else:
                directions.add((u, v))
    return directions


def verify_direction_count(phi: list[int], max_height: int = 100) -> None:
    for height in range(2, max_height + 1):
        directions = primitive_unoriented_directions(height)
        assert len(directions) == 4 * phi[height]


def crude_polynomial(t: int) -> int:
    return 328 * t**3 - 31575 * t**2 + 53750 * t - 30000


def verify_explicit_threshold(phi: list[int], max_t: int = 100_001) -> None:
    prefix = [0] * len(phi)
    for value in range(1, len(phi)):
        prefix[value] = prefix[value - 1] + phi[value]

    assert crude_polynomial(93) < 0
    assert crude_polynomial(95) > 0

    previous = crude_polynomial(95)
    for t in range(95, max_t + 1, 2):
        current = crude_polynomial(t)
        assert current > 0
        assert current >= previous
        previous = current

        height = ceil(49 * t / 100)
        top = (t - 1) // 2
        weighted_directions = 4 * (prefix[top] - prefix[height - 1])
        local_load = 1 / t + weighted_directions / ((t - 1) * (t - 2))
        assert local_load < 1 / 24

        assert height > (t - 1) / 3
        if height <= top:
            assert (t - 1) // height == 2
            assert (t - 1) // top == 2


def main() -> None:
    limit = 100_001
    phi = phi_sieve(limit)
    verify_direction_count(phi)
    verify_explicit_threshold(phi, max_t=limit)
    print(
        "verified exact top-height slice: 4 phi(K) directions and the "
        "49/100 local-load threshold for all odd t from 95 through 100001"
    )


if __name__ == "__main__":
    main()
