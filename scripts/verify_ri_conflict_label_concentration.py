#!/usr/bin/env python3
"""Finite checks for RI5bz--RI5cc."""

from itertools import product


def main() -> None:
    checks = 0
    for degree in range(0, 8):
        for K in range(1, 5):
            for weights in product(range(5), repeat=degree + 1):
                center = weights[0]
                neighbor_weights = weights[1:]
                for labels in product(range(K), repeat=degree):
                    buckets = [center] + [0] * K
                    for w, label in zip(neighbor_weights, labels):
                        buckets[label + 1] += w
                    total = sum(weights)
                    assert sum(buckets) == total
                    assert max(buckets) * (K + 1) >= total

                    # Deterministic finite sublabel refinement of every label bucket.
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
                    checks += 1
    print(f"verified {checks} labeled RI neighborhoods")


if __name__ == "__main__":
    main()
