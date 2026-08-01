#!/usr/bin/env python3
"""Check minimum-cost rollback faces and SCC factorization.

This checker validates CMR448--CMR461 on exhaustive side-three rollback hosts
and all side-three marked-edge cost profiles.  It installs only the canonical
optimal-face restriction and SCC factor split, not global termination.
"""
from __future__ import annotations

import hashlib
import itertools
import json
from math import ceil
from typing import Any, Iterable

Edge = tuple[int, int]
Matching = frozenset[Edge]


class OptimalFaceError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise OptimalFaceError(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


CONTRACT = {
    "schema": "prime-power-rollback-optimal-face-scc-ancestry/v1",
    "source_theorems": [f"CMR{i}" for i in range(448, 462)],
    "transition_kinds": [
        "rollback-minimum-cost-face-restriction",
        "rollback-tight-host-restriction",
        "rollback-optimal-scc-factor-split",
        "marked-ancestor-reset-optimal-face",
    ],
    "owner_effects": ["same-restoration-owner", "factor-child-owner-change"],
    "payments": [
        "minimum-restored-edge-cost",
        "zero-cycle-face-restriction",
        "strict-small-block-factorization",
        "rollback-active-level-stock",
        "scheduler-dispatch",
    ],
    "honesty_flags": {
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    },
}
EXPECTED_CONTRACT_DIGEST = "1281001711d4312dd98b8434e20dffb226b0608a893ffe5cf13f8b8e13940feb"


def all_edges(n: int) -> tuple[Edge, ...]:
    return tuple((i, j) for i in range(n) for j in range(n))


def perfect_matchings(
    rows: Iterable[int], cols: Iterable[int], edges: Iterable[Edge]
) -> tuple[Matching, ...]:
    rows = tuple(sorted(rows))
    cols = tuple(sorted(cols))
    edge_set = frozenset(edges)
    if len(rows) != len(cols):
        return ()
    if not rows:
        return (frozenset(),)
    out = []
    for perm in itertools.permutations(cols):
        matching = frozenset(zip(rows, perm))
        if matching <= edge_set:
            out.append(matching)
    return tuple(out)


def essential_edges(family: tuple[Matching, ...]) -> frozenset[Edge]:
    require(bool(family), "nonempty family required")
    common = set(family[0])
    for matching in family[1:]:
        common.intersection_update(matching)
    return frozenset(common)


def matching_cost(matching: Matching, marked: frozenset[Edge]) -> int:
    return len(matching & marked)


def transitive_reachability(n: int, arcs: set[tuple[int, int]]) -> list[list[bool]]:
    reach = [[False] * n for _ in range(n)]
    for i in range(n):
        reach[i][i] = True
    for i, j in arcs:
        reach[i][j] = True
    for k in range(n):
        for i in range(n):
            if reach[i][k]:
                for j in range(n):
                    reach[i][j] = reach[i][j] or reach[k][j]
    return reach


def strongly_connected_components(n: int, arcs: set[tuple[int, int]]) -> tuple[tuple[int, ...], ...]:
    reach = transitive_reachability(n, arcs)
    unseen = set(range(n))
    components = []
    while unseen:
        first = min(unseen)
        component = tuple(sorted(j for j in unseen if reach[first][j] and reach[j][first]))
        components.append(component)
        unseen.difference_update(component)
    return tuple(components)


def analyse_cost_face(
    n: int, allowed_edges: frozenset[Edge], marked: frozenset[Edge]
) -> dict[str, Any]:
    family = perfect_matchings(range(n), range(n), allowed_edges)
    require(family, "cost face requires a nonempty matching family")
    costs = {matching: matching_cost(matching, marked) for matching in family}
    optimum = min(costs.values())
    opt_family = tuple(sorted(
        (matching for matching in family if costs[matching] == optimum),
        key=lambda matching: tuple(sorted(matching)),
    ))
    base = opt_family[0]
    base_target = {row: col for row, col in base}
    target_to_index = {col: row for row, col in base}
    arcs: dict[tuple[int, int], tuple[Edge, int]] = {}
    for edge in sorted(allowed_edges - base):
        row, col = edge
        k = target_to_index[col]
        weight = (edge in marked) - ((k, base_target[k]) in marked)
        arcs[(row, k)] = (edge, int(weight))

    phi = [0] * n
    for _ in range(n - 1):
        changed = False
        for (j, k), (_, weight) in sorted(arcs.items()):
            value = phi[j] + weight
            if value < phi[k]:
                phi[k] = value
                changed = True
        if not changed:
            break
    for (j, k), (_, weight) in arcs.items():
        require(phi[k] <= phi[j] + weight, "negative alternating cycle detected")

    tight_arcs: set[tuple[int, int]] = set()
    tight_edges = set(base)
    for (j, k), (edge, weight) in arcs.items():
        reduced = weight + phi[j] - phi[k]
        require(reduced >= 0, "negative reduced rollback weight")
        if reduced == 0:
            tight_arcs.add((j, k))
            tight_edges.add(edge)
    tight_family = perfect_matchings(range(n), range(n), tight_edges)
    require(frozenset(tight_family) == frozenset(opt_family), "tight host is not exact optimum face")

    components = strongly_connected_components(n, tight_arcs)
    component_of = {
        vertex: index
        for index, component in enumerate(components)
        for vertex in component
    }
    optimal_core = set(base)
    for (j, k) in tight_arcs:
        if component_of[j] == component_of[k]:
            optimal_core.add(arcs[(j, k)][0])
    union_optimum = set().union(*opt_family)
    require(optimal_core == union_optimum, "optimal-allowed core mismatch")
    core_family = perfect_matchings(range(n), range(n), optimal_core)
    require(frozenset(core_family) == frozenset(opt_family), "optimal core family mismatch")

    local_families = []
    local_costs = []
    for component in components:
        rows = frozenset(component)
        cols = frozenset(base_target[row] for row in component)
        local_edges = frozenset(
            edge for edge in optimal_core if edge[0] in rows and edge[1] in cols
        )
        local_family = perfect_matchings(rows, cols, local_edges)
        require(local_family, "empty SCC factor")
        base_cost = sum((row, base_target[row]) in marked for row in component)
        require(
            all(matching_cost(matching, marked) == base_cost for matching in local_family),
            "local rollback cost is not constant",
        )
        local_families.append(local_family)
        local_costs.append(base_cost)

    product = {frozenset()}
    for local_family in local_families:
        product = {left | right for left in product for right in local_family}
    require(product == set(opt_family), "SCC product does not equal optimum family")
    require(sum(local_costs) == optimum, "rollback cost not additive across SCCs")

    require(all(-optimum <= value <= 0 for value in phi), "rollback-sensitive potential range failed")
    active_components = [
        component for component, cost in zip(components, local_costs) if cost > 0
    ]
    require(len(active_components) <= optimum, "too many rollback-active components")
    active_vertices = sum(len(component) for component in active_components)
    level_cells: dict[tuple[int, int], int] = {}
    for index, component in enumerate(components):
        if local_costs[index] > 0:
            for vertex in component:
                key = (index, phi[vertex])
                level_cells[key] = level_cells.get(key, 0) + 1
    if active_vertices:
        denominator = optimum + len(active_components)
        require(denominator > 0, "invalid active-level denominator")
        require(
            max(level_cells.values()) >= ceil(active_vertices / denominator),
            "active same-level concentration failed",
        )

    q = 2
    rollback_free_large = any(
        local_costs[index] == 0 and len(component) >= q
        for index, component in enumerate(components)
    )
    small_factorization = all(len(component) < q for component in components)
    active_concentration = active_vertices >= q
    require(
        rollback_free_large or small_factorization or active_concentration,
        "three-way rollback threshold endpoint failed",
    )
    endpoint = (
        "large-rollback-free-block"
        if rollback_free_large
        else "strict-small-block-factorization"
        if small_factorization
        else "rollback-active-level-concentration"
    )

    record = {
        "n": n,
        "allowed_edges": sorted(allowed_edges),
        "marked_edges": sorted(marked),
        "minimum_cost": optimum,
        "base_matching": sorted(base),
        "optimum_family": [sorted(matching) for matching in opt_family],
        "potential": phi,
        "tight_edges": sorted(tight_edges),
        "tight_arcs": sorted(tight_arcs),
        "components": [list(component) for component in components],
        "optimal_core": sorted(optimal_core),
        "local_costs": local_costs,
        "endpoint_q2": endpoint,
    }
    record["seal"] = digest({k: record[k] for k in record if k != "seal"})
    return record


def make_rollback_record(n: int, final_host: frozenset[Edge], edge: Edge) -> dict[str, Any]:
    final_family = perfect_matchings(range(n), range(n), final_host)
    require(final_family and edge in essential_edges(final_family), "final essential edge required")
    ancestor_avoiding = frozenset(all_edges(n)) - {edge}
    marked = frozenset(all_edges(n)) - final_host
    record = analyse_cost_face(n, ancestor_avoiding, marked)
    require(record["minimum_cost"] >= 1, "rollback optimum must use a restored edge")
    record["final_host"] = sorted(final_host)
    record["essential_edge"] = edge
    record["seal"] = digest({k: record[k] for k in record if k != "seal"})
    return record


def validate_rollback_record(record: dict[str, Any]) -> None:
    rebuilt = make_rollback_record(
        int(record["n"]),
        frozenset(tuple(edge) for edge in record["final_host"]),
        tuple(record["essential_edge"]),
    )
    require(record == rebuilt, "rollback optimal-face record mismatch")


def mutation_audit(valid: dict[str, Any]) -> int:
    replacements = [
        ("minimum_cost", -1),
        ("base_matching", []),
        ("optimum_family", []),
        ("potential", [99, 99, 99]),
        ("tight_edges", []),
        ("components", []),
        ("optimal_core", []),
        ("local_costs", []),
        ("endpoint_q2", "free"),
        ("seal", "0" * 64),
    ]
    rejected = 0
    for field, value in replacements:
        bad = json.loads(json.dumps(valid))
        bad[field] = value
        try:
            validate_rollback_record(bad)
        except Exception:
            rejected += 1
    require(rejected == len(replacements), "not every optimal-face corruption was rejected")
    return rejected


def finite_regression() -> dict[str, Any]:
    n = 3
    universe = all_edges(n)
    host_count = 0
    essential_pairs = 0
    optimum_states = 0
    tight_edge_incidences = 0
    scc_blocks = 0
    active_blocks = 0
    endpoint_counts: dict[str, int] = {}
    minimum_cost_histogram: dict[int, int] = {}
    sample = None

    for mask in range(1 << len(universe)):
        host = frozenset(universe[i] for i in range(len(universe)) if mask & (1 << i))
        family = perfect_matchings(range(n), range(n), host)
        if not family:
            continue
        host_count += 1
        for edge in sorted(essential_edges(family)):
            record = make_rollback_record(n, host, edge)
            validate_rollback_record(record)
            essential_pairs += 1
            optimum_states += len(record["optimum_family"])
            tight_edge_incidences += len(record["tight_edges"])
            scc_blocks += len(record["components"])
            active_blocks += sum(cost > 0 for cost in record["local_costs"])
            endpoint = record["endpoint_q2"]
            endpoint_counts[endpoint] = endpoint_counts.get(endpoint, 0) + 1
            cost = record["minimum_cost"]
            minimum_cost_histogram[cost] = minimum_cost_histogram.get(cost, 0) + 1
            if sample is None and len(record["optimum_family"]) > 1:
                sample = record

    marked_profiles = 0
    complete = frozenset(universe)
    for mask in range(1 << len(universe)):
        marked = frozenset(universe[i] for i in range(len(universe)) if mask & (1 << i))
        analyse_cost_face(n, complete, marked)
        marked_profiles += 1

    require(sample is not None, "no flexible optimum-face sample found")
    rejected = mutation_audit(sample)
    return {
        "side_three_matchable_final_hosts": host_count,
        "essential_rollback_pairs": essential_pairs,
        "minimum_cost_histogram": minimum_cost_histogram,
        "minimum_rollback_state_incidences": optimum_states,
        "tight_edge_incidences": tight_edge_incidences,
        "scc_factor_blocks": scc_blocks,
        "rollback_active_blocks": active_blocks,
        "threshold_endpoint_counts": endpoint_counts,
        "marked_ancestor_reset_profiles": marked_profiles,
        "rejected_corruptions": rejected,
    }


def main() -> None:
    contract_digest = digest(CONTRACT)
    require(contract_digest == EXPECTED_CONTRACT_DIGEST, "contract digest mismatch")
    report = {
        "contract_digest": contract_digest,
        "census": finite_regression(),
        "rollback_minimum_cost_face_ancestry_proved": 1,
        "rollback_tight_host_exact": 1,
        "rollback_optimal_scc_factorization_exact": 1,
        "marked_ancestor_reset_optimal_face_exact": 1,
        "all_owner_operations_proved": 0,
        "all_scheduler_operations_proved": 0,
        "all_restoration_operations_proved": 0,
        "all_construction_ancestry_proved": 0,
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    }
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
