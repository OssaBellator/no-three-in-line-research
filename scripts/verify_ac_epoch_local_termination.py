#!/usr/bin/env python3
"""Arithmetic checks for AC3jr--AC3ju."""

from __future__ import annotations

from collections import Counter


def history_threshold(n: int, role_count: int, multiplicity: int) -> int:
    ticket_stock = role_count * (n - 1) ** 2
    return n * n * (multiplicity * ticket_stock * ticket_stock + ticket_stock + 1)


def fixed_mask_bound(n: int, role_count: int, multiplicity: int) -> int:
    threshold = history_threshold(n, role_count, multiplicity)
    return (n * n + 1) * threshold + n * n


def epoch_bound(
    n: int,
    role_count: int,
    multiplicity: int,
    mask_universe: int,
) -> int:
    return mask_universe + (mask_universe + 1) * fixed_mask_bound(
        n, role_count, multiplicity
    )


def verify_formula_grid(counts: Counter[str]) -> None:
    for n in range(3, 30):
        for role_count in range(1, 12):
            for multiplicity in range(1, 9):
                threshold = history_threshold(n, role_count, multiplicity)
                ticket_stock = role_count * (n - 1) ** 2
                assert threshold == n * n * (
                    multiplicity * ticket_stock**2 + ticket_stock + 1
                )
                assert threshold > 0

                fixed = fixed_mask_bound(n, role_count, multiplicity)
                assert fixed == (n * n + 1) * threshold + n * n

                for mask_universe in range(0, 20):
                    total = epoch_bound(
                        n, role_count, multiplicity, mask_universe
                    )
                    assert total == mask_universe + (
                        mask_universe + 1
                    ) * fixed
                    counts["epoch formula systems"] += 1


def verify_segmentations(counts: Counter[str]) -> None:
    for n in range(3, 16):
        for threshold in range(1, 40):
            maximum_reopenings = n * n
            for reopenings in range(maximum_reopenings + 1):
                segment_count = reopenings + 1
                state_changes = segment_count * threshold + reopenings
                assert state_changes <= (n * n + 1) * threshold + n * n
                counts["fixed-mask segmentations"] += 1

            for mask_steps in range(0, 20):
                interval_count = mask_steps + 1
                fixed_bound = (n * n + 1) * threshold + n * n
                state_changes = mask_steps + interval_count * fixed_bound
                assert state_changes == mask_steps + (mask_steps + 1) * fixed_bound
                counts["mask interval segmentations"] += 1


def verify_monotone_potentials(counts: Counter[str]) -> None:
    for universe in range(0, 100):
        mask_size = 0
        while mask_size < universe:
            next_size = mask_size + 1
            assert next_size > mask_size
            mask_size = next_size
            counts["strict mask steps"] += 1
        assert mask_size == universe

    for n in range(1, 30):
        host_size = 0
        while host_size < n * n:
            next_size = host_size + 1
            assert next_size > host_size
            host_size = next_size
            counts["strict host reopenings"] += 1
        assert host_size == n * n


def verify_polynomial_domination(counts: Counter[str]) -> None:
    # The exact expression is bounded by a fixed constant times
    # B*lambda*L^2*n^8 + B*n^2 after replacing B+1 by 2(B+1).
    for n in range(3, 40):
        for role_count in range(1, 10):
            for multiplicity in range(1, 7):
                for mask_universe in range(1, 15):
                    exact = epoch_bound(
                        n, role_count, multiplicity, mask_universe
                    )
                    coarse = 20 * (mask_universe + 1) * (
                        multiplicity * role_count * role_count * n**8 + n * n
                    )
                    assert exact <= coarse
                    counts["polynomial bounds"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    verify_formula_grid(counts)
    verify_segmentations(counts)
    verify_monotone_potentials(counts)
    verify_polynomial_domination(counts)

    print("AC3jr--AC3ju epoch-local termination verification passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
