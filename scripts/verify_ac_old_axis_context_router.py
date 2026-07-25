#!/usr/bin/env python3
"""Verify AC3hi--AC3hk old-axis context routing."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product


def verify_context_router(
    max_points: int = 5,
    max_records: int = 5,
    max_weight: int = 3,
    max_k: int = 5,
) -> int:
    checks = 0
    pairs = list(combinations(range(max_points), 2))
    for record_count in range(1, min(max_records, len(pairs)) + 1):
        for contexts in combinations(pairs, record_count):
            for weights in product(range(1, max_weight + 1), repeat=record_count):
                total = sum(weights)
                adjacent = [
                    [
                        bool(set(contexts[i]) & set(contexts[j]))
                        for j in range(record_count)
                    ]
                    for i in range(record_count)
                ]
                closed_load = [
                    sum(
                        weights[j]
                        for j in range(record_count)
                        if adjacent[i][j]
                    )
                    for i in range(record_count)
                ]
                for k in range(1, max_k + 1):
                    overloads = [
                        i
                        for i in range(record_count)
                        if closed_load[i] > k * weights[i]
                    ]
                    if overloads:
                        i = overloads[0]
                        x, y = contexts[i]
                        load_x = sum(
                            weights[j]
                            for j in range(record_count)
                            if x in contexts[j]
                        )
                        load_y = sum(
                            weights[j]
                            for j in range(record_count)
                            if y in contexts[j]
                        )
                        assert load_x + load_y >= closed_load[i]
                        assert max(load_x, load_y) > Fraction(k * weights[i], 2)
                    else:
                        remaining = set(range(record_count))
                        selected = []
                        while remaining:
                            i = next(iter(remaining))
                            selected.append(i)
                            remaining = {
                                j for j in remaining if not adjacent[i][j]
                            }
                        selected_weight = sum(weights[i] for i in selected)
                        assert k * selected_weight >= total
                        for i, j in combinations(selected, 2):
                            assert set(contexts[i]).isdisjoint(contexts[j])
                    checks += 1
    return checks


def verify_pair_dispersion(max_pivots: int = 8, max_weight: int = 5) -> int:
    checks = 0
    for pivot_count in range(1, max_pivots + 1):
        for weights in product(range(max_weight + 1), repeat=min(pivot_count, 5)):
            padded = weights + (0,) * (pivot_count - len(weights))
            total = sum(padded)
            for beta in range(1, max_weight + 1):
                if any(weight > beta for weight in padded):
                    checks += 1
                    continue
                nonzero = sum(weight > 0 for weight in padded)
                if total:
                    assert nonzero * beta >= total
                checks += 1
    return checks


def main() -> None:
    contexts = verify_context_router()
    pairs = verify_pair_dispersion()
    print(
        "AC old-axis context router verified:",
        f"{contexts} weighted context systems,",
        f"{pairs} fixed-pair dispersion systems",
    )


if __name__ == "__main__":
    main()
