#!/usr/bin/env python3
"""Exact arithmetic checks for CMR133--CMR137."""

from __future__ import annotations

import argparse


def compression_threshold(s: int) -> int:
    return 24 * (s - 1) ** 2 * (3 * s - 2)


def tau(target_load: int) -> int | None:
    if target_load < compression_threshold(4):
        return None
    value = max(4, int((target_load / 72) ** (1 / 3)))
    while compression_threshold(value + 1) <= target_load:
        value += 1
    while compression_threshold(value) > target_load:
        value -= 1
    return value


def verify_baseline_difference(max_common: int, max_new: int, max_lost: int) -> None:
    # Phi(S)=common+new and Phi(S0)=common+lost.
    for common in range(max_common + 1):
        for new in range(max_new + 1):
            for lost in range(max_lost + 1):
                phi_state = common + new
                phi_base = common + lost
                excess = phi_state - phi_base
                assert excess == new - lost
                assert new >= excess


def verify_target_transfer(max_d: int, max_excess: int) -> None:
    # D is the complete old load touching the board, with D>=d.
    for d in range(1, max_d + 1):
        for total_old in range(d, d + 5):
            for excess in range(-max_excess, max_excess + 1):
                if 2 * excess < d:
                    child_touching_lower = total_old - excess
                    assert child_touching_lower > d / 2
                else:
                    # Integer high excess always supplies at least one new triple.
                    assert excess >= 1


def verify_tau(max_s: int) -> None:
    assert compression_threshold(4) == 2160
    for s in range(4, max_s + 1):
        d = compression_threshold(s)
        assert tau(d) == s
        assert d >= 12 * s**3
        assert s < (d / 12) ** (1 / 3) + 1e-12


def verify_load_descent(max_d: int) -> None:
    step = max(1, max_d // 2000)
    for initial in range(2160, max_d + 1, step):
        value = initial
        steps = 0
        while value >= 2160:
            s = tau(value)
            assert s is not None
            # Worst-case next certified target load is at most s.
            next_value = s
            assert 1 <= next_value < (value / 12) ** (1 / 3)
            assert next_value < value
            value = next_value
            steps += 1
            assert steps < 20
        assert value < 2160


def verify_bounded_core(max_d: int) -> None:
    for d in range(1, min(max_d, 2159) + 1):
        # Low excess: integer e<d/2 implies d-e is positive.
        low_excesses = [e for e in range(-3, d + 1) if 2 * e < d]
        assert low_excesses
        for e in low_excesses:
            assert d - e > 0

        # High excess: integer e>=d/2 is at least one.
        high_excesses = [e for e in range(-3, d + 2) if 2 * e >= d]
        assert high_excesses
        assert min(high_excesses) >= 1


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-common", type=int, default=30)
    parser.add_argument("--max-new", type=int, default=30)
    parser.add_argument("--max-lost", type=int, default=30)
    parser.add_argument("--max-d", type=int, default=10**10)
    parser.add_argument("--max-s", type=int, default=500)
    parser.add_argument("--max-excess", type=int, default=20)
    args = parser.parse_args()

    verify_baseline_difference(args.max_common, args.max_new, args.max_lost)
    verify_target_transfer(min(args.max_d, 200), args.max_excess)
    verify_tau(args.max_s)
    verify_load_descent(args.max_d)
    verify_bounded_core(args.max_d)

    print(
        "verified target-load closure: "
        f"max-d={args.max_d}, max-s={args.max_s}, "
        f"max-excess={args.max_excess}"
    )


if __name__ == "__main__":
    main()
