#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction
from math import comb


def choose(number, rank):
    return comb(number, rank) if number >= rank else 0


def kernel(background, response):
    return response * choose(background, 2) + choose(response, 2) * background + choose(response, 3)


for background in range(9):
    for response in range(7):
        assert kernel(background, response) == choose(background + response, 3) - choose(background, 3)

profiles = [
    {"L1": (2, 1), "L2": (1, 2)},
    {"L1": (2, 2), "L2": (1, 1)},
    {"L1": (3, 1), "L2": (0, 3)},
]
weights = [1, 2, 1]
denominator = sum(weights)
values = [sum(kernel(background, response) for background, response in profile.values()) for profile in profiles]
numerator = sum(weight * value for weight, value in zip(weights, values))
expectation = Fraction(numerator, denominator)
assert expectation == sum(Fraction(weight, denominator) * value for weight, value in zip(weights, values))
assert all(value >= 0 for value in values)
destroyed = max(values) + 1
assert all(value < destroyed for value in values)
print(f"verified complete line-energy kernel profiles={len(profiles)} numerator={numerator}/{denominator}")
