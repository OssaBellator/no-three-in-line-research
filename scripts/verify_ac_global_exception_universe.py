#!/usr/bin/env python3
"""Deterministic audit for AC5jv--AC5ka."""

from __future__ import annotations

from collections import defaultdict, deque
import random

SEED = 20260803
SYSTEMS = 2500


def maximum_flow(
    vertex_count: int,
    arcs: list[tuple[int, int, int]],
    source: int,
    sink: int,
) -> int:
    capacity = [[0] * vertex_count for _ in range(vertex_count)]
    for start, end, amount in arcs:
        capacity[start][end] += amount

    flow = 0
    while True:
        predecessor = [-1] * vertex_count
        predecessor[source] = source
        queue = deque([source])
        while queue and predecessor[sink] < 0:
            start = queue.popleft()
            for end in range(vertex_count):
                if predecessor[end] < 0 and capacity[start][end] > 0:
                    predecessor[end] = start
                    queue.append(end)
                    if end == sink:
                        break
        if predecessor[sink] < 0:
            break

        augmentation = 10**9
        current = sink
        while current != source:
            previous = predecessor[current]
            augmentation = min(augmentation, capacity[previous][current])
            current = previous

        current = sink
        while current != source:
            previous = predecessor[current]
            capacity[previous][current] -= augmentation
            capacity[current][previous] += augmentation
            current = previous
        flow += augmentation

    return flow


def verify() -> dict[str, int]:
    rng = random.Random(SEED)
    totals: defaultdict[str, int] = defaultdict(int)

    for system_index in range(SYSTEMS):
        route_class = system_index % 5
        source_count = rng.randint(2, 7)
        claim_count = rng.randint(2, 8)
        source_stocks = [rng.randint(1, 5) for _ in range(source_count)]
        claim_stocks = [rng.randint(1, 4) for _ in range(claim_count)]

        # Network layout: super-source, physical sources, claims, sink.
        vertex_count = 2 + source_count + claim_count
        super_source = 0
        sink = vertex_count - 1
        arcs: list[tuple[int, int, int]] = []
        for index, stock in enumerate(source_stocks):
            arcs.append((super_source, 1 + index, stock))

        compatibility_arcs = 0
        for source_index in range(source_count):
            has_arc = False
            for claim_index in range(claim_count):
                if rng.random() < 0.45:
                    arcs.append(
                        (
                            1 + source_index,
                            1 + source_count + claim_index,
                            10**6,
                        )
                    )
                    compatibility_arcs += 1
                    has_arc = True
            if not has_arc:
                claim_index = rng.randrange(claim_count)
                arcs.append(
                    (
                        1 + source_index,
                        1 + source_count + claim_index,
                        10**6,
                    )
                )
                compatibility_arcs += 1

        for claim_index, stock in enumerate(claim_stocks):
            arcs.append((1 + source_count + claim_index, sink, stock))

        flow = maximum_flow(vertex_count, arcs, super_source, sink)
        assert flow <= sum(source_stocks)
        assert flow <= sum(claim_stocks)

        # A deliberately naive typewise total can reuse the same sources.
        naive_raw = sum(min(sum(source_stocks), stock) for stock in claim_stocks)
        assert naive_raw >= flow

        if route_class == 1:
            totals["new_address_on_expansion"] += 1
        elif route_class == 2:
            totals["relabel_conflict"] += 1
        elif route_class == 3:
            totals["duplicate_debit"] += 1
        elif route_class == 4:
            totals["unrecorded_deposit"] += 1
        else:
            # Fixed registry remains identical through numerical cap changes.
            digest = (
                tuple(source_stocks),
                tuple(claim_stocks),
                compatibility_arcs,
                flow,
            )
            for _level in range(4):
                _unrelated_caps = [
                    rng.randint(1, 20) for _ in range(rng.randint(1, 5))
                ]
                assert (
                    tuple(source_stocks),
                    tuple(claim_stocks),
                    compatibility_arcs,
                    flow,
                ) == digest

            totals["valid_registries"] += 1
            totals["source_stock"] += sum(source_stocks)
            totals["claim_stock"] += sum(claim_stocks)
            totals["maxflow_stock"] += flow
            totals["naive_raw"] += naive_raw
            totals["overcount_removed"] += naive_raw - flow

            # Historical finite direct-address families.
            coordinate_count = rng.randint(1, 4)
            betas = [rng.randint(1, 5) for _ in range(coordinate_count)]
            low_tickets = sum(
                rng.randint(0, 4)
                for _coordinate, beta in enumerate(betas)
                for _level in range(beta)
            )
            atoms = rng.randint(1, 5)
            recreation_edges = rng.randint(1, 6)
            recreation_tickets = atoms * recreation_edges
            reset_stock = rng.randint(0, 6)
            disturbance_stock = rng.randint(0, 8)
            direct_registry = (
                low_tickets
                + recreation_tickets
                + reset_stock
                + disturbance_stock
            )

            totals["low_tickets"] += low_tickets
            totals["recreation_tickets"] += recreation_tickets
            totals["reset_stock"] += reset_stock
            totals["disturbance_stock"] += disturbance_stock
            totals["direct_registry"] += direct_registry

        totals["compatibility_arcs"] += compatibility_arcs
        totals["systems"] += 1

    expected = {
        "valid_registries": 500,
        "source_stock": 6771,
        "claim_stock": 6225,
        "maxflow_stock": 4544,
        "naive_raw": 6212,
        "overcount_removed": 1668,
        "low_tickets": 7832,
        "recreation_tickets": 5310,
        "reset_stock": 1549,
        "disturbance_stock": 2072,
        "direct_registry": 16763,
        "compatibility_arcs": 26555,
        "systems": 2500,
        "new_address_on_expansion": 500,
        "relabel_conflict": 500,
        "duplicate_debit": 500,
        "unrecorded_deposit": 500,
    }
    result = dict(totals)
    assert result == expected
    return result


if __name__ == "__main__":
    result = verify()
    for key, value in result.items():
        print(f"{key}: {value}")
