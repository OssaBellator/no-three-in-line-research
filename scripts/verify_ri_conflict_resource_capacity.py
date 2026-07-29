#!/usr/bin/env python3
"""Finite checks for RI5cd--RI5cg."""

from itertools import product


def main() -> None:
    checks = 0
    for n in range(1, 9):
        for k in range(1, 5):
            for mu in range(1, 5):
                # Exhaust small systems and use deterministic samples for larger ones.
                weight_vectors = product(range(4), repeat=n) if n <= 5 else (
                    tuple((seed * (i + 3) + i * i + 1) % 7 for i in range(n))
                    for seed in range(400)
                )
                for weights in weight_vectors:
                    label_vectors = product(range(k), repeat=n) if n <= 4 else (
                        tuple((seed + 2 * i + i * i) % k for i in range(n))
                        for seed in range(120)
                    )
                    for labels in label_vectors:
                        fibres = [[] for _ in range(k)]
                        for w, r in zip(weights, labels):
                            fibres[r].append(w)
                        total = sum(weights)
                        assert sum(sum(f) for f in fibres) == total
                        if all(len(f) <= mu for f in fibres):
                            selected = sum(max(f, default=0) for f in fibres)
                            assert mu * selected >= total
                        else:
                            assert any(len(f) > mu for f in fibres)
                        checks += 1
    print(f"verified {checks} RI resource-fibre systems")


if __name__ == "__main__":
    main()
