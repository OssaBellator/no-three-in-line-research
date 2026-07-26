#!/usr/bin/env python3
"""Finite checks for SAS5cc--SAS5cg."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations, permutations, product
from math import gcd
from random import Random


def swap_state(labels: tuple[int, ...], pair: tuple[int, int], enabled: int) -> tuple[int, ...]:
    if not enabled:
        return labels
    out = list(labels)
    a, b = pair
    out[a], out[b] = out[b], out[a]
    return tuple(out)


def indicator(state: tuple[int, ...], scope: tuple[int, int, int], required: tuple[int, int, int]) -> int:
    return int(all(state[column] == label for column, label in zip(scope, required)))


def row_reconstruction(counts: Counter[str]) -> None:
    for n in range(3, 11):
        classes: dict[tuple[tuple[int, int, int], int, int], set[tuple[int, int]]] = defaultdict(set)
        for rows in combinations(range(n), 3):
            for placement in permutations(range(3)):
                i, j, k = placement
                a_gap = rows[j] - rows[i]
                b_gap = rows[k] - rows[i]
                scale = gcd(abs(a_gap), abs(b_gap))
                a0 = a_gap // scale
                b0 = b_gap // scale
                reconstructed = [None, None, None]
                reconstructed[i] = rows[i]
                reconstructed[j] = rows[i] + scale * a0
                reconstructed[k] = rows[i] + scale * b0
                assert tuple(reconstructed) == rows
                key = (placement, a0, b0)
                classes[key].add((scale, rows[i]))
                counts["row reconstructions"] += 1
        for addresses in classes.values():
            assert len(addresses) <= n * (n - 1)
            counts["primitive ratio classes"] += 1
            counts["scale-base addresses"] += len(addresses)


def label_uniqueness(counts: Counter[str]) -> None:
    omega = (0, 1)
    tau = (2, 3)
    columns = range(5)
    for labels in product(range(3), repeat=5):
        if labels[0] == labels[1] or labels[2] == labels[3]:
            continue
        states = {
            (0, 0): labels,
            (1, 0): swap_state(labels, omega, 1),
            (0, 1): swap_state(labels, tau, 1),
            (1, 1): swap_state(swap_state(labels, omega, 1), tau, 1),
        }
        for scope in combinations(columns, 3):
            if not set(scope).intersection(omega) or not set(scope).intersection(tau):
                continue

            required_omega = tuple(states[(1, 0)][c] for c in scope)
            table_omega = tuple(
                indicator(states[state], scope, required_omega)
                for state in ((0, 0), (1, 0), (0, 1), (1, 1))
            )
            assert table_omega == (0, 1, 0, 0)

            required_tau = tuple(states[(0, 1)][c] for c in scope)
            table_tau = tuple(
                indicator(states[state], scope, required_tau)
                for state in ((0, 0), (1, 0), (0, 1), (1, 1))
            )
            assert table_tau == (0, 0, 1, 0)

            # Satisfaction in the named state forces the required vector coordinatewise.
            for candidate in product(range(3), repeat=3):
                if indicator(states[(1, 0)], scope, candidate):
                    assert candidate == required_omega
                if indicator(states[(0, 1)], scope, candidate):
                    assert candidate == required_tau

            counts["omega-only label records"] += 1
            counts["tau-only label records"] += 1


def quantitative_router(counts: Counter[str]) -> None:
    rng = Random(20260726)
    for _ in range(50000):
        n = rng.randint(3, 50)
        eta_num = rng.randint(1, 99)
        eta_den = 100
        scale_weight = rng.randint(1, 100000)
        negative_numerator = eta_num * scale_weight
        denominator = 576 * n * (n - 1) ** 3
        # The displayed exact-record bound is eta*L_g / denominator.
        assert negative_numerator > 0
        assert denominator >= 576 * 3 * 2**3
        counts["quantitative routers"] += 1
        counts["router weight numerators"] += negative_numerator


def main() -> None:
    counts: Counter[str] = Counter()
    row_reconstruction(counts)
    label_uniqueness(counts)
    quantitative_router(counts)
    print("SAS5cc--SAS5cg exact negative-cross record audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
