#!/usr/bin/env python3
"""Deterministic audit for AC5eg--AC5ek."""

from collections import defaultdict
from importlib import import_module
from random import Random

BASE = import_module("verify_ac_cut_arc_collision_pairs")
FLOW, UNIT_PATHS, ENABLED = BASE.FLOW, BASE.unit_paths, BASE.ENABLED
SEED, SYSTEMS, TYPED = 2401, 2000, False


def make_system(rng):
    nt, np, nq, nr = (rng.randint(2, 4), rng.randint(2, 3),
                      rng.randint(2, 3), rng.randint(2, 3))
    source, p0, q0, r0 = 0, 1, 1 + np, 1 + np + nq
    terminal0, sink = r0 + nr, r0 + nr + nt
    edges = []
    for i in range(np):
        edges.append((source, p0 + i, rng.randint(1, 3), ("sp", i)))
    for i in range(np):
        made = False
        for j in range(nq):
            if rng.random() < .7:
                edges.append((p0 + i, q0 + j, rng.randint(1, 3), ("pq", i, j)))
                made = True
        if not made:
            j = rng.randrange(nq)
            edges.append((p0 + i, q0 + j, rng.randint(1, 3), ("pq", i, j)))
    for j in range(nq):
        made = False
        for h in range(nr):
            if rng.random() < .7:
                edges.append((q0 + j, r0 + h, rng.randint(1, 3), ("qr", j, h)))
                made = True
        if not made:
            h = rng.randrange(nr)
            edges.append((q0 + j, r0 + h, rng.randint(1, 3), ("qr", j, h)))
    for h in range(nr):
        made = False
        for k in range(nt):
            if rng.random() < .7:
                edges.append((r0 + h, terminal0 + k, rng.randint(1, 3), ("rt", h, k)))
                made = True
        if not made:
            k = rng.randrange(nt)
            edges.append((r0 + h, terminal0 + k, rng.randint(1, 3), ("rt", h, k)))
    demand = [rng.randint(1, 3) for _ in range(nt)]
    for k, value in enumerate(demand):
        edges.append((terminal0 + k, sink, value, ("term", k)))
    return sink + 1, edges, source, sink, demand, [0] * nt


def collision_segment(path_a, path_b, collision_key):
    a, b = path_a[1], path_b[1]
    ia, ib = a.index(collision_key), b.index(collision_key)
    la, lb = ia, ib
    while la and lb and a[la - 1] == b[lb - 1]:
        la -= 1; lb -= 1
    ra, rb = ia, ib
    while ra + 1 < len(a) and rb + 1 < len(b) and a[ra + 1] == b[rb + 1]:
        ra += 1; rb += 1
    segment = a[la:ra + 1]
    assert segment == b[lb:rb + 1]
    source_prefix = la == lb == 0
    if not source_prefix:
        assert a[la - 1] != b[lb - 1]
    assert ra + 1 < len(a) and rb + 1 < len(b)
    assert a[ra + 1] != b[rb + 1]
    return segment, source_prefix


def main():
    rng = Random(SEED)
    out = defaultdict(int); out["systems"] = SYSTEMS
    for _ in range(SYSTEMS):
        n, edges, source, sink, demand, types = make_system(rng)
        count, values = len(demand), {}
        for mask in range(1, 1 << count):
            paid, _flow, _reach = FLOW(n, edges, source, sink, ENABLED(demand, mask))
            total = sum(demand[k] for k in range(count) if mask >> k & 1)
            values[mask] = (paid, total - paid); out["subset_checks"] += 1
        deficient = [m for m, (_paid, gap) in values.items() if gap > 0]
        if not deficient:
            continue
        size = min(m.bit_count() for m in deficient)
        core = min(m for m in deficient if m.bit_count() == size)
        members = [k for k in range(count) if core >> k & 1]
        out["deficient"] += 1
        if len(members) == 1:
            out["singletons"] += 1; continue
        side_a = sum(1 << k for k in members[:len(members) // 2])
        side_b = core ^ side_a
        _v, _f, reached = FLOW(n, edges, source, sink, ENABLED(demand, core))
        _a, flow_a, _ = FLOW(n, edges, source, sink, ENABLED(demand, side_a))
        _b, flow_b, _ = FLOW(n, edges, source, sink, ENABLED(demand, side_b))
        paths_a = UNIT_PATHS(n, edges, source, sink, flow_a)
        paths_b = UNIT_PATHS(n, edges, source, sink, flow_b)
        capacities, signatures = ENABLED(demand, core), defaultdict(int)
        for u, v, capacity, key in edges:
            if not reached[u] or reached[v]:
                continue
            pressure = flow_a[(u, v, key)] + flow_b[(u, v, key)] - capacities.get(key, capacity)
            if pressure <= 0:
                continue
            through_a = [path for path in paths_a if key in path[1]]
            through_b = [path for path in paths_b if key in path[1]]
            assert pressure <= min(len(through_a), len(through_b))
            out["positive_arcs"] += 1
            for path_a, path_b in zip(through_a[:pressure], through_b[:pressure]):
                segment, source_prefix = collision_segment(path_a, path_b, key)
                out["collision_pairs"] += 1; out["segment_edges"] += len(segment)
                out["max_segment_length"] = max(out["max_segment_length"], len(segment))
                out["source_prefix" if source_prefix else "internal_merge_split"] += 1
                signatures[(segment, types[path_a[0]], types[path_b[0]])] += 1
        assert signatures
        out["nontrivial"] += 1
        out["concentrated_pairs"] += max(signatures.values())
    print("AC collision-segment audit passed")
    for key, value in out.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
