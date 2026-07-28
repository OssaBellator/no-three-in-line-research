#!/usr/bin/env python3
"""Finite audit for AC5ak--AC5ao."""

from collections import defaultdict
from itertools import combinations
import random

SEED = 20260728


def subsets(n):
    for r in range(1, n + 1):
        for s in combinations(range(n), r):
            yield s


def main():
    rng = random.Random(SEED)
    counts = defaultdict(int)

    for _ in range(12000):
        n = rng.randint(2, 8)
        d = rng.randint(1, min(4, n))
        cmax = rng.randint(1, 6)
        costs = [rng.randint(0, cmax) for _ in range(n)]
        k_bad = rng.randint(1, 8)

        layers = []
        for _j in range(d):
            p = list(range(n))
            rng.shuffle(p)
            layers.append(p)

        blocked = [[rng.random() < 0.25 for _a in range(n)] for _j in range(d)]
        causes = [[rng.randrange(k_bad) for _a in range(n)] for _j in range(d)]

        delta_sum = 0
        cap_sum = 0
        for threshold in range(1, cmax + 2):
            best_delta = 0
            for X in subsets(n):
                low_neigh = set()
                loads = [0] * k_bad
                for a in X:
                    for j in range(d):
                        b = layers[j][a]
                        good = (not blocked[j][a]) and costs[b] < threshold
                        if good:
                            low_neigh.add(b)
                        else:
                            loads[causes[j][a]] += 1
                delta = max(0, len(X) - len(low_neigh))
                assert sum(loads) >= d * delta
                if delta > 0:
                    assert max(loads) * k_bad >= d * delta
                best_delta = max(best_delta, delta)
            delta_sum += best_delta

            threshold_caps = [0] * k_bad
            for X in subsets(n):
                loads = [0] * k_bad
                for a in X:
                    for j in range(d):
                        b = layers[j][a]
                        good = (not blocked[j][a]) and costs[b] < threshold
                        if not good:
                            loads[causes[j][a]] += 1
                for p in range(k_bad):
                    threshold_caps[p] = max(threshold_caps[p], loads[p])
            assert d * best_delta <= sum(threshold_caps)
            cap_sum += sum(threshold_caps)
            counts["thresholds"] += 1
            counts["deficiency_units"] += best_delta
            counts["bad_incidence_capacity"] += sum(threshold_caps)

        assert d * delta_sum <= cap_sum
        counts["systems"] += 1
        counts["candidate_incidences"] += n * d

    print("AC low-event cut/cause audit passed")
    for key in sorted(counts):
        print(f"  {key.replace('_', ' ')}: {counts[key]}")


if __name__ == "__main__":
    main()
