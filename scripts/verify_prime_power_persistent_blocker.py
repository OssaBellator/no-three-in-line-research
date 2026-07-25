#!/usr/bin/env python3
"""Finite checks for CMR522--CMR526."""

from __future__ import annotations

from itertools import combinations


Edge = tuple[int, int]


def is_matching(edges: tuple[Edge, ...] | set[Edge]) -> bool:
    return (
        len({left for left, _right in edges}) == len(edges)
        and len({right for _left, right in edges}) == len(edges)
    )


def maximum_matchings(edges: set[Edge]) -> tuple[int, list[set[Edge]]]:
    edge_list = list(edges)
    best_size = 0
    best: list[set[Edge]] = [set()]
    for size in range(1, len(edge_list) + 1):
        current = [
            set(choice)
            for choice in combinations(edge_list, size)
            if is_matching(choice)
        ]
        if current:
            best_size = size
            best = current
    return best_size, best


def graph_masks(side: int) -> list[int] | range:
    edge_count = side * side
    if side <= 3:
        return range(1 << edge_count)
    edges = [
        (left, right)
        for left in range(side)
        for right in range(side)
    ]
    return [
        0,
        (1 << edge_count) - 1,
        *[
            sum(
                1 << index
                for index, (left, right) in enumerate(edges)
                if (left + 2 * right + residue) % side == 0
            )
            for residue in range(side)
        ],
    ]


def verify_allowed_edge_criterion() -> int:
    checked = 0
    for side in range(1, 5):
        universe = [
            (left, right)
            for left in range(side)
            for right in range(side)
        ]
        for mask in graph_masks(side):
            edges = {
                edge
                for index, edge in enumerate(universe)
                if mask & (1 << index)
            }
            maximum_size, maximum_states = maximum_matchings(edges)

            for edge in edges:
                left, right = edge
                reduced = {
                    other
                    for other in edges
                    if other[0] != left and other[1] != right
                }
                reduced_size, _states = maximum_matchings(reduced)
                maximum_allowed = any(edge in state for state in maximum_states)

                assert maximum_allowed == (
                    1 + reduced_size == maximum_size
                )

                if not maximum_allowed:
                    assert reduced_size == maximum_size - 2
                    for state in maximum_states:
                        assert edge not in state
                        left_edges = [other for other in state if other[0] == left]
                        right_edges = [other for other in state if other[1] == right]
                        assert len(left_edges) == 1
                        assert len(right_edges) == 1
                        assert left_edges[0] != right_edges[0]
                        partner_left = left_edges[0]
                        partner_right = right_edges[0]
                        assert partner_left[0] == left
                        assert partner_right[1] == right
                        assert partner_left[1] != right
                        assert partner_right[0] != left

                checked += 1
    return checked


def verify_partner_incidence() -> None:
    for occurrence_count in range(1, 40):
        for threshold in range(2, 10):
            # If no partner edge occurs threshold times, 2R incidences require
            # at least ceil(2R/(threshold-1)) distinct partners.
            lower_bound = (2 * occurrence_count + threshold - 2) // (
                threshold - 1
            )
            assert lower_bound * (threshold - 1) >= 2 * occurrence_count


def main() -> None:
    checked = verify_allowed_edge_criterion()
    verify_partner_incidence()
    print(
        f"verified CMR522--CMR526 on {checked} edge instances: maximum-"
        "allowed criterion, exact two-endpoint deficiency, saturation by distinct "
        "partner edges, and persistent-cross incidence arithmetic"
    )


if __name__ == "__main__":
    main()
