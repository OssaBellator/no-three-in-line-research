#!/usr/bin/env python3
"""Verify GC4m--GC4p shared-token union and weighted router bounds."""
from itertools import product


def verify(max_ops=5, max_factors=5):
    checks = 0
    for n in range(1, max_ops + 1):
        for f in range(1, max_factors + 1):
            for masks in product(range(1 << (f - 1)), repeat=n):
                weights = [1 + j for j in range(f)]
                noncommon_incidence = 0
                reuse = [0] * f
                union = {0}
                local = []
                for mask in masks:
                    s = 0
                    for q in range(1, f):
                        if mask >> (q - 1) & 1:
                            reuse[q] += 1
                            union.add(q)
                            noncommon_incidence += weights[q]
                            s += weights[q]
                    local.append(s)
                r = max([1] + reuse[1:])
                union_weight = sum(weights[q] for q in union)
                assert union_weight >= weights[0] + noncommon_incidence / r
                lambdas = [s if i % 2 == 0 else 2 * s + 1 for i, s in enumerate(local)]
                eligible = [i for i in range(n) if lambdas[i] <= 2 * local[i]]
                under = [i for i in range(n) if i not in eligible]
                W = sum(lambdas)
                if sum(lambdas[i] for i in eligible) >= W / 2:
                    P = sum(local[i] for i in eligible)
                    assert P >= sum(lambdas[i] for i in eligible) / 2
                else:
                    assert sum(lambdas[i] for i in under) > W / 2
                checks += 1
    return checks


def main():
    print(f"GC same-token union payment: verified {verify()} weighted incidence systems")


if __name__ == '__main__':
    main()
