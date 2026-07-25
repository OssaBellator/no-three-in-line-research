#!/usr/bin/env python3
"""Finite checks for AC3ib--AC3if."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import permutations

Vertex = tuple[str, int]
Cell = tuple[int, int]
Perm = tuple[int, ...]


def cells(p: Perm) -> set[Cell]:
    return {(c, r) for c, r in enumerate(p)}


def canonical_cross(old: Perm, new: Perm) -> tuple[Cell, Cell, Cell, Cell]:
    removed = sorted(cells(old) - cells(new))
    assert removed
    u, v = removed[0]
    y = new[u]
    x = new.index(v)
    assert y != v and x != u
    return (u, v), (u, y), (x, v), (x, y)


def component_vertices(
    old: Perm, new: Perm, e: Cell
) -> tuple[set[Vertex], set[Cell]]:
    adjacency: dict[Vertex, list[tuple[Vertex, Cell]]] = defaultdict(list)
    for p in (old, new):
        for c, r in enumerate(p):
            if old[c] == new[c]:
                continue
            vc = ("c", c)
            vr = ("r", r)
            cell = (c, r)
            adjacency[vc].append((vr, cell))
            adjacency[vr].append((vc, cell))
    start = ("c", e[0])
    vertices: set[Vertex] = set()
    edges: set[Cell] = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex in vertices:
            continue
        vertices.add(vertex)
        for neighbour, cell in adjacency[vertex]:
            edges.add(cell)
            if neighbour not in vertices:
                stack.append(neighbour)
    return vertices, edges


def interior_path(
    old: Perm, new: Perm
) -> tuple[tuple[Cell, Cell, Cell], frozenset[Vertex], frozenset[Cell]] | None:
    e, r, c, p = canonical_cross(old, new)
    if p in cells(old):
        return None
    _, edges = component_vertices(old, new, e)
    u, v = e
    _, y = r
    x, _ = c
    fixed_edges = {e, r, c}
    path_edges = edges - fixed_edges
    assert len(edges) >= 6
    assert fixed_edges <= edges

    degree: Counter[Vertex] = Counter()
    for col, row in path_edges:
        degree[("c", col)] += 1
        degree[("r", row)] += 1
    start = ("r", y)
    end = ("c", x)
    assert degree[start] == degree[end] == 1
    for vertex, value in degree.items():
        if vertex not in {start, end}:
            assert value == 2
    internal = frozenset(vertex for vertex in degree if vertex not in {start, end})
    assert 2 <= len(internal) <= 2 * len(old) - 4
    assert ("c", u) not in internal and ("r", v) not in internal
    return (e, r, c), internal, frozenset(path_edges)


def maximal_disjoint(paths: list[frozenset[Vertex]]) -> list[int]:
    chosen: list[int] = []
    used: set[Vertex] = set()
    for index, path in enumerate(paths):
        if used.isdisjoint(path):
            chosen.append(index)
            used.update(path)
    return chosen


def check_geometry(max_n: int = 6) -> Counter[str]:
    counts: Counter[str] = Counter()
    for n in range(3, max_n + 1):
        perms = list(permutations(range(n)))
        by_signature: dict[
            tuple[Cell, Cell, Cell],
            list[tuple[Perm, Perm, frozenset[Vertex], frozenset[Cell]]],
        ] = defaultdict(list)
        for old in perms:
            for new in perms:
                if old == new:
                    continue
                result = interior_path(old, new)
                if result is None:
                    continue
                signature, internal, path_edges = result
                by_signature[signature].append((old, new, internal, path_edges))
                counts["long_components"] += 1
                counts["interior_vertices"] += len(internal)

        for records in by_signature.values():
            paths = [record[2] for record in records]
            total_paths = len(paths)
            for petal_target in range(2, min(6, total_paths + 1)):
                chosen = maximal_disjoint(paths)
                if len(chosen) >= petal_target:
                    counts["petal_outcomes"] += 1
                    continue
                witness_union: set[Vertex] = set()
                for index in chosen:
                    witness_union.update(paths[index])
                assert len(witness_union) <= (petal_target - 1) * (2 * n - 4)
                assert witness_union
                assert all(not witness_union.isdisjoint(path) for path in paths)
                loads = Counter(
                    vertex
                    for path in paths
                    for vertex in path
                    if vertex in witness_union
                )
                assert Fraction(max(loads.values()), 1) >= Fraction(
                    total_paths, (petal_target - 1) * (2 * n - 4)
                )
                counts["hub_outcomes"] += 1

            by_parent: dict[Perm, list[frozenset[Cell]]] = defaultdict(list)
            e, r, c = canonical_cross(records[0][0], records[0][1])[:3]
            for old, new, _, path_edges in records:
                e0, r0, c0, _ = canonical_cross(old, new)
                assert (e0, r0, c0) == (e, r, c)
                _, y = r
                x, _ = c
                alpha = old.index(y)
                beta = old[x]
                a = (alpha, y)
                b = (x, beta)
                boundary_path = frozenset(path_edges - {a, b})
                assert boundary_path
                assert len(boundary_path) <= 2 * n - 5
                by_parent[old].append(boundary_path)

            for parent_paths in by_parent.values():
                for petal_target in range(2, min(6, len(parent_paths) + 1)):
                    chosen: list[int] = []
                    used_edges: set[Cell] = set()
                    for index, path_edges in enumerate(parent_paths):
                        if used_edges.isdisjoint(path_edges):
                            chosen.append(index)
                            used_edges.update(path_edges)
                    if len(chosen) >= petal_target:
                        for i in range(petal_target):
                            for j in range(i):
                                assert parent_paths[chosen[i]].isdisjoint(
                                    parent_paths[chosen[j]]
                                )
                                counts["common_parent_edge_disjoint_pairs"] += 1
                        counts["common_parent_petal_outcomes"] += 1
                    else:
                        assert used_edges
                        assert len(used_edges) <= (
                            (petal_target - 1) * (2 * n - 5)
                        )
                        assert all(
                            not used_edges.isdisjoint(path) for path in parent_paths
                        )
                        loads = Counter(
                            cell
                            for path in parent_paths
                            for cell in path
                            if cell in used_edges
                        )
                        assert Fraction(max(loads.values()), 1) >= Fraction(
                            len(parent_paths),
                            (petal_target - 1) * (2 * n - 5),
                        )
                        counts["common_parent_cell_outcomes"] += 1
        counts["signature_classes"] += len(by_signature)
    return counts


def check_ledgers() -> Counter[str]:
    counts: Counter[str] = Counter()
    for petals in range(2, 21):
        for destroyed in range(1, 21):
            for fixed in range(0, 31):
                for total_petals in range(0, 101):
                    upper = Fraction(fixed, 1) + Fraction(total_petals, petals)
                    if upper < destroyed:
                        minimum_possible = total_petals // petals
                        assert fixed + minimum_possible < destroyed
                        counts["improving_ledgers"] += 1
                    else:
                        assert (
                            fixed * 2 >= destroyed
                            or total_petals * 2 >= petals * destroyed
                        )
                        counts["failed_ledgers"] += 1
    return counts


def main() -> None:
    total = check_geometry()
    total.update(check_ledgers())
    print("AC long-cycle petal audit passed")
    for key in sorted(total):
        print(f"{key}: {total[key]}")


if __name__ == "__main__":
    main()
