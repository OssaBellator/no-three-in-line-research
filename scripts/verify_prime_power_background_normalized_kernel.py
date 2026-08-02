#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction
from math import comb, lcm


def choose(number, rank):
    return comb(number, rank) if number >= rank else 0


def profile(background, scale):
    return Fraction(choose(background, 2), scale * scale), Fraction(background, scale), Fraction(1, 1)


def reconstruct(background, response, scale):
    rank_one, rank_two, rank_three = profile(background, scale)
    return scale * scale * response * rank_one + scale * choose(response, 2) * rank_two + choose(response, 3) * rank_three


def kernel(background, response):
    return response * choose(background, 2) + choose(response, 2) * background + choose(response, 3)


common_denominator = 1
for background in range(8):
    for response in range(6):
        reconstructed = []
        for scale in range(1, 6):
            coordinates = profile(background, scale)
            reconstructed.append(reconstruct(background, response, scale))
            assert reconstruct(background, response, scale) == kernel(background, response)
            for value in coordinates:
                common_denominator = lcm(common_denominator, value.denominator)
        assert len(set(reconstructed)) == 1
assert common_denominator > 0
print(f"verified background-normalized kernel common_denominator={common_denominator}")
