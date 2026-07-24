#!/usr/bin/env python3
"""Exhaustive finite checks for CMR210--CMR214."""

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


def degree(graph: int, t: int, vertex: int, left: bool) -> int:
    if left:
        return sum(bool(graph & (1 << (vertex * t + column))) for column in range(t))
    return sum(bool(graph & (1 << (row * t + vertex))) for row in range(t))


def neighbourhood(graph: int, t: int, left_mask: int) -> int:
    result = 0
    for row in range(t):
        if not (left_mask & (1 << row)):
            continue
        for column in range(t):
            if graph & (1 << (row * t + column)):
                result |= 1 << column
    return result


def essential_witnesses(graph: int, t: int, edge_index: int):
    row, column = divmod(edge_index, t)
    witnesses = []
    for left_mask in range(1, 1 << t):
        if not (left_mask & (1 << row)):
            continue
        right_mask = neighbourhood(graph, t, left_mask)
        if right_mask.bit_count() != left_mask.bit_count():
            continue
        if not (right_mask & (1 << column)):
            continue
        neighbours_in_left = [
            candidate_row
            for candidate_row in range(t)
            if left_mask & (1 << candidate_row)
            and graph & (1 << (candidate_row * t + column))
        ]
        if neighbours_in_left == [row]:
            witnesses.append((left_mask, right_mask))
    return witnesses


def verify_all_graphs(t: int) -> None:
    matching_masks = perfect_matching_masks(t)
    full_edge_count = t * t

    for graph in range(1 << full_edge_count):
        matchings = [mask for mask in matching_masks if mask & ~graph == 0]
        if not matchings:
            continue

        essential_mask = matchings[0]
        for mask in matchings[1:]:
            essential_mask &= mask

        for edge_index in range(full_edge_count):
            if not (graph & (1 << edge_index)):
                continue
            witnesses = essential_witnesses(graph, t, edge_index)
            is_essential = bool(essential_mask & (1 << edge_index))
            assert bool(witnesses) == is_essential

            if is_essential:
                for left_mask, right_mask in witnesses:
                    left_size = left_mask.bit_count()
                    assert left_size == right_mask.bit_count()
                    row, column = divmod(edge_index, t)
                    assert left_mask & (1 << row)
                    assert right_mask & (1 << column)

        minimum_degree = min(
            [degree(graph, t, vertex, True) for vertex in range(t)]
            + [degree(graph, t, vertex, False) for vertex in range(t)]
        )
        if 2 * minimum_degree >= t:
            assert essential_mask == 0
            for edge_index in range(full_edge_count):
                if graph & (1 << edge_index):
                    assert any(
                        not (matching & (1 << edge_index))
                        for matching in matchings
                    )


def main() -> None:
    verify_all_graphs(t=3)
    verify_all_graphs(t=4)
    print(
        "verified essential-edge factorization for all bipartite hosts at "
        "t=3,4 and no essential edge at minimum degree at least t/2"
    )


if __name__ == "__main__":
    main()
