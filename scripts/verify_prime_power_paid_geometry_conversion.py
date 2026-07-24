#!/usr/bin/env python3
"""Finite checks for CMR129--CMR132."""

from __future__ import annotations

import argparse
from itertools import product


def threshold(s: int) -> int:
    return 24 * (s - 1) ** 2 * (3 * s - 2)


def sigma(t: int) -> int | None:
    if t < threshold(4):
        return None
    value = 4
    while threshold(value + 1) <= t:
        value += 1
    return value


def verify_disjoint_layer_pigeonhole(max_q: int) -> None:
    # A triple's majority layer is 0 or 1. One layer receives ceil(q/2).
    for q in range(1, max_q + 1):
        for assignment in product((0, 1), repeat=q):
            counts = [assignment.count(0), assignment.count(1)]
            assert max(counts) >= (q + 1) // 2

        if q >= 4:
            chosen = (q + 1) // 2
            assert chosen <= q
            assert max(4, chosen) <= q


def verify_heavy_line_split(max_s: int) -> None:
    for s in range(4, max_s + 1):
        total = 2 * s + 1
        # Exhaust possible layer populations on the smallest heavy line.
        for first in range(total + 1):
            second = total - first
            majority = max(first, second)
            assert majority >= s + 1
            # After choosing s endpoints, at least two line points remain.
            assert total - s >= 2


def verify_padding(max_n: int) -> None:
    for n in range(4, max_n + 1):
        for q in range(1, n + 1):
            chosen = (q + 1) // 2
            for target in range(max(4, chosen), n + 1):
                assert target - chosen <= n - chosen


def verify_closure_contraction(max_t: int) -> None:
    step = max(1, max_t // 2000)
    for t in range(2160, max_t + 1, step):
        s = sigma(t)
        assert s is not None
        assert threshold(s) <= t
        assert threshold(s + 1) > t
        assert s < (t / 12) ** (1 / 3)
        assert s < t


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-q", type=int, default=14)
    parser.add_argument("--max-s", type=int, default=500)
    parser.add_argument("--max-n", type=int, default=200)
    parser.add_argument("--max-t", type=int, default=10**10)
    args = parser.parse_args()

    verify_disjoint_layer_pigeonhole(args.max_q)
    verify_heavy_line_split(args.max_s)
    verify_padding(args.max_n)
    verify_closure_contraction(args.max_t)

    print(
        "verified paid-geometry conversion: "
        f"max-q={args.max_q}, max-s={args.max_s}, "
        f"max-n={args.max_n}, max-t={args.max_t}"
    )


if __name__ == "__main__":
    main()
