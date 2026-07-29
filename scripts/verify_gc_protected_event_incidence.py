#!/usr/bin/env python3
"""Verify protected-event capacities derived from incidence and weight caps."""

from itertools import product


def main():
    checked = 0
    for k in range(1, 5):
        for assignment in product(range(k), repeat=5):
            for weights in product(range(1, 5), repeat=5):
                demands = [0] * k
                classes = [[] for _ in range(k)]
                for p, w in zip(assignment, weights):
                    demands[p] += w
                    classes[p].append(w)
                capacities = []
                for p in range(k):
                    d = len(classes[p])
                    L = max(classes[p], default=0)
                    capacities.append(d * L)
                    assert demands[p] <= capacities[p]
                assert sum(demands) <= sum(capacities)
                d_uniform = max((len(c) for c in classes), default=0)
                L_uniform = max(weights)
                assert sum(capacities) <= k * d_uniform * L_uniform
                checked += 1
    print(f"verified {checked} protected-event incidence instances")


if __name__ == "__main__":
    main()
