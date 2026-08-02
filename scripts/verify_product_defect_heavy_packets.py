#!/usr/bin/env python3
"""Verify PX223--PX224 defect-heavy product-level concentration."""
from __future__ import annotations

from collections import defaultdict
from itertools import combinations, permutations
from random import Random


Arc = tuple[int, int]
Event = frozenset[Arc]


def packet_crosses(packet: tuple[Arc, ...]) -> tuple[tuple[Arc, Arc, Event], ...]:
    return tuple(
        (
            first,
            second,
            frozenset(((first[0], second[1]), (second[0], first[1]))),
        )
        for first, second in combinations(packet, 2)
    )


def selected_packet_crosses(
    packet: tuple[Arc, ...],
    permutation: tuple[int, ...],
) -> tuple[tuple[Arc, Arc], ...]:
    chosen = frozenset((row, permutation[row]) for row in range(len(permutation)))
    return tuple(
        (first, second)
        for first, second, event in packet_crosses(packet)
        if event <= chosen
    )


def verify_selected_cross_matching() -> None:
    random = Random(223)
    for size in range(5, 14):
        for _ in range(100):
            packet_image = list(range(size))
            current_image = list(range(size))
            random.shuffle(packet_image)
            random.shuffle(current_image)
            packet = tuple(enumerate(packet_image))
            selected = selected_packet_crosses(packet, tuple(current_image))
            used_arcs = [arc for pair in selected for arc in pair]
            assert len(set(used_arcs)) == len(used_arcs)
            assert len(selected) <= len(packet) // 2
    print("selected packet crosses form disjoint packet-arc matchings")


def product_packets(
    rows: tuple[int, ...],
    columns: tuple[int, ...],
    anchor: tuple[int, int],
) -> dict[int, tuple[Arc, ...]]:
    a, b = anchor
    packets: dict[int, list[Arc]] = defaultdict(list)
    for row, x in enumerate(rows):
        for column, y in enumerate(columns):
            product = (x - a) * (y - b)
            if product:
                packets[product].append((row, column))
    return {product: tuple(arcs) for product, arcs in packets.items()}


def collinear_with_anchor(
    anchor: tuple[int, int],
    first: tuple[int, int],
    second: tuple[int, int],
) -> bool:
    return (
        (first[0] - anchor[0]) * (second[1] - anchor[1])
        == (second[0] - anchor[0]) * (first[1] - anchor[1])
    )


def verify_exact_defect_decomposition() -> None:
    random = Random(224)
    for size in range(5, 11):
        rows = tuple(random.sample(range(-40, 80), size))
        columns = tuple(random.sample(range(100, 240), size))
        anchors = ((-61, 17), (83, 271), (-73, 263))
        current = list(range(size))
        random.shuffle(current)
        current = tuple(current)
        selected_points = tuple(
            (rows[row], columns[current[row]]) for row in range(size)
        )

        direct_total = 0
        packet_total = 0
        for anchor in anchors:
            direct = sum(
                collinear_with_anchor(anchor, first, second)
                for first, second in combinations(selected_points, 2)
            )
            direct_total += direct

            for packet in product_packets(rows, columns, anchor).values():
                packet_total += len(selected_packet_crosses(packet, current))

        assert packet_total == direct_total
    print("exact anchor-product selected-defect decomposition verified")


def verify_heavy_level_counting() -> None:
    random = Random(225)
    for level_count in range(1, 100):
        loads = [random.randrange(0, 50) for _ in range(level_count)]
        total = sum(loads)
        for threshold in (1, 3, 7, 13, 25):
            heavy = [load for load in loads if load >= threshold]
            assert len(heavy) * threshold <= total
            assert len(heavy) <= total / threshold if total else not heavy
    print("heavy-level counting inequality verified")


def packet_events(packet: tuple[Arc, ...]) -> frozenset[Event]:
    return frozenset(event for _, _, event in packet_crosses(packet))


def allowed_permutations(
    size: int,
    packets: tuple[tuple[Arc, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    events = set()
    for packet in packets:
        events.update(packet_events(packet))
    return tuple(
        permutation
        for permutation in permutations(range(size))
        if all(
            not event
            <= frozenset((row, permutation[row]) for row in range(size))
            for event in events
        )
    )


def verify_heavy_packet_release() -> None:
    size = 8
    identity = tuple((index, index) for index in range(size))
    shift = tuple((index, (index + 1) % size) for index in range(size))
    current = tuple(
        value
        for pair in ((1, 0), (3, 2), (5, 4), (7, 6))
        for value in pair
    )
    packets = (identity, shift)
    loads = tuple(len(selected_packet_crosses(packet, current)) for packet in packets)
    assert loads[0] == size // 2
    heavy_packets = tuple(
        packet for packet, load in zip(packets, loads) if load >= 2
    )
    allowed = allowed_permutations(size, heavy_packets)
    assert allowed

    old_events = set()
    for packet in heavy_packets:
        old_events.update(packet_events(packet))
    for permutation in allowed:
        chosen = frozenset((row, permutation[row]) for row in range(size))
        assert all(not event <= chosen for event in old_events)
    print(
        "joint release removes all included old packet crosses: "
        f"loads={loads}, family={len(allowed)}"
    )


def main() -> None:
    verify_selected_cross_matching()
    verify_exact_defect_decomposition()
    verify_heavy_level_counting()
    verify_heavy_packet_release()
    print("PX223--PX224 verified")


if __name__ == "__main__":
    main()
