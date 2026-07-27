#!/usr/bin/env python3
"""Finite audit for AC3td--AC3th."""

from collections import Counter, defaultdict
from itertools import product
import random

SEED = 20260727


def primitive_zero_sum(vec, vals):
    if sum(v * c for v, c in zip(vals, vec)) != 0 or sum(vec) == 0:
        return False
    ranges = [range(c + 1) for c in vec]
    for sub in product(*ranges):
        if sub == tuple(0 for _ in vec) or sub == vec:
            continue
        if sum(v * c for v, c in zip(vals, sub)) == 0:
            return False
    return True


def extract_relations(counter, vals):
    counter = list(counter)
    relations = []
    while True:
        found = None
        ranges = [range(c + 1) for c in counter]
        for sub in product(*ranges):
            if not any(sub):
                continue
            if sum(v * c for v, c in zip(vals, sub)) == 0:
                cur = list(sub)
                changed = True
                while changed:
                    changed = False
                    for cand in product(*[range(c + 1) for c in cur]):
                        if not any(cand) or cand == tuple(cur):
                            continue
                        if sum(v * c for v, c in zip(vals, cand)) == 0:
                            cur = list(cand)
                            changed = True
                            break
                found = tuple(cur)
                break
        if found is None:
            return relations, tuple(counter)
        relations.append(found)
        counter = [c - f for c, f in zip(counter, found)]


def random_walk_decompose(q, edges, length, rng):
    start = rng.randrange(q)
    vertices = [start]
    edge_word = []
    for _ in range(length):
        edge = rng.choice(edges[vertices[-1]])
        edge_word.append(edge)
        vertices.append(edge[0])

    stack_vertices = [vertices[0]]
    stack_edges = []
    cycles = []
    position = {vertices[0]: 0}
    for edge in edge_word:
        vertex = edge[0]
        stack_edges.append(edge)
        stack_vertices.append(vertex)
        if vertex in position:
            index = position[vertex]
            cycles.append(stack_edges[index:])
            stack_edges = stack_edges[:index]
            stack_vertices = stack_vertices[: index + 1]
            position = {x: j for j, x in enumerate(stack_vertices)}
        else:
            position[vertex] = len(stack_vertices) - 1

    return edge_word, stack_edges, cycles


def main():
    rng = random.Random(SEED)
    counts = defaultdict(int)

    alphabets = [
        (-3, 1),
        (-2, 1),
        (-1, 2),
        (-3, -1, 2),
        (-2, 1, 3),
        (-3, -2, 1, 2),
    ]
    for vals in alphabets:
        positive = max(v for v in vals if v > 0)
        negative = max(-v for v in vals if v < 0)
        limit = positive + negative
        for vec in product(range(limit + 1), repeat=len(vals)):
            if sum(vec) > limit:
                continue
            if primitive_zero_sum(vec, vals):
                assert sum(vec) <= positive + negative
                counts["primitive_relations"] += 1

    for _ in range(12000):
        q = rng.randint(2, 8)
        max_increment = rng.randint(1, 8)
        edges = [[] for _ in range(q)]
        edge_id = 0
        for source in range(q):
            target = (source + 1) % q
            alpha = rng.randint(-max_increment, max_increment)
            edges[source].append((target, alpha, edge_id))
            edge_id += 1
        for _ in range(rng.randint(q, 3 * q)):
            source = rng.randrange(q)
            target = rng.randrange(q)
            alpha = rng.randint(-max_increment, max_increment)
            edges[source].append((target, alpha, edge_id))
            edge_id += 1

        word, residual, cycles = random_walk_decompose(
            q,
            edges,
            rng.randint(1, 100),
            rng,
        )
        assert len(residual) <= q - 1
        assert all(len(cycle) <= q for cycle in cycles)

        total = sum(edge[1] for edge in word)
        path_drift = sum(edge[1] for edge in residual)
        cycle_drifts = [sum(edge[1] for edge in cycle) for cycle in cycles]
        assert total == path_drift + sum(cycle_drifts)
        assert abs(path_drift) <= (q - 1) * max_increment

        nonzero = sorted(set(drift for drift in cycle_drifts if drift))
        if any(drift > 0 for drift in nonzero) and any(
            drift < 0 for drift in nonzero
        ):
            positive = max(drift for drift in nonzero if drift > 0)
            negative = max(-drift for drift in nonzero if drift < 0)
            counter = Counter(cycle_drifts)
            zero_count = counter.pop(0, 0)
            vals = tuple(sorted(counter))
            if sum(counter.values()) <= 12 and vals:
                relations, residual_counts = extract_relations(
                    tuple(counter[value] for value in vals),
                    vals,
                )
                for relation in relations:
                    assert primitive_zero_sum(relation, vals)
                    assert sum(relation) <= positive + negative

                residual_drift = sum(
                    value * count
                    for value, count in zip(vals, residual_counts)
                )
                assert sum(residual_counts) <= (
                    positive + negative + abs(residual_drift)
                )
                assert residual_drift == total - path_drift

                counts["relation_systems"] += 1
                counts["zero_cycle_occurrences"] += zero_count
                counts["extracted_relations"] += len(relations)
                counts["residual_cycles"] += sum(residual_counts)

                lift_width = abs(total) + rng.randint(0, 20)
                safe = (
                    positive
                    + negative
                    + lift_width
                    + (q - 1) * max_increment
                )
                assert sum(residual_counts) <= safe

        counts["walk_systems"] += 1
        counts["walk_edges"] += len(word)
        counts["simple_cycles"] += len(cycles)

    print("AC primitive-lift relation audit passed")
    keys = [
        "primitive_relations",
        "walk_systems",
        "walk_edges",
        "simple_cycles",
        "relation_systems",
        "extracted_relations",
        "residual_cycles",
        "zero_cycle_occurrences",
    ]
    for key in keys:
        print(f"  {key.replace('_', ' ')}: {counts[key]}")


if __name__ == "__main__":
    main()
