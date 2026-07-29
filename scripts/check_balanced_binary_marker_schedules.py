#!/usr/bin/env python3
from fractions import Fraction
from itertools import product

# Policy p=(1/2,1/3,1/6) realized by a binary routing tree.
# Root sends left (A) with 1/2; the right child sends B with 2/3 and C with 1/3.
P = (Fraction(1, 2), Fraction(1, 3), Fraction(1, 6))
DEPTH = (1, 2, 2)


def mechanical_bit(n: int, alpha: Fraction) -> int:
    """Increment of floor(n*alpha), n starts at 1."""
    return (n * alpha).numerator // (n * alpha).denominator - (((n - 1) * alpha).numerator // ((n - 1) * alpha).denominator)


def schedule(length: int):
    root_visits = 0
    right_visits = 0
    out = []
    for _ in range(length):
        root_visits += 1
        if mechanical_bit(root_visits, Fraction(1, 2)):
            out.append(0)
        else:
            right_visits += 1
            if mechanical_bit(right_visits, Fraction(2, 3)):
                out.append(1)
            else:
                out.append(2)
    return out


def discrepancies(word):
    counts = [0, 0, 0]
    maxima = [Fraction(0), Fraction(0), Fraction(0)]
    for n, a in enumerate(word, 1):
        counts[a] += 1
        for i in range(3):
            d = abs(Fraction(counts[i]) - n * P[i])
            maxima[i] = max(maxima[i], d)
            assert d <= DEPTH[i]
    return tuple(maxima)


# Two independently scheduled marker states may be interleaved arbitrarily.
# Every global observable discrepancy is the sum of the two local discrepancies.
W0 = schedule(31)
W1 = schedule(31)
maxima0 = discrepancies(W0)
maxima1 = discrepancies(W1)

# Exhaust every interleaving length pair through 30 occurrences per state.
observable = (Fraction(2), Fraction(-1), Fraction(3))
bound_one_state = sum(abs(observable[i]) * DEPTH[i] for i in range(3))
max_global = Fraction(0)
for n0, n1 in product(range(31), repeat=2):
    counts = [0, 0, 0]
    for a in W0[:n0] + W1[:n1]:
        counts[a] += 1
    expected_n = n0 + n1
    discrepancy = abs(sum(observable[i] * (Fraction(counts[i]) - expected_n * P[i]) for i in range(3)))
    max_global = max(max_global, discrepancy)
    assert discrepancy <= 2 * bound_one_state

period = schedule(6)
assert period.count(0) == 3 and period.count(1) == 2 and period.count(2) == 1
assert schedule(12) == period + period

print({
    "period": period,
    "leaf_prefix_discrepancies": maxima0,
    "interleavings_checked": 31 * 31,
    "max_global_observable_discrepancy": max_global,
    "certified_global_bound": 2 * bound_one_state,
})
