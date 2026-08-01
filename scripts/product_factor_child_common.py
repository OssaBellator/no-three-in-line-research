#!/usr/bin/env python3
"""Check product-rectangle, factor recursion, routing and forced-child ancestry."""
from __future__ import annotations

import copy
import hashlib
import itertools
import json
import math
from collections import Counter, defaultdict
from typing import Any, Iterable

Edge = tuple[int, int]
Matching = tuple[Edge, ...]
Triple = tuple[Edge, Edge, Edge]


class ProductFactorChildError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ProductFactorChildError(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def collinear(a: Edge, b: Edge, c: Edge) -> bool:
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])


def compatible(edges: Iterable[Edge]) -> bool:
    items = tuple(edges)
    return len({r for r, _ in items}) == len(items) and len({c for _, c in items}) == len(items)


def perfect_matchings(edges: Iterable[Edge], rows: Iterable[int], cols: Iterable[int]) -> list[Matching]:
    edge_set = set(edges)
    row_list = sorted(rows)
    col_list = sorted(cols)
    require(len(row_list) == len(col_list), "balanced host required")
    out: list[Matching] = []
    for perm in itertools.permutations(col_list):
        matching = tuple((row_list[i], perm[i]) for i in range(len(row_list)))
        if all(edge in edge_set for edge in matching):
            out.append(matching)
    return out


def essential_core(matchings: list[Matching]) -> set[Edge]:
    require(matchings, "essential core requires a matching family")
    core = set(matchings[0])
    for matching in matchings[1:]:
        core.intersection_update(matching)
    return core


def host_rows_cols(edges: Iterable[Edge]) -> tuple[set[int], set[int]]:
    edge_set = set(edges)
    return {r for r, _ in edge_set}, {c for _, c in edge_set}


def contract_host(edges: set[Edge], core: set[Edge]) -> tuple[set[Edge], set[int], set[int]]:
    core_rows = {r for r, _ in core}
    core_cols = {c for _, c in core}
    rows, cols = host_rows_cols(edges)
    return (
        {e for e in edges if e[0] not in core_rows and e[1] not in core_cols},
        rows - core_rows,
        cols - core_cols,
    )


def candidate_atoms(edges: Iterable[Edge]) -> list[Triple]:
    return [
        tuple(triple)  # type: ignore[arg-type]
        for triple in itertools.combinations(sorted(set(edges)), 3)
        if compatible(triple) and collinear(*triple)
    ]


def component_edges(M: Matching, N: Matching) -> list[set[Edge]]:
    symmetric = set(M) ^ set(N)
    adjacency: dict[tuple[str, int], list[Edge]] = defaultdict(list)
    for edge in symmetric:
        r, c = edge
        adjacency[("r", r)].append(edge)
        adjacency[("c", c)].append(edge)
    components: list[set[Edge]] = []
    seen: set[Edge] = set()
    for edge in sorted(symmetric):
        if edge in seen:
            continue
        stack = [edge]
        comp: set[Edge] = set()
        while stack:
            current = stack.pop()
            if current in seen:
                continue
            seen.add(current)
            comp.add(current)
            r, c = current
            for vertex in (("r", r), ("c", c)):
                for nxt in adjacency[vertex]:
                    if nxt not in seen:
                        stack.append(nxt)
        components.append(comp)
    return components

