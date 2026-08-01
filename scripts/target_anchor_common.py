#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
from collections import defaultdict
from typing import Any, Iterable

Edge = tuple[int, int]
LabelledEdge = tuple[int, int, int]
Matching = tuple[Edge, ...]
State = tuple[LabelledEdge, ...]


class TargetAnchorError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise TargetAnchorError(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def compatible(edges: Iterable[Edge]) -> bool:
    items = tuple(edges)
    return len({r for r, _ in items}) == len(items) and len({c for _, c in items}) == len(items)


def maximum_matching_size(edges: Iterable[Edge], rows: Iterable[int], cols: Iterable[int]) -> int:
    edge_set = set(edges)
    row_list = tuple(sorted(rows))
    col_list = tuple(sorted(cols))
    match_to_row: dict[int, int] = {}

    def augment(row: int, seen: set[int]) -> bool:
        for col in col_list:
            if col in seen or (row, col) not in edge_set:
                continue
            seen.add(col)
            if col not in match_to_row or augment(match_to_row[col], seen):
                match_to_row[col] = row
                return True
        return False

    return sum(augment(row, set()) for row in row_list)


def has_perfect_matching(edges: Iterable[Edge], rows: Iterable[int], cols: Iterable[int]) -> bool:
    rs, cs = tuple(rows), tuple(cols)
    return len(rs) == len(cs) and maximum_matching_size(edges, rs, cs) == len(rs)


def perfect_matchings(edges: Iterable[Edge], rows: Iterable[int], cols: Iterable[int]) -> list[Matching]:
    edge_set = set(edges)
    rs = tuple(sorted(rows))
    cs = tuple(sorted(cols))
    if len(rs) != len(cs):
        return []
    out = []
    for perm in itertools.permutations(cs):
        matching = tuple((rs[i], perm[i]) for i in range(len(rs)))
        if set(matching) <= edge_set:
            out.append(matching)
    return out


def essential_core(matchings: list[Matching]) -> set[Edge]:
    require(bool(matchings), "essential core requires family")
    core = set(matchings[0])
    for matching in matchings[1:]:
        core &= set(matching)
    return core


def permutation_states(n: int) -> list[State]:
    states = []
    perms = list(itertools.permutations(range(n)))
    for p0 in perms:
        cells0 = {(row, p0[row]) for row in range(n)}
        for p1 in perms:
            cells1 = {(row, p1[row]) for row in range(n)}
            if cells0.isdisjoint(cells1):
                state = tuple(sorted(
                    [(0, row, p0[row]) for row in range(n)]
                    + [(1, row, p1[row]) for row in range(n)]
                ))
                states.append(state)
    return states


def physical(state: State) -> set[Edge]:
    return {(row, column) for _, row, column in state}


def absence_runs(history: list[bool]) -> tuple[int, int]:
    runs = returns = 0
    active_absence = False
    for present in history:
        if not present and not active_absence:
            runs += 1
            active_absence = True
        elif present and active_absence:
            returns += 1
            active_absence = False
    return runs, returns


def component_edges(first: set[Edge], second: set[Edge]) -> list[set[Edge]]:
    symmetric = first ^ second
    adjacency: dict[tuple[str, int], set[Edge]] = defaultdict(set)
    for edge in symmetric:
        row, column = edge
        adjacency[("r", row)].add(edge)
        adjacency[("c", column)].add(edge)
    components = []
    seen: set[Edge] = set()
    for start in sorted(symmetric):
        if start in seen:
            continue
        stack = [start]
        component = set()
        while stack:
            edge = stack.pop()
            if edge in seen:
                continue
            seen.add(edge)
            component.add(edge)
            row, column = edge
            for vertex in (("r", row), ("c", column)):
                stack.extend(adjacency[vertex] - seen)
        components.append(component)
    return components
