#!/usr/bin/env python3
from fractions import Fraction
from itertools import product

A = ((3, 1, 0), (0, 3, 1), (1, 0, 3))
B = ((3, 1, 0), (1, 0, 3), (0, 3, 1))
KERNELS = (A, B)
D = 4
TARGET = Fraction(1, 40)
MAX_M = 12


def matmul(X, Y):
    return tuple(tuple(sum(X[i][k] * Y[k][j] for k in range(len(Y)))
                       for j in range(len(Y[0]))) for i in range(len(X)))


def vecmul(v, M):
    return tuple(sum(v[i] * M[i][j] for i in range(len(v)))
                 for j in range(len(M[0])))


def dobrushin(M):
    rows = len(M)
    return max(Fraction(sum(abs(M[i][j] - M[k][j]) for j in range(len(M[0]))), 2 * D)
               for i in range(rows) for k in range(rows))


assert matmul(A, B) != matmul(B, A)
for M in KERNELS:
    assert all(sum(row) == D for row in M)
    assert all(sum(M[i][j] for i in range(3)) == D for j in range(3))
    assert dobrushin(M) == Fraction(3, 4)

max_deviation = {}
witness = {}
max_vector = {}
for m in range(1, MAX_M + 1):
    best = Fraction(-1)
    best_word = None
    best_vec = None
    for word in product(range(2), repeat=m):
        v = (1, 0, 0)
        for bit in word:
            v = vecmul(v, KERNELS[bit])
        total = D ** m
        dev = max(abs(Fraction(x, total) - Fraction(1, 3)) for x in v)
        tv = sum(abs(Fraction(x, total) - Fraction(1, 3)) for x in v) / 2
        assert dev == tv
        if dev > best:
            best, best_word, best_vec = dev, word, v
    max_deviation[m] = best
    witness[m] = best_word
    max_vector[m] = best_vec

assert max_deviation[7] == Fraction(1813, 49152)
assert max_deviation[8] == Fraction(2401, 98304)
assert max_deviation[7] > TARGET
assert max_deviation[8] <= TARGET
for m in range(8, MAX_M + 1):
    assert max_deviation[m] <= TARGET

assert max(max_vector[8]) == 23446
exact_load = Fraction(max(max_vector[8]), D ** 8 * 16)
assert exact_load == Fraction(11723, 524288)

print({
    "switch_words_checked": sum(2 ** m for m in range(1, MAX_M + 1)),
    "noncommuting": True,
    "common_dobrushin_factor": "3/4",
    "sharp_target": "1/40",
    "sharp_horizon_blocks": 8,
    "worst_deviation_at_8": str(max_deviation[8]),
    "degree_16_load": str(exact_load),
    "status": "passed",
})
