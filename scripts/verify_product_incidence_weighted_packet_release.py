#!/usr/bin/env python3
"""Finite checks for PX307--PX309."""

from __future__ import annotations

from itertools import combinations
import math
import random

Cell = tuple[int, int]
Event = frozenset[Cell]
Packet = dict[int, int]


def packet_events(packet: Packet) -> set[Event]:
    arcs = list(packet.items())
    events: set[Event] = set()
    for (r, a), (s, b) in combinations(arcs, 2):
        events.add(frozenset({(r, b), (s, a)}))
    return events


def conflict(a: Event, b: Event) -> bool:
    if a == b:
        return False
    for r1, c1 in a:
        for r2, c2 in b:
            if r1 == r2 and c1 != c2:
                return True
            if c1 == c2 and r1 != r2:
                return True
    return False


def incidence(packets: list[Packet], h: int) -> int:
    row_load = [0] * h
    col_load = [0] * h
    for packet in packets:
        for r, c in packet.items():
            row_load[r] += 1
            col_load[c] += 1
    return max(row_load + col_load, default=0)


def random_packet(rng: random.Random, h: int) -> Packet:
    size = rng.randint(2, h)
    rows = rng.sample(range(h), size)
    cols = rng.sample(range(h), size)
    rng.shuffle(cols)
    return dict(zip(rows, cols))


def random_forbidden(rng: random.Random, h: int, delta: int) -> set[Cell]:
    cells: set[Cell] = set()
    row_degree = [0] * h
    col_degree = [0] * h
    candidates = [(r, c) for r in range(h) for c in range(h)]
    rng.shuffle(candidates)
    for r, c in candidates:
        if row_degree[r] >= delta or col_degree[c] >= delta:
            continue
        if rng.random() < 0.25:
            cells.add((r, c))
            row_degree[r] += 1
            col_degree[c] += 1
    return cells


def verify_dependency_counts() -> None:
    rng = random.Random(307)
    for h in range(4, 13):
        for _ in range(300):
            packets = [random_packet(rng, h) for _ in range(rng.randint(1, 8))]
            B = incidence(packets, h)
            delta = rng.randint(0, min(4, h))
            forbidden = random_forbidden(rng, h, delta)
            singleton_events = [frozenset({cell}) for cell in forbidden]
            cross_events = set().union(*(packet_events(packet) for packet in packets))

            for event in singleton_events:
                ss = sum(conflict(event, other) for other in singleton_events)
                sp = sum(conflict(event, other) for other in cross_events)
                assert ss <= max(0, 2 * delta - 2)
                assert sp <= 2 * B * (h - 1)

            for event in cross_events:
                ps = sum(conflict(event, other) for other in singleton_events)
                pp = sum(conflict(event, other) for other in cross_events)
                assert ps <= 4 * delta
                assert pp <= 4 * B * (h - 1)

            Q = len(cross_events)
            assert Q <= sum(len(packet) * (len(packet) - 1) // 2 for packet in packets)
            assert Q <= B * h * h / 2


def verify_lll_threshold() -> None:
    for delta in range(0, 20):
        for B in range(0, 20):
            scale = max(1, delta, B)
            for h in range(32 * scale, 32 * scale + 200):
                x1 = 2 / h
                x2 = 4 / (h * h)
                singleton_rhs = x1 * (1 - x1) ** (2 * delta) * (1 - x2) ** (2 * B * (h - 1))
                packet_rhs = x2 * (1 - x1) ** (4 * delta) * (1 - x2) ** (4 * B * (h - 1))
                assert singleton_rhs + 1e-15 >= 1 / h
                assert packet_rhs + 1e-15 >= 1 / (h * (h - 1))

                assert (1 - 2 / h) ** (delta * h) + 1e-15 >= math.exp(-4 * delta)


def complement_cells(packet: Packet, exposed: set[Cell]) -> set[Cell]:
    complements: set[Cell] = set()
    arcs = list(packet.items())
    for (r, a), (s, b) in combinations(arcs, 2):
        first = (r, b)
        second = (s, a)
        if first in exposed and second not in exposed:
            complements.add(second)
        if second in exposed and first not in exposed:
            complements.add(first)
    return complements


def verify_conditioned_degree() -> None:
    rng = random.Random(309)
    for h in range(4, 15):
        for _ in range(500):
            packets = [random_packet(rng, h) for _ in range(rng.randint(1, 10))]
            B = incidence(packets, h)

            rows = rng.sample(range(h), rng.randint(0, h))
            cols = rng.sample(range(h), len(rows))
            rng.shuffle(cols)
            exposed = set(zip(rows, cols))

            union = set().union(*(complement_cells(packet, exposed) for packet in packets))
            row_degree = [sum(r == rr for rr, _ in union) for r in range(h)]
            col_degree = [sum(c == cc for _, cc in union) for c in range(h)]
            assert max(row_degree + col_degree, default=0) <= B

            # Each individual packet contributes a partial matching.
            for packet in packets:
                comp = complement_cells(packet, exposed)
                assert len({r for r, _ in comp}) == len(comp)
                assert len({c for _, c in comp}) == len(comp)


def main() -> None:
    verify_dependency_counts()
    verify_lll_threshold()
    verify_conditioned_degree()
    print("incidence-weighted packet release verifier: PASS")


if __name__ == "__main__":
    main()
