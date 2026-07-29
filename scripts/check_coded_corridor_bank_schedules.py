#!/usr/bin/env python3
"""Exact checks for docs/426 coded corridor-bank schedules."""

from collections import Counter
from fractions import Fraction
import json
from math import ceil


def frac(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}"


K = 7
banks = tuple(range(K))


def balanced_codes(base, length):
    capacity = base ** length
    return {i: i % capacity for i in banks}


def combined_load(codes, q):
    counts = Counter(codes.values())
    return Fraction(max(counts.values()), q), max(counts.values())


q = 3
codes_len2 = balanced_codes(2, 2)
load_len2, ambiguity_len2 = combined_load(codes_len2, q)
assert ambiguity_len2 == ceil(K / 4) == 2
assert load_len2 == Fraction(2, 3)

codes_len3 = balanced_codes(2, 3)
load_len3, ambiguity_len3 = combined_load(codes_len3, q)
assert ambiguity_len3 == ceil(K / 8) == 1
assert load_len3 == Fraction(1, 3)

p = Fraction(2, 3)
conditioned_load = Fraction(ambiguity_len2, 2)
conditioned_bound = Fraction(ambiguity_len2, q) / p
assert conditioned_load == conditioned_bound == Fraction(1, 1)

assert ambiguity_len2 >= ceil(K / (2 ** 2))
assert ambiguity_len3 >= ceil(K / (2 ** 3))

print(json.dumps({
    "all_checks_passed": True,
    "banks": K,
    "alphabet_size": 2,
    "length_2_ambiguity": ambiguity_len2,
    "length_2_load": frac(load_len2),
    "length_3_ambiguity": ambiguity_len3,
    "length_3_load": frac(load_len3),
    "retained_density": frac(p),
    "conditioned_length_2_load": frac(conditioned_load),
}, indent=2))
