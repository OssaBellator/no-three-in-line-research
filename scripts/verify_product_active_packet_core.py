#!/usr/bin/env python3
"""Finite checks for PX310--PX313."""

from __future__ import annotations

from itertools import combinations
import random

Packet = dict[int, int]


def random_packet(rng: random.Random, h: int) -> Packet:
    size = rng.randint(2, h)
    rows = rng.sample(range(h), size)
    cols = rng.sample(range(h), size)
    rng.shuffle(cols)
    return dict(zip(rows, cols))


def selected_crosses(packet: Packet, current: list[int]) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    arcs = list(packet.items())
    out = []
    for first, second in combinations(arcs, 2):
        r, a = first
        s, b = second
        if current[r] == b and current[s] == a:
            out.append((first, second))
    return out


def active_packet(crosses):
    active = {}
    for (r, a), (s, b) in crosses:
        active[r] = a
        active[s] = b
    return active


def event_count(packet: Packet):
    return len(packet) * (len(packet) - 1) // 2


def verify_random_instances() -> None:
    rng = random.Random(310)
    for h in range(3, 18):
        for _ in range(1000):
            current = list(range(h))
            rng.shuffle(current)
            packets = [random_packet(rng, h) for _ in range(rng.randint(1, 20))]

            active_packets = []
            defects = []
            for alpha, packet in enumerate(packets):
                crosses = selected_crosses(packet, current)

                # PX223 disjointness on packet arcs.
                used_rows = set()
                used_cols = set()
                for (r, a), (s, b) in crosses:
                    assert r not in used_rows and s not in used_rows
                    assert a not in used_cols and b not in used_cols
                    used_rows.update({r, s})
                    used_cols.update({a, b})

                active = active_packet(crosses)
                assert len(active) == 2 * len(crosses)

                # The current matching is the union of cross transpositions on
                # the active row and packet-column sets.
                active_cols = set(active.values())
                image = {current[r] for r in active}
                assert image == active_cols
                for (r, a), (s, b) in crosses:
                    assert current[r] == b
                    assert current[s] == a

                if active:
                    active_packets.append((alpha, active))
                for first, second in crosses:
                    support = frozenset({first[0], first[1], second[0], second[1]})
                    defects.append((alpha, support))

            row_incidence = [0] * h
            col_incidence = [0] * h
            for _, packet in active_packets:
                for r, c in packet.items():
                    row_incidence[r] += 1
                    col_incidence[c] += 1
            b_act = max(row_incidence + col_incidence, default=0)

            endpoint_degree = [0] * h
            for _, support in defects:
                for x in support:
                    endpoint_degree[x] += 1
            lambda_old = max(endpoint_degree, default=0)
            assert b_act <= lambda_old

            q_act = sum(event_count(packet) for _, packet in active_packets)
            assert q_act <= b_act * h * h / 2


def verify_dichotomy_constants() -> None:
    rng = random.Random(313)
    for _ in range(10000):
        K = rng.randint(2, 20)
        m0 = rng.randint(1, 20)
        B = 4 * K * m0
        delta = rng.randint(0, 8)
        h = rng.randint(1, 1000)
        b_act = rng.randint(0, B + 100)

        if b_act > B:
            lambda_old = b_act
            assert lambda_old / (4 * K) > m0
        elif h >= 32 * max(1, delta, B):
            assert b_act <= B
            q_bound = b_act * h * h / 2
            assert 8 * q_bound / (h * h) <= 4 * B
        else:
            assert h < 32 * max(1, delta, B)


def main() -> None:
    verify_random_instances()
    verify_dichotomy_constants()
    print("active packet core verifier: PASS")


if __name__ == "__main__":
    main()
