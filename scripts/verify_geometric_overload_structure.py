#!/usr/bin/env python3
"""Finite checks for GC2w--GC2aa."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations


def factor_families(universe: tuple[int, ...]) -> list[tuple[frozenset[int], ...]]:
    factors = [
        frozenset(cells)
        for size in range(1, 4)
        for cells in combinations(universe, size)
    ]
    return [
        tuple(),
        tuple(factors[: min(8, len(factors))]),
        tuple(factor for factor in factors if 0 in factor)[:10],
        tuple(factor for factor in factors if 0 not in factor)[:10],
        tuple(factor for index, factor in enumerate(factors) if index % 2 == 0)[:12],
        tuple(factor for index, factor in enumerate(factors) if index % 3 == 0)[:12],
    ]


def verify_source_free(counts: Counter[str]) -> None:
    for partner_count in range(1, 7):
        partners = tuple(range(1, partner_count + 1))
        universe = (0,) + partners + (partner_count + 1, partner_count + 2)
        for factors in factor_families(universe):
            for partner in partners:
                destroyed = [
                    factor
                    for factor in factors
                    if 0 in factor or partner in factor
                ]
                isolated = not any(0 in factor for factor in factors) and not any(
                    partner in factor for factor in factors
                )
                assert (not destroyed) == isolated
                counts["source-free isolation checks"] += 1


def verify_private_overload(counts: Counter[str]) -> None:
    for partner_count in range(1, 7):
        partners = tuple(range(1, partner_count + 1))
        universe = (0,) + partners + (partner_count + 1, partner_count + 2)
        for factors in factor_families(universe):
            capacities = {
                factor: 1 + (sum(factor) % 3)
                for factor in factors
            }
            for kappa in (1, 2, 3):
                pools: dict[int, tuple[frozenset[int], ...]] = {}
                weights: dict[int, int] = {}
                for partner in partners:
                    pool = tuple(
                        factor
                        for factor in factors
                        if partner in factor and 0 not in factor
                    )
                    capacity = sum(capacities[factor] for factor in pool)
                    if capacity:
                        pools[partner] = pool
                        weights[partner] = kappa * capacity + 1
                if not pools:
                    continue

                demand: dict[tuple[int, frozenset[int]], Fraction] = {}
                for partner, pool in pools.items():
                    capacity = sum(capacities[factor] for factor in pool)
                    for factor in pool:
                        demand[(partner, factor)] = Fraction(
                            weights[partner] * capacities[factor],
                            capacity,
                        )
                    assert sum(
                        demand[(partner, factor)]
                        for factor in pool
                    ) == weights[partner]

                used = {factor for _, factor in demand}
                for factor in used:
                    factor_demand = sum(
                        value
                        for (partner, observed), value in demand.items()
                        if observed == factor
                    )
                    assert factor_demand > kappa * capacities[factor]
                    contributors = sum(
                        factor in pool
                        for pool in pools.values()
                    )
                    assert contributors <= len(factor) <= 3
                assert sum(demand.values()) == sum(weights.values())
                counts["private overload systems"] += 1


def verify_target_overload(counts: Counter[str]) -> None:
    for partner_count in range(1, 7):
        partners = tuple(range(1, partner_count + 1))
        universe = (0,) + partners + (partner_count + 1, partner_count + 2)
        for factors in factor_families(universe):
            capacities = {
                factor: 1 + (sum(factor) % 4)
                for factor in factors
            }
            target_link = tuple(factor for factor in factors if 0 in factor)
            target_capacity = sum(capacities[factor] for factor in target_link)
            if not target_capacity:
                continue
            for kappa in (1, 2, 3):
                total_weight = kappa * target_capacity + 1
                demand = {
                    factor: Fraction(
                        capacities[factor] * total_weight,
                        target_capacity,
                    )
                    for factor in target_link
                }
                assert all(
                    value > kappa * capacities[factor]
                    for factor, value in demand.items()
                )
                assert sum(demand.values()) == total_weight
                assert all(0 in factor for factor in demand)
                counts["target overload systems"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    verify_source_free(counts)
    verify_private_overload(counts)
    verify_target_overload(counts)
    print("GC2w--GC2aa overload-structure audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
