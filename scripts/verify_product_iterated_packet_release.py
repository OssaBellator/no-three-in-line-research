#!/usr/bin/env python3
"""Verify PX215--PX218 iterated product-packet release."""
from __future__ import annotations

from collections import defaultdict
from itertools import combinations, permutations
from math import exp, log
from random import Random


Arc = tuple[int, int]
Event = frozenset[Arc]


def product_packets(
    rows: tuple[int, ...],
    columns: tuple[int, ...],
    anchor: tuple[int, int],
) -> dict[int, tuple[Arc, ...]]:
    a, b = anchor
    packets: dict[int, list[Arc]] = defaultdict(list)
    for i, x in enumerate(rows):
        for j, y in enumerate(columns):
            product = (x - a) * (y - b)
            if product:
                packets[product].append((i, j))
    return {product: tuple(arcs) for product, arcs in packets.items()}


def packet_events(packet: tuple[Arc, ...]) -> frozenset[Event]:
    events: set[Event] = set()
    for (first_row, first_column), (second_row, second_column) in combinations(
        packet, 2
    ):
        assert first_row != second_row
        assert first_column != second_column
        events.add(
            frozenset(
                (
                    (first_row, second_column),
                    (second_row, first_column),
                )
            )
        )
    return frozenset(events)


def verify_product_level_overlap() -> None:
    rows = tuple(3 * index + 1 for index in range(9))
    columns = tuple(5 * index + 2 for index in range(9))
    anchors = ((-7, -11), (-5, 61), (41, -13), (43, 67))
    curves: list[tuple[tuple[int, int, int], frozenset[Arc]]] = []
    for anchor in anchors:
        for product, arcs in product_packets(rows, columns, anchor).items():
            curves.append(((anchor[0], anchor[1], product), frozenset(arcs)))

    for (first_id, first), (second_id, second) in combinations(curves, 2):
        if first_id[:2] == second_id[:2]:
            assert not first & second
        else:
            assert len(first & second) <= 2
    print("distinct product-level overlap at most two verified")


def pair_count(packet: tuple[Arc, ...]) -> int:
    # The packet subgrid has disjoint original row- and column-endpoint sets, so
    # two distinct packet arcs automatically define support four.
    return len(packet) * (len(packet) - 1) // 2


def verify_residual_packet_extraction() -> None:
    random = Random(216)
    for size in range(5, 11):
        rows = tuple(random.sample(range(-50, 80), size))
        columns = tuple(random.sample(range(100, 260), size))
        anchors = ((-70, 17), (83, 311), (-91, 307))
        entries: list[tuple[tuple[int, int, int], int, int]] = []
        total_arcs = 0
        total_pairs = 0
        for anchor in anchors:
            packets = product_packets(rows, columns, anchor)
            for product, packet in packets.items():
                mass = pair_count(packet)
                entries.append(((anchor[0], anchor[1], product), len(packet), mass))
                total_arcs += len(packet)
                total_pairs += mass

        assert total_arcs <= len(anchors) * size**2
        if total_pairs:
            best = max(entries, key=lambda entry: entry[2] / entry[1])
            _, packet_size, pair_mass = best
            assert pair_mass / packet_size >= total_pairs / (
                len(anchors) * size**2
            )
            assert packet_size >= 2 * total_pairs / (len(anchors) * size**2)
    print("residual packet extraction inequalities verified")


def union_events(packets: tuple[tuple[Arc, ...], ...]) -> frozenset[Event]:
    events: set[Event] = set()
    for packet in packets:
        events.update(packet_events(packet))
    return frozenset(events)


def allowed_permutations(
    size: int,
    forbidden: frozenset[Arc],
    packets: tuple[tuple[Arc, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    events = union_events(packets)
    result = []
    for permutation in permutations(range(size)):
        chosen = frozenset((row, permutation[row]) for row in range(size))
        if chosen & forbidden:
            continue
        if any(event <= chosen for event in events):
            continue
        result.append(permutation)
    return tuple(result)


def verify_joint_release_exact() -> None:
    size = 8
    identity = tuple((index, index) for index in range(size))
    shift = tuple((index, (index + 1) % size) for index in range(size))
    packets = (identity, shift)
    forbidden = frozenset((index, (index + 3) % size) for index in range(size))
    allowed = allowed_permutations(size, forbidden, packets)
    assert allowed

    events = union_events(packets)
    for permutation in allowed:
        chosen = frozenset((row, permutation[row]) for row in range(size))
        assert not chosen & forbidden
        assert all(not event <= chosen for event in events)
    print(f"exact two-packet released family positive at order {size}: {len(allowed)}")


def verify_joint_lll_inequalities() -> None:
    for packet_count in range(1, 17):
        for degree in range(0, 17):
            size = 32 * max(1, packet_count, degree)
            singleton_witness = 2 / size
            pair_witness = 4 / size**2

            singleton_lhs = (
                singleton_witness
                * (1 - singleton_witness) ** (2 * degree)
                * (1 - pair_witness) ** (2 * packet_count * (size - 1))
            )
            pair_lhs = (
                pair_witness
                * (1 - singleton_witness) ** (4 * degree)
                * (1 - pair_witness) ** (4 * packet_count * (size - 1))
            )
            assert singleton_lhs >= 1 / size
            assert pair_lhs >= 1 / (size * (size - 1))

            singleton_events = degree * size
            pair_events = packet_count * size * (size - 1) // 2
            density = (
                (1 - singleton_witness) ** singleton_events
                * (1 - pair_witness) ** pair_events
            )
            assert density >= exp(-4 * degree - 4 * packet_count)
            assert log(1 - 2 / size) >= -4 / size
            assert log(1 - 4 / size**2) >= -8 / size**2
    print("k-packet lopsided-LLL and density inequalities verified")


def complement_positions(
    packet: tuple[Arc, ...],
    exposure: tuple[Arc, ...],
) -> frozenset[Arc]:
    forward = dict(packet)
    inverse = {column: row for row, column in packet}
    complements: set[Arc] = set()
    for source, target in exposure:
        other_source = inverse.get(target)
        other_target = forward.get(source)
        if other_source is None or other_target is None or other_source == source:
            continue
        complements.add((other_source, other_target))
    return frozenset(complements)


def is_partial_matching(edges: frozenset[Arc]) -> bool:
    return (
        len({row for row, _ in edges}) == len(edges)
        and len({column for _, column in edges}) == len(edges)
    )


def verify_conditioned_packet_complements() -> None:
    random = Random(218)
    for size in range(6, 12):
        packet_count = 4
        packets = []
        for _ in range(packet_count):
            image = list(range(size))
            random.shuffle(image)
            packets.append(tuple(enumerate(image)))

        exposure_image = list(range(size))
        random.shuffle(exposure_image)
        exposure = tuple((row, exposure_image[row]) for row in range(size // 2))

        all_complements: list[frozenset[Arc]] = []
        for packet in packets:
            complements = complement_positions(packet, exposure)
            assert is_partial_matching(complements)
            all_complements.append(complements)

        union = set().union(*all_complements)
        row_degree = max(
            (
                sum(row == candidate_row for candidate_row, _ in union)
                for row in range(size)
            ),
            default=0,
        )
        column_degree = max(
            (
                sum(column == candidate_column for _, candidate_column in union)
                for column in range(size)
            ),
            default=0,
        )
        assert row_degree <= packet_count
        assert column_degree <= packet_count
    print("one complementary partial matching per packet verified")


def verify_conditioned_constants() -> None:
    for packet_count in range(1, 13):
        for degree in range(0, 13):
            residual_degree = degree + packet_count
            size = 32 * max(1, packet_count, residual_degree)
            x1 = 2 / size
            x2 = 4 / size**2
            assert (
                x1
                * (1 - x1) ** (2 * residual_degree)
                * (1 - x2) ** (2 * packet_count * (size - 1))
                >= 1 / size
            )
            assert (
                x2
                * (1 - x1) ** (4 * residual_degree)
                * (1 - x2) ** (4 * packet_count * (size - 1))
                >= 1 / (size * (size - 1))
            )
            assert exp(-4 * residual_degree - 4 * packet_count) == exp(
                -4 * degree - 8 * packet_count
            )
    print("conditioned joint-release constants verified")


def main() -> None:
    verify_product_level_overlap()
    verify_residual_packet_extraction()
    verify_joint_release_exact()
    verify_joint_lll_inequalities()
    verify_conditioned_packet_complements()
    verify_conditioned_constants()
    print("PX215--PX218 verified")


if __name__ == "__main__":
    main()
