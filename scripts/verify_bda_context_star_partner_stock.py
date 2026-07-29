#!/usr/bin/env python3
"""Finite checks for BDA5ck--BDA5cn."""

from itertools import combinations, product


def main() -> None:
    checks = 0
    for n in range(2, 8):
        edges = list(combinations(range(n), 2))
        weight_vectors = product(range(4), repeat=len(edges)) if n <= 4 else (
            tuple((seed + 3 * i + i * i) % 8 for i in range(len(edges)))
            for seed in range(1000)
        )
        for weights in weight_vectors:
            total = sum(weights)
            stars = [0] * n
            for (u, v), w in zip(edges, weights):
                stars[u] += w
                stars[v] += w
            assert sum(stars) == 2 * total
            assert max(stars) * n >= 2 * total
            x = max(range(n), key=lambda i: stars[i])
            incident = [(e, w) for e, w in zip(edges, weights) if x in e]
            partners = [v if u == x else u for (u, v), _ in incident]
            assert len(partners) == len(set(partners))
            for k in range(1, 5):
                buckets = [0] * k
                for idx, (_, w) in enumerate(incident):
                    buckets[(idx * idx + idx) % k] += w
                assert sum(buckets) == stars[x]
                assert max(buckets, default=0) * k >= stars[x]
            checks += 1
    print(f"verified {checks} weighted BDA partner-star systems")


if __name__ == "__main__":
    main()
