#!/usr/bin/env python3
from __future__ import annotations
from collections import deque
from itertools import combinations
import random

SEED = 43
SYSTEMS = 2500


def maximum_weight_independent_set(n, edges, weights):
    edge_set = {tuple(sorted(edge)) for edge in edges}
    best_mask = 0
    best_weight = -1
    for mask in range(1 << n):
        if any((mask >> u) & 1 and (mask >> v) & 1 for u, v in edge_set):
            continue
        weight = sum(weights[i] for i in range(n) if (mask >> i) & 1)
        if weight > best_weight or (weight == best_weight and mask < best_mask):
            best_weight = weight
            best_mask = mask
    return tuple(i for i in range(n) if (best_mask >> i) & 1), best_weight


def maximum_source_assignment(demands, tokens, eligible, capacities):
    copies = []
    for token in tokens:
        for copy in range(capacities[token]):
            copies.append((token, copy))
    size = 1 + len(demands) + len(copies) + 1
    source = 0
    sink = size - 1
    capacity = [[0] * size for _ in range(size)]
    for i, demand in enumerate(demands):
        capacity[source][1 + i] = 1
        for j, (token, _) in enumerate(copies):
            if (demand, token) in eligible:
                capacity[1 + i][1 + len(demands) + j] = 1
    for j in range(len(copies)):
        capacity[1 + len(demands) + j][sink] = 1

    flow = 0
    while True:
        previous = [-1] * size
        previous[source] = source
        queue = deque([source])
        while queue and previous[sink] < 0:
            u = queue.popleft()
            for v in range(size):
                if previous[v] < 0 and capacity[u][v] > 0:
                    previous[v] = u
                    queue.append(v)
        if previous[sink] < 0:
            break
        vertex = sink
        while vertex != source:
            predecessor = previous[vertex]
            capacity[predecessor][vertex] -= 1
            capacity[vertex][predecessor] += 1
            vertex = predecessor
        flow += 1

    reachable = {source}
    queue = deque([source])
    while queue:
        u = queue.popleft()
        for v in range(size):
            if v not in reachable and capacity[u][v] > 0:
                reachable.add(v)
                queue.append(v)
    cut_demands = tuple(
        demands[i] for i in range(len(demands)) if 1 + i in reachable
    )
    return flow, len(demands) - flow, cut_demands


def closed_load(object_id, edges, weights):
    neighbourhood = {object_id}
    for u, v in edges:
        if u == object_id:
            neighbourhood.add(v)
        elif v == object_id:
            neighbourhood.add(u)
    return sum(weights[value] for value in neighbourhood)


def labelled_descent(object_id, n, edges, weights, labels, k_value, q_value):
    classes = {}
    for edge in edges:
        u, v = edge
        if object_id not in edge:
            continue
        other = v if u == object_id else u
        classes.setdefault(labels[tuple(sorted(edge))], []).append(other)
    assert classes
    label, members = max(
        classes.items(),
        key=lambda item: (sum(weights[value] for value in item[1]), item[0]),
    )
    class_weight = sum(weights[value] for value in members)
    assert class_weight > (k_value - 1) * weights[object_id] / len(classes) - 1e-12
    induced = [edge for edge in edges if edge[0] in members and edge[1] in members]
    for value in members:
        if closed_load(value, induced, weights) > q_value * weights[value]:
            return "recursive-overload", label, value, tuple(sorted(members))
    chosen, _ = maximum_weight_independent_set(n, induced, weights)
    chosen = tuple(value for value in chosen if value in members)
    selected_weight = sum(weights[value] for value in chosen)
    assert selected_weight >= class_weight / q_value - 1e-12
    return "compatible-label-family", label, chosen, tuple(sorted(members))


def complete_conflict_graph(objects):
    edges = set()
    reasons = {}
    for i, j in combinations(range(len(objects)), 2):
        cause = []
        if set(objects[i]["footprint"]) & set(objects[j]["footprint"]):
            cause.append("footprint")
        if set(objects[i]["paid"]) & set(objects[j]["paid"]):
            cause.append("paid-overlap")
        if set(objects[i]["protected"]) & set(objects[j]["protected"]):
            cause.append("protected")
        if objects[i]["cross"].get(j) or objects[j]["cross"].get(i):
            cause.append("cross-certificate")
        if cause:
            edge = i, j
            edges.add(edge)
            reasons[edge] = tuple(cause)
    return edges, reasons


def run():
    rng = random.Random(SEED)
    stats = {
        "systems": SYSTEMS,
        "objects": 0,
        "conflict_edges": 0,
        "compatible_batches": 0,
        "paid_overloads": 0,
        "label_compatible_families": 0,
        "recursive_overloads": 0,
        "feasible_source_assignments": 0,
        "source_hall_failures": 0,
        "missing_conflict_rows": 0,
        "duplicate_paid_alias_witnesses": 0,
        "support_descents": 0,
    }

    for system in range(SYSTEMS):
        n = rng.randint(5, 9)
        objects = []
        for i in range(n):
            objects.append({
                "footprint": [i, (i + system) % 13] if rng.random() < 0.55 else [i],
                "paid": [i] if rng.random() < 0.7 else [i, 100 + i % 3],
                "protected": [rng.randrange(5)] if rng.random() < 0.3 else [],
                "cross": {},
                "weight": rng.randint(1, 8),
            })
        route = system % 5
        if route == 1:
            for i in range(1, n):
                objects[0]["cross"][i] = True
                objects[i]["weight"] = rng.randint(4, 8)
            objects[0]["weight"] = 1

        edges, reasons = complete_conflict_graph(objects)
        weights = [obj["weight"] for obj in objects]
        stats["objects"] += n
        stats["conflict_edges"] += len(edges)

        if route == 3:
            if edges:
                omitted = min(edges)
                proposed = set(edges)
                proposed.remove(omitted)
                assert omitted not in proposed and omitted in edges
            stats["missing_conflict_rows"] += 1
            continue
        if route == 4:
            if n >= 2:
                objects[1]["paid"] = list(objects[0]["paid"])
                assert set(objects[0]["paid"]) & set(objects[1]["paid"])
            stats["duplicate_paid_alias_witnesses"] += 1
            continue

        k_value = 3
        overload = None
        for object_id in range(n):
            if closed_load(object_id, edges, weights) > k_value * weights[object_id]:
                overload = object_id
                break
        if overload is None:
            _, selected_weight = maximum_weight_independent_set(n, edges, weights)
            assert selected_weight >= sum(weights) / k_value - 1e-12
            stats["compatible_batches"] += 1
        else:
            stats["paid_overloads"] += 1
            labels = {edge: reasons[edge][0] for edge in edges}
            result = labelled_descent(overload, n, edges, weights, labels, k_value, 2)
            if result[0] == "recursive-overload":
                stats["recursive_overloads"] += 1
                assert len(result[3]) < n
                stats["support_descents"] += 1
            else:
                stats["label_compatible_families"] += 1

        chosen, _ = maximum_weight_independent_set(n, edges, weights)
        demands = tuple(chosen)
        tokens = tuple(range(max(1, len(demands))))
        capacities = {token: 1 for token in tokens}
        eligible = {
            (demand, token)
            for demand in demands
            for token in tokens
            if (demand + token + system) % 3 != 0
        }
        if route == 2 and demands:
            eligible = {
                (demand, token)
                for demand, token in eligible
                if demand != demands[-1]
            }
        flow, unmatched, _ = maximum_source_assignment(
            demands, tokens, eligible, capacities
        )
        if flow == len(demands):
            stats["feasible_source_assignments"] += 1
        else:
            assert unmatched > 0
            stats["source_hall_failures"] += 1

    return stats


if __name__ == "__main__":
    output = run()
    print("AC AC2 structural re-extraction audit")
    for key, value in output.items():
        print(f"{key}: {value}")
