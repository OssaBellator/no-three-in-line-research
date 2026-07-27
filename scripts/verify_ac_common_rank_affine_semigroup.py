#!/usr/bin/env python3
"""Finite audit for AC3rp--AC3rt.

The script checks exact common-centre defect multiplication, interleaved bounded-expansion
budgets, zero-multiplier absorption, identity-only quotienting, same-sign translation budgets and
the finite residual classification, including the fact that different-centre involutions belong
to the mixed-centre branch.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from math import floor, gcd, log2
import random


def classify(maps: list[tuple[int, int]]) -> str:
    if all((A, B) == (1, 0) for A, B in maps):
        return "identity_only"

    centre: Fraction | None = None
    common = True
    for A, B in maps:
        if A == 1:
            if B != 0:
                common = False
                break
        else:
            q = Fraction(-B, A - 1)
            if centre is None:
                centre = q
            elif q != centre:
                common = False
                break
    if common and centre is not None:
        return "common_center"
    if all(A == 1 for A, _ in maps):
        signs = {1 if B > 0 else -1 for _, B in maps if B}
        return "same_sign_translation" if len(signs) == 1 else "mixed_sign_translation"
    return "mixed_center"


def main() -> None:
    rng = random.Random(20260727)
    stats: Counter[str] = Counter()
    maps_by_centre: dict[tuple[int, int], list[tuple[int, int]]] = {}

    for d in range(1, 5):
        for a in range(-6, 7):
            if gcd(abs(a), d) != 1:
                continue
            maps: list[tuple[int, int]] = []
            for A in range(-4, 5):
                numerator = (1 - A) * a
                if numerator % d:
                    continue
                B = numerator // d
                maps.append((A, B))
                for h in range(-8, 9):
                    c = d * h - a
                    h_next = A * h + B
                    assert d * h_next - a == A * c
                    stats["one_step_defect_tests"] += 1
            maps_by_centre[(a, d)] = maps

    for (a, d), maps in maps_by_centre.items():
        if not maps:
            continue
        for _ in range(200):
            h0 = rng.randint(-20, 20)
            h = h0
            product_A = 1
            word = [rng.choice(maps) for _ in range(rng.randint(0, 30))]
            for A, B in word:
                h = A * h + B
                product_A *= A
            assert d * h - a == product_A * (d * h0 - a)
            stats["interleaved_words"] += 1
            stats["interleaved_steps"] += len(word)

    for _ in range(20_000):
        c0 = rng.choice([x for x in range(-20, 21) if x])
        C = rng.randint(abs(c0), max(abs(c0), 10_000))
        c = c0
        expansions = 0
        unit_steps = 0
        for _step in range(200):
            A = rng.choice([-3, -2, -1, 1, 2, 3])
            c_next = A * c
            if abs(c_next) > C:
                break
            c = c_next
            if abs(A) >= 2:
                expansions += 1
            else:
                unit_steps += 1
        assert expansions <= floor(log2(C / abs(c0)))
        stats["bounded_defect_systems"] += 1
        stats["expanding_occurrences"] += expansions
        stats["unit_modulus_occurrences"] += unit_steps

    for _ in range(10_000):
        c = rng.randint(-100, 100)
        zero_seen = False
        for A in [rng.choice([-3, -2, -1, 0, 1, 2, 3]) for _ in range(20)]:
            c = A * c
            zero_seen = zero_seen or A == 0
            if zero_seen:
                assert c == 0
        stats["zero_absorption_systems"] += 1

    for sign in (-1, 1):
        for _ in range(20_000):
            increments = [0] + [sign * rng.randint(1, 8) for _ in range(rng.randint(1, 6))]
            b_min = min(abs(B) for B in increments if B)
            L = rng.randint(-50, 0)
            U = rng.randint(0, 80)
            h = rng.randint(L, U)
            nonidentity = 0
            for _step in range(200):
                B = rng.choice(increments)
                h_next = h + B
                if not L <= h_next <= U:
                    break
                h = h_next
                nonidentity += B != 0
            assert nonidentity <= floor((U - L) / b_min)
            stats["translation_systems"] += 1
            stats["translation_moves"] += nonidentity

    samples = [
        [(1, 0), (1, 0)],
        [(2, -1), (-1, 2)],
        [(1, 2), (1, 5)],
        [(1, 2), (1, -3)],
        [(0, 4), (-1, 8), (1, 0)],
        [(2, 0), (3, 1)],
        [(-1, 2), (-1, 6)],
        [(0, 0), (-1, 2), (-1, 6)],
    ]
    expected = [
        "identity_only",
        "common_center",
        "same_sign_translation",
        "mixed_sign_translation",
        "common_center",
        "mixed_center",
        "mixed_center",
        "mixed_center",
    ]
    for maps, want in zip(samples, expected):
        got = classify(maps)
        assert got == want, (maps, got, want)
        stats[f"classified_{got}"] += 1

    h = 7
    first = -h + 2
    second = -first + 6
    assert second == h + 4
    stats["distinct_centre_involution_compositions"] += 1

    print("AC common-rank affine semigroup audit passed")
    for key in sorted(stats):
        print(f"{key}: {stats[key]}")


if __name__ == "__main__":
    main()
