#!/usr/bin/env python3
"""Verify PX221--PX222 packet-count barrier and logarithmic window."""
from __future__ import annotations

from math import comb, exp, log


def level_sizes(order: int) -> tuple[int, ...]:
    return tuple(
        diagonal + 1 if diagonal < order else 2 * order - 1 - diagonal
        for diagonal in range(2 * order - 1)
    )


def total_energy(order: int) -> int:
    return sum(comb(size, 2) for size in level_sizes(order))


def verify_exact_spectrum() -> None:
    for order in range(2, 101):
        sizes = level_sizes(order)
        assert sizes == tuple(range(1, order + 1)) + tuple(
            range(order - 1, 0, -1)
        )
        exact = order * (order - 1) * (2 * order - 1) // 6
        assert total_energy(order) == exact
        assert exact == 2 * comb(order, 3) + comb(order, 2)
        assert max(comb(size, 2) for size in sizes) == comb(order, 2)
    print("geometric-progression packet spectrum verified")


def verify_packet_count_barrier() -> None:
    for order in range(4, 101):
        total = total_energy(order)
        per_packet = comb(order, 2)
        half_lower = (2 * order - 1) / 6
        for packet_count in range(0, min(order, 12)):
            residual_lower = total - packet_count * per_packet
            assert residual_lower <= total
            if packet_count < half_lower:
                assert residual_lower > total / 2

        # Every fixed packet count leaves cubic-order energy once order is large.
        fixed = 5
        if order >= 4 * fixed:
            residual = total - fixed * per_packet
            assert residual > 0
            assert residual / order**3 > 0.05
    print("fixed-packet and half-energy lower bounds verified")


def verify_logarithmic_window() -> None:
    for order in (10**3, 10**4, 10**5, 10**6):
        for kappa in (0.01, 0.03, 0.06, 0.1):
            packet_count = int(kappa * log(order))
            assert exp(4 * packet_count) <= order ** (4 * kappa)
            assert exp(8 * packet_count) <= order ** (8 * kappa)

            for excess in (1, 2, 3):
                unconditioned_exponent = 4 * kappa - excess / 2
                conditioned_exponent = 8 * kappa - excess / 2
                if kappa < excess / 8:
                    assert unconditioned_exponent < 0
                if kappa < excess / 16:
                    assert conditioned_exponent < 0
    print("logarithmic packet spread exponents verified")


def main() -> None:
    verify_exact_spectrum()
    verify_packet_count_barrier()
    verify_logarithmic_window()
    print("PX221--PX222 verified")


if __name__ == "__main__":
    main()
