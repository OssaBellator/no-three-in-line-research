#!/usr/bin/env python3
"""Verify PX232--PX234 optimized bounded-forbidden spread constants."""
from __future__ import annotations

from math import exp, log


def spread_constant(order: int, delta: int) -> float:
    witness = 1 / (order - 4 * delta)
    return (1 - witness) ** (-delta * order)


def verify_witness() -> None:
    for delta in range(1, 12):
        for order in range(8 * delta, 20 * delta + 1):
            witness = 1 / (order - 4 * delta)
            lhs = witness * (1 - witness) ** (2 * delta)
            assert lhs + 1e-15 >= 1 / order
    print("optimized LLL witness verified")


def verify_density_envelope() -> None:
    for delta in range(1, 12):
        previous = None
        for order in range(8 * delta, 200 * delta + 1):
            constant = spread_constant(order, delta)
            if order >= 8 * delta + 2:
                assert constant <= exp(2 * delta) + 1e-10
            if previous is not None:
                # The exact factor decreases toward e^Delta.
                assert constant <= previous + 1e-12
            previous = constant
        limiting_ratio = spread_constant(10**6 * delta, delta) / exp(delta)
        assert limiting_ratio < 1.001
    print("density envelope and e^Delta limit verified")


def verify_conditioned_orders() -> None:
    for delta in (1, 2, 3):
        for original in (128, 256, 512):
            for exposed in range(0, 25):
                residual = original - exposed
                if residual < 8 * delta:
                    continue
                constant = spread_constant(residual, delta)
                assert constant >= 1
                if residual >= 8 * delta + 2:
                    assert constant <= exp(2 * delta) + 1e-10
    print("conditioned residual constants verified")


def verify_adaptive_substitution() -> None:
    for delta in (1, 2, 3):
        for side, divisor in ((10**6, 64), (10**9, 128), (10**12, 256)):
            threshold = max(32, 16 * delta + 4)
            coefficient = 1024 * exp(2 * delta)
            size = 2 * (threshold * coefficient * side * divisor) ** 0.5
            probability = min(
                1 / log(2 * size),
                size / (coefficient * side * divisor),
            )
            retained = probability * size / 2
            assert retained >= 8 * delta + 2
            normalized = (
                512
                * exp(2 * delta)
                * probability
                * side
                * divisor
                / size
            )
            assert normalized <= 0.5 + 1e-12
    print("adaptive e^(2Delta) substitution verified")


def verify_small_sector_substitution() -> None:
    for delta in (1, 2, 3):
        for order in (8 * delta + 2, 64, 128):
            if order < 8 * delta + 2:
                continue
            constant = spread_constant(order, delta)
            assert constant <= exp(2 * delta) + 1e-10
            transposition = constant / 2
            cycle = constant / 3
            path = constant * (order - 2)
            assert transposition <= exp(2 * delta) / 2 + 1e-10
            assert cycle <= exp(2 * delta) / 3 + 1e-10
            assert path <= exp(2 * delta) * (order - 2) + 1e-10
    print("small-sector constant substitutions verified")


def main() -> None:
    verify_witness()
    verify_density_envelope()
    verify_conditioned_orders()
    verify_adaptive_substitution()
    verify_small_sector_substitution()
    print("PX232--PX234 verified")


if __name__ == "__main__":
    main()
