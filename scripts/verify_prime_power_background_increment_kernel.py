#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction
from math import comb


def choose(number, rank):
    return comb(number, rank) if number >= rank else 0


def kernel(background, response):
    return response * choose(background, 2) + choose(response, 2) * background + choose(response, 3)


def increment(background, response):
    return response * background + choose(response, 2)


for background in range(10):
    for response in range(7):
        assert kernel(background + 1, response) - kernel(background, response) == increment(background, response)
        assert increment(background, response) >= 0
        assert increment(background, response) == response * background + choose(response, 2) + 0

for initial in range(5):
    for steps in range(6):
        for response in range(5):
            assert sum(increment(background, response) for background in range(initial, initial + steps)) == kernel(initial + steps, response) - kernel(initial, response)

weighted = [(Fraction(1, 3), increment(2, 3)), (Fraction(2, 5), increment(4, 2))]
assert sum(weight * value for weight, value in weighted) == Fraction(1, 3) * 9 + Fraction(2, 5) * 9
print("verified background increment kernel identities=420")
