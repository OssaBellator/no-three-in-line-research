#!/usr/bin/env python3
"""Deterministic finite audit for RI5he--RI5hh."""

from collections import defaultdict, deque
import math
import random


def maximum_matching(left, edges):
    adjacency = {u: [] for u in left}
    for u, v in edges:
        adjacency[u].append(v)
    match_right = {}

    def augment(u, seen):
        for v in adjacency[u]:
            if v in seen:
                continue
            seen.add(v)
            if v not in match_right or augment(match_right[v], seen):
                match_right[v] = u
                return True
        return False

    for u in left:
        augment(u, set())
    match_left = {u: v for v, u in match_right.items()}
    return match_left, match_right


def alternating_closure(edges, match_left, match_right, roots):
    adjacency = defaultdict(set)
    for u, v in edges:
        adjacency[u].add(v)
    incidence_set = set(roots)
    token_set = set()
    queue = deque(("L", u) for u in roots)
    while queue:
        side, item = queue.popleft()
        if side == "L":
            for token in adjacency[item]:
                if match_left.get(item) == token:
                    continue
                if token not in token_set:
                    token_set.add(token)
                    queue.append(("R", token))
        elif item in match_right:
            incidence = match_right[item]
            if incidence not in incidence_set:
                incidence_set.add(incidence)
                queue.append(("L", incidence))
    return incidence_set, token_set


def audit(seed):
    rng = random.Random(seed)
    key_count = rng.randint(1, 4)
    left, right, left_key, right_key = [], [], {}, {}
    for key in range(key_count):
        for index in range(rng.randint(1, 7)):
            item = f"r{key}_{index}"
            left.append(item)
            left_key[item] = key
        for index in range(rng.randint(1, 7)):
            item = f"t{key}_{index}"
            right.append(item)
            right_key[item] = key

    predicate_count = rng.randint(1, 6)
    edges, failures = set(), {}
    for incidence in left:
        for token in right:
            if left_key[incidence] != right_key[token]:
                continue
            pair = (incidence, token)
            if rng.random() < 0.45:
                edges.add(pair)
            else:
                labels = {j for j in range(predicate_count) if rng.random() < 0.35}
                failures[pair] = labels or {rng.randrange(predicate_count)}

    match_left, match_right = maximum_matching(left, edges)
    roots = [u for u in left if u not in match_left]
    stats = defaultdict(int)
    stats["vertices"] = len(left) + len(right)
    stats["edges"] = len(edges)
    stats["roots"] = len(roots)
    if not roots:
        return stats

    support_size = rng.randint(1, 5)
    cause = {u: rng.randrange(support_size) for u in roots}
    groups = defaultdict(list)
    for root in roots:
        groups[(cause[root], left_key[root])].append(root)
    _, selected = max(groups.items(), key=lambda item: (len(item[1]), str(item[0])))
    key = left_key[selected[0]]
    m = len(selected)
    assert m >= math.ceil(len(roots) / len(groups))

    left_key_set = [u for u in left if left_key[u] == key]
    right_key_set = [v for v in right if right_key[v] == key]
    key_edges = {(u, v) for u, v in edges if left_key[u] == key}
    incidence_set, token_set = alternating_closure(
        key_edges, match_left, match_right, selected
    )
    neighbourhood = {v for u, v in key_edges if u in incidence_set}
    assert neighbourhood == token_set
    assert len(incidence_set) - len(token_set) == m

    stats["selected_roots"] = m
    stats["closure_vertices"] = len(incidence_set) + len(token_set)
    if len(right_key_set) < len(left_key_set):
        stats["shortfall"] = len(left_key_set) - len(right_key_set)
        return stats

    outside = set(right_key_set) - token_set
    assert len(outside) >= m
    rectangle = [(u, v) for u in selected for v in outside]
    assert all(pair not in edges for pair in rectangle)

    label_counts = defaultdict(int)
    root_label_counts = defaultdict(lambda: defaultdict(int))
    for pair in rectangle:
        label = min(failures[pair])
        label_counts[label] += 1
        root_label_counts[pair[0]][label] += 1
    label = max(label_counts, key=label_counts.get)
    assert label_counts[label] * predicate_count >= m * m
    assert max(root_label_counts[u][label] for u in selected) >= math.ceil(
        m / predicate_count
    )

    stats["balanced"] = 1
    stats["rectangle_pairs"] = len(rectangle)
    stats["predicate_pairs"] = label_counts[label]
    return stats


def main():
    totals = defaultdict(int)
    for seed in range(17, 2517):
        for name, value in audit(seed).items():
            totals[name] += value
    expected = {
        "vertices": 50283,
        "edges": 45911,
        "roots": 8198,
        "selected_roots": 4072,
        "closure_vertices": 9702,
        "shortfall": 5059,
        "balanced": 330,
        "rectangle_pairs": 1222,
        "predicate_pairs": 802,
    }
    assert dict(totals) == expected, (dict(totals), expected)
    print("RI5he--RI5hh audit passed:", expected)


if __name__ == "__main__":
    main()
