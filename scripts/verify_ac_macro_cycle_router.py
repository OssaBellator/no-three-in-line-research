#!/usr/bin/env python3
"""Finite checks for AC3kz--AC3lc."""

from __future__ import annotations

from collections import Counter
from itertools import permutations, product
from math import prod


def falling(value: int, length: int) -> int:
    if length == 0:
        return 1
    return prod(range(value - length + 1, value + 1))


def erase_loops(walk: tuple[int, ...]) -> tuple[int, ...]:
    path: list[int] = []
    positions: dict[int, int] = {}
    for vertex in walk:
        if vertex in positions:
            cut = positions[vertex]
            for removed in path[cut + 1 :]:
                positions.pop(removed, None)
            path = path[: cut + 1]
        else:
            positions[vertex] = len(path)
            path.append(vertex)
    return tuple(path)


def verify_loop_erasure(counts: Counter[str]) -> None:
    for profile_count in range(2, 7):
        alpha, beta = 0, 1
        vertices = tuple(range(profile_count))
        # Return walks begin at beta and end at alpha.  Complete directed graphs
        # make every adjacent pair an available macro edge.
        for internal_length in range(0, 6):
            for internal in product(vertices, repeat=internal_length):
                walk = (beta,) + internal + (alpha,)
                path = erase_loops(walk)
                assert path[0] == beta
                assert path[-1] == alpha
                assert len(path) == len(set(path))
                assert len(path) <= profile_count
                cycle = (alpha,) + path
                assert cycle[0] == cycle[-1]
                assert len(cycle) - 1 <= profile_count
                counts["return walks"] += 1


def verify_cycle_word_count(counts: Counter[str]) -> None:
    for profile_count in range(2, 9):
        internal_vertices = tuple(range(2, profile_count))
        for decoration_count in range(1, 6):
            exact = 0
            for internal_length in range(0, profile_count - 1):
                ordered = list(permutations(internal_vertices, internal_length))
                exact += len(ordered) * decoration_count ** (internal_length + 1)
                counts["simple return paths"] += len(ordered)
            formula = sum(
                falling(profile_count - 2, internal_length)
                * decoration_count ** (internal_length + 1)
                for internal_length in range(0, profile_count - 1)
            )
            assert exact == formula
            counts["cycle-stock formulas"] += 1


def verify_first_field_return(counts: Counter[str]) -> None:
    # Profiles are two-field words.  Edge alpha->beta changes the least differing
    # field, and every beta-to-alpha path must have a first return of that field.
    values = (0, 1, 2)
    profiles = tuple(product(values, repeat=2))
    for alpha in profiles:
        for beta in profiles:
            if alpha == beta:
                continue
            changed = [index for index in range(2) if alpha[index] != beta[index]]
            field = min(changed)
            for internal_length in range(0, 4):
                for internal in product(profiles, repeat=internal_length):
                    path = (beta,) + internal + (alpha,)
                    first_return = next(
                        index for index, profile in enumerate(path[1:], start=1)
                        if profile[field] == alpha[field]
                    )
                    assert 1 <= first_return < len(path)
                    assert all(
                        profile[field] != alpha[field]
                        for profile in path[:first_return]
                    )
                    counts["field-return paths"] += 1


def verify_cycle_ticket_potential(counts: Counter[str]) -> None:
    for edge_stock in range(0, 8):
        for ticket_stock in range(0, 8):
            for epoch_bound in range(0, 8):
                potential = (epoch_bound + 1) * (edge_stock + ticket_stock)
                for internal in range(0, epoch_bound + 1):
                    current = potential + internal
                    if internal < epoch_bound:
                        assert current + 1 > current
                    first_edge = (epoch_bound + 1) * (edge_stock + 1 + ticket_stock)
                    assert first_edge > current or internal == epoch_bound + 1
                    first_ticket = (epoch_bound + 1) * (edge_stock + ticket_stock + 1)
                    assert first_ticket > current or internal == epoch_bound + 1
                    counts["cycle-ticket potential states"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    verify_loop_erasure(counts)
    verify_cycle_word_count(counts)
    verify_first_field_return(counts)
    verify_cycle_ticket_potential(counts)

    print("AC3kz--AC3lc macro-cycle audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
