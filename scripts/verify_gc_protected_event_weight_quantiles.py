#!/usr/bin/env python3
"""Finite checks for GC4ah--GC4ak."""

from itertools import combinations


def top_sum(weights, d):
    return sum(sorted(weights, reverse=True)[:d])


def main():
    checks = 0
    values = range(6)
    for n in range(1, 8):
        # Deterministic mixed weight vectors.
        vectors = [tuple((i * a + b) % 6 for i in range(n)) for a in range(1, 5) for b in range(4)]
        for weights in vectors:
            for d in range(n + 1):
                cap = top_sum(weights, d)
                best = 0
                for r in range(d + 1):
                    for idx in combinations(range(n), r):
                        best = max(best, sum(weights[i] for i in idx))
                assert cap == best
                checks += 1

        # Aggregate address-specific versus global quantiles.
        global_weights = tuple((3 * i + n) % 7 for i in range(n))
        pools = [global_weights[::2], global_weights[1::2], global_weights]
        caps = [min(2, len(pool)) for pool in pools]
        local_total = sum(top_sum(pool, d) for pool, d in zip(pools, caps))
        global_total = sum(top_sum(global_weights, d) for d in caps)
        assert local_total <= global_total

        W = sum(global_weights) + 1
        if local_total < W:
            eta = local_total / W
            assert W - local_total >= (1 - eta) * W - 1e-12

    print(f"verified {checks} protected-event top-weight capacities")


if __name__ == "__main__":
    main()
