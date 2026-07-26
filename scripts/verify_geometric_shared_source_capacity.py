#!/usr/bin/env python3
"""Finite checks for GC2s--GC2v."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import product


def verify_private_allocation(counts: Counter[str], limit: int = 75_000) -> None:
    for rank in range(1, 4):
        for partner_count in range(1, 5):
            for factor_count in range(1, 5):
                nonempty_masks = tuple(range(1, 1 << factor_count))
                for incidence_masks in product(nonempty_masks, repeat=partner_count):
                    factor_degrees = [
                        sum(
                            (incidence_masks[partner] >> factor) & 1
                            for partner in range(partner_count)
                        )
                        for factor in range(factor_count)
                    ]
                    if max(factor_degrees) > rank:
                        continue
                    for capacities in product((1, 2), repeat=factor_count):
                        private_capacity = [
                            sum(
                                capacities[factor]
                                for factor in range(factor_count)
                                if (incidence_masks[partner] >> factor) & 1
                            )
                            for partner in range(partner_count)
                        ]
                        for kappa in (1, 2):
                            weights = [
                                kappa * private_capacity[partner]
                                for partner in range(partner_count)
                            ]
                            loads = [Fraction(0) for _ in range(factor_count)]
                            sent = Fraction(0)
                            for partner in range(partner_count):
                                for factor in range(factor_count):
                                    if not ((incidence_masks[partner] >> factor) & 1):
                                        continue
                                    payment = Fraction(
                                        weights[partner] * capacities[factor],
                                        rank * kappa * private_capacity[partner],
                                    )
                                    loads[factor] += payment
                                    sent += payment
                            assert all(
                                loads[factor] <= capacities[factor]
                                for factor in range(factor_count)
                            )
                            assert sent == Fraction(sum(weights), rank * kappa)
                            counts["aggregate private systems"] += 1
                            if counts["aggregate private systems"] >= limit:
                                return


def verify_target_pool(counts: Counter[str], limit: int = 125_000) -> None:
    for factor_count in range(1, 6):
        for capacities in product((1, 2, 3), repeat=factor_count):
            target_capacity = sum(capacities)
            for partner_count in range(1, 6):
                for weights in product((0, 1, 2), repeat=partner_count):
                    total = sum(weights)
                    if total == 0:
                        continue
                    for kappa in (1, 2, 3):
                        if total > kappa * target_capacity:
                            continue
                        loads = [
                            Fraction(total * capacity, kappa * target_capacity)
                            for capacity in capacities
                        ]
                        assert all(
                            loads[factor] <= capacities[factor]
                            for factor in range(factor_count)
                        )
                        assert sum(loads) == Fraction(total, kappa)
                        counts["shared target systems"] += 1
                        if counts["shared target systems"] >= limit:
                            return


def verify_four_way_router(counts: Counter[str]) -> None:
    for weights in product(range(6), repeat=4):
        total = sum(weights)
        if total == 0:
            continue
        assert max(weights) * 4 >= total
        private, source_free, underweight, target_only = weights
        for rank in range(1, 4):
            for kappa in range(1, 4):
                if private * 4 >= total:
                    paid = Fraction(private, rank * kappa)
                    assert paid >= Fraction(total, 4 * rank * kappa)
                if target_only * 4 >= total:
                    for target_capacity in range(1, 7):
                        if target_only <= kappa * target_capacity:
                            paid = Fraction(target_only, kappa)
                            assert paid >= Fraction(total, 4 * kappa)
                        else:
                            assert Fraction(target_only, target_capacity) > kappa
                counts["four-way routers"] += 1


def verify_overload_split(counts: Counter[str]) -> None:
    for weight in range(1, 20):
        for capacity in range(1, 10):
            for kappa in range(1, 5):
                if weight <= kappa * capacity:
                    assert Fraction(weight, kappa) <= capacity
                else:
                    assert Fraction(weight, capacity) > kappa
                counts["dominance alternatives"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    verify_private_allocation(counts)
    verify_target_pool(counts)
    verify_four_way_router(counts)
    verify_overload_split(counts)
    print("GC2s--GC2v shared source capacity audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
