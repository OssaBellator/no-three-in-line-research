#!/usr/bin/env python3
"""Finite audit for AC3uc--AC3ug."""

from __future__ import annotations

from collections import defaultdict
from itertools import product
from math import ceil, gcd
import random

SEED = 20260727


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def normalize(values):
    g = 0
    for value in values:
        g = gcd(g, abs(value))
    if g <= 1:
        return tuple(values)
    return tuple(value // g for value in values)


def find_rank(vectors, q, limit):
    for w in product(range(1, limit + 1), repeat=q):
        if all(dot(w, v) < 0 for v in vectors):
            return w
    return None


def find_primitive_witness(vectors, q, coeff_limit):
    k = len(vectors)
    best = None
    for x in product(range(coeff_limit + 1), repeat=k):
        if not any(x):
            continue
        z = tuple(sum(x[j] * vectors[j][i] for j in range(k)) for i in range(q))
        if min(z) < 0:
            continue
        combined = normalize(tuple(x) + z)
        x_n = combined[:k]
        z_n = combined[k:]
        support = sum(value > 0 for value in combined)
        key = (support, sum(x_n), max(combined), combined)
        if best is None or key < best[0]:
            best = (key, x_n, z_n)
    return None if best is None else (best[1], best[2])


def exhaustive_small(counts):
    for q in (1, 2):
        b = 2
        d_q = ceil((q ** (q / 2)) * (b**q))
        rank_limit = 24
        max_k = 3 if q == 1 else 2
        for k in range(1, max_k + 1):
            coordinate_vectors = list(product(range(-b, b + 1), repeat=q))
            for vectors in product(coordinate_vectors, repeat=k):
                rank = find_rank(vectors, q, rank_limit)
                witness = find_primitive_witness(vectors, q, d_q)
                assert (rank is None) != (witness is None)
                if rank is not None:
                    assert all(dot(rank, v) <= -1 for v in vectors)
                    counts["exhaustive rank systems"] += 1
                else:
                    x, z = witness
                    vx = tuple(sum(x[j] * vectors[j][i] for j in range(k)) for i in range(q))
                    assert vx == z
                    assert min(z) >= 0
                    combined = tuple(x) + tuple(z)
                    assert sum(value > 0 for value in combined) <= q + 1
                    assert max(combined) <= d_q
                    assert sum(x) <= (q + 1) * d_q
                    counts["exhaustive circulation systems"] += 1
                    counts["primitive circulation occurrences"] += sum(x)
                counts["exhaustive systems"] += 1


def random_small_alternatives(counts):
    rng = random.Random(SEED + 1)
    q = 2
    b = 2
    d_q = ceil((q ** (q / 2)) * (b**q))
    coordinate_vectors = list(product(range(-b, b + 1), repeat=q))
    for _ in range(500):
        k = 3
        vectors = tuple(rng.choice(coordinate_vectors) for _j in range(k))
        rank = find_rank(vectors, q, 24)
        witness = find_primitive_witness(vectors, q, d_q)
        assert (rank is None) != (witness is None)
        if rank is not None:
            assert all(dot(rank, v) < 0 for v in vectors)
            counts["sampled small rank systems"] += 1
        else:
            x, z = witness
            assert tuple(sum(x[j] * vectors[j][i] for j in range(k)) for i in range(q)) == z
            assert min(z) >= 0
            assert sum(value > 0 for value in tuple(x) + tuple(z)) <= q + 1
            assert max(tuple(x) + tuple(z)) <= d_q
            counts["sampled small circulation systems"] += 1
            counts["sampled circulation occurrences"] += sum(x)
        counts["sampled small systems"] += 1


def random_rank_histories(counts):
    rng = random.Random(SEED)
    for _ in range(8000):
        q = rng.randint(2, 6)
        k = rng.randint(1, 9)
        w = [rng.randint(1, 8) for _ in range(q)]
        vectors = []
        gross = []
        for _j in range(k):
            while True:
                v = [rng.randint(-5, 5) for _ in range(q)]
                if dot(w, v) <= -1:
                    break
            c = [max(-value, 0) + rng.randint(0, 2) for value in v]
            r = [c[i] + v[i] for i in range(q)]
            assert min(r) >= 0
            vectors.append(v)
            gross.append((c, r))

        m0 = [rng.randint(10, 40) for _ in range(q)]
        m = m0[:]
        h0 = dot(w, m0)
        delta = min(-dot(w, v) for v in vectors)
        l_macro = rng.randint(1, 12)
        l_gate = rng.randint(1, 20)
        steps = 0
        gates = 0
        edges = 0

        while True:
            legal = []
            for j, (c, _r) in enumerate(gross):
                if all(m[i] >= c[i] for i in range(q)):
                    m_next = [m[i] + vectors[j][i] for i in range(q)]
                    if min(m_next) >= 0:
                        legal.append(j)
            if not legal:
                break
            j = rng.choice(legal)
            h_old = dot(w, m)
            m = [m[i] + vectors[j][i] for i in range(q)]
            h_new = dot(w, m)
            assert h_new - h_old == dot(w, vectors[j]) <= -delta
            macro_gates = rng.randint(1, l_macro)
            macro_edges = sum(rng.randint(1, l_gate) for _ in range(macro_gates))
            gates += macro_gates
            edges += macro_edges
            steps += 1
            assert steps <= h0 // delta

        assert gates <= (h0 // delta) * l_macro
        assert edges <= (h0 // delta) * l_macro * l_gate
        counts["random ranked systems"] += 1
        counts["ranked macro steps"] += steps
        counts["ranked completed gates"] += gates
        counts["ranked control edges"] += edges


def main():
    counts = defaultdict(int)
    exhaustive_small(counts)
    random_small_alternatives(counts)
    random_rank_histories(counts)
    print("AC coupled-resource cone audit passed")
    for key in sorted(counts):
        print(f"  {key}: {counts[key]}")


if __name__ == "__main__":
    main()
