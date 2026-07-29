#!/usr/bin/env python3
import math
import random
from collections import Counter


def greedy_matching(edges):
    used_left, used_right, matching = set(), set(), []
    for left, right in sorted(edges):
        if left not in used_left and right not in used_right:
            matching.append((left, right))
            used_left.add(left)
            used_right.add(right)
    return matching


def run(seed=20260729, systems=2500):
    rng = random.Random(seed)
    counts = Counter()
    for _ in range(systems):
        m = rng.randint(1, 12)
        n = rng.randint(m, 18)
        q = rng.randint(1, 8)
        labels = {(u, v): rng.randrange(q) for u in range(m) for v in range(n)}
        masses = Counter(labels.values())
        predicate = min(p for p, c in masses.items() if c == max(masses.values()))
        edges = [edge for edge, label in labels.items() if label == predicate]
        e = len(edges)
        assert e * q >= m * n >= m * m

        degree_cap = rng.randint(1, max(m, n))
        left_degree = Counter(u for u, _ in edges)
        right_degree = Counter(v for _, v in edges)
        if max([0] + list(left_degree.values()) + list(right_degree.values())) > degree_cap:
            counts['stars'] += 1
            continue

        matching = greedy_matching(edges)
        assert len(matching) >= math.ceil(e / (2 * degree_cap - 1))
        witness_count = rng.randint(1, max(1, len(matching)))
        witness = {edge: rng.randrange(witness_count) for edge in matching}
        multiplicity_cap = rng.randint(1, max(1, len(matching)))
        multiplicities = Counter(witness.values())
        if max(multiplicities.values()) > multiplicity_cap:
            counts['overloads'] += 1
            continue

        representatives = {}
        for edge in matching:
            representatives.setdefault(witness[edge], edge)
        stock = list(representatives.values())
        assert len(stock) >= math.ceil(len(matching) / multiplicity_cap)
        assert len({u for u, _ in stock}) == len(stock)
        assert len({v for _, v in stock}) == len(stock)
        assert len({witness[edge] for edge in stock}) == len(stock)
        counts['stocks'] += 1
        counts['stock_edges'] += len(stock)

    print(dict(counts))
    print(f'checked {systems} RI predicate rectangles')


if __name__ == '__main__':
    run()
