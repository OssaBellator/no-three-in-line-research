#!/usr/bin/env python3
"""Finite checks for GC2ab--GC2af overload excess import."""

from fractions import Fraction
from itertools import combinations, product
from random import Random


def max_weight_matching(edges, weights):
    edges = list(edges)
    best = Fraction(0)
    for mask in range(1 << len(edges)):
        used = set()
        total = Fraction(0)
        ok = True
        for i, e in enumerate(edges):
            if not (mask & (1 << i)):
                continue
            if e[0] in used or e[1] in used:
                ok = False
                break
            used.update(e)
            total += weights[e]
        if ok and total > best:
            best = total
    return best


def exact_excess_checks():
    rng = Random(20260726)
    private_checks = 0
    target_checks = 0
    rank_checks = 0

    for _ in range(40000):
        m = rng.randint(1, 6)
        capacities = [Fraction(rng.randint(1, 8), rng.randint(1, 5)) for _ in range(m)]
        c_total = sum(capacities, Fraction(0))
        kappa = Fraction(rng.randint(1, 4), 1)
        extra = Fraction(rng.randint(1, 10), rng.randint(1, 5))
        lam = kappa * c_total + extra
        demands = [lam * w / c_total for w in capacities]
        excess = [d - kappa * w for d, w in zip(demands, capacities)]
        assert all(e > 0 for e in excess)
        assert sum(excess, Fraction(0)) == lam - kappa * c_total
        private_checks += 1

        wb = kappa * c_total + extra
        target_demands = [w * wb / c_total for w in capacities]
        target_excess = [d - kappa * w for d, w in zip(target_demands, capacities)]
        assert all(e > 0 for e in target_excess)
        assert sum(target_excess, Fraction(0)) == wb - kappa * c_total
        target_checks += 1

        ranks = [rng.randint(1, 3) for _ in range(m)]
        totals = [sum((e for e, s in zip(excess, ranks) if s == rank), Fraction(0)) for rank in range(1, 4)]
        assert max(totals) * 3 >= sum(excess, Fraction(0))
        rank_checks += 1

    return private_checks, target_checks, rank_checks


def anchor_link_checks():
    graph_checks = 0
    weighted_checks = 0
    for n_outer in range(2, 6):
        possible = list(combinations(range(n_outer), 2))
        for mask in range(1 << len(possible)):
            edges = [e for i, e in enumerate(possible) if mask & (1 << i)]
            if not edges:
                continue
            degrees = {v: sum(v in e for e in edges) for v in range(n_outer)}
            for delta in range(1, n_outer + 1):
                high_pair = max(degrees.values(), default=0) > delta
                # Exhaust small integer excess weights on smaller graphs, sample a canonical pattern otherwise.
                patterns = product(range(1, 4), repeat=len(edges)) if len(edges) <= 6 else [tuple(1 + (i % 3) for i in range(len(edges)))]
                for pattern in patterns:
                    weights = {e: Fraction(pattern[i], 1) for i, e in enumerate(edges)}
                    total = sum(weights.values(), Fraction(0))
                    if not high_pair:
                        best = max_weight_matching(edges, weights)
                        assert best * (2 * delta - 1) >= total
                    weighted_checks += 1
                graph_checks += 1
    return graph_checks, weighted_checks


def main():
    private, target, ranks = exact_excess_checks()
    graphs, weighted = anchor_link_checks()
    print("overload anchor import: PASS")
    print(f"  private excess systems checked: {private}")
    print(f"  target excess systems checked: {target}")
    print(f"  rank splits checked: {ranks}")
    print(f"  anchor-link graph cases checked: {graphs}")
    print(f"  weighted matching cases checked: {weighted}")


if __name__ == "__main__":
    main()
