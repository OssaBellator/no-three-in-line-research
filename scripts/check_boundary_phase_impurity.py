#!/usr/bin/env python3
"""Verify PP3bvy--PP3bwe on a finite labelled boundary graph."""

from __future__ import annotations

import argparse
import json
from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Edge:
    u: str
    v: str
    label: int


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    return parser.parse_args()


def require_name(value: Any, where: str) -> str:
    if not isinstance(value, str) or not value:
        raise ValueError(f"{where} must be a nonempty string")
    return value


def parse_payload(raw: Any) -> tuple[list[str], dict[str, int], list[Edge]]:
    if not isinstance(raw, dict):
        raise ValueError("top-level JSON must be an object")

    owners_raw = raw.get("owners")
    if not isinstance(owners_raw, list) or not 1 <= len(owners_raw) <= 3:
        raise ValueError("owners must be a list of one to three names")
    owners = [require_name(value, f"owners[{i}]") for i, value in enumerate(owners_raw)]
    if len(set(owners)) != len(owners):
        raise ValueError("owner names must be distinct")

    boundary_raw = raw.get("boundary_components")
    if not isinstance(boundary_raw, list):
        raise ValueError("boundary_components must be a list")
    boundary: dict[str, int] = {}
    for i, item in enumerate(boundary_raw):
        if not isinstance(item, dict):
            raise ValueError(f"boundary_components[{i}] must be an object")
        name = require_name(item.get("id"), f"boundary_components[{i}].id")
        size = item.get("size")
        if isinstance(size, bool) or not isinstance(size, int) or size <= 0:
            raise ValueError(f"boundary_components[{i}].size must be a positive integer")
        if name in boundary or name in owners:
            raise ValueError(f"duplicate vertex name {name!r}")
        boundary[name] = size

    vertices = set(owners) | set(boundary)
    edges_raw = raw.get("edges")
    if not isinstance(edges_raw, list):
        raise ValueError("edges must be a list")
    edges: list[Edge] = []
    for i, item in enumerate(edges_raw):
        if not isinstance(item, dict):
            raise ValueError(f"edges[{i}] must be an object")
        u = require_name(item.get("u"), f"edges[{i}].u")
        v = require_name(item.get("v"), f"edges[{i}].v")
        label = item.get("label")
        if u not in vertices or v not in vertices:
            raise ValueError(f"edges[{i}] contains an unknown vertex")
        if u == v:
            raise ValueError(f"edges[{i}] must not be a loop")
        if label not in (0, 1) or isinstance(label, bool):
            raise ValueError(f"edges[{i}].label must be 0 or 1")
        if u in boundary and v in boundary:
            raise ValueError("boundary--boundary edges are not allowed")
        edges.append(Edge(u, v, int(label)))

    return owners, boundary, edges


def adjacency(vertices: set[str], edges: list[Edge]) -> dict[str, list[tuple[str, int]]]:
    graph = {vertex: [] for vertex in vertices}
    for edge in edges:
        graph[edge.u].append((edge.v, edge.label))
        graph[edge.v].append((edge.u, edge.label))
    for values in graph.values():
        values.sort()
    return graph


def propagate(
    graph: dict[str, list[tuple[str, int]]]
) -> tuple[dict[str, int], list[list[str]]]:
    phase: dict[str, int] = {}
    components: list[list[str]] = []
    for root in sorted(graph):
        if root in phase:
            continue
        phase[root] = 0
        queue = deque([root])
        component: list[str] = []
        while queue:
            vertex = queue.popleft()
            component.append(vertex)
            for neighbor, label in graph[vertex]:
                required = phase[vertex] ^ label
                if neighbor in phase:
                    if phase[neighbor] != required:
                        raise ValueError(
                            f"infeasible labelled cycle through {vertex!r}--{neighbor!r}"
                        )
                    continue
                phase[neighbor] = required
                queue.append(neighbor)
        components.append(sorted(component))
    return phase, components


def shortest_conflict_path(
    graph: dict[str, list[tuple[str, int]]], start: str, goal: str
) -> tuple[list[str], int]:
    queue = deque([start])
    parent: dict[str, tuple[str, int] | None] = {start: None}
    while queue:
        vertex = queue.popleft()
        if vertex == goal:
            break
        for neighbor, label in graph[vertex]:
            if neighbor not in parent:
                parent[neighbor] = (vertex, label)
                queue.append(neighbor)
    if goal not in parent:
        raise RuntimeError("conflict vertices are unexpectedly disconnected")

    path = [goal]
    xor_label = 0
    cursor = goal
    while parent[cursor] is not None:
        previous, label = parent[cursor]  # type: ignore[misc]
        xor_label ^= label
        path.append(previous)
        cursor = previous
    path.reverse()
    return path, xor_label


def analyze(
    owners: list[str], boundary: dict[str, int], edges: list[Edge]
) -> dict[str, Any]:
    vertices = set(owners) | set(boundary)
    graph = adjacency(vertices, edges)
    phase, components = propagate(graph)
    owner_set = set(owners)
    results: list[dict[str, Any]] = []
    global_cost = 0
    global_q = 0
    global_energy_ratio = 0.0

    for index, component in enumerate(components):
        component_owners = [v for v in component if v in owner_set]
        component_boundary = [v for v in component if v in boundary]
        boundary_by_phase = {
            bit: [v for v in component_boundary if phase[v] == bit] for bit in (0, 1)
        }
        owner_by_phase = {
            bit: [v for v in component_owners if phase[v] == bit] for bit in (0, 1)
        }
        boundary_mass = {
            bit: sum(boundary[v] for v in boundary_by_phase[bit]) for bit in (0, 1)
        }
        owner_mass = {bit: len(owner_by_phase[bit]) for bit in (0, 1)}
        total_phase_mass = {
            bit: boundary_mass[bit] + owner_mass[bit] for bit in (0, 1)
        }
        cost = min(total_phase_mass.values())
        q = min(boundary_mass.values())
        total_boundary = sum(boundary_mass.values())
        energy = boundary_mass[0] * boundary_mass[1]
        energy_ratio = energy / total_boundary if total_boundary else 0.0
        total_weight = total_boundary + len(component_owners)
        one_weight = total_phase_mass[1]
        imbalance = total_weight - 2 * one_weight
        imbalance_cost = (total_weight - abs(imbalance)) // 2
        if imbalance_cost != cost:
            raise RuntimeError("imbalance formula check failed")
        if not (q <= cost <= q + len(component_owners)):
            raise RuntimeError("boundary-minority sandwich check failed")
        if not (energy_ratio <= q + 1e-12 <= 2 * energy_ratio + 1e-12 or q == 0):
            raise RuntimeError("conflict-energy bound check failed")

        witness: dict[str, Any] | None = None
        if boundary_by_phase[0] and boundary_by_phase[1]:
            start = boundary_by_phase[0][0]
            goal = boundary_by_phase[1][0]
            path, xor_label = shortest_conflict_path(graph, start, goal)
            owner_count = sum(vertex in owner_set for vertex in path)
            if xor_label != 1:
                raise RuntimeError("conflict path does not have odd label XOR")
            if len(path) - 1 > 2 * owner_count or owner_count > 3:
                raise RuntimeError("bounded conflict-witness check failed")
            witness = {
                "start": start,
                "goal": goal,
                "path": path,
                "edge_count": len(path) - 1,
                "owner_count": owner_count,
                "label_xor": xor_label,
            }

        lighter_phase = 0 if boundary_mass[0] <= boundary_mass[1] else 1
        cover_vertices = boundary_by_phase[lighter_phase]
        cover_weight = sum(boundary[v] for v in cover_vertices)
        if cover_weight != q:
            raise RuntimeError("conflict-cover check failed")

        global_cost += cost
        global_q += q
        global_energy_ratio += energy_ratio
        results.append(
            {
                "component": index,
                "vertices": component,
                "owners": component_owners,
                "boundary_phase_0": boundary_by_phase[0],
                "boundary_phase_1": boundary_by_phase[1],
                "boundary_mass_0": boundary_mass[0],
                "boundary_mass_1": boundary_mass[1],
                "boundary_minority_q": q,
                "conflict_energy": energy,
                "conflict_energy_over_boundary_mass": energy_ratio,
                "exact_minimum_recleaning_cost": cost,
                "imbalance": imbalance,
                "t_only_feasible": q == 0,
                "minimum_conflict_cover_vertices": cover_vertices,
                "minimum_conflict_cover_weight": cover_weight,
                "sample_conflict_witness": witness,
            }
        )

    if not (global_q <= global_cost <= global_q + len(owners)):
        raise RuntimeError("global boundary-minority sandwich check failed")
    if global_cost > len(owners) + 2 * global_energy_ratio + 1e-12:
        raise RuntimeError("global conflict-energy upper bound failed")

    return {
        "owner_count": len(owners),
        "component_count": len(components),
        "propagated_phase": dict(sorted(phase.items())),
        "components": results,
        "global_boundary_minority_Q": global_q,
        "global_exact_minimum_recleaning_cost": global_cost,
        "global_conflict_energy_ratio_sum": global_energy_ratio,
        "global_additive_owner_gap": global_cost - global_q,
        "all_checks_passed": True,
    }


def main() -> None:
    args = parse_args()
    try:
        raw = json.loads(args.input.read_text(encoding="utf-8"))
        owners, boundary, edges = parse_payload(raw)
        result = analyze(owners, boundary, edges)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"check failed: {exc}") from exc
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
