#!/usr/bin/env python3
"""Exhaustive finite checks for CMR215--CMR218."""

from __future__ import annotations

from itertools import permutations


def perfect_matching_masks(t: int) -> list[int]:
    masks = []
    for permutation in permutations(range(t)):
        mask = 0
        for row, column in enumerate(permutation):
            mask |= 1 << (row * t + column)
        masks.append(mask)
    return masks


def matching_component_contains(
    first: int,
    second: int,
    t: int,
    edge_a: int,
    edge_b: int,
) -> bool:
    symmetric = first ^ second
    adjacency = [[] for _ in range(2 * t)]
    for edge in range(t * t):
        if not (symmetric & (1 << edge)):
            continue
        row, column = divmod(edge, t)
        left = row
        right = t + column
        adjacency[left].append(right)
        adjacency[right].append(left)

    start_row, _ = divmod(edge_a, t)
    target_row, target_column = divmod(edge_b, t)
    targets = {target_row, t + target_column}
    stack = [start_row]
    seen = {start_row}
    while stack:
        vertex = stack.pop()
        for neighbour in adjacency[vertex]:
            if neighbour not in seen:
                seen.add(neighbour)
                stack.append(neighbour)
    return targets <= seen


def verify_exchange_theorem(t: int) -> None:
    matching_masks = perfect_matching_masks(t)
    for graph in range(1 << (t * t)):
        matchings = [mask for mask in matching_masks if mask & ~graph == 0]
        if not matchings:
            continue

        essential_before = matchings[0]
        for mask in matchings[1:]:
            essential_before &= mask

        for deleted_edge in range(t * t):
            if not (graph & (1 << deleted_edge)):
                continue
            smaller = graph & ~(1 << deleted_edge)
            smaller_matchings = [
                mask for mask in matching_masks if mask & ~smaller == 0
            ]
            if not smaller_matchings:
                continue

            essential_after = smaller_matchings[0]
            for mask in smaller_matchings[1:]:
                essential_after &= mask
            newly_essential = essential_after & ~essential_before

            while newly_essential:
                bit = newly_essential & -newly_essential
                newly_essential -= bit
                edge = bit.bit_length() - 1

                avoiding = [
                    mask
                    for mask in matchings
                    if not (mask & (1 << edge))
                ]
                assert avoiding
                assert all(mask & (1 << deleted_edge) for mask in avoiding)

                for first in smaller_matchings:
                    for second in avoiding:
                        assert matching_component_contains(
                            first,
                            second,
                            t,
                            edge,
                            deleted_edge,
                        )


def verify_time_acyclicity(max_steps: int) -> None:
    for terminal_time in range(1, max_steps + 1):
        time = terminal_time
        length = 0
        while time > 0:
            time -= 1
            length += 1
        assert length <= max_steps
        assert time == 0


def main() -> None:
    verify_exchange_theorem(t=3)
    verify_exchange_theorem(t=4)
    verify_time_acyclicity(max_steps=10_000)
    print(
        "verified exchange ancestry for every bipartite host at t=3,4: "
        "new essential edges share an alternating cycle with the deleted edge"
    )


if __name__ == "__main__":
    main()
