#!/usr/bin/env python3
"""Finite checks for GC2o--GC2r."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations, product


def verify_rank_reuse(counts: Counter[str]) -> None:
    for partner_count in range(1, 7):
        partners = tuple(range(1, partner_count + 1))
        target = 0
        universe = (target,) + partners + (partner_count + 1, partner_count + 2)
        for rank in range(1, 4):
            factors = [
                frozenset(cells)
                for size in range(1, rank + 1)
                for cells in combinations(universe, size)
            ]
            private = {
                partner: [
                    factor
                    for factor in factors
                    if partner in factor and target not in factor
                ]
                for partner in partners
            }
            if any(not private[partner] for partner in partners):
                continue
            samples = [tuple(options[0] for options in private.values())]
            samples.append(tuple(options[-1] for options in private.values()))
            samples.append(
                tuple(options[index % len(options)] for index, options in enumerate(private.values()))
            )
            for assigned in samples:
                multiplicities = {
                    factor: sum(chosen == factor for chosen in assigned)
                    for factor in set(assigned)
                }
                assert max(multiplicities.values()) <= rank
                counts["rank assignments"] += 1


def verify_congestion(counts: Counter[str]) -> None:
    for rank in range(1, 4):
        for kappa in range(1, 4):
            for factor_count in range(1, 5):
                for partner_count in range(1, 7):
                    for source_map in product(range(factor_count), repeat=partner_count):
                        if max(source_map.count(q) for q in range(factor_count)) > rank:
                            continue
                        for capacities in product((1, 2, 3), repeat=factor_count):
                            weight_options = []
                            for q in source_map:
                                cap = capacities[q]
                                weight_options.append((0, cap, kappa * cap))
                            for weights in product(*weight_options):
                                loads = [
                                    sum(
                                        weights[index]
                                        for index, q in enumerate(source_map)
                                        if q == factor
                                    )
                                    for factor in range(factor_count)
                                ]
                                assert all(
                                    loads[factor] <= rank * kappa * capacities[factor]
                                    for factor in range(factor_count)
                                )
                                paid = [
                                    Fraction(weight, rank * kappa)
                                    for weight in weights
                                ]
                                for factor in range(factor_count):
                                    assert sum(
                                        paid[index]
                                        for index, q in enumerate(source_map)
                                        if q == factor
                                    ) <= capacities[factor]
                                counts["congestion systems"] += 1
                                if counts["congestion systems"] >= 75_000:
                                    return


def classify(
    target: int,
    partner: int,
    destroyed: tuple[frozenset[int], ...],
    weight: int,
    capacities: dict[frozenset[int], int],
    kappa: int,
) -> str:
    if not destroyed:
        return "source-free"
    assert all(target in factor or partner in factor for factor in destroyed)
    private = [factor for factor in destroyed if partner in factor and target not in factor]
    if not private:
        assert all(target in factor for factor in destroyed)
        return "target-common"
    if all(weight > kappa * capacities[factor] for factor in private):
        return "private-underweight"
    return "eligible"


def verify_failure_router(counts: Counter[str]) -> None:
    target = 0
    partners = (1, 2, 3, 4)
    factors = tuple(
        frozenset(cells)
        for size in range(1, 4)
        for cells in combinations((0, 1, 2, 3, 4, 5), size)
    )
    capacities = {factor: 1 + (sum(factor) % 3) for factor in factors}
    choices_by_partner = []
    for partner in partners:
        target_common = tuple(factor for factor in factors if target in factor)[:4]
        private = tuple(
            factor for factor in factors if partner in factor and target not in factor
        )[:4]
        mixed = tuple(
            factor for factor in factors if target in factor or partner in factor
        )[:6]
        choices_by_partner.append((tuple(), target_common, private, mixed))

    for kappa in (1, 2):
        for destroyed_choices in product(*choices_by_partner):
            for weights in product((1, 2, 4), repeat=len(partners)):
                roles = [
                    classify(
                        target,
                        partner,
                        destroyed,
                        weight,
                        capacities,
                        kappa,
                    )
                    for partner, destroyed, weight in zip(partners, destroyed_choices, weights)
                ]
                total = sum(weights)
                eligible = sum(
                    weight for weight, role in zip(weights, roles) if role == "eligible"
                )
                if eligible * 2 >= total:
                    assert eligible >= Fraction(total, 2)
                else:
                    residual = {
                        role: sum(
                            weight
                            for weight, observed in zip(weights, roles)
                            if observed == role
                        )
                        for role in (
                            "source-free",
                            "target-common",
                            "private-underweight",
                        )
                    }
                    assert max(residual.values()) >= Fraction(total, 6)
                counts["failure systems"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    verify_rank_reuse(counts)
    verify_congestion(counts)
    verify_failure_router(counts)
    print("GC2o--GC2r partner-private source audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
