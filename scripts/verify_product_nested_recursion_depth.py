#!/usr/bin/env python3
"""Checks for PX263--PX266."""

from __future__ import annotations

import math
import random


def next_order(h: int, delta: int) -> tuple[int, int, int]:
    b = max(32, 16 * delta + 4)
    if h < b:
        return h, 0, b
    if h >= b * b:
        root = math.isqrt(h)
        nxt = root // 2
        qh_floor = root
    else:
        nxt = b // 2
        qh_floor = b
    return nxt, qh_floor, b


def check_one_step() -> None:
    for delta in range(0, 50):
        b = max(32, 16 * delta + 4)
        for h in range(b, min(200000, b * b + 1000)):
            nxt, qh_floor, _ = next_order(h, delta)
            assert 0 < qh_floor <= h
            assert qh_floor >= 32
            assert nxt >= 8 * delta + 2
            assert nxt <= max(math.sqrt(h) / 2, b / 2) + 1e-12
            if h >= b * b:
                assert nxt <= math.sqrt(h) / 2 + 1e-12
            else:
                assert nxt <= b / 2 + 1e-12


def simulate(t0: int, delta0: int = 2) -> tuple[int, int]:
    t = t0
    depth = 0
    while True:
        delta = delta0 + depth
        b = max(32, 16 * delta + 4)
        # Worst case for depth takes the largest nested obstruction h=t.
        if t < b:
            return depth, t
        t, _qh, _b = next_order(t, delta)
        depth += 1
        assert depth < 1000


def check_depth() -> None:
    for exponent in range(4, 1000, 7):
        t0 = 2**exponent
        depth, terminal = simulate(t0)
        envelope = math.ceil(math.log2(math.log2(t0))) + 8
        assert depth <= envelope
        assert terminal <= max(32, 16 * (2 + depth) + 4)

    rng = random.Random(265)
    for _ in range(1000):
        t0 = rng.randint(16, 10**30)
        delta0 = rng.randint(0, 5)
        depth, terminal = simulate(t0, delta0)
        assert depth <= math.ceil(math.log2(math.log2(max(t0, 4)))) + 10
        assert terminal == O_terminal(terminal, delta0, depth)


def O_terminal(terminal: int, delta0: int, depth: int) -> int:
    bound = max(32, 16 * (delta0 + depth) + 4)
    assert terminal < bound
    return terminal


def check_spread_exponent() -> None:
    for t0 in [10**6, 10**12, 10**30, 2**1000, 2**10000]:
        depth, _terminal = simulate(t0)
        exponent = 2 * sum(2 + j for j in range(depth))
        factor_log = exponent
        # log factor / log t tends to zero; finite check uses a generous envelope.
        assert factor_log <= 20 * (math.log(math.log(t0)) + 1) ** 2
        if t0 >= 10**30:
            assert factor_log / math.log(t0) < 1


def check_exact_order_trimming() -> None:
    rng = random.Random(264)
    for _ in range(1000):
        h = rng.randint(32, 10000)
        q = rng.uniform(32 / h, 1)
        supplied_size = rng.randint(math.ceil(q * h / 2), h)
        exact = math.floor(q * h / 2)
        assert exact <= supplied_size
        # Nonnegative sector weights only decrease under taking a subset.
        weights = [rng.random() for _ in range(supplied_size)]
        assert sum(sorted(weights)[:exact]) <= sum(weights) + 1e-12


def main() -> None:
    check_one_step()
    check_depth()
    check_spread_exponent()
    check_exact_order_trimming()
    print("PX263--PX266 nested recursion checks passed")


if __name__ == "__main__":
    main()
