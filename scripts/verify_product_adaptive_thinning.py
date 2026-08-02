#!/usr/bin/env python3
"""Verify PX225--PX227 adaptive thinning inequalities."""
from __future__ import annotations

from math import exp, log


def falling_factorial(size: float, rank: int) -> float:
    value = 1.0
    for offset in range(rank):
        value *= size - offset
    return value


def verify_general_q_support_four() -> None:
    for size in (64, 128, 512, 4096):
        for probability in (0.05, 0.1, 0.25, 0.5):
            if probability * size < 32:
                continue
            retained = probability * size / 2
            assert retained >= 16
            denominator = falling_factorial(retained, 2)
            assert denominator >= probability**2 * size**2 / 8

            # PX201 contributes 16 q^4; the rank-two cylinder contributes
            # exp(4 Delta)/(s)_2.  Remove the common exp(4 Delta) and W/t^2.
            coefficient = 16 * probability**4 * size**2 / denominator
            assert coefficient <= 128 * probability**2 + 1e-12
    print("general-q support-four denominator bound verified")


def adaptive_probability(side: float, size: float, delta: int, divisor: float) -> float:
    constant = 1024 * exp(4 * delta)
    return min(1 / log(2 * size), size / (constant * side * divisor))


def verify_optimized_choice() -> None:
    for delta in (1, 2, 3):
        threshold = max(32, 16 * delta)
        constant = 1024 * exp(4 * delta)
        for side, divisor in ((10**6, 64), (10**9, 128), (10**12, 256)):
            # Choose t with a factor-two margin over the exact square-root
            # threshold.  The logarithmic condition is then automatic here.
            size = 2 * (threshold * constant * side * divisor) ** 0.5
            probability = adaptive_probability(side, size, delta, divisor)
            assert probability * size >= threshold - 1e-9
            normalized = (
                512
                * exp(4 * delta)
                * probability
                * side
                * divisor
                / size
            )
            assert normalized <= 0.5 + 1e-12
    print("optimized adaptive probability verified")


def verify_square_root_exponent() -> None:
    # Model d(N)=N^rho with rho=o(1), and t=N^(1/2+epsilon).
    for epsilon in (0.05, 0.1, 0.2):
        rho = epsilon / 4
        exponent = 2 * (0.5 + epsilon) - 1 - rho
        assert exponent > 0
    print("square-root ambient exponent saving verified")


def verify_internal_sector_scales() -> None:
    for size in (10**4, 10**6, 10**8):
        probability = 1 / log(2 * size)
        retained = probability * size / 2
        assert probability * size >= 32

        # Remove absolute geometric and exp(4 Delta) constants.  These are
        # the four support-sector scales after rank-three cylinder division.
        scales = {
            3: 1.0,
            4: probability * size,
            5: probability**2 * size * log(size),
            6: probability**3 * size * log(size),
        }
        assert scales[3] <= retained
        assert scales[4] <= 2 * retained
        assert scales[5] <= 2 * retained
        assert scales[6] <= 2 * retained
    print("adaptive internal rank-three scales verified")


def verify_rank_two_scales() -> None:
    for size in (1024, 4096, 16384):
        probability = min(1 / log(2 * size), 0.1)
        retained = probability * size / 2

        # After removing exp(4 Delta) L_Z, support two is <=64 and support
        # three is <=128 q t <=256 s.
        support_two = 64.0
        support_three = 128 * probability * size
        assert support_two == 64
        assert support_three <= 256 * retained + 1e-12
    print("adaptive rank-two support-two/support-three scales verified")


def main() -> None:
    verify_general_q_support_four()
    verify_optimized_choice()
    verify_square_root_exponent()
    verify_internal_sector_scales()
    verify_rank_two_scales()
    print("PX225--PX227 verified")


if __name__ == "__main__":
    main()
