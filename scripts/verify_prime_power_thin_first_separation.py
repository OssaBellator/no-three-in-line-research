#!/usr/bin/env python3
"""Exact arithmetic checks for CMR294--CMR297."""

from __future__ import annotations

from collections import Counter
from math import ceil


def valuation(n: int, p: int) -> int:
    assert n != 0
    n = abs(n)
    value = 0
    while n % p == 0:
        n //= p
        value += 1
    return value


def signature(d: int, e: int, p: int) -> tuple[int, tuple[int, int]]:
    assert d != 0 and e != 0
    depth = min(valuation(d, p), valuation(e, p))
    x = (d // (p**depth)) % p
    y = (e // (p**depth)) % p
    assert (x, y) != (0, 0)
    if x == 0:
        return depth, (0, 1)
    inverse = pow(x, -1, p)
    return depth, (1, (y * inverse) % p)


def verify_exact_signature_alphabet() -> None:
    cases = ((3, 4), (5, 3), (7, 2), (11, 2))
    for p, max_h in cases:
        for h in range(1, max_h + 1):
            t = p**h
            for d in range(1, t):
                r = valuation(d, p)
                observed = {
                    signature(d, e, p)
                    for e in range(-(t - 1), t)
                    if e != 0
                }
                assert len(observed) <= r + p
                for depth, direction in observed:
                    if depth < r:
                        assert direction == (0, 1)
                    else:
                        assert depth == r
                        assert direction[0] == 1


def verify_pigeonhole_bounds() -> None:
    for p, h in ((3, 4), (5, 3), (7, 2), (11, 2)):
        t = p**h
        for d in range(1, t):
            counts = Counter(
                signature(d, e, p)
                for e in range(1, t - 1)
            )
            if not counts:
                continue
            largest = max(counts.values())
            r = valuation(d, p)
            assert largest >= ceil((t - 2) / (r + p))
            assert ceil((t - 2) / (r + p)) >= ceil(
                (t - 2) / (h + p - 1)
            )


def verify_prefix_scale_lift() -> None:
    for p in (3, 5, 7, 11):
        for s in range(5):
            scale = p**s
            for d in range(1, 30):
                for e in range(-29, 30):
                    if e == 0:
                        continue
                    depth, direction = signature(d, e, p)
                    lifted_depth, lifted_direction = signature(
                        scale * d, scale * e, p
                    )
                    assert lifted_depth == s + depth
                    assert lifted_direction == direction


def verify_width_three_denominator() -> None:
    for p, h in ((3, 4), (5, 3), (7, 2), (11, 2)):
        t = p**h
        if t < 10:
            continue
        for outer_gap in range(1, t):
            r = valuation(outer_gap, p)
            bound = ceil((t - 9) / (r + p))
            uniform = ceil((t - 9) / (h + p - 1))
            assert bound >= uniform


def main() -> None:
    verify_exact_signature_alphabet()
    verify_pigeonhole_bounds()
    verify_prefix_scale_lift()
    verify_width_three_denominator()
    print(
        "verified thin-blocker first-separation signatures: exact alphabets, "
        "pigeonhole bounds, and prefix-scale lifting"
    )


if __name__ == "__main__":
    main()
