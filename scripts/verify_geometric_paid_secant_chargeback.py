#!/usr/bin/env python3
"""Finite checks for GC2g--GC2j."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import ceil, floor


def verify_payment(counts: Counter[str]) -> None:
    # Incidence columns are current factors; rows are current corrections.
    for correction_count in range(1, 5):
        for factor_count in range(1, 5):
            for rank in range(1, 4):
                row_masks = range(1, 1 << factor_count)
                for masks in product(row_masks, repeat=correction_count):
                    column_degrees = [
                        sum(mask >> factor & 1 for mask in masks)
                        for factor in range(factor_count)
                    ]
                    if max(column_degrees) > rank:
                        continue
                    for weights in product((1, 2), repeat=factor_count):
                        destroyed = [
                            sum(weights[f] for f in range(factor_count) if mask >> f & 1)
                            for mask in masks
                        ]
                        # Use extremal and interior gain choices without exploding the grid.
                        gain_options = [
                            tuple(1 for _ in destroyed),
                            tuple(destroyed),
                            tuple(max(1, (value + 1) // 2) for value in destroyed),
                        ]
                        for gains in gain_options:
                            ratios = []
                            for factor in range(factor_count):
                                ratios.append(
                                    sum(
                                        Fraction(gains[i], destroyed[i])
                                        for i, mask in enumerate(masks)
                                        if mask >> factor & 1
                                    )
                                )
                            kappa = max(ratios, default=Fraction(0))
                            K = max(Fraction(1), kappa)
                            charges = [
                                [
                                    Fraction(gains[i] * weights[f], 1) / (K * destroyed[i])
                                    if masks[i] >> f & 1
                                    else Fraction(0)
                                    for f in range(factor_count)
                                ]
                                for i in range(correction_count)
                            ]
                            for i in range(correction_count):
                                assert sum(charges[i]) == Fraction(gains[i], 1) / K
                                assert sum(charges[i]) <= gains[i]
                            factor_payments = [
                                sum(charges[i][f] for i in range(correction_count))
                                for f in range(factor_count)
                            ]
                            assert all(factor_payments[f] <= weights[f] for f in range(factor_count))
                            total_gain = sum(gains)
                            total_payment = sum(factor_payments)
                            assert total_payment == Fraction(total_gain, 1) / K
                            assert total_payment * rank >= total_gain

                            for subset_mask in range(1, 1 << factor_count):
                                subset = [f for f in range(factor_count) if subset_mask >> f & 1]
                                W = sum(factor_payments[f] for f in subset)
                                if W == 0:
                                    continue
                                candidates = [
                                    (gains[i], charges[i][f])
                                    for i in range(correction_count)
                                    for f in subset
                                    if charges[i][f] > 0
                                ]
                                assert candidates
                                best_gain, best_charge = max(candidates, key=lambda item: item[1])
                                assert best_gain >= best_charge
                                assert best_charge * rank * len(subset) >= W
                                counts["chargeback fibres"] += 1
                            counts["payment systems"] += 1


def greedy_matching(triples: tuple[tuple[int, int, int], ...]) -> tuple[tuple[int, int, int], ...]:
    remaining = list(triples)
    selected: list[tuple[int, int, int]] = []
    while remaining:
        chosen = remaining[0]
        selected.append(chosen)
        support = set(chosen)
        remaining = [triple for triple in remaining if support.isdisjoint(triple)]
    return tuple(selected)


def verify_star_matching(counts: Counter[str]) -> None:
    points = range(6)
    all_triples = tuple(combinations(points, 3))
    # Exhaust all subfamilies up to six triples and representative positive weights.
    for family_size in range(1, 7):
        for triples in combinations(all_triples, family_size):
            for weights in (tuple(1 for _ in triples), tuple(1 + (i % 2) for i in range(len(triples)))):
                total = sum(weights)
                point_load = {
                    point: sum(weight for triple, weight in zip(triples, weights) if point in triple)
                    for point in points
                }
                for mu in (1, 2):
                    for lam in range(1, total + 1):
                        heavy = any(weight > mu for weight in weights)
                        star = max(point_load.values(), default=0) > lam
                        if heavy:
                            counts["heavy outputs"] += 1
                            continue
                        if star:
                            point = max(point_load, key=point_load.get)
                            degree = sum(point in triple for triple in triples)
                            assert degree >= floor(lam / mu) + 1
                            counts["star outputs"] += 1
                            continue
                        matching = greedy_matching(triples)
                        assert len(matching) >= ceil(Fraction(total, 3 * lam))
                        counts["matching outputs"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    verify_payment(counts)
    verify_star_matching(counts)
    print("GC2g--GC2j paid-secant chargeback audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
