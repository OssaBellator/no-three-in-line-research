#!/usr/bin/env python3
"""Verify BDA4e radial-pair load regularization."""

from __future__ import annotations

from collections import defaultdict
from itertools import product
from math import ceil


Point = tuple[int, int]
Vector = tuple[int, int]
Record = tuple[Point, int]


def role_scales(h: int, q: int, scale: Vector) -> tuple[int, ...]:
    u, v = scale
    return 0, h * u, h * v, (h + q) * u, (h + q) * v


def support(
    record: Record,
    q: int,
    direction: Vector,
    scale: Vector,
) -> set[Point]:
    (x, y), h = record
    a, b = direction
    return {
        (x + multiple * a, y + multiple * b)
        for multiple in role_scales(h, q, scale)
    }


def conflict_graph(
    records: tuple[Record, ...],
    q: int,
    direction: Vector,
    scale: Vector,
) -> dict[Record, set[Record]]:
    supports = {
        record: support(record, q, direction, scale)
        for record in records
    }
    rows = {
        record: {point[0] for point in points}
        for record, points in supports.items()
    }
    columns = {
        record: {point[1] for point in points}
        for record, points in supports.items()
    }
    graph = {record: set() for record in records}
    for index, first in enumerate(records):
        for second in records[index + 1:]:
            if (
                rows[first] & rows[second]
                or columns[first] & columns[second]
            ):
                graph[first].add(second)
                graph[second].add(first)
    return graph


def coordinate_loads(
    records: tuple[Record, ...],
    q: int,
    direction: Vector,
    scale: Vector,
    coordinate: int,
) -> dict[int, set[Record]]:
    loads: dict[int, set[Record]] = defaultdict(set)
    for record in records:
        values = {
            point[coordinate]
            for point in support(record, q, direction, scale)
        }
        for value in values:
            loads[value].add(record)
    return loads


def greedy_colouring(
    graph: dict[Record, set[Record]],
) -> dict[Record, int]:
    colours: dict[Record, int] = {}
    for record in graph:
        forbidden = {
            colours[neighbour]
            for neighbour in graph[record]
            if neighbour in colours
        }
        colour = 0
        while colour in forbidden:
            colour += 1
        colours[record] = colour
    return colours


def matching_role(
    record: Record,
    coordinate_value: int,
    coordinate: int,
    q: int,
    direction: Vector,
    scale: Vector,
) -> int:
    anchor, h = record
    step = direction[coordinate]
    for role, multiple in enumerate(role_scales(h, q, scale)):
        if anchor[coordinate] + multiple * step == coordinate_value:
            return role
    raise AssertionError("loaded coordinate has no supporting role")


def verify_family(
    records: tuple[Record, ...],
    q: int,
    direction: Vector,
    scale: Vector,
) -> None:
    graph = conflict_graph(records, q, direction, scale)
    row_loads = coordinate_loads(
        records,
        q,
        direction,
        scale,
        0,
    )
    column_loads = coordinate_loads(
        records,
        q,
        direction,
        scale,
        1,
    )
    maximum_load = max(
        [1]
        + [len(loaded) for loaded in row_loads.values()]
        + [len(loaded) for loaded in column_loads.values()]
    )
    maximum_degree = max(
        (len(neighbours) for neighbours in graph.values()),
        default=0,
    )
    assert maximum_degree <= 10 * (maximum_load - 1)

    colouring = greedy_colouring(graph)
    colour_count = max(colouring.values(), default=-1) + 1
    assert colour_count <= 10 * (maximum_load - 1) + 1
    for first, neighbours in graph.items():
        assert all(
            colouring[first] != colouring[second]
            for second in neighbours
        )

    weights = {
        record: index % 7 + 1
        for index, record in enumerate(records)
    }
    weight_by_colour: dict[int, int] = defaultdict(int)
    for record, colour in colouring.items():
        weight_by_colour[colour] += weights[record]
    total_weight = sum(weights.values())
    assert max(weight_by_colour.values(), default=0) * (
        10 * (maximum_load - 1) + 1
    ) >= total_weight

    a, b = direction
    u, v = scale
    role_data = (
        None,
        (0, u),
        (0, v),
        (1, u),
        (1, v),
    )
    for coordinate, loads, step in (
        (0, row_loads, a),
        (1, column_loads, b),
    ):
        for value, loaded_records in loads.items():
            groups: dict[int, list[Record]] = defaultdict(list)
            for record in loaded_records:
                role = matching_role(
                    record,
                    value,
                    coordinate,
                    q,
                    direction,
                    scale,
                )
                groups[role].append(record)
            heaviest = max(groups.values(), key=len)
            assert len(heaviest) >= ceil(len(loaded_records) / 5)
            role = matching_role(
                heaviest[0],
                value,
                coordinate,
                q,
                direction,
                scale,
            )
            for anchor, h in heaviest:
                if role == 0:
                    assert anchor[coordinate] == value
                else:
                    stage, multiplier = role_data[role]
                    assert anchor[coordinate] == (
                        value - (h + stage * q) * multiplier * step
                    )

            paid_group = max(
                groups.values(),
                key=lambda group: sum(weights[record] for record in group),
            )
            assert 5 * sum(weights[record] for record in paid_group) >= (
                sum(weights[record] for record in loaded_records)
            )
            paid_role = matching_role(
                paid_group[0],
                value,
                coordinate,
                q,
                direction,
                scale,
            )
            for anchor, h in paid_group:
                if paid_role == 0:
                    assert anchor[coordinate] == value
                else:
                    stage, multiplier = role_data[paid_role]
                    assert anchor[coordinate] == (
                        value - (h + stage * q) * multiplier * step
                    )


def verify_paid_coanchor_extraction(
    maximum_slots: int = 8,
    weight_cap: int = 2,
) -> None:
    for slot_count in range(1, maximum_slots + 1):
        for weights in product(
            range(weight_cap + 1),
            repeat=slot_count,
        ):
            total_weight = sum(weights)
            overlap = sum(
                min(left, right)
                for left, right in zip(weights, weights[1:])
            )
            lower_bound = max(
                0,
                2 * total_weight - weight_cap * (slot_count + 1),
            )
            assert overlap >= lower_bound

            parity_weights = (
                sum(
                    min(weights[index], weights[index + 1])
                    for index in range(0, slot_count - 1, 2)
                ),
                sum(
                    min(weights[index], weights[index + 1])
                    for index in range(1, slot_count - 1, 2)
                ),
            )
            assert sum(parity_weights) == overlap
            assert 2 * max(parity_weights) >= overlap


def main() -> None:
    directions = ((1, 1), (2, -1), (1, -2))
    scales = ((1, 2), (-1, 2), (2, -3))
    anchors = tuple(
        (x, y)
        for x in range(-3, 4)
        for y in range(-3, 4)
    )
    for q in range(2, 6):
        for direction in directions:
            for scale in scales:
                records = tuple(
                    (anchor, h)
                    for h in range(1, 6)
                    for anchor in anchors
                    if (anchor[0] + 2 * anchor[1] + h) % 5 == 0
                )
                assert all(
                    len(support(record, q, direction, scale)) <= 5
                    for record in records
                )
                verify_family(records, q, direction, scale)
    verify_paid_coanchor_extraction()
    print("BDA radial-pair regularization: verified")


if __name__ == "__main__":
    main()
