#!/usr/bin/env python3
"""Verify primitive-direction root windows for real hyperbola incidences."""
from __future__ import annotations

import argparse
from collections import defaultdict
from itertools import combinations
from math import gcd, isqrt

Point = tuple[int, int]
Direction = tuple[int, int]


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n) + 1, 2))


def inv(x: int, p: int) -> int:
    if x % p == 0:
        raise ZeroDivisionError("zero has no inverse modulo p")
    return pow(x, p - 2, p)


def point(channel: int, x: int, p: int) -> Point:
    return x, channel * inv(x, p) % p


def collinear(a: Point, b: Point, c: Point) -> bool:
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])


def primitive_step(anchor: Point, target: Point) -> tuple[Direction, int]:
    dx = target[0] - anchor[0]
    dy = target[1] - anchor[1]
    g = gcd(abs(dx), abs(dy))
    if g == 0:
        raise ValueError("anchor and target must be distinct")
    r, s, t = dx // g, dy // g, g
    if r < 0 or (r == 0 and s < 0):
        r, s, t = -r, -s, -t
    return (r, s), t


def feasible_steps(anchor: Point, direction: Direction, p: int) -> list[int]:
    z, w = anchor
    r, s = direction
    return [
        t
        for t in range(-(p - 2), p - 1)
        if 1 <= z + t * r <= p - 1 and 1 <= w + t * s <= p - 1
    ]


def channel_word(channel: int, anchor: Point, direction: Direction, t: int, p: int) -> int:
    z, w = anchor
    r, s = direction
    return (channel + (z * s + w * r) * t + r * s * t * t) % p


def check_pair(p: int, source_channel: int, anchor_channel: int) -> tuple[float, int]:
    source = {x: point(source_channel, x, p) for x in range(1, p)}
    counts: list[int] = []

    for z in range(1, p):
        anchor = point(anchor_channel, z, p)
        groups: dict[Direction, list[int]] = defaultdict(list)
        for target in source.values():
            direction, t = primitive_step(anchor, target)
            groups[direction].append(t)
            assert channel_word(anchor_channel, anchor, direction, t, p) == source_channel

        root_window_secants = 0
        for direction, observed in groups.items():
            interval = feasible_steps(anchor, direction, p)
            assert len(interval) < p
            height = max(abs(direction[0]), abs(direction[1]))
            assert sum(t != 0 for t in interval) <= (p - 2) // height
            predicted = [
                t
                for t in interval
                if t != 0
                and channel_word(anchor_channel, anchor, direction, t, p) == source_channel
            ]
            assert sorted(predicted) == sorted(observed)
            assert len(observed) <= 2
            root_window_secants += len(observed) == 2

        brute = sum(
            collinear(source[x], source[u], anchor)
            for x, u in combinations(range(1, p), 2)
        )
        assert root_window_secants == brute
        counts.append(root_window_secants)

    return sum(counts) / len(counts), max(counts)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, default=17)
    parser.add_argument("--a", type=int, default=1)
    parser.add_argument("--b", type=int, default=3)
    parser.add_argument("--all-pairs", action="store_true")
    args = parser.parse_args()

    p = args.prime
    if not is_prime(p) or p == 2:
        parser.error("--prime must be an odd prime")
    a, b = args.a % p, args.b % p
    if a == 0 or b == 0 or a == b:
        parser.error("--a and --b must be distinct nonzero residues")

    pairs = (
        [(x, y) for x in range(1, p) for y in range(1, p) if x != y]
        if args.all_pairs
        else [(a, b)]
    )
    global_max = 0
    for source_channel, anchor_channel in pairs:
        average, maximum = check_pair(p, source_channel, anchor_channel)
        global_max = max(global_max, maximum)
        if not args.all_pairs:
            print(
                f"p={p}, source={source_channel}, anchor={anchor_channel}: "
                f"average real secants={average:.3f}, max={maximum}"
            )
    if args.all_pairs:
        print(
            f"p={p}: all {len(pairs)} ordered channel pairs passed; "
            f"global max real secants per anchor={global_max}"
        )


if __name__ == "__main__":
    main()
