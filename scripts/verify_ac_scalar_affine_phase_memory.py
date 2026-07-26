#!/usr/bin/env python3
"""Finite audit for scalar-affine memory on zero-surplus phase cycles."""

from __future__ import annotations

from itertools import product
from math import comb
from random import Random


def compose(maps: list[tuple[int, int]]) -> tuple[int, int]:
    """Return (A,B) for applying maps h -> a*h+b in listed order."""
    A, B = 1, 0
    for a, b in maps:
        A, B = a * A, a * B + b
    return A, B


def apply_map(A: int, B: int, h: int) -> int:
    return A * h + B


def iterate_formula(A: int, B: int, h: int, n: int) -> int:
    if n == 0:
        return h
    if A == 1:
        return h + n * B
    return (A**n) * h + B * ((A**n - 1) // (A - 1))


def exhaustive_word_composition() -> int:
    tested = 0
    alphabet = [(-2, -1), (-1, 2), (0, -2), (1, -1), (1, 0), (2, 1)]
    for length in range(1, 6):
        for maps in product(alphabet, repeat=length):
            A, B = compose(list(maps))
            for h in range(-5, 6):
                direct = h
                for a, b in maps:
                    direct = a * direct + b
                assert direct == apply_map(A, B, h)
                for n in range(7):
                    x = h
                    for _ in range(n):
                        x = apply_map(A, B, x)
                    assert x == iterate_formula(A, B, h, n)
                    tested += 1
    return tested


def finite_order_cases() -> int:
    tested = 0
    for B in range(-7, 8):
        for h in range(-12, 13):
            f = apply_map(0, B, h)
            assert apply_map(0, B, f) == f
            assert apply_map(-1, B, apply_map(-1, B, h)) == h
            assert apply_map(1, 0, h) == h
            tested += 3
    return tested


def translation_and_expansion_checks() -> tuple[int, int]:
    translations = 0
    expansions = 0
    for B in range(-5, 6):
        if B == 0:
            continue
        for L in range(-8, 2):
            for U in range(max(L, -1), 9):
                width = U - L
                bound = width // abs(B)
                for h in range(L, U + 1):
                    n = 0
                    x = h
                    while L <= x + B <= U:
                        x += B
                        n += 1
                    assert n <= bound
                    translations += 1

    for A in list(range(-4, -1)) + list(range(2, 5)):
        for B in range(-4, 5):
            for h in range(-8, 9):
                c = (A - 1) * h + B
                h2 = apply_map(A, B, h)
                c2 = (A - 1) * h2 + B
                assert c2 == A * c
                if c == 0:
                    assert h2 == h
                else:
                    assert abs(c2) >= 2 * abs(c)
                expansions += 1
    return translations, expansions


def random_cycle_addresses(seed: int = 20260727, systems: int = 50000) -> tuple[int, int]:
    rng = Random(seed)
    addresses = 0
    state_stock_checks = 0
    for _ in range(systems):
        m = rng.randint(1, 7)
        Bstock = rng.randint(0, 9)
        q = rng.randint(1, 8)
        n_occ = comb(Bstock + m - 1, m - 1)
        assert n_occ >= 1
        n_phase = q * n_occ
        assert n_phase >= q
        state_stock_checks += 1

        length = rng.randint(1, min(12, n_phase))
        maps = [(rng.randint(-2, 2), rng.randint(-5, 5)) for _ in range(length)]
        A, Bb = compose(maps)
        h = rng.randint(-100, 100)
        direct = h
        for a, b in maps:
            direct = a * direct + b
        assert direct == A * h + Bb

        assert A in (-1, 0, 1) or abs(A) >= 2
        if A == 1 and Bb == 0:
            assert direct == h
        elif A == 0:
            assert apply_map(A, Bb, direct) == direct
        elif A == -1:
            assert apply_map(A, Bb, direct) == h
        elif A == 1:
            assert direct - h == Bb
        else:
            c = (A - 1) * h + Bb
            c2 = (A - 1) * direct + Bb
            assert c2 == A * c
        addresses += 1
    return addresses, state_stock_checks


def main() -> None:
    exhaustive = exhaustive_word_composition()
    finite = finite_order_cases()
    translations, expansions = translation_and_expansion_checks()
    addresses, stock = random_cycle_addresses()
    print("scalar-affine phase-memory audit passed")
    print(f"  exhaustive iterate identities: {exhaustive}")
    print(f"  finite-order checks: {finite}")
    print(f"  bounded translation chains: {translations}")
    print(f"  expanding-defect checks: {expansions}")
    print(f"  random cycle addresses: {addresses}")
    print(f"  phase-state stock checks: {stock}")


if __name__ == "__main__":
    main()
