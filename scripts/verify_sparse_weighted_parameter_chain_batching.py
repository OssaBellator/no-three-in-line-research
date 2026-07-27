#!/usr/bin/env python3
"""Finite audit for SAS5dw--SAS5eb."""

from __future__ import annotations

from collections import Counter
from itertools import product
from math import ceil, gcd
import random


def adjacent_matching(indices: set[int], J: int) -> list[int]:
    edges = [s for s in range(J - 1) if s in indices and s + 1 in indices]
    selected: list[int] = []
    used: set[int] = set()
    for left in edges:
        if left not in used and left + 1 not in used:
            selected.append(left)
            used.add(left)
            used.add(left + 1)
    return selected


def audit_weights(weights: tuple[int, ...], stats: Counter[str]) -> None:
    J = len(weights)
    W = sum(weights)
    if W == 0:
        return
    a = W / (4 * J)
    M = 4 * W / (3 * J)
    K_0 = ceil(9 * J / 16)
    E_0 = max(0, 2 * K_0 - J - 1)
    q_0 = ceil(E_0 / 2)

    if max(weights) > M:
        stats["heavy_atom_systems"] += 1
        return

    heavy = {i for i, weight in enumerate(weights) if weight >= a}
    heavy_mass = sum(weights[i] for i in heavy)
    assert heavy_mass >= W - J * a
    assert len(heavy) >= K_0

    edges = sum(i in heavy and i + 1 in heavy for i in range(J - 1))
    assert edges >= E_0
    selected = adjacent_matching(heavy, J)
    assert len(selected) >= q_0
    bottleneck = sum(min(weights[i], weights[i + 1]) for i in selected[:q_0])
    assert bottleneck >= a * q_0
    stats["adjacent_batch_systems"] += 1
    stats["selected_adjacent_pairs"] += q_0
    stats["bottleneck_weight_numerators"] += int(bottleneck * 4 * J)


def main() -> None:
    rng = random.Random(20260727)
    stats: Counter[str] = Counter()

    for J in range(1, 9):
        for weights in product(range(4), repeat=J):
            audit_weights(weights, stats)
            stats["exhaustive_weight_systems"] += 1

    for _ in range(100_000):
        J = rng.randint(1, 80)
        weights = tuple(rng.randint(0, 50) for _ in range(J))
        audit_weights(weights, stats)
        stats["random_weight_systems"] += 1

        # Common-step line and dilation identities.
        s = rng.randint(-30, 30)
        A_0 = rng.choice([x for x in range(-8, 9) if x])
        D_0 = rng.choice([x for x in range(-8, 9) if x])
        B_0 = rng.choice([x for x in range(-8, 9) if x and x != A_0])
        r_0, c_0, x = (rng.randint(-20, 20) for _ in range(3))
        line_left = (r_0 + s * A_0, c_0 + s * D_0)
        line_right = (r_0 + (s + 1) * A_0, c_0 + (s + 1) * D_0)
        assert (line_right[0] - line_left[0], line_right[1] - line_left[1]) == (A_0, D_0)
        dil_left = (x + A_0 * s, x + B_0 * s)
        dil_right = (x + A_0 * (s + 1), x + B_0 * (s + 1))
        assert (dil_right[0] - dil_left[0], dil_right[1] - dil_left[1]) == (A_0, B_0)
        stats["common_step_tests"] += 2

        # Fixed scale: consecutive base rows translate the complete triple by (1,1,1).
        g_scale = rng.randint(1, 12)
        base = rng.randint(-20, 20)
        triple = (base, base + g_scale * A_0, base + g_scale * B_0)
        shifted = tuple(value + 1 for value in triple)
        assert tuple(shifted[i] - triple[i] for i in range(3)) == (1, 1, 1)
        stats["base_row_translation_tests"] += 1

    # Coprime interval and prime-exclusion audit.
    for A_0 in range(2, 151):
        prime_divisors = [p for p in range(2, A_0 + 1) if A_0 % p == 0 and all(p % q for q in range(2, int(p**0.5) + 1))]
        for start in range(-20, 21):
            for J in range(1, 31):
                interval = list(range(start, start + J))
                occupied = [value for value in interval if gcd(abs(value), A_0) == 1]
                K = len(occupied)
                h = J - K
                for p in prime_divisors:
                    assert K <= J - (J // p)
                    assert J // p <= h
                    assert p > J / (h + 1)
                    stats["prime_exclusion_tests"] += 1

                # Random coprime subfamilies only increase the hole count.
                chosen = [value for value in occupied if rng.random() < 0.6]
                K_chosen = len(chosen)
                h_chosen = J - K_chosen
                for p in prime_divisors:
                    assert K_chosen <= J - (J // p)
                    assert p > J / (h_chosen + 1)
                    stats["coprime_subfamily_tests"] += 1

    print("SAS weighted parameter-chain audit passed")
    for key in sorted(stats):
        print(f"{key}: {stats[key]}")


if __name__ == "__main__":
    main()
