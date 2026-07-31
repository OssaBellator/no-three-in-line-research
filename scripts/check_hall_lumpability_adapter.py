#!/usr/bin/env python3
from fractions import Fraction
from itertools import product

A = ((3, 1, 0), (0, 3, 1), (1, 0, 3))
B = ((3, 1, 0), (1, 0, 3), (0, 3, 1))
QUOTIENTS = (A, B)
FIBRES = ((0, 1), (2, 3), (4, 5))


def balanced_block(k):
    hi = (k + 1) // 2
    lo = k // 2
    return ((hi, lo), (lo, hi))


def microscopic(kernel):
    matrix = [[0] * 6 for _ in range(6)]
    for i in range(3):
        for j in range(3):
            block = balanced_block(kernel[i][j])
            for u in range(2):
                for v in range(2):
                    matrix[2 * i + u][2 * j + v] = block[u][v]
    return tuple(tuple(row) for row in matrix)


def multiply(vector, matrix):
    return [sum(vector[i] * matrix[i][j] for i in range(len(vector))) for j in range(len(matrix[0]))]


def aggregate(vector):
    return [sum(vector[s] for s in fibre) for fibre in FIBRES]


def tv_distance(counts, total):
    return sum(abs(Fraction(c, total) - Fraction(1, 3)) for c in counts) / 2


MICRO = tuple(microscopic(kernel) for kernel in QUOTIENTS)
for kernel, micro in zip(QUOTIENTS, MICRO):
    assert all(sum(row) == 4 for row in micro)
    assert all(sum(micro[i][j] for i in range(6)) == 4 for j in range(6))
    for syndrome, fibre in enumerate(FIBRES):
        for state in fibre:
            for target, target_fibre in enumerate(FIBRES):
                assert sum(micro[state][u] for u in target_fibre) == kernel[syndrome][target]

# Exact microscopic-to-quotient commutation for every switch word through length ten.
words_checked = 0
for length in range(11):
    for word in product(range(2), repeat=length):
        for start_state in range(6):
            micro_vector = [0] * 6
            micro_vector[start_state] = 1
            quotient_vector = [0] * 3
            quotient_vector[start_state // 2] = 1
            for symbol in word:
                micro_vector = multiply(micro_vector, MICRO[symbol])
                quotient_vector = multiply(quotient_vector, QUOTIENTS[symbol])
            assert aggregate(micro_vector) == quotient_vector
        words_checked += 1

worst = {}
for length in (7, 8):
    best = Fraction(-1)
    witness = None
    for start in range(3):
        for word in product(range(2), repeat=length):
            vector = [0, 0, 0]
            vector[start] = 1
            for symbol in word:
                vector = multiply(vector, QUOTIENTS[symbol])
            deviation = tv_distance(vector, 4 ** length)
            if deviation > best:
                best = deviation
                witness = (start, word, tuple(vector))
    worst[length] = (best, witness)

assert worst[7][0] == Fraction(1813, 49152)
assert worst[8][0] == Fraction(2401, 98304)
assert max(worst[8][1][2]) == 23446
reverse_load = Fraction(23446, 4 ** 8 * 16)
assert reverse_load == Fraction(11723, 524288)

print({
    "microscopic_states": 6,
    "syndrome_classes": 3,
    "switch_words_checked": words_checked,
    "sharp_horizon": 8,
    "worst_deviation_at_8": str(worst[8][0]),
    "reverse_load_degree_16": str(reverse_load),
    "status": "passed",
})
