#!/usr/bin/env python3
"""Verify RI5f--RI5g physical completion-debt decomposition."""

from __future__ import annotations

from itertools import permutations, product


def decompose(
    current: tuple[int, ...],
    target: tuple[int, ...],
    selected: frozenset[int],
):
    inverse_current = {
        row: column for column, row in enumerate(current)
    }
    successor = {
        column: inverse_current[target[column]]
        for column in selected
    }

    internal_successor = {
        column: (
            successor[column]
            if successor[column] in selected
            else None
        )
        for column in selected
    }
    predecessor = {column: None for column in selected}
    for column, next_column in internal_successor.items():
        if next_column is not None:
            assert predecessor[next_column] is None
            predecessor[next_column] = column

    paths: list[tuple[tuple[int, ...], int]] = []
    visited: set[int] = set()
    for start in sorted(
        column
        for column in selected
        if predecessor[column] is None
    ):
        path: list[int] = []
        column: int | None = start
        while column is not None:
            assert column not in visited
            visited.add(column)
            path.append(column)
            column = internal_successor[column]
        outside = successor[path[-1]]
        assert outside not in selected
        paths.append((tuple(path), outside))

    cycles: list[tuple[int, ...]] = []
    for start in sorted(selected - visited):
        cycle: list[int] = []
        column = start
        while column not in visited:
            visited.add(column)
            cycle.append(column)
            next_column = internal_successor[column]
            assert next_column is not None
            column = next_column
        assert column == start
        cycles.append(tuple(cycle))

    return successor, tuple(cycles), tuple(paths)


def verify_structure(maximum_size: int = 5) -> int:
    checked = 0
    for size in range(2, maximum_size + 1):
        for current in permutations(range(size)):
            for target in permutations(range(size)):
                for mask in range(1, 1 << size):
                    selected = frozenset(
                        column
                        for column in range(size)
                        if mask & (1 << column)
                    )
                    successor, cycles, paths = decompose(
                        current, target, selected
                    )
                    covered = {
                        column
                        for cycle in cycles
                        for column in cycle
                    } | {
                        column
                        for path, _ in paths
                        for column in path
                    }
                    assert covered == selected
                    assert (
                        sum(map(len, cycles))
                        + sum(len(path) for path, _ in paths)
                        == len(selected)
                    )

                    all_cycle_columns = {
                        column
                        for cycle in cycles
                        for column in cycle
                    }
                    assert {
                        current[column]
                        for column in all_cycle_columns
                    } == {
                        target[column]
                        for column in all_cycle_columns
                    }

                    exits = []
                    for cycle in cycles:
                        assert {
                            current[column] for column in cycle
                        } == {
                            target[column] for column in cycle
                        }
                        assert {
                            successor[column] for column in cycle
                        } == set(cycle)

                    for path, outside in paths:
                        exits.append(outside)
                        assert outside not in selected
                        for offset in range(len(path) - 1):
                            assert target[path[offset]] == current[
                                path[offset + 1]
                            ]
                        assert target[path[-1]] == current[outside]
                    assert len(exits) == len(set(exits))
                    checked += 1
    return checked


def verify_weighted_dichotomy(maximum_size: int = 4) -> int:
    checked = 0
    for size in range(2, maximum_size + 1):
        for current in permutations(range(size)):
            for target in permutations(range(size)):
                for mask in range(1, 1 << size):
                    selected = frozenset(
                        column
                        for column in range(size)
                        if mask & (1 << column)
                    )
                    _, cycles, paths = decompose(
                        current, target, selected
                    )
                    ordered = tuple(sorted(selected))
                    for weight_values in product(
                        (1, 2, 3), repeat=len(ordered)
                    ):
                        weights = dict(zip(ordered, weight_values))
                        total = sum(weights.values())
                        cycle_weight = sum(
                            weights[column]
                            for cycle in cycles
                            for column in cycle
                        )
                        path_weights = tuple(
                            sum(weights[column] for column in path)
                            for path, _ in paths
                        )
                        if 2 * cycle_weight < total:
                            assert paths
                            maximum = max(path_weights)
                            assert 2 * len(paths) * maximum > total
                            cap = max(weights.values())
                            heavy_index = path_weights.index(maximum)
                            heavy_path = paths[heavy_index][0]
                            assert len(heavy_path) * cap >= maximum
                        checked += 1
    return checked


def main() -> None:
    structure = verify_structure()
    weighted = verify_weighted_dichotomy()
    print(
        "RI physical completion debt verified:",
        f"{structure} permutation restrictions,",
        f"{weighted} weighted decompositions",
    )


if __name__ == "__main__":
    main()
