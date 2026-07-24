#!/usr/bin/env python3
"""Arithmetic checks for CMR190--CMR192."""

from __future__ import annotations

from math import ceil


def compression_threshold(s: int) -> int:
    return 12 * (s - 1) ** 2 * (3 * s - 2)


def outside_mass(targets: int) -> int:
    return ceil(2 * targets / 11)


def rho(targets: int) -> int | None:
    mass = outside_mass(targets)
    if mass < compression_threshold(4):
        return None
    value = 4
    while compression_threshold(value + 1) <= mass:
        value += 1
    return value


def verify_floor_ceiling(max_targets: int) -> None:
    for targets in range(1, max_targets + 1):
        local = (9 * targets) // 11
        outside = targets - local
        assert outside == outside_mass(targets)
        assert local + outside == targets
        assert 11 * outside >= 2 * targets


def verify_first_threshold() -> None:
    first = next(
        targets
        for targets in range(1, 20_000)
        if rho(targets) is not None
    )
    assert first == 5935
    assert outside_mass(first) == 1080
    assert compression_threshold(4) == 1080


def verify_compression(max_targets: int) -> None:
    step = max(1, max_targets // 10_000)
    for targets in range(1, max_targets + 1, step):
        value = rho(targets)
        if value is None:
            assert outside_mass(targets) < compression_threshold(4)
            continue
        assert compression_threshold(value) <= outside_mass(targets)
        assert compression_threshold(value + 1) > outside_mass(targets)
        assert value >= 4


def main() -> None:
    verify_floor_ceiling(max_targets=100_000)
    verify_first_threshold()
    verify_compression(max_targets=10**9)
    print(
        "verified batch parent lifting: 2/11 outside mass, "
        "first compression threshold R=5935, and rho arithmetic"
    )


if __name__ == "__main__":
    main()
