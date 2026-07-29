#!/usr/bin/env python3
"""Deterministic audit for AC5kb--AC5kg."""

from __future__ import annotations

from collections import defaultdict
from math import prod
import random

SEED = 20260804
SYSTEMS = 2500


def box_count(caps: list[int]) -> int:
    return prod(cap + 1 for cap in caps)


def verify() -> dict[str, int]:
    rng = random.Random(SEED)
    totals: defaultdict[str, int] = defaultdict(int)

    for system_index in range(SYSTEMS):
        route_class = system_index % 5
        dimension = rng.randint(1, 4)
        state_count = rng.randint(6, 24)

        states: list[tuple[int, ...]] = [
            tuple(rng.randint(0, 2) for _ in range(dimension))
        ]
        parents: list[int | None] = [None]
        for state_index in range(1, state_count):
            parent = rng.randrange(state_index)
            parents.append(parent)
            base = states[parent]
            states.append(
                tuple(max(0, value + rng.randint(-1, 4)) for value in base)
            )

        caps = [
            max(0, states[0][coordinate] + rng.randint(0, 1))
            for coordinate in range(dimension)
        ]
        initial_count = box_count(caps)

        if route_class == 0:
            included = {0}
            expansions = 0
            shell = 0
            iterations = 0

            while len(included) < state_count and iterations < 1000:
                # Close all currently internal reachable edges.
                for state_index in range(1, state_count):
                    parent = parents[state_index]
                    if (
                        state_index not in included
                        and parent in included
                        and all(
                            states[state_index][coordinate] <= caps[coordinate]
                            for coordinate in range(dimension)
                        )
                    ):
                        included.add(state_index)
                        totals["internal_refinements"] += 1

                if len(included) == state_count:
                    break

                pending = [
                    state_index
                    for state_index in range(1, state_count)
                    if state_index not in included
                    and parents[state_index] in included
                ]
                assert pending
                selected = min(pending)
                required = states[selected]

                previous_count = box_count(caps)
                caps = [
                    max(caps[coordinate], required[coordinate])
                    for coordinate in range(dimension)
                ]
                current_count = box_count(caps)
                shell += current_count - previous_count
                included.add(selected)
                expansions += 1
                iterations += 1

            assert iterations < 1000
            assert len(included) == state_count
            assert shell == box_count(caps) - initial_count
            totals["valid_systems"] += 1
            totals["states_exposed"] += state_count
            totals["expansions"] += expansions
            totals["shell"] += shell

        elif route_class == 1:
            selected = 1
            omitted_coordinate = rng.randrange(dimension)
            successor_record: list[int | None] = [
                states[selected][coordinate]
                if coordinate != omitted_coordinate
                else None
                for coordinate in range(dimension)
            ]
            assert successor_record[omitted_coordinate] is None
            totals["omitted_successor"] += 1

        elif route_class == 2:
            pending = 1
            assert parents[pending] is not None
            queue_age = rng.randint(2, 10)
            totals["starved_queue"] += 1
            totals["starvation_age"] += queue_age

        elif route_class == 3:
            totals["schema_change"] += 1

        else:
            selected = 1
            assert parents[selected] is not None
            totals["misclassified_boundary"] += 1

        totals["systems"] += 1

    expected = {
        "internal_refinements": 3745,
        "valid_systems": 500,
        "states_exposed": 7366,
        "expansions": 3121,
        "shell": 1710268,
        "systems": 2500,
        "omitted_successor": 500,
        "starved_queue": 500,
        "starvation_age": 2904,
        "schema_change": 500,
        "misclassified_boundary": 500,
    }
    result = dict(totals)
    assert result == expected
    return result


if __name__ == "__main__":
    result = verify()
    for key, value in result.items():
        print(f"{key}: {value}")
