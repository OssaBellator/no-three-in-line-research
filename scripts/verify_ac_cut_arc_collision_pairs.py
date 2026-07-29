#!/usr/bin/env python3
"""Deterministic audit for AC5eb--AC5ef."""

from collections import defaultdict
from importlib import import_module
from random import Random

BASE = import_module("verify_ac_canonical_cut_pressure")
FLOW = getattr(BASE, "maxflow", None) or getattr(BASE, "flow")
MAKE_SYSTEM = getattr(BASE, "make_system", None) or getattr(BASE, "system")
ENABLED = BASE.enabled
SEED, SYSTEMS, TYPED = 2201, 3000, False


def unit_paths(n, edges, source, sink, used):
    adjacency = defaultdict(list)
    remaining = {}
    for u, v, _capacity, key in edges:
        amount = used[(u, v, key)]
        if amount > 0:
            adjacency[u].append((str(key), v, key))
            remaining[(u, v, key)] = amount
    for u in adjacency:
        adjacency[u].sort()

    paths = []
    while any(amount > 0 for amount in remaining.values()):
        parent = {}
        visiting = set()

        def search(u):
            if u == sink:
                return True
            visiting.add(u)
            for _order, v, key in adjacency.get(u, []):
                if remaining.get((u, v, key), 0) > 0 and v not in visiting:
                    parent[v] = (u, key)
                    if search(v):
                        return True
            visiting.remove(u)
            return False

        assert search(source)
        nodes, keys, cursor = [sink], [], sink
        while cursor != source:
            previous, key = parent[cursor]
            nodes.append(previous)
            keys.append(key)
            cursor = previous
        nodes.reverse()
        keys.reverse()
        multiplicity = min(
            remaining[(nodes[i], nodes[i + 1], keys[i])]
            for i in range(len(keys))
        )
        terminal = next(key[1] for key in keys if key[0] == "term")
        paths.extend((terminal, tuple(keys)) for _ in range(multiplicity))
        for i, key in enumerate(keys):
            remaining[(nodes[i], nodes[i + 1], key)] -= multiplicity
    return sorted(paths, key=lambda item: (item[0], str(item[1])))


def main():
    rng = Random(SEED)
    out = defaultdict(int)
    out["systems"] = SYSTEMS
    for _ in range(SYSTEMS):
        n, edges, source, sink, demand, types = MAKE_SYSTEM(rng)
        count = len(demand)
        values = {}
        for mask in range(1, 1 << count):
            paid, _flow, _reach = FLOW(n, edges, source, sink, ENABLED(demand, mask))
            total = sum(demand[k] for k in range(count) if mask >> k & 1)
            values[mask] = (paid, total - paid)
            out["subset_checks"] += 1
        deficient = [mask for mask, (_paid, gap) in values.items() if gap > 0]
        if not deficient:
            continue
        size = min(mask.bit_count() for mask in deficient)
        core = min(mask for mask in deficient if mask.bit_count() == size)
        members = [k for k in range(count) if core >> k & 1]
        if len(members) == 1:
            out["singletons"] += 1
            continue
        side_a = sum(1 << k for k in members[: len(members) // 2])
        side_b = core ^ side_a
        _value, _core_flow, reached = FLOW(n, edges, source, sink, ENABLED(demand, core))
        _a, flow_a, _ = FLOW(n, edges, source, sink, ENABLED(demand, side_a))
        _b, flow_b, _ = FLOW(n, edges, source, sink, ENABLED(demand, side_b))
        paths_a = unit_paths(n, edges, source, sink, flow_a)
        paths_b = unit_paths(n, edges, source, sink, flow_b)
        capacities = ENABLED(demand, core)
        positive = 0
        for u, v, capacity, key in edges:
            if not reached[u] or reached[v]:
                continue
            capacity = capacities.get(key, capacity)
            pressure = flow_a[(u, v, key)] + flow_b[(u, v, key)] - capacity
            if pressure <= 0:
                continue
            through_a = [path for path in paths_a if key in path[1]]
            through_b = [path for path in paths_b if key in path[1]]
            assert len(through_a) == flow_a[(u, v, key)]
            assert len(through_b) == flow_b[(u, v, key)]
            assert pressure <= min(len(through_a), len(through_b))
            pairs = list(zip(through_a[:pressure], through_b[:pressure]))
            assert all(a[0] in members and b[0] in members for a, b in pairs)
            class_load = defaultdict(int)
            for a, b in pairs:
                class_load[(a[0], b[0])] += 1
            a_classes = len({a[0] for a, _b in pairs})
            b_classes = len({b[0] for _a, b in pairs})
            assert max(class_load.values()) * a_classes * b_classes >= pressure
            positive += 1
            out["positive_arcs"] += 1
            out["collision_pairs"] += pressure
            out["path_pair_checks"] += pressure
            out["side_a_path_uses"] += len(through_a)
            out["side_b_path_uses"] += len(through_b)
            out["max_pressure"] = max(out["max_pressure"], pressure)
        assert positive > 0
        out["nontrivial_cores"] += 1
    print("AC cut-arc collision audit passed")
    for key, value in out.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
