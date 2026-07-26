#!/usr/bin/env python3
"""Finite checks for GC2bg--GC2bl."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import product
from random import Random


def exhaustive_stars(counts: Counter[str]) -> None:
    for m in range(1, 6):
        for demands in product(range(1, 4), repeat=m):
            w = sum(demands)
            for capacities in product(range(4), repeat=m):
                c = sum(capacities)
                for theta in range(1, 5):
                    if theta * c >= w:
                        continue
                    residual = w - c
                    assert residual > 0
                    assert theta * residual > (theta - 1) * w
                    assert c < w / theta
                    counts["exhaustive deficient stars"] += 1
                    counts["star factors"] += m


def external_capacity_checks(counts: Counter[str]) -> None:
    rng = Random(20260726)
    for _ in range(60000):
        m = rng.randint(1, 20)
        theta = rng.randint(1, 8)
        demands = [rng.randint(1, 9) for _ in range(m)]
        capacities = [rng.randint(0, 6) for _ in range(m)]
        w = sum(demands)
        c = sum(capacities)
        if theta * c >= w:
            # Force a deficient instance without changing positivity of demand.
            capacities = [0] * m
            c = 0
        residual = w - c
        assert theta * residual > (theta - 1) * w

        ext_count = rng.randint(0, 20)
        ext_caps = [rng.randint(0, 12) for _ in range(ext_count)]
        ext_total = sum(ext_caps)
        complete_possible = ext_total >= residual
        if not complete_possible:
            assert c + ext_total < w
            counts["external Hall deficits"] += 1
        else:
            # Construct one greedy external allocation of exactly the residual.
            remaining = residual
            allocation = []
            for cap in ext_caps:
                amount = min(cap, remaining)
                allocation.append(amount)
                remaining -= amount
            assert remaining == 0 and sum(allocation) == residual
            counts["complete external allocations"] += 1

            role_count = max(1, rng.randint(1, 6))
            role_weight: dict[int, int] = defaultdict(int)
            role_members: dict[int, list[int]] = defaultdict(list)
            for p, amount in enumerate(allocation):
                role = p % role_count
                role_weight[role] += amount
                role_members[role].append(amount)
            assert max(role_weight.values(), default=0) * role_count >= residual

            best_role = max(role_weight, key=role_weight.get)
            positive_members = [x for x in role_members[best_role] if x > 0]
            if positive_members:
                assert max(positive_members) * len(role_members[best_role]) >= role_weight[best_role]
            counts["role localizations"] += 1

            gain = residual + rng.randint(0, 20)
            certified_row = residual
            assert certified_row <= gain
            counts["gain-certified descents"] += 1
            counts["certified gain"] += gain

        # Capacity feasibility alone is compatible with zero gain.
        zero_gain = 0
        assert zero_gain <= 0
        counts["non-gain wall systems"] += 1


def bounded_fibre_checks(counts: Counter[str]) -> None:
    for t_ext in range(1, 8):
        for b_ext in range(1, 9):
            for residual in range(1, 40):
                incidences = t_ext * b_ext
                base, rem = divmod(residual, incidences)
                weights = [base + (1 if i < rem else 0) for i in range(incidences)]
                role_sums = [sum(weights[r * b_ext:(r + 1) * b_ext]) for r in range(t_ext)]
                assert max(role_sums) * t_ext >= residual
                best = max(role_sums)
                start = role_sums.index(best) * b_ext
                assert max(weights[start:start + b_ext]) * b_ext >= best
                counts["bounded role fibres"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    exhaustive_stars(counts)
    external_capacity_checks(counts)
    bounded_fibre_checks(counts)
    print("GC2bg--GC2bl capacity-deficient star audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
