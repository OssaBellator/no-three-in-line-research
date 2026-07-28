#!/usr/bin/env python3

import math
import random


def max_matching_size(adj, n_right, allowed=None):
    masks = {0}
    for neighbours in adj:
        nxt = set(masks)
        for mask in masks:
            for r in neighbours:
                if allowed is not None and r not in allowed:
                    continue
                if not (mask >> r) & 1:
                    nxt.add(mask | (1 << r))
        masks = nxt
    return max(mask.bit_count() for mask in masks)


def minimum_cost(adj, costs):
    dp = {0: 0}
    for neighbours in adj:
        nxt = {}
        for mask, value in dp.items():
            for r in neighbours:
                if not (mask >> r) & 1:
                    new_mask = mask | (1 << r)
                    new_value = value + costs[r]
                    nxt[new_mask] = min(nxt.get(new_mask, 10**9), new_value)
        dp = nxt
    return min(dp.values())


def main():
    rng = random.Random(20260728)
    graphs = thresholds = total_cost = 0

    for _ in range(2500):
        n_left = rng.randint(2, 6)
        n_right = rng.randint(n_left, 8)
        costs = [rng.randint(0, 5) for _ in range(n_right)]
        adj = []
        for i in range(n_left):
            neighbours = {i}
            neighbours.update(r for r in range(n_right) if rng.random() < 0.35)
            adj.append(sorted(neighbours))

        assert max_matching_size(adj, n_right) == n_left
        optimum = minimum_cost(adj, costs)
        layer_cake = 0

        for t in range(max(costs)):
            allowed = {r for r, cost in enumerate(costs) if cost <= t}
            matching = max_matching_size(adj, n_right, allowed)
            deficiency = n_left - matching
            layer_cake += deficiency

            left_degrees = [sum(r in allowed for r in neighbours) for neighbours in adj]
            d_t = min(left_degrees)
            right_loads = [sum(r in neighbours for neighbours in adj) for r in allowed]
            D_t = max(right_loads, default=0)
            if D_t > 0:
                bound = math.floor(n_left * max(0.0, 1.0 - d_t / D_t) + 1e-12)
                assert deficiency <= bound
            thresholds += 1

        assert layer_cake == optimum
        total_cost += optimum
        graphs += 1

    print(f"audited {graphs:,} restricted-menu transport graphs")
    print(f"checked {thresholds:,} endpoint-cost thresholds")
    print(f"exact total minimum-cost mass {total_cost:,}")


if __name__ == "__main__":
    main()
