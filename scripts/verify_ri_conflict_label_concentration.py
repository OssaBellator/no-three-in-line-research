#!/usr/bin/env python3
"""Finite checks for RI5bz--RI5cc."""

from itertools import product


def check(weights, labels, K):
    center = weights[0]
    neighbor_weights = weights[1:]
    buckets = [center] + [0] * K
    for w, label in zip(neighbor_weights, labels):
        buckets[label + 1] += w
    total = sum(weights)
    assert sum(buckets) == total
    assert max(buckets) * (K + 1) >= total

    for label in range(K):
        members = [
            (idx, w)
            for idx, (w, lab) in enumerate(zip(neighbor_weights, labels))
            if lab == label
        ]
        for R in range(1, 4):
            sub = [0] * R
            for idx, w in members:
                sub[idx % R] += w
            assert sum(sub) == buckets[label + 1]
            assert max(sub, default=0) * R >= buckets[label + 1]


def main() -> None:
    checks = 0
    # Exhaust all small neighborhoods.
    for degree in range(0, 4):
        for K in range(1, 4):
            for weights in product(range(4), repeat=degree + 1):
                for labels in product(range(K), repeat=degree):
                    check(weights, labels, K)
                    checks += 1

    # Deterministic larger samples.
    for degree in range(4, 13):
        for K in range(1, 7):
            for seed in range(500):
                weights = tuple((seed * (i + 3) + i * i + 2) % 17 for i in range(degree + 1))
                labels = tuple((seed + 3 * i + i * i) % K for i in range(degree))
                check(weights, labels, K)
                checks += 1

    print(f"verified {checks} labeled RI neighborhoods")


if __name__ == "__main__":
    main()
