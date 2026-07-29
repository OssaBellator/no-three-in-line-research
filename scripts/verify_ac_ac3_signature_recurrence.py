#!/usr/bin/env python3
from __future__ import annotations
from collections import defaultdict
import random

SEED = 47
SYSTEMS = 2500
KINDS = ("product", "cross", "coordinate", "wrap", "bda", "ri")


def strongly_connected_components(n, edges):
    graph = [[] for _ in range(n)]
    reverse = [[] for _ in range(n)]
    for u, v, _ in edges:
        graph[u].append(v)
        reverse[v].append(u)
    seen = [False] * n
    order = []

    def dfs(u):
        seen[u] = True
        for v in graph[u]:
            if not seen[v]:
                dfs(v)
        order.append(u)

    for vertex in range(n):
        if not seen[vertex]:
            dfs(vertex)

    component = [-1] * n

    def reverse_dfs(u, label):
        component[u] = label
        for v in reverse[u]:
            if component[v] < 0:
                reverse_dfs(v, label)

    label = 0
    for vertex in reversed(order):
        if component[vertex] < 0:
            reverse_dfs(vertex, label)
            label += 1
    groups = defaultdict(list)
    for vertex, value in enumerate(component):
        groups[value].append(vertex)
    return list(groups.values())


def find_cycle(vertices, edges):
    vertex_set = set(vertices)
    graph = defaultdict(list)
    for u, v, index in edges:
        if u in vertex_set and v in vertex_set:
            graph[u].append((v, index))
    for u in graph:
        graph[u].sort()
    state = {}
    stack = []
    position = {}

    def dfs(u):
        state[u] = 1
        position[u] = len(stack)
        stack.append(u)
        for v, _ in graph[u]:
            if state.get(v, 0) == 0:
                result = dfs(v)
                if result:
                    return result
            elif state.get(v) == 1:
                return tuple(stack[position[v]:] + [v])
        stack.pop()
        position.pop(u, None)
        state[u] = 2
        return None

    for vertex in sorted(vertex_set):
        if state.get(vertex, 0) == 0:
            result = dfs(vertex)
            if result:
                return result
    return None


def make_signature(rng, kind, index):
    record = {
        "kind": kind,
        "channel": rng.randrange(4),
        "owner_route": rng.choice(["PAID", "FIXED_CURRENT", "PROSPECTIVE"]),
    }
    if kind == "product":
        record["coords"] = (rng.randint(-20, 20), rng.randint(-20, 20))
    elif kind == "cross":
        record["level"] = rng.randint(-20, 20)
    elif kind == "coordinate":
        record["axis"] = rng.randrange(2)
        record["level"] = rng.randint(-20, 20)
    elif kind == "wrap":
        record["num"] = rng.randint(-50, 50)
        record["den"] = rng.randint(1, 20)
    elif kind == "bda":
        record["denominator"] = rng.randint(2, 30)
        record["det_occ"] = ("det", index)
    else:
        record["subgroup_order"] = rng.randint(1, 20)
        record["physical_occ"] = ("ri", index)
    return tuple(sorted(record.items()))


def run():
    rng = random.Random(SEED)
    stats = {
        "systems": SYSTEMS,
        "signature_records": 0,
        "first_exposures": 0,
        "ticketed_reuses": 0,
        "paid_or_delegated_reuses": 0,
        "unticketed_cycles": 0,
        "cycle_edges": 0,
        "malformed_signatures": 0,
        "duplicate_ticket_aliases": 0,
        "support_descents": 0,
        "reopening_ticket_failures": 0,
    }

    for system in range(SYSTEMS):
        route = system % 5
        vertex_count = rng.randint(5, 10)
        signatures = [
            make_signature(rng, KINDS[(system + i) % len(KINDS)], system * 20 + i)
            for i in range(rng.randint(3, 7))
        ]
        stats["signature_records"] += len(signatures)
        exposed = set()
        used_tickets = set()
        old_edges = []
        full_universe = set(range(vertex_count))
        current_universe = set(full_universe)

        if route == 4:
            malformed = dict(signatures[0])
            malformed.pop("owner_route", None)
            assert "owner_route" not in malformed
            stats["malformed_signatures"] += 1
            continue

        for step in range(rng.randint(8, 18)):
            source = rng.randrange(vertex_count)
            target = rng.randrange(vertex_count)
            signature = signatures[rng.randrange(len(signatures))]
            if signature not in exposed:
                exposed.add(signature)
                stats["first_exposures"] += 1
                continue

            if route == 0:
                ticket = ("ticket", signature, step)
                assert ticket not in used_tickets
                used_tickets.add(ticket)
                stats["ticketed_reuses"] += 1
            elif route == 1:
                stats["paid_or_delegated_reuses"] += 1
            elif route == 2:
                old_edges.append((source, target, step))
            else:
                if len(current_universe) > 1:
                    current_universe.remove(min(current_universe))
                    stats["support_descents"] += 1
                elif step % 2 == 0:
                    ticket = ("reopen", system, step)
                    assert ticket not in used_tickets
                    used_tickets.add(ticket)
                    current_universe = set(full_universe)
                    stats["ticketed_reuses"] += 1
                else:
                    stats["reopening_ticket_failures"] += 1

        if route == 2:
            old_edges.extend([(0, 1, 1000), (1, 0, 1001)])
            cyclic_component = None
            for component in sorted(
                strongly_connected_components(vertex_count, old_edges),
                key=lambda values: (min(values), len(values)),
            ):
                if len(component) > 1 or any(
                    u == v and u in component for u, v, _ in old_edges
                ):
                    cyclic_component = component
                    break
            assert cyclic_component is not None
            cycle = find_cycle(cyclic_component, old_edges)
            assert cycle is not None
            stats["unticketed_cycles"] += 1
            stats["cycle_edges"] += len(cycle) - 1

        if route == 0 and used_tickets:
            ticket = next(iter(used_tickets))
            alias = ("alias", ticket)
            assert alias != ticket
            stats["duplicate_ticket_aliases"] += 1

    return stats


if __name__ == "__main__":
    output = run()
    print("AC AC3 signature recurrence audit")
    for key, value in output.items():
        print(f"{key}: {value}")
