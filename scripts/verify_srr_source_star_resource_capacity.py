#!/usr/bin/env python3
"""Finite checks for SRR2aw--SRR2az."""

from itertools import product


def main() -> None:
    checks = 0
    for n in range(1, 9):
        for resources in range(1, 5):
            for mu in range(1, 5):
                weight_vectors = product(range(5), repeat=n) if n <= 5 else (
                    tuple((seed + 3 * i + i * i) % 9 for i in range(n))
                    for seed in range(300)
                )
                for weights in weight_vectors:
                    assignments = product(range(resources), repeat=n) if n <= 4 else (
                        tuple((seed * 2 + i * i + i) % resources for i in range(n))
                        for seed in range(100)
                    )
                    for labels in assignments:
                        fibres = [[] for _ in range(resources)]
                        for w, r in zip(weights, labels):
                            fibres[r].append(w)
                        total = sum(weights)
                        assert sum(sum(f) for f in fibres) == total
                        if all(len(f) <= mu for f in fibres):
                            stock = sum(max(f, default=0) for f in fibres)
                            assert mu * stock >= total
                        else:
                            assert any(len(f) > mu for f in fibres)
                        checks += 1
    print(f"verified {checks} source-star resource systems")


if __name__ == "__main__":
    main()
