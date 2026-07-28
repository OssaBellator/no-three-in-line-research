#!/usr/bin/env python3
"""Finite audit for AC3uh--AC3ul."""

from collections import defaultdict
from functools import lru_cache
from itertools import combinations_with_replacement, product
import random

SEED = 20260728


def find_buffered_order(vectors, q, b):
    """Return an index order with every boundary prefix >= -2*q*b."""
    n = len(vectors)
    lower = -2 * q * b

    @lru_cache(None)
    def dfs(mask, prefix):
        if mask == (1 << n) - 1:
            return ()
        used_values = set()
        for j, v in enumerate(vectors):
            if mask >> j & 1 or v in used_values:
                continue
            used_values.add(v)
            nxt = tuple(prefix[i] + v[i] for i in range(q))
            if min(nxt) < lower:
                continue
            tail = dfs(mask | (1 << j), nxt)
            if tail is not None:
                return (j,) + tail
        return None

    return dfs(0, (0,) * q)


def random_internal_word(v, rng):
    """Make a small integer step word with exact net increment v."""
    q = len(v)
    steps = []
    for i, target in enumerate(v):
        sign = 1 if target >= 0 else -1
        for _ in range(abs(target)):
            step = [0] * q
            step[i] = sign
            steps.append(tuple(step))
    # Insert cancelling excursions, which may increase internal drawdown.
    for _ in range(rng.randint(0, 3)):
        i = rng.randrange(q)
        step1 = [0] * q
        step2 = [0] * q
        if rng.random() < 0.5:
            step1[i], step2[i] = -1, 1
        else:
            step1[i], step2[i] = 1, -1
        pos = rng.randrange(len(steps) + 1)
        steps[pos:pos] = [tuple(step1), tuple(step2)]
    return steps


def drawdown(word, q):
    cur = [0] * q
    d = [0] * q
    for step in word:
        for i in range(q):
            cur[i] += step[i]
            d[i] = max(d[i], -cur[i])
    return d, tuple(cur)


def audit_system(vectors, rng, counts):
    q = len(vectors[0])
    b = max(1, max(abs(x) for v in vectors for x in v))
    total = tuple(sum(v[i] for v in vectors) for i in range(q))
    assert min(total) >= 0

    order = find_buffered_order(tuple(vectors), q, b)
    assert order is not None

    prefix = [0] * q
    for j in order:
        for i in range(q):
            prefix[i] += vectors[j][i]
        assert min(prefix) >= -2 * q * b
        counts["boundary_prefixes"] += 1
    assert tuple(prefix) == total

    words = [random_internal_word(v, rng) for v in vectors]
    d_all = []
    for v, word in zip(vectors, words):
        d, net = drawdown(word, q)
        assert net == v
        d_all.extend(d)
    D = max(d_all, default=0)

    resources = [2 * q * b + D] * q
    initial = tuple(resources)
    gates = 0
    edges = 0
    l_macro = max(1, max(len(w) for w in words))
    l_gate = rng.randint(1, 7)
    for j in order:
        for step in words[j]:
            for i in range(q):
                resources[i] += step[i]
                assert resources[i] >= 0
            edges += l_gate
        gates += len(words[j])
    assert tuple(resources[i] - initial[i] for i in range(q)) == total
    assert gates <= len(vectors) * l_macro
    assert edges <= len(vectors) * l_macro * l_gate

    counts["systems"] += 1
    counts["macro_occurrences"] += len(vectors)
    counts["internal_edges"] += sum(len(w) for w in words)
    counts["buffer_units"] += q * (2 * q * b + D)


def main():
    rng = random.Random(SEED)
    counts = defaultdict(int)

    # Exhaustive small one- and two-resource nondecreasing multisets.
    for q in (1, 2):
        alphabet = list(product((-1, 0, 1), repeat=q))
        alphabet.remove((0,) * q)
        for n in range(1, 6):
            for idxs in combinations_with_replacement(range(len(alphabet)), n):
                vectors = [alphabet[j] for j in idxs]
                total = [sum(v[i] for v in vectors) for i in range(q)]
                if min(total) < 0:
                    continue
                audit_system(vectors, rng, counts)
                counts["exhaustive_systems"] += 1

    # Random larger systems in dimensions up to four.
    for _ in range(12000):
        q = rng.randint(1, 4)
        b = rng.randint(1, 4)
        n = rng.randint(1, 9)
        for _attempt in range(200):
            vectors = [
                tuple(rng.randint(-b, b) for _ in range(q))
                for _ in range(n)
            ]
            if all(all(x == 0 for x in v) for v in vectors):
                continue
            total = [sum(v[i] for v in vectors) for i in range(q)]
            if min(total) >= 0:
                break
        else:
            # Guaranteed fallback: unit positive vectors.
            vectors = [tuple(1 if i == j % q else 0 for i in range(q)) for j in range(n)]
        audit_system(vectors, rng, counts)
        counts["random_systems"] += 1

    print("AC buffered circulation-ordering audit passed")
    for key in sorted(counts):
        print(f"  {key.replace('_', ' ')}: {counts[key]}")


if __name__ == "__main__":
    main()
