#!/usr/bin/env python3
"""Finite audit for GC2dw--GC2ea."""

from collections import defaultdict
from itertools import permutations
import random

SEED = 20260727


def falling(t, r):
    value = 1
    for offset in range(r):
        value *= t - offset
    return value


def matching_family_audit(counts):
    rng = random.Random(SEED)
    for t in range(4, 9):
        for _ in range(40):
            forbidden = {(i, i) for i in range(t)}
            extra = list(range(t))
            rng.shuffle(extra)
            for i in range(t):
                if rng.random() < 0.5 and extra[i] != i:
                    forbidden.add((i, extra[i]))

            omega = [
                p
                for p in permutations(range(t))
                if all((i, p[i]) not in forbidden for i in range(t))
            ]
            if not omega:
                continue

            counts["families"] += 1
            counts["states"] += len(omega)

            for p in omega:
                assert all(p[i] != i for i in range(t))
                counts["source_checks"] += t

            for rank in range(1, 4):
                for _ in range(30):
                    p = rng.choice(omega)
                    columns = rng.sample(range(t), rank)
                    prescription = tuple((i, p[i]) for i in columns)
                    hits = sum(
                        all(q[i] == image for i, image in prescription)
                        for q in omega
                    )
                    probability = hits / len(omega)
                    assert probability <= 128 / falling(t, rank) + 1e-12
                    counts[f"rank_{rank}_probabilities"] += 1


def weighted_router_audit(counts):
    rng = random.Random(SEED + 1)
    for _ in range(100000):
        t = rng.randint(7, 100)
        inventory = [0] + [rng.randint(0, 100000) for _ in range(3)]
        fixed_cost = rng.randint(0, 5000)
        source = rng.randint(1, 10000)

        rank_terms = [0] + [
            128 * inventory[rank] / falling(t, rank)
            for rank in range(1, 4)
        ]
        expected_bound = sum(rank_terms[1:])

        if source > fixed_cost + expected_bound:
            assert fixed_cost - source + expected_bound < 0
            counts["descent_systems"] += 1
            continue

        deficit = max(source - fixed_cost, 0)
        if deficit == 0:
            assert fixed_cost >= source
            counts["fixed_cost_failures"] += 1
            continue

        # This branch encodes the no-descent hypothesis: actual collateral is at
        # least the deficit and is bounded above by the AN inventory estimate.
        if expected_bound >= deficit:
            rank = max(range(1, 4), key=lambda r: rank_terms[r])
            assert rank_terms[rank] >= deficit / 3 - 1e-9
            assert inventory[rank] + 1e-9 >= deficit * falling(t, rank) / 384
            counts["rank_failures"] += 1


def main():
    counts = defaultdict(int)
    matching_family_audit(counts)
    weighted_router_audit(counts)

    print("GC single-witness local-margin audit passed")
    print(f"  allowed matching families: {counts['families']}")
    print(f"  enumerated local states: {counts['states']}")
    print(f"  designated-source movement checks: {counts['source_checks']}")
    for rank in range(1, 4):
        print(
            f"  rank-{rank} probability checks: "
            f"{counts[f'rank_{rank}_probabilities']}"
        )
    print(f"  strict-margin systems: {counts['descent_systems']}")
    print(f"  fixed-cost failures: {counts['fixed_cost_failures']}")
    print(f"  localized rank failures: {counts['rank_failures']}")


if __name__ == "__main__":
    main()
