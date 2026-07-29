#!/usr/bin/env python3
from __future__ import annotations
from collections import deque
import random

SEED = 53
SYSTEMS = 2500


def simplify_return(repeated_edge, walk):
    stack = []
    position = {}
    for vertex in walk:
        if vertex in position:
            index = position[vertex]
            for removed in stack[index + 1:]:
                position.pop(removed, None)
            stack = stack[:index + 1]
        else:
            position[vertex] = len(stack)
            stack.append(vertex)
    alpha, beta, _ = repeated_edge
    assert stack[0] == beta and stack[-1] == alpha
    return tuple([alpha] + stack)


def first_field_return(cycle, profiles, field):
    alpha = cycle[0]
    target = profiles[alpha][field]
    for index, vertex in enumerate(cycle[1:], 1):
        if profiles[vertex][field] == target:
            return index
    raise AssertionError("no field return")


def maximum_flow(claims, sources, eligible, stock):
    copies = []
    for source in sources:
        for copy in range(stock[source]):
            copies.append((source, copy))
    size = 1 + len(claims) + len(copies) + 1
    start = 0
    sink = size - 1
    capacity = [[0] * size for _ in range(size)]
    for i, claim in enumerate(claims):
        capacity[start][1 + i] = 1
        for j, (source, _) in enumerate(copies):
            if (claim, source) in eligible:
                capacity[1 + i][1 + len(claims) + j] = 1
    for j in range(len(copies)):
        capacity[1 + len(claims) + j][sink] = 1

    flow = 0
    while True:
        previous = [-1] * size
        previous[start] = start
        queue = deque([start])
        while queue and previous[sink] < 0:
            u = queue.popleft()
            for v in range(size):
                if previous[v] < 0 and capacity[u][v] > 0:
                    previous[v] = u
                    queue.append(v)
        if previous[sink] < 0:
            break
        vertex = sink
        while vertex != start:
            predecessor = previous[vertex]
            capacity[predecessor][vertex] -= 1
            capacity[vertex][predecessor] += 1
            vertex = predecessor
        flow += 1
    return flow


def run():
    rng = random.Random(SEED)
    stats = {
        "systems": SYSTEMS,
        "return_episodes": 0,
        "simple_cycles": 0,
        "deleted_subwalk_vertices": 0,
        "first_field_returns": 0,
        "paid_cycles": 0,
        "descent_cycles": 0,
        "source_ticket_cycles": 0,
        "recreation_ticket_cycles": 0,
        "impossible_cycles": 0,
        "unresolved_cycle_cores": 0,
        "ticket_flow_assignments": 0,
        "ticket_flow_failures": 0,
        "duplicate_cycle_ticket_witnesses": 0,
    }

    for system in range(SYSTEMS):
        route = system % 5
        vertex_count = rng.randint(4, 9)
        field_count = rng.randint(2, 5)
        profiles = [
            tuple(rng.randrange(4) for _ in range(field_count))
            for _ in range(vertex_count)
        ]
        alpha = 0
        beta = 1
        profiles[alpha] = tuple(0 for _ in range(field_count))
        profiles[beta] = tuple(1 if i == 0 else 0 for i in range(field_count))
        repeated_edge = alpha, beta, ("decoration", system % 7)
        walk = [beta]
        for _ in range(rng.randint(3, 10)):
            walk.append(rng.randrange(vertex_count))
        walk.append(alpha)
        original_length = len(walk)
        cycle = simplify_return(repeated_edge, walk)
        stats["return_episodes"] += 1
        stats["simple_cycles"] += 1
        stats["deleted_subwalk_vertices"] += max(
            0, original_length - (len(cycle) - 1)
        )
        return_index = first_field_return(cycle, profiles, 0)
        assert return_index >= 1
        stats["first_field_returns"] += 1

        record = {
            "cycle": cycle,
            "field": 0,
            "prefix": cycle[:return_index + 1],
            "occurrences": [
                ("edge", system, index) for index in range(len(cycle) - 1)
            ],
        }
        if route == 0:
            record["paid_owner"] = "owner", system
            record["destroyed"] = 1
            stats["paid_cycles"] += 1
        elif route == 1:
            record["rank_bank"] = "bank", system
            record["before"] = rng.randint(1, 8)
            record["after"] = record["before"] - 1
            stats["descent_cycles"] += 1
        elif route == 2:
            if system % 2 == 0:
                record["ticket_kind"] = "source"
                stats["source_ticket_cycles"] += 1
            else:
                record["ticket_kind"] = "recreation"
                stats["recreation_ticket_cycles"] += 1
            record["ticket"] = "ticket", system
            record["lineage"] = "lineage", system
            claims = (record["ticket"],)
            sources = (("source", system % 17),)
            stock = {sources[0]: 1}
            eligible = {(claims[0], sources[0])}
            assert maximum_flow(claims, sources, eligible, stock) == 1
            stats["ticket_flow_assignments"] += 1
            alias = "alias", record["ticket"]
            assert alias != record["ticket"]
            stats["duplicate_cycle_ticket_witnesses"] += 1
        elif route == 3:
            record["impossibility"] = "failed-physical-edge", system
            stats["impossible_cycles"] += 1
        else:
            assert all(
                field not in record
                for field in ("paid_owner", "rank_bank", "ticket", "impossibility")
            )
            stats["unresolved_cycle_cores"] += 1
            claims = (("ticket", system),)
            sources = (("source", system),)
            stock = {sources[0]: 0}
            assert maximum_flow(claims, sources, set(), stock) == 0
            stats["ticket_flow_failures"] += 1

    return stats


if __name__ == "__main__":
    output = run()
    print("AC cycle discharge compiler audit")
    for key, value in output.items():
        print(f"{key}: {value}")
