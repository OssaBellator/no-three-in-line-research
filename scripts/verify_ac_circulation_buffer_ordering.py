#!/usr/bin/env python3
"""Finite audit for AC3uh--AC3ul."""

from collections import defaultdict
from itertools import combinations_with_replacement, product
import random

SEED = 20260727


def canonical_prefix_min(vectors):
    q = len(vectors[0]) if vectors else 1
    cur = [0] * q
    mins = [0] * q
    for vec in sorted(vectors):
        for i, value in enumerate(vec):
            cur[i] += value
            mins[i] = min(mins[i], cur[i])
    return mins, cur


def exhaustive(counts):
    alphabet = list(product(range(-1, 2), repeat=2))
    for n in range(1, 7):
        for ids in combinations_with_replacement(range(len(alphabet)), n):
            vectors = [alphabet[i] for i in ids]
            total = [sum(v[j] for v in vectors) for j in range(2)]
            if min(total) < 0:
                continue
            mins, final = canonical_prefix_min(vectors)
            assert all(value >= -(n - 1) for value in mins)
            assert final == total
            counts["exhaustive circulations"] += 1
            counts["exhaustive macro occurrences"] += n


def random_internal_path(net, p_cap, rng):
    q = len(net)
    length = rng.randint(1, 8)
    prefixes = []
    for _t in range(length - 1):
        prefixes.append(tuple(rng.randint(-p_cap, p_cap + abs(net[i])) for i in range(q)))
    prefixes.append(tuple(net))
    return prefixes


def sampled(counts):
    rng = random.Random(SEED)
    for _ in range(20000):
        q = rng.randint(1, 6)
        n = rng.randint(1, 18)
        b = rng.randint(0, 5)

        vectors = []
        for _j in range(n - 1):
            vectors.append(tuple(rng.randint(-b, b) for _ in range(q)))
        subtotal = [sum(v[i] for v in vectors) for i in range(q)]
        final = []
        for i in range(q):
            needed = max(-subtotal[i], -b)
            if needed > b:
                # Restart with a guaranteed nonnegative-total construction.
                final = None
                break
            final.append(rng.randint(needed, b))
        if final is None:
            vectors = []
            n = rng.randint(1, 12)
            for _j in range(n):
                vectors.append(tuple(rng.randint(0, b) for _ in range(q)))
        else:
            vectors.append(tuple(final))

        total = [sum(v[i] for v in vectors) for i in range(q)]
        assert min(total) >= 0
        n = len(vectors)
        mins, ordered_total = canonical_prefix_min(vectors)
        assert all(value >= -(n - 1) * b for value in mins)
        assert ordered_total == total

        p_cap = rng.randint(0, 8)
        paths = {vec: random_internal_path(vec, p_cap, rng) for vec in set(vectors)}
        p = max(
            [0]
            + [max(0, -prefix[i]) for path in paths.values() for prefix in path for i in range(q)]
        )
        buffer = (n - 1) * b + p
        stock = [buffer + rng.randint(0, 9) for _ in range(q)]
        cur = stock[:]
        for vec in sorted(vectors):
            start = cur[:]
            for prefix in paths[vec]:
                state = [start[i] + prefix[i] for i in range(q)]
                assert min(state) >= 0
            for i in range(q):
                cur[i] += vec[i]
        assert all(cur[i] >= stock[i] for i in range(q))

        l_macro = rng.randint(1, 11)
        l_gate = rng.randint(1, 17)
        macro_gates = {vec: rng.randint(1, l_macro) for vec in set(vectors)}
        gate_count = sum(macro_gates[vec] for vec in sorted(vectors))
        edge_count = sum(rng.randint(1, l_gate) for _ in range(gate_count))
        assert gate_count <= n * l_macro
        assert edge_count <= n * l_macro * l_gate

        counts["sampled systems"] += 1
        counts["sampled macro occurrences"] += n
        counts["sampled resource coordinates"] += q
        counts["sampled internal prefixes"] += sum(len(path) for path in paths.values())
        counts["full buffer units"] += q * buffer
        counts["completed gates"] += gate_count
        counts["control edges"] += edge_count
        if p > 0:
            counts["systems with internal deficit"] += 1
        if b == 0:
            counts["zero net-bound systems"] += 1


def main():
    counts = defaultdict(int)
    exhaustive(counts)
    sampled(counts)
    print("AC circulation buffer-ordering audit passed")
    for key in sorted(counts):
        print(f"  {key}: {counts[key]}")


if __name__ == "__main__":
    main()
