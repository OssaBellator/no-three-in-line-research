#!/usr/bin/env python3
from fractions import Fraction
from itertools import product

# Symmetric two-syndrome kernels with exact Dobrushin factors.
KERNELS = {
    "A": ((Fraction(3, 4), Fraction(1, 4)),
          (Fraction(1, 4), Fraction(3, 4))),  # tau=1/2
    "B": ((Fraction(7, 8), Fraction(1, 8)),
          (Fraction(1, 8), Fraction(7, 8))),  # tau=3/4
}
TAU = {"A": Fraction(1, 2), "B": Fraction(3, 4)}
TARGET = Fraction(1, 100)
MAX_N = 20


def allowed(word: str) -> bool:
    return "BB" not in word


def step(v, matrix):
    return tuple(sum(v[i] * matrix[i][j] for i in range(2)) for j in range(2))

worst = {}
worst_words = {}
for n in range(1, MAX_N + 1):
    candidates = []
    for letters in product("AB", repeat=n):
        word = "".join(letters)
        if not allowed(word):
            continue
        v = (Fraction(1), Fraction(0))
        tau_product = Fraction(1)
        for letter in word:
            v = step(v, KERNELS[letter])
            tau_product *= TAU[letter]
        deviation = abs(v[0] - Fraction(1, 2))
        assert deviation == Fraction(1, 2) * tau_product
        candidates.append((deviation, word, v))
    max_dev = max(x[0] for x in candidates)
    words = sorted(x[1] for x in candidates if x[0] == max_dev)
    worst[n] = max_dev
    worst_words[n] = words
    expected = Fraction(1, 2) * TAU["B"] ** ((n + 1) // 2) * TAU["A"] ** (n // 2)
    assert max_dev == expected
    expected_word = (("BA" * ((n + 1) // 2))[:n] if n % 2 else ("AB" * (n // 2)))
    assert words[0] == expected_word

horizon = next(n for n in range(1, MAX_N + 1) if worst[n] <= TARGET)
assert horizon == 8
assert worst[7] == Fraction(81, 4096)
assert worst[8] == Fraction(81, 8192)

DEGREE = 20
load = (Fraction(1, 2) + worst[horizon]) / DEGREE
assert load == Fraction(4177, 163840)

print({
    "automaton": "forbid BB",
    "kernel_factors": {k: str(v) for k, v in TAU.items()},
    "sharp_horizon": horizon,
    "worst_word": worst_words[horizon][0],
    "worst_deviation": str(worst[horizon]),
    "degree_20_load": str(load),
    "status": "passed",
})
