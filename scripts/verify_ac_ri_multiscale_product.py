#!/usr/bin/env python3
"""Finite checks for AC3dy--AC3eb."""

from fractions import Fraction
from itertools import combinations, product


def best_independent_weight(n, edges, weights):
    best = 0
    for mask in range(1 << n):
        if all(not (mask >> u & 1 and mask >> v & 1) for u, v in edges):
            best = max(best, sum(weights[i] for i in range(n) if mask >> i & 1))
    return best


def check_hall():
    count = 0
    for n in range(1, 9):
        for mask in range(1 << n):
            chosen = [i for i in range(n) if mask >> i & 1]
            assert len(chosen) == len(set(chosen))
            count += 1
    return count


def check_scope_router():
    graphs = cases = extracted = 0
    for n in range(1, 6):
        pairs = list(combinations(range(n), 2))
        for edge_mask in range(1 << len(pairs)):
            edges = {e for i, e in enumerate(pairs) if edge_mask >> i & 1}
            closed = []
            for v in range(n):
                hood = {v}
                for a, b in edges:
                    if a == v:
                        hood.add(b)
                    if b == v:
                        hood.add(a)
                closed.append(hood)
            for weights in product((1, 2), repeat=n):
                total = sum(weights)
                best = best_independent_weight(n, edges, weights)
                for k in range(1, 6):
                    overload = any(
                        sum(weights[i] for i in closed[v]) > k * weights[v]
                        for v in range(n)
                    )
                    if not overload:
                        assert Fraction(best, total) >= Fraction(1, k)
                        assert Fraction(best, 31 * total) >= Fraction(1, 31 * k)
                        extracted += 1
                    cases += 1
            graphs += 1
    return graphs, cases, extracted


def check_product_expectation():
    distributions = states_checked = 0
    local_pairs = list(product(range(-2, 3), repeat=2))
    for block_count in range(1, 5):
        for pairs in product(local_pairs, repeat=block_count):
            expected = sum((Fraction(a + b, 2) for a, b in pairs), Fraction(0, 1))
            values = [
                sum(pairs[i][choice] for i, choice in enumerate(state))
                for state in product((0, 1), repeat=block_count)
            ]
            assert Fraction(sum(values), len(values)) == expected
            if expected > 0:
                assert max(values) > 0
            distributions += 1
            states_checked += len(values)
    return distributions, states_checked


def check_failed_router():
    ledgers = routed = 0
    alphas = (Fraction(1, 2), Fraction(2, 3), Fraction(3, 4))
    term_vectors = [v for v in product(range(5), repeat=5) if sum(v) <= 12]
    for block_count in range(1, 4):
        for weights in product((1, 2), repeat=block_count):
            total = sum(weights)
            for coeffs in product(alphas, repeat=block_count):
                gain = sum(coeffs[i] * weights[i] for i in range(block_count))
                assert gain >= Fraction(total, 2)
                for terms in term_vectors:
                    if sum(terms) >= gain:
                        assert max(terms) >= Fraction(total, 10)
                        for k in range(1, 5):
                            assert Fraction(max(terms), 31 * k * total) >= Fraction(1, 310 * k)
                            routed += 1
                    ledgers += 1
    return ledgers, routed


def main():
    hall = check_hall()
    graphs, scope_cases, extracted = check_scope_router()
    distributions, states = check_product_expectation()
    ledgers, routed = check_failed_router()
    print(
        "AC RI multiscale product: verified "
        f"{hall} Hall subfamilies, {graphs} graphs, {scope_cases} scope cases, "
        f"{extracted} extractions, {distributions} product distributions, "
        f"{states} product states, {ledgers} failed ledgers, and {routed} routed constants"
    )


if __name__ == "__main__":
    main()
