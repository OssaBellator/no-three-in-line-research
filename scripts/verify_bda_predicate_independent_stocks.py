#!/usr/bin/env python3
import math
import random
from collections import Counter


def greedy_matching(edges):
    used_l, used_r, out = set(), set(), []
    for u, v in sorted(edges):
        if u not in used_l and v not in used_r:
            out.append((u, v)); used_l.add(u); used_r.add(v)
    return out


def run(seed=20260730, systems=2500):
    rng = random.Random(seed)
    stats = Counter()
    for _ in range(systems):
        m, n, q = rng.randint(1, 12), rng.randint(1, 18), rng.randint(1, 8)
        n = max(n, m)
        labels = {(u, v): rng.randrange(q) for u in range(m) for v in range(n)}
        masses = Counter(labels.values())
        p = min(k for k, value in masses.items() if value == max(masses.values()))
        edges = [edge for edge, label in labels.items() if label == p]
        e = len(edges)
        assert e * q >= m * n >= m * m
        D = rng.randint(1, max(m, n))
        dl, dr = Counter(u for u, _ in edges), Counter(v for _, v in edges)
        if max([0] + list(dl.values()) + list(dr.values())) > D:
            stats['stars'] += 1
            continue
        matching = greedy_matching(edges)
        assert len(matching) >= math.ceil(e / (2 * D - 1))
        witness = {edge: rng.randrange(max(1, len(matching))) for edge in matching}
        mu = rng.randint(1, max(1, len(matching)))
        mult = Counter(witness.values())
        if max(mult.values()) > mu:
            stats['overloads'] += 1
            continue
        reps = {}
        for edge in matching:
            reps.setdefault(witness[edge], edge)
        stock = list(reps.values())
        assert len(stock) >= math.ceil(len(matching) / mu)
        assert len({u for u, _ in stock}) == len(stock)
        assert len({v for _, v in stock}) == len(stock)
        assert len({witness[e] for e in stock}) == len(stock)
        stats['stocks'] += 1
        stats['stock_edges'] += len(stock)
    print(dict(stats))
    print(f'checked {systems} BDA predicate rectangles')


if __name__ == '__main__':
    run()
