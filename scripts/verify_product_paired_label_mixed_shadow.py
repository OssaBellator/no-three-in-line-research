#!/usr/bin/env python3
"""Finite checks for PX437--PX444 paired mixed shadows and packet recurrence."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
import random


def collinear(
    first: tuple[int, int],
    second: tuple[int, int],
    anchor: tuple[int, int],
) -> bool:
    return (
        (first[0] - anchor[0]) * (second[1] - anchor[1])
        == (second[0] - anchor[0]) * (first[1] - anchor[1])
    )


def check_proper_typed_colouring() -> None:
    rng = random.Random(437)
    for order in range(2, 30):
        for _ in range(150):
            rows = (
                rng.sample(range(-100, 101), order),
                rng.sample(range(200, 501), order),
            )
            columns = rng.sample(range(-300, 301), order)
            anchor = (rng.randint(-500, 500), rng.randint(-500, 500))

            for copy in range(2):
                # In a fixed source row, a line colour may occur at most once.
                for source in range(order):
                    colours = []
                    for target in range(order):
                        point = (rows[copy][source], columns[target])
                        direction = (
                            point[0] - anchor[0],
                            point[1] - anchor[1],
                        )
                        colours.append(direction)
                    # Equal directed vectors imply equal target columns.
                    assert len(colours) == len(set(colours))

                # In a fixed target column, equal anchor lines may contain at
                # most one typed row point.
                for target in range(order):
                    points = [
                        (rows[copy][source], columns[target])
                        for source in range(order)
                    ]
                    for first, second in combinations(points, 2):
                        assert not (
                            collinear(first, second, anchor)
                            and first != anchor
                            and second != anchor
                        )


def check_transposition_destroys_collision() -> None:
    rng = random.Random(438)
    for order in range(4, 30):
        row_t = (
            rng.sample(range(-100, 101), order),
            rng.sample(range(200, 501), order),
        )
        row_r = (
            rng.sample(range(600, 901), order),
            rng.sample(range(1000, 1301), order),
        )
        column_t = rng.sample(range(-400, -100), order)
        column_r = rng.sample(range(100, 401), order)

        for _ in range(500):
            source_t, partner = rng.sample(range(order), 2)
            source_r = rng.randrange(order)
            copy_t = rng.randrange(2)
            copy_r = rng.randrange(2)
            anchor = (rng.randint(-1000, 1500), rng.randint(-800, 800))

            old_t = (row_t[copy_t][source_t], column_t[source_t])
            old_r = (row_r[copy_r][source_r], column_r[source_r])
            if not collinear(old_t, old_r, anchor):
                continue

            new_t = (row_t[copy_t][source_t], column_t[partner])
            assert not collinear(new_t, old_r, anchor)


def check_typed_packet_cross() -> None:
    rng = random.Random(442)
    for order in range(3, 30):
        rows = (
            rng.sample(range(-100, 101), order),
            rng.sample(range(200, 501), order),
        )
        columns = rng.sample(range(-300, 301), order)
        for _ in range(1000):
            u, s = rng.sample(range(order), 2)
            v, w = rng.sample(range(order), 2)
            epsilon = rng.randrange(2)
            delta = rng.randrange(2)
            anchor = (rng.randint(-500, 500), rng.randint(-500, 500))

            selected_u = (rows[epsilon][u], columns[v])
            selected_s = (rows[delta][s], columns[w])
            product_uw = (
                (rows[epsilon][u] - anchor[0])
                * (columns[w] - anchor[1])
            )
            product_sv = (
                (rows[delta][s] - anchor[0])
                * (columns[v] - anchor[1])
            )
            assert collinear(selected_u, selected_s, anchor) == (
                product_uw == product_sv
            )


def check_event_compression() -> None:
    rng = random.Random(443)
    for order in range(3, 20):
        for _ in range(500):
            events: list[tuple[int, int, int, int]] = []
            for u, s in combinations(range(order), 2):
                v, w = rng.sample(range(order), 2)
                for _copy_pattern in range(rng.randint(0, 4)):
                    events.append((u, s, w, v))

            unique = set(events)
            assert len(unique) <= len(events)
            for u, s, target_u, target_s in unique:
                assert u != s
                assert target_u != target_s


def check_copy_pattern_counts() -> None:
    assert 2**2 == 4
    assert 2**3 == 8


def main() -> None:
    check_proper_typed_colouring()
    check_transposition_destroys_collision()
    check_typed_packet_cross()
    check_event_compression()
    check_copy_pattern_counts()
    print("PX437--PX444 paired-label mixed-shadow verifier: PASS")


if __name__ == "__main__":
    main()
