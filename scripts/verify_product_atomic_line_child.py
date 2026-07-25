#!/usr/bin/env python3
"""Finite verifier for PX323--PX326."""

from itertools import product
from math import ceil
import random


def admissible_partners(matrix, r):
    m = len(matrix)
    return [
        s for s in range(m)
        if s != r and not matrix[r][s] and not matrix[s][r]
    ]


def check_matrix(matrix):
    m = len(matrix)
    row_deg = [sum(row) for row in matrix]
    col_deg = [sum(matrix[r][c] for r in range(m)) for c in range(m)]
    delta = max(row_deg + col_deg, default=0)
    for r in range(m):
        a = len(admissible_partners(matrix, r))
        assert a >= m - 1 - 2 * delta
        if m >= 2 * delta + 2:
            assert a >= 1


def exhaustive_graphs():
    for m in range(1, 5):
        off = [(r, c) for r in range(m) for c in range(m) if r != c]
        for bits in product((0, 1), repeat=len(off)):
            matrix = [[False] * m for _ in range(m)]
            for i in range(m):
                matrix[i][i] = True
            for (r, c), bit in zip(off, bits):
                matrix[r][c] = bool(bit)
            check_matrix(matrix)


def random_graphs():
    rng = random.Random(20260725)
    for m in range(5, 11):
        for _ in range(500):
            p = rng.random() * 0.6
            matrix = [[False] * m for _ in range(m)]
            for r in range(m):
                for c in range(m):
                    matrix[r][c] = (r == c) or (rng.random() < p)
            check_matrix(matrix)


def atomic_ledgers():
    for K in range(1, 9):
        for d in range(1, 25):
            for mu1 in range(25):
                for mu2 in range(25):
                    for lam in range(25):
                        c = mu1 + mu2 + lam
                        if d > c:
                            assert -d + c < 0
                        else:
                            q = ceil(d / 3)
                            assert max(mu1, mu2, lam) >= q
                            if max(mu1, mu2) >= q:
                                assert ceil(max(mu1, mu2) / K) >= ceil(d / (3 * K))
                            else:
                                assert lam + 2 >= ceil(d / 3) + 2


if __name__ == "__main__":
    exhaustive_graphs()
    random_graphs()
    atomic_ledgers()
    print("PX323--PX326 verified")
