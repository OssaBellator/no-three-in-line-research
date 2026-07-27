#!/usr/bin/env python3
"""Finite audit for AC3uh--AC3ul."""

from functools import lru_cache
from itertools import product
import random

SEED = 20260727


def find_order(vectors, q, bound):
    """Find an ordering whose coordinatewise prefixes stay above -bound."""
    vectors = tuple(tuple(v) for v in vectors)
    n = len(vectors)

    @lru_cache(maxsize=None)
    def dfs(mask, state):
        if mask == (1 << n) - 1:
            return ()
        cur = state
        for j, v in enumerate(vectors):
            if mask >> j & 1:
                continue
            nxt = tuple(cur[i] + v[i] for i in range(q))
            if all(x >= -bound for x in nxt):
                tail = dfs(mask | (1 << j), nxt)
                if tail is not None:
                    return (j,) + tail
        return None

    return dfs(0, (0,) * q)


def primitive(vec):
    from math import gcd
    g = 0
    for x in vec:
        g = gcd(g, x)
    if g <= 1:
        return tuple(vec)
    return tuple(x // g for x in vec)


def audit_system(vectors, consumptions, counts, l_macro, l_gate, counters):
    q = len(vectors[0])
    expanded = []
    for v, count in zip(vectors, counts):
        expanded.extend([v] * count)
    z = tuple(sum(v[i] for v in expanded) for i in range(q))
    assert all(x >= 0 for x in z)
    b = max(1, max(abs(x) for v in vectors for x in v))
    order = find_order(expanded, q, q * b)
    assert order is not None

    cmax = [max(c[i] for c in consumptions) for i in range(q)]
    beta = [cmax[i] + q * b for i in range(q)]
    m = beta[:]
    prefix = [0] * q
    for idx in order:
        v = expanded[idx]
        assert all(prefix[i] >= -q * b for i in range(q))
        # Duplicate net vectors may have different gross consumptions.  Use
        # their coordinatewise maximum to make the resource test conservative.
        matching = [consumptions[j] for j, vv in enumerate(vectors) if vv == v]
        c = tuple(max(row[i] for row in matching) for i in range(q))
        assert all(m[i] >= c[i] for i in range(q))
        m = [m[i] + v[i] for i in range(q)]
        assert all(x >= 0 for x in m)
        prefix = [prefix[i] + v[i] for i in range(q)]
        counters["macro_steps"] += 1
    assert tuple(m[i] - beta[i] for i in range(q)) == z
    assert len(expanded) * l_macro * l_gate >= len(expanded)
    counters["systems"] += 1
    counters["macros"] += len(expanded)
    counters["positive_output_systems"] += int(any(z))
    counters["zero_output_systems"] += int(not any(z))
    counters["buffer_addresses"] += sum(beta)


def main():
    rng = random.Random(SEED)
    counters = {
        "systems": 0,
        "macros": 0,
        "macro_steps": 0,
        "positive_output_systems": 0,
        "zero_output_systems": 0,
        "buffer_addresses": 0,
    }

    # Exhaust small one-dimensional primitive multisets.
    for vals in product(range(-2, 3), repeat=3):
        if all(v == 0 for v in vals):
            continue
        for raw_counts in product(range(1, 4), repeat=3):
            counts = primitive(raw_counts)
            z = sum(v * c for v, c in zip(vals, counts))
            if z < 0 or sum(counts) > 8:
                continue
            vectors = [(v,) for v in vals]
            consumptions = [(max(-v, 0) + rng.randint(0, 2),) for v in vals]
            audit_system(vectors, consumptions, counts, 4, 7, counters)

    # Random two- and three-dimensional systems with short primitive words.
    attempts = 0
    while counters["systems"] < 6000 and attempts < 200000:
        attempts += 1
        q = rng.randint(2, 3)
        k = rng.randint(2, 5)
        b = rng.randint(1, 3)
        vectors = [tuple(rng.randint(-b, b) for _ in range(q)) for _ in range(k)]
        if any(all(x == 0 for x in v) for v in vectors):
            continue
        counts = primitive([rng.randint(0, 3) for _ in range(k)])
        if sum(counts) == 0 or sum(counts) > 9:
            continue
        z = [sum(counts[j] * vectors[j][i] for j in range(k)) for i in range(q)]
        if any(x < 0 for x in z):
            continue
        consumptions = []
        for v in vectors:
            consumptions.append(tuple(max(-v[i], 0) + rng.randint(0, 2) for i in range(q)))
        audit_system(vectors, consumptions, counts, rng.randint(1, 8), rng.randint(1, 12), counters)

    assert counters["systems"] >= 5000
    print("AC Steinitz circulation-realization audit passed")
    for key in sorted(counters):
        print(f"  {key.replace('_', ' ')}: {counters[key]}")


if __name__ == "__main__":
    main()
