#!/usr/bin/env python3
"""Finite verifier for PX334--PX337."""

from itertools import product
import random


def partners(matrix, q):
    n = len(matrix)
    return [
        r for r in range(n)
        if r != q and not matrix[q][r] and not matrix[r][q]
    ]


def check_aux(matrix):
    n = len(matrix)
    row = [sum(x for x in matrix[r]) for r in range(n)]
    col = [sum(matrix[r][c] for r in range(n)) for c in range(n)]
    delta = max(row + col, default=0)
    for q in range(n):
        p = partners(matrix, q)
        assert len(p) >= n - 1 - 2 * delta
        if n >= 2 * delta + 3:
            assert len(p) >= 2
            for collision in p:
                safe = [r for r in p if r != collision]
                assert safe


def exhaustive():
    primary_states = [(0, 1), (1, 0)]
    for a, b in primary_states:
        assert a != b

    for n in range(1, 5):
        off = [(r, c) for r in range(n) for c in range(n) if r != c]
        for bits in product((0, 1), repeat=len(off)):
            matrix = [[False] * n for _ in range(n)]
            for i in range(n):
                matrix[i][i] = True
            for (r, c), bit in zip(off, bits):
                matrix[r][c] = bool(bit)
            check_aux(matrix)


def random_checks():
    rng = random.Random(143337)
    for n in range(5, 11):
        for _ in range(1000):
            p = rng.random() * 0.5
            matrix = [[False] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    matrix[r][c] = (r == c) or (rng.random() < p)
            check_aux(matrix)


if __name__ == "__main__":
    exhaustive()
    random_checks()
    print("PX334--PX337 verified")
