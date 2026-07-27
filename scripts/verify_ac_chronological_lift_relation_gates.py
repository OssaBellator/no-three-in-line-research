#!/usr/bin/env python3
"""Finite audit for AC3ti--AC3tm."""

from collections import deque, defaultdict
from itertools import product
from math import gcd
import random

SEED = 20260727


def shortest_paths(q, edges):
    adjacency = [[] for _ in range(q)]
    by_id = {}
    for edge_id, u, v, inc in edges:
        adjacency[u].append((edge_id, v))
        by_id[edge_id] = (u, v, inc)
    for row in adjacency:
        row.sort()

    paths = {}
    for source in range(q):
        paths[(source, source)] = ()
        queue = deque([source])
        best = {source: ()}
        while queue:
            u = queue.popleft()
            for edge_id, v in adjacency[u]:
                candidate = best[u] + (edge_id,)
                if v not in best:
                    best[v] = candidate
                    queue.append(v)
        assert len(best) == q
        for target, word in best.items():
            paths[(source, target)] = word
            assert len(word) <= q - 1
    return paths, by_id, adjacency


def canonical_cycle(edge_word, vertex_word):
    rotations = []
    k = len(edge_word)
    for i in range(k):
        rotations.append(
            (
                edge_word[i:] + edge_word[:i],
                vertex_word[i:] + vertex_word[:i],
            )
        )
    return min(rotations, key=lambda item: item[0])


def simple_cycles(q, edges, adjacency, by_id):
    found = {}
    for start in range(q):
        def dfs(u, vertices, edge_word):
            for edge_id, v in adjacency[u]:
                if v == start:
                    word = edge_word + (edge_id,)
                    verts = tuple(vertices)
                    cword, cverts = canonical_cycle(word, verts)
                    drift = sum(by_id[e][2] for e in cword)
                    found[cword] = (cverts[0], drift)
                elif v not in vertices and len(vertices) < q:
                    dfs(v, vertices + [v], edge_word + (edge_id,))
        dfs(start, [start], ())
    return [
        {"word": word, "base": base, "drift": drift}
        for word, (base, drift) in sorted(found.items())
    ]


def simulate(word, start, by_id):
    vertex = start
    drift = 0
    for edge_id in word:
        u, v, inc = by_id[edge_id]
        assert u == vertex
        vertex = v
        drift += inc
    return vertex, drift


def macro_word(root, relation_cycles, paths):
    ordered = sorted(
        relation_cycles,
        key=lambda cycle: cycle["word"],
    )
    word = list(paths[(root, ordered[0]["base"])])
    for index, cycle in enumerate(ordered):
        word.extend(cycle["word"])
        target = root if index + 1 == len(ordered) else ordered[index + 1]["base"]
        word.extend(paths[(cycle["base"], target)])
    return tuple(word), ordered


def primitive_pair_relation(pos_cycle, neg_cycle):
    pos = pos_cycle["drift"]
    neg = -neg_cycle["drift"]
    common = gcd(pos, neg)
    return [pos_cycle] * (neg // common) + [neg_cycle] * (pos // common)


def exhaustive_primitive_bound():
    checks = 0
    for values in (
        (-3, 2),
        (-2, -1, 3),
        (-3, 1, 2),
        (-4, -1, 3),
        (-3, -2, 1, 2),
    ):
        p = max(v for v in values if v > 0)
        n = max(-v for v in values if v < 0)
        limit = p + n
        for counts in product(range(limit + 1), repeat=len(values)):
            size = sum(counts)
            if size == 0 or size > limit:
                continue
            if sum(c * v for c, v in zip(counts, values)) != 0:
                continue
            primitive = True
            ranges = [range(c + 1) for c in counts]
            for sub in product(*ranges):
                if all(x == 0 for x in sub) or sub == counts:
                    continue
                if sum(x * v for x, v in zip(sub, values)) == 0:
                    primitive = False
                    break
            if primitive:
                assert size <= limit
                checks += 1
    return checks


def main():
    rng = random.Random(SEED)
    counts = defaultdict(int)
    counts["exhaustive_primitive_relations"] = exhaustive_primitive_bound()

    for _ in range(4500):
        q = rng.randint(2, 6)
        edge_specs = set()

        # Bidirected cycle guarantees strong connectivity.
        for u in range(q):
            v = (u + 1) % q
            edge_specs.add((u, v))
            edge_specs.add((v, u))
        for _ in range(rng.randint(q, 3 * q)):
            edge_specs.add((rng.randrange(q), rng.randrange(q)))

        edges = []
        amplitude = rng.randint(1, 6)
        for edge_id, (u, v) in enumerate(sorted(edge_specs)):
            increment = rng.randint(-amplitude, amplitude)
            edges.append((edge_id, u, v, increment))

        paths, by_id, adjacency = shortest_paths(q, edges)
        cycles = simple_cycles(q, edges, adjacency, by_id)
        counts["graphs"] += 1
        counts["connector_paths"] += q * q
        counts["simple_cycles"] += len(cycles)

        amax = max(abs(edge[3]) for edge in edges)
        for (u, v), path in paths.items():
            end, drift = simulate(path, u, by_id)
            assert end == v
            assert len(path) <= q - 1
            assert abs(drift) <= (q - 1) * amax

        positive = [cycle for cycle in cycles if cycle["drift"] > 0]
        negative = [cycle for cycle in cycles if cycle["drift"] < 0]
        if not positive or not negative:
            continue

        p = max(cycle["drift"] for cycle in positive)
        n = max(-cycle["drift"] for cycle in negative)
        relation_limit = p + n
        root = 0
        macros = []

        for _sample in range(min(8, len(positive) * len(negative))):
            pos_cycle = rng.choice(positive)
            neg_cycle = rng.choice(negative)
            relation = primitive_pair_relation(pos_cycle, neg_cycle)
            assert len(relation) <= relation_limit
            assert sum(cycle["drift"] for cycle in relation) == 0

            word, ordered = macro_word(root, relation, paths)
            end, beta = simulate(word, root, by_id)
            assert end == root

            connector_drift = beta - sum(cycle["drift"] for cycle in ordered)
            assert connector_drift == beta
            k = len(relation)
            length_bound = k * q + (k + 1) * (q - 1)
            assert len(word) <= length_bound
            assert abs(beta) <= (k + 1) * (q - 1) * amax
            assert len(word) <= (2 * q - 1) * relation_limit + (q - 1)
            macros.append((word, beta))
            counts["first_level_relations"] += 1
            counts["macro_edges"] += len(word)

        positive_macros = [item for item in macros if item[1] > 0]
        negative_macros = [item for item in macros if item[1] < 0]
        if positive_macros and negative_macros:
            pword, pdef = rng.choice(positive_macros)
            nword, ndef = rng.choice(negative_macros)
            common = gcd(pdef, -ndef)
            pcount = (-ndef) // common
            ncount = pdef // common
            assert pcount + ncount <= pdef + (-ndef)
            second_word = pword * pcount + nword * ncount
            end, drift = simulate(second_word, root, by_id)
            assert end == root
            assert drift == 0
            lmac = (2 * q - 1) * relation_limit + (q - 1)
            assert len(second_word) <= (pdef + (-ndef)) * lmac
            counts["second_level_returns"] += 1
            counts["second_level_edges"] += len(second_word)

    print("AC chronological lift-relation audit passed")
    for key in sorted(counts):
        print(f"  {key.replace('_', ' ')}: {counts[key]}")


if __name__ == "__main__":
    main()
